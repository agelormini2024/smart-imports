---
id: si-research-024
title: BRAND-CAND-003 — Method v2 Agile — F10 Minimum Landed Cost Dataset
description: Cierre público del dataset mínimo decision-grade previo al Landed Cost Screen.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-25
updated: 2026-09-25
phase: business-intelligence
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-003
  - indoor-air
  - phase-10
---

# BRAND-CAND-003 — Method v2 Agile — F10 Minimum Landed Cost Dataset

Estado: `CLOSED`

## 1. Objetivo

F10 responde:

> ¿Existe un dataset mínimo suficientemente defendible para abrir F11 sin esperar precisión procurement-grade?

```text
DECISION-GRADE
≠ PROCUREMENT-GRADE
```

## 2. Calidad del dataset por Product Base

### BASE-HOGAR-009

```text
COST
→ PUBLIC_CONFIRMED

LOGISTICS
→ COMPOSITE_PROXY

QUALITY
→ MEDIA
```

El costo y la logística proceden de comparables públicos del mismo Product Base, no del mismo SKU.

### BASE-HOGAR-010

```text
COST + LOGISTICS
→ PUBLIC_CONFIRMED / SAME-SKU para el benchmark principal de F10

QUALITY
→ MEDIA/ALTA
```

Permanece abierto el gate de materialidad/capacidad del sorbente y el Incoterm exacto.

### BASE-HOGAR-011

```text
COST + LOGISTICS
→ PUBLIC_CONFIRMED / SAME-SKU

QUALITY
→ MEDIA/ALTA

ELIGIBILITY
→ HIGHLY CONDITIONED
```

La calidad económica/logística del dataset no resuelve ozone-free, subproductos, disableability ni safety.

## 3. Principio operativo

La fase confirma:

```text
SUPPLIER RESPONSE
≠ PHASE PROGRESS
```

El contacto directo enriquece el dataset, pero no debe bloquear el camino crítico cuando existe evidencia pública suficiente para una decisión preliminar.

## 4. Materialización y validación

```text
MATRIX
matrix-aut55-brand-cand-003-phase10.xlsx

SHA-256
b29bf6e8a6922246dffbaeca83aa2580f64aa1c96f352c6048483abda16a447e

RESULT
PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

## 5. Cierre

```text
F10 CLOSED
→ F11 — Landed Cost Screen
```

## 6. Confidencialidad

Los precios, condiciones de compra y datos sensibles quedan en la matriz operativa privada. El repositorio público conserva calidad de evidencia, gaps y decisión metodológica.
