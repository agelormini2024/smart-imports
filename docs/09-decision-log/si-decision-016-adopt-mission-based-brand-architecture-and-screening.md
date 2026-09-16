---
id: si-decision-016
title: Adopt Mission-Based Brand Architecture and Brand Candidate Screening
description: Adopta un Brand System reusable basado en territorio, misiones y problemas, con screening previo a Method v2.
version: 1.0.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-16
updated: 2026-09-16
tags:
  - decision
  - brand
  - portfolio
  - missions
  - screening
  - method-v2
related:
  - si-brand-001
  - si-brand-002
  - si-roadmap-002
  - si-decision-015
audience:
  - founder
  - partner
  - assistant
phase: brand-strategy
---

# SI-DECISION-016 — Adoptar arquitectura de marca por misiones y Brand Candidate Screening

## 1. Contexto

Smart Imports necesita construir portfolios coherentes sin convertir la marca en una colección de categorías comerciales o productos oportunistas.

Durante la validación de Method v2 apareció además una distinción que debía formalizarse:

```text
BRAND FIT
¿Queremos que nuestra marca venda este producto?

METHOD V2
¿Existe realmente un negocio defendible alrededor de este producto?
```

Ambas preguntas son necesarias y no deben mezclarse.

La exploración inicial de una posible marca asociada a sustentabilidad mostró que territorios como:

- `eco`;
- `smart home`;
- `hogar saludable`;
- `tecnología útil`;

pueden ser demasiado amplios, demasiado restrictivos o inducir justificaciones artificiales.

Las pruebas de frontera mostraron mejores resultados al organizar el portfolio alrededor de **misiones y problemas**.

## 2. Decisión

Se decide:

1. adoptar un **Brand System reusable** para Smart Imports;
2. organizar cada marca mediante:
   ```text
   Brand
   → Brand Territory
   → Missions
   → Problems
   → Solutions
   → Brand Candidate Screening
   → Method v2
   ```
3. organizar el portfolio por misiones y problemas, no por categorías comerciales;
4. utilizar `Marca Hogar` como primera implementación real del sistema;
5. mantener por ahora `Marca Hogar` centrada en el hogar para evitar una expansión excesiva del territorio;
6. utilizar como descriptor interno:
   ```text
   Un hogar que funciona mejor.
   ```
   sin tratarlo como nombre comercial ni slogan definitivo;
7. adoptar `Brand Candidate Screening v0.1` como primera forma operativa del futuro `Brand Product Filter`, previa a Method v2;
8. mantener separados Brand Fit y atractivo comercial;
9. permitir que productos fuera de una marca permanezcan como conocimiento u oportunidades potenciales de Smart Imports;
10. diseñar el sistema para que pueda reutilizarse en futuras marcas con territorios propios, utilizando `Mundo Fitness` como ejemplo conceptual de reusabilidad;
11. no modificar por esta decisión `matrix-aut36`, `full-matrix-v5 0.7.0` ni Matrix Validator v0.1.0;
12. registrar necesidades futuras de modelo de datos y RAG sin implementarlas automáticamente.

## 3. Justificación

### 3.1 Las categorías no construyen identidad

Una organización basada en:

```text
Mascotas
Cocina
Smart Home
Electrodomésticos
```

replica taxonomías comerciales, pero no explica qué representa la marca.

### 3.2 Las misiones sobreviven al cambio de tecnología

Una misión como:

```text
Usar mejor los recursos
```

puede mantenerse aunque cambien:

- dispositivos;
- tecnologías;
- proveedores;
- arquitecturas;
- categorías de marketplace.

### 3.3 El sistema permite portfolios transversales coherentes

Productos comercialmente distintos pueden pertenecer a una misma marca cuando resuelven problemas compatibles con una misión.

Ejemplo:

```text
detector de fugas
+ purificador de aire
+ compostera
+ monitor energético
```

La coherencia proviene del problema y la misión, no de la categoría.

### 3.4 La marca no sustituye Method v2

Un candidato puede tener alto Brand Fit y fallar por:

- Demanda;
- Competencia;
- origen;
- Headroom;
- Landed Cost;
- riesgo;
- operación.

También puede existir una oportunidad comercial fuerte fuera del territorio de una marca.

### 3.5 El sistema es reusable

El valor metodológico no depende de Hogar.

Una futura marca del `Mundo Fitness`, por ejemplo, podría definir misiones como:

```text
entrenar
recuperar
medir
progresar
sostener el hábito
```

y utilizar después el mismo Brand Candidate Screening y Method v2.

## 4. Consecuencias

### Positivas

- mayor coherencia de portfolio;
- menor riesgo de convertirse en un importador de gadgets sin identidad;
- capacidad de rechazar oportunidades que no pertenecen a una marca;
- reusabilidad del método para múltiples marcas;
- mejor separación entre estrategia de marca e inteligencia comercial;
- futura capacidad de consultas RAG cruzando Brand Fit y Method v2.

### Costos y riesgos

- el territorio necesita versionado y revisión;
- las misiones pueden requerir ajustes con experiencia real;
- una definición demasiado amplia puede perder poder de exclusión;
- una definición demasiado estrecha puede perder buenas oportunidades;
- se requiere disciplina para no convertir cada beneficio accesorio en una justificación de Brand Fit.

## 5. Primera implementación

`Marca Hogar v0.1` se define en `SI-BRAND-001`.

Misiones iniciales:

1. mejorar las condiciones del hogar;
2. usar mejor los recursos;
3. reducir y gestionar residuos;
4. resolver problemas domésticos recurrentes conectados con el núcleo.

## 6. Primer screening

`BRAND-CAND-001`:

```text
Sistema doméstico de detección de fugas de agua con corte automático
```

Resultado:

```text
PASS TO METHOD V2
```

El detalle se conserva en `SI-BRAND-002`.

## 7. Relación con Matrix / Engine

Esta decisión no autoriza cambios sobre:

```text
Application: Matrix Validator v0.1.0
Schema: full-matrix-v5 0.7.0
Technical baseline: aut32
Commercial snapshot: aut36
```

Las futuras necesidades de modelado de:

- Brand;
- Brand Territory;
- Mission;
- Problem;
- Solution;
- Brand Fit;
- Brand Relevance;
- Brand Credibility;

se registrarán conceptualmente hasta que exista evidencia suficiente para Matrix vNext o para el modelo persistente del Intelligence Engine.

## 8. Documentos relacionados

- [SI-BRAND-001 — Brand System reutilizable y Marca Hogar](../07-brand/si-brand-001-reusable-brand-system-and-home-territory.md)
- [SI-BRAND-002 — Brand Candidate Screening](../07-brand/si-brand-002-brand-candidate-screening-method.md)
- [SI-ROADMAP-002 — Estado actual y handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-015 — Adoptar aut36 y validar Method v2](./si-decision-015-adopt-aut36-and-validate-method-v2-through-landed-cost-screen.md)

## 9. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-16 | Se adopta Brand System reusable, arquitectura por misiones y Brand Candidate Screening previo a Method v2. |
