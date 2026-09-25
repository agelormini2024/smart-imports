---
id: si-research-025
title: BRAND-CAND-003 — Method v2 Agile — F11 Landed Cost Screen
description: Cierre público del Landed Cost Screen decision-grade de BRAND-CAND-003.
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
  - phase-11
---

# BRAND-CAND-003 — Method v2 Agile — F11 Landed Cost Screen

Estado: `CLOSED`

## 1. Objetivo

F11 transforma el dataset de origen/logística en escenarios comparables de `Economic Landed Cost`.

```text
LANDED COST SCREEN
≠ COTIZACIÓN FINAL
≠ TOTAL CASH OUTLAY
≠ PRODUCT SELECTION
```

## 2. Correcciones metodológicas relevantes

Antes de calcular se corrigieron dos fricciones:

1. los escenarios de primera tanda deben usar comparables de costo compatibles con el MOQ efectivo del escenario;
2. el flete aéreo debe usar `chargeable weight`, considerando peso físico y peso volumétrico.

Este segundo punto fue material para los purificadores de mayor volumen físico.

## 3. Resultado por Product Base

```text
BASE-HOGAR-009
→ ECONOMY BELOW TARGET
→ el volumen físico y el flete aéreo deterioran la estructura

BASE-HOGAR-010
→ ECONOMY OBJECTIVE MET
→ estructura suficiente bajo el screen decision-grade

BASE-HOGAR-011
→ ECONOMY STRONGLY BELOW TARGET
→ además conserva gates técnicos y de safety
```

F11 no decide todavía STOP/PASS final. Esa interpretación corresponde a F12.

## 4. Aprendizaje estructural

```text
CHEAP FACTORY PRICE
≠ GOOD IMPORT ECONOMICS
```

En esta familia:

```text
PHYSICAL VOLUME
→ CHARGEABLE WEIGHT
→ FREIGHT BURDEN
→ COMMERCIAL VIABILITY
```

La logística pasa a ser una dimensión comercial estructural, no un ajuste menor.

## 5. Supuestos

Se preservó la estructura decision-grade de la Golden Run: flete aéreo proxy, seguro, derecho como working assumption, tasa estadística, despachante, cargos de origen, logística local y TCA.

NCM, derechos definitivos, intervenciones y costos finales requieren revisión profesional externa.

## 6. Materialización y validación

```text
MATRIX
matrix-aut56-brand-cand-003-phase11-corrected.xlsx

SHA-256
a4b18664cb8133c94081af0ba259dc911acf08a0ad00b60cefaef54dd81a800f

RESULT
PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

## 7. Cierre

```text
F11 CLOSED
→ F12 — Margin + ROI
```

## 8. Confidencialidad

Las simulaciones numéricas completas y los inputs comerciales sensibles permanecen en la matriz privada.
