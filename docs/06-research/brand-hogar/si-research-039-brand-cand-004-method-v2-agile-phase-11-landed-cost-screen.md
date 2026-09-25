---
id: si-research-039
title: BRAND-CAND-004 — Method v2 Agile — F11 Landed Cost Screen
description: Screening decision-grade de Economic Landed Cost para los Product Bases activos de monitoreo doméstico del consumo energético.
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
  - phase-11
  - landed-cost
related:
  - si-research-028
  - si-research-029
  - si-research-030
  - si-research-031
  - si-research-032
  - si-research-033
  - si-research-034
  - si-research-035
  - si-research-036
  - si-research-037
  - si-research-038
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F11 Landed Cost Screen

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input

F10 quedó formalmente cerrada sobre:

```text
matrix-aut69-brand-cand-004-phase10-corrected.xlsx
SHA-256: 5707b57c230246ead43d0f0198174cdc5380e8a6d77802fe33bbafcd34d9903e
Result: PASS
```

PB activos: `BASE-HOGAR-016`, `BASE-HOGAR-017`, `BASE-HOGAR-019`.

## 2. Regla económica

```text
HEADROOM ≠ LANDED COST ≠ MARGIN
ECONOMIC LANDED COST ≠ TOTAL CASH OUTLAY
```

F11 modela costo económico unitario. La interpretación formal de margen y ROI corresponde a F12.

## 3. Supuestos comunes

```text
air freight proxy          USD 10/kg
chargeable weight          max(peso físico, CBM × 167)
insurance                  0,5%
import duty                18% — WORKING ASSUMPTION
statistical rate            3%
customs broker              5% CIF
origin normalization       USD 150 / shipment
local logistics            USD 100 / shipment
TCA flat                   official weight band / physical kg
FX comparison baseline     ARS/USD 1.535
```

El FX 1.535 es baseline histórica del proyecto, no FX actual.

## 4. TCA aplicado

```text
> 5–10 kg   → USD 71,14
>10–20 kg   → USD 103,14
>20–50 kg   → USD 149,93
```

El flat depende del peso físico, no del chargeable weight.

## 5. BASE-HOGAR-016

### 50 unidades — MARG-0025

```text
origin cost       USD 5,50/u — COT-0051 low-MOQ
gross weight      12,50 kg
CBM               0,0648
volumetric        10,82 kg
chargeable        12,50 kg
TCA               USD 103,14
Economic LC       USD 17,19/u
Max economic LC   USD 23,37/u
```

### 100 unidades — MARG-0026

```text
origin cost       USD 4,00/u — COT-0052
gross weight      25,00 kg
CBM               0,1296
volumetric        21,64 kg
chargeable        25,00 kg
TCA               USD 149,93
Economic LC       USD 12,23/u
Max economic LC   USD 23,37/u
```

Lectura F11: `LC BELOW MAX ECONOMIC LANDED` en ambos escenarios.

## 6. BASE-HOGAR-017

### 50 unidades — MARG-0027

```text
origin cost       USD 4,60/u
gross weight      15,00 kg
CBM               0,0400
chargeable        15,00 kg
TCA               USD 103,14
Economic LC       USD 16,69/u
Max economic LC   USD 7,34/u
```

### 100 unidades — MARG-0028

```text
origin cost       USD 4,60/u
gross weight      30,00 kg
CBM               0,0800
chargeable        30,00 kg
TCA               USD 149,93
Economic LC       USD 13,62/u
Max economic LC   USD 7,34/u
```

Lectura F11: `LC ABOVE MAX ECONOMIC LANDED` en ambos escenarios.

## 7. BASE-HOGAR-019

### 50 unidades — MARG-0029

```text
origin cost       USD 5,60/u
gross weight       6,25 kg
CBM               0,0144
chargeable         6,25 kg
TCA               USD 71,14
Economic LC       USD 15,10/u
Max economic LC   USD 8,80/u
```

### 100 unidades — MARG-0030

```text
origin cost       USD 5,60/u
gross weight      12,50 kg
CBM               0,0288
chargeable        12,50 kg
TCA               USD 103,14
Economic LC       USD 12,21/u
Max economic LC   USD 8,80/u
```

Lectura F11: `LC ABOVE MAX ECONOMIC LANDED` en ambos escenarios.

## 8. Resultado consolidado

| Product Base | 50 u LC | 100 u LC | Max economic LC | Lectura F11 |
|---|---:|---:|---:|---|
| BASE-HOGAR-016 | USD 17,19 | USD 12,23 | USD 23,37 | BELOW MAX |
| BASE-HOGAR-017 | USD 16,69 | USD 13,62 | USD 7,34 | ABOVE MAX |
| BASE-HOGAR-019 | USD 15,10 | USD 12,21 | USD 8,80 | ABOVE MAX |

F9 preguntaba si existía espacio teórico. F11 muestra cuánto de ese espacio sobrevive a logística, nacionalización y costos fijos.

## 9. Gate F11

```text
PASS TO F12 — CONDITIONED
```

F11 no emite STOP/FINALIST por PB. F12 debe interpretar `MARG-0025..MARG-0030` sin recalcular landed cost.

## 10. Materialización

```text
MARG-0025 … MARG-0030
EVID-0266
SRC-0442
EVSRC-0547 … EVSRC-0559
RES-MARG-0016
```

También se actualizan `EXT-0035 / SRC-0359` con las bandas TCA low-weight usadas.

Archivo preparado:

```text
matrix-aut70-brand-cand-004-phase11-corrected.xlsx
SHA-256: d7456f1902788ea85624c90f191c96bf1f48a7f5c6560c859294c6603e8c8f29
```

### Corrección de materialización aut70

El primer intento de validación detectó exclusivamente errores estructurales de materialización:

```text
RES-MARG-0016
→ faltaba Margen Objetivo % = 25%

Resumen Margen Vista
→ faltaba la fila derivada 17

MARG-0025 … MARG-0030
→ faltaba Fuente Global ID
```

Corrección aplicada:

```text
Resumen Margen!AN17 = 0,25
Resumen Margen Vista!A17:T17 = fórmulas derivadas desde Resumen Margen row 17
Simulación Margen!AD26:AD31 = SRC-0442
```

No se modificaron los cálculos, supuestos, landed costs ni la interpretación conceptual de F11.

## 11. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut70
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F11 CLOSED
```

## 12. Próxima acción

F11 queda `CLOSED`. Ejecutar `F12 — Margin + ROI` en modalidad `AUTO`.

## 13. Changelog

### 2026-09-25 — v0.1.0

- F10 queda formalmente cerrada sobre `aut69 corrected PASS`;
- se modelan seis escenarios 50/100 u;
- se aplica chargeable weight y TCA por peso físico;
- 016 queda debajo del max landed en ambos escenarios;
- 017 y 019 quedan por encima del max landed en ambos escenarios;
- se agregan MARG-0025..0030 y RES-MARG-0016;
- se prepara `matrix-aut70-brand-cand-004-phase11-corrected.xlsx`;
- F11 queda pendiente del Matrix Validator.


## Validación oficial F11

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: d7456f1902788ea85624c90f191c96bf1f48a7f5c6560c859294c6603e8c8f29
```
