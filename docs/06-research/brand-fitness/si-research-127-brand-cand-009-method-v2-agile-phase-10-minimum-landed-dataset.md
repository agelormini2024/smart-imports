---
id: si-research-127
title: BRAND-CAND-009 — Method v2 Agile — Fase 10 — Minimum Landed Dataset
description: Dataset mínimo de MOQ, precio público, peso y embalaje por SKU con reconciliación de discrepancias y campos desconocidos explícitos.
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
phase: F10
mode: AUTO
baseline_revision: aut167
baseline_sha256: eca04f469f0fea429f07c38c36569fc31d657729753e2316ff71c3660789f21f
matrix_revision: aut168
matrix_output: matrix-aut168-brand-cand-009-phase10-minimum-landed-dataset.xlsx
matrix_sha256: 84ac4470bbeb8e1e8d0fe03d9a76292d9a2d6b39988fd9bc7eaab1a17326cbf5
structural_audit: PASS
validation_status: DOUBLE_PASS_CONFIRMED
publication_status: READY_FOR_F9_F13_DOCUMENTARY_CHECKPOINT
---

# SI-RESEARCH-127 — BRAND-CAND-009 — F10: Minimum Landed Dataset

<!-- BRAND-CAND-009-F9-F13-CANONICAL-STATUS:START -->
## Estado canónico — cierre AUTO confirmado el 21/10/2026

