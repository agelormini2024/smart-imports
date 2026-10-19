---
id: si-research-110
title: BRAND-CAND-008 — Method v2 — F7 Shortlist pre-origin
description: Evaluación preliminar de elegibilidad pre-origin de BASE-FIT-009 a partir de F6 reconciliada.
version: 0.1.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-19
updated: 2026-10-19
brand: brand-fitness
brand_candidate: BRAND-CAND-008
source_hypothesis: FIT-CAND-002
scope_alias: Nicho ID 39
phase: F7
mode: AUTO
baseline: aut146
baseline_sha256: 7fa57317c2ec2987c162644a16a234e7156e93eac47534da52ac43448d06525e
matrix_output: matrix-aut147-brand-cand-008-phase7-shortlist-pre-origin.xlsx
matrix_output_sha256: 68e5b7797a05d33e289f1dd928507b434414673ef98c313e82a999ec318392d5
validation_status: DOUBLE_PASS
publication_status: PREPARED_FOR_F4_F13_CHECKPOINT
---

# SI-RESEARCH-110 — BRAND-CAND-008 — F7 Shortlist pre-origin

> **Estado vigente al 19/10/2026: F7 Shortlist pre-origin CLOSED / Data Fidelity Preflight v2.4 PASS / Matrix Validator 0.1.0 PASS**, 0 errores, 0 advertencias, findings y limitations vacíos. Snapshot `aut147` — SHA-256 `68e5b7797a05d33e289f1dd928507b434414673ef98c313e82a999ec318392d5`. Las menciones posteriores a estados pendientes reflejan el momento de redacción previo al cierre, no el estado vigente.

## 1. Contrato, alcance y baseline

**F7 — AUTO**, conforme a `SI-BIM-PROC-003 v1.0.6`, recibe Product Bases normalizadas en F6 y produce una shortlist **pre-origin**. No agrega un score de F7, no abre F8 automáticamente, no estima costos FOB/EXW, landed, margen o ROI y no selecciona proveedor.

Baseline: `matrix-aut146-brand-cand-008-phase6-reconciled-product-base.xlsx`, SHA-256 `7fa57317c2ec2987c162644a16a234e7156e93eac47534da52ac43448d06525e`. El 19/10/2026, el log de F6 confirmó Data Fidelity Preflight v2.4 **PASS** y Matrix Validator 0.1.0 (`full-matrix-v5 0.7.0`) **PASS**, sin findings ni limitations. Quedó una sola Product Base del candidato: `BASE-FIT-009`.

La decisión inicial F6 de cero Product Bases en `aut145` queda preservada como antecedente; `aut146` reconcilió una decisión de tipo B. Los scores de fases cerradas permanecen **Demanda 2/5 (Baja), Competencia 2/5 (Baja), Potencial de Marca 2/5 (Baja)**.

## 2. Única Product Base evaluada

**`BASE-FIT-009` — Tabla plegable para flexiones con agarres reconfigurables.** Familia funcional de entrenamiento de peso corporal principalmente de tren superior. Referencias `ML-0184` (MTL) y `ML-0185` (Jazak), ambas `DIRECT_CONDITIONED`. No son SKU técnicamente idénticos y sólo Jazak incorpora bandas según la captura histórica.

| Variable | Evidencia o limitación |
|---|---|
| Problema primario | Permitir una sesión de ejercicio al cambiar de espacio; ajuste sólo parcial por depender de suelo y superficie seguros |
| Demanda específica entre contextos | No demostrada; los contadores visibles no desagregan motivo ni período |
| Competencia / diferenciación | Dos soluciones similares; commodity y competencia por precio como riesgos |
| Precio local histórico | ARS 24.990 MTL y ARS 22.999 Jazak, capturas del 16/10/2026 |
| Ticket | Ambos por debajo del umbral exploratorio ARS 50.000; alerta, no veto |
| Seguridad y calidad | Verificar estabilidad, encastres, adherencia de apoyos, cargas reales e instrucciones; no inferir seguridad de reseñas |
| Primera etapa / logística | Formato plegable y sin electrónica favorecen simplicidad potencial; peso/volumen reales sin confirmar |
| Economía de importación | No hay FOB/EXW, MOQ, packing, landed, margen ni ROI validado |

**Fuentes originales conservadas:**

