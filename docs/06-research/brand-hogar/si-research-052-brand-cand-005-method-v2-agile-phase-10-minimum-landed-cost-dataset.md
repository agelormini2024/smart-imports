---
id: si-research-052
title: BRAND-CAND-005 — Method v2 Agile — Fase 10 — Minimum Landed Cost Dataset
description: Dataset mínimo decision-grade para habilitar Landed Cost de las Product Bases activas de BRAND-CAND-005.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-28
updated: 2026-09-30
brand: brand-hogar
brand_candidate: brand-cand-005
method: method-v2-agile
phase: F10
---

# SI-RESEARCH-052 — BRAND-CAND-005 — Method v2 Agile — Fase 10 — Minimum Landed Cost Dataset

## 1. Metadata

- **Brand Candidate:** `BRAND-CAND-005`
- **Territorio:** Marca Hogar
- **Tema:** Compostaje / procesamiento doméstico de residuos orgánicos
- **Fase:** F10 — Minimum Landed Cost Dataset
- **Fecha:** 2026-09-28
- **Input matrix:** `matrix-aut85-brand-cand-005-phase9.xlsx`
- **Input validator:** PASS — Matrix Validator `0.1.0` / schema `full-matrix-v5 0.7.0`
- **Input SHA-256:** `7fb8169ecbc12ad31f4ad35e62be54a77107ab8f5c649c2d46081669ce50c2e1`
- **Output matrix:** `matrix-aut86-brand-cand-005-phase10.xlsx`
- **Output SHA-256:** `2271556ff168dbaeb35c2d78094590443ef584ed60560e9756732f82008102a0`
- **Output validator:** PASS — Matrix Validator `0.1.0` / schema `full-matrix-v5 0.7.0`
- **Output validation:** `0 errors / 0 warnings / 0 info / 0 limitations`
- **Estado de F10:** `CLOSED — VALIDATOR PASS`
- **F11:** `OPENED AFTER F10 PASS`

## 2. Objetivo de la fase

F10 no busca una cotización formal ni cerrar procurement. Busca alcanzar un dataset mínimo suficiente para que F11 pueda modelar **Economic Landed Cost** sin inventar peso, volumen, MOQ o especificaciones materiales.

Reglas de la fase:

```text
DECISION-GRADE ≠ PROCUREMENT-GRADE
SAME-SKU / SAME-LISTING > COMPOSITE PROXY
PUBLIC PRICE ≠ FORMAL QUOTE
MOQ / PRICE TIER deben permanecer unidos
```

La evidencia pública se amplió sólo donde existía un gap material. No se duplicó sourcing cuando el dataset de F8 ya era suficiente.

## 3. Scope activo

F10 trabaja únicamente sobre los tres Product Bases que sobrevivieron F9:

- `BASE-HOGAR-024` — Compostera modular apilable 40–60 L
- `BASE-HOGAR-025` — Compostera giratoria 120 L — doble cámara
- `BASE-HOGAR-028` — Procesador eléctrico térmico countertop 3–4 L

`BASE-HOGAR-026` y `BASE-HOGAR-027` permanecen en watchlist. `BASE-HOGAR-029` continúa como `SUPPORT_PB / ADJACENT`.

---

## 4. BASE-HOGAR-024 — Compostera modular apilable 40–60 L

### 4.1 Gap proveniente de F9

F9 utilizó `COT-0054` como comparación de costo/origen, pero el dataset seguía siendo compuesto porque faltaban capacidad exacta 40–60 L y un dato logístico utilizable.

No se debía inventar packing.

### 4.2 Evidencia de costo/origen preservada — COT-0054

Supplier listing público:

- modelo: `WB25101`
- proveedor: Yangjiang Welsource Plastic Products Factory
- plataforma: Made-in-China
- precio: **USD 24,29**
- tier: **50–499 sets**
- MOQ: **50**
- 5 working trays
- base colectora
- spigot
- coir starter
- manual
- transport package declarado: carton

Fuente:

`https://www.made-in-china.com/showroom/wsgardenwares/product-detailUAlrSpKvbXRW/China-5-Tray-Square-Plastic-Worm-Composter-Worm-Compost-Bin-Set-Worm-Composting.html`

### 4.3 Nueva evidencia logística same-model — COT-0060

Se encontró un downstream branded SKU de VEVOR con **el mismo model number `WB25101`** y arquitectura coincidente de 5 bandejas + base/spigot.

Dataset público:

- model number: `WB25101`
- capacidad: **50 L**
- bandejas: **5**
- material: **HDPE**
- peso de producto: **5,1 kg**
- dimensiones unloaded: **400 × 400 × 410 mm**
- dimensiones loaded: **400 × 400 × 650 mm**

Fuente:

`https://www.vevor.com/compost-tumbler-c_11277/vevor-5-tray-worm-composter-50-l-worm-compost-bin-outdoor-and-indoor-sustainable-design-worm-farm-kit-for-recycling-food-waste-worm-castings-worm-tea-vermiculture-and-vermicomposting-p_010234676318`

El model number y la arquitectura hacen razonable utilizar esta evidencia como **same-model downstream logistics proxy**, pero **no prueban** una relación OEM entre Welsource y VEVOR.

Para F11 se materializa como proxy:

```text
CBM proxy = 0,40 × 0,40 × 0,41 = 0,0656 m³
peso físico proxy = 5,1 kg
units = 1
```

Estos valores representan envelope unloaded + product weight públicos, **no carton dimensions ni gross weight emitidos por el supplier**.

### 4.4 Resultado F10

```text
BASE-HOGAR-024
DECISION-GRADE — SAME-MODEL DOWNSTREAM LOGISTICS PROXY / COMPOSITE
```

Quality flags:

- costo/MOQ: público supplier-side;
- capacidad 50 L: same-model downstream;
- logística: proxy same-model, no packing sheet;
- gross weight de caja: no confirmado;
- relación OEM supplier↔VEVOR: no probada.

Aplicabilidad F11:

- el tier de `COT-0054` es **50–499**, por lo que 50 y 100 unidades sí son compatibles con el precio público de USD 24,29;
- peso y volumen deben conservar flag `LOGISTICS_PROXY`.

---

## 5. BASE-HOGAR-025 — Compostera giratoria 120 L — doble cámara

### 5.1 Dataset preservado — COT-0056

El dataset de F8 ya era suficientemente fuerte y no se justificó duplicar sourcing.

`COT-0056`:

- modelo: `TG4204011`
- 120 L
- dual chamber
- modified PP
- anti-UV / anti-frost declarados
- producto: **64 × 61,3 × 75,5 cm**
- package: **62 × 56 × 20 cm**
- gross weight: **11 kg**
- units/package: **1**
- precio: **USD 28,80** para **439–910**
- precio: **USD 25,80** desde **1117**
- custom logo / packaging desde **1000**

Listing de origen utilizado en F8:

`https://www.alibaba.com/product-detail/Winslow-Ross-120L-capacity-organic-compost_1600977589621.html`

Como verificación adicional de consistencia de modelo, el sitio oficial de Vertak lista `120L Compost Tumbler TG4204011` entre sus productos:

`https://www.vertak.com/china-best-compost-tumbler-factory/`

### 5.2 Resultado F10

```text
BASE-HOGAR-025
DECISION-GRADE — SAME-LISTING PUBLIC CONFIRMED
```

No existe un gap material adicional para abrir F11.

El riesgo dominante no es la calidad del dataset sino la estructura comercial/logística:

- MOQ alto;
- unidad voluminosa;
- 11 kg gross por unidad;
- custom packaging requiere escala mayor.

### 5.3 Restricción crítica para F11

El precio **USD 28,80 no es un precio para 50 o 100 unidades**. Está publicado para **439–910**.

Por lo tanto:

```text
50 / 100 u al precio USD 28,80
≠ escenario comercial ejecutable
```

F11 debe elegir una de estas dos formas sin mezclar significados:

1. modelar un escenario ejecutable a **MOQ 439**, o
2. conservar sensibilidades estandarizadas 50/100 para comparabilidad transversal, pero marcarlas explícitamente como:

```text
NON-EXECUTABLE AT PUBLIC MOQ
```

No deben interpretarse como un purchase case real.

---

## 6. BASE-HOGAR-028 — Procesador eléctrico térmico countertop

### 6.1 Same-SKU público — COT-0058

La fuente pública del `CLEESINK MLT-450` aporta suficiente información para F11, pero contiene una inconsistencia interna que F10 debe hacer visible.

Datos técnicos consistentes:

- modelo: `MLT-450`
- capacidad: **4,5 L**
- potencia: **650 W**
- voltage/frequency: **110/220V 50/60Hz**
- MOQ declarado en tabla: **100**
- muestra pública: **USD 140**
- warranty: **1 year**
- carbon bag life cycle: **6 months**
- blade: **non-detachable**
- motor: **brushed**
- certificaciones declaradas: **CE / FCC / CB / RoHS / KC**

Fuente principal:

`https://cleesink.en.made-in-china.com/product/SgVUzrWxJJkC/China-4-5L-220V-Kitchen-Food-Waste-Garbage-Recycler-for-Family-Usage.html`

El sitio oficial de Cleesink también identifica al `MLT-450` como 4,5 L / 650 W / 110V-220V 50-60Hz y declara active carbon filter con reemplazo a 6 meses:

`https://www.cleesink.com/en/multi-series/102.html`

### 6.2 Inconsistencia pública de packing

El mismo listing expone dos juegos de datos:

**Packaging & Delivery:**

```text
39 × 33,8 × 33,8 cm
7,3 kg gross
```

**Tabla detallada del modelo:**

```text
Carton size: 410 × 520 × 320 mm
N/G Weight: 9,5 / 11,5 kg
```

La diferencia es material para flete aéreo.

F10 no intenta reconciliarla inventando una explicación. Para el Landed Cost Screen se adopta conservadoramente el segundo juego:

```text
CBM = 0,41 × 0,52 × 0,32 = 0,068224 m³
peso gross = 11,5 kg
```

### 6.3 Service / electrical flags

Queda públicamente cubierto:

- 220V;
- 50Hz dentro de 50/60Hz;
- vida declarada del carbon bag: 6 meses;
- warranty declarada: 1 año;
- certificaciones declaradas.

No queda cerrado a nivel procurement:

- 240V exacto;
- SKU y disponibilidad real de filtros de reemplazo;
- pricing de filtros;
- repuestos generales;
- documentación certificada correspondiente al SKU exacto;
- soporte/garantía aplicable a una operación local.

### 6.4 Resultado F10

```text
BASE-HOGAR-028
DECISION-GRADE — SAME-SKU PUBLIC / CONSERVATIVE PACKING
```

Es suficiente para F11 porque los gaps remanentes afectan procurement/service, no impiden un screening económico preliminar.

Restricción F11:

- **100 u** coincide con el MOQ público conservador;
- **50 u** no debe tratarse como escenario comercial ejecutable sin un tier específico.

---

## 7. Resultado consolidado F10

| Product Base | Resultado F10 | Dataset para F11 | Quality flag dominante |
|---|---|---|---|
| `BASE-HOGAR-024` | `DECISION-GRADE — SAME-MODEL DOWNSTREAM LOGISTICS PROXY / COMPOSITE` | Sí | supplier carton/gross no confirmado |
| `BASE-HOGAR-025` | `DECISION-GRADE — SAME-LISTING PUBLIC CONFIRMED` | Sí | MOQ 439 + volumetría |
| `BASE-HOGAR-028` | `DECISION-GRADE — SAME-SKU PUBLIC / CONSERVATIVE PACKING` | Sí | packing público inconsistente + service gaps |

Los tres Product Bases dispusieron de evidencia suficiente para habilitar F11. `aut86` obtuvo `PASS` local limpio y F10 quedó formalmente `CLOSED`.

No se contactan proveedores en F10.

## 8. Materialización en matriz

Cambios principales de `aut86`:

- nuevo `COT-0060` para el proxy logístico same-model de `BASE-HOGAR-024`;
- refinamiento conservador de `COT-0058` a 0,068224 m³ / 11,5 kg;
- nota F10 en `COT-0056` sobre MOQ/tier;
- nuevo `SRC-0473` — fuente pública `COT-0060`;
- nuevo `SRC-0474` — análisis consolidado F10;
- nuevo `EVID-0279` — Minimum Landed Cost Dataset;
- nuevos `EVSRC-0611` a `EVSRC-0615`;
- actualización de notas de `BASE-HOGAR-024`, `025` y `028`;
- actualización del estado de `BRAND-CAND-005` en `Nichos`;
- **no se crea `EVAL-0026`**, porque F10 no agrega una evaluación formal de criterio.

## 9. Handoff exacto a F11

Con `aut86 PASS` confirmado:

```text
F10 CLOSED
→ abrir F11 — Landed Cost Screen
```

F11 debe conservar los supuestos metodológicos ya vigentes del proyecto, pero aplicar los MOQ/tier correctamente:

```text
BASE-HOGAR-024
50 / 100 u → tier público ejecutable

BASE-HOGAR-025
MOQ 439 → escenario comercial ejecutable
50 / 100 u → sólo sensibilidad NON-EXECUTABLE AT PUBLIC MOQ

BASE-HOGAR-028
100 u → alineado a MOQ público conservador
50 u → sensibilidad / tier no confirmado
```

F10 no calcula margen ni ROI.

```text
ECONOMIC LANDED COST ≠ TOTAL CASH OUTLAY
HEADROOM ≠ LANDED COST ≠ MARGIN
```

## 10. Checkpoint

Estado al cerrar este documento:

```text
CONCEPTUAL ANALYSIS      COMPLETE
MATRIX MATERIALIZATION  COMPLETE — aut86
MATRIX VALIDATOR        PASS — 0 errors / 0 warnings / 0 info / 0 limitations
DOCUMENTARY CHECKPOINT  COMPLETE
F10                      CLOSED
F11                      OPENED AFTER PASS
```
