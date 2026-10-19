---
id: si-research-112
title: BRAND-CAND-008 — Method v2 — F9 Import Cost Headroom
description: Techo teórico landed bajo supuestos comerciales de screening, a partir de dos comparables ML y tres publicaciones Alibaba.
version: 0.1.0
status: closed
owner: Alejandro Gelormini
created: 2026-10-19
updated: 2026-10-19
brand: brand-fitness
brand_candidate: BRAND-CAND-008
phase: F9
mode: AUTO
baseline: aut148
baseline_sha256: 786676c581f97a972f38688a7dc6e0a27371e535c4cf224360fed71afa45c2c4
matrix_revision: aut149
matrix_sha256: 88aa184fd9668d9e47efd68f4ea7348ac2a08214cd1f47d265ba9360c890e0ec
validation_status: DOUBLE_PASS
publication_status: PREPARED_FOR_F4_F13_CHECKPOINT
---

# SI-RESEARCH-112 — BRAND-CAND-008 — F9 Import Cost Headroom

> **Estado vigente al 19/10/2026: F9 Headroom CLOSED / Data Fidelity Preflight v2.4 PASS / Matrix Validator 0.1.0 PASS**, 0 errores, 0 advertencias, findings y limitations vacíos. Snapshot `aut149` — SHA-256 `88aa184fd9668d9e47efd68f4ea7348ac2a08214cd1f47d265ba9360c890e0ec`. Las menciones posteriores a estados pendientes reflejan el momento de redacción previo al cierre, no el estado vigente.

## 1. Objetivo y gate

F9, `AUTO`, modela el **techo teórico tolerable de costo importado (headroom)** para una sola Product Base, `BASE-FIT-009` — Tabla plegable para flexiones con agarres reconfigurables. **No estima un costo importado real.** La información vigente procede de fichas públicas de Alibaba y dos comparables argentinos: no existe cotización FOB/EXW, costo de logística cotizado, posición arancelaria confirmada, composición exacta del kit, validación de seguridad ni estimación de disposición a pagar por una variante diferente.

F8 está `CLOSED / DOUBLE PASS / FOUNDER APPROVED 2026-10-19`. El Founder aprobó KESIDI TH-PUB001 como **referencia principal condicionada**, 123Sports J001 como comparación secundaria y Aofit 12-en-1 como referencia adicional. Es screening exploratorio; no selección de proveedor ni autorización de compra. `aut148` es baseline histórica, SHA-256 `786676c581f97a972f38688a7dc6e0a27371e535c4cf224360fed71afa45c2c4`.

## 2. Fuentes y precios históricos de venta Argentina

| Fuente | Producto comparable | PVP observado | Conversión referencial | Observación |
|---|---|---:|---:|---|
| `ML-0185` / `SRC-0537` | Jazak Push Up multifuncional | ARS 22.999 | USD **14,98** | Captura Mercado Libre 16/10/2026; comparable directo condicionado |
| `ML-0184` / `SRC-0536` | MTL Push Up Board | ARS 24.990 | USD **16,28** | Captura Mercado Libre 16/10/2026; comparable directo condicionado |

Conversión ilustrativa a FX histórico **ARS 1.535/USD**. Los USD presentados se redondean a dos decimales, de acuerdo con la lectura histórica del screening. **No** actualizar con un FX posterior, ni asumir que el mismo PVP corresponde a la variante KESIDI.

## 3. Referencias públicas de origen

| Fuente | Proveedor / modelo | Precio publicado inicial | Restricción de comparabilidad |
|---|---|---:|---|
| `COT-0070` / `SRC-0541` / `EVID-0327` | 123Sports J001 | USD 4,94 / unidad | Variante y accesorios no confirmados; MOQ anunciado 20 |
| `COT-0071` / `SRC-0542` / `EVID-0328` | Aofeite 12 en 1 | USD 4,50 / **par** | Unidad «par», ficha material acero vs imagen de tabla; MOQ anunciado 10 pares |
| `COT-0072` / `SRC-0543` / `EVID-0329` | KESIDI TH-PUB001 | USD 6,50 / unidad publicada | Selector MOQ 2 vs ficha 100; inclusión y funcionamiento de contador, apoyos y bandas no confirmados |

Enlaces originales preservados completos en `Cotizaciones Proveedores!U71:U73` y `Fuentes!K542:K544`:

- https://www.alibaba.com/product-detail/Foldable-Push-up-Board-Training-for_1600594930153.html?source_from=alilens_1792419272578
- https://www.alibaba.com/product-detail/12-in-1-Premium-Workout-Fitness_1600481825322.html?source_from=alilens_1792419312185
- https://www.alibaba.com/product-detail/Multifunctional-Push-Up-Board-Fitness-Equipment_1601599804379.html?spm=a2700.prosearch.normal_offer.d_image.2d0f67af45qdw3&priceId=bde15b0aab884cf8ae1c1f119086cc7c

Estos precios **no son FOB/EXW** ni son necesariamente de SKU comparables. Ninguno autoriza calcular costo real de importación.

