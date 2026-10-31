---
id: si-roadmap-002
title: Project Status and Handoff
description: Estado operativo, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports.
version: 1.23.16
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-10-21
tags:
  - status
  - handoff
  - roadmap
  - continuity
related:
  - si-roadmap-001
  - si-agent-001
  - si-func-001
  - si-tech-001
  - si-tech-002
  - si-decision-010
  - si-decision-011
  - si-research-005
  - si-decision-014
  - si-research-006
  - si-decision-015
  - si-brand-001
  - si-brand-002
  - si-decision-016
  - si-decision-017
audience:
  - founder
  - partner
  - developer
  - assistant
phase: research
---

# SI-ROADMAP-002 — Estado actual y handoff de Smart Imports

<!-- RW-P001-CP03-DOCUMENTAL:START -->
## RW-P001 CP04 — Delta comercial, C08 y bicicletas TT (31/10/2026; DRAFT)

- **Documento:** `SI-RESEARCH-WORKBENCH-007` en `docs/06-research/research-workbench/`; síntesis pública. Anexo de ofertas, mensajes, PDFs y precios en custodia **privada** `RW-P001/CP04`; no subirlo a Git.
- **Revisión de Eduardo (30/10):** `C03` pasa a principal prioridad de atención, `C08` continúa condicionado y `C01` queda relegado/reabrible para primera importación. Entrevista cualitativa, no estadística representativa.
- **C08:** Tucson S10 aportó cotización con DHL para dos volúmenes; AURALIZ aporta evidencia visible en Argentina; Langston informó discontinuación de BE02, BE17/BE20 16 GB y quedó pendiente confirmación sobre BE17 32 GB. Sin landed, muestra o calidad comparable validada.
- **Nueva hipótesis `RW-P001-TT-001`:** tres referencias exploratorias de bicicletas TT (Twitter T3, Java TT Vega, T800/FLM). Posible prueba de 3–4 bicicletas **NO APROBADA**; necesidades de compradores, talles, armado, posventa, márgenes e importación pendientes.
- **Gate de marca y canal:** presencia argentina y autodeclaración de 'distribuidor oficial' NO acreditan por sí mismas representación/exclusividad. Twitter: presencia local declarada, posible conflicto comercial, HOLD. Java: oficialidad alegada por tercero, por confirmar. FLM/T800: titular/fabricante efectivo por identificar. Verificar con titular, INPI y asesor; no dar por prohibida ni por libre la importación por una sola evidencia.
- **Siguiente disparador:** información de campo de Eduardo en nueva reunión. No avanzar con RFQ profundo, muestras, compras ni proveedor homologado antes del despachante. CP03 documental sigue cerrado en `32fb5a0`, informes comerciales siguen DRAFT, `aut171` intacta.

## RW-P001 CP03 — Decision Reports piloto (30/10/2026; DRAFT)
- **Entregable del Workbench:** informe de oportunidad comercial para socio/despachante, derivado de investigación y matriz; no otro ciclo completo Method v2. Contrato piloto `SI-RESEARCH-WORKBENCH-005` y registro de versiones `SI-RESEARCH-WORKBENCH-006`, en `docs/06-research/research-workbench/`.
- **Informes preparados (privados):** C01 torquímetro v0.1, C03 chaleco hidratación 5L v0.1, C08 auriculares natación v0.4. C08 v0.4 revisa **solo el precio de venta hipotético** y su sensibilidad; demanda/quality/landed siguen no comprobados. Tres informes **DRAFT**; sin candidato comercialmente viable validado.
- **Economía didáctica:** costo puesto máximo, Headroom, pruebas de sensibilidad de landed **no calibradas**, margen/ROI económico y caja por separado; supuestos conservadores plausibles, nunca peor escenario imaginable; ausencia ⇒ NO CALCULABLE. No se modificó `aut171` histórico ni se homologó la matriz CP03 al Engine.
- **Delta de proveedores post-CP02:** C03-S01 Youk respondió; ronda original ahora **cinco con respuesta y dos sin respuesta**. Evidencia IPX8 Tucson S10 sigue parcial (una muestra; informe completo no recibido). CP02 4/3 es corte histórico, no error a reescribir.
- **Gate:** revisión Founder/socio → despachante para NCM/intervenciones/costo real → SOLO DESPUÉS investigación profunda de proveedores (muestras, QA, homologación, negociación) → selección final de 3–4 productos si procede. Ninguna compra autorizada; Method v2/F14 no se modifican.
- Evidencia, cotizaciones y PDFs completos fuera de Git, en custodia privada RW-P001/CP03. Próximo paso: feedback de Eduardo y contraste de mercado/equivalencia para C08, sin acelerar negociación.
<!-- RW-P001-CP03-DOCUMENTAL:END -->


<!-- RW-P001-CP02-REVIEW:START -->
## Research Workbench — RW-P001 CP02 (30/10/2026) — DRAFT / revisión pendiente
- Piloto de atleta amateur: exploración C01–C15; documento complementario `SI-RESEARCH-WORKBENCH-004` (no altera el Discovery Log `001` original en Biblioteca).
- Registro de siete consultas a proveedores: `SI-RESEARCH-WORKBENCH-002`; cuatro respuestas conocidas, tres sin respuesta registrada al cierre de ronda. Se preservan enlaces originales y discrepancias.
- Ranking de **prioridad de investigación** `SI-RESEARCH-WORKBENCH-003`: C03, C01 y C08 sujetos a evidencias y al filtro aduanero; **ningún producto aún comercialmente viable validado**.
- Estado: documentación en revisión, sin aprobación de inversión; no modifica Method v2, cierres F0–F13, ni abre F14. Documentación sensible y PDFs permanecen privados.
- Documentos: `docs/06-research/research-workbench/si-research-workbench-002-supplier-screening.md`, `si-research-workbench-003-commercial-pipeline.md`, `si-research-workbench-004-pilot-001-c01-c15-addendum.md`.
<!-- RW-P001-CP02-REVIEW:END -->

<!-- BRAND-CAND-009-F9-F13-DOCUMENTARY-CHECKPOINT:START -->
## BRAND-CAND-009 — Checkpoint Method v2 F9–F13 (2026-10-21)

**F0–F13 CLOSED / F9–F13 AUTO — DOUBLE PASS EN LAS CINCO FASES / SHORTLIST CONDICIONADA PARA REVISIÓN EXTERNA.** F0–F8 publicados en `234abec`, F8 COLLABORATIVE aprobado expresamente por Founder el 21/10/2026. Contrato `SI-BIM-PROC-003 v1.0.7`: checkpoint conjunto F9–F13. **F14 NOT OPENED**; no se autoriza profundización de proveedores, RFQ, muestras ni compras.

- **F9 — Headroom:** `aut167` DOUBLE PASS, SHA-256 `eca04f469f0fea429f07c38c36569fc31d657729753e2316ff71c3660789f21f`. Siete pares aritméticos; diferencia de precios ≠ margen; variante elástica adyacente `COT-0075` excluida.
- **F10 — Minimum Landed Dataset:** `aut168` DOUBLE PASS, SHA-256 `84ac4470bbeb8e1e8d0fe03d9a76292d9a2d6b39988fd9bc7eaab1a17326cbf5`. Ocho ofertas, cero master packing verificado; faltantes logísticos explícitos.
- **F11 — Landed Cost Screen:** `aut169` DOUBLE PASS, SHA-256 `1c3119c7070bb70122bcde4100c1b01047237c093500def751f5bbcd27e1c8f8`. Factores hipotéticos 1,5×/2×/3×; **landed real indeterminado**.
- **F12 — Margin + ROI:** `aut170` DOUBLE PASS, SHA-256 `8af1e46af2d70d40baac83667ad80cb1476284bc2258398bd442ba14c849f4b0`. **Margen y ROI NO CALCULABLES**; no son cero.
- **F13 — Final Shortlist:** `aut171` DOUBLE PASS, SHA-256 `e938ff75c3f7f51052965e0cfa46b5ba7c3e7cd4ab03f613a0fb020b8684b6b7`. **`BASE-FIT-010 FINALIST — CONDITIONED`** para revisión externa; **`BASE-FIT-011 SECONDARY RESERVE — CONDITIONED`**; `BASE-FIT-012 NOT COMMERCIAL FINALIST — SAFETY-GATED`; `BASE-FIT-013 DEFER — REOPENABLE`. `EVAL-0038 = 3/5`, confianza baja.

En las cinco fases: **Data Fidelity Preflight v2.4 PASS + Matrix Validator 0.1.0 (`full-matrix-v5 0.7.0`) PASS**, sin errores, advertencias, hallazgos ni limitaciones. `aut171` contiene 29 hojas y 1.958 fórmulas; ni los datos comerciales históricos ni las evidencias de F8 fueron reescritos fuera de las celdas autorizadas.

**Decisión y próximo gate:** Method v2 F0–F13 completo para este candidato, sin proveedores homologados ni producto autorizado para importar. La revisión con el socio y el despachante definirá la fricción importadora, las prioridades reales de portfolio y qué producto merecería profundización. **No abrir F14 automáticamente.** XLSX, PDFs, logs, manifests y ledgers permanecen privados y fuera de Git. Los checkpoints F0–F3, F4–F6 y F7–F8 debajo de éste son historia vigente de sus respectivas etapas, no estado más reciente.

<!-- BRAND-CAND-009-F9-F13-DOCUMENTARY-CHECKPOINT:END -->

<!-- BRAND-CAND-009-F7-F8-DOCUMENTARY-CHECKPOINT:START -->
## BRAND-CAND-009 — Checkpoint Method v2 F7–F8 (2026-10-21)

**F7–F8 CLOSED / DOUBLE PASS EN AMBAS FASES / F8 COLLABORATIVE — FOUNDER REVIEW APPROVED EXPRESAMENTE (21/10/2026).** Contrato aprobado `SI-BIM-PROC-003 v1.0.7`; cadencia documental F0–F3, F4–F6, F7–F8 y F9–F13. El checkpoint F4–F6 ya se publicó en `b10fa2c`. Se preserva la auditoría real del Governance Preflight pre-F8 (GOV-001..009 PASS, commit `58cad04`).

