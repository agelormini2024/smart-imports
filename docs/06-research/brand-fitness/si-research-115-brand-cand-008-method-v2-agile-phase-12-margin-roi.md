---
id: si-research-115
title: BRAND-CAND-008 — Method v2 — F12 Margin + ROI
description: Interpretación económica de BASE-FIT-009 sin margen ni ROI ficticios, bajo sensibilidad aérea no ejecutable F11 y brechas logísticas materiales.
version: 0.1.0
status: closed
owner: Alejandro Gelormini
created: 2026-10-19
updated: 2026-10-19
brand: brand-fitness
brand_candidate: BRAND-CAND-008
phase: F12
mode: AUTO
baseline: aut151
baseline_sha256: caa1d887543b0edcc2ada1e5ce0bf85ce7c80053e3a953378f8e7926066df860
matrix_revision: aut152
matrix_sha256: 3e970884eebbd4a39591c748c2d6af0f3e8aaf52fbdcbf82ee5101dedce077af
validation_status: DOUBLE_PASS
publication_status: PREPARED_FOR_F4_F13_CHECKPOINT
---

# SI-RESEARCH-115 — BRAND-CAND-008 — F12 Margin + ROI

> **Estado vigente al 19/10/2026: F12 Margin + ROI CLOSED / Data Fidelity Preflight v2.4 PASS / Matrix Validator 0.1.0 PASS**, 0 errores, 0 advertencias, findings y limitations vacíos. Snapshot `aut152` — SHA-256 `3e970884eebbd4a39591c748c2d6af0f3e8aaf52fbdcbf82ee5101dedce077af`. Las menciones posteriores a estados pendientes reflejan el momento de redacción previo al cierre, no el estado vigente.

> **F12 AUTO — CLOSED / DOBLE PASS canónico `aut152` confirmado el 19/10/2026.** El contrato `SI-BIM-PROC-003 v1.0.6` establece «F12 | F11 | Margin + ROI | interpreta, no recalcula». Por lo tanto, F12 interpreta F9–F11 y **no produce valores de margen o retorno sobre inversión sin un costo landed completo, confiable y atribuible al mismo SKU**. Se sigue el precedente `SI-RESEARCH-101` de `BRAND-CAND-007`.

## 1. Alcance, entradas y límites

- Candidato: `BRAND-CAND-008`, misión «Entrenamiento flexible y portátil», única Product Base del candidato `BASE-FIT-009` — Tabla plegable para flexiones con agarres reconfigurables.
- `F3 Demanda: 2/5 / Baja`, `F4 Competencia: 2/5 / Baja`, `F5 Potencial de Marca: 2/5 / Baja`: **los scores originales no cambian** en F12.
- `F6 RECONCILED / aut146`, `F7 CLOSED / aut147`, `F8 COLLABORATIVE CLOSED / Founder APPROVED 2026-10-19 / aut148`, `F9 CLOSED / aut149`, `F10 CLOSED / aut150`, `F11 CLOSED / aut151`; todos los snapshots operativos cerrados tienen doble PASS.
- `SI-RESEARCH-114` F11 aporta un **estrés aéreo no ejecutable con supuesto histórico USD 10/kg facturable**; no es cotización ni costo landed.
- F12 **no actualiza** precios, FX, ventas visibles, fuentes, `Simulación Margen`, margen, ROI, ni genera `MARG-*`. No convierte incógnitas en ceros o márgenes negativos declarados.

## 2. Hechos y resultados ya producidos por F9–F11 (no recalculados)

