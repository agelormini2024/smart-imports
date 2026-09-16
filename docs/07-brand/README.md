---
id: docs-07-brand-readme
title: 07 — Brand
description: Índice de documentación del Brand System de Smart Imports y sus implementaciones de marca.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-09-16
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

## 1. Propósito

Esta sección documenta el sistema de construcción de marcas y portfolios de Smart Imports.

El objetivo no es limitarse a identidad visual, naming o comunicación. La marca se trata como una capa estratégica que define:

- territorio;
- misiones;
- problemas;
- soluciones;
- criterios de pertenencia al portfolio;
- relación entre Brand Fit y evaluación comercial.

## 2. Principio rector

Smart Imports adopta una arquitectura basada en:

```text
BRAND
→ BRAND TERRITORY
→ MISSIONS
→ PROBLEMS
→ SOLUTIONS
→ BRAND CANDIDATE SCREENING
→ METHOD V2
```

El sistema es deliberadamente reutilizable.

`Marca Hogar` es la primera implementación real, pero el mismo marco debe poder aplicarse a futuras marcas con territorios y misiones diferentes, por ejemplo una eventual marca del `Mundo Fitness`.

## 3. Documentos vigentes

| Documento | Propósito |
|---|---|
| [SI-BRAND-001 — Brand System reutilizable y territorio de Marca Hogar](./si-brand-001-reusable-brand-system-and-home-territory.md) | Define el marco reusable de marca y su primera implementación sobre Hogar. |
| [SI-BRAND-002 — Brand Candidate Screening](./si-brand-002-brand-candidate-screening-method.md) | Define cómo una solución es evaluada antes de ingresar a Method v2. |
| [SI-DECISION-016 — Arquitectura de marca por misiones](../09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md) | Formaliza la decisión metodológica. |

## 4. Separación fundamental

```text
BRAND FIT
¿Queremos que nuestra marca venda este producto?

METHOD V2
¿Existe realmente un negocio defendible alrededor de este producto?
```

Un alto Brand Fit no implica atractivo comercial.

Un producto comercialmente atractivo puede quedar fuera del territorio de una marca concreta.

## 5. Estado

Al 2026-09-16:

- `Brand System v0.1`: definido para validación práctica.
- `Marca Hogar v0.1`: primer territorio aplicado.
- `Brand Candidate Screening v0.1`: operativo.
- `BRAND-CAND-001`: aprobado para pasar a Method v2.
- matriz, schema y Matrix Validator: sin cambios por este frente.

## 6. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Placeholder inicial. |
| 0.2.0 | 2026-09-16 | Se incorpora Brand System, Marca Hogar y Brand Candidate Screening como nueva capa estratégica reusable. |
