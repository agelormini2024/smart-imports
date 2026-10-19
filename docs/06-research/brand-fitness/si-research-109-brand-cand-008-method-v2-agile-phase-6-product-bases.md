---
id: si-research-109
title: BRAND-CAND-008 — Method v2 Agile — Fase 6 — Product Bases
description: Reconciliación controlada de decisión en F6 (Tipo B); normalización condicionada de BASE-FIT-009.
version: 0.2.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-16
updated: 2026-10-19
brand_candidate: BRAND-CAND-008
source_hypothesis: FIT-CAND-002
scope_alias: Nicho ID 39
phase: F6
mode: AUTO
correction_type: DECISION_IMPACTING_TYPE_B
historical_f6_snapshot: matrix-aut145-brand-cand-008-phase6-no-product-bases.xlsx
historical_f6_sha256: 73ce0b6ccdb960277e969e11878e7e56ae661a3b71a0b63bc52581fc2a1c496a
matrix_output_validated: matrix-aut146-brand-cand-008-phase6-reconciled-product-base.xlsx
matrix_output_sha256: 7fa57317c2ec2987c162644a16a234e7156e93eac47534da52ac43448d06525e
product_bases_validated: 1
validation_status: DOUBLE_PASS
publication_status: PREPARED_FOR_F4_F13_CHECKPOINT
---

# SI-RESEARCH-109 — BRAND-CAND-008 / F6 — Reconciliación de Product Bases

> **Estado vigente al 19/10/2026: F6 Product Bases (reconciliada) CLOSED / Data Fidelity Preflight v2.4 PASS / Matrix Validator 0.1.0 PASS**, 0 errores, 0 advertencias, findings y limitations vacíos. Snapshot `aut146` — SHA-256 `7fa57317c2ec2987c162644a16a234e7156e93eac47534da52ac43448d06525e`. Las menciones posteriores a estados pendientes reflejan el momento de redacción previo al cierre, no el estado vigente.

## 1. Motivo de la corrección

F6 fue cerrada inicialmente el 16/10/2026 con **0 Product Bases** y `aut145` con doble PASS. Ese archivo es idéntico en bytes a `aut144` y **se conserva sin modificaciones**. La evaluación inicial exigió acreditar diferenciación y oportunidad comercial para admitir siquiera una Product Base. Una revisión posterior distinguió entre **normalización funcional (F6)** y **evaluación de elegibilidad/shortlist (F7)**.

La corrección **modifica una decisión**, no corrige un fallo del Matrix Validator. Conforme al contrato `SI-BIM-PROC-003 v1.0.6`, sección 12, se trata como **Tipo B — Decision-impacting correction**: F6 `REOPEN`, nueva materialización, doble validación y conservación íntegra del histórico. No se reabren F0–F5, ni se alteran Demanda 2/5 Baja, Competencia 2/5 Baja o Potencial de Marca 2/5 Baja.

El paquete anterior de cierre `STOP — REOPENABLE / FREEZE` para F4–F6 **queda suspendido y no debe aplicarse**.

## 2. Identidad Product Base propuesta

**`BASE-FIT-009` — Tabla plegable para flexiones con agarres reconfigurables.**

Se trata de una familia funcional de soportes reconfigurables para ejercicios de peso corporal, principalmente del tren superior, que puede guardarse plegada. No se la presenta como un SKU, un diseño homologado, una tecnología exclusiva ni una recomendación de compra. La variante de Jazak añade bandas, pero su inclusión no transforma a las dos referencias en productos técnicamente idénticos.

| Aspecto | Resultado documentado |
|---|---|
| Arquitectura | `SOL-008-A2` — peso corporal y soportes portátiles |
| Publicaciones directas condicionadas | `ML-0184` MTL / `ML-0185` Jazak |
| Competencia vinculada | `COMP-0182` / `COMP-0183` |
| Fuentes globales | `SRC-0536` / `SRC-0537` |
| Evidencias F3 | `EVID-0317` / `EVID-0318` |
| Verificaciones F3 | `MLV-0033` / `MLV-0034` |
| Precio histórico al 16/10/2026 | ARS 22.999–24.990 |
| Ventas literales | MTL `+500 vendidos`; Jazak `+100 vendidos`, sin período especificado |
| Ratings | 4,7 y 4,3 respectivamente |
| Comercialización | Dos vendedores distintos en esta muestra; no equivale a dos fabricantes independientes |

**URLs originales, obligatorias para la trazabilidad:**

- **MTL / ML-0184:** https://www.mercadolibre.com.ar/tabla-push-up-board-mtl-plegable-multifuncional-10-en-1-ejercicio-pecho-espalda-hombros-triceps-portatil-ligera-antideslizante-entrenamiento-completo-fuerza-tonificacion-fitness-hogar-gimnasio/p/MLA61425889
- **Jazak / ML-0185:** https://www.mercadolibre.com.ar/tabla-push-up-multifuncional-jazak-con-bandas-de-resistencia-para-gym-fitness/p/MLA69466075

Las capturas PDF privadas y sus hashes se conservan en las evidencias y registros de verificación existentes. No son cifras mensuales ni prueban demanda motivada por entrenar fuera del hogar.

## 3. Riesgos y límites que F6 no debe borrar

