---
id: si-research-085
title: BRAND-CAND-010 — Post-close Evidence Reconciliation
description: Reconciliación post-cierre de fidelidad de evidencia, source binding y reglas de ejecución para BRAND-CAND-010.
version: 1.0.2
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-08
updated: 2026-10-10
brand: brand-fitness
brand_candidate: brand-cand-010
method: method-v2-agile
phase: post-close-reconciliation
---

# SI-RESEARCH-085 — BRAND-CAND-010 — Post-close Evidence Reconciliation

## 1. Motivo

Después del cierre documental de `BRAND-CAND-010`, una revisión humana detectó una desviación de fidelidad: algunos registros de `Publicaciones ML.Ventas visibles` contenían interpretación en lugar del dato crudo observable.

Matrix Validator no podía detectar esa desviación porque era semántica.

## 2. Clasificación

```text
TYPE: DATA FIDELITY / TRACEABILITY
EARLIEST AFFECTED PHASE: F3 — Demand
DECISION IMPACT: REVIEWED / NO CHANGE
REOPEN F3–F13: NO
RECONCILIATION TYPE: POST-CLOSE / NON-DECISION-IMPACTING
F14: NOT OPENED
```

## 3. Política aplicada

```text
RAW EVIDENCE
→ NORMALIZATION / CLASSIFICATION
→ INTERPRETATION
→ SCORE + CONFIDENCE
→ DECISION
```

Un campo raw no contiene interpretación. Un contador sólo se conserva/restaura si quedó preservado o puede vincularse inequívocamente a la captura correspondiente. Ante ambigüedad se usa `No informadas`. Una reverificación posterior se registra con su propia fecha y no reescribe silenciosamente la captura histórica.

## 4. Resultado de F3 ratificado

```text
A1 walking pad → POSITIVE / MODERATE
A3 pedalera → STRONG ADJACENT / WEAK JOB-SPECIFIC
A2 under-desk elliptical → WEAK / NOT DEMONSTRATED
A4 standing-desk balance board → WEAK / NOT DEMONSTRATED

EVAL-0029
Demand = 3/5
Confidence = Media
RATIFIED
```

## 5. Auditoría F8/F10

Los inputs decisivos de origen/economía fueron revisados nuevamente. `COT-0061` y `COT-0063` conservan suficiencia `decision-grade`.

```text
DECISION-GRADE ≠ PROCUREMENT-GRADE
PUBLIC LISTING ≠ FORMAL QUOTE
```

No se recalcula F11/F12 porque la auditoría no identificó un cambio de input capaz de modificar la decisión económica vigente.

## 6. Resultado estratégico

```text
BASE-FIT-001 → STOP — REOPENABLE / LOGISTICS GATE
BASE-FIT-002 → STOP — REOPENABLE / DEMAND + LOGISTICS GATE
BASE-FIT-003 → DEFER — LOW DEMAND PROOF
BASE-FIT-004 → DEFER — LOW DEMAND PROOF / STANDING-DESK DEPENDENCY
BRAND-CAND-010 → NO PORTFOLIO FINALIST / FREEZE
F14 → NOT OPENED
```

## 7. Lineage de snapshots

```text
aut118
→ snapshot histórico de cierre F13
→ SHA-256: 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a

aut119 corrected
→ primera reconciliación post-cierre
→ dual PASS
→ superseded antes de publicación

aut120
→ segunda reconciliación post-cierre
→ corrige trazabilidad temporal y amplía el preflight F6
→ dual PASS
→ BASELINE VIGENTE
→ SHA-256: 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2
```

`aut120` no representa F14 ni una nueva fase comercial. F0–F13 permanecen `CLOSED`.

## 8. Snapshot vigente

```text
matrix-aut120-brand-cand-010-post-close-reconciliation.xlsx
SHA-256: 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2

Data Fidelity Preflight: PASS
Publications audited: 24
Product Bases found for scope: 4
Exit code: 0

Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Findings: []
Limitations: []
Exit code: 0
```

## 9. Cambio permanente de proceso

La reconciliación activa `SI-BIM-001`, `SI-BIM-PROC-003`, `SI-DECISION-018`, `scripts/validate-method-v2-data-fidelity.py` y `scripts/validate-method-v2-checkpoint.sh`.

## 10. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.2 | 2026-10-10 | Cierra reconciliación sobre aut120 dual PASS y fija la baseline vigente. |
| 1.0.1 | 2026-10-10 | Registra aut119 corrected dual PASS como reconciliación intermedia. |
| 1.0.0 | 2026-10-08 | Reconciliación preparada. |
