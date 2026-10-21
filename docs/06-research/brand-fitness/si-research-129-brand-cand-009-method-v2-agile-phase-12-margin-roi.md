---
id: si-research-129
title: BRAND-CAND-009 — Method v2 Agile — Fase 12 — Margin + ROI
description: Evaluación de disponibilidad del margen y ROI sin introducir costos supuestos ni recalcular F11.
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
phase: F12
mode: AUTO
baseline_revision: aut169
baseline_sha256: 1c3119c7070bb70122bcde4100c1b01047237c093500def751f5bbcd27e1c8f8
matrix_revision: aut170
matrix_output: matrix-aut170-brand-cand-009-phase12-margin-roi-readiness.xlsx
matrix_sha256: 8af1e46af2d70d40baac83667ad80cb1476284bc2258398bd442ba14c849f4b0
structural_audit: PASS
validation_status: DOUBLE_PASS_CONFIRMED
publication_status: READY_FOR_F9_F13_DOCUMENTARY_CHECKPOINT
---

# SI-RESEARCH-129 — BRAND-CAND-009 — F12: Margin + ROI

<!-- BRAND-CAND-009-F9-F13-CANONICAL-STATUS:START -->
## Estado canónico — cierre AUTO confirmado el 21/10/2026

**F12 CLOSED / AUTO / DOUBLE PASS CONFIRMED.** Matriz privada `aut170` con SHA-256 `8af1e46af2d70d40baac83667ad80cb1476284bc2258398bd442ba14c849f4b0`; **Data Fidelity Preflight v2.4 PASS** y **Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` PASS**, sin errores, advertencias, findings o limitations. La auditoría estructural PASS preservó 29 hojas, 1.958 fórmulas, referencias y celdas históricas; únicamente cambió interpretación autorizada. No se requiere Founder Approval para una fase AUTO.

**Conclusión vigente:** Faltan costo nacionalizado, precio de venta propio, gastos del canal e inversión: **margen bruto, neto, ROI y payback NO CALCULABLES**. No se imputan ceros ni costos ficticios.

**Gobierno:** F0–F8 estaban CLOSED/PUBLISHED en `234abec`. **F9–F13 quedan CLOSED a nivel metodológico; checkpoint documental F9–F13 en preparación, no publicado hasta commit/push. F14 NOT OPENED.** No se autorizaron RFQ, contacto comercial, muestras, homologación, negociación, importaciones, pedidos ni compras. Los datos económicos no confirmados conservan el estado desconocido.

> **Lectura histórica:** los párrafos posteriores que mencionan `PENDING_DOUBLE_PASS`, fases posteriores aún no abiertas o documentos privados describen el momento de materialización previo al cierre. Este bloque y el frontmatter reconciliado son el estado canónico vigente, sin alterar la evidencia original.
<!-- BRAND-CAND-009-F9-F13-CANONICAL-STATUS:END -->

## 1. Contrato y alcance

El contrato `SI-BIM-PROC-003 v1.0.7` establece **F12: F11 → Margin + ROI; interpreta, no recalcula**. F11 `aut169` se cerró con **Data Fidelity Preflight v2.4 PASS + Matrix Validator 0.1.0 / full-matrix-v5 0.7.0 PASS**, sin warnings el 21/10/2026. F12 es **AUTO** y no requiere intervención del Founder para decidir su contenido; sí requiere doble PASS sobre esta nueva matriz antes de CLOSED. F13 y F14 siguen **NOT OPENED**.

**Resultado:** con la evidencia F8–F11 disponible, **margen bruto, margen neto, ROI y período de recupero NO SON CALCULABLES**. No se asigna 0%, no se reemplazan valores faltantes por 0 ni se usan escenarios sintéticos de F11 para completar una estructura de costos.

## 2. Fuente, trazabilidad y frontera de validez

- **Mercado Libre (histórico 19/10/2026):** ML-0189..0192, precios de oferta de terceros, en ARS y USD utilizando FX histórico ARS 1.540/USD con fuente secundaria declarada. No son PVP propio ni pedidos pagados.
- **Alibaba (capturas F8):** COT-0073..0080, ocho fichas vinculadas a `SRC`, `EVID`, URL de ficha individual, PDF y SHA-256 en `f8-source-manifest-009.json`. Son precios publicados, no ofertas formales ni FOB negociados. `COT-0075` es una variante **elástica adyacente** de `BASE-FIT-010`, excluida del comparable exacto.
- **F10:** ocho productos con datos parciales de packing individual y peso; **cero cajas mayoristas verificadas**, sin CBM/volumen facturable, NCM, tributos, FOB o flete confirmado.
- **F11:** siete pantallas matemáticas con múltiplos de paridad y factores **SINTÉTICOS** 1,5×/2×/3×. Dos corresponden a `BASE-FIT-012`, sólo diagnóstico, `SAFETY-GATED`. Esos factores **no son costos landed**, tasas de importación ni márgenes.

El archivo `margin-roi-readiness-ledger-aut170.json` conserva por oferta los IDs de fuente, la URL y SHA de cada PDF, los precios históricos y los campos económicos faltantes, expresados como `null`.

## 3. Qué se necesita para calcular Margin + ROI de verdad

**La ausencia de datos impide calcular, no implica rentabilidad cero ni favorable.** Antes de modelar deben conocerse, por SKU seleccionado: (a) costo landed unitario con NCM, aranceles/impuestos, gastos aduaneros, seguro, flete y packing mayorista; (b) precio de venta propio y tratamiento impositivo; (c) comisiones de canales, cobranza, envío final, packaging y devoluciones; (d) inversión inicial, inventario, capital de trabajo y plazos; (e) velocidad/volumen de venta y costos de adquisición de clientes. La validación técnica de seguridad condiciona adicionalmente los productos que soportan carga corporal.

De forma conceptual: **margen unitario requiere precio neto propio menos costos unitarios atribuibles**; **ROI necesita un beneficio/incremento neto respecto del capital comprometido en un período declarado**. Sin esos denominadores y numeradores, no hay un ROI válido. Los precios de Mercado Libre de terceros y los multiplicadores F11 no sustituyen dichos inputs.

## 4. Interpretación por Product Base

| Product Base | Resultado F12 | Fundamento | Acción permitida |
|---|---|---|---|
| `BASE-FIT-010` | **LEAD — CONDITIONAL / MARGIN + ROI NOT CALCULABLE** | Dos listados funcionalmente condicionados, `COT-0073/0074`; `COT-0075` ELÁSTICA excluida. Brecha F9/F11 no cubre gastos reales | Mantener candidato para evaluación posterior, sin adjudicar fabricante |
| `BASE-FIT-011` | **SECONDARY — CONDITIONAL / MARGIN + ROI NOT CALCULABLE** | Tres construcciones distintas (`COT-0076..0078`); transporte y apoyo/peso complican equivalencia y costo real | Mantener alternativa sin comparar con ROI inventado |
| `BASE-FIT-012` | **SAFETY-GATED / NO COMMERCIAL CLEARANCE** | `COT-0079/0080` carecen de ensayos estructurales, presión, fricción, fatiga y reconciliación técnica | No habilitar selección comercial aunque los precios muestren aparente brecha |
| `BASE-FIT-013` | **DEFER — REOPENABLE / NO ORIGIN** | Sin COT en F8, sin datos mínimos para pantalla ni ROI | No extrapolar desde las otras Product Bases |

## 5. Decisión metodológica y preparación de F13

- `F12 = FINANCIAL_READINESS_SCREEN_COMPLETE / MARGIN_AND_ROI_NOT_DETERMINABLE`.
- No elevar ninguna Product Base a `APPROVED TO BUY`; no declarar márgenes, ROI, payback, flete unitario ni costos nacionalizados.
- `BASE-FIT-010` se conserva como LEAD condicionada; `BASE-FIT-011`, alternativa secundaria; `BASE-FIT-012` continúa SAFETY-GATED; `BASE-FIT-013`, diferida.
- La siguiente fase `F13 (AUTO)` debe **integrar F3–F12**, mantener estos bloqueos y preparar la shortlist final **condicionada a socio + despachante**, sin abrir F14 implícitamente.
- Sin RFQ, proveedor seleccionado, muestras, homologaciones, importación ni contacto hasta la conversación externa acordada.

## 6. Materialización y gate

Baseline `aut169` SHA `1c3119c7070bb70122bcde4100c1b01047237c093500def751f5bbcd27e1c8f8` / DOUBLE PASS registrado en `validation-aut169-brand-cand-009-f11.log`. `aut170` SHA `8af1e46af2d70d40baac83667ad80cb1476284bc2258398bd442ba14c849f4b0`. Auditoría estructural local: 29 hojas, 1.958 fórmulas conservadas, exactamente 7 celdas de interpretación modificadas (`Nichos!AD41:AF41` y `Productos Base!N107:N110`), sin cambios de precios, evidencia cruda, fórmulas ni hoja `Simulación Margen`. No se cargan filas ficticias ni se simula ROI.

**VALIDACIÓN CANÓNICA: PENDING_ON_FOUNDER_MAC.** Debe ejecutarse Data Fidelity Preflight + Matrix Validator. Documentación privada hasta checkpoint F9–F13. No operaciones Git.
