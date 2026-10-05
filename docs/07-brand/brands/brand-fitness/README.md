---
id: brand-fitness
title: Marca Fitness — Screening cerrado
description: Estado vigente de Marca Fitness después del primer bloque formal de Brand Candidate Screening.
version: 0.4.0
status: screening-closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-03
updated: 2026-10-05
tags:
  - brand
  - fitness
  - exploration
  - reusable-brand-system
related:
  - si-brand-001
  - si-brand-002
  - si-brand-003
---

# Marca Fitness — Screening cerrado

## 1. Estado vigente

```text
Architecture baseline: v0.2
Territory baseline: FROZEN
Missions baseline: FROZEN
Brand Candidate Screening: CLOSED
Formal candidates: BRAND-CAND-007..010
PASS TO METHOD V2: 4
Method v2: ELIGIBLE / NOT OPENED
Product Bases: NOT DEFINED
Purchase Decision: NONE
```

## 2. Territorio vigente

> **Ayudar a personas a conservar, recuperar y desarrollar capacidad física en una vida cotidiana marcada por sedentarismo, poco tiempo y espacios limitados, mediante soluciones simples, compactas, comprensibles y sostenibles en el tiempo.**

`+50` permanece como contexto/segmento potencial a explorar; no define la marca.

## 3. Misiones

```text
M1 — Construir y conservar fuerza útil
M2 — Incorporar movimiento y entrenamiento en la vida cotidiana
M3 — Conservar y recuperar movilidad, estabilidad y capacidad física
M4 — Entender el progreso y sostener la constancia
```

## 4. Lifecycle de IDs

| Hypothesis ID | Formal Candidate ID | Candidate | Territory Relationship | Decision |
|---|---|---|---|---|
| `FIT-CAND-001` | [`BRAND-CAND-007`](./candidates/brand-cand-007-accessible-compact-strength.md) | Fuerza accesible y compacta | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-002` | [`BRAND-CAND-008`](./candidates/brand-cand-008-flexible-portable-training.md) | Entrenamiento flexible y portátil | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-005` | [`BRAND-CAND-009`](./candidates/brand-cand-009-mobility-stability-physical-capacity.md) | Movilidad, estabilidad y conservación/recuperación de capacidad física | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-007` | [`BRAND-CAND-010`](./candidates/brand-cand-010-integrated-movement-sedentary-day.md) | Movimiento integrado a la jornada sedentaria | `CORE` | `PASS TO METHOD V2` |

## 5. Hipótesis no promovidas

```text
FIT-CAND-003 → MERGED INTO FIT-CAND-005 → sin ID formal propio
FIT-CAND-004 → MERGED INTO FIT-CAND-001 → sin ID formal propio
FIT-CAND-006 → TRANSVERSAL CAPABILITY: Medición + feedback + constancia → sin ID formal propio
```

Los IDs históricos se preservan y no se reutilizan.

## 6. Documentos

- [`Candidate Hypotheses v0.1`](./fitness-candidate-hypotheses-v0.1.md) — historial de hipótesis.
- [`Pre-screening Architecture v0.2`](./fitness-pre-screening-architecture-v0.2.md) — baseline del screening.
- [`Brand Candidates`](./candidates/README.md) — índice vigente y expedientes.
- [`SI-BRAND-002`](../../si-brand-002-brand-candidate-screening-method.md) — método reusable de screening.
- [`SI-BRAND-003`](../../si-brand-003-opportunity-intake-and-discovery.md) — ingreso de futuras oportunidades.

## 7. Próxima decisión

```text
BRAND-CAND-007..010
→ ELIGIBLE FOR METHOD V2
→ EXECUTION ORDER: NOT DECIDED
→ METHOD V2: NOT OPENED
```

La próxima tarea es decidir el orden de ejecución comercial. No hay Product Bases Fitness definidos todavía.

## Changelog

| Version | Fecha | Cambio |
|---|---|---|
| 0.4.0 | 2026-10-05 | Se cierra el primer bloque de Brand Candidate Screening: FIT-CAND-001/002/005/007 promueven a BRAND-CAND-007..010, todos CORE / PASS TO METHOD V2; Method v2 permanece sin abrir. |
| 0.3.0 | 2026-10-05 | Se congela Fitness v0.2 como baseline pre-screening: territorio revisado, cuatro misiones, cuatro candidatos activos, FIT-CAND-003/004 absorbidos y FIT-CAND-006 reclasificado como capacidad transversal. |
| 0.2.0 | 2026-10-05 | Se integra SI-BRAND-003 y se habilitan rutas de descubrimiento descendente y ascendente antes del Brand Candidate Screening. |
| 0.1.0 | 2026-10-03 | Se abre Marca Fitness como exploración reusable del Brand System. |
