---
id: si-research-126
title: BRAND-CAND-009 — Method v2 Agile — Fase 9 — Headroom
description: Comparación aritmética trazable entre precios locales históricos y precios públicos Alibaba; sin landed cost ni margen.
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
phase: F9
mode: AUTO
baseline_revision: aut166
baseline_sha256: 51ad3d9d4d548a4804d6237004fa54a48d043ff03323e0f8810d917437e5cb95
matrix_revision: aut167
matrix_output: matrix-aut167-brand-cand-009-phase9-headroom.xlsx
matrix_sha256: eca04f469f0fea429f07c38c36569fc31d657729753e2316ff71c3660789f21f
structural_audit: PASS
validation_status: DOUBLE_PASS_CONFIRMED
publication_status: READY_FOR_F9_F13_DOCUMENTARY_CHECKPOINT
---

# SI-RESEARCH-126 — BRAND-CAND-009 — F9: Headroom

<!-- BRAND-CAND-009-F9-F13-CANONICAL-STATUS:START -->
## Estado canónico — cierre AUTO confirmado el 21/10/2026

**F9 CLOSED / AUTO / DOUBLE PASS CONFIRMED.** Matriz privada `aut167` con SHA-256 `eca04f469f0fea429f07c38c36569fc31d657729753e2316ff71c3660789f21f`; **Data Fidelity Preflight v2.4 PASS** y **Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` PASS**, sin errores, advertencias, findings o limitations. La auditoría estructural PASS preservó 29 hojas, 1.958 fórmulas, referencias y celdas históricas; únicamente cambió interpretación autorizada. No se requiere Founder Approval para una fase AUTO.

**Conclusión vigente:** Se conservaron siete comparaciones aritméticas trazables de precios históricos frente a precios públicos Alibaba; `COT-0075` — variante elástica adyacente — excluida del comparable directo. La diferencia de precios no acredita margen, FOB negociado, landed cost ni ROI. `BASE-FIT-012` continúa `SAFETY-GATED`.

**Gobierno:** F0–F8 estaban CLOSED/PUBLISHED en `234abec`. **F9–F13 quedan CLOSED a nivel metodológico; checkpoint documental F9–F13 en preparación, no publicado hasta commit/push. F14 NOT OPENED.** No se autorizaron RFQ, contacto comercial, muestras, homologación, negociación, importaciones, pedidos ni compras. Los datos económicos no confirmados conservan el estado desconocido.

> **Lectura histórica:** los párrafos posteriores que mencionan `PENDING_DOUBLE_PASS`, fases posteriores aún no abiertas o documentos privados describen el momento de materialización previo al cierre. Este bloque y el frontmatter reconciliado son el estado canónico vigente, sin alterar la evidencia original.
<!-- BRAND-CAND-009-F9-F13-CANONICAL-STATUS:END -->

## 1. Contrato, estado y pregunta

**F0–F6 PUBLISHED; F7–F8 CLOSED / DOCUMENTARY PUBLISHED** (commit `234abec`); F8 fue `COLLABORATIVE`, obtuvo doble PASS de `aut166` y aprobación expresa del Founder el 21/10/2026. **F9 AUTO / MATERIALIZED / PENDING_DOUBLE_PASS**, por lo que **NO está CLOSED** todavía. **F10 y F14 NOT OPENED**.

`SI-BIM-PROC-003 v1.0.7`, contrato por fase: **F9 = precio local + origen → Headroom; headroom ≠ landed cost**. La pregunta aquí es estrictamente: ¿hay diferencias aritméticas de precio **que justifiquen explorar** el dataset F10, sin prometer que se podrán capturar como ganancia?

Este Research mantiene la frontera **Capa A (precios/IDs/fechas) → Capa B (par comparable/adyacente) → Capa C (lectura) → Capa D (gate condicionado)**. No se asigna score de margen; `EVAL-0038 = 3/5, confianza baja` permanece inalterado.

## 2. Datos fuente y método

- **Precios locales históricos:** `ML-0189..0192`, capturas originales de Mercado Libre del **19/10/2026**, precio ARS core y USD coincidentes con su capa `ACTIVE / EXACT_SOURCE` de `Publicaciones ML` y `Verificaciones ML`. **FX ARS/USD 1.540**, asociado a la fecha **19/10/2026**, como tipo BNA billete vendedor reportado por una fuente **secundaria** Zion/Ámbito; **no hay captura oficial directa del BNA**. Mantenimiento íntegro de las fuentes `SRC-0544..0547` y de las verificaciones: **no se vuelven a consultar ni se reescribe el historial**.
- **Origen:** `Cotizaciones Proveedores.COT-0073..0080` y `Fuentes.SRC-0550..0557`, respaldadas por `EVID-0336..0343` / `EVSRC-0752..0759`; fichas Alibaba individuales y PDFs privados capturados durante F8. Aunque la hoja se denomina «Cotizaciones Proveedores», **son precios anunciados por tramo**; no hay cotización vinculante, FOB confirmado ni equivalencia industrial del SKU.
- **Cálculo aritmético descriptivo por pareja** (USD): `Brecha aparente = precio local USD publicado − precio público origen USD`; `Brecha aparente % = 100 × brecha / precio local USD`. Redondeo del resultado monetario a 2 decimales y del porcentaje a 1 decimal. La conversión USD de ML usa `ROUND(ARS / 1540, 2)` y se retiene el USD verificado preexistente. Los tramos **no se extrapolan** a cantidades inferiores. Sólo una arquitectura comparable con reservas habilita el *indicador exploratorio*; **la variante elástica `COT-0075` queda excluida** del cálculo comparable.

> **BRECHA APARENTE ≠ MARGEN BRUTO ≠ MARGEN NETO ≠ COSTO IMPORTADO ≠ FOB NEGOCIADO ≠ ROI.** El precio final argentino incluye impuestos, comisiones, logística, flete, gastos de importación, estructura, riesgo y otros componentes no estimados aquí. **Tampoco representa un precio propio factible.**

## 3. Matriz de ocho referencias con trazabilidad

Los PVP y valores de origen se expresan en **USD por unidad**, asociados al producto/variante, a la fecha histórica y al **tramo público indicado**; no se han unificado proveedores, materiales ni mecanismos. Los valores son ilustrativos, no cotizaciones actuales.

| Product Base | ML / precio local | Alibaba / source | Local USD | Origen USD | MOQ pública | Brecha USD | Brecha % del PVP | Lectura |
|---|---|---|---:|---:|---:|---:|---:|---|
| `BASE-FIT-010` | `ML-0189` | `COT-0073` / `SRC-0550` | 5,19 | 1,9 | 1 | 3,29 | 63,4 | Condicionado |
| `BASE-FIT-010` | `ML-0189` | `COT-0074` / `SRC-0551` | 5,19 | 1,44 | 100 | 3,75 | 72,3 | Condicionado |
| `BASE-FIT-010` | `ML-0189` | `COT-0075` / `SRC-0552` | 5,19 | 1,35 | 2 | — | — | **EXCLUIDO** |
| `BASE-FIT-011` | `ML-0190` | `COT-0076` / `SRC-0553` | 18,33 | 11,49 | 2 | 6,84 | 37,3 | Condicionado |
| `BASE-FIT-011` | `ML-0190` | `COT-0077` / `SRC-0554` | 18,33 | 12,45 | 50 | 5,88 | 32,1 | Condicionado |
| `BASE-FIT-011` | `ML-0190` | `COT-0078` / `SRC-0555` | 18,33 | 8,0 | 2 | 10,33 | 56,4 | Condicionado |
| `BASE-FIT-012` | `ML-0191` | `COT-0079` / `SRC-0556` | 14,28 | 3,4 | 1 | 10,88 | 76,2 | Descriptivo / SAFETY-GATED |
| `BASE-FIT-012` | `ML-0191` | `COT-0080` / `SRC-0557` | 14,28 | 1,82 | 200 | 12,46 | 87,3 | Descriptivo / SAFETY-GATED |

**`BASE-FIT-013` (tabla Freeman)**: la referencia local `ML-0192` está capturada en ARS **19.990** / USD **12,98**, pero **no existen ofertas de origen F8** para la PB. Por tanto, **headroom no calculable / DEFER — REOPENABLE**. Prohibido inventar origen, proxy o costo.

## 4. Interpretación por Product Base

### `BASE-FIT-010` — LEAD — CONDITIONAL

Precio local histórico `ML-0189 / SRC-0544`: **ARS 7.990 = USD 5,19** (FX 1.540). Dos referencias con similitud funcional:

- `COT-0073 / SRC-0550` **Mingying JH8-11**: precio público **USD 1,90**, diferencia aparente **USD 3,29 (63,4%)**; elasticidad y tracción reales no aclaradas.
- `COT-0074 / SRC-0551` **Changchun 10 bucles no elásticos anunciados**: precio público **USD 1,44** a **MOQ 100**, diferencia aparente **USD 3,75 (72,3%)**; texto contradictorio de elasticidad y fabricante no confirmado.

`COT-0075 / SRC-0552` **Shuoxing JT-007 ELÁSTICA** (USD 1,35) es sólo **ADYACENTE**, expresamente **sin headroom comparable**. Las diferencias no validan costos industriales, calidad, seguridad, disposición a pagar ni rentabilidad. El precio local bajo **amplifica el riesgo de que flete, impuestos y costos comerciales consuman toda la brecha**. La prioridad sigue LEAD **sólo para verificar F10**, no para importar.

### `BASE-FIT-011` — SECONDARY — CONDITIONAL

Precio local histórico `ML-0190 / SRC-0545`: **ARS 28.233,05 = USD 18,33**. `COT-0076` madera/plataforma única **USD 11,49** (brecha **USD 6,84; 37,3%**); `COT-0077` madera doble apoyo **USD 12,45 / MOQ 50** (brecha **USD 5,88; 32,1%**); `COT-0078` acero **USD 8** (brecha **USD 10,33; 56,4%**). **No son SKU equivalentes**: comparación contra GMP local de catorce niveles anunciados; CHENGMO ofrece cinco ángulos declarados, VICTORY doble apoyo y BNcompany acero. Las masas publicadas ~3–5 kg, dimensiones y empaquetado podrían generar costos significativos, **pero F9 no los cuantifica**. No inferir eficiencia logística ni seguridad.

### `BASE-FIT-012` — SAFETY-GATED, ARITMÉTICA SIN ELIGIBILIDAD

Precio local histórico `ML-0191 / SRC-0546`: **ARS 21.990 = USD 14,28**. `COT-0079` Yongsheng **USD 3,40** (brecha **USD 10,88; 76,2%**); `COT-0080` Bstar **USD 1,82 / MOQ 200** (brecha **USD 12,46; 87,3%**). Aunque el diferencial aritmético parece mayor, **no valida seguridad**. Permanecen pendientes presión de inflado, ensayos de carga/rotura/fatiga, fricción, advertencias, control del material y discrepancia **33 vs 34 cm** de Bstar. **Sin recomendación comercial ni de proveedor**, no convertir el indicador en una decisión de compra o homologación.

### `BASE-FIT-013` — DEFER — REOPENABLE

Sin cotización/origen comparable de F8, **no se calcula brecha**, ni se abre sourcing. Siguen pendientes evidencias reales de seguridad y diferenciación para reabrir.

## 5. Decisiones F9 y preparación de F10 (sin abrirla)

| Product Base | Lectura F9 propuesta | Límite obligatorio para fases posteriores |
|---|---|---|
| `BASE-FIT-010` | HEADROOM INDICATIVE / CONDITIONAL — posible examinar dataset F10 | Identidad de correa no elástica, tracción, costuras, MOQ y datos físicos por SKU; no RFQ antes de consulta externa |
| `BASE-FIT-011` | HEADROOM WEAK-TO-CONDITIONAL — interés metodológico secundario | Construcción distinta, peso/CBM, packing, fricción y mecanismo de bloqueo; no equivalencias forzadas |
| `BASE-FIT-012` | HEADROOM NUMERIC ONLY / SAFETY-GATED — no elegible comercialmente | F10 puede sólo documentar faltantes públicos; la falta de ensayos mantiene el STOP de seguridad |
| `BASE-FIT-013` | NO HEADROOM / DEFER — REOPENABLE | Ningún costo sustituido por proxy ni apertura automática de sourcing |

**F10**, cuando corresponda tras doble PASS de F9, sólo podrá construir un **Minimum Landed Dataset** con datos públicos **realmente observados** y vacíos explícitos. Prohibido inferir packing, gross weight o Incoterm ausente, simular FOB como cotización, hacer contactos/profundización, pedir muestras u homologar antes de las reuniones con el socio y el despachante. **F11–F12 no quedan autorizadas por un headroom positivo. F14 continúa NOT OPENED.**

## 6. Materialización, auditoría y gate

**Baseline F8 validada:** `matrix-aut166-brand-cand-009-phase8-origin-screening.xlsx` — SHA-256 `51ad3d9d4d548a4804d6237004fa54a48d043ff03323e0f8810d917437e5cb95`, **DOUBLE PASS y Founder APPROVED**. F7–F8 documentados y publicados en commit `234abec`.

**Snapshot F9:** `matrix-aut167-brand-cand-009-phase9-headroom.xlsx` — SHA-256 `eca04f469f0fea429f07c38c36569fc31d657729753e2316ff71c3660789f21f`. 29 hojas y **1.958 fórmulas preservadas**; **7 celdas lógicas modificadas exclusivamente**: `Nichos!AD41:AF41` y `Productos Base!N107:N110`. **Ninguna alta ni mutación** en `Publicaciones ML`, `Verificaciones ML`, `Cotizaciones Proveedores`, `Fuentes`, `Evidencias`, `Evidencia Fuentes`, `Evaluaciones`, `Simulación Margen` o vistas derivadas. El dataset machine-readable `headroom-ledger-aut167.json` es un derivado auditado (no se agrega a la matriz como fuente primaria ni se publica en Git).

**Resultado local de integridad estructural:** PASS en auditoría portátil. **Doble validación canónica:** `PENDING_ON_FOUNDER_MAC` hasta recibir log de `Data Fidelity Preflight v2.4` + `Matrix Validator 0.1.0 / full-matrix-v5 0.7.0`; **F9 no se cierra automáticamente por la sola auditoría estructural**.

**Siguiente gate si doble PASS:** revisión del resultado por el asistente, cierre **F9 AUTO** sin aprobación adicional del Founder, F10 **NOT OPENED** hasta iniciar deliberadamente. Research F9 se conserva privado hasta **checkpoint documental F9–F13**, salvo corrección justificada de gobierno. **No publicar XLSX, logs, PDFs ni manifiestos privados**.
