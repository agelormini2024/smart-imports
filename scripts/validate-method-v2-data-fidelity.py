#!/usr/bin/env python3
"""
Smart Imports — Method v2 Data Fidelity Preflight

Validates semantic/data-fidelity invariants that Matrix Validator cannot infer.
Run BEFORE Matrix Validator for every Method v2 matrix materialization.

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

def col_num(ref: str) -> int:
    m = re.match(r"([A-Z]+)", ref)
    if not m:
        raise ValueError(f"Referencia de celda inválida: {ref}")
    letters = m.group(1)
    n = 0
    for ch in letters:
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

        rid = None
        sheets = wb.find(f"{{{NS_MAIN}}}sheets")
        if sheets is None:
            raise RuntimeError("workbook.xml no contiene sheets")

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

def finding(code, sheet, row, record_id, field, actual, expected):
    return {
        "code": code,
        "sheet": sheet,
        "row": row,
        "recordId": record_id,
        "field": field,
        "actual": actual,
        "expected": expected,
    }

def clean(v):
    return (v or "").strip()

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
        publication_rows = table(path, "Publicaciones ML")
        product_base_rows = table(path, "Productos Base")
    except Exception as e:
        print(f"ERROR TÉCNICO leyendo XLSX: {e}", file=sys.stderr)
        return 2

    candidate_publications = [
        (r, x) for r, x in publication_rows if clean(x.get("Nicho")) == args.niche
    ]
    candidate_product_bases = [
        (r, x) for r, x in product_base_rows if clean(x.get("Nicho")) == args.niche
    ]

    if args.phase >= 3 and not candidate_publications:
        errors.append(finding(
            "DF-ML-000", "Publicaciones ML", None, None, "Nicho",
            None, "Al menos una publicación del candidato desde F3"
        ))

    for row, rec in candidate_publications:
        rid = rec.get("ML ID")
        sales = clean(rec.get("Ventas visibles"))
        link = clean(rec.get("Link"))
        source_id = clean(rec.get("Fuente Global ID"))
        pub_type = clean(rec.get("Tipo de Publicación"))

        if args.phase >= 3:
            if not sales or not SALES_RE.fullmatch(sales):
                errors.append(finding(
                    "DF-ML-001", "Publicaciones ML", row, rid, "Ventas visibles",
                    sales or None,
                    "Dato crudo cuantificado (+1000, +500, +5 mil, 2...) o 'No informadas'; nunca interpretación"
                ))

            if not link.startswith("http"):
                errors.append(finding(
                    "DF-ML-002", "Publicaciones ML", row, rid, "Link",
                    link or None, "URL fuente obligatoria"
                ))

            if not source_id:
                errors.append(finding(
                    "DF-ML-003", "Publicaciones ML", row, rid, "Fuente Global ID",
                    None, "Fuente global obligatoria"
                ))

            if pub_type not in ALLOWED_PUB_TYPES:
                errors.append(finding(
                    "DF-ML-004", "Publicaciones ML", row, rid, "Tipo de Publicación",
                    pub_type or None,
                    "DIRECT | DIRECT_CONDITIONED | ADJACENT | SUBSTITUTE"
                ))

        if args.phase < 6:
            pb = clean(rec.get("Producto Base"))
            pbid = clean(rec.get("ID Producto Base"))
            if pb or pbid:
                errors.append(finding(
                    "DF-PB-001", "Publicaciones ML", row, rid, "Product Base",
                    f"{pbid} / {pb}".strip(" /"),
                    "Antes de F6 no puede existir normalización de Product Base"
                ))

    # F6 boundary must be enforced even if a premature PB was created directly
    # in Productos Base without being linked yet from Publicaciones ML.
    if args.phase < 6:
        for row, rec in candidate_product_bases:
            pbid = clean(rec.get("ID Producto Base"))
            if pbid:
                errors.append(finding(
                    "DF-PB-002", "Productos Base", row, pbid, "ID Producto Base",
                    pbid,
                    "No debe existir ningún Product Base del candidato antes de F6"
                ))

    print("============================================================")
    print("SMART IMPORTS — METHOD V2 DATA FIDELITY PREFLIGHT")
    print("============================================================")
    print(f"File:  {path}")
    print(f"Niche: {args.niche}")
    print(f"Phase: F{args.phase}")
    print(f"Publications audited: {len(candidate_publications)}")
    print(f"Product Bases found for scope: {len(candidate_product_bases)}")
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
    print("Data-fidelity invariants satisfied.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
