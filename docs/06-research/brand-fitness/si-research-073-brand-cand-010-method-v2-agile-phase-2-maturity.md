---
id: si-research-073
title: BRAND-CAND-010 — Method v2 Agile — Fase 2 — Maturity
description: Evaluación de madurez de las arquitecturas relevantes para movimiento integrado a la jornada sedentaria.
version: 0.2.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-07
updated: 2026-10-08
brand: brand-fitness
brand_candidate: brand-cand-010
method: method-v2-agile
phase: F2
mode: AUTO
---

# SI-RESEARCH-073 — BRAND-CAND-010 — Fase 2 — Maturity

## 1. Estado

```text
F1 CLOSED — aut106 PASS
F2 CLOSED — aut107 PASS
F3 COMPLETED POSTERIORMENTE — aut108 PASS
```

## 2. Pregunta de F2

> ¿Qué tan estabilizada está cada arquitectura en términos de mecanismo, formato comercial, mantenimiento, seguridad, infraestructura necesaria y heterogeneidad entre implementaciones?

F2 no mide todavía:

```text
DEMANDA ARGENTINA
COMPETENCIA LOCAL
BRAND POTENTIAL
ORIGEN
ECONOMÍA
PRODUCT BASES
```

## 3. Regla de interpretación

`MATURITY` no equivale a atractivo comercial.

Se observa cualitativamente:

1. mecanismo técnicamente establecido;
2. formatos comerciales repetibles;
3. disponibilidad de múltiples implementaciones;
4. mantenimiento conocido;
5. riesgos operativos identificables;
6. dependencia de instalación / infraestructura;
7. heterogeneidad entre productos;
8. posibilidad de comparar especificaciones relevantes.

Estados de trabajo:

```text
HIGH
MEDIUM-HIGH
MEDIUM
LOW-MEDIUM / CONDITIONAL
```

## 4. Lectura consolidada

| Arquitectura | Madurez | Condición dominante |
|---|---|---|
| A1 — walking pad / under-desk treadmill | HIGH | ELECTRICAL / MOTOR / NOISE / SAFETY / LOGISTICS |
| A2 — elíptica sentada bajo escritorio | MEDIUM-HIGH | CLEARANCE / ERGONOMICS / MECHANICAL QA |
| A3 — ciclo / pedalera sentada bajo escritorio | HIGH | CLEARANCE / STABILITY / MECHANICAL QA |
| A4 — balance board para standing desk | MEDIUM-HIGH | STABILITY / FALL RISK / STANDING-DESK DEPENDENCY |
| A5 — rocker footrest | HIGH como ergonomía; CONDITIONAL para este candidate | JOB BOUNDARY |
| A6 — mini stepper | HIGH como fitness; EXCLUDED por boundary | BRAND-CAND-008 |

## 5. Señales por arquitectura

### A1 — Walking pad

La arquitectura está fuertemente estabilizada: existen múltiples marcas y formatos actuales, con criterios de comparación repetidos —velocidad, dimensiones de deck, potencia, ruido, capacidad, plegado y guardado—.

La heterogeneidad relevante permanece en:
- motor y durabilidad;
- ruido real;
- longitud/ancho de cinta;
- peso y logística;
- seguridad;
- tensión eléctrica;
- uso real durante tareas.

**Maturity:** `HIGH`.

Referencia:
https://www.tomsguide.com/best-picks/best-under-desk-treadmills

### A2 — Elíptica sentada bajo escritorio

La categoría es comercialmente repetible y suficientemente estable para distinguir versiones manuales y motorizadas. Cubii mantiene múltiples modelos y especifica uso sentado y compatibilidad bajo escritorio.

La heterogeneidad relevante permanece en:
- trayectoria real del pedal;
- clearance de rodillas;
- resistencia;
- manual vs motorized;
- ruido;
- estabilidad;
- peso y calidad mecánica.

**Maturity:** `MEDIUM-HIGH`.

Referencias:
https://www.consumerreports.org/health/ellipticals/best-under-desk-ellipticals-of-the-year-a2943054360/
https://help.cubii.com/hc/en-us/articles/360036305813-Will-Cubii-ellipticals-fit-under-my-desk
https://help.cubii.com/hc/en-us/articles/360046065154-Can-I-stand-on-Cubii-ellipticals

### A3 — Ciclo / pedalera bajo escritorio

El mecanismo de mini ciclo estacionario es técnicamente simple y estabilizado. Las variables comerciales relevantes —altura de pedal, resistencia, estabilidad, ruido, straps, display y calidad del volante— son comparables.

La principal incertidumbre futura no es madurez tecnológica sino fit local y demanda.

**Maturity:** `HIGH`.

### A4 — Balance board para standing desk

La arquitectura está comercialmente establecida y existen productos explícitamente diseñados para standing desks. El mecanismo es simple y de bajo mantenimiento.

Permanece condicionada por:
- dependencia de trabajo de pie;
- estabilidad;
- riesgo de caída;
- peso máximo;
- intensidad de movimiento;
- frontera entre actividad y ergonomía.

**Maturity:** `MEDIUM-HIGH`.

Referencias:
https://fluidstance.com/pages/standing-desk-balance-boards
https://fluidstance.com/pages/level-flow

### A5 — Rocker footrest

El mecanismo es maduro como accesorio ergonómico, pero su madurez no resuelve el problema metodológico: puede pertenecer más a confort/ergonomía que a actividad física.

**Maturity:** `HIGH` en su categoría.
**Fit en BRAND-CAND-010:** `CONDITIONAL / SUPPORT`.

### A6 — Mini stepper

La arquitectura es madura como fitness compacto, pero queda fuera del core por boundary.

**Maturity:** `HIGH`.
**Fit en BRAND-CAND-010:** `EXCLUDED`.

## 6. Conclusión

Las arquitecturas core presentan madurez suficiente para pasar a medición de demanda.

La principal incertidumbre ya no es si las soluciones existen o si sus mecanismos son comprensibles, sino:

```text
¿EXISTE DEMANDA LOCAL OBSERVABLE EN ARGENTINA
PARA ESTAS FAMILIAS DENTRO DEL JOB DEFINIDO?
```

## 7. Gate

```text
PASS TO F3 — DEMAND
```

F3 fue el primer gate `COLLABORATIVE`.

Cierre confirmado:

```text
aut107 → Matrix Validator PASS
→ F2 CLOSED
→ F3 — Demand / Mercado Libre Argentina completada posteriormente
```

No se crean Product Bases antes de F6.
