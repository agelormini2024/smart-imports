---
id: si-research-104
title: BRAND-CAND-008 — Method v2 Agile — Fase 1 — Market / Solution Map
description: Mapa de arquitecturas de solución para entrenamiento flexible y portátil, sin creación de Product Bases.
version: 0.3.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-16
updated: 2026-10-16
brand: brand-fitness
brand_candidate: brand-cand-008
method: method-v2-agile
phase: F1
mode: AUTO
---

# SI-RESEARCH-104 — BRAND-CAND-008 — F1: Market / Solution Map

## 1. Estado y linaje

```text
SCREENING: CLOSED — PASS TO METHOD V2
F0: CLOSED — AUTO / aut139 DOUBLE PASS
F0 SHA-256: ffc2478f2f1ebd46dfb7dd4242b48ea2187c4190f9f39543bd5653b15f0c99ed
F1: CLOSED — AUTO / aut140 DOUBLE PASS
MATRIX SCOPE ALIAS: Nicho ID 39
BASELINE INPUT: aut139
F1 GLOBAL SNAPSHOT: aut140 — VALIDATED / CLOSED
F1 SHA-256: e757eea904bb4f117d2be20d83903b3adb646ed66c1d85575205d55f2d5b39ab
PRODUCT BASES: NOT DEFINED
F2: OPENED — AUTO / MATURITY ASSESSMENT
F3: COLLABORATIVE / NOT OPENED
F14: NOT OPENED
```

**Contrato:** `SI-BIM-PROC-003 v1.0.6` — F1 recibe el Brief F0 y entrega un mapa de soluciones; **arquitectura ≠ Product Base**. No se reutilizan scores ni demanda del candidato `007`.

## 2. Problema y criterio de inclusión

> Mantener un entrenamiento útil aunque cambien el lugar, el tiempo disponible o el contexto cotidiano.

La arquitectura debe habilitar una **sesión intencional** y permitir adaptación al menos plausible entre contextos (hogar, espacio pequeño, viaje o agenda variable). La capacidad de transporte, por sí sola, no demuestra entrenamiento útil ni demanda de mercado.

Se observan cinco variables, sin asignar aún puntajes: **función física, dependencia del entorno, preparación/guardado, progresión y seguridad**.

## 3. Mapa de arquitecturas — hipótesis funcionales

| Código | Arquitectura funcional | Mecanismo y posibilidad de uso | Dependencias y riesgo principal | Fit conceptual |
|---|---|---|---|---|
| `SOL-008-A1` | Resistencia elástica portátil, con o sin anclaje | Series de resistencia por selección de banda, longitud/elongación y configuración. Un sistema sin anclaje puede reducir dependencia del entorno. | Fatiga/rotura, fijaciones, variabilidad de carga y necesidad de instrucciones. No confundir con `BASE-FIT-005/006`. | `DIRECT — CONDITIONED` |
| `SOL-008-A2` | Entrenamiento de peso corporal con soportes ligeros de suelo | Circuitos, planchas, desplazamientos o patrones de fuerza con accesorios de deslizamiento/agarre, si son necesarios. | Requiere suelo y espacio libre; sensibilidad a superficie, adherencia y nivel de usuario. Sin equipamiento no implica oportunidad de importación. | `DIRECT — CONDITIONED` |
| `SOL-008-A3` | Suspensión/anclaje transportable | Ejercicios con peso corporal mediante variación de ángulo y palanca, en lugares con puntos de fijación admisibles. | **Gate crítico de anclaje**; inspección de puerta/estructura, riesgo de caída y montaje repetido. Riesgo de duplicación con `BASE-FIT-008`. | `DIRECT — HIGH SAFETY GATE` |
| `SOL-008-A4` | Resistencia modular compacta con barra, plataforma o interfaces | Configuraciones intercambiables que permiten distintos patrones de ejercicio sin usar varias máquinas. | Más piezas y tiempos de montaje; uniones y retención bajo carga; tamaño real y complejidad. | `DIRECT — CONDITIONED` |
| `SOL-008-A5` | Acondicionamiento portátil por intervalos | Sesiones estructuradas de coordinación/cardio con implementos mínimos, por ejemplo cuerda de salto, cuando el contexto lo permite. | Altura libre, ruido, impacto, vecinos, superficie y limitaciones individuales; no apto para todos los lugares. | `DIRECT — CONTEXT-CONDITIONED` |

**Importante:** los cinco códigos `SOL` identifican **hipótesis de arquitectura**, no productos, nichos nuevos ni Product Bases. No deben trasladarse a `Productos Base` o a `Publicaciones ML` en F1.

El mapa no postula cinco mercados independientes: una misma solución puede combinar `A1` con `A4`, o `A2` con `A3`; habrá que deduplicar por función y problema primario.

## 4. Evidencia externa — alcance de lo comprobado

**Hechos respaldados por fuentes de ejercicio (NO evidencia comercial argentina):**

