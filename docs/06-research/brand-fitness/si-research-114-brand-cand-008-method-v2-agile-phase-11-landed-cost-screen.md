---
id: si-research-114
title: BRAND-CAND-008 — Method v2 — F11 Landed Cost Screen
description: Sensibilidades aéreas no ejecutables de BASE-FIT-009 con proxy histórico, preservando los límites del dataset F10 y la trazabilidad de F8/F9.
version: 0.1.0
status: closed
owner: Alejandro Gelormini
created: 2026-10-19
updated: 2026-10-19
brand: brand-fitness
brand_candidate: BRAND-CAND-008
phase: F11
mode: AUTO
baseline: aut150
baseline_sha256: cfa223d219ce6bc8ad63a5318b00f656b259ea846405667bf062e848a06f3e57
matrix_revision: aut151
matrix_sha256: caa1d887543b0edcc2ada1e5ce0bf85ce7c80053e3a953378f8e7926066df860
validation_status: DOUBLE_PASS
publication_status: PREPARED_FOR_F4_F13_CHECKPOINT
---

# SI-RESEARCH-114 — BRAND-CAND-008 — F11 Landed Cost Screen

> **Estado vigente al 19/10/2026: F11 Landed Cost Screen CLOSED / Data Fidelity Preflight v2.4 PASS / Matrix Validator 0.1.0 PASS**, 0 errores, 0 advertencias, findings y limitations vacíos. Snapshot `aut151` — SHA-256 `caa1d887543b0edcc2ada1e5ce0bf85ce7c80053e3a953378f8e7926066df860`. Las menciones posteriores a estados pendientes reflejan el momento de redacción previo al cierre, no el estado vigente.

## 1. Alcance y política de evidencia

F11 (`AUTO`) toma el dataset F10 validado y prueba **restricciones económicas bajo supuestos expresos**, sin construir ni certificar un costo landed. El contrato `SI-BIM-PROC-003 v1.0.6` determina que F11 es un **Landed Cost Screen, sin decisión final**. Se adopta la política de sensibilidad ya documentada en `SI-RESEARCH-100` para `BRAND-CAND-007`: **USD 10 por kg facturable de flete aéreo como proxy histórico ilustrativo**, no tarifa vigente, no cotización, no ruta elegida ni plan logístico.

No se trasplantan aranceles, tasas, seguro, flete real, gastos de aduana, NCM o impuestos de otros candidatos. **Un peso de paquete individual declarado no equivale a peso facturable de embarque**, que puede incluir peso volumétrico y embalaje mayorista. Se mantiene la separación entre precio público Alibaba, precio FOB/EXW negociado, costo puesto en Argentina, precio de venta, margen y ROI.

F10: `SI-RESEARCH-113`, `aut150` doble PASS (29 hojas, 1.942 fórmulas); `BASE-FIT-009` única Product Base del candidato. Las ofertas F8 están vinculadas a PDFs privados capturados el 19/10/2026, `COT-0070..0072`, `SRC-0541..0543`, `EVID-0327..0329`, `EVSRC-0743..0745`. F8 fue aprobada expresamente por el Founder el 19/10/2026 con KESIDI principal condicionada. La cohorte marketplace F3 son cinco capturas; los precios locales específicos de F9 proceden de `ML-0185` Jazak y `ML-0184` MTL.

## 2. Fórmula y headroom que NO se recalcula

Del Research F9, a FX histórico **ARS 1.535/USD** y supuestos ilustrativos de canal 25%, comercial 5%, margen objetivo 25% del neto después del canal:

`H = PVP histórico USD × 0,5125`; para Jazak, `H_bajo = 7,6773 USD`, para MTL, `H_alto = 8,3435 USD` (magnitudes de cuatro decimales del screening). **No** se interpreta que KESIDI tenga asegurado el PVP de esos comparables, ni que las ventas incluyan la prima por contador o accesorios.