- `ML-0184 / SRC-0536 / EVID-0317 / MLV-0033`: https://www.mercadolibre.com.ar/tabla-push-up-board-mtl-plegable-multifuncional-10-en-1-ejercicio-pecho-espalda-hombros-triceps-portatil-ligera-antideslizante-entrenamiento-completo-fuerza-tonificacion-fitness-hogar-gimnasio/p/MLA61425889
- `ML-0185 / SRC-0537 / EVID-0318 / MLV-0034`: https://www.mercadolibre.com.ar/tabla-push-up-multifuncional-jazak-con-bandas-de-resistencia-para-gym-fitness/p/MLA69466075

Los PDFs y sus hashes permanecen privados. No reverificar ni reescribir los datos históricos de F3 durante F7. Las demás publicaciones `ML-0186..0188` y fuentes permanecen como comparables adyacentes y no se convierten en Product Bases.

## 3. Decisión F7 propuesta — aún no validada en matriz

**`BASE-FIT-009`: PASS TO ORIGIN — CONDITIONED / EXPLORATORY ONLY / LOW-TICKET + DIFFERENTIATION + SAFETY GATES.**

Esta es una propuesta de triage **limitada**: sólo habilitaría una exploración mínima en F8 para comprobar si existe una arquitectura OEM real, trazable y diferenciable, con seguridad y costo de origen que puedan justificar continuar. No equivale a aprobar importación ni a recomendar compra. La propuesta se fundamenta en que existe una Product Base normalizada y una presencia comercial observable, pero ninguna ventaja de marca confirmada.

**Preguntas decisivas para F8 (COLLABORATIVE):**

1. ¿Existen productos realmente equivalentes a la función de `BASE-FIT-009`, con modelo y componentes inequívocos, no simples kits genéricos?
2. ¿Qué evidencia técnica existe sobre la seguridad de los encastres, apoyos, capacidades declaradas y materiales?
3. ¿Se puede diferenciar la propuesta mediante calidad, instrucciones y progresión verificables, evitando una competencia puramente por precio?
4. ¿Algún listing público muestra precio, cantidad mínima, packaging y peso trazables al **mismo** SKU? No tratar la publicación como cotización formal.
5. ¿El costo preliminar de origen, sumado a las fricciones locales aún desconocidas, hace razonable seguir investigando un ticket histórico inferior a ARS 50.000?

**Condición de no avance:** si F8 no identifica una variante concreta con diferenciación y seguridad al menos defendibles, `BASE-FIT-009` debería pasar a `DEFER/STOP — REOPENABLE` sin forzar datos económicos. El objetivo de completar Method v2 no autoriza declarar cerradas F9–F13 si faltan sus inputs mínimos reales.

## 4. Materialización y cierre pendiente

El documento es **DRAFT**, no cierre F7. Se materializó `matrix-aut147-brand-cand-008-phase7-shortlist-pre-origin.xlsx`, derivada de `aut146` sin sobrescribirla; SHA-256 `68e5b7797a05d33e289f1dd928507b434414673ef98c313e82a999ec318392d5`. La auditoría OOXML local verificó 29 hojas, 1.942 fórmulas, cinco URLs originales conservadas y cambios exclusivamente en `Nichos!AD40:AF40` y `Productos Base!N106`. Esto **NO sustituye** el doble PASS canónico.

Para declarar F7 `CLOSED`, ejecutar `scripts/validate-method-v2-checkpoint.sh` para F7 y comprobar **Data Fidelity Preflight PASS + Matrix Validator PASS**, luego registrar los resultados en este Research.

F8 permanecerá `NOT OPENED` hasta entonces; su modalidad es **COLLABORATIVE**, con investigación y aprobación explícita del Founder para cierre. No ejecutar Git todavía: el checkpoint documental se consolidará según la cadencia vigente.

## Nota de cierre consolidada — 19/10/2026

La fase **F7 Shortlist pre-origin** quedó **CLOSED** tras el doble PASS canónico de `aut147` (SHA-256 `68e5b7797a05d33e289f1dd928507b434414673ef98c313e82a999ec318392d5`); no se reabren sus fuentes ni se altera la historia de la evaluación. La evidencia posterior se analiza en las fases siguientes, sin trasladar aprobaciones de un gate a otro.
