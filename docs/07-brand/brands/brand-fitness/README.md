---
id: brand-fitness
title: Marca Fitness — Pre-screening
description: Baseline pre-screening de Marca Fitness reutilizando el Brand System de Smart Imports.
version: 0.3.0
status: pre-screening-ready
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

# Marca Fitness — Pre-screening

## 1. Estado vigente

```text
Architecture baseline: v0.2
Territory: FROZEN FOR SCREENING
Missions: FROZEN FOR SCREENING
Brand Candidate Screening: READY / NOT STARTED
Method v2: NOT OPENED
Product Bases: NOT DEFINED
Purchase Decision: NONE
```

La arquitectura v0.2 reemplaza como baseline activa a la lista inicial v0.1, que se conserva como antecedente histórico.

## 2. Territorio v0.2

> **Ayudar a personas a conservar, recuperar y desarrollar capacidad física en una vida cotidiana marcada por sedentarismo, poco tiempo y espacios limitados, mediante soluciones simples, compactas, comprensibles y sostenibles en el tiempo.**

La edad no define el territorio.

`+50` es un contexto/segmento potencialmente relevante, pero el mismo problema puede aparecer en personas más jóvenes con trabajo sedentario, oficina, desarrollo de software, home office, estudio prolongado, viajes o largos períodos sin entrenamiento.

## 3. Contexto transversal

```text
VIDA SEDENTARIA / BAJA ACTIVIDAD COTIDIANA
```

Se utiliza como hipótesis de problema de usuario, no como claim científico, médico o terapéutico.

## 4. Misiones

```text
M1 — Construir y conservar fuerza útil
M2 — Incorporar movimiento y entrenamiento en la vida cotidiana
M3 — Conservar y recuperar movilidad, estabilidad y capacidad física
M4 — Entender el progreso y sostener la constancia
```

## 5. Candidate Register pre-screening

| ID | Candidato | Estado |
|---|---|---|
| `FIT-CAND-001` | Fuerza accesible y compacta | `ACTIVE — PRE-SCREENING` |
| `FIT-CAND-002` | Entrenamiento flexible y portátil | `ACTIVE — PRE-SCREENING` |
| `FIT-CAND-003` | Recuperación y movilidad | `MERGED INTO FIT-CAND-005` |
| `FIT-CAND-004` | Calistenia y peso corporal | `MERGED INTO FIT-CAND-001` |
| `FIT-CAND-005` | Movilidad, estabilidad y conservación/recuperación de capacidad física | `ACTIVE — PRE-SCREENING` |
| `FIT-CAND-006` | Entrenamiento medible / fitness inteligente | `RECLASSIFIED AS TRANSVERSAL CAPABILITY` |
| `FIT-CAND-007` | Movimiento integrado a la jornada sedentaria | `ACTIVE — PRE-SCREENING` |

Los IDs históricos se preservan y no se reutilizan.

## 6. Capacidad transversal

`FIT-CAND-006` deja de operar como Brand Candidate independiente.

Su función conceptual pasa a ser:

```text
Medición + feedback + constancia
```

Puede aplicarse a múltiples candidatos y no obtiene Brand Fit por tecnología en sí misma.

## 7. Rutas de descubrimiento

Marca Fitness conserva las dos rutas de `SI-BRAND-003`:

```text
DESCENDENTE
territorio → misión → problema → solución

ASCENDENTE
producto descubierto → solución → problema → misión → territorio
```

Ambas convergen en `Brand Candidate Screening`.

## 8. Documentos

- [`Fitness Candidate Hypotheses v0.1`](./fitness-candidate-hypotheses-v0.1.md) — antecedente histórico inicial.
- [`Fitness Pre-screening Architecture v0.2`](./fitness-pre-screening-architecture-v0.2.md) — baseline activa.
- [`SI-BRAND-002 — Brand Candidate Screening`](../../si-brand-002-brand-candidate-screening-method.md).
- [`SI-BRAND-003 — Ingreso de oportunidades y descubrimiento`](../../si-brand-003-opportunity-intake-and-discovery.md).

## 9. Próxima acción

```text
Abrir FIT-CAND-001
→ Brand Candidate Screening
→ documentar decisión
→ recién después continuar con FIT-CAND-002
```

No abrir Method v2 hasta obtener `PASS TO METHOD V2`.

## Changelog

| Version | Fecha | Cambio |
|---|---|---|
| 0.3.0 | 2026-10-05 | Se congela Fitness v0.2 como baseline pre-screening: territorio revisado, cuatro misiones, cuatro candidatos activos, FIT-CAND-003/004 absorbidos y FIT-CAND-006 reclasificado como capacidad transversal. |
| 0.2.0 | 2026-10-05 | Se integra SI-BRAND-003 y se habilitan rutas de descubrimiento descendente y ascendente antes del Brand Candidate Screening. |
| 0.1.0 | 2026-10-03 | Se abre Marca Fitness como exploración reusable del Brand System. |
