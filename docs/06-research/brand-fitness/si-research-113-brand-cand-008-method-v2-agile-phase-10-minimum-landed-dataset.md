---
id: si-research-113
title: BRAND-CAND-008 — Method v2 — F10 Minimum Landed Cost Dataset
description: Dataset mínimo de origen, MOQ, pesos, empaque y brechas para BASE-FIT-009, sin equiparar datos públicos a cotizaciones formales.
version: 0.1.0
status: closed
owner: Alejandro Gelormini
created: 2026-10-19
updated: 2026-10-19
brand: brand-fitness
brand_candidate: BRAND-CAND-008
phase: F10
mode: AUTO
baseline: aut149
baseline_sha256: 88aa184fd9668d9e47efd68f4ea7348ac2a08214cd1f47d265ba9360c890e0ec
matrix_revision: aut150
matrix_sha256: cfa223d219ce6bc8ad63a5318b00f656b259ea846405667bf062e848a06f3e57
validation_status: DOUBLE_PASS
publication_status: PREPARED_FOR_F4_F13_CHECKPOINT
---

# SI-RESEARCH-113 — BRAND-CAND-008 — F10 Minimum Landed Cost Dataset

> **Estado vigente al 19/10/2026: F10 Minimum Landed Dataset CLOSED / Data Fidelity Preflight v2.4 PASS / Matrix Validator 0.1.0 PASS**, 0 errores, 0 advertencias, findings y limitations vacíos. Snapshot `aut150` — SHA-256 `cfa223d219ce6bc8ad63a5318b00f656b259ea846405667bf062e848a06f3e57`. Las menciones posteriores a estados pendientes reflejan el momento de redacción previo al cierre, no el estado vigente.

## 1. Propósito, contrato y límites

F10 — `AUTO` — consolida para `BASE-FIT-009` un **dataset mínimo de origen y logística, más un registro de brechas**, utilizando las mismas tres fichas Alibaba de F8 y el headroom exploratorio F9. El contrato vigente `SI-BIM-PROC-003 v1.0.6` exige como entrada «costo/MOQ/packing/peso» y salida «Minimum Landed Dataset». Sigue el criterio documentado en `SI-RESEARCH-099` para `BRAND-CAND-007`: **minimum dataset con brechas ≠ datos completos para comprar**.

No hubo nuevos contactos ni cotizaciones formales. Las fuentes corresponden a las capturas PDF del 19/10/2026; los valores son declaraciones de publicaciones, no información independiente ni facturas proforma. El headroom ilustrativo no es un landed cost. Se mantienen en HOLD negociaciones detalladas, homologación y muestras hasta las reuniones con el socio y el despachante de aduana.

## 2. Datos observados por referencia (Capa A)

| Registro y fuente | Precio público y unidad comercial | MOQ / tier | Peso y empaque publicados | Grado de atribución al producto |
|---|---|---|---|---|
| `COT-0070` / `SRC-0541` / `EVID-0327`: 123Sports J001 | USD **4,94/unidad**, tier 20–499; USD 4,33 (500–1.999), USD 3,97 (2.000–4.999), USD 3,56 (≥5.000) | Publicación: **20 unidades**. Logo desde 500, packaging personalizado desde 300 | Producto **78 × 19,5 × 1,8 cm** y peso **1,35 kg**; «tamaño del paquete» **45 × 18 × 25 cm**, bruto **2,0 kg**, presentación individual | **Parcial**: datos declarados en la misma ficha J001, pero accesorios/tier, dimensiones de caja master, unidades/caja, CBM y peso facturable no confirmados |
| `COT-0071` / `SRC-0542` / `EVID-0328`: Aofeite «12 en 1» | USD **4,50/par**, tier 10–299 pares; 4,30 (300–499), 4,10 (500–999), 3,80 (≥1.000) | Selector y ficha: **10 pares**; packaging personalizado desde 1.000 pares | Publica «tamaño del paquete» **64 × 25 × 10 cm**, peso bruto **0,5 kg** | **No atribuible de forma confiable**: la ficha mezcla «barra push up», **acero**, unidad «par» y fotografías de **tablero plegable**; no usar pesos/precio como equivalentes a BASE-FIT-009 |
| `COT-0072` / `SRC-0543` / `EVID-0329`: KESIDI TH-PUB001 | USD **6,50/unidad**, tier 2–499; USD 5,50 (500–999), USD 5 (≥1.000) | **Inconsistencia:** selector mínimo **2 uds** versus ficha con «MOQ 100 pcs» | Material declarado **PP**; producto **59 × 36 × 5 cm**; neto **1,3 kg** y bruto **1,6 kg**; paquete individual **38 × 23,5 × 10,5 cm** | **Parcial**: medidas/peso de presentación declarada, pero variante exacta a USD 6,50, contador, bandas, apoyos, unidades/caja, master carton, CBM, seguridad e Incoterm sin confirmar |