| Dimensión | KESIDI TH-PUB001 (prioridad de F8, condicionada) | 123Sports J001 (comparable de origen) | Aofeite 12 en 1 |
|---|---|---|---|
| Fuente origen | `COT-0072 / SRC-0543 / EVID-0329` | `COT-0070 / SRC-0541 / EVID-0327` | `COT-0071 / SRC-0542 / EVID-0328` |
| Precio de publicación | USD **6,50/unidad** (no FOB/EXW) | USD **4,94/unidad** (no FOB/EXW) | USD **4,50/par**; identidad de producto y unidad contradictorias |
| Headroom F9 (basado en PVP histórico **Jazak/MTL**, no precio premium KESIDI) | USD **7,6773–8,3435**, techo teórico landed; remanente previo a gastos **1,1773–1,8435**, **no margen** | Mismo rango referencial; remanente **2,7373–3,4035**, no margen | No aplicable sin reconciliar SKU/unidad |
| Escenario hipotético F11: **0,5 kg facturable × USD 10/kg** | Producto publicado + flete proxy = USD **11,50**, supera ambos headrooms | Producto publicado + flete proxy = USD **9,94**, supera ambos headrooms | No se calcula |
| Información ausente decisiva | MOQ contradictorio 2 vs 100; configuración / contador / accesorios, packing máster, costo real, NCM y seguridad | configuración de oferta, accesorios, packing máster, kg facturables, tributos | tabla vs barra de acero y precio por par |
| Costo landed, margen neto, ROI | **NO DETERMINABLES** | **NO DETERMINABLES** | **NO DETERMINABLES** |

**Límites económicos:** el FX histórico ARS 1.535/USD, los supuestos de costos comerciales/canal y el margen objetivo que formaron el techo F9 no son tasas vigentes ni resultados efectivos de operaciones. Los contadores visibles y precios de Mercado Libre corresponden a comparables locales, no a ventas demostradas de la variante KESIDI. El saldo nominal frente al headroom no debe etiquetarse como «margen».

## 3. Interpretación económica por referencia

### 3.1 KESIDI — principal de origen, **HOLD — REOPENABLE**

- **Bajo el estrés aéreo elegido**, ya el producto de origen público más flete ilustrativo excede el techo teórico; todavía faltarían gastos positivos no cuantificados. El análisis no alcanza para emitir un precio landed.
- No es válido calcular un margen bruto, neto o ROI con `O + r × w`, porque `w` y `r` son hipotéticos y además no incluyen impuestos, seguro, aduana, logística local, QA ni costos de capital.
- Los apoyos, bandas y contador podrían motivar diferenciación; **no hay evidencia de una prima de precio aceptada en Argentina** ni configuración de accesorios confirmada para el precio público citado.
- No se infiere que marítimo/LCL sea viable o inviable: faltan master carton, CBM, NCM, presupuesto consolidado y requisitos que deberán revisar socio y despachante.
- **Confianza en viabilidad de importación: Baja**, por falta de datos ejecutables; esto es una valoración de incertidumbre económica, no un cambio del score de demanda/competencia/marca.

### 3.2 123Sports — comparable económico, **HOLD — REOPENABLE / VARIANT UNCONFIRMED**

El menor precio de origen no demuestra mejor margen: la variante y los accesorios incluidos no son necesariamente equivalentes a KESIDI; el estrés aéreo hipotético también supera el headroom histórico y no hay costo landed ni ROI medible. Sigue siendo un comparable útil, no un proveedor recomendado.

### 3.3 Aofeite — **NOT COMPARABLE / SOURCE RECONCILIATION REQUIRED**

La publicación mezcla barra metálica, tablero en imagen y unidad comercial por par. No se aplica ratio de precios, no se construyen costos unitarios por supuesta tabla ni se interpreta margen o ROI.

## 4. Decisión F12 — clasificación condicionada

| Product Base | Resultado económico | Confianza de importación | Gate y condición |
|---|---|---|---|
| `BASE-FIT-009` | **`AIR STRESS UNFAVORABLE UNDER EXPLICIT PROXY / MARGIN + ROI NOT DETERMINABLE / MARITIME UNDETERMINED`** | **Baja** | **`HOLD — REOPENABLE`** sujeto a revisión con socio/despachante, requisitos/NCM, packing y masa facturable, MOQ/variante, seguridad, costo integral y disposición de pago adicional |