Definiciones del estrés: `O` = precio publicado del origen; `w` = **kg facturables hipotéticos, no peso real**; `r` = 10 USD/kg histórico hipotético; `C_parcial = O + r × w`. Se confronta `C_parcial` contra `H` sólo para entender cuán estrecha sería la tolerancia económica: **C_parcial NO ES LANDED COST**. Los costos desconocidos **no son cero**; están deliberadamente fuera de este escenario parcial.

## 3. KESIDI TH-PUB001 — referencia principal condicionada

**Origen observado:** `COT-0072` / `SRC-0543` / `EVID-0329`, precio publicado USD **6,50 por unidad** (tier 2–499), **no FOB/EXW**; el MOQ publicado es contradictorio (**2 vs 100**) y la vinculación del contador, apoyos y bandas con el precio de esta variante no está confirmada. En la ficha se observa **1,6 kg bruto de paquete individual**, no facturable certificado ni caja master; material PP y empaque final de importación no comprobados.

| Magnitud de estrés | Resultado USD | Interpretación |
|---|---:|---|
| `H_bajo – O` | 1,1773 | Tolerancia teórica *antes* de gastos, no margen |
| `H_alto – O` | 1,8435 | Ídem |
| Hipótesis **0,5 kg facturable** × 10 USD/kg | 5,00 sólo flete | `C_parcial = 11,50`, excede ambos headrooms |
| Hipótesis **1,0 kg facturable** × 10 USD/kg | 10,00 sólo flete | `C_parcial = 16,50`, excede ambos headrooms |
| Hipótesis **1,6 kg facturable** × 10 USD/kg | 16,00 sólo flete | `C_parcial = 22,50`, excede ambos headrooms; **1,6 es hipótesis basada sólo en peso bruto de presentación individual, no peso facturable confirmado** |
| Masa facturable máxima matemática `((H−O)/10)` | **0,1177–0,1844 kg** | Umbral antes de *cualquier* otro gasto y sin validar volumetría; no recomendación logística |

Incluso en una prueba de 0,5 kg el precio publicado más flete hipotético supera el techo teórico. La evidencia sostiene **`NON-EXECUTABLE AIR STRESS / UNFAVORABLE UNDER STATED ASSUMPTION / MARITIME UNDETERMINED / PREMIUM PVP UNPROVEN`**, no «margen negativo real» ni rechazo universal de cualquier vía marítima o variante.

## 4. 123Sports J001 — comparable económico secundario

**Origen observado:** `COT-0070` / `SRC-0541` / `EVID-0327`, USD **4,94/unidad**, tier 20–499, no FOB/EXW; material ABS, dimensiones de paquete individual y bruto publicado **2,0 kg**, no master carton ni peso facturable. Accesorios del precio base sin atribución confirmada.

| Magnitud de estrés | Resultado USD | Interpretación |
|---|---:|---|
| `H_bajo – O` / `H_alto – O` | **2,7373–3,4035** | Tolerancia teórica antes de todos los gastos |
| `0,5 kg` hipotético × 10 USD/kg | 5,00 sólo flete | `C_parcial = 9,94`, excede ambos headrooms |
| `1,0 kg` hipotético × 10 USD/kg | 10,00 sólo flete | `C_parcial = 14,94`, excede ambos headrooms |
| `2,0 kg` hipotético × 10 USD/kg | 20,00 sólo flete | `C_parcial = 24,94`, **condicional**, no masa facturable demostrada |
| Masa máxima matemática `((H−O)/10)` | **0,2737–0,3404 kg** | Umbral ideal anterior a todo otro gasto |

La comparación de precios J001 vs KESIDI es **no equivalente por funcionalidad**; no elegir automáticamente el producto más barato por este screen. Resultado: `NON-EXECUTABLE AIR STRESS / UNFAVORABLE UNDER STATED ASSUMPTION / VARIANT UNCONFIRMED / MARITIME UNDETERMINED`.

