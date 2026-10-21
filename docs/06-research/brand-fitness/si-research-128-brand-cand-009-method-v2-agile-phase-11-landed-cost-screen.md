---
id: si-research-128
title: BRAND-CAND-009 — Method v2 Agile — Fase 11 — Landed Cost Screen
description: Pantalla de estrés económico hipotético; fronteras de factibilidad y lagunas documentadas sin falsear costo landed.
version: 0.1.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-21
updated: 2026-10-21
brand: brand-fitness
brand_candidate: BRAND-CAND-009
source_hypothesis: FIT-CAND-005
scope_alias: 'Marca Fitness — movilidad, estabilidad y conservación/recuperación de capacidad física'
phase: F11
mode: AUTO
baseline_revision: aut168
baseline_sha256: 84ac4470bbeb8e1e8d0fe03d9a76292d9a2d6b39988fd9bc7eaab1a17326cbf5
matrix_revision: aut169
matrix_output: matrix-aut169-brand-cand-009-phase11-landed-cost-screen.xlsx
matrix_sha256: 1c3119c7070bb70122bcde4100c1b01047237c093500def751f5bbcd27e1c8f8
structural_audit: PASS
validation_status: DOUBLE_PASS_CONFIRMED
publication_status: READY_FOR_F9_F13_DOCUMENTARY_CHECKPOINT
---

# SI-RESEARCH-128 — BRAND-CAND-009 — F11: Landed Cost Screen

<!-- BRAND-CAND-009-F9-F13-CANONICAL-STATUS:START -->
## Estado canónico — cierre AUTO confirmado el 21/10/2026

