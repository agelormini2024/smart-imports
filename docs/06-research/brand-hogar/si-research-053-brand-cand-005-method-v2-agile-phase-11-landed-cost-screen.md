---
id: si-research-053
title: BRAND-CAND-005 — Method v2 Agile — Fase 11 — Landed Cost Screen
description: Screening decision-grade de Landed Cost para las Product Bases activas de BRAND-CAND-005.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-30
updated: 2026-09-30
brand: brand-hogar
brand_candidate: brand-cand-005
method: method-v2-agile
phase: F11
---

# SI-RESEARCH-053 — BRAND-CAND-005 — Method v2 Agile — Fase 11 — Landed Cost Screen

## Estado

- Brand Candidate: `BRAND-CAND-005 — Compostaje / procesamiento doméstico de residuos orgánicos`
- Fase: `F11 — Landed Cost Screen`
- Input validado: `matrix-aut86-brand-cand-005-phase10.xlsx`
- SHA-256 input: `2271556ff168dbaeb35c2d78094590443ef584ed60560e9756732f82008102a0`
- F10: `CLOSED — VALIDATOR PASS`
- Output materializado: `matrix-aut88-brand-cand-005-phase11-derived-view-fix.xlsx`
- SHA-256 output: `6ed7aef02997e1a993fa745f6f618525675ff28cd7242160ae310e35cc8ad51b`
- Validator output: `PASS — 0 errors / 0 warnings / 0 info / 0 limitations`
- Estado F11: `CLOSED — VALIDATOR PASS`

### Corrección de materialización

`aut87` fue ejecutado contra Matrix Validator y devolvió `FAIL` con 20 errores `DERIVED_VIEW_FORMULA_REQUIRED`, todos concentrados en `Resumen Margen Vista!A20:T20`. La fila `RES-MARG-0019` contenía valores materializados en la vista derivada en lugar de las fórmulas de proyección requeridas desde `Resumen Margen`. No se detectó un problema en los escenarios `MARG-0031..MARG-0037` ni en la lógica económica de F11.

`aut88` corrigió exclusivamente esa materialización: restauró las 20 fórmulas de proyección con el mismo patrón usado por las filas anteriores. La corrección obtuvo `PASS` local limpio y F11 quedó formalmente `CLOSED`.
- F12: `OPENED AFTER F11 PASS`

## 1. Objetivo

F11 transforma el dataset mínimo decision-grade de F10 en un **Economic Landed Cost Screen** comparable. No busca una liquidación aduanera definitiva ni una cotización logística ejecutable.

Reglas de lectura:

```text
HEADROOM ≠ LANDED COST ≠ MARGIN
ECONOMIC LANDED COST ≠ TOTAL CASH OUTLAY
AIR STRESS SCREEN ≠ LOGISTICS PLAN
PUBLIC PRICE ≠ FORMAL QUOTE
DECISION-GRADE ≠ PROCUREMENT-GRADE
ECONOMIC FIT ≠ GOOD FIRST PRODUCT
```

F11 tampoco decide `STOP / PASS / FINALIST`; esa interpretación corresponde a F12 y fases posteriores.

## 2. Baseline y método conservado

Para comparabilidad transversal con los Brand Candidates anteriores se conserva la baseline histórica del proyecto:

```text
FX comparison baseline        ARS/USD 1.535
channel cost                  25%
commercial cost                5%
target margin                 25% del precio neto
max economic landed          51,25% del precio bruto
```

El FX 1.535 es una **baseline histórica de proyecto**, no una cotización actual.

Modelo F11:

```text
chargeable weight = max(peso físico, CBM × 167)
air freight proxy = USD 10/kg de chargeable weight
insurance = 0,5% × (origin cost + air freight)
CIF screen = origin cost + air freight + insurance
import duty = 18% × CIF        — WORKING ASSUMPTION hasta NCM
tasa estadística = 3% × CIF
despachante = 5% × CIF
origin normalization = USD 150 / embarque
local logistics = USD 100 / embarque
TCA flat = banda oficial según peso físico del embarque
```