- **F7 — Shortlist pre-origin, AUTO:** `SI-RESEARCH-124`; matriz privada `aut165` con **Data Fidelity Preflight v2.4 PASS y Matrix Validator 0.1.0 / full-matrix-v5 0.7.0 PASS**, SHA-256 `0630735db2ad9122e4eb93ab196393aa8dd971d1afe8c08cc09cefd781c20aae`. Cuatro Product Bases: `BASE-FIT-010` LEAD — CONDITIONAL; `BASE-FIT-011` SECONDARY — CONDITIONAL; `BASE-FIT-012` SAFETY-GATED; `BASE-FIT-013` DEFER — REOPENABLE.
- **F8 — Origin Screening / Alibaba, COLLABORATIVE:** `SI-RESEARCH-125`; matriz privada `aut166` con **Data Fidelity Preflight v2.4 PASS y Matrix Validator 0.1.0 / full-matrix-v5 0.7.0 PASS**, SHA-256 `51ad3d9d4d548a4804d6237004fa54a48d043ff03323e0f8810d917437e5cb95`. Cero errores, advertencias, findings y limitations. El Founder **aprobó expresamente el cierre el 21/10/2026**, con todas las reservas documentadas.
- **Evidencias F8:** ocho fichas individuales Alibaba, ocho fuentes, ocho evidencias y ocho vínculos; `BASE-FIT-010` 3 (incluida una variante **elástica ADYACENTE**, no equivalencia exacta a la PB no elástica), `BASE-FIT-011` 3 (madera simple, doble y acero), `BASE-FIT-012` 2 (**SAFETY-GATED**) y `BASE-FIT-013` 0 (**DEFER**). La URL que mostraba sólo recomendaciones se excluyó. No se duplicaron PDFs idénticos.

**Reservas:** oferta en Alibaba ≠ fabricante efectivo del SKU; publicación ≠ cotización formal; precios de pantalla ≠ FOB negociado; verificación del proveedor o claims RoHS/CP65/CE/carga ≠ homologación de seguridad. La selección, las muestras, RFQ, ensayos y la profundización del proveedor quedan diferidas hasta conversar con el socio y el despachante. **Ningún proveedor o producto aprobado para importar; F9 NOT OPENED; F14 NOT OPENED.** Las matrices, PDFs, logs y respaldos siguen fuera de Git.

<!-- BRAND-CAND-009-F7-F8-DOCUMENTARY-CHECKPOINT:END -->

<!-- BRAND-CAND-009-F4-F6-DOCUMENTARY-CHECKPOINT:START -->
## BRAND-CAND-009 — Checkpoint Method v2 F4–F6 (2026-10-20)

**F4–F6 CLOSED / AUTO / DOUBLE PASS POR FASE.** Este checkpoint regulariza la publicación documental omitida después de F6. No reabre ni invalida F7. No se ejecutaron búsquedas de origen en F8 ni se autorizaron compras.

- **F4 Competencia** — `SI-RESEARCH-121`, `aut162` DOBLE PASS, SHA-256 `5017b62deeef096e150dedab749044fc64b71e400903b875d89e8efbe42a2f73`. Se registraron seis comparables `COMP-0187..0192`; `aut161` falló `DERIVED_VIEW_ROW_MISSING` y se conserva como intento histórico NO VALIDADO. `aut162` corrigió la fila derivada de `RES-COMP-0015`.
- **F5 Potencial de Marca** — `SI-RESEARCH-122`, `aut163` DOBLE PASS, SHA-256 `0d19fd39ca2dad470258e283286ffd443c8d58f9f03e2cffadd71f7ae5d352bd`. Evaluación `EVAL-0038`: **3/5, confianza baja**; diferenciación hipotética, no demostrada.
- **F6 Product Bases** — `SI-RESEARCH-123`, `aut164` DOBLE PASS, SHA-256 `3e39e5e00b2c6b3706ed0b152d6d5a8d7c684df21d3eb5ea5b0d503426315a8c`. Bases candidatas `BASE-FIT-010..013`, sin aprobación de SKU, proveedor ni compra.

**Estado de continuidad que no integra esta publicación:** F7 SHORTLIST PRE-ORIGIN ya fue validada técnicamente (AUTO, `aut165` DOBLE PASS, SHA-256 `0630735db2ad9122e4eb93ab196393aa8dd971d1afe8c08cc09cefd781c20aae`). Su Research `SI-RESEARCH-124` se reserva para el checkpoint **F7–F8**, después de ejecutar F8 colaborativamente, recibir aprobación expresa del Founder y obtener doble PASS. **F8 NOT OPENED; F14 NOT OPENED.**

**Límites:** seis publicaciones y seis verificaciones de F3 preservadas; cuatro PB candidatas, ninguna selección comercial definitiva. No hay costos FOB/EXW ni landed, rentabilidad acreditada, seguridad homologada, equivalencia OEM ni autorización de compra. El contador histórico de ventas de ML no representa ventas mensuales ni tamaño de mercado.

**Trazabilidad:** `SI-RESEARCH-121..123` de este checkpoint y baseline privada `aut164`; `SI-RESEARCH-124` + `aut165` son posteriores y permanecen fuera de esta publicación documental. PDFs, XLSX, logs y respaldos son privados, fuera de Git.

<!-- BRAND-CAND-009-F4-F6-DOCUMENTARY-CHECKPOINT:END -->

<!-- BRAND-CAND-009-F0-F3-DOCUMENTARY-CHECKPOINT:START -->
## BRAND-CAND-009 — Checkpoint Method v2 F0–F3 (2026-10-19)

**F0–F3 CLOSED / aut160 DOBLE PASS / F3 COLLABORATIVE con aprobación expresa del Founder (19/10/2026).** F0, F1 y F2 fueron AUTO. Investigación de movilidad, estabilidad y capacidad física no clínica, `FIT-CAND-005` / `CORE`.

- F0 Research Brief `aut154` — DOUBLE PASS — `04c3ee21055858cca8d439c0130c2a8284b56795aa84d9cbbae9d7eb2ea8ef6c`.
- F1 Solution Map `aut155` — DOUBLE PASS — `607a97df651d6c78914e0880c70b40d13509d45e73c17026b45dea02fb762208`; cinco arquitecturas, ninguna Product Base.
- F2 Maturity `aut156` — DOUBLE PASS — `ad35b330bdafb64d64ec3eeff13e72df71c95819026eab68038d1ac648119fd1`; madurez de mecanismos no acredita seguridad del producto.
- F3 Demanda Marketplace `aut160` — DOUBLE PASS — `ff3f9fa529bc4e82789a64cf1c89657b154dff03439d6b802e457c003536b420`; **6 publicaciones** y **6 verificaciones de ledger**, 0 Product Bases; A1=2, A2=1, A3=0 (referencia contextual), A4=2, A5=1.

**Lectura aprobada con reservas:** A1 y A4 tienen señales comerciales locales y requieren comprobaciones de progresión y seguridad; A2 y A5 son secundarias/condicionadas; A3 no acredita apoyo o transferencias seguras ni demanda directa. Confianza cualitativa **baja/condicionada**, sin score numérico aprobado. Los contadores son acumulados visibles, no demanda mensual ni un mercado dimensionado. No se aprobaron proveedores, márgenes, costos de importación, Product Bases ni compras.

**Historial de corrección F3:** `aut157` falló `DF-MLV-028` ×4; `aut158` reconciliado y doble PASS, `aut159` doble PASS y `aut160` doble PASS. `aut157` NO es baseline válida.

**Fuente documental:** `SI-RESEARCH-117..120` en `docs/06-research/brand-fitness/`; `SI-BIM-PROC-003 v1.0.6`. **Siguiente paso F4 — Competencia, AUTO, NOT OPENED**: reutilizar la misma cohorte F3, sin recolectar/reinventar demanda. **F14 NOT OPENED.** Matrices XLSX, PDFs y logs privados fuera de Git.
<!-- BRAND-CAND-009-F0-F3-DOCUMENTARY-CHECKPOINT:END -->

<!-- BRAND-CAND-008-F4-F13-FINAL-CHECKPOINT:START -->
## BRAND-CAND-008 — Cierre Method v2 F4–F13 (2026-10-19)

**F0–F13 CLOSED / NO FINALIST / FREEZE — REOPENABLE.** La única Product Base es **`BASE-FIT-009` — tabla plegable para flexiones con agarres reconfigurables**: `DEFER — REOPENABLE / PORTFOLIO WATCHLIST / NOT FIRST-STAGE FIT`. No está en la shortlist de primera importación. **F14 NOT OPENED**.

**Resultados:** Demanda (F3) **2/5 Baja**, Competencia (F4) **2/5 Baja**, Potencial de Marca (F5) **2/5 Baja**. F6 se reconcilió mediante corrección Tipo B: `aut145` con cero PB es histórico válido; `aut146` normalizó una única PB. F7 exploratorio condicionado; F8 aprobado explícitamente por Founder el 19/10/2026, KESIDI como referencia condicionada; F9–F12 sin landed, margen ni ROI confirmados; F13 sin finalistas. No hubo homologación, RFQ formal ni autorización de compra.

```text
F4  aut143-r1: b9945f9feb58f5c5a17e56896f6c14e24b31724a70546c66f82244dfbfa3672c — DOUBLE PASS
F5  aut144: 73ce0b6ccdb960277e969e11878e7e56ae661a3b71a0b63bc52581fc2a1c496a — DOUBLE PASS
F6  aut145 HISTORICAL: 73ce0b6ccdb960277e969e11878e7e56ae661a3b71a0b63bc52581fc2a1c496a — DOUBLE PASS
F6  aut146 RECONCILED: 7fa57317c2ec2987c162644a16a234e7156e93eac47534da52ac43448d06525e — DOUBLE PASS
F7  aut147: 68e5b7797a05d33e289f1dd928507b434414673ef98c313e82a999ec318392d5 — DOUBLE PASS
F8  aut148: 786676c581f97a972f38688a7dc6e0a27371e535c4cf224360fed71afa45c2c4 — DOUBLE PASS
F9  aut149: 88aa184fd9668d9e47efd68f4ea7348ac2a08214cd1f47d265ba9360c890e0ec — DOUBLE PASS
F10 aut150: cfa223d219ce6bc8ad63a5318b00f656b259ea846405667bf062e848a06f3e57 — DOUBLE PASS
F11 aut151: caa1d887543b0edcc2ada1e5ce0bf85ce7c80053e3a953378f8e7926066df860 — DOUBLE PASS
F12 aut152: 3e970884eebbd4a39591c748c2d6af0f3e8aaf52fbdcbf82ee5101dedce077af — DOUBLE PASS
F13 aut153: 4c88c0ac2e4d459f17707da38d8f4b72fb7cdaf0d157dc1d3e8b8c4505b10540 — DOUBLE PASS
Data Fidelity Preflight v2.4: PASS
Matrix Validator 0.1.0 / full-matrix-v5 0.7.0: PASS, 0 errors / 0 warnings
F14: NOT OPENED
```

