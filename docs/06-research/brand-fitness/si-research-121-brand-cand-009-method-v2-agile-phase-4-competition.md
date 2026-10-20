---
id: si-research-121
title: BRAND-CAND-009 — Method v2 Agile — Fase 4 — Competencia
version: 0.2.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-20
updated: 2026-10-20
brand: brand-fitness
brand_candidate: brand-cand-009
source_hypothesis: FIT-CAND-005
method: method-v2-agile
phase: F4
mode: AUTO
baseline: matrix-aut160-brand-cand-009-phase3-a5-coordination.xlsx
baseline_sha256: ff3f9fa529bc4e82789a64cf1c89657b154dff03439d6b802e457c003536b420
matrix_revision: aut162
matrix_output: matrix-aut162-brand-cand-009-phase4-competition-derived-view-correction.xlsx
matrix_sha256: 5017b62deeef096e150dedab749044fc64b71e400903b875d89e8efbe42a2f73
structural_audit: PASS_CORRECTED
validation_status: DOUBLE_PASS_CONFIRMED
phase_closure: CLOSED
publication_status: IN_F4_F6_DOCUMENTARY_CHECKPOINT
---

# SI-RESEARCH-121 — BRAND-CAND-009 — F4: Competencia

<!-- BRAND-CAND-009-F4-F6-CANONICAL-STATUS:START -->
## Estado canónico al checkpoint F4–F6 — 20/10/2026