La columna legacy `Costo FOB USD` de `Simulación Margen` se usa como **costo de origen de referencia**; no transforma automáticamente un precio público en Incoterm FOB confirmado.

## 3. TCA aplicado

Se usa el tarifario oficial ya registrado como `SRC-0359 / EXT-0035`. Las bandas relevantes para estos escenarios son:

| Peso físico del embarque | TCA flat USD |
|---:|---:|
| >200–350 kg | 381,16 |
| >500–750 kg | 622,56 |
| >1.000–1.500 kg | 880,22 |
| >4.000–5.000 kg | 1.916,92 |

El TCA se aplica sobre **peso físico**, no sobre chargeable weight.

## 4. Escenarios materializados

### BASE-HOGAR-024 — Compostera modular apilable 40–60 L

Inputs:

- costo/MOQ: `COT-0054` — USD 24,29; tier público 50–499;
- logística: `COT-0060` — same-model downstream proxy `WB25101`;
- proxy unitario: 5,1 kg; 0,0656 m³;
- venta local de referencia: `ML-0143` — ARS 94.558;
- costo puesto económico máximo: ~USD 31,57/u.

Resultados:

| MARG | Unidades | Ejecutable con dato público | Peso físico kg | Chargeable kg | TCA USD | Economic LC USD/u | Margen mecánico |
|---|---:|---|---:|---:|---:|---:|---:|
| MARG-0031 | 50 | Sí | 255,00 | 547,76 | 381,16 | 182,11 | -300,83% |
| MARG-0032 | 100 | Sí | 510,00 | 1.095,52 | 622,56 | 178,21 | -292,39% |

Lectura F11: el **peso volumétrico domina**. La escala diluye costos fijos, pero no modifica la estructura bajo aéreo. No se concluye que el PB sea inviable con cualquier logística: LCL/ocean, nesting real y supplier packing no se modelan aquí.

### BASE-HOGAR-025 — Compostera giratoria 120 L — doble cámara

Inputs:

- `COT-0056` — USD 28,80 para **439–910 unidades**;
- packing same-listing: 62 × 56 × 20 cm; 11 kg; 1 unidad;
- venta local de referencia: `ML-0140` — ARS 188.340;
- costo puesto económico máximo: ~USD 62,88/u.

Se preservan 50/100 unidades sólo como sensibilidad transversal y se incorpora obligatoriamente el MOQ 439:

| MARG | Unidades | Estado comercial | Peso físico kg | Chargeable kg | TCA USD | Economic LC USD/u | Margen mecánico |
|---|---:|---|---:|---:|---:|---:|---:|
| MARG-0033 | 50 | **NON-EXECUTABLE AT PUBLIC MOQ** | 550 | 579,824 | 622,56 | 200,77 | -124,84% |
| MARG-0034 | 100 | **NON-EXECUTABLE AT PUBLIC MOQ** | 1.100 | 1.159,648 | 880,22 | 194,62 | -118,16% |
| MARG-0035 | 439 | **EXECUTABLE AT PUBLIC MOQ/TIER** | 4.829 | 5.090,855 | 1.916,92 | 188,25 | -111,24% |

Lectura F11: aun en MOQ 439 el escenario aéreo es fuertemente negativo. En este tamaño, el aéreo se interpreta como **stress screen**, no como recomendación logística. Un escenario marítimo/LCL podría modificar materialmente la estructura y queda fuera de F11.

### BASE-HOGAR-028 — Procesador eléctrico térmico countertop 3–4 L

Inputs:

- `COT-0058` — USD 140;
- MOQ conservador: 100;
- packing conservador F10: 11,5 kg; 0,068224 m³;
- venta local de referencia: `ML-0149` — ARS 1.101.000;
- costo puesto económico máximo: ~USD 367,60/u.

