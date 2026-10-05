---
id: brand-fitness-candidates-readme
title: Marca Fitness — Brand Candidates
description: Índice de expedientes de Brand Candidate Screening de Marca Fitness.
version: 0.2.0
status: screening-closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-05
updated: 2026-10-05
---

# Marca Fitness — Brand Candidates

## 1. Estado

```text
SCREENINGS CLOSED: 4
PASS TO METHOD V2: 4
METHOD V2 OPENED: 1
PRODUCT BASES DEFINED: 0
```

PASS habilita investigación comercial posterior; no implica prioridad, recomendación de importación ni apertura automática de Method v2.

Método aplicado: `SI-BRAND-002 v0.4`.

## 2. Mapeo de hipótesis a candidatos formales

| Hypothesis ID | Formal Candidate ID | Candidate | Territory Relationship | Decision | Method v2 |
|---|---|---|---|---|---|
| `FIT-CAND-001` | [`BRAND-CAND-007`](./brand-cand-007-accessible-compact-strength.md) | Fuerza accesible y compacta | `CORE` | `PASS TO METHOD V2` | `ELIGIBLE — NOT OPENED` |
| `FIT-CAND-002` | [`BRAND-CAND-008`](./brand-cand-008-flexible-portable-training.md) | Entrenamiento flexible y portátil | `CORE` | `PASS TO METHOD V2` | `ELIGIBLE — NOT OPENED` |
| `FIT-CAND-005` | [`BRAND-CAND-009`](./brand-cand-009-mobility-stability-physical-capacity.md) | Movilidad, estabilidad y conservación/recuperación de capacidad física | `CORE` | `PASS TO METHOD V2` | `ELIGIBLE — NOT OPENED` |
| `FIT-CAND-007` | [`BRAND-CAND-010`](./brand-cand-010-integrated-movement-sedentary-day.md) | Movimiento integrado a la jornada sedentaria | `CORE` | `PASS TO METHOD V2` | `F0 OPENED — MATRIX PENDING` |

## 3. Hipótesis no promovidas

```text
FIT-CAND-003 → MERGED INTO FIT-CAND-005 → sin BRAND-CAND ID propio
FIT-CAND-004 → MERGED INTO FIT-CAND-001 → sin BRAND-CAND ID propio
FIT-CAND-006 → RECLASSIFIED AS TRANSVERSAL CAPABILITY → sin BRAND-CAND ID propio
```

Los IDs históricos se preservan y no se reutilizan.

## 4. Distinciones consolidadas

```text
BRAND-CAND-007 → fuerza
BRAND-CAND-008 → entrenamiento flexible
BRAND-CAND-009 → movilidad / estabilidad / capacidad física
BRAND-CAND-010 → movimiento distribuido durante la jornada
```

Frontera crítica:

```text
BRAND-CAND-008 → existe intención de entrenar
BRAND-CAND-010 → existe necesidad de romper la inactividad de la jornada
```

## 5. Próximo gate

Se decidió abrir primero `BRAND-CAND-010`.

```text
BRAND-CAND-010
→ F0 OPENED
→ ANALYSIS COMPLETE
→ MATRIX MATERIALIZATION PENDING
→ F0 NOT CLOSED

BRAND-CAND-007..009
→ ELIGIBLE — NOT OPENED
```

Próximo gate formal:

```text
aut105 materialized after global lineage reconciliation
→ Matrix Validator PASS
→ F0 CLOSED
→ F1 — Market / Solution Map
```
