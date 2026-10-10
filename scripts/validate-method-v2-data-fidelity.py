#!/usr/bin/env python3
"""
Smart Imports — Method v2 Data Fidelity Preflight v2.2

Purpose
-------
Validate semantic/data-fidelity invariants that Matrix Validator cannot infer.

Marketplace contract from governance v1.0.3:
- raw capture remains immutable;
- current verification is a separate layer;
- every active marketplace verification carries sales, ARS price, USD conversion,
  FX value/date/basis and exact source binding;
- historical sources that cannot be recovered are explicitly HISTORICAL_ONLY;
- new marketplace rows created after the governance gate must carry ARS + USD
  in the core row as well as a verification record;
- seller/store sales never substitute product-level sales.

No third-party dependencies. Reads XLSX via ZIP/XML only.
"""

from __future__ import annotations
import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
NS_REL_OFFICE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_REL_PACKAGE = "http://schemas.openxmlformats.org/package/2006/relationships"

SALES_RE = re.compile(r"^(?:No informadas|\+\d+(?:\s*mil)?|\d+)$", re.IGNORECASE)
ALLOWED_PUB_TYPES = {"DIRECT", "DIRECT_CONDITIONED", "ADJACENT", "SUBSTITUTE"}
ALLOWED_STATUS = {"ACTIVE", "HISTORICAL_ONLY"}
ALLOWED_BINDING = {"EXACT_SOURCE", "EXACT_MODEL_CURRENT", "SOURCE_UNAVAILABLE"}
GOVERNANCE_EFFECTIVE_EXCEL_DATE = 46305  # 2026-10-10
USD_TOLERANCE = 0.02

def col_num(ref: str) -> int:
    m = re.match(r"([A-Z]+)", ref)
    if not m:
        raise ValueError(f"Referencia de celda inválida: {ref}")
    n = 0
    for ch in m.group(1):
        n = n * 26 + ord(ch) - 64
    return n

def shared_strings(z):
    try:
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    out = []
    for si in root.findall(f"{{{NS_MAIN}}}si"):
        out.append("".join(t.text or "" for t in si.iter(f"{{{NS_MAIN}}}t")))
    return out

def cell_value(cell, shared):
    t = cell.attrib.get("t")
    if t == "inlineStr":
        return "".join(x.text or "" for x in cell.iter(f"{{{NS_MAIN}}}t"))
    v = cell.find(f"{{{NS_MAIN}}}v")
    if v is None:
        return None
    if t == "s":
        return shared[int(v.text)]
    return v.text

def load_sheet_rows(path: Path, sheet_name: str):
    with zipfile.ZipFile(path) as z:
        shared = shared_strings(z)
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        sheets = wb.find(f"{{{NS_MAIN}}}sheets")
        if sheets is None:
            raise RuntimeError("workbook.xml no contiene sheets")

        rid = None
        for s in sheets:
            if s.attrib.get("name") == sheet_name:
                rid = s.attrib[f"{{{NS_REL_OFFICE}}}id"]
                break
        if rid is None:
            raise RuntimeError(f'No existe la hoja "{sheet_name}"')

        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        target = None
        for rel in rels.findall(f"{{{NS_REL_PACKAGE}}}Relationship"):
            if rel.attrib["Id"] == rid:
                target = rel.attrib["Target"].lstrip("/")
                if not target.startswith("xl/"):
                    target = "xl/" + target
                break
        if target is None:
            raise RuntimeError(f"No se pudo resolver la hoja {sheet_name}")

        root = ET.fromstring(z.read(target))
        sheet_data = root.find(f"{{{NS_MAIN}}}sheetData")
        if sheet_data is None:
            return []

        rows = []
        for row in sheet_data:
            vals = {}
            for c in row.findall(f"{{{NS_MAIN}}}c"):
                vals[col_num(c.attrib["r"])] = cell_value(c, shared)
            rows.append((int(row.attrib["r"]), vals))
        return rows

