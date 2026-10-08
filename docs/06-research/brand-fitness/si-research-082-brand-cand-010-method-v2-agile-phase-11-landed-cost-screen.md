---
id: si-research-082
title: BRAND-CAND-010 — Method v2 Agile — Fase 11 — Landed Cost Screen
version: 0.1.0
status: closed
created: 2026-10-08
updated: 2026-10-08
brand_candidate: brand-cand-010
phase: F11
mode: AUTO
---

# SI-RESEARCH-082 — BRAND-CAND-010 — F11 Landed Cost Screen

## Baseline
```text
FX comparison baseline = 1.535 ARS/USD
air freight proxy = US$10/kg chargeable
chargeable weight = max(physical, CBM×167)
insurance = 0,5%
import duty = 18% CIF — WORKING ASSUMPTION
statistical rate = 3%
customs broker = 5% CIF
origin normalization = US$150/shipment
local logistics = US$100/shipment
TCA flat = banda oficial por peso físico
```

## BASE-FIT-001 — Walking pad
| Qty | Executable | Economic LC/u | Max LC/u |
|---:|---|---:|---:|
| 50 | Sí | US$311.13 | US$144.75 |
| 100 | Sí | US$303.82 | US$144.75 |

El peso físico (17 kg/u) domina el aéreo.

## BASE-FIT-002 — Pedalera
| Qty | Executable | Economic LC/u | Max LC/u |
|---:|---|---:|---:|
| 50 | No — sensibilidad | US$70.54 | US$12.95 |
| 100 | No — sensibilidad | US$66.27 | US$12.95 |
| 500 | Sí — MOQ público | US$62.22 | US$12.95 |

El peso volumétrico y el bajo ticket local destruyen la economía aérea.

```text
AIR STRESS SCREEN ≠ LOGISTICS PLAN
ECONOMIC LANDED COST ≠ TOTAL CASH OUTLAY
```

F11 no decide STOP/PASS; F12 interpreta.

Estado: `ANALYSIS COMPLETE / MATRIX MATERIALIZED / VALIDATOR PASS / CLOSED`.