**F11 CLOSED / AUTO / DOUBLE PASS CONFIRMED.** Matriz privada `aut169` con SHA-256 `1c3119c7070bb70122bcde4100c1b01047237c093500def751f5bbcd27e1c8f8`; **Data Fidelity Preflight v2.4 PASS** y **Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` PASS**, sin errores, advertencias, findings o limitations. La auditoría estructural PASS preservó 29 hojas, 1.958 fórmulas, referencias y celdas históricas; únicamente cambió interpretación autorizada. No se requiere Founder Approval para una fase AUTO.

**Conclusión vigente:** Screen con escenarios matemáticos hipotéticos de multiplicadores 1,5×, 2× y 3×; **cero landed costs reales calculados**. Los supuestos no sustituyen NCM, impuestos, flete, packing ni cotización formal.

**Gobierno:** F0–F8 estaban CLOSED/PUBLISHED en `234abec`. **F9–F13 quedan CLOSED a nivel metodológico; checkpoint documental F9–F13 en preparación, no publicado hasta commit/push. F14 NOT OPENED.** No se autorizaron RFQ, contacto comercial, muestras, homologación, negociación, importaciones, pedidos ni compras. Los datos económicos no confirmados conservan el estado desconocido.

> **Lectura histórica:** los párrafos posteriores que mencionan `PENDING_DOUBLE_PASS`, fases posteriores aún no abiertas o documentos privados describen el momento de materialización previo al cierre. Este bloque y el frontmatter reconciliado son el estado canónico vigente, sin alterar la evidencia original.
<!-- BRAND-CAND-009-F9-F13-CANONICAL-STATUS:END -->

## 1. Contrato y gate

`SI-BIM-PROC-003 v1.0.7`: **F11 = «dataset F10 + supuestos → Landed Cost Screen», «no decisión final»**. F7–F8 CLOSED/PUBLISHED (commit `234abec`), F9 `aut167` DOUBLE PASS, F10 `aut168` DOUBLE PASS el 21/10/2026. **F11 AUTO materializada en `aut169` / doble PASS pendiente**. F12/F13/F14 NOT OPENED. El screen no constituye cálculo landed, selección de proveedor, aprobación de producto ni margen/ROI.

## 2. Fuente y nivel de confianza

- Capa A: precios locales `ML-0189..0192` en USD convertidos desde ARS con FX histórico **ARS 1.540/USD**, captura 19/10/2026 y base FX secundaria declarada, según ledger F9; precios públicos Alibaba `COT-0073..0080` con URL original, PDF SHA, tier/MOQ por modelo. Las ocho fichas estaban capturadas y vinculadas en F8; el ledger F10 conservó detalles físicos, discrepancias y ausencia de packing master.
- Capa B: `BASE-FIT-010` tiene dos referencias condicionadas y una **ELÁSTICA adyacente excluida** (`COT-0075`). `BASE-FIT-011` tiene tres arquitecturas distintas. `BASE-FIT-012` sólo aritmética diagnóstica **SAFETY-GATED**; `BASE-FIT-013` permanece diferida y sin origen.
- Capa C — **hipótesis matemática no observada**: factores sintéticos `1,5×`, `2×` y `3×` aplicados *únicamente* al precio público de origen. No representan multiplicadores reales de importación ni una desagregación estimada de tributos, seguros, flete, gastos aduaneros, comisiones o financiación.
- Capa D — límite de decisión: **LANDED_COST_NOT_DETERMINABLE_WITH_F10_DATA**. No hay master packing confirmado, NCM/tributos con despacho, FOB negociado, seguro, flete ni costos de canal. `UNKNOWN ≠ 0`.

## 3. Definiciones reproducibles

`Precio nocional del escenario USD = precio publicado en origen × factor sintético`.

`Múltiplo de paridad = precio histórico local USD / precio público origen USD`.

`¿Debajo de precio local? = precio nocional escenario < precio local USD`, comparación **exclusivamente aritmética**. Una diferencia positiva NO es margen; el precio local es una publicación minorista de tercero, no el PVP fijado para la futura marca. La fórmula de paridad no representa umbral económico suficiente para importar ni límite verdadero de costos: omite comisión de venta, impuestos, marketing, devoluciones y otras cargas, además de las de importación.

El stress test es una *prueba conceptual de sensibilidad*: factores seleccionados arbitrariamente para no fingir precisión. **No hay estimación de landed cost**. Todas las cifras se calculan por mismo par ML/COT del ledger, nunca mezclando SKU ni pesos de otras fichas. En especial, ninguna dimensión de paquete individual se convierte en CBM o flete mayorista.

## 4. Pantalla por oferta

Precios en USD; las columnas de escenario indican únicamente si el costo nocional queda **por debajo** del precio local en factores **1,5× / 2× / 3×**, respectivamente.

| COT | Product Base | Origen público USD | Local histórico USD | Paridad | 1,5× / 2× / 3× | Uso permitido |
|---|---|---:|---:|---:|---|---|
| `COT-0073` | `BASE-FIT-010` | 1.9 | 5.19 | 2.73x | Sí / Sí / No | CONDITIONAL_SCREEN_NOT_LANDED |
| `COT-0074` | `BASE-FIT-010` | 1.44 | 5.19 | 3.60x | Sí / Sí / Sí | CONDITIONAL_SCREEN_NOT_LANDED |
| `COT-0075` | `BASE-FIT-010` | 1.35 | 5.19 | — | — | EXCLUDED_ADJACENT_ELASTIC_NO_SCREEN |
| `COT-0076` | `BASE-FIT-011` | 11.49 | 18.33 | 1.60x | Sí / No / No | CONDITIONAL_SCREEN_NOT_LANDED |
| `COT-0077` | `BASE-FIT-011` | 12.45 | 18.33 | 1.47x | No / No / No | CONDITIONAL_SCREEN_NOT_LANDED |
| `COT-0078` | `BASE-FIT-011` | 8.0 | 18.33 | 2.29x | Sí / Sí / No | CONDITIONAL_SCREEN_NOT_LANDED |
| `COT-0079` | `BASE-FIT-012` | 3.4 | 14.28 | 4.20x | Sí / Sí / Sí | SAFETY_GATED_ARITHMETIC_ONLY |
| `COT-0080` | `BASE-FIT-012` | 1.82 | 14.28 | 7.85x | Sí / Sí / Sí | SAFETY_GATED_ARITHMETIC_ONLY |

**Lectura condicionada.** `BASE-FIT-010`: COT-0073 paridad 2,73× y COT-0074 paridad 3,60×; la brecha aparente es exploratoria con presión commodity, elasticidad/materiales/fabricante no homologados. `COT-0075` no se usa ni siquiera para escenarios por tratarse de variante elástica. `BASE-FIT-011`: COT-0076 1,60×; COT-0077 1,47×; COT-0078 2,29×. Se observa menor tolerancia aritmética al costo en las dos alternativas de madera, pero la comparación es parcial por diferencias de diseño, tamaño, masa y funciones; acero no constituye sustitución demostrada. `BASE-FIT-012`: COT-0079 4,20×; COT-0080 7,85× **son cifras diagnósticas sin habilitación comercial**, pues faltan pruebas mecánicas y reconciliación de modelo. `BASE-FIT-013`: no existe comparación ni escenario.

## 5. Riesgos y gates bloqueantes

| Dato o control necesario | Estado | Implicancia |
|---|---|---|
| Precio formal e Incoterm por SKU/MOQ | No confirmado | Público ≠ cotización |
| Master packing/unidades, CBM y peso bruto facturable | No verificados | No se puede modelar carga/flete |
| NCM, aranceles, impuestos, intervenciones | Pendiente despachante | No se puede calcular costo nacionalizado |
| Flete, seguro, gastos portuarios/aduaneros | No cotizados | No hay costo logístico real |
| Comisiones y cargas de canal / PVP propio | No modelados | No hay margen/ROI calculable |
| Ensayos estructurales y advertencias para discos | No acreditados | SAFETY-GATED sigue bloqueando avance comercial |
| Fabricante efectivo, homogeneidad de SKU y calidad | No verificados | No hay oferta procurement-grade |

Los datos se conseguirían **después** de reunión con socio y despachante, sólo si se autoriza profundización. No realizar RFQ, contacto, negociación, muestras ni compra ahora.

## 6. Resultado F11 y frontera hacia F12

- `BASE-FIT-010`: **LEAD — CONDITIONAL / ECONOMICALLY UNRESOLVED**. No confundir aparente resistencia a múltiples hipotéticos con margen demostrado.
- `BASE-FIT-011`: **SECONDARY — CONDITIONAL / LOGISTICS SENSITIVITY HIGH**. Especial atención a madera, dimensiones y variante acero; no decisión final.
- `BASE-FIT-012`: **SAFETY-GATED — NO COMMERCIAL CLEARANCE**. Los números no cambian el gate.
- `BASE-FIT-013`: **DEFER — REOPENABLE / NO ORIGIN**.

**F11: SCREEN COMPLETE WITH MATERIAL GAPS / REAL LANDED UNCALCULABLE**. F12, tras F11 DOUBLE PASS, deberá **interpretar** esta insuficiencia y analizar posibilidad/no disponibilidad de Margin + ROI *sin recalcular* importación ni inventar costes. F13 integrará gates y mantendrá F14 cerrado hasta revisión externa.

## 7. Materialización y validación

Baseline `aut168` SHA `84ac4470bbeb8e1e8d0fe03d9a76292d9a2d6b39988fd9bc7eaab1a17326cbf5`, Doble PASS del Founder. `aut169` SHA `1c3119c7070bb70122bcde4100c1b01047237c093500def751f5bbcd27e1c8f8`. Auditoría estructural local: 29 hojas, 1.958 fórmulas y cambios únicamente en `Nichos!AD41:AF41` y `Productos Base!N107:N110` (7 celdas). `Cotizaciones Proveedores`, `Simulación Margen`, `Fuentes`, `Evidencias`, `Publicaciones ML` y registros de verificación idénticos; no se alteran celdas históricas. `landed-screen-ledger-aut169.json` guarda los supuestos sintéticos y los enlaces de fuente por par.

**VALIDACIÓN CANÓNICA: PENDING_ON_FOUNDER_MAC** — obligatorio `Data Fidelity Preflight v2.4` más `Matrix Validator 0.1.0 / full-matrix-v5 0.7.0`. F11 no debe declararse CLOSED antes del log completo. Research privado hasta checkpoint F9–F13. No Git en esta etapa.
