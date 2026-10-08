---
id: si-research-072
title: BRAND-CAND-010 — Method v2 Agile — Fase 1 — Market / Solution Map
description: Mapa de arquitecturas de solución para movimiento integrado a la jornada sedentaria dentro de Marca Fitness.
version: 0.2.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-07
updated: 2026-10-08
brand: brand-fitness
brand_candidate: brand-cand-010
method: method-v2-agile
phase: F1
mode: AUTO
---

# SI-RESEARCH-072 — BRAND-CAND-010 — Fase 1 — Market / Solution Map

## 1. Estado

```text
F0 CLOSED — aut105 PASS
F1 CLOSED — aut106 PASS
```

## 2. Boundary

El mapa parte del job:

> Incorporar movimiento físico real dentro de una jornada predominantemente sedentaria, con baja fricción y sin exigir por defecto una sesión formal de entrenamiento.

Regla de frontera:

```text
MOVIMIENTO DISTRIBUIDO DURANTE LA JORNADA
→ BRAND-CAND-010

SESIÓN / RUTINA DE EJERCICIO
→ BRAND-CAND-008
```

## 3. Arquitecturas / familias de solución

```text
A1 — walking pad / under-desk treadmill
A2 — elíptica sentada bajo escritorio
A3 — ciclo / pedalera sentada bajo escritorio
A4 — tabla de movimiento / balance para standing desk
A5 — footrest basculante / rocker activo [ADJACENT / SUPPORT]
A6 — mini stepper [BOUNDARY / EXCLUDE FROM CORE]
```

### A1 — Walking pad / under-desk treadmill
Marcha a baja velocidad sobre cinta motorizada, normalmente combinada con escritorio de pie.

**Fit:** CORE — STRONG.

### A2 — Elíptica sentada bajo escritorio
Movimiento elíptico de miembros inferiores desde posición sentada.

**Fit:** CORE — STRONG.

### A3 — Ciclo / pedalera sentada bajo escritorio
Pedaleo circular con resistencia desde una silla.

**Fit:** CORE — STRONG.

### A4 — Tabla de movimiento / balance para standing desk
Plataforma que induce micro-movimientos y cambios de apoyo durante trabajo de pie.

**Fit:** CORE — CONDITIONED.

### A5 — Footrest basculante / rocker activo
Movimiento de tobillo/pierna desde sedestación.

**Fit:** ADJACENT / SUPPORT.

La frontera con ergonomía/confort es alta.

### A6 — Mini stepper
Stepping hidráulico de pie.

**Fit:** BOUNDARY / EXCLUDE FROM CORE.

El uso dominante se aproxima más a una sesión de ejercicio que a movimiento integrado a la tarea.

## 4. Ejes comparativos para las fases siguientes

- mecanismo de movimiento;
- postura de uso;
- simultaneidad real con trabajo;
- ruido / distracción;
- espacio y guardado;
- dependencia de standing desk;
- carga eléctrica o mecánica;
- seguridad;
- mantenimiento;
- facilidad de incorporación recurrente.

## 5. Evidencia mínima suficiente

La categoría de under-desk treadmill está comercialmente establecida con múltiples fabricantes y modelos actuales. Cubii mantiene una línea específica de elípticas sentadas diseñadas para caber bajo escritorio. FluidStance mantiene una línea específica de balance boards para standing desk.

Referencias públicas:
- https://www.tomsguide.com/best-picks/best-under-desk-treadmills
- https://help.cubii.com/hc/en-us/articles/360036305813-Will-Cubii-ellipticals-fit-under-my-desk
- https://fluidstance.com/pages/standing-desk-balance-boards

## 6. Regla metodológica

```text
MISMO JOB ≠ MISMA ARQUITECTURA
ARQUITECTURA / FAMILIA ≠ PRODUCT BASE
```

En F1 todavía no se crean Product Bases.

## 7. Gate

```text
PASS TO F2 — MATURITY
```

Cierre confirmado:

```text
aut106 → Matrix Validator PASS
→ F1 CLOSED
→ F2 — Maturity completada posteriormente
```