**Origen:** tres referencias Alibaba con URL original y PDFs privados: KESIDI `COT-0072`, 123Sports `COT-0070`, Aofeite `COT-0071`; cinco publicaciones ML preservadas. **Economía:** headroom teórico USD 7,68–8,34; origen KESIDI público USD 6,50; estrés aéreo desfavorable bajo proxy histórico; marítimo indeterminado. No inventar costos landed, margen, ROI ni viabilidad regulatoria. Reevaluar únicamente tras reuniones con socio y despachante y evidencia nueva verificable.

**Documentación:** `SI-RESEARCH-107..116`, `decision-report-brand-cand-008-para-socio-y-despachante.md`, `SI-METHOD-NOTE-001`. PDFs, XLSX, logs y scripts de trabajo permanecen privados.
<!-- BRAND-CAND-008-F4-F13-FINAL-CHECKPOINT:END -->

<!-- BRAND-CAND-008-F0-F3-CHECKPOINT:START -->
## BRAND-CAND-008 — Checkpoint Method v2 F0–F3 (2026-10-16)

**F0–F3 CLOSED / Demanda 2/5 / Confianza Baja / aut142-r1 DOBLE PASS.** F0–F2 AUTO; F3 COLLABORATIVE con aprobación explícita del Founder el 16/10/2026. Cinco publicaciones de Mercado Libre con URLs, PDF privados y referencias cruzadas; no hay Product Bases.

```text
F0 — aut139 — PASS — ffc2478f2f1ebd46dfb7dd4242b48ea2187c4190f9f39543bd5653b15f0c99ed
F1 — aut140 — PASS — e757eea904bb4f117d2be20d83903b3adb646ed66c1d85575205d55f2d5b39ab
F2 — aut141 — PASS — d0332a267fac3b7c0ae48e776f10d965100864a0c0dc563d839fdeab9cb6deca
F3 — aut142-r1 — PASS — 97b3260521630f7e00067946a3cc23341f965f1b209a8a5a7d65da0f5c9fdaf0
EVAL-0035 — Demanda 2/5 — Confianza Baja
Data Fidelity Preflight v2.4: PASS
Matrix Validator 0.1.0 / full-matrix-v5 0.7.0: PASS
F4 — NEXT / AUTO / NOT OPENED
F14 — NOT OPENED
```

**Lectura:** las ventas observadas en artículos adyacentes no validan demanda por entrenamiento flexible entre contextos. Cuatro de cinco referencias tienen ticket inferior a ARS 50.000; ese importe es una alerta orientativa, no regla excluyente ni rentabilidad demostrada. El primer `aut142` falló por tres códigos `COMPARABLE_ADYACENTE` en lugar de `ADJACENT`; `aut142-r1` corrigió sólo esas tres celdas y obtuvo doble PASS. No se reabre F3, no se transfiere demanda del candidato `007` y no se abre F8.

**Trazabilidad:** `ML-0184..0188`, `SRC-0536..0540`, `EVID-0317..0321`, `EVSRC-0733..0737`, `MLV-0033..0037`, `EVAL-0035`. Los cinco enlaces originales y hashes de PDF están documentados en `SI-RESEARCH-106` y la matriz privada. XLSX, PDF y logs no se publican.

**Siguiente bloque:** F4 Competencia → F5 Potencial de Marca → F6 Product Bases, AUTO, con el siguiente checkpoint documental después de F6; ninguna Product Base está definida antes de F6. La reunión con socio/despachante permanece como gate externo separado.
<!-- BRAND-CAND-008-F0-F3-CHECKPOINT:END -->


<!-- BRAND-CAND-007-F9-F13-CHECKPOINT:START -->
## BRAND-CAND-007 — Cierre Method v2 F9–F13 (2026-10-14)

**F0–F13 CLOSED / aut138 DOBLE PASS / SHORTLIST PARA REVISIÓN EXTERNA — CONDICIONADA.** F9–F13 se ejecutaron en modalidad **AUTO**, conservando Data Fidelity Preflight v2.4 PASS y Matrix Validator `full-matrix-v5 0.7.0` PASS por cada matriz. **F14 NOT OPENED.**

```text
F9 — Import Cost Headroom      aut134 — PASS — cdfd9960d7f1a36222a85c9c31c242a6259d84cef334cf2e259ada3131322071
F10 — Minimum Landed Dataset   aut135 — PASS — def947f2fa6dcde1a5596e3a16829ab9cd0be514228a778edfd10b1d68ca0c7b
F11 — Landed Cost Screen       aut136 — PASS — 2e2a9728768b884c407b1abdc0ebbc4a9e0063f85a39f270a59b73fe34c619c6
F12 — Margin + ROI             aut137 — PASS — bae4d15aca6f6599ae7895ae59b6284c5fb917014b08bed531fb1683eb2d82ca
F13 — Final Shortlist          aut138 — PASS — a7fbea16213714e0adee4e153c9910a538174c1e75850998df1754d596b147dd
BASE-FIT-005 — EXTERNAL REVIEW SHORTLIST / LEAD CONDITIONED / HOLD
BASE-FIT-007 — EXTERNAL REVIEW SHORTLIST / CONDITIONED / HOLD
BASE-FIT-006 — DEFER — REOPENABLE / COMMODITY + JOB PROOF
BASE-FIT-008 — DEFER — REOPENABLE / CRITICAL SAFETY GATE
ECONOMIC / PROCUREMENT FINALIST: NONE WITH CURRENT EVIDENCE
F14: NOT OPENED
```

**Interpretación económica:** headroom es techo teórico, no landed. F11 usa un proxy aéreo de estrés **no ejecutable**; las alternativas marítimas, tributos/NCM y requisitos aplicables están pendientes de evaluación profesional. **No hay landed confirmado, margen ni ROI numéricos defendibles.** La consulta breve enviada a dos proveedores de mancuernas 20 kg no constituye homologación y sus respuestas se incorporarán con fuente y fecha cuando estén disponibles; no se presupone resultado alguno.

**Próxima acción:** usar `docs/06-research/brand-fitness/decision-report-brand-cand-007-para-socio-y-despachante.md` junto con `SI-RESEARCH-098..102` en la reunión con el socio y despachante. **Sólo después** decidir qué Product Bases o proveedores profundizar y si revisar escenarios de costos con datos concretos. No hubo RFQ formal, muestras, proveedor aprobado, compra o apertura de F14. Las matrices, logs y PDF permanecen privados fuera de Git.
<!-- BRAND-CAND-007-F9-F13-CHECKPOINT:END -->

<!-- BRAND-CAND-007-F7-F8-CHECKPOINT:START -->
## BRAND-CAND-007 — Checkpoint único F7–F8 (2026-10-14)

**F7–F8 CLOSED / aut133 PASS / HOLD para revisión externa.** F7 AUTO y F8 COLLABORATIVE culminaron con Data Fidelity Preflight v2.4 y Matrix Validator `full-matrix-v5 0.7.0` **PASS** en ambas matrices, sin errores, warnings, findings ni limitations. La aprobación del Founder para F8 se registra **expresamente** al ejecutar este checkpoint. La matriz `aut133` constituye un snapshot técnico **previo** a dicha aprobación; no se modifica retroactivamente.

```text
F7 Shortlist Pre-Origin: aut132 — CLOSED / AUTO / PASS
F7 SHA-256: ca2aa758788c53be1307aa10bb0c3b7ba03cbda0126141b1eb121844979d828b
F8 Origin Screening: aut133 — CLOSED / COLLABORATIVE / DOUBLE PASS / FOUNDER REVIEW APPROVED
F8 SHA-256: 02a689d96fd98d2b46fea21aa5d6630fa27eff7a5f0e0cfa10d61bae6f8b1ccf
F8 ofertas Alibaba observadas: COT-0065..0069 (5); SRC-0531..0535; EVID-0312..0316; EVSRC-0728..0732
BASE-FIT-005 — HOLD / dos ofertas observadas / seguridad, ensayo de bandas-anclajes y condiciones no homologadas
BASE-FIT-007 — HOLD / tres ofertas observadas / variantes 10-15-20 kg exploratorias, materiales y logística sin resolver
BASE-FIT-006 — DEFER / reabrible con demanda específica y diferenciación verificable
BASE-FIT-008 — DEFER / reabrible únicamente con base de seguridad técnica suficiente
F9: NOT OPENED
```

**No se eligieron proveedores, no hubo RFQ ni muestras, no se definieron costos FOB/landed ni importaciones.** La profundización de producto/proveedor permanece en pausa hasta la reunión con el socio y el despachante; éstos deben informar las fricciones regulatorias, logísticas, económicas y de calidad que permitirán decidir reaperturas y prioridades. `SI-RESEARCH-096` y `SI-RESEARCH-097` documentan la trazabilidad. Los cinco PDF y las matrices permanecen privados fuera de Git. No se abrió `BRAND-CAND-008..009` en paralelo.
<!-- BRAND-CAND-007-F7-F8-CHECKPOINT:END -->

<!-- BRAND-CAND-007-F4-F6-CHECKPOINT:START -->
## BRAND-CAND-007 — Checkpoint F4–F6 (2026-10-14)

**F4–F6 CLOSED — aut131 PASS.** Ejecución AUTO con validación canónica en cada fase y un único checkpoint documental conjunto. Se reutilizó la cohorte de seis publicaciones F3, sin alterar sus ventas, precios, FX ni el ledger histórico.

