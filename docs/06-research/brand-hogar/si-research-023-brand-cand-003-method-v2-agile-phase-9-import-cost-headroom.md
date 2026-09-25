---
id: si-research-023
title: BRAND-CAND-003 — Method v2 Agile — F9 Import Cost Headroom
description: Cierre público de F9 con screening económico preliminar de los Product Bases activos.
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
  - phase-9
---

# BRAND-CAND-003 — Method v2 Agile — F9 Import Cost Headroom

Estado: `CLOSED`

## 1. Objetivo

F9 responde:

> ¿Existe holgura económica preliminar suficiente para justificar reunir un dataset mínimo de Landed Cost?

Regla:

```text
HEADROOM
≠ LANDED COST
≠ MARGIN
```

F9 es un filtro. No estima todavía el costo puesto real y no selecciona proveedor.

## 2. Scope

Entraron al screen:

```text
BASE-HOGAR-009 — HEPA / partículas
BASE-HOGAR-010 — HEPA + sorbente material
BASE-HOGAR-011 — HEPA + tratamiento activo complementario
```

## 3. Resultado

```text
BASE-HOGAR-009
→ SURVIVES
→ señal económica suficiente para justificar F10

BASE-HOGAR-010
→ SURVIVES — STRONG ECONOMIC SIGNAL
→ mejor holgura relativa del scope

BASE-HOGAR-011
→ SURVIVES — HIGHLY CONDITIONED
→ holgura más ajustada y muy sensible a comparabilidad
```

La economía no elimina condiciones técnicas previas.

Para `BASE-HOGAR-010` sigue abierto:

```text
CARBON PRESENT
≠ MATERIAL SORBENT DEMONSTRATED
```

Para `BASE-HOGAR-011` siguen dominando safety, subproductos y disciplina de claims.

## 4. Baseline de comparación

Para preservar comparabilidad transversal con la Golden Run se reutilizó el mismo baseline económico de proyecto y la misma convención de costos comerciales.

El detalle numérico de simulaciones permanece en la matriz operativa privada.

## 5. Materialización y validación

```text
MATRIX
matrix-aut54-brand-cand-003-phase9-corrected.xlsx

SHA-256
06fd11abdb8179fafe22705f6fc38e53d2ae761831ba82db66fc400816f9cc92

VALIDATOR
Matrix Validator 0.1.0
full-matrix-v5 0.7.0

RESULT
PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

## 6. Cierre

```text
F9 CLOSED
→ F10 — Minimum Landed Cost Dataset
```

## 7. Confidencialidad

Este documento conserva metodología, interpretación y estado. No publica cotizaciones privadas completas, objetivos de negociación ni simulaciones comerciales sensibles.