| MARG | Unidades | Estado comercial | Peso físico kg | Chargeable kg | TCA USD | Economic LC USD/u | Margen mecánico | ROI mecánico |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| MARG-0036 | 50 | **NON-EXECUTABLE AT PUBLIC MOQ** | 575 | 575 | 622,56 | 340,36 | 30,06% | 47,52% |
| MARG-0037 | 100 | **EXECUTABLE AT PUBLIC MOQ** | 1.150 | 1.150 | 880,22 | 334,21 | 31,21% | 50,23% |

Lectura F11: el escenario ejecutable de 100 unidades **cumple mecánicamente** el objetivo económico bajo este screen. Esto no elimina las condiciones técnicas y de servicio heredadas de F10: 220–240V/50Hz exacto, filtros/repuestos, documentación de certificaciones, garantía/postventa y disciplina de claims sobre el output.

## 5. Síntesis

Se materializan **7 escenarios**, de los cuales **4 son ejecutables** con los datos públicos usados:

```text
BASE-HOGAR-024  50 u   EXECUTABLE
BASE-HOGAR-024 100 u   EXECUTABLE
BASE-HOGAR-025 439 u   EXECUTABLE
BASE-HOGAR-028 100 u   EXECUTABLE
```

Los restantes (`025/50`, `025/100`, `028/50`) son sensibilidad y quedan explícitamente marcados `NON-EXECUTABLE AT PUBLIC MOQ`.

Resultado descriptivo F11:

- `BASE-HOGAR-024`: estructura aérea fuertemente negativa por volumetría.
- `BASE-HOGAR-025`: estructura aérea fuertemente negativa incluso al MOQ público 439; el modo logístico es una variable estructural.
- `BASE-HOGAR-028`: estructura económica suficiente en 100 unidades bajo el screen, con condiciones técnicas/postventa todavía abiertas.

F11 **no emite decisión final por Product Base**. La interpretación formal queda reservada a F12.

## 6. Trazabilidad incorporada en aut88

```text
MARG-0031 .. MARG-0037
RES-MARG-0019
SRC-0475
EVID-0280
EVSRC-0616 .. EVSRC-0622
```

No se creó una evaluación formal nueva (`EVAL-0026` permanece disponible) porque F11 no agrega un criterio de scoring.

## 7. Fuentes reutilizadas

- `SRC-0358 / EXT-0034` — proxy de flete aéreo China → Argentina.
- `SRC-0359 / EXT-0035` — Terminal de Cargas Argentina, Precio Flat: https://www.aeropuertosargentinacargas.com.ar/precios.aspx
- `SRC-0360 / EXT-0036` — tasa de estadística: https://www.argentina.gob.ar/normativa/nacional/norma-407914
- `SRC-0361 / EXT-0037` — referencia base CIF / import tariffs: https://www.trade.gov/country-commercial-guides/argentina-import-tariffs
- `SRC-0362 / EXT-0038` — proxy de honorarios de despachante: https://www.estudiotalamo.com/blog/cuanto-cobra-despachante-aduana-argentina-2026
- `SRC-0474 / EVID-0279` — F10 Minimum Landed Cost Dataset.
- `SRC-0475 / EVID-0280` — consolidado interno F11.

## 8. Checkpoint y próxima acción

```text
CONCEPTUAL ANALYSIS      COMPLETE
MATRIX MATERIALIZATION  COMPLETE — aut88
MATRIX VALIDATOR        PASS — aut88 / 0 errors / 0 warnings / 0 info / 0 limitations
DOCUMENTARY CHECKPOINT  COMPLETE
F11                     CLOSED
F12                     OPENED AFTER PASS
```

`aut88` obtuvo `PASS` limpio. F11 quedó cerrada y F12 se abrió sobre `MARG-0031..MARG-0037`, preservando los execution flags sin recalcular Landed Cost ni reabrir sourcing.
