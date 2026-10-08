---
id: si-research-074
title: BRAND-CAND-010 — Method v2 Agile — Fase 3 — Demand
description: Evaluación colaborativa de demanda local para movimiento integrado a la jornada sedentaria mediante evidencia de Mercado Libre Argentina.
version: 0.1.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-08
updated: 2026-10-08
brand: brand-fitness
brand_candidate: brand-cand-010
method: method-v2-agile
phase: F3
mode: COLLABORATIVE
---

# SI-RESEARCH-074 — BRAND-CAND-010 — F3 Demand

## 1. Input vigente

```text
F0 CLOSED — aut105 PASS
F1 CLOSED — aut106 PASS
F2 CLOSED — aut107 PASS
F3 — COLLABORATIVE
```

F3 combina recolección humana de evidencia local en Mercado Libre Argentina con normalización, análisis y materialización automática.

## 2. Pregunta de F3

> ¿Existe demanda local observable y suficientemente defendible por soluciones que permitan integrar movimiento físico real dentro de una jornada sedentaria?

F3 no estima tamaño total de mercado ni crea Product Bases.

## 3. Reglas metodológicas

```text
VENTAS VISIBLES ≠ TAMAÑO DE MERCADO
SIN VENTAS VISIBLES ≠ SIN DEMANDA
OFERTA DISPONIBLE ≠ EVIDENCIA DE DEMANDA
QUERY COHORT ≠ PRODUCT BASE
SEARCH TERM ≠ MARKET SEGMENT
DEMANDA DE REHABILITACIÓN / FITNESS
≠
DEMANDA DEL JOB WORK-WHILE-MOVING
```

## 4. Muestra

Se normalizaron **24 publicaciones únicas** de Mercado Libre Argentina:

```text
ML-0152 … ML-0175
```

Distribución conceptual:

```text
A1 — walking pad / cinta compacta                  8
A3 — ciclo / pedalera sentada                     6
A2 — elíptica sentada bajo escritorio             5
A4 — balance board para standing desk             4
A3/A2 — mini pedalera elíptica adyacente          1
TOTAL                                              24
```

No se crean Product Bases en F3. Esa frontera corresponde a F6.

## 5. A1 — Walking pad / cinta compacta

```text
LOCAL OFFER SIGNAL: CONFIRMED
LOCAL DEMAND SIGNAL: CONFIRMED — MODERATE
DEMAND DEPTH: CONCENTRATED IN FEW MODELS
```

La evidencia incluye comparables directos como G-Fitness Walking Pad y Force by Gadnic Ultra Slim, además de THERUN bajo escritorio sin tracción visible. Cintas tradicionales/compactas se conservan sólo como sustitutos o benchmarks de categoría amplia.

Conclusión: **Minimum Sufficient Evidence alcanzada** para una señal positiva de demanda específica.

## 6. A3 — Ciclo / pedalera sentada

```text
LOCAL OFFER SIGNAL: CONFIRMED
JOB-SPECIFIC DEMAND SIGNAL: WEAK / NOT DEMONSTRATED
ADJACENT PRODUCT-FORM DEMAND: STRONG
```

La demanda visible fuerte está dominada por rehabilitación, movilidad y ejercicio de bajo impacto. Existen comparables explícitamente under-desk, pero con precios altos y sin tracción visible suficiente.

Conclusión: no transferir ventas de rehabilitación al job de movimiento durante trabajo.

## 7. A2 — Elíptica sentada bajo escritorio

```text
LOCAL OFFER SIGNAL: CONFIRMED
DIRECT COMPARABLES: PRESENT
LOCAL DEMAND SIGNAL: WEAK / NOT DEMONSTRATED
```

Cubii JR1, Lubbygim y otros comparables muestran que la arquitectura existe en ML Argentina, pero la tracción visible específica es baja.

## 8. A4 — Balance board para standing desk

```text
LOCAL OFFER SIGNAL: CONFIRMED
DIRECT COMPARABLES: PRESENT
LOCAL DEMAND SIGNAL: WEAK / NOT DEMONSTRATED
ADJACENT DEMAND: PRESENT IN PROPRIOCEPTION / FITNESS
```

Las tablas específicas para escritorio tienen oferta, pero no demanda visible suficiente. Las tablas de propiocepción muestran otro job y se conservan como adyacentes.

## 9. Resultado consolidado

```text
A1 — walking pad                         → POSITIVE / MODERATE
A3 — under-desk cycle / pedal           → WEAK JOB-SPECIFIC / STRONG ADJACENT
A2 — under-desk elliptical              → WEAK / NOT DEMONSTRATED
A4 — standing-desk balance board        → WEAK / NOT DEMONSTRATED
```

La demanda del candidato se considera **positiva pero heterogénea**.

## 10. Evaluación

```text
EVAL-0029
Criterio: Demanda
Valor: 3/5
Confianza: Media
Soporte: EVID-0285
```

Racional:
- existe demanda específica observable para walking pads;
- la señal está concentrada en pocos modelos;
- el formato pedalera tiene fuerte demanda adyacente, pero no job-specific;
- elípticas y balance boards under-desk tienen oferta pero tracción visible débil;
- Mercado Libre no permite inferir tamaño total de mercado.

## 11. Materialización

```text
matrix-aut108-brand-cand-010-phase3.xlsx
```

Registros agregados:

```text
Publicaciones ML : ML-0152 ... ML-0175
Fuentes          : SRC-0480 ... SRC-0504
Evidencias       : EVID-0285
Evaluaciones     : EVAL-0029
Evidencia Fuentes: EVSRC-0627 ... EVSRC-0651
```

No se crean Product Bases en F3.

## 12. Gate

Estado previo a validación:

```text
F3 CLOSED — aut108 PASS
```

Cierre confirmado:

```text
F3 CLOSED — aut108 PASS
→ F4 — Competition completada posteriormente
→ se reutilizaron las mismas publicaciones de Mercado Libre
```