## 4. Fórmula y supuestos del headroom

Se reutiliza la **política de sensibilidad ilustrativa de `BRAND-CAND-007`** para permitir una lectura comparable, sin transformarla en hecho de mercado:

- `P` = PVP bruto USD del comparable argentino (aproximado).
- Costo canal: `0,25 × P`.
- Costos comerciales: `0,05 × P`.
- Base de margen objetivo: venta neta tras canal `0,75 × P`.
- Margen objetivo: `0,25 × (0,75 × P)`.
- **Headroom teórico = `P − 0,25P − 0,05P − 0,25(0,75P)` = `0,5125 × P`.**

| Referencia | PVP USD | Headroom teórico USD | Diferencia ilustrativa vs KESIDI USD 6,50 |
|---|---:|---:|---:|
| Jazak / ML-0185 | 14,98 | **7,6773** | **1,1773** |
| MTL / ML-0184 | 16,28 | **8,3435** | **1,8435** |

La diferencia **no es margen**, beneficio ni un presupuesto real disponible para flete. Sólo confronta un precio público de origen no contractual con un techo teórico comercial. La comparación Jazak/MTL contra KESIDI **no prueba equivalencia funcional ni disposición a pagar**. Para 123Sports y Aofeite no se declara viabilidad; en Aofeite ni siquiera se ha conciliado la unidad comercial «par».

## 5. Diagnóstico F9

**HEADROOM TIGHT — EXPLORATORY / LOW CONFIDENCE.** Bajo los supuestos elegidos, la referencia prioritaria KESIDI deja poca tolerancia aparente antes de gastos de importación; hay riesgo material de que la propuesta no alcance los objetivos económicos con precios locales similares. A favor sólo existe una **hipótesis** de funciones adicionales (apoyos, bandas, contador), no una prima de precio observada ni calidad comprobada.

Las siguientes variables **no están documentadas para cálculo confiable** y no deben completarse por conjetura: FOB/EXW, arancel/NCM, tributos, aduana, flete, CBM/peso por caja vinculados al SKU correcto, costos locales, landed cost, margen neto, ROI, tasa de defectos y precio real realizable de variante premium.

No se incorpora `MARG-` ni fila de simulación económica en F9; la hoja `Simulación Margen` conserva sus registros históricos. Tampoco se asigna un puntaje de «Margen Potencial» en `Nichos` o `Evaluaciones` sólo a partir de estos headrooms. Las fases económicas posteriores, si se ejecutan, deben distinguir modelado condicionado de costos comprobados.

## 6. Materialización e integridad

- **Entrada:** `aut148`, SHA-256 `786676c581f97a972f38688a7dc6e0a27371e535c4cf224360fed71afa45c2c4`.
- **Salida preparada:** `matrix-aut149-brand-cand-008-phase9-headroom.xlsx`, SHA-256 `88aa184fd9668d9e47efd68f4ea7348ac2a08214cd1f47d265ba9360c890e0ec`.
- **Cambios autorizados y efectivos:** exclusivamente `Nichos!AD40:AF40`, que registra la fase, este Research y los supuestos/headroom con sus IDs.
- **Preservación local comprobada:** 29 hojas, 1.942 fórmulas, cinco URLs de Mercado Libre y tres URLs de Alibaba; ningún precio, evaluación, Product Base, costo ni registro `MARG` antiguo fue alterado. Auditoría OOXML local **PASS**, independiente del Engine.
- **Cierre canónico:** ambos validadores PASS sobre `aut149` el 19/10/2026 (0 errores, 0 warnings, 0 findings, 0 limitations). El validador estructural no acredita rentabilidad.

## 7. Cierre canónico F9 y próximo gate

**F9 CLOSED — AUTO — DOUBLE PASS CONFIRMADO el 19/10/2026** sobre `aut149`: Data Fidelity Preflight v2.4 **PASS** (5 publicaciones, 5 verificaciones, 1 Product Base), Matrix Validator 0.1.0 `full-matrix-v5 0.7.0` **PASS**, 0 errores / 0 advertencias / `findings []` / `limitations []`; hash `88aa184fd9668d9e47efd68f4ea7348ac2a08214cd1f47d265ba9360c890e0ec`. Log local privado `validation-aut149-brand-cand-008-f9.log`.

**F10 habilitada** conforme al contrato para documentar información mínima pública y las brechas, sin RFQ formal ni homologación anticipada. Mantener el HOLD comercial hasta reunión con socio y despachante. `F14 NOT OPENED`. Documentos funcionales en español; PDFs, XLSX, logs y scripts de trabajo permanecen privados, no se publican en Git.

## Nota de cierre consolidada — 19/10/2026

La fase **F9 Headroom** quedó **CLOSED** tras el doble PASS canónico de `aut149` (SHA-256 `88aa184fd9668d9e47efd68f4ea7348ac2a08214cd1f47d265ba9360c890e0ec`); no se reabren sus fuentes ni se altera la historia de la evaluación. La evidencia posterior se analiza en las fases siguientes, sin trasladar aprobaciones de un gate a otro.
