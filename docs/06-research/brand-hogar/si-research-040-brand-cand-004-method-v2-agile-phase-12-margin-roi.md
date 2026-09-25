---
id: si-research-040
title: BRAND-CAND-004 — Method v2 Agile — F12 Margin + ROI
description: Interpretación formal de margen y ROI para los escenarios de landed cost de monitoreo doméstico del consumo energético.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-25
updated: 2026-09-25
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-004
  - energy-monitoring
  - phase-12
  - margin
  - roi
related:
  - si-research-039
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F12 Margin + ROI

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input

F11 quedó formalmente cerrada sobre:

```text
matrix-aut70-brand-cand-004-phase11-corrected.xlsx
SHA-256: d7456f1902788ea85624c90f191c96bf1f48a7f5c6560c859294c6603e8c8f29
Result: PASS
```

F12 interpreta, sin recalcular landed cost:

```text
MARG-0025 … MARG-0030
```

## 2. Regla

```text
MARGIN POSITIVE ≠ PRODUCT READY
ROI SOBRE COSTO ECONÓMICO ≠ ROI TOTAL DEL NEGOCIO
ECONOMÍA SUFICIENTE ≠ ELEGIBILIDAD TOTAL
```

Indicador primario:

```text
Margen % sobre precio neto
```

Indicador complementario:

```text
ROI sobre Economic Landed Cost
```

Objetivo económico:

```text
Margen ≥ 25% del precio neto
```

## 3. BASE-HOGAR-016 — plug-level standalone

### 50 unidades — MARG-0025

```text
Economic LC     USD 17.19
Margen          USD 14.73/u
Margen %        43.06%
ROI             85.66%
```

### 100 unidades — MARG-0026

```text
Economic LC     USD 12.23
Margen          USD 19.69/u
Margen %        57.57%
ROI             161.00%
```

Resultado:

```text
PASS TO F13 — CONDITIONED
```

Cumple el objetivo económico en ambos escenarios.

Condiciones abiertas:

```text
accuracy / test evidence
plug Argentina/AU exacto
packing same-SKU
certificación / requisitos locales
revisión externa
```

## 4. BASE-HOGAR-017 — smart plug + monitoring

### 50 unidades — MARG-0027

```text
Economic LC     USD 16.69
Margen          USD -6.65/u
Margen %        -61.91%
ROI             -39.88%
```

### 100 unidades — MARG-0028

```text
Economic LC     USD 13.62
Margen          USD -3.59/u
Margen %        -33.41%
ROI             -26.36%
```

Resultado:

```text
STOP — REOPENABLE
```

El bajo costo de origen no compensa ticket local, costos fijos y logística en los escenarios modelados.

Sólo se reabre ante un cambio estructural de costo, escala/consolidación, precio defendible, arquitectura comercial o diferenciación material.

## 5. BASE-HOGAR-019 — DIN direct meter

### 50 unidades — MARG-0029

```text
Economic LC     USD 15.10
Margen          USD -3.08/u
Margen %        -23.95%
ROI             -20.42%
```

### 100 unidades — MARG-0030

```text
Economic LC     USD 12.21
Margen          USD -0.19/u
Margen %        -1.49%
ROI             -1.57%
```

Resultado:

```text
STOP — REOPENABLE
```

A 100 unidades se aproxima al break-even, pero no alcanza el margen objetivo.

Además siguen abiertos:

```text
safety
accuracy / class
certificación
instalación profesional
```

## 6. Resultado consolidado

| Product Base | Margen 50 u | Margen 100 u | ROI 50 u | ROI 100 u | F12 |
|---|---:|---:|---:|---:|---|
| BASE-HOGAR-016 | 43.06% | 57.57% | 85.66% | 161.00% | PASS TO F13 — CONDITIONED |
| BASE-HOGAR-017 | -61.91% | -33.41% | -39.88% | -26.36% | STOP — REOPENABLE |
| BASE-HOGAR-019 | -23.95% | -1.49% | -20.42% | -1.57% | STOP — REOPENABLE |

## 7. Funnel después de F12

```text
ACTIVE FOR F13
→ BASE-HOGAR-016

STOP — REOPENABLE
→ BASE-HOGAR-017
→ BASE-HOGAR-019
```

F12 no elige proveedor ni producto final.

## 8. Gate F12

Resultado conceptual:

```text
PASS
```

F13 debe evaluar únicamente `BASE-HOGAR-016` e integrar:

```text
economía
+ Brand Fit
+ calidad de evidencia
+ complejidad
+ condiciones técnicas
```

sin abrir F14.

## 9. Materialización

F12 agrega:

```text
EVID-0267
SRC-0443
EVSRC-0560
RES-MARG-0017
```

y actualiza las notas de `BASE-HOGAR-016`, `017` y `019`.

Archivo preparado:

```text
matrix-aut71-brand-cand-004-phase12.xlsx
SHA-256: 7a19864d60fff48ef5a8f0a71b00866700b1d9de25f0c28cd437a2fc8b8c1b24
```

## 10. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut71
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F12 CLOSED
```

F13 no se declara formalmente abierta hasta obtener PASS limpio del Matrix Validator.

## 11. Próxima acción

F12 queda `CLOSED`. Ejecutar `F13 — Final Shortlist` en modalidad `AUTO` sólo con `BASE-HOGAR-016`.

## 12. Changelog

### 2026-09-25 — v0.1.0

- F11 queda formalmente cerrada sobre `aut70 corrected PASS`;
- F12 interpreta `MARG-0025..0030` sin recalcular landed cost;
- `BASE-HOGAR-016` pasa a F13 — CONDITIONED;
- `BASE-HOGAR-017` queda STOP — REOPENABLE;
- `BASE-HOGAR-019` queda STOP — REOPENABLE;
- se agrega `RES-MARG-0017`;
- se prepara `matrix-aut71-brand-cand-004-phase12.xlsx`;
- F12 queda pendiente del Matrix Validator.


## Validación oficial F12

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: 7a19864d60fff48ef5a8f0a71b00866700b1d9de25f0c28cd437a2fc8b8c1b24
```
