---
id: brand-fitness
title: Marca Fitness — Screening cerrado / Method v2
description: Estado vigente de Marca Fitness; BRAND-CAND-007 y BRAND-CAND-010 F0–F13 cerrados, BRAND-CAND-008 F0–F13 cerrado sin finalistas y reabrible, BRAND-CAND-009 F0–F13 cerrado con shortlist condicionada; F14 no abierta y revisión externa pendiente.
version: 0.5.15
status: screening-closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-03
updated: 2026-10-21
tags:
  - brand
  - fitness
  - exploration
  - reusable-brand-system
related:
  - si-brand-001
  - si-brand-002
  - si-brand-003
---

# Marca Fitness — Screening cerrado

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

Último snapshot `aut153` **DOBLE PASS**; SHA-256 `4c88c0ac2e4d459f17707da38d8f4b72fb7cdaf0d157dc1d3e8b8c4505b10540`. Checkpoint documental para revisar antes de commit y push. Siguiente candidato `BRAND-CAND-009` elegible, **no abierto hasta publicación de este cierre**.
<!-- BRAND-CAND-008-F4-F13-FINAL-CHECKPOINT:END -->

<!-- BRAND-CAND-008-F0-F3-CHECKPOINT:START -->
## BRAND-CAND-008 — Checkpoint Method v2 F0–F3 (2026-10-16)

**F0–F3 CLOSED / Demanda 2/5 / Confianza Baja / aut142-r1 DOBLE PASS.** F0–F2 AUTO; F3 COLLABORATIVE con aprobación explícita del Founder el 16/10/2026. Cinco publicaciones de Mercado Libre con URLs, PDF privados y referencias cruzadas; no hay Product Bases.

F0 `aut139`, F1 `aut140`, F2 `aut141`, F3 `aut142-r1` — todos con Data Fidelity Preflight + Matrix Validator PASS. SHA-256 F3: `97b3260521630f7e00067946a3cc23341f965f1b209a8a5a7d65da0f5c9fdaf0`.

**Próximo gate: F4 Competencia (AUTO), sobre la misma cohorte F3; F4 todavía no abierto.** F5–F6 AUTO, próximo checkpoint al finalizar F6; no subir XLSX, PDF o logs a Git.
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
## BRAND-CAND-007 — checkpoint F0–F3 (2026-10-13)

**F0–F3 CLOSED / aut128 PASS / Demanda 3/5 / Confianza Media**. F3 ejecutada COLLABORATIVE con aprobación explícita del Founder. Seis publicaciones verificadas y trazables; sin Product Bases. Próximo gate **F4 — Competencia AUTO**, sobre la misma cohorte de F3. Checkpoint siguiente al finalizar F6. Research `SI-RESEARCH-089..092`. SHA-256 de aut128: `3fd9bce9fe32866ea30f33e26e3b3eaf9753a36e3223faf200618f8c8c4aba30`.
<!-- BRAND-CAND-007-F0-F3-CHECKPOINT:END -->

<!-- BRAND-CAND-010-DOCUMENTARY-CHECKPOINT:START -->
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
<!-- BRAND-CAND-010-DOCUMENTARY-CHECKPOINT:END -->

## 1. Estado vigente

```text
Architecture baseline: v0.2
Territory baseline: FROZEN
Missions baseline: FROZEN
Brand Candidate Screening: CLOSED
Formal candidates: BRAND-CAND-007..010
PASS TO METHOD V2: 4
Method v2: BRAND-CAND-010 F0 OPENED / MATRIX PENDING / NOT CLOSED
Product Bases: NOT DEFINED
Purchase Decision: NONE
```

## 2. Territorio vigente

> **Ayudar a personas a conservar, recuperar y desarrollar capacidad física en una vida cotidiana marcada por sedentarismo, poco tiempo y espacios limitados, mediante soluciones simples, compactas, comprensibles y sostenibles en el tiempo.**

`+50` permanece como contexto/segmento potencial a explorar; no define la marca.

## 3. Misiones

```text
M1 — Construir y conservar fuerza útil
M2 — Incorporar movimiento y entrenamiento en la vida cotidiana
M3 — Conservar y recuperar movilidad, estabilidad y capacidad física
M4 — Entender el progreso y sostener la constancia
```

## 4. Lifecycle de IDs