```text
F4 — Competencia: CLOSED / aut129 PASS / EVAL-0033: 3/5, Confianza Media
F5 — Potencial de Marca: CLOSED / aut130 PASS / EVAL-0034: 3/5, Confianza Baja
F6 — Product Bases: CLOSED / aut131 PASS / BASE-FIT-005..008 (4)
F7 — Shortlist Pre-Origin: NEXT / AUTO
F8 — Origin Screening: COLLABORATIVE / Founder Review REQUIRED
Data Fidelity Preflight v2.4 + Matrix Validator full-matrix-v5 0.7.0: PASS en F4, F5 y F6
SHA-256 aut129: 287d0f6bd93ce167b92f8967c2cf1690d0a620d58829e8cb827f13481983294f
SHA-256 aut130: 8ba9d75fa09c0bf03a78372d4b9255190af27825f2272f77458f326cfbbdd106
SHA-256 aut131: 99477da455a27a477245b5e4bc66c00992597f1b1ff32c2ab6376258f54c078d
```

Documentos nuevos: `SI-RESEARCH-093..095` en `docs/06-research/brand-fitness/`. Product Bases normalizadas: `BASE-FIT-005` bandas tubulares, `BASE-FIT-006` bandas loop, `BASE-FIT-007` mancuernas/barra ajustables 20 kg y `BASE-FIT-008` sistema de suspensión. Se mantienen riesgos pendientes de seguridad y durabilidad, y **no hay finalista, proveedor ni recomendación de importación**. La matriz permanece privada, fuera de Git.
<!-- BRAND-CAND-007-F4-F6-CHECKPOINT:END -->

<!-- BRAND-CAND-007-F0-F3-CHECKPOINT:START -->
## BRAND-CAND-007 — Checkpoint F0–F3 (2026-10-13)

`FIT-CAND-001 — Fuerza accesible y compacta` llegó a F3 con ejecución AUTO en F0–F2 y revisión COLLABORATIVE en F3. Alejandro aprobó **Demanda 3/5 / Confianza Media** sobre seis capturas de Mercado Libre (dos elásticas, dos de carga ajustable y dos de suspensión), capturadas el 2026-10-13.

```text
F0 CLOSED — aut124 PASS (4899f4fc595ebe1e07a4b245e5cf1cf300183f6bcd04c3937916f104a13bf108)
F1 CLOSED — aut125 PASS (b3b51eec44716a9d55e17a7d8adf7347bf06adc6a894afd5fb9afec417029aac)
F2 CLOSED — aut126 PASS (f55bdc6b4eb08c377e50dba79952f23955fcb7e1e7bb40c640313905ae32c0f1)
F3 CLOSED — aut128 PASS (3fd9bce9fe32866ea30f33e26e3b3eaf9753a36e3223faf200618f8c8c4aba30)
EVAL-0032 — Demanda 3/5 / Confianza Media
Data Fidelity Preflight v2.4 + Matrix Validator full-matrix-v5 0.7.0: PASS
NEXT: F4→F6 AUTO; próximo checkpoint documental al finalizar F6
Product Bases: NO (F6 es primer gate habilitado)
```

Research: `SI-RESEARCH-089..092` en `docs/06-research/brand-fitness/`. Fuente de trazabilidad estructurada: matriz privada `aut128`; no se incorporan PDF de captura ni datos privados al repositorio.
<!-- BRAND-CAND-007-F0-F3-CHECKPOINT:END -->

<!-- FITNESS-PRESCREENING-V02:START -->
## Checkpoint operativo — BRAND-CAND-010 Method v2 cerrado / 2026-10-08

```text
SCREENING: CLOSED
METHOD V2: F0–F13 CLOSED
F13 MATRIX: matrix-aut118-brand-cand-010-phase13-final-corrected.xlsx
F13 SHA-256: 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a
POST-CLOSE BASELINE: matrix-aut123-brand-cand-010-post-close-core-snapshot-reconciliation.xlsx
POST-CLOSE SHA-256: 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb
Data Fidelity Preflight: PASS
Matrix Validator: PASS / errors 0 / warnings 0 / info 0
F14: NOT OPENED

FINAL RESULT: NO PORTFOLIO FINALIST

BASE-FIT-001 — Walking pad compacta under-desk
→ STOP — REOPENABLE / LOGISTICS GATE
→ principal hipótesis de reapertura

BASE-FIT-002 — Pedalera compacta under-desk
→ STOP — REOPENABLE / DEMAND + LOGISTICS GATE

BASE-FIT-003 — Elíptica compacta under-desk
→ DEFER — LOW DEMAND PROOF

BASE-FIT-004 — Balance board para standing desk
→ DEFER — LOW DEMAND PROOF / STANDING-DESK DEPENDENCY

BRAND-CAND-007 → F0–F13 CLOSED / aut138 PASS / EXTERNAL REVIEW READY / F14 NOT OPENED
BRAND-CAND-008 → ELIGIBLE — NOT OPENED
BRAND-CAND-009 → ELIGIBLE — NOT OPENED
```

La walking pad queda como principal hipótesis de reapertura porque fue la única arquitectura con demanda local específica defendible, pero el screen de landed cost aéreo la deja fuera de shortlist final. Reabrir exige evidencia logística marítima/LCL decision-grade y validación de requisitos eléctricos, QA y postventa.

`NO FINALIST` no equivale a descartar definitivamente el candidato. Significa que, con la evidencia disponible y los supuestos comparables del Method v2, ninguna Product Base justifica pasar hoy a Portfolio Review como finalista.

Próximo gate de Marca Fitness: `BRAND-CAND-007` F0–F13 CLOSED / aut138 doble PASS; Decision Report listo para reunión con socio y despachante, sin finalista económico ni F14 abierto. `BRAND-CAND-008..009` elegibles sin abrir.
<!-- FITNESS-PRESCREENING-V02:END -->

<!-- HOGAR-PAUSE-AND-OPPORTUNITY-INTAKE:START -->
## Checkpoint operativo — cierre interno Marca Hogar / 2026-10-07

```text
INTERNAL PORTFOLIO REVIEW: COMPLETE
FIRST-STAGE LEAD: BASE-HOGAR-016
BACKUP: BASE-HOGAR-006 — LOCAL DEMAND NOT YET CONFIRMED
SECONDARY: BASE-HOGAR-010 / BASE-HOGAR-002
RESERVE: BASE-HOGAR-028 / BASE-PET-003
BRAND-CAND-002: DEFERRED / PAUSED
EXTERNAL REVIEW: PENDING
PROCUREMENT: NOT OPENED
F14: NOT OPENED
PORTFOLIO BASELINE: FROZEN
```

Portfolio Review: `SI-RESEARCH-071`.
Decisión: `SI-DECISION-017`.

`aut104` permanece como último snapshot de Hogar. Portfolio Review no consume `aut`; `aut105` queda reservado para `BRAND-CAND-010 / Marca Fitness`.

Fuente: `docs/07-brand/brands/brand-hogar/brand-hogar-external-review-pause-checkpoint.md`.

### Mejora metodológica reusable

Se mantiene `SI-BRAND-003 — Ingreso de oportunidades y descubrimiento`.

El sistema admite descubrimiento descendente `territorio → misión → problema → solución → producto` y descubrimiento ascendente `producto → solución → problema → misión → territorio`. Ambas rutas convergen en Brand Candidate Screening antes de Method v2.

```text
ORIGEN DE LA IDEA ≠ CALIDAD DE LA OPORTUNIDAD
```

Fuente: `docs/07-brand/si-brand-003-opportunity-intake-and-discovery.md`.
<!-- HOGAR-PAUSE-AND-OPPORTUNITY-INTAKE:END -->

<!-- BRAND-CAND-006-HANDOFF:START -->
## Checkpoint operativo — BRAND-CAND-006 / 2026-10-05

```text
BRAND-CAND-006
Mode: RETROSPECTIVE + REUSE + RECONCILIATION

F0 CLOSED — aut91 PASS
F1 CLOSED — aut92 PASS
F2 CLOSED — aut93 PASS
F3 CLOSED — aut94 corrected PASS
F4 CLOSED — aut95 PASS
F5 CLOSED — aut96 PASS
F6 CLOSED — aut97 PASS
F7 CLOSED — aut98 PASS
F8 CLOSED — aut99 PASS
F9 CLOSED — aut100 PASS
F10 CLOSED — aut101 PASS
F11 CLOSED — aut102 PASS
F12 CLOSED — aut103 PASS
F13 CLOSED — aut104 PASS
F14 NOT OPENED

Finalist: BASE-PET-003 — FINALIST — CONDITIONED
Portfolio eligibility: ELIGIBLE FOR PORTFOLIO REVIEW
First-stage fit: NOT FIRST-STAGE FIT
Candidate status: PORTFOLIO REVIEW READY / FREEZE
```

Snapshot final:

