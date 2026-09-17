---
id: si-brand-001
title: Reusable Brand System
description: Define el Brand System reutilizable de Smart Imports para construir marcas y portfolios coherentes antes de aplicar Method v2.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-16
updated: 2026-09-17
tags:
  - brand
  - brand-system
  - portfolio
  - missions
  - brand-fit
related:
  - si-brand-002
  - si-decision-016
  - si-roadmap-002
  - si-agent-001
audience:
  - founder
  - partner
  - assistant
phase: brand-strategy
---

# SI-BRAND-001 — Brand System reutilizable

> La marca no debe decirnos qué producto comprar. Debe decirnos qué problemas queremos ser reconocidos por resolver.

## 1. Propósito

Este documento define el **Brand System reutilizable** de Smart Imports.

Su objetivo es establecer una arquitectura común para construir múltiples marcas sin mezclar identidad de marca, pertenencia al portfolio y evaluación comercial.

Cada instancia de marca se documenta bajo:

```text
docs/07-brand/brands/<brand-id>/
```

## 2. Separación fundamental

```text
BRAND FIT
¿Queremos que nuestra marca venda este producto?

METHOD V2
¿Existe realmente un negocio defendible alrededor de este producto?
```

Ninguna pregunta sustituye a la otra.

## 3. Arquitectura reusable

```text
BRAND
  ↓
BRAND TERRITORY
  ↓
MISSIONS
  ↓
PROBLEMS
  ↓
SOLUTIONS
  ↓
BRAND CANDIDATE SCREENING
  ↓
CANDIDATOS APROBADOS
  ↓
METHOD V2
  ↓
PRODUCT BASES / OPORTUNIDADES EVALUADAS
```

### 3.1 Brand

Instancia concreta construida mediante el Brand System, con territorio, misiones, problemas y candidatos propios.

### 3.2 Brand Territory

Espacio estratégico en el que una marca decide jugar. Debe permitir crecimiento sin perder capacidad de exclusión.

### 3.3 Missions

Expresan **qué mejora busca producir la marca**. No son categorías comerciales ni taxonomías de marketplace.

### 3.4 Problems

Cada misión se descompone en problemas concretos y reconocibles.

### 3.5 Solutions

Una `Solution` es una familia conceptual que intenta resolver un problema. Todavía no es necesariamente un `Product Base`.

### 3.6 Product Base

Method v2 puede normalizar una Solution en una o más arquitecturas/configuraciones comercialmente significativas.

```text
SOLUTION ≠ PRODUCT BASE
```

Ejemplo:

```text
SOLUTION
Detección y prevención de fugas

→ PRODUCT BASE A
Sensor puntual + válvula

→ PRODUCT BASE B
Monitor de caudal central + válvula

→ PRODUCT BASE C
Sistema basado en presión/acústica + corte
```

## 4. Principios generales

### 4.1 La pertenencia debe ser natural

> **¿Este producto entra naturalmente dentro de esta marca o tenemos que inventar una explicación para justificarlo?**

Cuando la explicación se vuelve artificial, probablemente se encontró un límite del territorio.

### 4.2 El vínculo debe ser central

Un beneficio accesorio no es suficiente para justificar Brand Fit.

### 4.3 La mejora debe ser tangible

Conveniencia, novedad o conectividad no equivalen automáticamente a valor de marca.

### 4.4 La tecnología es un medio

```text
SMART ≠ BRAND FIT
```

### 4.5 La credibilidad importa

```text
BRAND RELEVANCE
¿El problema pertenece al territorio?

BRAND CREDIBILITY
¿La solución realmente puede sostener la mejora que promete?
```

Un candidato puede tener alta relevancia y credibilidad todavía desconocida.

## 5. Reusabilidad entre marcas

Primera instancia real:

```text
brand-hogar
```

Ejemplo conceptual de una futura instancia:

```text
brand-fitness
```

Una eventual marca del `Mundo Fitness` podría definir, por ejemplo:

```text
Territorio:
mejorar la práctica física de forma consistente

Misiones posibles:
- entrenar;
- recuperar;
- medir;
- progresar;
- sostener el hábito.
```

Ese ejemplo demuestra reusabilidad; no constituye una decisión de lanzar una marca Fitness.

## 6. Estructura documental

```text
docs/07-brand/
├── si-brand-001-reusable-brand-system.md
├── si-brand-002-brand-candidate-screening-method.md
└── brands/
    ├── brand-hogar/
    │   ├── README.md
    │   └── candidates/
    │       ├── README.md
    │       ├── brand-cand-001-....md
    │       └── brand-cand-002-....md
    └── brand-fitness/
        └── ...
```

Responsabilidades:

```text
SI-BRAND-001
→ reglas del Brand System

SI-BRAND-002
→ método reusable de screening

brands/<brand-id>/README.md
→ territorio, misiones, límites y Candidate Register

brands/<brand-id>/candidates/
→ expediente individual y handoff de cada candidato
```

## 7. IDs

Los IDs `BRAND-CAND-XXX` son globales dentro de Smart Imports. No se reinicia la numeración por marca.

```text
Candidate ID: BRAND-CAND-017
Brand: brand-fitness
```

Esto evita colisiones y simplifica trazabilidad, BD y RAG.

## 8. Relación con Method v2

```text
BRAND SYSTEM
¿Dónde queremos jugar?

→ Brand Territory
→ Missions
→ Problems
→ Solutions
→ Brand Candidate Screening

METHOD V2
¿Dónde existe negocio?

→ Demand
→ Competition
→ Product Base normalization
→ Origin
→ Headroom
→ Minimum Landed Cost Dataset
→ Landed Cost Screen
→ Decision
```

El Brand System no modifica las reglas vigentes de Method v2.

`Brand Candidate Screening` es la primera forma operativa del futuro `Brand Product Filter`. Su formalización debe surgir de evidencia acumulada usando candidatos reales.

## 9. Consecuencias futuras para Intelligence Engine

Sin modificar todavía matriz, schema ni Engine, se registran necesidades conceptuales potenciales:

```text
BRAND
BRAND_TERRITORY
MISSION
PROBLEM
SOLUTION
BRAND_CANDIDATE
BRAND_FIT_EVALUATION
BRAND_RELEVANCE
BRAND_CREDIBILITY
BRAND_TERRITORY_VERSION
```

`PRODUCT_BASE` deberá poder relacionarse tanto con evaluaciones de Method v2 como con evaluaciones de Brand Fit.

Estas entidades son necesidades futuras de modelado, no cambios autorizados sobre `full-matrix-v5 0.7.0`.

## 10. Documentos relacionados

- [SI-BRAND-002 — Brand Candidate Screening](./si-brand-002-brand-candidate-screening-method.md)
- [Marca Hogar](./brands/brand-hogar/README.md)
- [SI-DECISION-016 — Arquitectura de marca por misiones](../09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md)
- [SI-ROADMAP-002 — Estado actual y handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 11. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-16 | Primera definición del Brand System reusable junto con Marca Hogar v0.1. |
| 0.2.0 | 2026-09-17 | Se separa el Brand System reusable de sus instancias y se formaliza `brands/<brand-id>/`. |
