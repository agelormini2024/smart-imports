---
id: si-research-054
title: BRAND-CAND-005 — Method v2 Agile — Fase 12 — Margin + ROI
description: Interpretación formal de margen y ROI sobre los escenarios decision-grade de BRAND-CAND-005.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-30
updated: 2026-09-30
brand: brand-hogar
brand_candidate: brand-cand-005
method: method-v2-agile
phase: F12
---

# SI-RESEARCH-054 — BRAND-CAND-005 — Method v2 Agile — Fase 12: Margin + ROI

## 1. Objetivo

Interpretar formalmente los escenarios económicos ya materializados en F11 para `BRAND-CAND-005 — Compostaje / procesamiento doméstico de residuos orgánicos`.

F12 **no recalcula Landed Cost** y no agrega supuestos logísticos nuevos.

Reglas de lectura:

```text
MARGIN % SOBRE PRECIO NETO = indicador económico primario
ROI SOBRE COSTO ECONÓMICO = indicador complementario
NON-EXECUTABLE SENSITIVITY ≠ COMMERCIAL SCENARIO
ECONOMIC FIT ≠ GOOD FIRST PRODUCT
STOP — REOPENABLE ≠ ARQUITECTURA INVÁLIDA
```

Margen objetivo vigente del Method v2:

```text
25% sobre precio neto
```

El tipo de cambio `ARS/USD 1.535` se conserva únicamente como **baseline histórica de comparabilidad**. No se presenta como tipo de cambio actual.

---

## 2. Input validado

F12 parte de:

```text
matrix-aut88-brand-cand-005-phase11-derived-view-fix.xlsx
```

F11 quedó validada localmente con:

```text
Matrix Validator: 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: []
SHA-256: 6ed7aef02997e1a993fa745f6f618525675ff28cd7242160ae310e35cc8ad51b
```

Escenarios interpretados:

```text
MARG-0031 .. MARG-0037
```

---

## 3. Execution flags preservados

F12 conserva exactamente la ejecutabilidad definida en F10/F11.

### BASE-HOGAR-024

```text
50 u   → EXECUTABLE al tier público usado
100 u  → EXECUTABLE al tier público usado
```

### BASE-HOGAR-025

```text
50 u   → NON-EXECUTABLE AT PUBLIC MOQ
100 u  → NON-EXECUTABLE AT PUBLIC MOQ
439 u  → EXECUTABLE AT PUBLIC MOQ / TIER
```

El precio de `USD 28,80` de `COT-0056` pertenece al tier público `439–910 u`.

### BASE-HOGAR-028

```text
50 u   → NON-EXECUTABLE al MOQ público conservador
100 u  → EXECUTABLE
```

Por lo tanto, el escenario 50 u de `BASE-HOGAR-028` puede informar sensibilidad, pero **no prueba viabilidad comercial de un lote de 50 unidades**.

---

## 4. Resultados por Product Base

### 4.1 BASE-HOGAR-024 — Compostera modular apilable 40–60 L

Escenarios ejecutables:

| Lote | Margen % | ROI sobre costo | Lectura |
|---:|---:|---:|---|
| 50 u | -300,83% | -76,32% | Negativo |
| 100 u | -292,39% | -75,80% | Negativo |

La escala reduce marginalmente costos fijos por unidad, pero no modifica la conclusión. Bajo el screen aéreo vigente, el peso volumétrico domina la estructura y el Economic Landed Cost queda muy por encima del máximo compatible con el margen objetivo.

Decisión F12:

```text
STOP — REOPENABLE
```

Condición de reapertura:

- modo logístico que cambie materialmente la estructura;
- packing/nesting sustancialmente mejor;
- costo de origen inferior;
- precio local defendible superior;
- o una combinación demostrada de esas variables.

No corresponde negociar para “rescatar” el PB sin una modificación estructural.

---

## 4.2 BASE-HOGAR-025 — Compostera giratoria 120 L — doble cámara

Sensibilidades no ejecutables:

| Lote | Ejecutable | Margen % | ROI |
|---:|---|---:|---:|
| 50 u | NO | -124,84% | -57,22% |
| 100 u | NO | -118,16% | -55,87% |