```text
matrix-aut104-brand-cand-006-phase13.xlsx
SHA-256: a5caeebe1954b59ea1bf37e29b22e8961820305b743584eaf5355b0439cd056e
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Research publicado: `SI-RESEARCH-056..069`.

La identidad de `BASE-PET-003` se preserva `REUSE AS-IS`.

La reconciliación global `aut96..aut104` queda completa. `BRAND-CAND-010 / aut105` queda desbloqueado como siguiente target operativo, todavía pendiente de materialización.
<!-- BRAND-CAND-006-HANDOFF:END -->

<!-- BRAND-CANDIDATE-DOC-CLOSE-RULE:START -->
## Regla obligatoria — cierre documental antes del siguiente Brand Candidate

El cierre operativo de un Brand Candidate **no termina con el PASS de F13**.

Secuencia obligatoria de cierre:

```text
F13 validada con PASS
→ publicar SI-RESEARCH de F0–F13 en smart-imports
→ actualizar expediente del Brand Candidate
→ actualizar índices de Research y Marca Hogar
→ actualizar README raíz
→ actualizar SI-ROADMAP-002
→ ejecutar verificación documental y git diff --check
→ git add / commit / push con aprobación humana
→ recién entonces abrir el siguiente Brand Candidate
```

Reglas derivadas:

- ningún candidato siguiente se abre mientras el anterior esté sólo cerrado en chat/matriz;
- la fuente de continuidad es el repo `smart-imports`, no la conversación;
- `commit` y `push` siguen siendo pasos humanos explícitos;
- un candidato en `FREEZE` no se reabre para sourcing/F14 salvo Portfolio Review, revisión externa o contradicción material.

Esta regla aplica a todos los Brand Candidates actuales y futuros.
<!-- BRAND-CANDIDATE-DOC-CLOSE-RULE:END -->

<!-- BRAND-CAND-005-HANDOFF:START -->
## Checkpoint operativo — BRAND-CAND-005 / 2026-09-30

```text
Method v2 Agile: Fases 0–13 CLOSED
Snapshot comercial vigente: matrix-aut90-brand-cand-005-phase13.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 2bb0e30d75f98d9d90b60942b0b84ea409544e0966b5d5a4fd88e51fc65fbe9e
Finalist: BASE-HOGAR-028 — FINALIST — CONDITIONED
Portfolio eligibility: ELIGIBLE FOR PORTFOLIO REVIEW
First-stage fit: NOT FIRST-STAGE FIT
Portfolio status: PORTFOLIO REVIEW READY
Candidate status: FREEZE
F14: NOT OPENED
```

`BASE-HOGAR-024` queda `STOP — REOPENABLE`. `BASE-HOGAR-025` queda `STOP — REOPENABLE / LOGISTICS GATE`. `BASE-HOGAR-028` sobrevive condicionado por demanda local débil/no visible, postventa de electrodoméstico, compatibilidad eléctrica exacta, filtros/repuestos, warranty, documentación/certificaciones, seguridad y disciplina de claims sobre el output.

Próxima secuencia:

```text
DOCUMENTARY CLOSE BRAND-CAND-005
→ verificación documental / git diff --check
→ git add / commit / push humano
→ BRAND-CAND-006 — residuos de mascotas
→ Portfolio Review global
→ revisión externa
→ selección para profundización
→ decisión sobre F14
```

No reabrir F14 ni tratar el finalista como producto listo antes de Portfolio Review y gate externo.
<!-- BRAND-CAND-005-HANDOFF:END -->

<!-- BRAND-CAND-004-HANDOFF:START -->
## Checkpoint operativo — BRAND-CAND-004 / 2026-09-25

```text
Method v2 Agile: Fases 0–13 CLOSED
Snapshot comercial vigente: matrix-aut72-brand-cand-004-phase13.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 560fd2073da35327babe7a473c726e012f8d5496223f98c9d4f1dd5212948ced
Finalist: BASE-HOGAR-016 — FINALIST — CONDITIONED
Portfolio status: PORTFOLIO REVIEW READY
Candidate status: FREEZE
F14: NOT OPENED
```

`BASE-HOGAR-017` y `BASE-HOGAR-019` quedan `STOP — REOPENABLE`. `BASE-HOGAR-016` sobrevive condicionado por accuracy/test evidence, configuración eléctrica exacta, plug Argentina/AU, packing/peso same-SKU, certificación/requisitos locales y futura revisión externa.

Próxima secuencia:

```text
DOCUMENTARY CLOSE BRAND-CAND-004
→ BRAND-CAND-005
→ BRAND-CAND-006
→ Portfolio Review global
→ revisión externa
→ selección para profundización
→ decisión sobre F14
```
<!-- BRAND-CAND-004-HANDOFF:END -->

<!-- BRAND-CAND-003-HANDOFF:START -->
## Checkpoint operativo — BRAND-CAND-003 / 2026-09-25

```text
Method v2 Agile: Fases 0–13 CLOSED
Snapshot comercial vigente: matrix-aut58-brand-cand-003-phase13.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: ec5c8b8f52cc3ae13c2d759e41b4f90f568948fa03676271ce585894d80c44da
Finalist: BASE-HOGAR-010 — FINALIST — CONDITIONED
Portfolio status: PORTFOLIO REVIEW READY
Candidate status: FREEZE
F14: NOT OPENED
```

`BASE-HOGAR-009` y `BASE-HOGAR-011` quedan `STOP — REOPENABLE`. `BASE-HOGAR-010` sobrevive condicionado por materialidad/capacidad del sorbente, claims, filtros/repuestos, compatibilidad eléctrica y futura revisión externa.

`BRAND-CAND-002` permanece `PASS TO METHOD V2 — DEFERRED / PAUSED`. La pausa responde a una preocupación del founder sobre aprobación/costo regulatorio; requiere revisión externa y **no** se registra como conclusión regulatoria verificada.

`BRAND-CAND-002` permanece `PASS TO METHOD V2 — DEFERRED / PAUSED`. La pausa responde a una preocupación del founder sobre aprobación/costo regulatorio, pendiente de revisión externa; **no se registra como conclusión regulatoria verificada**.

Próxima secuencia obligatoria:

```text
BRAND-CAND-004
→ BRAND-CAND-005
→ BRAND-CAND-006
→ Portfolio Review global
→ revisión externa
→ selección para profundización
→ decisión sobre F14
```
<!-- BRAND-CAND-003-HANDOFF:END -->

<!-- SI-F13-CHECKPOINT:START -->
## Checkpoint operativo — BRAND-CAND-001 / 2026-09-24

```text
Golden Run Method v2: Fases 0–13 CLOSED
Snapshot comercial vigente: matrix-aut44-brand-cand-001-phase13-corrected.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 37b2b37c5c61355efec271b7ecb49df74c2264e2f721830a1c2478858a850f56
Portfolio status: PORTFOLIO REVIEW READY
F14: NOT OPENED
```

F13 conserva `BASE-HOGAR-002` y `BASE-HOGAR-006` como `FINALIST — CONDITIONED`. `BRAND-CAND-001` queda en `FREEZE`: completar los candidatos restantes hasta F13, comparar finalistas y realizar revisión externa —incluido despachante— antes de decidir qué producto abre F14.
<!-- SI-F13-CHECKPOINT:END -->

<!-- SI-F12-CHECKPOINT:START -->
## Checkpoint operativo — BRAND-CAND-001 / 2026-09-23

```text
Golden Run Method v2: Fases 0–12 CLOSED
Snapshot comercial vigente: matrix-aut43-brand-cand-001-phase12.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 5b602747404dce8584c3735552009487607ffe4a642c56bb05b8b9aba0663315
Next gate: F13 — Shortlist final
```

F12 reduce el camino activo a `BASE-HOGAR-002` y `BASE-HOGAR-006`, ambos condicionados. `BASE-HOGAR-003` queda STOP — REOPENABLE. No reabrir sourcing ni negociación fina salvo evidencia material nueva.
<!-- SI-F12-CHECKPOINT:END -->

<!-- SI-F11-CHECKPOINT:START -->
## Checkpoint operativo — BRAND-CAND-001 / 2026-09-23

```text
Golden Run Method v2: Fases 0–11 CLOSED
Snapshot comercial vigente: matrix-aut42-brand-cand-001-phase11.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 6204f672b70d9e4629ee047aac31e25044b93e37037c9db98a303cc95cb6361c
Next gate: F12 — Margin + ROI
```

F11 cerró seis escenarios decision-grade de Landed Cost para `BASE-HOGAR-002`, `BASE-HOGAR-003` y `BASE-HOGAR-006`. Los tres pasan a F12 condicionados. No reabrir sourcing, negociación fina ni Matrix Validator salvo contradicción material o bloqueo real.
<!-- SI-F11-CHECKPOINT:END -->

> Punto de entrada operativo obligatorio para retomar el proyecto sin depender de un chat específico.

## 1. Fuentes de verdad

```text
Documentación y negocio:
https://github.com/agelormini2024/smart-imports

Software ejecutable:
https://github.com/agelormini2024/smart-imports-engine

Snapshot comercial vigente:
matrix-aut58-brand-cand-003-phase13.xlsx
→ full-matrix-v5 0.7.0
→ PASS limpio

Baseline técnica de release:
matrix-aut32-id-formats-corrected.xlsx
→ Matrix Validator v0.1.0
```

No confundir:

- `aut32`: baseline técnica de la release del Validator.
- `aut34`: snapshot comercial histórico correspondiente al cierre de Fase 6 del Nicho 3.
- `aut36`: checkpoint comercial histórico del Nicho 3, con Method v2 materializado hasta Landed Cost Screen.
- `aut37`: snapshot comercial operativo vigente, correspondiente a la Golden Run de `BRAND-CAND-001` cerrada hasta Fase 6.

## 2. Snapshot al 2026-09-18

| Campo | Estado |
|---|---|
| Fase general | Research / validación del método sobre múltiples nichos |
| Matrix Validator | v0.1.0 publicado y cerrado |
| Schema operativo | `full-matrix-v5 0.7.0` |
| Tests | 40 archivos / 170 tests |
| CLI | 5 casos operativos |
| E2E público | 10 fixtures |
| CI | Verde |
| Matriz comercial vigente | `matrix-aut44-brand-cand-001-phase13-corrected.xlsx` |
| Resultado aut44 | PASS / 0 errors / 0 warnings / 0 info / 0 limitations |
| Nicho 1 — Energía Solar Portátil | Pausado selectivamente |
| Nicho 2 — Viaje organizado | Screening de origen/headroom realizado; Landed Cost defendible pendiente |
| Nicho 3 — Mascotas | Method v2 ejecutado internamente hasta Fase 11; primer strong candidate pendiente de validación profesional |
| Próxima acción Golden Run | Fase 11 — Landed Cost de `BRAND-CAND-001` |
| Próxima acción Nicho 3 | Consolidar finalistas y preparar el gate profesional externo |
| Brand System | v0.4; se agrega lifecycle de Hypothesis ID local → `BRAND-CAND-XXX` formal/global, manteniendo `CORE` / `STRONG ADJACENCY` y separación Brand Fit / Method v2 |
| Brand Candidate Screening | v0.4 operativo; `PROSPECTIVE` / `RETROSPECTIVE`; lifecycle Hypothesis ID → `BRAND-CAND-XXX`; 001–005 = `CORE / PASS`; 006 = `STRONG ADJACENCY / BRAND FIT CONFIRMED`; 007–010 = `CORE / PASS TO METHOD V2` |
| Próxima acción Brand | BRAND-CAND-007 F0–F13 CLOSED / aut138 DOBLE PASS / shortlist condicionada para revisión externa BASE-FIT-005/007 (HOLD); BASE-FIT-006/008 DEFER; Decision Report previo a reuniones socio+despachante; ningún finalista económico, F14 NOT OPENED. BRAND-CAND-010 continúa FREEZE; 008/009 sin abrir; Marca Hogar sin cambio de prioridad. |

## 3. Snapshot histórico del Nicho 3 — 2026-09-17

### Estado general

Smart Imports completó la validación interna de Method v2 hasta `Landed Cost Screen` sobre el Nicho 3.

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Baseline técnica: aut32
Snapshot comercial del checkpoint: aut36
Archivo: matrix-aut36-niche3-method-v2-checkpoint-corrected.xlsx
Resultado: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: 219d9954acca9fefda5f6edef2eab18f93bf0b4564e45d3e1442f13d6db39a53
```

