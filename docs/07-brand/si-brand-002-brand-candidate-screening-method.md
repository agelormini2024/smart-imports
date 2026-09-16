---
id: si-brand-002
title: Brand Candidate Screening Method
description: Método reusable para decidir si una solución tiene suficiente Brand Fit para ingresar a Method v2.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-16
updated: 2026-09-16
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

`Brand Candidate Screening` es el filtro previo a Method v2 que decide si una **solución** merece consumir investigación comercial bajo una marca concreta.

Responde:

> **Si esta oportunidad terminara siendo un excelente negocio, ¿querríamos venderla bajo esta marca?**

No responde:

- si existe demanda;
- si la competencia es favorable;
- si existe margen;
- si el origen es viable;
- si el Landed Cost cierra;
- si conviene importar.

Esas preguntas pertenecen a Method v2.

## 2. Alcance reusable

El método no pertenece exclusivamente a `Marca Hogar`.

Cada futura marca puede definir:

```text
Brand Territory
→ Missions
→ Problems
```

y usar el mismo `Brand Candidate Screening`.

Ejemplo conceptual:

```text
Marca Hogar
→ misiones del hogar
→ Brand Candidate Screening
→ Method v2

Mundo Fitness
→ misiones de fitness
→ Brand Candidate Screening
→ Method v2
```

El filtro cambia de contexto de marca; la lógica metodológica se conserva.

### 2.1 Relación con el futuro Brand Product Filter

`Brand Candidate Screening v0.1` es la primera forma operativa del concepto de `Brand Product Filter`.

La denominación `Screening` se mantiene mientras el método se valida con candidatos reales y todavía no existe evidencia suficiente para fijar reglas, ponderaciones o umbrales más rígidos.

Si la experiencia demuestra estabilidad, este screening podrá evolucionar hacia un `Brand Product Filter` formal sin cambiar su propósito central:

> decidir si una solución pertenece suficientemente al territorio de una marca antes de invertir trabajo de Method v2.

## 3. Unidad de evaluación

La unidad inicial es una **Solution / Brand Candidate**, no necesariamente un Product Base.

Ejemplo:

```text
Brand Candidate:
Sistema doméstico de detección de fugas con corte automático
```

Method v2 podrá normalizar posteriormente múltiples Product Bases.

Por lo tanto:

```text
BRAND CANDIDATE / SOLUTION ≠ PRODUCT BASE
```

## 4. Dimensiones del screening v0.1

### 4.1 Problema reconocible

Pregunta:

> ¿Resuelve un problema cotidiano claramente identificable dentro del territorio de la marca?

Una narrativa artificial o excesivamente abstracta es señal de bajo Brand Fit.

### 4.2 Mission Fit

Pregunta:

> ¿El problema pertenece naturalmente a una misión vigente?

La relación debe poder explicarse sin deformar la misión.

### 4.3 Centralidad

Pregunta:

> ¿La mejora relacionada con la marca forma parte de la razón principal de existencia del producto?

Un beneficio accesorio no es suficiente.

### 4.4 Tangibilidad

Pregunta:

> ¿Produce una mejora concreta o sólo agrega conveniencia?

Ejemplo:

```text
control remoto desde una app
```

no constituye por sí mismo una mejora relevante.

### 4.5 Tecnología útil

Pregunta:

> Cuando existe tecnología, ¿contribuye directamente al resultado?

El método evita premiar `smartness` como atributo independiente.

### 4.6 Credibilidad

Pregunta:

> ¿La mejora prometida podría sostenerse posteriormente con evidencia razonable?

En esta etapa no se exige validar completamente el claim.

Se exige que el claim sea potencialmente investigable.

### 4.7 Experiencia de marca

Pregunta:

> ¿Existe capacidad de construir una experiencia coherente mediante información, packaging, instrucciones, soporte, repuestos, garantía o postventa?

El objetivo no es limitarse a colocar un logo sobre un producto genérico.

### 4.8 Territory Risk

Pregunta:

> ¿Aceptar este candidato obliga a expandir el territorio de manera difícil de controlar?

Este criterio protege contra la deriva de portfolio.

## 5. Brand Relevance y Brand Credibility

Se distinguen dos conceptos.

### 5.1 Brand Relevance

> ¿El problema pertenece al territorio?

### 5.2 Brand Credibility

> ¿La solución realmente puede producir la mejora que promete?

Ejemplo:

```text
Procesador de residuos orgánicos

Brand Relevance: HIGH
Brand Credibility: UNKNOWN
```

La solución puede pertenecer claramente al territorio mientras todavía sea necesario demostrar su impacto real.

Esta distinción se registra conceptualmente para un futuro modelo de datos.

No se incorpora todavía a la matriz vigente.

## 6. Estados del screening

La versión 0.1 utiliza tres estados.

### PASS TO METHOD V2

La solución tiene suficiente Brand Fit como para justificar investigación comercial.

No implica recomendación de importación.

### HOLD — BRAND FIT UNCLEAR

Existe una relación plausible con el territorio, pero el caso necesita una definición mejor o existe riesgo de expansión conceptual.

### OUTSIDE BRAND TERRITORY

La solución puede ser comercialmente interesante, pero no pertenece naturalmente a la marca.

No debe eliminarse necesariamente del conocimiento de Smart Imports.

## 7. No usar scoring numérico prematuro

La versión 0.1 no asigna un score de 0 a 100.

La metodología todavía se encuentra en validación práctica y no existe evidencia suficiente para justificar ponderaciones numéricas.

Pueden utilizarse lecturas cualitativas como `fuerte`, `muy alto`, `borde` o equivalentes para describir un caso, pero no constituyen una escala formal ni reemplazan la decisión de screening.

El objetivo inicial es responder:

```text
1. ¿Pertenece?
2. ¿Por qué pertenece?
3. ¿Qué misión y problema representa?
4. ¿Qué claims o supuestos deberán validarse después?
```

## 8. Salida mínima de un screening

Cada screening debe producir:

```text
Candidate ID
Candidate
Brand
Mission
Problem
Brand-fit rationale
Claims / assumptions to validate
Territory risks
Decision
Decision rationale
Date
```

## 9. Flujo

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

## 10. Relación con Method v2

El Brand Candidate Screening no debe evaluar anticipadamente:

- Demanda;
- Competencia;
- origen;
- Headroom;
- Landed Cost;
- margen;
- ROI.

Esta separación evita que Brand Fit se convierta en una forma encubierta de scoring comercial.

Ejemplos posibles:

```text
Brand Fit: HIGH
Method v2: WEAK
```

Producto coherente con la marca, pero mal negocio.

```text
Brand Fit: LOW
Method v2: STRONG
```

Buena oportunidad comercial, pero no para esa marca.

Ambos resultados son válidos.

## 11. Brand Candidate Register inicial — Marca Hogar

| ID | Candidate | Mission | Status | Brand Fit preliminar |
|---|---|---|---|---|
| `BRAND-CAND-001` | Sistema de detección de fugas + corte automático | Usar mejor los recursos | `PASS TO METHOD V2` | Muy alto |
| `BRAND-CAND-002` | Purificación de agua doméstica | Mejorar condiciones del hogar | `PENDING` | — |
| `BRAND-CAND-003` | Purificación de aire | Mejorar condiciones del hogar | `PENDING` | — |
| `BRAND-CAND-004` | Monitor de consumo energético | Usar mejor los recursos | `PENDING` | — |
| `BRAND-CAND-005` | Compostaje / procesamiento de residuos orgánicos | Reducir y gestionar residuos | `PENDING` | — |
| `BRAND-CAND-006` | Arenero automático open-top / acceso amplio (`BASE-PET-003`) | Problemas domésticos recurrentes | `RETROSPECTIVE BRAND SCREENING PENDING` | — |