## 5. Aofeite — origen no reconciliado

`COT-0071` / `SRC-0542` / `EVID-0328`: listado USD **4,50/par**, material acero / «barra push up» y fotografías de tablero plegable inconsistentes. **No hacer estrés numérico ni conversión ficticia de par a tabla**; queda `NON-COMPARABLE UNTIL SKU + UNIT RECONCILED`.

## 6. Brechas, sesgos y decisiones permitidas

Se desconocen la variante exacta y sus accesorios, FOB/EXW negociado, MOQ vinculante, master carton, kg/CBM facturables, seguro, ruta, NCM, aranceles/tributos, aduana, gastos locales, QA/seguridad, garantías, prima de precio, rentabilidad y ROI. La sensibilidad aérea histórica **no prueba** viabilidad ni inviabilidad del transporte marítimo/LCL, ni ofrece un costo real para importación.

**Decisión técnica F11 propuesta — `AIR STRESS UNFAVORABLE UNDER EXPLICIT PROXY / LANDED NOT CALCULABLE / MARITIME UNDETERMINED / HOLD FOR EXTERNAL REVIEW`.** No hay autorización de compra, homologación, muestras, RFQ formal o compromiso de capital. KESIDI conserva prioridad **para revisión externa condicionada**, no calidad/precio homologados. Se mantiene el gate socio/despachante: sólo después de esas reuniones se definirá si tiene sentido profundizar proveedores y escenarios logísticos.

F12 (`AUTO`) deberá **interpretar los resultados F11 SIN recalcularlos** ni inventar margen / ROI numérico. F13 integrará demanda 2/5 Baja, competencia 2/5 Baja, potencial de marca 2/5 Baja, riesgos de seguridad y datos económicos para la Final Shortlist; `F14 NOT OPENED`.

## 7. Materialización y gate F11

- Entrada: `matrix-aut150-brand-cand-008-phase10-minimum-landed-dataset.xlsx`, SHA-256 `cfa223d219ce6bc8ad63a5318b00f656b259ea846405667bf062e848a06f3e57` (doble PASS F10, log `validation-aut150-brand-cand-008-f10.log`).
- Salida: `matrix-aut151-brand-cand-008-phase11-landed-cost-screen.xlsx`, SHA-256 `caa1d887543b0edcc2ada1e5ce0bf85ce7c80053e3a953378f8e7926066df860`.
- Sólo se autoriza modificar `Nichos!AD40:AF40` y `Productos Base!N106`, para comentarios narrativos y vínculos al Research. `Simulación Margen` y `Cotizaciones Proveedores` permanecen intactas; no se crea fila `MARG-`, tipo de cambio, costo o ROI inventado.
- Integridad requerida: 29 hojas, 1.942 fórmulas, cinco URLs ML y tres URLs Alibaba con sus parámetros originales completos; el resto del workbook debe ser inalterado.
- **Cierre:** `F11 CLOSED / AUTO`, confirmado en `validation-aut151-brand-cand-008-f11.log`: Data Fidelity Preflight v2.4 `PASS`, Matrix Validator 0.1.0 (`full-matrix-v5 0.7.0`) `PASS`; errores=0, warnings=0, findings=[] y limitations=[]. SHA-256 cotejado `caa1d887543b0edcc2ada1e5ce0bf85ce7c80053e3a953378f8e7926066df860`. F12 (`AUTO`) habilitada, sin apertura de F14.

## Nota de cierre consolidada — 19/10/2026

La fase **F11 Landed Cost Screen** quedó **CLOSED** tras el doble PASS canónico de `aut151` (SHA-256 `caa1d887543b0edcc2ada1e5ce0bf85ce7c80053e3a953378f8e7926066df860`); no se reabren sus fuentes ni se altera la historia de la evaluación. La evidencia posterior se analiza en las fases siguientes, sin trasladar aprobaciones de un gate a otro.