### Matrix Validator — estado cerrado

```text
Application: 0.1.0
Tag: v0.1.0
Schema operativo: full-matrix-v5 0.7.0
Runtime: Node.js 24
Package manager: pnpm 11
Comportamiento: read-only
Test files: 40
Tests: 170
CLI: 5 casos operativos
E2E público: 10 fixtures
CI: verde
Baseline técnica: aut32 / PASS
```

No reabrir el Validator sin un requerimiento comercial concreto y bloqueante.

### Method v2

```text
Fases 0–6  → cerradas
Fase 7     → shortlist pre-origen cerrada
Fase 8     → screening de origen cerrado
Fase 9     → Headroom cerrado
Fase 10    → dataset mínimo ejecutado en sobrevivientes
Fase 11    → primer Landed Cost Screen completado
```

`BASE-PET-003` es el primer `STRONG CANDIDATE — PENDING PROFESSIONAL VALIDATION`.

El 2026-09-16 el proveedor confirmó que la diferencia entre dimensiones de producto y caja se explica porque el producto se envía parcialmente desmontado. El packing queda aclarado y no constituye un bloqueo actual.

`BASE-PET-004` queda pendiente de respuesta de proveedor antes de completar su Fase 10/11.

### Próximo gate

```text
completar 5–6 candidatos firmes
→ negociar FOB/condiciones
→ preparar paquete homogéneo
→ despachante
→ validar NCM / intervenciones / certificaciones / costos
→ recalcular
→ shortlist final
→ decisión de importación
```

La revisión del despachante es una dependencia profesional externa y no requiere reabrir el Matrix Validator.

## 4. Matriz del checkpoint histórico del Nicho 3 — aut36

```text
matrix-aut36-niche3-method-v2-checkpoint-corrected.xlsx
SHA-256:
219d9954acca9fefda5f6edef2eab18f93bf0b4564e45d3e1442f13d6db39a53
```

Validación:

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

`aut36` conserva la materialización de Fase 6 y agrega el recorrido de Method v2 hasta Landed Cost Screen:

- Nicho 29 normalizado.
- 3 Evaluaciones nuevas.
- 8 Productos Base `BASE-PET-*`.
- publicaciones y competencia local normalizadas.
- benchmarks externos.
- evidencias y fuentes trazables.
- cuatro resúmenes de competencia por arquitectura.
- segmentos competitivos, incluidos sustitutos.

No incorpora todavía Landed Cost ni una selección final de proveedores.

## 5. Método vigente — Method v2

Jerarquía:

```text
NICHO
→ NECESIDAD / FAMILIA
→ ARQUITECTURA DE SOLUCIÓN
→ PRODUCTO BASE
```

Reglas consolidadas:

- `publicación ≠ competidor ≠ SKU ≠ Producto Base`;
- normalizar antes de evaluar;
- Demanda y Competencia se evalúan por separado;
- complejidad técnica es riesgo, no descarte automático;
- un sustituto puede ser una combinación de productos;
- `OEM platform ≠ exact supplier`;
- safety claim no equivale a seguridad validada;
- network generation no equivale a network compatibility;
- standby battery no equivale a tracking battery;
- private-label capability no equivale a Potencial de Marca.

## 6. Nicho 3 — estado por arquitectura

| Arquitectura | Estado | Potencial de Marca |
|---|---|---|
| Vacuum Grooming | ADVANCE | MEDIO–ALTO |
| Arenero automático/smart | ADVANCE | ALTO — CONDICIONADO |
| Smart Fountain | ADVANCE | MEDIO–ALTO |
| GPS + Wellness | ADVANCE — CONDITIONAL | ALTO — FUERTEMENTE CONDICIONADO |

Watchlist:

- Dedicated Pet Camera + interaction.
- Mobile Pet Robot.

## 7. Productos Base del Nicho 3

| ID | Producto Base |
|---|---|
| BASE-PET-001 | Vacuum Grooming doméstico integrado |
| BASE-PET-002 | Arenero automático rotativo cerrado |
| BASE-PET-003 | Arenero automático open-top / acceso amplio |
| BASE-PET-004 | Arenero automático de rastrillo |
| BASE-PET-005 | Fuente inteligente automatizada/conectada |
| BASE-PET-006 | Fuente con monitoreo cuantitativo de hidratación |
| BASE-PET-007 | Tracker GPS 4G para mascotas |
| BASE-PET-008 | Tracker GPS + Wellness avanzado |

## 8. Necesidades futuras descubiertas para Matrix vNext

No bloquean el ciclo actual.

1. `Familia` y `Arquitectura` explícitas.
2. `Tipo Competencia = DIRECTA | INDIRECTA | SUSTITUTO | BENCHMARK`.
3. `Nichos.Proxima Accion` alineada con las fases de Method v2.

Mantener `full-matrix-v5 0.7.0` estable mientras estas necesidades no justifiquen un nuevo schema.

## 9. Estado comercial por nicho

### Nicho 1 — Energía Solar Portátil

- AT-999 y compras permanecen pausadas.
- Conservar evidencia histórica.
- No forzar reactivación sin una nueva razón comercial.

### Nicho 2 — Viaje organizado y equipaje funcional

- Demanda y Competencia cerradas.
- Screening de proveedores/origen realizado.
- Headroom screening realizado.
- Landed Cost defendible sigue pendiente.
- No crear snapshots MARG basados en supuestos no defendibles.

### Nicho 3 — Mascotas

- Research Brief: cerrado.
- Madurez: cerrada.
- Demanda: cerrada.
- Competencia: cerrada.
- Potencial de Marca: cerrado.
- Productos Base: cerrados.
- Materialización del checkpoint del Nicho 3: `aut36` PASS.
- Próximo gate: consolidar 5–6 candidatos firmes, negociar condiciones y preparar la validación profesional externa.

## 10. Próxima secuencia del Nicho 3

```text
completar BASE-PET-004 cuando responda el proveedor
→ consolidar aproximadamente 5–6 candidatos firmes
→ negociar FOB y condiciones con los finalistas
→ preparar paquete homogéneo para despachante
→ validar NCM / derechos / intervenciones / certificaciones / costos
→ actualizar Landed Cost con datos profesionales
→ construir shortlist final
→ decisión real de importación
```

Las Fases 7–11 ya forman parte del recorrido interno cerrado de Method v2. No deben reaparecer como trabajo futuro salvo que nueva evidencia obligue a reabrir un candidato concreto.

## 11. Nuevo frente — Brand System

El 2026-09-16 se formaliza una nueva capa estratégica previa a Method v2.

Principio:

```text
BRAND FIT
¿Queremos que nuestra marca venda este producto?

METHOD V2
¿Existe realmente un negocio defendible alrededor de este producto?
```

Arquitectura reusable:

```text
BRAND
→ BRAND TERRITORY
→ MISSIONS
→ PROBLEMS
→ SOLUTIONS
→ BRAND CANDIDATE SCREENING
→ METHOD V2
```

`Marca Hogar` es la primera implementación real, con el descriptor interno:

> **Un hogar que funciona mejor.**

El portfolio se organiza por misiones y problemas, no por categorías comerciales.

Misiones v0.1:

1. mejorar las condiciones del hogar;
2. usar mejor los recursos;
3. reducir y gestionar residuos;
4. resolver problemas domésticos recurrentes conectados con el núcleo.

El sistema debe ser reusable para futuras marcas con territorios y misiones propios. `Mundo Fitness` queda registrado como ejemplo conceptual de esa reusabilidad, no como una marca decidida.

Primer candidato:

```text
BRAND-CAND-001
Sistema doméstico de detección de fugas de agua con corte automático
→ PASS TO METHOD V2
```

El Brand System no requirió modificar `full-matrix-v5 0.7.0` ni Matrix Validator v0.1.0. La ejecución de `BRAND-CAND-001` generó `aut37` como nuevo snapshot comercial vigente, preservando `aut36` como checkpoint histórico del Nicho 3. Las necesidades futuras de modelado de Brand, Territory, Mission, Problem, Solution y Brand Fit se registran conceptualmente antes de decidir Matrix vNext o cambios del Intelligence Engine.

## 12. Bloqueos y dependencias

| Tema | Estado | Acción |
|---|---|---|
| Matrix Validator | Cerrado | No reabrir sin requerimiento comercial |
| Matrix vNext | No bloqueante | Registrar requisitos y diferir |
| Brand System | v0.3 consolidado; arquitectura reusable con `CORE` / `STRONG ADJACENCY`, category-creep protection y separación Brand Fit / Method v2 |
| Validación profesional externa | En preparación | Consolidar 5–6 candidatos, negociar condiciones y preparar revisión con despachante |
| Niche 3 origin | Screening cerrado en sobrevivientes | Reabrir sólo si aparece un nuevo candidato firme |
| Landed Cost Niche 3 | Screening preliminar iniciado | Completar sólo en finalistas y validar profesionalmente |
| Wellness local | Hipótesis abierta | Mantener como condición |
| Seguridad areneros | Riesgo crítico posterior | Evaluar en sourcing/QA |
| Compatibilidad GPS | Riesgo crítico posterior | Exigir variante/bandas documentadas |

## 13. Protocolo para abrir un nuevo chat