def table(path: Path, sheet_name: str):
    rows = load_sheet_rows(path, sheet_name)
    if not rows:
        return []
    _, header_vals = rows[0]
    headers = {str(v).strip(): c for c, v in header_vals.items() if v is not None}
    result = []
    for row_num, vals in rows[1:]:
        result.append((row_num, {h: vals.get(c) for h, c in headers.items()}))
    return result

def clean(v):
    return (v or "").strip()

def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None

def finding(code, sheet, row, record_id, field, actual, expected):
    return {
        "code": code, "sheet": sheet, "row": row, "recordId": record_id,
        "field": field, "actual": actual, "expected": expected
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("xlsx")
    ap.add_argument("--niche", required=True)
    ap.add_argument("--phase", type=int, required=True, choices=range(0, 14))
    args = ap.parse_args()

    path = Path(args.xlsx)
    if not path.is_file():
        print(f"ERROR: no existe {path}", file=sys.stderr)
        return 2

    errors = []
    try:
        pubs = table(path, "Publicaciones ML")
        pbs = table(path, "Productos Base")
    except Exception as e:
        print(f"ERROR TÉCNICO leyendo XLSX: {e}", file=sys.stderr)
        return 2

    # `Verificaciones ML` is optional before F3, but mandatory from F3 onward.
    # This keeps F0-F2 executable while making marketplace economics enforceable
    # as soon as marketplace evidence enters the Method v2 pipeline.
    try:
        verifs = table(path, "Verificaciones ML")
        verification_sheet_present = True
    except RuntimeError as e:
        if 'No existe la hoja "Verificaciones ML"' in str(e):
            verifs = []
            verification_sheet_present = False
        else:
            print(f"ERROR TÉCNICO leyendo XLSX: {e}", file=sys.stderr)
            return 2
    except Exception as e:
        print(f"ERROR TÉCNICO leyendo XLSX: {e}", file=sys.stderr)
        return 2

    candidate_pubs = [(r,x) for r,x in pubs if clean(x.get("Nicho")) == args.niche]
    candidate_pbs = [(r,x) for r,x in pbs if clean(x.get("Nicho")) == args.niche]
    candidate_verifs = [(r,x) for r,x in verifs if clean(x.get("Nicho")) == args.niche]

    if args.phase >= 3 and not candidate_pubs:
        errors.append(finding("DF-ML-000","Publicaciones ML",None,None,"Nicho",None,
                              "Al menos una publicación del candidato desde F3"))

    if args.phase >= 3 and not verification_sheet_present:
        errors.append(finding("DF-MLV-009","Verificaciones ML",None,None,"Hoja",
                              None,"La hoja Verificaciones ML es obligatoria desde F3"))

    # Append-only verification ledger.
    # Verificación ID identifies an event; ML ID may repeat over time.
    ledger_by_ml = {}
    seen_verification_ids = set()

    for row, lrec in candidate_verifs:
        vid = clean(lrec.get("Verificación ID"))
        mid = clean(lrec.get("ML ID"))
        vdate = num(lrec.get("Fecha Verificación"))

        if not vid:
            errors.append(finding("DF-MLV-000","Verificaciones ML",row,mid or None,
                                  "Verificación ID",None,"Verificación ID obligatorio"))
        elif vid in seen_verification_ids:
            errors.append(finding("DF-MLV-001","Verificaciones ML",row,mid or None,
                                  "Verificación ID",vid,"Verificación ID único"))
        else:
            seen_verification_ids.add(vid)

        if not mid:
            errors.append(finding("DF-MLV-010","Verificaciones ML",row,vid or None,
                                  "ML ID",None,"ML ID obligatorio"))
            continue

        if vdate is None or vdate <= 0:
            errors.append(finding("DF-MLV-011","Verificaciones ML",row,mid,
                                  "Fecha Verificación",lrec.get("Fecha Verificación"),
                                  "Fecha Verificación válida"))
            continue

        status_l = clean(lrec.get("Estado Evidencia ML"))
        binding_l = clean(lrec.get("Binding Verificación ML"))
        sales_l = clean(lrec.get("Ventas visibles"))
        url_l = clean(lrec.get("Fuente Verificación ML"))
        ars_l = lrec.get("Precio ARS")
        usd_l = lrec.get("Precio USD")
        fx_l = num(lrec.get("FX ARS/USD"))

        required_ledger = [
            "Producto","Estado Evidencia ML","Binding Verificación ML",
            "Precio ARS","Precio USD","Ventas visibles","FX ARS/USD","FX Fecha",
            "FX Fuente / Basis","Fuente Verificación ML","Observaciones"
        ]
        missing_ledger = [f for f in required_ledger if clean(lrec.get(f)) == ""]
        if missing_ledger:
            errors.append(finding("DF-MLV-012","Verificaciones ML",row,mid,
                                  "Ledger completeness",missing_ledger,
                                  "Todos los campos obligatorios de verificación completos"))

        if status_l not in ALLOWED_STATUS:
            errors.append(finding("DF-MLV-013","Verificaciones ML",row,mid,
                                  "Estado Evidencia ML",status_l or None,
                                  "ACTIVE | HISTORICAL_ONLY"))
        if binding_l not in ALLOWED_BINDING:
            errors.append(finding("DF-MLV-014","Verificaciones ML",row,mid,
                                  "Binding Verificación ML",binding_l or None,
                                  "EXACT_SOURCE | EXACT_MODEL_CURRENT | SOURCE_UNAVAILABLE"))
        if not SALES_RE.fullmatch(sales_l):
            errors.append(finding("DF-MLV-015","Verificaciones ML",row,mid,
                                  "Ventas visibles",sales_l or None,
                                  "Contador cuantificado o 'No informadas'"))
        if not url_l.startswith("http"):
            errors.append(finding("DF-MLV-016","Verificaciones ML",row,mid,
                                  "Fuente Verificación ML",url_l or None,"URL obligatoria"))
        if fx_l is None or fx_l <= 0:
            errors.append(finding("DF-MLV-017","Verificaciones ML",row,mid,
                                  "FX ARS/USD",lrec.get("FX ARS/USD"),"FX numérico > 0"))
        if not clean(lrec.get("FX Fecha")):
            errors.append(finding("DF-MLV-018","Verificaciones ML",row,mid,
                                  "FX Fecha",None,"FX Fecha obligatoria"))
        if not clean(lrec.get("FX Fuente / Basis")):
            errors.append(finding("DF-MLV-019","Verificaciones ML",row,mid,
                                  "FX Fuente / Basis",None,"FX Fuente / Basis obligatoria"))

        if status_l == "ACTIVE":
            ars_num = num(ars_l)
            usd_num = num(usd_l)
            if ars_num is None or ars_num <= 0:
                errors.append(finding("DF-MLV-020","Verificaciones ML",row,mid,
                                      "Precio ARS",ars_l,"Precio ARS numérico > 0"))
            if usd_num is None or usd_num <= 0:
                errors.append(finding("DF-MLV-021","Verificaciones ML",row,mid,
                                      "Precio USD",usd_l,"Precio USD numérico > 0"))
            if binding_l == "SOURCE_UNAVAILABLE":
                errors.append(finding("DF-MLV-022","Verificaciones ML",row,mid,
                                      "Binding Verificación ML",binding_l,
                                      "ACTIVE no puede usar SOURCE_UNAVAILABLE"))
            if ars_num and usd_num and fx_l:
                expected = round(ars_num / fx_l, 2)
                if abs(usd_num - expected) > USD_TOLERANCE:
                    errors.append(finding("DF-MLV-023","Verificaciones ML",row,mid,
                                          "Precio USD",usd_num,
                                          f"ROUND(Precio ARS / FX, 2) = {expected}"))
        elif status_l == "HISTORICAL_ONLY":
            if binding_l != "SOURCE_UNAVAILABLE":
                errors.append(finding("DF-MLV-024","Verificaciones ML",row,mid,
                                      "Binding Verificación ML",binding_l,
                                      "HISTORICAL_ONLY requiere SOURCE_UNAVAILABLE"))
            if clean(ars_l) != "No verificable" or clean(usd_l) != "No verificable":
                errors.append(finding("DF-MLV-025","Verificaciones ML",row,mid,
                                      "Precio",f"{ars_l} / {usd_l}",
                                      "'No verificable' para fuente histórica no recuperable"))
            if sales_l.lower() != "no informadas":
                errors.append(finding("DF-MLV-026","Verificaciones ML",row,mid,
                                      "Ventas visibles",sales_l,
                                      "HISTORICAL_ONLY usa 'No informadas'"))

        ledger_by_ml.setdefault(mid, []).append((row, lrec, vdate))

    for row, rec in candidate_pubs:
        mid = clean(rec.get("ML ID"))
        sales = clean(rec.get("Ventas visibles"))
        link = clean(rec.get("Link"))
        source_id = clean(rec.get("Fuente Global ID"))
        pub_type = clean(rec.get("Tipo de Publicación"))

        if args.phase >= 3:
            if not sales or not SALES_RE.fullmatch(sales):
                errors.append(finding("DF-ML-001","Publicaciones ML",row,mid,"Ventas visibles",
                                      sales or None,
                                      "Dato raw cuantificado (+1000, +500, +5 mil, 2...) o 'No informadas'"))
            if not link.startswith("http"):
                errors.append(finding("DF-ML-002","Publicaciones ML",row,mid,"Link",
                                      link or None,"URL fuente obligatoria"))
            if not source_id:
                errors.append(finding("DF-ML-003","Publicaciones ML",row,mid,"Fuente Global ID",
                                      None,"Fuente global obligatoria"))
            if pub_type not in ALLOWED_PUB_TYPES:
                errors.append(finding("DF-ML-004","Publicaciones ML",row,mid,"Tipo de Publicación",
                                      pub_type or None,
                                      "DIRECT | DIRECT_CONDITIONED | ADJACENT | SUBSTITUTE"))

            # Marketplace verification layer is mandatory in the current contract.
            required = [
                "Fecha Verificación ML","Estado Evidencia ML","Binding Verificación ML",
                "Precio ARS Verificado","Precio USD Verificado","Ventas visibles Verificadas",
                "FX ARS/USD","FX Fecha","FX Fuente / Basis","Fuente Verificación ML",
                "Observaciones Verificación ML"
            ]
            missing = [f for f in required if clean(rec.get(f)) == ""]
            if missing:
                errors.append(finding("DF-MLV-002","Publicaciones ML",row,mid,
                                      "Marketplace verification layer",missing,
                                      "Todos los campos de verificación obligatorios completos"))

            status = clean(rec.get("Estado Evidencia ML"))
            binding = clean(rec.get("Binding Verificación ML"))
            vsales = clean(rec.get("Ventas visibles Verificadas"))
            vurl = clean(rec.get("Fuente Verificación ML"))
            vars_ = rec.get("Precio ARS Verificado")
            vusd = rec.get("Precio USD Verificado")
            fx = num(rec.get("FX ARS/USD"))

            if status not in ALLOWED_STATUS:
                errors.append(finding("DF-MLV-003","Publicaciones ML",row,mid,"Estado Evidencia ML",
                                      status or None,"ACTIVE | HISTORICAL_ONLY"))
            if binding not in ALLOWED_BINDING:
                errors.append(finding("DF-MLV-004","Publicaciones ML",row,mid,"Binding Verificación ML",
                                      binding or None,
                                      "EXACT_SOURCE | EXACT_MODEL_CURRENT | SOURCE_UNAVAILABLE"))
            if not SALES_RE.fullmatch(vsales):
                errors.append(finding("DF-MLV-005","Publicaciones ML",row,mid,
                                      "Ventas visibles Verificadas",vsales or None,
                                      "Contador cuantificado o 'No informadas'"))
            if not vurl.startswith("http"):
                errors.append(finding("DF-MLV-006","Publicaciones ML",row,mid,
                                      "Fuente Verificación ML",vurl or None,"URL obligatoria"))
            if fx is None or fx <= 0:
                errors.append(finding("DF-FX-001","Publicaciones ML",row,mid,"FX ARS/USD",
                                      rec.get("FX ARS/USD"),"FX numérico > 0"))
            if not clean(rec.get("FX Fecha")):
                errors.append(finding("DF-FX-002","Publicaciones ML",row,mid,"FX Fecha",
                                      None,"Fecha/baseline FX obligatoria"))
            if not clean(rec.get("FX Fuente / Basis")):
                errors.append(finding("DF-FX-003","Publicaciones ML",row,mid,"FX Fuente / Basis",
                                      None,"Fuente o basis explícita obligatoria"))

            if status == "ACTIVE":
                ars = num(vars_)
                usd = num(vusd)
                if ars is None or ars <= 0:
                    errors.append(finding("DF-PRICE-001","Publicaciones ML",row,mid,
                                          "Precio ARS Verificado",vars_,"Precio ARS numérico > 0"))
                if usd is None or usd <= 0:
                    errors.append(finding("DF-PRICE-002","Publicaciones ML",row,mid,
                                          "Precio USD Verificado",vusd,"Precio USD numérico > 0"))
                if binding == "SOURCE_UNAVAILABLE":
                    errors.append(finding("DF-PRICE-003","Publicaciones ML",row,mid,
                                          "Binding Verificación ML",binding,
                                          "ACTIVE no puede usar SOURCE_UNAVAILABLE"))
                if ars and usd and fx:
                    expected = round(ars / fx, 2)
                    if abs(usd - expected) > USD_TOLERANCE:
                        errors.append(finding("DF-FX-004","Publicaciones ML",row,mid,
                                              "Precio USD Verificado",usd,
                                              f"ROUND(Precio ARS Verificado / FX, 2) = {expected}"))
            elif status == "HISTORICAL_ONLY":
                if binding != "SOURCE_UNAVAILABLE":
                    errors.append(finding("DF-HIST-001","Publicaciones ML",row,mid,
                                          "Binding Verificación ML",binding,
                                          "HISTORICAL_ONLY requiere SOURCE_UNAVAILABLE"))
                if clean(str(vars_)) != "No verificable" or clean(str(vusd)) != "No verificable":
                    errors.append(finding("DF-HIST-002","Publicaciones ML",row,mid,
                                          "Precio verificado",f"{vars_} / {vusd}",
                                          "'No verificable' cuando no existe source binding exacto"))
                if vsales.lower() != "no informadas":
                    errors.append(finding("DF-HIST-003","Publicaciones ML",row,mid,
                                          "Ventas visibles Verificadas",vsales,
                                          "HISTORICAL_ONLY usa 'No informadas'"))

            # Append-only ledger: every publication needs at least one event, and
            # the current summary must reflect the most recent verification date.
            entries = ledger_by_ml.get(mid, [])
            if not entries:
                errors.append(finding("DF-MLV-007","Verificaciones ML",None,mid,"ML ID",None,
                                      "Al menos una verificación ledger por publicación"))
            else:
                latest_date = max(item[2] for item in entries)
                summary_date = num(rec.get("Fecha Verificación ML"))

                if summary_date is None or abs(summary_date - latest_date) > 1e-9:
                    errors.append(finding("DF-MLV-027","Publicaciones ML",row,mid,
                                          "Fecha Verificación ML",
                                          rec.get("Fecha Verificación ML"),
                                          f"Debe coincidir con la fecha ledger más reciente: {latest_date}"))
                else:
                    latest_entries = [item for item in entries if abs(item[2] - latest_date) <= 1e-9]

                    def same_value(a, b, tolerance=USD_TOLERANCE):
                        na, nb = num(a), num(b)
                        if na is not None and nb is not None:
                            return abs(na - nb) <= tolerance
                        return clean(a) == clean(b)

                    mapping = [
                        ("Estado Evidencia ML", "Estado Evidencia ML"),
                        ("Binding Verificación ML", "Binding Verificación ML"),
                        ("Precio ARS Verificado", "Precio ARS"),
                        ("Precio USD Verificado", "Precio USD"),
                        ("Ventas visibles Verificadas", "Ventas visibles"),
                        ("FX ARS/USD", "FX ARS/USD"),
                        ("FX Fecha", "FX Fecha"),
                        ("FX Fuente / Basis", "FX Fuente / Basis"),
                        ("Fuente Verificación ML", "Fuente Verificación ML"),
                        ("Observaciones Verificación ML", "Observaciones"),
                    ]

                    matches_latest = any(
                        all(same_value(rec.get(pub_field), lrec.get(ledger_field))
                            for pub_field, ledger_field in mapping)
                        for _, lrec, _ in latest_entries
                    )
                    if not matches_latest:
                        errors.append(finding("DF-MLV-028","Publicaciones ML",row,mid,
                                              "Marketplace verification layer",
                                              "No coincide con ledger",
                                              "Debe coincidir con una verificación ledger de la fecha más reciente"))

            # New captures after governance must be complete in the core row too.
            capture_date = num(rec.get("Fecha Relevamiento"))
            if capture_date is not None and capture_date >= GOVERNANCE_EFFECTIVE_EXCEL_DATE:
                core_ars = num(rec.get("Precio ARS"))
                core_usd = num(rec.get("Precio USD"))
                if core_ars is None or core_ars <= 0:
                    errors.append(finding("DF-PRICE-004","Publicaciones ML",row,mid,"Precio ARS",
                                          rec.get("Precio ARS"),
                                          "Nueva captura marketplace: Precio ARS obligatorio"))
                if core_usd is None or core_usd <= 0:
                    errors.append(finding("DF-PRICE-005","Publicaciones ML",row,mid,"Precio USD",
                                          rec.get("Precio USD"),
                                          "Nueva captura marketplace: Precio USD obligatorio"))
                if core_ars and core_usd and fx:
                    expected = round(core_ars/fx,2)
                    if abs(core_usd-expected)>USD_TOLERANCE:
                        errors.append(finding("DF-FX-005","Publicaciones ML",row,mid,"Precio USD",
                                              core_usd,f"ROUND(Precio ARS / FX, 2) = {expected}"))

        if args.phase < 6:
            pb = clean(rec.get("Producto Base"))
            pbid = clean(rec.get("ID Producto Base"))
            if pb or pbid:
                errors.append(finding("DF-PB-001","Publicaciones ML",row,mid,"Product Base",
                                      f"{pbid} / {pb}".strip(" /"),
                                      "Antes de F6 no puede existir Product Base"))

    # No orphan ledger rows for this niche.
    pub_ids = {clean(r.get("ML ID")) for _,r in candidate_pubs}
    for row, rec in candidate_verifs:
        mid = clean(rec.get("ML ID"))
        if mid and mid not in pub_ids:
            errors.append(finding("DF-MLV-008","Verificaciones ML",row,mid,"ML ID",mid,
                                  "Ledger no puede apuntar a una publicación inexistente"))

    if args.phase < 6:
        for row, rec in candidate_pbs:
            pbid = clean(rec.get("ID Producto Base"))
            if pbid:
                errors.append(finding("DF-PB-002","Productos Base",row,pbid,"ID Producto Base",
                                      pbid,"No debe existir Product Base antes de F6"))

    print("============================================================")
    print("SMART IMPORTS — METHOD V2 DATA FIDELITY PREFLIGHT v2.2")
    print("============================================================")
    print(f"File: {path}")
    print(f"Niche: {args.niche}")
    print(f"Phase: F{args.phase}")
    print(f"Publications audited: {len(candidate_pubs)}")
    print(f"Verification ledger rows: {len(candidate_verifs)}")
    print(f"Product Bases found for scope: {len(candidate_pbs)}")
    print()

    if errors:
        print(f"RESULT: FAIL ({len(errors)} error(s))")
        for e in errors:
            print(
                f"- {e['code']} | {e['sheet']} row {e['row']} | "
                f"{e['recordId']} | {e['field']} | actual={e['actual']!r} | "
                f"expected={e['expected']}"
            )
        return 1

    print("RESULT: PASS")
    print("Marketplace sales + ARS/USD + FX invariants satisfied.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
