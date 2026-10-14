---
id: si-research-096
title: BRAND-CAND-007 — Method v2 — F7 Shortlist pre-origin
version: 0.1.1
status: closed
phase: F7
mode: AUTO
brand: brand-fitness
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
scope_alias: Nicho ID 38
scope_value: Marca Fitness — fuerza accesible y compacta
baseline: aut131
matrix: aut132
created: 2026-10-14
updated: 2026-10-14
related:
  - si-bim-proc-003
  - si-decision-020
  - si-research-092
  - si-research-093
  - si-research-094
  - si-research-095
---

# SI-RESEARCH-096 — BRAND-CAND-007 — F7 Shortlist pre-origin

## 1. Alcance y prerrequisitos

F7 se ejecuta en modalidad **AUTO**, sobre las cuatro Product Bases creadas en F6 (`BASE-FIT-005..008`) y la matriz `aut131` con **triple doble PASS** (F4, F5 y F6). No crea un criterio de scoring adicional, no reabre F3–F5 ni crea nuevos Product Bases. No realiza sourcing ni afirma origen o rentabilidad.

Cohorte comercial preservada: `ML-0178..ML-0183`, seis PDF de Mercado Libre capturados el **13/10/2026**, con `SRC-0525..SRC-0530` y verificaciones `MLV-0027..0032`. Demanda F3: **3/5, Confianza Media** (aprobación Founder); competencia F4: **3/5, Media**; potencial de marca F5: **3/5, Baja**.

El propósito de F7 es filtrar qué soluciones justifican investigación preliminar de origen (F8) bajo criterios preexistentes: relevancia central para la misión de fuerza cotidiana, evidencia de demanda específica, simplicidad para primera etapa, fragilidad/seguridad, peso/volumen y posventa. **PASS TO ORIGIN no equivale a recomendación de importar.**

## 2. Decisión por Product Base — capa D validada

| Product Base | Decisión F7 validada | Razonamiento | Condición de reapertura / avance |
|---|---|---|---|
| `BASE-FIT-005` — Bandas tubulares con manijas y anclaje | **PASS TO ORIGIN — CONDITIONED / CORE / FIRST-STAGE CANDIDATE** | Alineación central con fuerza, bajo volumen/peso potencial y sistema compacto. Cohorte: `ML-0178`; las ventas visibles son una señal histórica de producto, no forecast de marca nueva. | En F8 distinguir calidad, bandas y resistencia real, mecanismo y seguridad del anclaje, accesorios, manuales, capacidad de reposición y claims verificables. |
| `BASE-FIT-006` — Bandas loop de resistencia y asistencia | **OUT OF SHORTLIST — DEFER / JOB-CONDITIONED / HIGH COMMODITY** | Compatible con fuerza pero con usos amplios de movilidad/asistencia; el contador de la publicación no determina cuánto corresponde al problema de fuerza. Riesgo de commodity y solapamiento operativo con 005. | Reabrir con evidencia de demanda específica para fuerza y una propuesta de progresión, calidad y economía defendible. |
| `BASE-FIT-007` — Mancuernas/barra ajustables, formato 20 kg | **PASS TO ORIGIN — CONDITIONED / DEMAND LEAD / LOGISTICS GATE** | La progresión de carga tiene gran alineación con fuerza y comparables `ML-0180/0181` con señales comerciales. Riesgos materiales de peso, fijaciones, roscas, materiales y logística; **no se presume aptitud de primera importación**. | En F8 comprobar configuraciones, materiales, packing, peso real y posibilidades de control de calidad; costos detallados corresponden a F9–F11. |
| `BASE-FIT-008` — Sistema de suspensión y anclaje | **OUT OF SHORTLIST — DEFER / CRITICAL SAFETY GATE** | Ajuste funcional válido y formato compacto, pero las consecuencias de falla de anclaje/costuras son graves. Claims de 120/200 kg sin ensayos externos no permiten reducir el riesgo. | Reabrir sólo con información técnica independiente o verificable sobre resistencia, anclajes, costuras, instrucciones y responsabilidades de garantía. |

Estas son **decisiones de triage pre-origin**. No se agrega un score de F7; los scores F3–F5 permanecen inalterados. Tampoco se infieren costo FOB, MOQ, disponibilidad OEM, certificaciones reales ni seguridad comprobada.

## 3. Capas de evidencia y límites

- **Capa A — Raw Evidence:** seis fichas/PDF y registros `ML-0178..0183`, fuentes y ledger existentes. Ventas históricas de producto/catálogo no representan ventas mensuales ni cuota de mercado; precios ARS refieren exclusivamente al 13/10/2026.
- **Capa B — Clasificación:** `BASE-FIT-005..008` normalizadas en F6. Esta fase no mezcla dos arquitecturas por similitud aparente de la oferta.
- **Capa C — Interpretación:** relevancia para fuerza, carga de seguridad, riesgo commodity y complejidad logística, explicitados como inferencia con evidencia limitada.
- **Capa D — Gate:** dos `PASS TO ORIGIN — CONDITIONED`, dos `DEFER` con condiciones de reapertura. No se agrega una evaluación escalar ni se reemplazan los criterios preexistentes.

El shortlist habilitado al obtener F7 doble PASS es `BASE-FIT-005` y `BASE-FIT-007`. `BASE-FIT-006` y `008` no se investigan sistemáticamente en origen sin reapertura fundada.

## 4. Materialización de F7 — aut132

```text
Input: aut131 / F4–F6 CLOSED / triple doble PASS
Output: matrix-aut132-brand-cand-007-phase7-shortlist-pre-origin-pending-gate.xlsx
SHA-256: ca2aa758788c53be1307aa10bb0c3b7ba03cbda0126141b1eb121844979d828b
Productos Base!N102:N105: decisiones F7 añadidas a observaciones históricas
Nichos!AD39:AF39: próxima acción, vínculo documental y decisión F7
Publicaciones ML, Verificaciones ML, Fuentes, Ventas, ARS/USD y FX: sin cambio intencional
Hoja/filas/fórmulas: 29 hojas, 1.942 fórmulas y cantidad de celdas preservadas
Data Fidelity Preflight v2.4: PASS — 6 publicaciones, 6 verificaciones, 4 Product Bases
Matrix Validator full-matrix-v5 0.7.0: PASS — errores=0, warnings=0, info=0
F7: CLOSED / AUTO — DOBLE PASS — aut132
```

**No existió un checkpoint documental separado en F7.** La doble validación se ejecutó al abrir F8 (14/10/2026), antes del screening de origen. El cierre documental se integra con F8, sin crear una interrupción intermedia.

## 5. Handoff hacia F8

```text
F8 — Origin Screening / Alibaba
mode: COLLABORATIVE
Founder participation: REQUIRED
Founder Review: REQUIRED FOR CLOSE
Active Product Bases: BASE-FIT-005, BASE-FIT-007 — F7 doble PASS
External supplier responses/RFQs: not required at this screening gate
```

Mantener: `ORIGIN CONFIRMED ≠ SUPPLIER SELECTED`, `PUBLIC LISTING ≠ FORMAL QUOTE`, `DECISION-GRADE ≠ PROCUREMENT-GRADE`.

## 6. Evidencia canónica de cierre de F7

`apertura-f8-brand-cand-007.log` registra SHA-256 `ca2aa758788c53be1307aa10bb0c3b7ba03cbda0126141b1eb121844979d828b`, Data Fidelity PASS, Matrix Validator PASS sin hallazgos y F7 elegible para cierre. El checkpoint documental único F7–F8 registra este cierre junto con el Founder Review de F8, sin cambiar las decisiones de F7.