1. Compartir ambos repositorios.
2. Pedir lectura inicial de `SI-ROADMAP-002`.
3. Para tareas del Nicho 3, consultar `SI-RESEARCH-005`.
4. Para Fases 7–11 y estado de Method v2, consultar `SI-RESEARCH-006` y `SI-DECISION-015`.
5. Para tareas de marca, consultar `SI-BRAND-001`, `SI-BRAND-002`, `SI-BRAND-003` y `SI-DECISION-016`.
6. Adjuntar `aut96` cuando la tarea requiera el snapshot comercial validado más reciente. Usar snapshots anteriores sólo para reproducir checkpoints históricos concretos.
7. No volver a adjuntar PDFs históricos ya consolidados.
8. Mantener separadas tareas de negocio (`smart-imports`) y técnicas (`smart-imports-engine`).
9. No reabrir decisiones técnicas cerradas salvo que el flujo comercial descubra un bloqueo real.

## 14. Próxima acción concreta

```text
MARCA HOGAR
→ INTERNAL PORTFOLIO REVIEW COMPLETE
→ PORTFOLIO BASELINE FROZEN
→ EXTERNAL REVIEW PENDING
→ F14 NOT OPENED

PRIMARY WORKSTREAM
→ MARCA FITNESS
→ BRAND-CAND-010
→ materializar aut105
→ Matrix Validator PASS
→ cerrar F0
→ continuar Method v2
```

Marca Hogar sólo se reabre por gate externo, contradicción material o decisión explícita. No se reabren F0–F13 por defecto.

## 15. Documentos relacionados

- [SI-RESEARCH-005 — Niche 3 Phases 0–6](../06-research/niche-003-pet-care-wellness-technology/si-research-005-niche-3-phases-0-to-6.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-DECISION-014 — Adopt Niche 3 Method v2 and aut34](../09-decision-log/si-decision-014-adopt-niche3-method-v2-and-aut34.md)
- [SI-RESEARCH-006 — Niche 3 Phases 7–11 / Method v2 validation](../06-research/niche-003-pet-care-wellness-technology/si-research-006-niche-3-phases-7-to-11-method-v2-validation.md)
- [SI-DECISION-015 — Adopt aut36 and validate Method v2](../09-decision-log/si-decision-015-adopt-aut36-and-validate-method-v2-through-landed-cost-screen.md)
- [SI-BRAND-001 — Brand System reusable](../07-brand/si-brand-001-reusable-brand-system.md)
- [SI-BRAND-002 — Brand Candidate Screening](../07-brand/si-brand-002-brand-candidate-screening-method.md)
- [Marca Hogar — territorio y Candidate Register](../07-brand/brands/brand-hogar/README.md)
- [SI-DECISION-016 — Arquitectura de marca por misiones](../09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md)

<!-- ECONOMIC-BRIEFING-PENDING:START -->
## Pendiente futuro — Documento didáctico de evaluación económica para reunión con socio

### Estado

```text
TRIGGER MET
MEETING MATERIAL — PREPARE WHEN NEEDED
Brand Candidates relevantes completados hasta F13
→ Portfolio Review interno completo
```

### Objetivo

Preparar un documento simple, muy didáctico y completamente en español para explicar al socio cómo Smart Imports evalúa económicamente una oportunidad de producto.

No debe enseñar finanzas en abstracto. Debe mostrar, utilizando **uno o más productos reales investigados por Smart Imports y números propios de las matrices**, cómo una oportunidad pasa de:

```text
“parece interesante”
→
“económicamente defendible o no”
```

### Recorrido pedagógico obligatorio

```text
Precio local
→ Headroom
→ Costo de origen
→ Landed Cost
→ Margen
→ ROI
→ significado para la decisión
```

### Conceptos a explicar en lenguaje sencillo

```text
HEADROOM
→ ¿hay espacio económico suficiente para investigar la importación?

LANDED COST
→ ¿cuánto estimamos que cuesta realmente poner el producto en Argentina?

MARGEN
→ ¿cuánto queda económicamente después del costo puesto y los costos comerciales?

ROI
→ ¿qué retorno unitario obtenemos respecto del costo económico invertido?
```

### Distinciones obligatorias

```text
Headroom ≠ Landed Cost

Economic Landed Cost ≠ Total Cash Outlay

ROI sobre costo económico
≠
ROI total del negocio / capital total invertido
```

### Selección de ejemplos

Usar uno o más Product Bases reales investigados por Smart Imports y sus números reales.

Cuando el portfolio esté completo, priorizar ejemplos que permitan contrastar, por ejemplo:

```text
economía holgada
vs.
economía ajustada o no defendible
```

La selección definitiva debe hacerse recién después de completar los Brand Candidates relevantes hasta F13, para elegir casos pedagógicamente representativos del portfolio real.

### Regla de activación

El trigger ya fue cumplido. El entregable permanece como material de reunión a preparar cuando se necesite, sin bloquear el cambio de workstream a Fitness.
<!-- ECONOMIC-BRIEFING-PENDING:END -->

## 16. Changelog

| Version | Date | Change |
|---|---|---|
| 1.23.10 | 2026-10-14 | BRAND-CAND-007 F9–F13 CLOSED / aut138 doble PASS; Decision Report y shortlist condicionada para reunión externa. |
| 1.23.9 | 2026-10-14 | BRAND-CAND-007 F7–F8 CLOSED, aut132/aut133 doble PASS, Founder Review aprobado, HOLD externo. |
| 1.23.8 | 2026-10-14 | Checkpoint BRAND-CAND-007 F4–F6, aut131 triple doble PASS, F7 siguiente. |
| 1.23.7 | 2026-10-13 | Checkpoint BRAND-CAND-007 F0–F3, aut128 PASS, F4 siguiente. |
| 1.23.1 | 2026-10-08 | BRAND-CAND-010 completa Method v2 F0–F13 sobre aut105–aut118 PASS; NO FINALIST / FREEZE; BASE-FIT-001 queda principal reapertura por logistics gate; F14 no se abre. |
| 1.23.0 | 2026-10-07 | Marca Hogar cierra Portfolio Review interno; BASE-HOGAR-016 lead, BASE-HOGAR-006 backup; baseline congelada, revisión externa pendiente y workstream principal cambia a Marca Fitness / aut105. |
| 1.22.0 | 2026-10-05 | BRAND-CAND-006 completa F6–F13 sobre aut97–aut104 PASS; BASE-PET-003 queda FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW / NOT FIRST-STAGE FIT; candidato PORTFOLIO REVIEW READY / FREEZE; aut105 queda desbloqueado para BRAND-CAND-010. |
| 1.21.0 | 2026-10-05 | BRAND-CAND-006 cierra F5 sobre aut96 PASS; EVAL-0028 = 4/5 Media; siguiente gate F6 y aut97. |
| 1.20.0 | 2026-10-05 | Marca Fitness abre Method v2 únicamente para BRAND-CAND-010; SI-RESEARCH-070 deja F0 analysis complete / matrix pending / not closed, con Nicho ID 37 y aut105 reservados tras el lineage aut96..aut104. |
| 1.19.0 | 2026-10-05 | Marca Fitness cierra screenings: BRAND-CAND-007..010 = CORE / PASS TO METHOD V2; Brand System y Screening formalizan la trazabilidad desde FIT-CAND y el próximo gate es decidir el orden de Method v2. |
| 1.18.0 | 2026-10-05 | Marca Fitness congela baseline pre-screening v0.2 con territorio/misiones revisados, candidatos activos 001/002/005/007, 003/004 absorbidos y 006 reclasificado; siguiente gate FIT-CAND-001. |
| 1.17.0 | 2026-10-05 | Marca Hogar queda en pausa operativa hasta reuniones con socio y despachante; se documentan entregables de revisión externa y SI-BRAND-003 para ingreso reusable de oportunidades descendentes/ascendentes. |
| 1.16.0 | 2026-10-03 | BRAND-CAND-006 queda F0–F4 CLOSED sobre aut91–aut95 PASS; F5 análisis completo pero no cerrado. Se registra Decision Reporter prototipado, prioridad primera compra/revisión externa y apertura exploratoria de Marca Fitness. |
| 1.15.0 | 2026-09-30 | BRAND-CAND-005 completa F0–F13; aut90 PASS; BASE-HOGAR-028 FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW / NOT FIRST-STAGE FIT; candidato PORTFOLIO REVIEW READY / FREEZE; siguiente ejecución BRAND-CAND-006 después del cierre documental. |
| 1.13.0 | 2026-09-25 | Se registra como pendiente futuro el documento didáctico para reunión con socio sobre Precio local → Headroom → Costo de origen → Landed Cost → Margen → ROI, usando ejemplos reales de Smart Imports y activado sólo después de completar los candidatos relevantes hasta F13. |
| 1.12.0 | 2026-09-25 | BRAND-CAND-003 completa F0–F13; aut58 PASS; BASE-HOGAR-010 FINALIST — CONDITIONED; candidato PORTFOLIO REVIEW READY / FREEZE; siguiente ejecución BRAND-CAND-004. |
| 1.11.0 | 2026-09-23 | BRAND-CAND-001 completa Fase 10; aut41 PASS y próxima acción Fase 11 — Landed Cost. |
| 1.10.0 | 2026-09-21 | BRAND-CAND-001 completa Fase 9; aut40 PASS y próxima acción Fase 10 — Minimum Landed Cost Dataset. |
| 1.9.0 | 2026-09-21 | BRAND-CAND-001 completa Fases 7–8; aut39 PASS y próxima acción Fase 9 — Headroom. |
| 1.8.0 | 2026-09-18 | BRAND-CAND-001 completa Golden Run hasta Fase 6; aut37 PASS y próxima acción Fase 7. |
| 0.7.0 | 2026-08-03 | Handoff de v3/v4 y normalización de fuentes. |
| 0.8.0 | 2026-08-04 | Adopción de aut31/v5, 144 tests y cierre técnico de vistas derivadas. |
| 1.0.0 | 2026-09-11 | Matrix Validator cerrado; `aut34` adoptada; Method v2 y Fases 0–6 del Nicho 3 consolidadas. |
| 1.1.0 | 2026-09-16 | Se incorpora Brand System reusable, Marca Hogar v0.1, Brand Candidate Screening y aclaración de packing de PET-003. |
| 1.2.0 | 2026-09-17 | Se separan Brand System e instancia Marca Hogar; BRAND-CAND-002 queda PASS y se formalizan expedientes por candidato. |
| 1.3.0 | 2026-09-17 | BRAND-CAND-003 queda PASS TO METHOD V2 y se registra su handoff; próximo screening BRAND-CAND-004. |
| 1.4.0 | 2026-09-17 | BRAND-CAND-004 queda PASS TO METHOD V2 y se registra su handoff; próximo screening BRAND-CAND-005. |
| 1.5.0 | 2026-09-17 | BRAND-CAND-005 queda PASS TO METHOD V2 y se registra su handoff; próximo screening retrospectivo BRAND-CAND-006. |
| 1.6.0 | 2026-09-17 | BRAND-CAND-006 confirma Brand Fit retrospectivamente; próximo paso: consolidar aprendizajes del bloque de seis screenings. |