**F10 CLOSED / AUTO / DOUBLE PASS CONFIRMED.** Matriz privada `aut168` con SHA-256 `84ac4470bbeb8e1e8d0fe03d9a76292d9a2d6b39988fd9bc7eaab1a17326cbf5`; **Data Fidelity Preflight v2.4 PASS** y **Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` PASS**, sin errores, advertencias, findings o limitations. La auditoría estructural PASS preservó 29 hojas, 1.958 fórmulas, referencias y celdas históricas; únicamente cambió interpretación autorizada. No se requiere Founder Approval para una fase AUTO.

**Conclusión vigente:** Dataset mínimo reconstruido con ocho ofertas y datos públicos observables; **cero master packing mayorista verificado**, CBM y pesos facturables indeterminados. Diferencias declaradas de pesos/medidas permanecen como advertencias y no se imputan.

**Gobierno:** F0–F8 estaban CLOSED/PUBLISHED en `234abec`. **F9–F13 quedan CLOSED a nivel metodológico; checkpoint documental F9–F13 en preparación, no publicado hasta commit/push. F14 NOT OPENED.** No se autorizaron RFQ, contacto comercial, muestras, homologación, negociación, importaciones, pedidos ni compras. Los datos económicos no confirmados conservan el estado desconocido.

> **Lectura histórica:** los párrafos posteriores que mencionan `PENDING_DOUBLE_PASS`, fases posteriores aún no abiertas o documentos privados describen el momento de materialización previo al cierre. Este bloque y el frontmatter reconciliado son el estado canónico vigente, sin alterar la evidencia original.
<!-- BRAND-CAND-009-F9-F13-CANONICAL-STATUS:END -->

## 1. Contrato operativo y estado

**F0–F8 CLOSED / PUBLISHED** en commit `234abec` (F8 COLLABORATIVE con aprobación expresa del Founder). **F9 CLOSED AUTO** en `aut167` por doble PASS canónico recibido el 21/10/2026 (SHA `eca04f469f0fea429f07c38c36569fc31d657729753e2316ff71c3660789f21f`). **F10 AUTO — MATERIALIZED / PENDING_DOUBLE_PASS**. F11/F12/F13/F14 no abiertos. No se requiere Founder Review para cerrar una fase AUTO que supera ambos validadores y la auditoría factual.

`SI-BIM-PROC-003 v1.0.7`: F10 = **«costo/MOQ/packing/peso → Minimum Landed Dataset»** y **«decision-grade ≠ procurement-grade»**. Aquí `costo` significa el **precio público del artículo en origen**, no un costo puesto en Argentina. Solo se reportan datos de la **misma publicación/SKU**; nunca se rellenan vacíos con otra oferta, promedios o datos de distintas variantes. F11 podrá, luego del doble PASS, estudiar estrés hipotético con supuestos expresos, nunca afirmar landed real sin documentación.

## 2. Proveniencia de fuentes y frontera entre capas

- **Capa A — hecho:** ocho fichas originales Alibaba (`COT-0073..0080`, `SRC-0550..0557`, `EVID-0336..0343`) aportadas en F8. Cada PDF fue vuelto a cotejar con el SHA-256 de `f8-source-manifest-009.json`. Precios y MOQ están anclados en `Cotizaciones Proveedores`. Las fichas son **ofertas de catálogo**, no cotizaciones vinculantes.
- **Capa B — clasificación:** los pesos/dimensiones anunciados en «Empaque y entrega» son del **artículo individual enviado en Alibaba**. No se convierten automáticamente en cajas master mayoristas, peso facturable o base de CBM para exportación. El volumen geométrico individual del ledger es una operación dimensional aritmética, no el volumen facturable de transporte.
- **Capa C — interpretación:** se explicitan conflictos de peso, dimensiones, unidades por caja, material/elasticidad y claims técnicos. Una coincidencia de número no prueba condiciones logísticas.
- **Capa D — decisión:** dataset `PARTIAL / MATERIAL GAPS`; ninguna base alcanza grado de compra; BASE-FIT-012 conserva `SAFETY-GATED` y BASE-FIT-013 `DEFER — REOPENABLE`.

La ficha de `COT-0079` indica en FAQ precio publicado tipo **EXW**, sin cotización formal. La FAQ de `COT-0075` enumera modalidades EXW/FOB, **sin vincularlas al valor unitario**. El resto: Incoterm del precio no confirmado. Ningún FOB negociado.

## 3. Dataset mínimo por publicación

Pesos y medidas de la columna «Paquete individual» pertenecen a la sección comercial de embalaje/envío de Alibaba; **no son master carton**. La columna de peso del producto es dato comercial no certificado; en Bstar **incluye bomba**.

| Oferta | Product Base | USD publicado / MOQ | Peso producto kg | Paquete individual cm | Bruto individual kg | Estado |
|---|---|---:|---:|---|---:|---|
| `COT-0073` | `BASE-FIT-010` | 1,9 / 1 | 0,115 | 15×10×3 | 0,5 | Condicionado |
| `COT-0074` | `BASE-FIT-010` | 1,44 / 100 | — | 14×14×5 | 0,108 | Condicionado |
| `COT-0075` | `BASE-FIT-010` | 1,35 / 2 | — | 30×15×8 | 0,25 | **ELÁSTICA ADYACENTE** |
| `COT-0076` | `BASE-FIT-011` | 11,49 / 2 | 3,65 | 42×32×20 | 5,0 | Condicionado |
| `COT-0077` | `BASE-FIT-011` | 12,45 / 50 | 5,0 | 50×40×30 | 5,0 | Condicionado |
| `COT-0078` | `BASE-FIT-011` | 8,0 / 2 | 3,3 | 40×10×40 | 10,0 | Condicionado |
| `COT-0079` | `BASE-FIT-012` | 3,4 / 1 | — | 38×38×8 | 2,0 | **SAFETY-GATED** |
| `COT-0080` | `BASE-FIT-012` | 1,82 / 200 | 0,9 | 36×36×10 | 1,2 | **SAFETY-GATED** |

`BASE-FIT-013`: ninguna oferta fuente en F8, por lo que no tiene datos F10. No se utilizan sus valores locales como proxy de origen.

## 4. Discrepancias y datos faltantes materiales

**`BASE-FIT-010` — LEAD CONDITIONAL.** `COT-0073/Mingying` declara 115 g netos, 132 g con caja de color y 500 g de peso bruto del paquete individual; la diferencia queda **sin resolver**, no se escoge el más conveniente. `COT-0074/Changchun` publica 108 g de bruto individual, pero no prueba peso neto, materiales ni fábrica del SKU; MOQ 100 de ese tramo y ficha con lenguaje elástico/no elástico contradictorio. `COT-0075/Shuoxing` es **ELÁSTICA** y continúa excluida como comparable directo; se conserva el dato logístico únicamente como referencia adyacente.

**`BASE-FIT-011` — SECONDARY CONDITIONAL.** `COT-0076/CHENGMO`: producto 3,65 kg y paquete 5 kg, madera plataforma única. `COT-0077/VICTORY`: producto y paquete listados en 5 kg, madera doble apoyo, claim carga 160 kg no ensayada. `COT-0078/BNcompany`: producto 3,3 kg frente a **10 kg de bruto individual** según logística Alibaba; acero, claim 150 kg no ensayado. No inferir que 10 kg corresponde al carton master ni que 3,3 kg es factura comprobada. Diferente arquitectura y peso significan que no hay SKU homogéneo para comparar fletes.

**`BASE-FIT-012` — SAFETY-GATED.** `COT-0079/Yongsheng`: bruto de paquete individual 2 kg, 38×38×8 cm, bolsa OPP anunciada, precio EXW en FAQ, pero sin ingeniería de embalaje ni ensayos mecánicos. `COT-0080/Bstar`: peso **900 g con bomba**, bruto individual 1,2 kg, embalaje individual 36×36×10 cm. La ficha declara además **20 piezas/caja y cartón 70×35×23 cm**. Ambos esquemas no están reconciliados; para 20 embalajes individuales de las dimensiones publicadas el volumen geométrico supera el del supuesto master, de modo que **no se puede utilizar como composición logística confirmada**. La diferencia 34 cm título vs 33 cm ficha permanece abierta; ninguno tiene ensayo de fricción, presión, carga o fatiga.

**`BASE-FIT-013` — DEFER.** No se buscó origen, peso, packing ni se creó proxy. Sólo un nuevo gate técnico y una decisión posterior podrán reabrirla.

## 5. Datos económicos y logísticos todavía desconocidos

| Campo requerido para un costo importado | Estado F10 |
|---|---|
| Precio origen por SKU y MOQ declarado | **PUBLICADO**, no confirmado contractualmente |
| Incoterm ligado al precio / fecha / puerto | **NO CONFIRMADO** (Yongsheng: EXW sólo en FAQ) |
| Packing MASTER / unidades por master | **NO VERIFICADO** (Bstar: claim contradictorio) |
| Peso bruto de envío mayorista | **NO VERIFICADO** |
| CBM master / volumen facturable | **NO VERIFICADO** |
| NCM, intervenciones, aranceles e impuestos de importación | **DESCONOCIDOS — pendiente despachante** |
| Flete real, seguro, despachante, almacenaje, gastos portuarios | **DESCONOCIDOS** |
| Costos/condiciones de canal y PVP propio | **NO MODELADOS** |
| Ensayos y homologación técnica | **NO VERIFICADOS; SAFETY-GATED para disco** |

**UNKNOWN ≠ 0**. `COT.P/Q/R` (CBM Caja, Peso Bruto Caja, Unidades por Caja) se mantienen **vacías** para las ocho ofertas, ya que su semántica exige caja comercial mayorista consistente; no se contaminan con dimensiones de paquete de consumidor. No hay modificaciones a `Simulación Margen`, `Resumen Margen`, `Cotizaciones Proveedores`, `Fuentes`, `Evidencias` o `Verificaciones ML`.

## 6. Decisión F10 y fronteras de F11

**F10 = DATASET MINIMUM COLLECTED WITH MATERIAL GAPS / NOT LANDED-CALCULABLE.** La captura pública alcanzó evidencia suficiente para detectar fricción y definir qué información faltaría tras la revisión externa, no para cotizar una importación. `BASE-FIT-010` sigue LEAD condicionado; `BASE-FIT-011` SECONDARY condicionado; `BASE-FIT-012` SAFETY-GATED; `BASE-FIT-013` DEFER — REOPENABLE.

**F11**, sólo después del doble PASS de F10, podrá evaluar *stress screens* claramente hipotéticos o determinar que el landed es indeterminable. Los pesos brutos individuales observados **no se transformarán en pesos facturables confirmados**. Ninguna fase habilita por sí sola RFQ, selección de proveedor, muestras, compra ni apertura de F14; contactos y profundización esperan reunión con socio y despachante.

## 7. Materialización y controles

Baseline inmutable `aut167` SHA `eca04f469f0fea429f07c38c36569fc31d657729753e2316ff71c3660789f21f` (F9 DOUBLE PASS). Snapshot `aut168` SHA `84ac4470bbeb8e1e8d0fe03d9a76292d9a2d6b39988fd9bc7eaab1a17326cbf5`. 29 hojas, 1.958 fórmulas conservadas y **sólo siete celdas de decisión/seguimiento** cambiadas: `Nichos!AD41:AF41`, `Productos Base!N107:N110`. Auditoría estructural PASS; source hashes de ocho PDFs PASS; código `audit-aut168-f10.py` reproduce las verificaciones. Dataset serializado separado como `minimum-landed-ledger-aut168.json` (fuente estructurada de trabajo, privado, no destinado a Git).

Doble PASS canónico `Data Fidelity Preflight v2.4` + `Matrix Validator 0.1.0 / full-matrix-v5 0.7.0`: **PENDING_ON_FOUNDER_MAC**. No declarar F10 CLOSED sin ese resultado. Research F10 privado hasta checkpoint F9–F13. Ningún Git add/commit/push en esta etapa.