- **Diferenciación:** no demostrada; el formato podría ser commodity.
- **Ticket:** ambas referencias están por debajo del umbral orientativo ARS 50.000, que es una alerta y **no un veto automático**.
- **Seguridad:** estabilidad, antideslizamiento, uniones y encastres requieren pruebas por diseño concreto. Las reseñas expresan inquietudes, no evidencia concluyente de defectos generalizados.
- **Portabilidad:** plegado y transporte físicos plausibles; no está demostrada la frecuencia de uso entre contextos, su efectividad, la progresión o la disposición a pagar.
- **Economía/importación:** ningún costo EXW/FOB, NCM, landed, margen ni ROI validado.
- **Solapamiento:** no duplicar `BASE-FIT-005/006` (bandas) ni `BASE-FIT-008` (suspensión). `ML-0186..0188` (Alpina y GYM MAN) permanecen `ADJACENT` y no se vinculan a esta nueva Product Base.

**F7 será el filtro de shortlist.** Registrar una Product Base en F6 no obliga a promoverla a F8 ni a continuar fases económicas sin input legítimo.

## 4. Materialización controlada — aut146

Baseline: `aut145`, con SHA-256 `73ce0b6ccdb960277e969e11878e7e56ae661a3b71a0b63bc52581fc2a1c496a` y doble PASS anterior. El nuevo archivo **no reemplazará** `aut145`.

Modificaciones previstas únicamente en:

1. `Productos Base!A106:N106`: nueva base `BASE-FIT-009`, dos comparables directos condicionados y dos vendedores, precios históricos, riesgos y URLs originales.
2. `Publicaciones ML!Q185:R186`: vinculación funcional de MTL/Jazak a `BASE-FIT-009`. No se alteran los campos `ML ID`, fechas, precio, ventas, tipo de publicación, link, FX ni verificaciones.
3. `Competencia ML!F183:G184`: vinculación de `COMP-0182/0183` a la misma PB.
4. `Nichos!AD40:AF40`: estado y referencia al Research revisado, sin modificar los scores de F3–F5.

Controles previos: nombre/orden de las 29 hojas, 1.942 fórmulas, ID `BASE-FIT-009` libre, celdas de destino vacías salvo metadatos explícitamente autorizados, y cinco URLs originales de investigación intactas. Auditar diferencias por celda y no reserializar datos históricos restantes. El resultado debe procesarse mediante `scripts/validate-method-v2-checkpoint.sh` para **fase F6**.

**El cierre final de F6 queda pendiente de: (a) Data Fidelity Preflight v2.4 PASS, (b) Matrix Validator 0.1.0 / full-matrix-v5 0.7.0 PASS y (c) incorporación del hash resultante en este Research.** Un PASS de estructura local **no sustituye** esos controles.

## 5. Condiciones de transición

Si `aut146` supera ambos controles, el estado podrá pasar a `F6 RECONCILED / CLOSED`, y `BASE-FIT-009` podrá entrar a **F7 AUTO — Pre-Origin Shortlist**, sin ninguna promesa de clasificación favorable. F8 sigue siendo COLLABORATIVE, y todo ejercicio posterior requiere datos reales; no se deben inventar proveedores, FOB/EXW, fletes, tributos, landed, márgenes o ROI.

En el momento de preparar este documento, **`F6 REOPEN / aut146 PENDING DOUBLE PASS / F7–F14 NOT OPENED / GIT CHECKPOINT SUSPENDED`**. La actualización documental pública de F4–F6 se retomará sólo después del resultado técnico y de revisar el diff.

## 6. Adenda de cierre técnico de F6 reconciliada — 2026-10-19

El log `validation-aut146-brand-cand-008-f6.log` confirmó **Data Fidelity Preflight v2.4 PASS** y **Matrix Validator v0.1.0 / full-matrix-v5 0.7.0 PASS**, con 0 errores, 0 advertencias, findings `[]` y limitations `[]`. El preflight identificó 5 publicaciones, 5 filas de verificación y **1 Product Base** para el scope.

La baseline vigente es `matrix-aut146-brand-cand-008-phase6-reconciled-product-base.xlsx`, SHA-256 `7fa57317c2ec2987c162644a16a234e7156e93eac47534da52ac43448d06525e`. **F6 RECONCILED / CLOSED (AUTO)**. `BASE-FIT-009` queda normalizada como familia funcional, sin atribuirle viabilidad de importación. El cierre original `aut145` continúa conservado como antecedente de la reconciliación Tipo B.

Las secciones anteriores que decían «pendiente de validación» reflejan el estado **anterior al doble PASS**. No deben interpretarse como estado vigente. La transición a F7 AUTO queda habilitada por el contrato, sin reabrir F0–F5.

## Confirmación posterior de la reconciliación

`aut145` (0 Product Bases) se conserva como antecedente **válido históricamente**, no como baseline actual. `aut146` obtuvo doble PASS, normalizó `BASE-FIT-009` sin alterar `BASE-FIT-001..008` ni los registros adyacentes y quedó **F6 CLOSED — RECONCILED**. La revisión aplica la corrección Tipo B del contrato; F7–F13 se ejecutaron después sobre esa base. El paquete anterior F4–F6 que ordenaba `STOP / FREEZE` prematuro fue anulado y **no debe ejecutarse**.