| 1.7.0 | 2026-09-17 | Se consolida Brand System v0.3: Territory Relationship, Screening Type y soporte formal de screening retrospectivo. |
| 1.14.0 | 2026-09-25 | BRAND-CAND-004 completa F0–F13; aut72 PASS; BASE-HOGAR-016 FINALIST — CONDITIONED; candidato PORTFOLIO REVIEW READY / FREEZE; se formaliza la regla obligatoria de cierre documental + commit/push antes de abrir el siguiente Brand Candidate. |
## Golden Run BRAND-CAND-001 — Fases 0–6

Estado:

```text
Input: BRAND-CAND-001
Method v2: Fases 0–6 COMPLETADAS
Matrix: matrix-aut37-brand-cand-001-phase6.xlsx
SHA-256: 6c0f1524fe102fe5c531edb890639bb9fa9845fbc4cc1b9e046ce9ceb96387ff
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
Next Action: Fase 7 — shortlist pre-origen
```

Cinco Product Bases pasan al gate de Fase 7: `BASE-HOGAR-002` a `BASE-HOGAR-006`. `BASE-HOGAR-001`, `BASE-HOGAR-007` y `BASE-HOGAR-008` son PB de soporte y no avanzan automáticamente.

La matriz usa el Nicho ID 32 como `MATRIX_SCOPE_ALIAS` exclusivamente por compatibilidad con `full-matrix-v5 0.7.0`. El input conceptual sigue siendo `BRAND-CAND-001`; esta fricción queda registrada para Matrix vNext / Intelligence Engine, sin reabrir ahora el schema ni el Validator.

Fuente de ejecución: [SI-RESEARCH-007](../06-research/brand-hogar/si-research-007-brand-cand-001-method-v2-golden-run-phases-0-to-6.md).
## Golden Run BRAND-CAND-001 — Fases 7–8

Estado:

```text
Input: BRAND-CAND-001
Method v2: Fases 0–8 COMPLETADAS
Matrix vigente: matrix-aut39-brand-cand-001-phase8.xlsx
SHA-256: 62341e1c202f87a531f96e9573613f9adda588e70e761eee9254e214a30a658c
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
Next Action: Fase 9 — Headroom
```

Shortlist / origen:

```text
BASE-HOGAR-003 → ACTIVE / ORIGIN CONFIRMED
BASE-HOGAR-006 → ACTIVE / ORIGIN CONFIRMED
BASE-HOGAR-002 → ACTIVE SECONDARY / ORIGIN CONFIRMED — CONDITIONAL
BASE-HOGAR-004 → WATCHLIST / ORIGIN CONFIRMED
BASE-HOGAR-005 → PAUSED
```

Las respuestas documentales pendientes de proveedores no bloquean el gate ya demostrado. Se actualiza sólo la evidencia afectada; Fase 8 se reabre únicamente ante una contradicción estructural.

Fuente de ejecución: [SI-RESEARCH-008](../06-research/brand-hogar/si-research-008-brand-cand-001-method-v2-golden-run-phases-7-to-8.md).
## Golden Run BRAND-CAND-001 — Fase 9

Estado:

```text
Input: BRAND-CAND-001
Method v2: Fases 0–9 COMPLETADAS
Matrix vigente: matrix-aut40-brand-cand-001-phase9.xlsx
SHA-256: 525e8aefb5db96a30b8d5565f05fd9c1ac283f1a8eafffbbd7d5f75f9ecc4512
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
Next Action: Fase 10 — Minimum Landed Cost Dataset
```

Resultado del gate:

```text
BASE-HOGAR-002 → SURVIVES / PASS TO F10
BASE-HOGAR-003 → SURVIVES — CONDITIONED / PASS TO F10
BASE-HOGAR-006 → SURVIVES / PASS TO F10
BASE-HOGAR-004 → WATCHLIST
BASE-HOGAR-005 → PAUSED
```

`HEADROOM ≠ LANDED COST`. Los ratios y datos comerciales exactos permanecen en la matriz operativa y registros privados.

Fase 10 debe reunir configuración exacta, Incoterm, tier/MOQ aplicable, packing, unidades por caja, dimensiones/CBM, pesos y documentación técnica mínima antes de abrir Landed Cost.

Fuente de ejecución: [SI-RESEARCH-009](../06-research/brand-hogar/si-research-009-brand-cand-001-method-v2-golden-run-phase-9-headroom.md).
## Golden Run BRAND-CAND-001 — Fase 10

Estado:

```text
Input: BRAND-CAND-001
Method v2: Fases 0–13 COMPLETADAS
Matrix vigente: matrix-aut44-brand-cand-001-phase13-corrected.xlsx
SHA-256: 37b2b37c5c61355efec271b7ecb49df74c2264e2f721830a1c2478858a850f56
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
Next Action: FREEZE BRAND-CAND-001 / continuar candidatos restantes hasta F13 / Portfolio Review futuro
```

Resultado del gate:

```text
BASE-HOGAR-002 → FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW
BASE-HOGAR-003 → STOP — REOPENABLE
BASE-HOGAR-006 → FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW
BASE-HOGAR-004 → WATCHLIST
BASE-HOGAR-005 → PAUSED

BRAND-CAND-001 → PORTFOLIO REVIEW READY / FREEZE
F14 → NOT OPENED
```

Principios observados:

```text
DECISION-GRADE ≠ PROCUREMENT-GRADE
SUPPLIER RESPONSE ≠ PHASE PROGRESS
```

El contacto con proveedores enriquece la evidencia, pero no debe controlar el camino crítico cuando datos públicos o proxies conservadores permiten una decisión defendible.

F13 consolidó la shortlist final. `BRAND-CAND-001` queda en freeze hasta Portfolio Review; la revisión externa previa deberá incluir al despachante antes de decidir qué producto abre F14.

Fuente de ejecución vigente: [SI-RESEARCH-013 — Fase 13 Shortlist final](../06-research/brand-hogar/si-research-013-brand-cand-001-method-v2-golden-run-phase-13-final-shortlist.md).

<!-- METHOD-V2-GOVERNANCE-2026-10-10:START -->
## Governance Method v2 + BRAND-CAND-010 reconciliado — 2026-10-10

```text
DATA FIDELITY PREFLIGHT v2.4 PASS
+
MATRIX VALIDATOR PASS

F13 HISTORICAL SNAPSHOT: matrix-aut118-brand-cand-010-phase13-final-corrected.xlsx
F13 SHA-256: 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a

aut120: SUPERSEDED / 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2

CURRENT POST-CLOSE BASELINE: matrix-aut123-brand-cand-010-post-close-core-snapshot-reconciliation.xlsx
CURRENT SHA-256: 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb

Marketplace contract:
Precio ARS + Precio USD + Ventas visibles + FX + FX Fecha/Basis + source binding

F0–F13: CLOSED
F14: NOT OPENED
```

El candidato `BRAND-CAND-007` ya abierto debe continuar aplicando `SI-BIM-PROC-003 v1.0.6`, `SI-DECISION-019`, `SI-DECISION-020` y Data Fidelity Preflight v2.4; los candidatos `BRAND-CAND-008..009` deberán heredar ese contrato antes de abrirse.

Marca Hogar conserva una deuda histórica de reconciliación marketplace que debe resolverse por Brand Candidate antes de reutilizar esa evidencia como baseline vigente.
<!-- METHOD-V2-GOVERNANCE-2026-10-10:END -->

<!-- AUT123-SNAPSHOT-BASELINE:START -->
## aut123 — Core + snapshot baseline vigente

```text
aut121 corrected
→ marketplace economics dual PASS
→ SUPERSEDED: core operativo incompleto/stale
→ 7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc

aut122
→ core marketplace materialization
→ Data Fidelity Preflight v2.3 PASS
→ Matrix Validator PASS
→ SUPERSEDED: estado pre-proyección no preservado estructuralmente
→ 67e850c0a40fb274629429587f9ce5b500eddb51da6580fccb2c48f060dba4ba

aut123
→ 21 ACTIVE core complete / synchronized
→ 5 HISTORICAL_ONLY explícitos
→ 26/26 Snapshot Pre-Proyección ML
→ ML-0160 temporal proof: +500 → +100
→ Core + Snapshot Fidelity PASS
→ Data Fidelity Preflight v2.4 PASS
→ Matrix Validator PASS / 0 errors / 0 warnings / 0 info
→ CURRENT POST-CLOSE BASELINE
→ 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb

F0–F13: CLOSED
F14: NOT OPENED
```

```text
ACTIVE CORE = VERIFIED CURRENT LAYER
CURRENT CORE PROJECTION REQUIRES PRE-PROJECTION SNAPSHOT
CURRENT VERIFICATION ≠ HISTORICAL CAPTURE
```
<!-- AUT123-SNAPSHOT-BASELINE:END -->

<!-- METHOD-V2-F8-COLLABORATIVE:START -->
## Governance — F8 Origin Screening / Alibaba

Cambio prospectivo vigente desde `SI-DECISION-020`:

```text
F8 MODE: COLLABORATIVE
Founder participation: REQUIRED
Founder Review: APPROVED → requerido para CLOSE
```

Para el próximo Brand Candidate:

1. F7 entrega shortlist pre-origin.
2. F8 abre discovery colaborativo en Alibaba.
3. Alejandro participa en búsqueda y revisión de productos/variantes.
4. El agente puede automatizar triage, normalización, deduplicación, clasificación, materialización y validación.
5. Se presenta el origin shortlist.
6. F8 sólo puede cerrar después de `Founder Review: APPROVED` + validación canónica PASS.

No se reabren Brand Candidates históricos únicamente por esta corrección de governance.
<!-- METHOD-V2-F8-COLLABORATIVE:END -->