Esta clasificación **no es un `PASS` económico ni un `STOP` definitivo**, y no homologa KESIDI u otro proveedor. La información disponible permite una decisión de *screening* condicionada, pero **no autoriza compras, muestras, cotizaciones formales o compromiso de capital**. La profundización de proveedores y logística se mantiene postergada hasta las reuniones externas acordadas.

F13 (`AUTO`) deberá integrar las capas de F3–F12, valorar expresamente la diferenciación prometida frente al mercado, el riesgo de commodity / ticket, la seguridad y la fricción económica, y emitir su **Final Shortlist/Decision Report**, sin abrir F14 implícitamente. Una base normalizada no tiene por qué convertirse en FINALIST.

## 5. Fuente y trazabilidad

La evidencia pública de origen de F8 está archivada y enlazada en `SI-RESEARCH-111`; no se vuelven a recolectar ni reescribir sus URL originales. Las tres fichas capturadas el 19/10/2026 son:

1. 123Sports J001: https://www.alibaba.com/product-detail/Foldable-Push-up-Board-Training-for_1600594930153.html?source_from=alilens_1792419272578
2. Aofeite: https://www.alibaba.com/product-detail/12-in-1-Premium-Workout-Fitness_1600481825322.html?source_from=alilens_1792419312185
3. KESIDI TH-PUB001: https://www.alibaba.com/product-detail/Multifunctional-Push-Up-Board-Fitness-Equipment_1601599804379.html?spm=a2700.prosearch.normal_offer.d_image.2d0f67af45qdw3&priceId=bde15b0aab884cf8ae1c1f119086cc7c

Source binding original y PDF privados: `COT-0070..0072 / SRC-0541..0543 / EVID-0327..0329 / EVSRC-0743..0745`. Los precios de Mercado Libre corresponden a `ML-0184` y `ML-0185` y mantienen su información de captura/FX en la matriz.

## 6. Materialización y cierre técnico

- **Baseline**: `matrix-aut151-brand-cand-008-phase11-landed-cost-screen.xlsx`, SHA-256 `caa1d887543b0edcc2ada1e5ce0bf85ce7c80053e3a953378f8e7926066df860`, **F11 DOUBLE PASS** confirmado en log `validation-aut151-brand-cand-008-f11.log`.
- **Snapshot F12**: `matrix-aut152-brand-cand-008-phase12-margin-roi.xlsx`, SHA-256 `3e970884eebbd4a39591c748c2d6af0f3e8aaf52fbdcbf82ee5101dedce077af`.
- **Modificaciones permitidas**: `Nichos!AD40:AF40`, `Productos Base!N106`, como observaciones narrativas y referencia al presente Research. No se agregan datos en hojas de costo ni rentabilidad.
- **Integridad local verificada**: 29 hojas, 1.942 fórmulas; URLs originales (cinco ML y tres Alibaba), fuentes, cotizaciones publicadas y todas las demás celdas preservadas.
- **Gate de cierre F12 confirmado**: Data Fidelity Preflight v2.4 `PASS` + Matrix Validator 0.1.0 / schema `full-matrix-v5 0.7.0` `PASS` en el Mac del Founder, `phase=12`; errors=0, warnings=0, info=0, findings=[], limitations=[]. Log `validation-aut152-brand-cand-008-f12.log`.
- **Siguiente fase**: F13 habilitada por el doble PASS F12. `F14 NOT OPENED`; la actualización Git queda pendiente del checkpoint documental posterior a F13.

## Nota de cierre consolidada — 19/10/2026

La fase **F12 Margin + ROI** quedó **CLOSED** tras el doble PASS canónico de `aut152` (SHA-256 `3e970884eebbd4a39591c748c2d6af0f3e8aaf52fbdcbf82ee5101dedce077af`); no se reabren sus fuentes ni se altera la historia de la evaluación. La evidencia posterior se analiza en las fases siguientes, sin trasladar aprobaciones de un gate a otro.