| Hypothesis ID | Formal Candidate ID | Candidate | Territory Relationship | Decision |
|---|---|---|---|---|
| `FIT-CAND-001` | [`BRAND-CAND-007`](./candidates/brand-cand-007-accessible-compact-strength.md) | Fuerza accesible y compacta | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-002` | [`BRAND-CAND-008`](./candidates/brand-cand-008-flexible-portable-training.md) | Entrenamiento flexible y portátil | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-005` | [`BRAND-CAND-009`](./candidates/brand-cand-009-mobility-stability-physical-capacity.md) | Movilidad, estabilidad y conservación/recuperación de capacidad física | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-007` | [`BRAND-CAND-010`](./candidates/brand-cand-010-integrated-movement-sedentary-day.md) | Movimiento integrado a la jornada sedentaria | `CORE` | `PASS TO METHOD V2` |

## 5. Hipótesis no promovidas

```text
FIT-CAND-003 → MERGED INTO FIT-CAND-005 → sin ID formal propio
FIT-CAND-004 → MERGED INTO FIT-CAND-001 → sin ID formal propio
FIT-CAND-006 → TRANSVERSAL CAPABILITY: Medición + feedback + constancia → sin ID formal propio
```

Los IDs históricos se preservan y no se reutilizan.

## 6. Documentos

- [`Candidate Hypotheses v0.1`](./fitness-candidate-hypotheses-v0.1.md) — historial de hipótesis.
- [`Pre-screening Architecture v0.2`](./fitness-pre-screening-architecture-v0.2.md) — baseline del screening.
- [`Brand Candidates`](./candidates/README.md) — índice vigente y expedientes.
- [`SI-BRAND-002`](../../si-brand-002-brand-candidate-screening-method.md) — método reusable de screening.
- [`SI-BRAND-003`](../../si-brand-003-opportunity-intake-and-discovery.md) — ingreso de futuras oportunidades.

## 7. Ejecución Method v2

```text
BRAND-CAND-010
→ FIRST FITNESS CANDIDATE
→ F0 ANALYSIS COMPLETE
→ MATRIX MATERIALIZATION PENDING
→ F0 NOT CLOSED

BRAND-CAND-007 → F0–F13 CLOSED / aut138 PASS / EXTERNAL REVIEW READY / F14 NOT OPENED
BRAND-CAND-008..009 → ELIGIBLE — NOT OPENED
```

Research vigente: [`SI-RESEARCH-070`](../../../06-research/brand-fitness/si-research-070-brand-cand-010-method-v2-agile-phase-0-research-brief.md).

BRAND-CAND-010 creó formalmente `BASE-FIT-001`..`BASE-FIT-004` en F6; ninguno quedó seleccionado como portfolio finalist. La prioridad comercial inmediata de Marca Hogar no cambia.

## Changelog

| Version | Fecha | Cambio |
|---|---|---|
| 0.5.10 | 2026-10-16 | BRAND-CAND-008 F0–F3 CLOSED / aut142-r1 doble PASS / F4 AUTO siguiente. |
| 0.5.9 | 2026-10-14 | BRAND-CAND-007 F9–F13 CLOSED / aut138 doble PASS; Decision Report y shortlist condicionada para reunión externa. |
| 0.5.8 | 2026-10-14 | BRAND-CAND-007 F7–F8 CLOSED, aut132/aut133 doble PASS, Founder Review aprobado, HOLD externo. |
| 0.5.7 | 2026-10-14 | Checkpoint BRAND-CAND-007 F4–F6, aut131 triple doble PASS, F7 siguiente. |
| 0.5.6 | 2026-10-13 | Checkpoint BRAND-CAND-007 F0–F3, aut128 PASS, F4 siguiente. |
| 0.5.0 | 2026-10-05 | Se abre Method v2 para BRAND-CAND-010: F0 Research Brief completo en SI-RESEARCH-070; materialización y Validator pendientes; 007–009 permanecen elegibles sin abrir. |
| 0.4.0 | 2026-10-05 | Se cierra el primer bloque de Brand Candidate Screening: FIT-CAND-001/002/005/007 promueven a BRAND-CAND-007..010, todos CORE / PASS TO METHOD V2; Method v2 permanece sin abrir. |
| 0.3.0 | 2026-10-05 | Se congela Fitness v0.2 como baseline pre-screening: territorio revisado, cuatro misiones, cuatro candidatos activos, FIT-CAND-003/004 absorbidos y FIT-CAND-006 reclasificado como capacidad transversal. |
| 0.2.0 | 2026-10-05 | Se integra SI-BRAND-003 y se habilitan rutas de descubrimiento descendente y ascendente antes del Brand Candidate Screening. |
| 0.1.0 | 2026-10-03 | Se abre Marca Fitness como exploración reusable del Brand System. |

<!-- BRAND-CAND-010-RECONCILIATION:START -->
## BRAND-CAND-010 — baseline reconciliada vigente

`matrix-aut123-brand-cand-010-post-close-core-snapshot-reconciliation.xlsx` / `23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb` es la baseline post-close vigente tras Data Fidelity Preflight v2.4 PASS + Matrix Validator PASS.

```text
aut118 → F13 histórico / 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a
aut119 corrected → reconciliación intermedia / superseded before publication
aut120 → data-fidelity baseline / 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2 / SUPERSEDED
aut121 → primera materialización / Matrix Validator FAIL por vocabulario
aut121 corrected → marketplace economics / dual PASS / SUPERSEDED / 7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc
aut122 → current-core materialization / v2.3 PASS / SUPERSEDED / 67e850c0a40fb274629429587f9ce5b500eddb51da6580fccb2c48f060dba4ba
aut123 → core + pre-projection snapshot / CURRENT / 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb
```

`aut123` conserva snapshot pre-proyección, ledger de verificaciones y core vigente.

Resultado estratégico sin cambios: NO PORTFOLIO FINALIST / FREEZE / F14 NOT OPENED.
<!-- BRAND-CAND-010-RECONCILIATION:END -->
