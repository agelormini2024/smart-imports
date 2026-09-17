---
id: docs-07-brand-readme
title: 07 — Brand
description: Índice del Brand System de Smart Imports y sus instancias de marca.
version: 0.6.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-09-17
tags:
  - smart-imports
  - brand
  - portfolio
  - brand-system
related:
  - si-brand-001
  - si-brand-002
  - si-decision-016
---

# 07 — Brand

> La marca define dónde queremos jugar; Method v2 determina dónde existe un negocio defendible.

## 1. Arquitectura

```text
Brand System reusable
├── SI-BRAND-001 — arquitectura general
├── SI-BRAND-002 — screening reusable
└── brands/
    └── brand-hogar/
        ├── territorio / misiones / límites
        └── candidates/
            └── expedientes individuales
```

## 2. Metodología reusable

| Documento | Propósito |
|---|---|
| [SI-BRAND-001](./si-brand-001-reusable-brand-system.md) | Arquitectura común para construir cualquier marca. |
| [SI-BRAND-002](./si-brand-002-brand-candidate-screening-method.md) | Screening reusable previo a Method v2. |
| [SI-DECISION-016](../09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md) | Decisión metodológica. |

## 3. Instancias de marca

| Brand ID | Estado | Descripción |
|---|---|---|
| [`brand-hogar`](./brands/brand-hogar/README.md) | v0.1 / validación práctica | Primera implementación real. |

`brand-fitness` / `Mundo Fitness` permanece como ejemplo conceptual de reusabilidad, no como marca decidida.

## 4. Estado al 2026-09-17

- Brand System reusable: v0.2.
- Brand Candidate Screening: v0.2.
- Marca Hogar: v0.1.
- `BRAND-CAND-001`: `PASS TO METHOD V2`.
- `BRAND-CAND-002`: `PASS TO METHOD V2`.
- `BRAND-CAND-003`: `PASS TO METHOD V2`.
- `BRAND-CAND-004`: `PASS TO METHOD V2`.
- `BRAND-CAND-005`: `PASS TO METHOD V2`.
- Próximo screening: `BRAND-CAND-006 — PET-003 (screening retrospectivo)`.
- matriz, schema y Matrix Validator: sin cambios.

## 5. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Placeholder inicial. |
| 0.2.0 | 2026-09-16 | Se incorpora Brand System, Marca Hogar y Brand Candidate Screening. |
| 0.3.0 | 2026-09-17 | Se separa metodología reusable de instancias y expedientes de candidatos. |
| 0.4.0 | 2026-09-17 | Se documenta BRAND-CAND-003 como PASS TO METHOD V2 y se avanza a BRAND-CAND-004. |
| 0.5.0 | 2026-09-17 | Se documenta BRAND-CAND-004 como PASS TO METHOD V2 y se avanza a BRAND-CAND-005. |
| 0.6.0 | 2026-09-17 | Se documenta BRAND-CAND-005 como PASS TO METHOD V2 y se avanza al screening retrospectivo de BRAND-CAND-006. |
