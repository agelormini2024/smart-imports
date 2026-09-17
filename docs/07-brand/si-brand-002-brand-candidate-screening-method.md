---
id: si-brand-002
title: Brand Candidate Screening Method
description: Método reusable para decidir si una solución tiene suficiente Brand Fit para ingresar a Method v2.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-16
updated: 2026-09-17
tags:
  - brand
  - screening
  - brand-fit
  - portfolio
  - method
related:
  - si-brand-001
  - si-decision-016
  - si-roadmap-002
audience:
  - founder
  - partner
  - assistant
phase: brand-strategy
---

# SI-BRAND-002 — Brand Candidate Screening

> Primero decidir si queremos jugar ahí. Después preguntar si existe negocio.

## 1. Propósito

`Brand Candidate Screening` decide si una **Solution** merece consumir investigación comercial bajo una marca concreta.

Responde:

> **Si esta oportunidad terminara siendo un excelente negocio, ¿querríamos venderla bajo esta marca?**

No evalúa demanda, competencia, margen, origen, Headroom, Landed Cost ni decisión de importación. Eso pertenece a Method v2.

## 2. Alcance reusable

Cada marca define:

```text
Brand Territory
→ Missions
→ Problems
```

y utiliza el mismo `Brand Candidate Screening`.

```text
brand-hogar
→ misiones de Hogar
→ Brand Candidate Screening
→ Method v2

brand-fitness
→ misiones de Fitness
→ Brand Candidate Screening
→ Method v2
```

### 2.1 Relación con Brand Product Filter

`Brand Candidate Screening` es la primera forma operativa del futuro `Brand Product Filter`.

Se mantiene la denominación `Screening` mientras el método se valida con candidatos reales y todavía no existe evidencia suficiente para fijar reglas, ponderaciones o umbrales rígidos.

## 3. Unidad de evaluación

La unidad inicial es una **Solution / Brand Candidate**, no necesariamente un Product Base.

```text
BRAND CANDIDATE / SOLUTION ≠ PRODUCT BASE
```

## 4. Dimensiones del screening

### 4.1 Problema reconocible

> ¿Resuelve un problema claramente identificable dentro del territorio de la marca?

### 4.2 Mission Fit

> ¿El problema pertenece naturalmente a una misión vigente?

### 4.3 Centralidad

> ¿La mejora relacionada con la marca forma parte de la razón principal de existencia de la solución?

### 4.4 Tangibilidad

> ¿Produce una mejora concreta o sólo agrega conveniencia?

### 4.5 Tecnología útil

> Cuando existe tecnología, ¿contribuye directamente al resultado?

### 4.6 Credibilidad

> ¿La mejora prometida podría sostenerse posteriormente con evidencia razonable?

### 4.7 Experiencia de marca

> ¿Existe capacidad de construir una experiencia coherente mediante información, packaging, instrucciones, soporte, repuestos, garantía o postventa?

### 4.8 Territory Risk

> ¿Aceptar este candidato obliga a expandir el territorio de manera difícil de controlar?

## 5. Brand Relevance y Brand Credibility

```text
BRAND RELEVANCE
¿El problema pertenece al territorio?

BRAND CREDIBILITY
¿La solución realmente puede producir la mejora que promete?
```

La solución puede pertenecer al territorio mientras todavía sea necesario demostrar su impacto real.

## 6. Estados

### PASS TO METHOD V2

Brand Fit suficiente para justificar investigación comercial. No implica recomendación de importación.

### HOLD — BRAND FIT UNCLEAR

Relación plausible, pero necesita definición adicional o existe riesgo de expansión conceptual.

### OUTSIDE BRAND TERRITORY

Puede ser una oportunidad comercial, pero no pertenece naturalmente a esa marca.

## 7. No usar scoring numérico prematuro

No se asigna score 0–100.

Pueden utilizarse lecturas cualitativas como `fuerte`, `muy alto` o `borde`, pero no constituyen una escala formal ni sustituyen la decisión de screening.

## 8. Salida mínima

```text
Candidate ID
Candidate
Brand
Mission
Problem
Solution definition
Brand Relevance
Brand Credibility
Brand-fit rationale
Claims / assumptions to validate
Territory risks
Decision
Decision rationale
Method v2 handoff
Date
```

## 9. Persistencia documental

El método no acumula screenings concretos.

Cada marca mantiene su registro en:

```text
docs/07-brand/brands/<brand-id>/README.md
```

Cada candidato mantiene su expediente en:

```text
docs/07-brand/brands/<brand-id>/candidates/brand-cand-XXX-<slug>.md
```

La ficha individual constituye la fuente de verdad del handoff entre Brand System y Method v2.

## 10. Flujo

```text
IDEA / PRODUCTO OBSERVADO
          ↓
IDENTIFICAR SOLUCIÓN
          ↓
BRAND CANDIDATE SCREENING
          ↓
 ┌────────┼────────┐
 ↓        ↓        ↓
PASS     HOLD    OUTSIDE
 ↓
METHOD V2
 ↓
NORMALIZACIÓN / PRODUCT BASES
 ↓
EVALUACIÓN COMERCIAL
```

## 11. Relación con Method v2

El screening no debe evaluar anticipadamente:

- Demanda;
- Competencia;
- origen;
- Headroom;
- Landed Cost;
- margen;
- ROI.

Son válidos resultados como:

```text
Brand Fit: HIGH
Method v2: WEAK
```

y también:

```text
Brand Fit: LOW
Method v2: STRONG
```

## 12. Consecuencias futuras para modelado

```text
BRAND_CANDIDATE
BRAND_FIT_EVALUATION
BRAND_RELEVANCE
BRAND_CREDIBILITY
MISSION
PROBLEM
SOLUTION
DECISION
DECISION_RATIONALE
CLAIM_TO_VALIDATE
TERRITORY_RISK
METHOD_V2_HANDOFF
```

No se modifica todavía la matriz vigente.

## 13. Documentos relacionados

- [SI-BRAND-001 — Brand System reusable](./si-brand-001-reusable-brand-system.md)
- [Marca Hogar](./brands/brand-hogar/README.md)
- [SI-DECISION-016](../09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md)

## 14. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-16 | Primera versión reusable y primer screening aplicado. |
| 0.2.0 | 2026-09-17 | Se separan resultados concretos del método y se formaliza persistencia por marca/candidato. |