`BRAND-CAND-006` ya cuenta con investigación previa en Method v2 por haber surgido antes de formalizar el Brand System. Su inclusión en este registro sirve como prueba retrospectiva del filtro, no reinicia su evaluación comercial.

## 12. Screening 001 — Detección de fugas + corte automático

### 12.1 Candidate

```text
ID: BRAND-CAND-001
Solution: Sistema doméstico de detección de fugas de agua con corte automático
Brand: Marca Hogar
Primary Mission: Usar mejor los recursos
Secondary Mission: Resolver problemas domésticos recurrentes
Date: 2026-09-16
```

### 12.2 Problema

Una pérdida de agua puede permanecer sin detectar, desperdiciar un recurso y provocar daños en la vivienda.

**Evaluación:** fuerte.

### 12.3 Mission Fit

La solución interviene directamente sobre:

```text
agua
+ desperdicio
+ prevención
```

**Evaluación:** muy fuerte.

### 12.4 Centralidad

La detección y prevención de pérdidas constituye la función central de la solución.

**Evaluación:** muy fuerte.

### 12.5 Tangibilidad

El beneficio puede expresarse como:

- detectar;
- alertar;
- cortar;
- prevenir pérdida;
- prevenir daño.

No depende de una función de conveniencia.

**Evaluación:** muy fuerte.

### 12.6 Tecnología útil

Sensores, válvula, automatización y alertas pueden contribuir directamente al resultado.

Funciones accesorias de interfaz no modifican el Brand Fit central.

**Evaluación:** fuerte.

### 12.7 Credibilidad

El producto permite potencialmente validar:

- sensibilidad;
- tiempo de reacción;
- capacidad de cierre;
- presión soportada;
- caudal;
- falsos positivos;
- comportamiento sin conectividad;
- operación manual de emergencia.

**Evaluación:** alto potencial de validación.

### 12.8 Experiencia de marca

Existe capacidad de agregar valor mediante:

- instrucciones en español;
- compatibilidad clara;
- instalación;
- soporte;
- procedimientos de emergencia;
- repuestos;
- garantía.

**Evaluación:** fuerte.

### 12.9 Territory Risk

Aceptar esta solución no obliga a aceptar Smart Home genérico.

La razón de pertenencia es el problema agua/recursos, no la conectividad.

**Evaluación:** bajo.

### 12.10 Claims / assumptions to validate

Al ingresar a Method v2 deberán validarse, según la arquitectura concreta:

- qué tipo de fugas detecta;
- cómo realiza el corte;
- condiciones de instalación;
- compatibilidad con instalaciones domésticas;
- presión y caudal;
- dependencia de red eléctrica o conectividad;
- confiabilidad;
- certificaciones/intervenciones que correspondan;
- riesgos de instalación y postventa.

### 12.11 Decisión

```text
PASS TO METHOD V2
```

Razón:

> La solución pertenece naturalmente a la misión `Usar mejor los recursos`, su beneficio es central y tangible, la tecnología puede aportar directamente al resultado y su aceptación no expande arbitrariamente el territorio de Marca Hogar.

## 13. Próximo candidato

```text
BRAND-CAND-002
Purificación de agua doméstica
```

Este caso deberá prestar especial atención a:

- claims de salud;
- calidad de agua;
- microbiología;
- certificaciones;
- reemplazo de consumibles;
- Brand Credibility.

## 14. Consecuencias futuras para modelado

Sin modificar el sistema vigente, se registran como candidatos de modelo:

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
```

La necesidad se observará durante el uso real antes de decidir Matrix vNext o modelo persistente del Intelligence Engine.

## 15. Documentos relacionados

- [SI-BRAND-001 — Brand System reutilizable y Marca Hogar](./si-brand-001-reusable-brand-system-and-home-territory.md)
- [SI-DECISION-016 — Arquitectura de marca por misiones](../09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md)
- [SI-ROADMAP-002 — Estado actual y handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 16. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-16 | Primera versión reusable del Brand Candidate Screening y registro de BRAND-CAND-001. |