Escenario comercialmente alineado al dato público:

| Lote | Ejecutable | Margen % | ROI |
|---:|---|---:|---:|
| 439 u | SÍ | -111,24% | -54,38% |

La lectura relevante es el escenario de 439 unidades. Continúa siendo fuertemente negativo bajo aéreo.

F11 ya estableció que el aéreo funciona aquí como **air-stress-screen**, no como plan logístico recomendado. F12 no puede asumir que marítimo/LCL resolverá la economía porque ese escenario todavía no fue modelado.

Decisión F12:

```text
STOP — REOPENABLE / LOGISTICS GATE
```

Condición de reapertura:

```text
packing real
+ modelo marítimo/LCL
+ costos de importación consistentes
→ nuevo escenario decision-grade
```

El headroom favorable detectado en F9 sigue siendo una señal útil, pero:

```text
HEADROOM ≠ LANDED COST
```

---

## 4.3 BASE-HOGAR-028 — Procesador eléctrico térmico countertop 3–4 L

Sensibilidad no ejecutable:

| Lote | Ejecutable | Margen % | ROI |
|---:|---|---:|---:|
| 50 u | NO | 30,06% | 47,52% |

Escenario ejecutable:

| Lote | Ejecutable | Margen % | ROI |
|---:|---|---:|---:|
| 100 u | SÍ | 31,21% | 50,23% |

El escenario de 100 unidades supera el margen objetivo de 25%.

Decisión F12:

```text
PASS TO F13 — CONDITIONED
```

La continuidad es económica, no una aprobación integral del producto.

Permanecen abiertos como condiciones independientes:

- filtros y repuestos;
- disponibilidad y costo de replacements;
- `220–240V / 50Hz` exacto;
- documentación/certificaciones declaradas;
- warranty y service;
- semántica de claims;
- definición correcta del output;
- riesgo de confundir reducción de volumen / deshidratación / molienda con compost terminado.

Regla:

```text
ECONOMIC FIT ≠ GOOD FIRST PRODUCT
```

---

## 5. Resultado consolidado de F12

```text
BASE-HOGAR-024
→ STOP — REOPENABLE

BASE-HOGAR-025
→ STOP — REOPENABLE / LOGISTICS GATE

BASE-HOGAR-028
→ PASS TO F13 — CONDITIONED
```

F12 reduce el funnel económico activo a un solo PB:

```text
BASE-HOGAR-028
```

Esto **no selecciona proveedor**, **no selecciona producto final** y **no abre F14**.

---

## 6. Evidencia y trazabilidad materializada

Nuevos IDs:

```text
RES-MARG-0020
SRC-0476
EVID-0281
EVSRC-0623
```

No se crea `EVAL-0026`, porque F12 no incorpora un nuevo criterio formal del modelo legacy; interpreta económicamente escenarios ya existentes.

Matriz:

```text
matrix-aut89-brand-cand-005-phase12.xlsx
SHA-256: d089ca491a1413be64362bb02da7aef8ac924b6caab75a5b48eea0340d994b78
```

La fila nueva de `Resumen Margen Vista` se materializó como **derived view mediante fórmulas**, siguiendo el patrón exigido por `full-matrix-v5 0.7.0`.

---

## 7. Próximo checkpoint

Estado al materializar `aut89`:

```text
F11
→ CLOSED — aut88 PASS

F12
→ CONCEPTUAL ANALYSIS COMPLETE
→ MATRIX MATERIALIZATION COMPLETE — aut89
→ MATRIX VALIDATOR PASS — 0 errors / 0 warnings / 0 info / 0 limitations
→ CLOSED — aut89 PASS

F13
→ OPENED AFTER F12 PASS
```

`aut89` obtuvo `PASS` limpio. F12 quedó formalmente cerrada y F13 se abrió para evaluar únicamente `BASE-HOGAR-028`.

`BASE-HOGAR-024` y `BASE-HOGAR-025` permanecen preservados como `STOP — REOPENABLE`; no se borran del conocimiento del candidato.