Las dimensiones de «paquete» no deben trasladarse automáticamente a «dimensiones de caja master» ni los pesos de presentación al **peso bruto por caja mayorista**; el peso facturable depende también de embalaje consolidado y criterio de transporte. La posible geometría plegada del modelo KESIDI **no equivale a una verificación física**. En Aofeite, no calcular volumen o peso de una «tabla 12 en 1» a partir de la barra de acero descrita en la ficha.

**Precios públicos:** no están identificados como Incoterm FOB/EXW, no se negociaron, no confirman disponibilidad, misma variante ni composición del kit. **MOQ de muestra/listing ≠ MOQ real de marca propia.**

## 3. Fuente exacta y custodia

**Origen y fecha:** capturas Alibaba entregadas por el Founder el **19/10/2026**, conservadas como PDF privado, cada una vinculada a una única ficha del proveedor y un `SRC`:

1. `COT-0070 / SRC-0541` — https://www.alibaba.com/product-detail/Foldable-Push-up-Board-Training-for_1600594930153.html?source_from=alilens_1792419272578 — PDF «1-Tabla Plegable De Realce Para Mujer,Equipo De Fitness De Realce,Tabla De Entrenamiento - Buy Product on Alibaba.com.pdf», SHA-256 `2ac567294276750017d0f187a44c5266943e808ae99734ff944ff35b1e170c02`; precio/peso/packing: páginas 1–2.
2. `COT-0071 / SRC-0542` — https://www.alibaba.com/product-detail/12-in-1-Premium-Workout-Fitness_1600481825322.html?source_from=alilens_1792419312185 — PDF «2-Sistema De Ejercicio Físico Premium 12 En 1,Entrenamiento De Tracción,Tabla De Flexiones Plegable - Buy Product on Alibaba.com.pdf», SHA-256 `2c80aba9e3a70a0024a7fb3ef002b08a10edb9e1a51584691a0e99384fd5a8a8`; precio, unidad y MOQ: p. 1, inconsistencia técnica y peso: p. 2.
3. `COT-0072 / SRC-0543` — https://www.alibaba.com/product-detail/Multifunctional-Push-Up-Board-Fitness-Equipment_1601599804379.html?spm=a2700.prosearch.normal_offer.d_image.2d0f67af45qdw3&priceId=bde15b0aab884cf8ae1c1f119086cc7c — PDF «3-Tabla Multifuncional Para Flexiones,Equipo De Fitness Para Ejercicios Musculares,Soporte Plegable Con Contador Para Entrenamiento En Casa - Buy Product on Alibaba.com.pdf», SHA-256 `24c1ffbc9365c4a5174635c9c658520f7e65a2a7d3385e3f014200ce2153787c`; precio/tier: p. 1; detalle MOQ y empaque: p. 2; función y pesos: p. 4.