**F4 CLOSED / AUTO.** `aut162`: Data Fidelity Preflight v2.4 PASS + Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` PASS, sin errores, advertencias ni limitaciones. `aut161` falló `DERIVED_VIEW_ROW_MISSING` y se conserva como intento no válido. `aut162` corrigió `Resumen Competencia Vista!A16:P16` incorporando 16 fórmulas sin alterar el histórico. Se documentaron seis observaciones `COMP-0187..0192`, sin extrapolar participación de mercado.

**Estado documental a esta fecha:** F0–F3 publicado; F4–F6 preparado para su checkpoint documental. **Estado operativo posterior:** F7 ya obtuvo doble PASS en la matriz privada `aut165` (SHA-256 `0630735db2ad9122e4eb93ab196393aa8dd971d1afe8c08cc09cefd781c20aae`), pero su Research `SI-RESEARCH-124` se publicará junto con F8 después de la revisión y aprobación expresa del Founder. **F8 NOT OPENED / F14 NOT OPENED.** Las menciones posteriores de `PENDING_DOUBLE_PASS` o `NOT OPENED` para fases ya validadas son fotografías de la ejecución anterior al log, no su estado actual. Ni la shortlist ni las PB implican autorización de importación.
<!-- BRAND-CAND-009-F4-F6-CANONICAL-STATUS:END -->


## Nota de corrección técnica — 20/10/2026

- `aut161` **FALLÓ** el Matrix Validator por `DERIVED_VIEW_ROW_MISSING`, registro `RES-COMP-0015`: faltaba `Resumen Competencia Vista!A16:P16`. El Data Fidelity Preflight v2.4 había dado **PASS**.
- La matriz `aut161` se preserva como **intento fallido**, no como baseline válida para F5.
- `aut162` repara **solamente esa fila derivada**, con 16 fórmulas y sus resultados correspondientes a `Resumen Competencia!A16:AE16`. Se conservaron íntegros los 36 componentes XLSX no afectados y las 15 filas previas de la hoja derivada.
- **Integridad estructural local: PASS.** La validación canónica de `aut162` todavía está **PENDING_DOUBLE_PASS**. F4 **NOT CLOSED** y F5 **NOT OPENED** hasta revisión del log.

## 1. Estado y objetivo

`BRAND-CAND-009 / FIT-CAND-005 / Marca Fitness — CORE`. **F0–F3 CLOSED**. F3 fue aprobada expresamente por el Founder el 19/10/2026; su baseline canónica es `aut160` con doble PASS. **F4 es AUTO**, está materializada en `aut162` y continúa **PENDING_DOUBLE_PASS** hasta revisar los dos validadores del Engine. **F5, F8 y F14 NO ABIERTAS**.

Pregunta de F4: ¿qué configuración competitiva exhiben las **mismas seis publicaciones capturadas en F3**, dónde hay evidencia de fortaleza comercial y qué brechas de producto o experiencia podrían justificar una propuesta de marca, sin confundir hipótesis con ventaja demostrada?

Contrato: [SI-BIM-PROC-003 v1.0.6](https://github.com/agelormini2024/smart-imports/blob/main/docs/02-business-intelligence-manual/procedures/si-bim-proc-003-method-v2-execution-contract.md), §4 (F4), §3 (capas), §13 (Minimum Sufficient Evidence) y §15 (gate). **No se releva ni se reconstruye demanda en F4**. Se utilizan los datos históricos de F3, sin nuevas capturas, precios ni ventas.

## 2. Cohorte y perímetro

| Arquitectura | Competidores analizados | IDs F4 | Lectura preliminar |
|---|---:|---|---|
| A1 — Movilidad articular guiada | 2 | `COMP-0187`, `COMP-0188` | Dos implementos funcionalmente diferentes: cinta y tabla inclinada |
| A2 — Deslizamiento controlado | 1 | `COMP-0191` | Deslizadores FITNESAS, con frontera de fuerza |
| A3 — Apoyos y transferencias | 0 | Sin fila F4 | Barra DRG como contexto adyacente, sin prueba de soporte seguro |
| A4 — Equilibrio con desafío graduable | 2 | `COMP-0189`, `COMP-0190` | Disco inflable y tabla rígida oscilante |
| A5 — Coordinación de pasos | 1 | `COMP-0192` | Escalera CHD con propuesta orientada a agilidad |
| **Total F4** | **6** | `COMP-0187..0192` | **Cinco vendedores identificables y seis marcas; no es un censo del mercado** |

**Identidades y concentración observada:** los seis productos se atribuyen a las marcas **Expert, GMP, PMG, New Plast, FITNESAS y CHD**. Se identifican cinco vendedores diferentes: EL REY DEL ENTRETENIMIENTO, tienda GMP, FONTANA DEPORTES, tienda FITNESAS y chaquideportes. **EL REY** aparece tanto en A1 como en A4, pero son productos y marcas distintos. Este solapamiento no permite declarar concentración sectorial ni calcular market share.

## 3. Hallazgos competitivos por arquitectura

### A1 — Movilidad guiada

- **Expert / cinta** (`ML-0189`, `COMP-0187`): en F3 se capturaron ARS 7.990, `+1000 vendidos`, 4,4/5 y 103 calificaciones. La correa con bucles ofrece una referencia de graduación simple, mientras que las opiniones difieren sobre la resistencia de costuras. La descripción promete alivio de dolor y menos lesiones sin ensayo clínico aportado: son **claims del vendedor**, no conclusión de Smart Imports.
- **GMP / tabla inclinada de 14 niveles** (`ML-0190`, `COMP-0188`): ARS 28.233,05, `+50 vendidos`, 3,9/5 y 12 calificaciones. Reseñas señalan que el nivel inicial podría resultar demasiado exigente para principiantes. El formato mecánico y el ticket no son directamente comparables a una cinta flexible.
- **Brecha hipotética:** progresión realmente graduada, instrucciones claras y ensayos de durabilidad, no una promesa preventiva de lesiones ni un precio premium supuesto. **Prioridad F5: núcleo condicionado.**

### A4 — Equilibrio graduable

- **PMG / disco inflable** (`ML-0191`, `COMP-0189`): ARS 21.990, `+1000 vendidos`, 4,0/5 con sólo 2 calificaciones. La ficha declara carga y antideslizamiento; no incluye en la captura prueba independiente que permita atribuir seguridad universal.
- **New Plast / tabla Freeman** (`ML-0192`, `COMP-0190`): ARS 19.990, `+50 vendidos`, 2,6/5 con 5 calificaciones. Las reseñas aluden a superficie sin antideslizante y resistencia deficiente. Son **señales de usuarios en una muestra muy pequeña**, no tasa de falla del producto.
- **Brecha hipotética:** estabilidad controlada, resistencia estructural, compatibilidad de superficies, límites de carga y progresión comprensible. Una eventual propuesta necesita verificar técnicamente los riesgos de caída. **Prioridad F5: núcleo condicionado con gate de seguridad alto.**

### A2 — Deslizamiento controlado

- **FITNESAS / discos Gliding Slider** (`ML-0193`, `COMP-0191`): ARS 8.900, `+500 vendidos`, 4,9/5 con 41 calificaciones. Las opiniones describen rayaduras y fricción variable según el piso. La presentación enfatiza trabajo de zona media y fuerza, por lo que el encaje con `009` es parcial.
- **Brecha hipotética:** guía de superficies y material compatible. No se ha demostrado demanda por un producto superior ni disposición a pagar más. **Prioridad F5: secundaria/condicionada por solapamiento con `BRAND-CAND-007`.**

### A5 — Coordinación de pasos

- **CHD / escalera de cinco escalones** (`ML-0194`, `COMP-0192`): ARS 7.500, `+100 vendidos`, 5,0/5 con apenas 2 calificaciones. El vendedor vende coordinación y velocidad, no progresión de capacidad física no clínica como propuesta central.
- **Brecha hipotética:** secuencias de baja complejidad, instrucciones por niveles y control de superficies. No se ha acreditado que estos beneficios justifiquen diferencial de marca. **Prioridad F5: secundaria.**

### A3 — Apoyos y transferencias

La barra doble de ballet DRG (`MLA-3385221556`, PDF privado) conserva carácter de **contexto excluido del ledger F3**. Una venta de ese artículo y su existencia en marketplace no acreditan idoneidad para cargar peso corporal, asistir incorporaciones ni transferencias seguras. **Sin fila `Competencia ML` para A3; prioridad baja y no extrapolar demanda directa.**

## 4. Lectura transversal: hecho, interpretación y decisión

| Dimensión | Evidencia factual | Interpretación acotada | Límite |
|---|---|---|---|
| Oferta | 6 publicaciones en 4 arquitecturas, 5 vendedores y 6 marcas | Existen implementaciones comerciales distintas | No representa el universo competitivo argentino |
| Precio | Precios históricos ARS de F3, sin recaptura | Hay tickets distintos por arquitectura y mecanismo | No comparar directamente A1 cinta con tabla inclinada ni precio con margen |
| Reputación | Calificaciones y reseñas tomadas literalmente en F3 | Temas de fricción, resistencia y progresión aparecen en algunos comentarios | N pequeño y sin auditoría de calidad |
| Fortaleza de vendedor | Tiendas oficiales, estatus MercadoLíder y volumen del vendedor en capturas | Barreras competitivas posibles por reputación y distribución | Ventas del vendedor no equivalen a ventas de cada producto |
| Diferenciación | Ninguna ventaja demostrada de una nueva marca | Posibles atributos: enseñanza progresiva, material y seguridad | No hay willingness-to-pay ni prestaciones ensayadas |
| Seguridad | Claims y reseñas, sin homologación | Especial atención en A4 y apoyos A3 | No afirmar certificación, ergonomía ni prevención de caídas |

**Saturación y concentración del mercado: NO DETERMINADAS.** La muestra es dirigida, pequeña y heterogénea; cualquier puntuación de saturación, cuota de mercado o competencia numérica sería artificial. Por este motivo `Nichos!F41` queda sin score nuevo, `Resumen Competencia` mantiene una lectura cualitativa y las celdas de puntaje por publicación no se rellenan sin método de scoring aprobado.

## 5. Recomendación operacional para F5 — Brand Potential

Mantener **A1 y A4** como hipótesis de función principal, sujetas a seguridad, progresión y evaluación del beneficio real del implemento. Conservar **A2 y A5** como soluciones complementarias/condicionadas; no promover A3 a propuesta de soporte o transferencia segura con la evidencia actual.

F5 deberá distinguir si una marca puede ofrecer una experiencia educativa/producto superior **demostrable** frente a accesorios genéricos; F4 no demuestra por sí sola el potencial de marca ni selecciona productos. Sigue prohibida la creación de Product Bases antes de F6. No sourcing, no MOQ, no FOB/EXW, no landed, no margen/ROI y no decisión de compra.

**Confianza F4: BAJA / CONDICIONADA.** Conclusión para el gate, si la matriz supera doble PASS: **F4 CLOSED WITH RESERVATIONS / F5 AUTO NEXT**. No requiere Founder Gate adicional por ser AUTO.

## 6. Fuentes originales, IDs y trazabilidad

Las capturas privadas están fechadas el **19/10/2026**. Se mantienen **exactamente las URLs históricas registradas en F3**, incluso sus parámetros, sin sustituirlas por URLs reconstruidas o snippets. Cada `COMP` enlaza a `Publicaciones ML` por `ML ID` y reutiliza el `Fuente Global ID` ya validado. El análisis se fechó el 20/10/2026; no es una nueva verificación de precio o ventas.

- `ML-0189` / `SRC-0544` / `EVID-0330` — Cinta De Elongación -pilates Yoga- Tela- Colores - El Rey. Captura: `Cinta De Elongación -pilates Yoga- Tela- Colores - El Rey _ MercadoLibre.pdf`. URL exacta de F3: https://articulo.mercadolibre.com.ar/MLA-776567826-cinta-de-elongacion-pilates-yoga-tela-colores-el-rey-_JM?searchVariation=34984704980
- `ML-0190` / `SRC-0545` / `EVID-0331` — Elongador Piernas Yoga Tabla Inclinada 14n. Flexibilidad Gmp. Captura: `Elongador Piernas Yoga Tabla Inclinada 14n. Flexibilidad Gmp _ MercadoLibre.pdf`. URL exacta de F3: https://articulo.mercadolibre.com.ar/MLA-1375597897-elongador-piernas-yoga-tabla-inclinada-14n-flexibilidad-gmp-_JM
- `ML-0191` / `SRC-0546` / `EVID-0332` — Disco Propiocepcion Equilibrio Balance Pinches Bosu - El Rey. Captura: `Disco Propiocepcion Equilibrio Balance Pinches Bosu - El Rey _ MercadoLibre.pdf`. URL exacta de F3: https://articulo.mercadolibre.com.ar/MLA-620026985-disco-propiocepcion-equilibrio-balance-pinches-bosu-el-rey-_JM
- `ML-0192` / `SRC-0547` / `EVID-0333` — Tabla De Equilibrio Freeman Propiocepción Disco Balance. Captura: `Tabla De Equilibrio Freeman Propiocepción Disco Balance _ MercadoLibre.pdf`. URL exacta de F3: https://articulo.mercadolibre.com.ar/MLA-780628597-tabla-de-equilibrio-freeman-propiocepcion-disco-balance-_JM
- `ML-0193` / `SRC-0548` / `EVID-0334` — Discos Deslizantes Gliding Slider Fitnesas (par). Captura: `A2-Discos Deslizantes Gliding Slider Fitnesas (par) _ MercadoLibre.pdf`. URL exacta de F3: https://www.mercadolibre.com.ar/discos-deslizantes-gliding-slider-fitnesas-par/up/MLAU3407738164?utm_source=chatgpt.com
- `ML-0194` / `SRC-0549` / `EVID-0335` — Escalera De Coordinación 5 Escalones, Fitness/ Entrenamiento. Captura: `A5-Escalera De Coordinación 5 Escalones, Fitness_ Entrenamiento _ MercadoLibre.pdf`. URL exacta de F3: https://articulo.mercadolibre.com.ar/MLA-931500547-escalera-de-coordinacion-5-escalones-fitness-entrenamiento-_JM

- Referencia A3 contextual: `A3-Barra Ballet Doble Portátil Regulable Danza 1alto X2ancho _ MercadoLibre.pdf`; publicación `MLA-3385221556`. No se incorpora como séptima publicación ni como competidor directo de transferencia.
- Fuente de verdad publicada: [SI-RESEARCH-120 — F3](https://github.com/agelormini2024/smart-imports/blob/main/docs/06-research/brand-fitness/si-research-120-brand-cand-009-method-v2-agile-phase-3-marketplace-demand.md).

## 7. Materialización, controles y gate pendiente

- **Baseline:** `matrix-aut160-brand-cand-009-phase3-a5-coordination.xlsx` — SHA-256 `ff3f9fa529bc4e82789a64cf1c89657b154dff03439d6b802e457c003536b420` (F3 CLOSED / DOUBLE PASS).
- **Snapshot F4 corregido:** `matrix-aut162-brand-cand-009-phase4-competition-derived-view-correction.xlsx` — SHA-256 `5017b62deeef096e150dedab749044fc64b71e400903b875d89e8efbe42a2f73`.
- **Delta de F4 sobre aut160:** `Nichos!AD41:AF41`, `Competencia ML!A188:Y193` y `Resumen Competencia!A16:AE16`. **Corrección aut161 → aut162:** sólo alta de `Resumen Competencia Vista!A16:P16` con 16 fórmulas derivadas del resumen canónico.
- **Nuevos IDs:** `COMP-0187..0192` y `RES-COMP-0015`. `ML-0189..0194`, `SRC-0544..0549`, `EVID-0330..0335` son referencias ya existentes, NO altas nuevas.
- **Integridad de aut162:** 29 hojas, 1.958 fórmulas (1.942 originales + 16 nuevas), 37 miembros XLSX, ninguna celda o fórmula histórica modificada; todos los URLs de F3 conservados y ninguna Product Base creada. Auditoría adjunta `audit-aut162-f4-correction.json`.
- **Estado canónico:** **PENDING_DOUBLE_PASS**. El Founder ejecutará un solo comando en Warp. Sólo después de recibir Data Fidelity Preflight v2.4 PASS y Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` PASS, y revisar el log, declararemos **F4 CLOSED**.
- **Git:** no publicar Research individual ahora; checkpoint documental posterior según roadmap. No ejecutar `git add`, `commit` ni `push` con este paquete.
