---
id: si-research-026
title: BRAND-CAND-003 — Method v2 Agile — F12 Margin + ROI
description: Interpretación pública de margen y ROI sobre los escenarios F11.
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
  - phase-12
---

# BRAND-CAND-003 — Method v2 Agile — F12 Margin + ROI

Estado: `CLOSED`

## 1. Objetivo

F12 interpreta los escenarios de F11; no recalcula Landed Cost.

```text
F11 = CALCULATION
F12 = INTERPRETATION
```

El margen objetivo se mantiene alineado con la Golden Run. ROI sobre costo económico es complementario y no funciona como un segundo gate independiente.

## 2. Resultado

### BASE-HOGAR-009

```text
MARGIN
→ NEGATIVE IN BOTH SCENARIOS

F12
→ STOP — REOPENABLE
```

Reabrir sólo ante un cambio estructural en packing/volumen, costo, precio defendible o modo logístico.

### BASE-HOGAR-010

```text
MARGIN
→ OBJECTIVE MET IN BOTH SCENARIOS

F12
→ PASS TO F13 — CONDITIONED
```

La condición principal sigue siendo técnica/comercial:

```text
CARBON PRESENT
≠ MATERIAL SORBENT VALIDATED
```

También permanecen filtros/repuestos, compatibilidad eléctrica, claims y revisión externa.

### BASE-HOGAR-011

```text
MARGIN
→ STRONGLY NEGATIVE IN BOTH SCENARIOS

F12
→ STOP — REOPENABLE
```

Su reapertura requiere mejorar la estructura económica **y** resolver safety, ozone/subproductos y claims.

## 3. Funnel posterior a F12

```text
BASE-HOGAR-009 → STOP — REOPENABLE
BASE-HOGAR-010 → PASS TO F13 — CONDITIONED
BASE-HOGAR-011 → STOP — REOPENABLE
```

Shortlist activa:

```text
BASE-HOGAR-010
```

## 4. Materialización y validación

```text
MATRIX
matrix-aut57-brand-cand-003-phase12.xlsx

SHA-256
95f4a0ba926d1ea1f4fa188cd324044dc817b44831bcd5f3009e9fe649179057

RESULT
PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

## 5. Cierre

```text
F12 CLOSED
→ F13 — Shortlist final
→ BASE-HOGAR-010 only
```

## 6. Confidencialidad

Los porcentajes y simulaciones comerciales completos permanecen en la matriz operativa privada. El repositorio público conserva la decisión y sus razones.
