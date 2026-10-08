---
id: si-research-080
title: BRAND-CAND-010 — Method v2 Agile — Fase 9 — Import Cost Headroom
version: 0.1.0
status: closed
created: 2026-10-08
updated: 2026-10-08
brand_candidate: brand-cand-010
phase: F9
mode: AUTO
---

# SI-RESEARCH-080 — BRAND-CAND-010 — F9 Import Cost Headroom

Baseline histórica del proyecto:
```text
FX comparison baseline = ARS/USD 1.535
channel cost = 25%
commercial cost = 5%
target margin = 25%
max economic landed = 51,25% del precio bruto
```

El FX es baseline histórica, **no FX actual**.

## BASE-FIT-001
- benchmark local: `ML-0153` — ARS 433,535
- costo origen: `COT-0061` — US$59,90
- max economic landed: ~US$144.75
- headroom: **~2.42x**
- lectura: `SURVIVES`, pero logística/peso será dominante.

## BASE-FIT-002
- benchmark local de forma física: `ML-0160` — ARS 38,790
- costo origen: `COT-0063` — US$9,50
- max economic landed: ~US$12.95
- headroom: **~1.36x**
- lectura: `SURVIVES — HIGHLY CONDITIONED`; buffer estrecho, MOQ alto y demand-job gap.

```text
HEADROOM ≠ LANDED COST ≠ MARGIN
```

Estado: `ANALYSIS COMPLETE / MATRIX MATERIALIZED / VALIDATOR PASS / CLOSED`.
Cierre confirmado: `F9 CLOSED — aut114 PASS`; `F10 Minimum Landed Cost Dataset — AUTO` fue ejecutada posteriormente.