1. ACSM, actualización del posicionamiento de entrenamiento de fuerza 2026 (17/03/2026): la actividad con peso corporal, bandas elásticas y rutinas domiciliarias puede ser eficaz como entrenamiento de resistencia; la constancia y el esfuerzo tienen importancia central. https://acsm.org/resistance-training-guidelines-update-2026/ (consulta 2026-10-16).
2. American Council on Exercise (ACE), *The ACE Workout Builder for Resistance Band Workouts* (julio de 2025): distintas posiciones de anclaje y configuraciones permiten ejercicios sobre varios grupos musculares; recomienda inspección de bandas, conexiones y superficies. https://www.acefitness.org/continuing-education/certified/july-2025/8897/the-ace-workout-builder-for-resistance-band-workouts/ (consulta 2026-10-16).
3. NSCA, *Resistance Band Training*: la carga elástica varía con la elongación; su evaluación requiere considerar el mecanismo físico, no sólo una cifra de resistencia comercial. https://www.nsca.com/education/articles/kinetic-select/resistance-band-training/ (consulta 2026-10-16).

**Inferencias de trabajo (no medidas ni resultados de mercado):** portabilidad útil, tiempos de montaje, dependencia ambiental y barreras de adopción pueden modificar la experiencia; F2 debe investigar madurez y F3 demanda local con evidencia separada. Las fuentes anteriores **no certifican la seguridad de un SKU ni volumen de ventas, costos, proveedores o viabilidad de importación**.

## 5. Fronteras y deduplicación

- `BRAND-CAND-007`: su problema primario es fuerza accesible y compacta. Los mecanismos de bandas o suspensión pueden solaparse; `008` sólo conserva el análisis propio si la **adaptación entre contextos** es central. No se crean duplicados de `BASE-FIT-005..008`.
- `BRAND-CAND-009`: si el beneficio primario es recuperación/movilidad o estabilidad, la solución corresponde allí, no a `008`.
- `BRAND-CAND-010`: si el uso principal es microactividad dispersa durante la jornada sin sesión deliberada, queda fuera.
- Accesorios de transporte o almacenamiento que no habilitan ejercicio se excluyen del núcleo. Las aplicaciones o tecnologías son complementarias y no crean arquitectura por sí mismas.

## 6. Comparación F1 — sin score comercial

| Arquitectura | Dependencia de infraestructura | Portabilidad conceptual | Precaución antes de F2 |
|---|---|---|---|
| A1 — Elásticos | Variable según modalidad con/sin anclaje | Alta como hipótesis física | Seguridad, resistencia e instrucciones |
| A2 — Peso corporal / suelo | Suelo, espacio, privacidad | Alta, pero monetización no demostrada | Diferenciación e importabilidad reales |
| A3 — Suspensión | Punto de fijación técnicamente apto | Alta en transporte, condicionada en uso | Gate de seguridad del anclaje |
| A4 — Resistencia modular | Superficie de uso, montaje | Variable | Volumen, piezas, durabilidad |
| A5 — Intervalos/cardio portátil | Espacio vertical/superficie/entorno tolerante | Alta física, uso condicionado | Fricciones de entorno e impacto |

Estas son clasificaciones **cualitativas e interpretativas**, no observaciones de publicaciones o verificaciones de mercado.

## 7. Resultado de F1 y transición

La hipótesis de solución no se reduce a un único artículo. Hay mecanismos distintos para resolver el problema; cada uno exhibe restricciones que deberán decidir su madurez comercial/técnica en F2. No se identifica ganador ni se recomienda compra.

**F2 — Maturity (AUTO):** evaluar para las arquitecturas anteriores grado de madurez, dependencias críticas, diferenciación real y fragilidad del supuesto de portabilidad. No inferir demanda/competencia local, no abrir Alibaba, no crear Product Bases.

**Materialización F1:** `matrix-aut140-brand-cand-008-phase1-market-solution-map.xlsx` derivada de `aut139`, SHA-256 `e757eea904bb4f117d2be20d83903b3adb646ed66c1d85575205d55f2d5b39ab`. Comparación estructural: 29 hojas y 1.942 fórmulas preservadas; 3 únicas modificaciones en `Nichos!AD40:AF40`; ningún registro histórico cambiado, agregado o eliminado.

**Cierre F1 (2026-10-16):** Data Fidelity Preflight v2.4 **PASS** y Matrix Validator v0.1.0 (`full-matrix-v5 0.7.0`) **PASS**; errores=0, warnings=0, info=0, findings=[], limitations=[]. SHA-256 canónico: `e757eea904bb4f117d2be20d83903b3adb646ed66c1d85575205d55f2d5b39ab`. F1 **CLOSED** y F2 **OPENED — AUTO**, pendiente de su propia doble validación.

## 8. Estado documental

Research preparado para integración en `docs/06-research/brand-fitness/` después de validar el snapshot. Su número `SI-RESEARCH-104` no apareció ocupado en la ruta verificada de `main` el 2026-10-16, pero deberá comprobarse nuevamente antes de publicar. Checkpoint documental acumulado F0–F3; Git lo ejecuta el Founder, no el asistente.
