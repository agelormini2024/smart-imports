---
id: docs-07-brand-readme
title: 07 — Brand
description: Índice del Brand System de Smart Imports y sus instancias de marca.
version: 0.13.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-10-05
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

<!-- OPPORTUNITY-INTAKE:START -->
## Ingreso de oportunidades

El Brand System admite oportunidades descubiertas tanto desde una investigación estructurada como desde un producto observado espontáneamente.

```text
DESCUBRIMIENTO DESCENDENTE
territorio → misión → problema → solución → producto

DESCUBRIMIENTO ASCENDENTE
producto → solución → problema → misión → territorio
```

Ambas rutas convergen antes de `Brand Candidate Screening`.

```text
ORIGEN DE LA IDEA ≠ CALIDAD DE LA OPORTUNIDAD
```

Documento: [`SI-BRAND-003 — Ingreso de oportunidades y descubrimiento`](./si-brand-003-opportunity-intake-and-discovery.md).
<!-- OPPORTUNITY-INTAKE:END -->

<!-- BRAND-FITNESS-EXPLORATION:START -->
## Marca Fitness — primer Method v2 abierto

```text
Brand Candidate Screening: CLOSED
BRAND-CAND-007 → CORE / PASS TO METHOD V2 / NOT OPENED
BRAND-CAND-008 → CORE / PASS TO METHOD V2 / NOT OPENED
BRAND-CAND-009 → CORE / PASS TO METHOD V2 / NOT OPENED
BRAND-CAND-010 → CORE / PASS TO METHOD V2 / F0 OPENED
F0 → ANALYSIS COMPLETE / MATRIX PENDING / NOT CLOSED

FIT-CAND-003 → MERGED
FIT-CAND-004 → MERGED
FIT-CAND-006 → TRANSVERSAL CAPABILITY

Product Bases Fitness: NOT DEFINED
```

Documentos:

- [`Marca Fitness`](./brands/brand-fitness/README.md)
- [`Brand Candidates`](./brands/brand-fitness/candidates/README.md)
- [`Pre-screening Architecture v0.2`](./brands/brand-fitness/fitness-pre-screening-architecture-v0.2.md) — baseline histórica
- [`SI-RESEARCH-070`](../06-research/brand-fitness/si-research-070-brand-cand-010-method-v2-agile-phase-0-research-brief.md)

Los `FIT-CAND-*` se conservan como trazabilidad histórica local; `BRAND-CAND-*` identifica los candidatos formales globales.

La prioridad comercial inmediata de Smart Imports continúa siendo la primera importación de Marca Hogar después de las revisiones externas pendientes con socio y despachante.
<!-- BRAND-FITNESS-EXPLORATION:END -->

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

- Brand System reusable: v0.3.
- Brand Candidate Screening: v0.3.
- Marca Hogar: v0.1.
- `BRAND-CAND-001`: `PASS TO METHOD V2`.
- `BRAND-CAND-002`: `PASS TO METHOD V2`.
- `BRAND-CAND-003`: `PASS TO METHOD V2`.
- `BRAND-CAND-004`: `PASS TO METHOD V2`.
- `BRAND-CAND-005`: `PASS TO METHOD V2`.
- `BRAND-CAND-006`: `BRAND FIT CONFIRMED` — strong adjacency.
- Próximo paso: aplicar Brand System v0.3 a oportunidades reales futuras y observar si aparecen excepciones que justifiquen otra evolución metodológica.
- matriz, schema y Matrix Validator: sin cambios.

## 5. Changelog

| Version | Date | Change |
|---|---|---|
| 0.13.0 | 2026-10-05 | Marca Fitness abre Method v2 únicamente para BRAND-CAND-010; F0 queda analysis complete / matrix pending / not closed y 007–009 permanecen elegibles sin abrir. |
| 0.12.0 | 2026-10-05 | Se cierra el primer bloque de screening de Marca Fitness: cuatro hipótesis promueven a BRAND-CAND-007..010 como CORE / PASS TO METHOD V2; se preservan IDs locales como trazabilidad. |
| 0.11.0 | 2026-10-05 | Marca Fitness congela arquitectura pre-screening v0.2 con territorio/misiones revisados, cuatro candidatos activos y decisiones MERGED/RECLASSIFIED trazables. |
| 0.1.0 | 2026-07-02 | Placeholder inicial. |
| 0.2.0 | 2026-09-16 | Se incorpora Brand System, Marca Hogar y Brand Candidate Screening. |
| 0.3.0 | 2026-09-17 | Se separa metodología reusable de instancias y expedientes de candidatos. |
| 0.4.0 | 2026-09-17 | Se documenta BRAND-CAND-003 como PASS TO METHOD V2 y se avanza a BRAND-CAND-004. |
| 0.5.0 | 2026-09-17 | Se documenta BRAND-CAND-004 como PASS TO METHOD V2 y se avanza a BRAND-CAND-005. |
| 0.6.0 | 2026-09-17 | Se documenta BRAND-CAND-005 como PASS TO METHOD V2 y se avanza al screening retrospectivo de BRAND-CAND-006. |
| 0.7.0 | 2026-09-17 | BRAND-CAND-006 confirma Brand Fit como strong adjacency; finaliza el bloque inicial de screenings. |

| 0.8.0 | 2026-09-17 | Se consolida Brand System / Brand Candidate Screening v0.3 con Territory Relationship y soporte prospectivo/retrospectivo. |
| 0.9.0 | 2026-10-03 | Se abre Marca Fitness como exploración reusable del Brand System; FIT-CAND-001..006 quedan como hipótesis pre-screening. BRAND-CAND-006 continúa su reconciliación retrospectiva en Marca Hogar. |
| 0.10.0 | 2026-10-05 | Se incorpora SI-BRAND-003: ingreso de oportunidades espontáneas, descubrimiento descendente/ascendente y convergencia obligatoria en Brand Candidate Screening antes de Method v2. |