Vínculos: `EVID-0327..0329`, `EVSRC-0743..0745`. La matriz conserva las URLs textuales completas en `Cotizaciones Proveedores!U71:U73` y `Fuentes!K542:K544`; `Productos Base!N106` enlaza la lectura F10 y el Research. No se fabrican nuevos IDs para volver a documentar las mismas observaciones.

## 4. Registro de brechas materiales (Capa B/C)

| Campo del Minimum Landed Dataset | KESIDI (principal) | 123Sports (secundaria) | Aofeite (referencia) |
|---|---|---|---|
| Precio de referencia público | Observado USD 6,50 / tier 2–499, **no compra** | Observado USD 4,94 / tier 20–499, **no compra** | USD 4,50/**par**, no equivalente |
| MOQ vinculante de la variante | **NO CONFIRMADO (2 vs 100)** | 20 de publicación, personalizado distinto | 10 **pares**, identidad contradictoria |
| Variante exacta y elementos incluidos | Contador/alimentación, apoyos, bandas **sin confirmar para ese precio** | Accesorios **sin confirmar para ese precio** | Modelo/SKU de tabla **no reconciliado** |
| Peso bruto facturable / volumen por caja master | **DESCONOCIDO**, hay medidas de paquete individual | **DESCONOCIDO**, hay medidas de paquete individual | **DESCONOCIDO y no comparable** |
| Unidades por caja master | Desconocido | Desconocido | Desconocido |
| Incoterm / EXW / FOB / puerto | Desconocido | Desconocido | Desconocido |
| NCM, tasas, tributos, intervenciones | **Pendiente despachante** | **Pendiente despachante** | **Pendiente despachante** |
| Ensayos de carga, estabilidad, componentes, garantías | No verificados | No verificados; carga 250 kg sólo declaración | No verificados; EN71 no acredita seguridad para fitness |
| Flete, seguro, despacho, gastos locales | No cotizados | No cotizados | No cotizados |
| Costo landed, margen, ROI | **NO CALCULABLE** con evidencia existente | **NO CALCULABLE** | **NO CALCULABLE** |

**Política de materialización:** `Cotizaciones Proveedores!P71:R73` permanece en blanco. Los campos `CBM Caja`, `Peso Bruto Caja Kg` y `Unidades por Caja` requieren un empaque/packaging mayorista identificable para el SKU concreto. Rellenarlos con pesos y dimensiones de un paquete individual haría pasar un *proxy* por dato confirmado. Se conservan sin modificación las tres filas de COT y sus precios, URLs, tier y notas F8.

## 5. Proyección del headroom F9 y umbral de decisión (Capa C)

Precios locales históricos `ML-0185` Jazak ARS 22.999 ≈ **USD 14,98**, `ML-0184` MTL ARS 24.990 ≈ **USD 16,28**, FX histórico **1.535 ARS/USD** (no actual). Bajo supuestos ilustrativos F9 — canal 25 %, comercial 5 % y margen objetivo 25 % del neto tras canal — **techo landed = 51,25 % del PVP histórico**. Resulta **USD 7,6773–8,3435** por unidad.

El precio público KESIDI USD **6,50** deja sólo **USD 1,1773–1,8435 de tolerancia teórica** *antes* de flete, seguro, tributos, logística, garantía y costos finales. La hipótesis de prima por funcionalidades no tiene evidencia local. **No presentar esta resta como margen, beneficio, flete disponible contractual ni costo landed real.**

## 6. Gate F10 y alcance de F11 (Capa D)

**Resultado propuesto F10 — `MINIMUM LANDED DATASET DOCUMENTED — WITH MATERIAL GAPS / NON-PROCUREMENT-GRADE`**.

- `BASE-FIT-009`: **PARCIAL / F11 SENSITIVITY ELIGIBLE ONLY**. KESIDI es referencia principal aprobada en F8, **no proveedor elegido**. La evidencia basta para un escenario condicional de estrés F11, no para una importación ejecutable.
- Aofeite: **NON-COMPARABLE UNTIL SKU RECONCILED**; no usar el precio «par» como costo de una tabla reconfigurable.
- 123Sports: comparable funcional/económico, pero no hay costos de packaging mayorista ni calidad y SKU confirmados.
- F11 podrá efectuar sensibilidades de coste **no ejecutables** con supuestos explícitos y no deberá transformar peso de paquete individual en peso facturable real ni afirmar que se puede importar.
- F12 interpretará el resultado sin recalcular; F13 integrará los riesgos y podrá concluir `NO FINALIST / FREEZE` sin abrir F14.

**Gate comercial externo en HOLD:** ningún contacto profundo con proveedores, cotización detallada, muestra u homologación hasta reunión con socio y despachante. Los datos faltantes son **desconocidos**, nunca equivalentes a cero.

## 7. Materialización e integridad

- Baseline F9: `aut149`, SHA-256 `88aa184fd9668d9e47efd68f4ea7348ac2a08214cd1f47d265ba9360c890e0ec`, Data Fidelity Preflight y Matrix Validator ambos PASS del 19/10/2026.
- Output preparado F10: `matrix-aut150-brand-cand-008-phase10-minimum-landed-dataset.xlsx`, SHA-256 `cfa223d219ce6bc8ad63a5318b00f656b259ea846405667bf062e848a06f3e57`.
- Cambios autorizados y observados: **`Nichos!AD40:AF40` y `Productos Base!N106`**. No hay modificación de `Cotizaciones Proveedores`, `Publicaciones ML`, `Fuentes`, `Evidencias`, `Verificaciones ML`, `Simulación Margen` ni scores de F3–F5.
- Auditoría OOXML local independiente del Engine: **PASS**; 29 hojas, 1.942 fórmulas, cinco URLs ML y tres URLs Alibaba conservadas. No hay nuevos registros `MARG` ni IDs inventados.
- **Estado de validación:** `PENDING_DOUBLE_PASS`; los controles locales no reemplazan Data Fidelity Preflight v2.4 y Matrix Validator 0.1.0 `full-matrix-v5 0.7.0`.

## 8. Próximo gate

Al confirmar el doble PASS del snapshot `aut150` en la Mac del Founder: `F10 CLOSED (AUTO)`, avance a **F11 — Landed Cost Screen** limitado a sensibilidad explícita, no cotización ejecutable ni compra. `F14 NOT OPENED`. Documentación en español; datos técnicos y metadatos conservan convenciones del repositorio. Este Research se publicará en el checkpoint documental pertinente, nunca se subirán los XLSX, PDFs, logs ni scripts de trabajo.


## 9. Cierre canónico confirmado F10 — 2026-10-19

**F10 CLOSED — AUTO / DOUBLE PASS:** `matrix-aut150-brand-cand-008-phase10-minimum-landed-dataset.xlsx`, SHA-256 `cfa223d219ce6bc8ad63a5318b00f656b259ea846405667bf062e848a06f3e57`. Data Fidelity Preflight v2.4 **PASS** (5 publicaciones auditadas, 5 ledger, 1 PB); Matrix Validator 0.1.0, `full-matrix-v5 0.7.0`, **PASS**, errores 0, warnings 0, info 0, `findings []`, `limitations []`. Evidencia privada: `validation-aut150-brand-cand-008-f10.log`. Los indicadores `F10 NO CLOSED` del script corresponden al momento de ejecución previo al resultado de los validadores.

**Gate F11 habilitado:** sólo escenario de estrés exploratorio, no adquisición; no editar retrospectivamente aut150.

## Nota de cierre consolidada — 19/10/2026

La fase **F10 Minimum Landed Dataset** quedó **CLOSED** tras el doble PASS canónico de `aut150` (SHA-256 `cfa223d219ce6bc8ad63a5318b00f656b259ea846405667bf062e848a06f3e57`); no se reabren sus fuentes ni se altera la historia de la evaluación. La evidencia posterior se analiza en las fases siguientes, sin trasladar aprobaciones de un gate a otro.
