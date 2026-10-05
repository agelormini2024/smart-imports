---
id: brand-fitness-pre-screening-architecture-v0.2
title: Marca Fitness — Arquitectura pre-screening v0.2
description: Baseline conceptual congelada para iniciar Brand Candidate Screening con territorio, misiones, contexto transversal y candidatos depurados.
version: 0.2.0
status: pre-screening-ready
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-05
updated: 2026-10-05
brand: brand-fitness
tags:
  - brand-fitness
  - pre-screening
  - territory
  - missions
  - candidates
related:
  - si-brand-001
  - si-brand-002
  - si-brand-003
---

# Marca Fitness — Arquitectura pre-screening v0.2

## 1. Propósito

Congelar una baseline conceptual de Marca Fitness antes de abrir el primer `Brand Candidate Screening`.

Esta baseline no constituye:

- validación de demanda;
- análisis de competencia;
- selección de Product Bases;
- evaluación de origen;
- estimación de costos;
- decisión de importación;
- claim científico, médico o terapéutico.

Es una definición de **dónde queremos jugar** para poder aplicar posteriormente `SI-BRAND-002`.

## 2. Estado formal

```text
Brand: Marca Fitness
Architecture baseline: v0.2
Territory: FROZEN FOR SCREENING
Missions: FROZEN FOR SCREENING
Active pre-screening candidates: 4
Brand Candidate Screening: READY / NOT STARTED
Method v2: NOT OPENED
Product Bases: NOT DEFINED
Purchase Decision: NONE
```

`FROZEN FOR SCREENING` significa baseline estable para comparar candidatos. No implica que el territorio sea inmutable para siempre.

## 3. Territorio v0.2

> **Ayudar a personas a conservar, recuperar y desarrollar capacidad física en una vida cotidiana marcada por sedentarismo, poco tiempo y espacios limitados, mediante soluciones simples, compactas, comprensibles y sostenibles en el tiempo.**

El territorio no se define por edad.

`+50` se conserva como un contexto/segmento potencialmente relevante para explorar problemas de fuerza, movilidad, estabilidad o retorno a la actividad, pero la marca no se restringe a ese grupo.

También pueden pertenecer al territorio personas más jóvenes con:

- trabajo de oficina;
- desarrollo de software;
- home office;
- estudio prolongado;
- viajes frecuentes;
- baja actividad cotidiana;
- largos períodos sin entrenamiento.

Regla:

```text
EDAD
≠
TERRITORIO
```

La edad puede modificar intensidad, necesidades o lenguaje del problema; no define por sí sola Brand Fit.

## 4. Contexto transversal

```text
VIDA SEDENTARIA / BAJA ACTIVIDAD COTIDIANA
```

Este contexto puede atravesar múltiples misiones:

```text
sedentarismo
├── menor estímulo de fuerza
├── pocas oportunidades de movimiento
├── rigidez / poca variedad de posiciones
├── pérdida o baja de estabilidad y capacidad
└── dificultad para sostener hábitos físicos
```

La hipótesis se utiliza como marco de problemas de usuario, no como afirmación científica ni diagnóstica.

## 5. Misiones v0.2

### Misión 1 — Construir y conservar fuerza útil

Ayudar a desarrollar, recuperar o conservar fuerza aplicable al entrenamiento general y a la vida cotidiana sin depender necesariamente de un gimnasio completo.

### Misión 2 — Incorporar movimiento y entrenamiento en la vida cotidiana

Reducir la fricción para moverse o entrenar cuando existen restricciones de tiempo, espacio, lugar, trabajo, viaje o rutina.

### Misión 3 — Conservar y recuperar movilidad, estabilidad y capacidad física

Facilitar trabajo progresivo sobre movilidad, estabilidad, movimiento y retorno a la actividad sin convertir la marca en una propuesta médica o terapéutica.

### Misión 4 — Entender el progreso y sostener la constancia

Hacer visible el progreso, facilitar feedback y reducir la fricción que lleva al abandono.

Esta misión puede expresarse como una capacidad transversal y no obliga a crear un Brand Candidate tecnológico independiente.

## 6. Arquitectura de candidatos depurada

### Activos para screening

```text
FIT-CAND-001 — Fuerza accesible y compacta
FIT-CAND-002 — Entrenamiento flexible y portátil
FIT-CAND-005 — Movilidad, estabilidad y conservación/recuperación de capacidad física
FIT-CAND-007 — Movimiento integrado a la jornada sedentaria
```

### Históricos / reclasificados

```text
FIT-CAND-003 — MERGED INTO FIT-CAND-005
FIT-CAND-004 — MERGED INTO FIT-CAND-001
FIT-CAND-006 — RECLASSIFIED AS TRANSVERSAL CAPABILITY
```

Los IDs históricos no se eliminan ni se reutilizan.

## 7. Decisión — FIT-CAND-004

`FIT-CAND-004 — Calistenia y peso corporal` deja de ser candidato independiente.

Razón:

El problema principal no es distinto de `FIT-CAND-001`; la diferencia está principalmente en la arquitectura de solución.

```text
PROBLEMA
Construir / conservar fuerza de forma accesible

ARQUITECTURAS POSIBLES
├── carga externa ajustable
├── resistencia elástica
├── peso corporal / calistenia
└── sistemas híbridos
```

Decisión:

```text
FIT-CAND-004
→ MERGED INTO FIT-CAND-001
```

Calistenia / peso corporal permanece disponible como arquitectura de solución a investigar posteriormente.

## 8. Decisión — FIT-CAND-003

`FIT-CAND-003 — Recuperación y movilidad` deja de ser candidato independiente.

Razón:

La recuperación posterior a la actividad es un subproblema defendible, pero el candidato más amplio y coherente con el territorio actual es `FIT-CAND-005`.

```text
FIT-CAND-005
├── movilidad
├── estabilidad
├── retorno progresivo
├── conservación de capacidad
└── recuperación / automanejo postactividad, cuando corresponda
```

Decisión:

```text
FIT-CAND-003
→ MERGED INTO FIT-CAND-005
```

La absorción no autoriza claims médicos o terapéuticos.

## 9. Decisión — FIT-CAND-006

`FIT-CAND-006 — Entrenamiento medible / fitness inteligente` deja de ser candidato independiente.

Razón:

Medición, feedback y constancia pueden acompañar múltiples problemas:

```text
FIT-CAND-001 + progresión
FIT-CAND-002 + frecuencia / sesiones
FIT-CAND-005 + evolución / constancia
FIT-CAND-007 + pausas / movimiento / hábito
```

La tecnología es un medio, no el problema.

Decisión:

```text
FIT-CAND-006
→ RECLASSIFIED AS TRANSVERSAL CAPABILITY
→ Medición + feedback + constancia
```

No se crea todavía un nuevo ID de capacidad. Se hará sólo si existe necesidad operativa real.

Si en el futuro aparece un problema autónomo cuya razón principal sea medir capacidad/progreso, puede reingresar mediante `SI-BRAND-003` como nueva oportunidad.

## 10. FIT-CAND-001 — Fuerza accesible y compacta

Problema núcleo:

> **Construir o conservar fuerza sin depender de un gimnasio completo, mucho espacio ni una colección extensa de equipamiento.**

Misión primaria:

```text
Construir y conservar fuerza útil
```

Posibles arquitecturas futuras, todavía no Product Bases:

- carga externa ajustable;
- resistencia elástica;
- peso corporal / calistenia;
- sistemas híbridos;
- equipamiento plegable o modular.

Estado:

```text
ACTIVE — PRE-SCREENING
```

## 11. FIT-CAND-002 — Entrenamiento flexible y portátil

Problema núcleo:

> **Mantener un entrenamiento útil aunque cambien el lugar, el tiempo disponible o el contexto cotidiano.**

Misión primaria:

```text
Incorporar movimiento y entrenamiento en la vida cotidiana
```

Estado:

```text
ACTIVE — PRE-SCREENING
```

## 12. FIT-CAND-005 — Movilidad, estabilidad y capacidad física

Problema núcleo:

> **Conservar o recuperar movilidad, estabilidad y capacidad física de forma progresiva y comprensible.**

Misión primaria:

```text
Conservar y recuperar movilidad, estabilidad y capacidad física
```

Incluye como subproblemas potenciales:

- rigidez;
- poca variedad de movimiento;
- retorno progresivo a la actividad;
- estabilidad;
- recuperación postactividad cuando sea coherente.

No implica por sí mismo:

- tratar lesiones;
- curar dolor;
- reducir inflamación;
- reemplazar atención profesional.

Estado:

```text
ACTIVE — PRE-SCREENING
```

## 13. FIT-CAND-007 — Movimiento integrado a la jornada sedentaria

Problema núcleo:

> **Pasar demasiadas horas con muy baja actividad y necesitar incorporar movimiento frecuente de forma simple, breve y compatible con la jornada cotidiana.**

Misión primaria:

```text
Incorporar movimiento y entrenamiento en la vida cotidiana
```

Criterios conceptuales fuertes para futuras soluciones:

- uso rápido;
- poco espacio;
- mínimo montaje;
- bajo ruido;
- fácil guardado;
- compatible con ropa cotidiana;
- sesiones breves;
- posibilidad de repetición varias veces al día;
- baja fricción mental.

Regla orientativa:

> **La solución debe ser más fácil de usar que de postergar.**

Estado:

```text
ACTIVE — PRE-SCREENING
```

## 14. Capacidad transversal — Medición, feedback y constancia

Esta capacidad puede aplicarse a cualquiera de los candidatos activos.

```text
fuerza
movimiento cotidiano
movilidad / estabilidad
entrenamiento flexible
        ↓
medición / feedback / constancia
```

No debe premiarse tecnología por sí misma.

```text
SMART
≠
BRAND FIT
```

## 15. Reglas de integridad

```text
PROBLEMA ≠ PRODUCTO
ARQUITECTURA DE SOLUCIÓN ≠ BRAND CANDIDATE
TECNOLOGÍA ≠ PROBLEMA
EDAD ≠ TERRITORIO
CLAIM MÉDICO ≠ PROPUESTA FITNESS POR DEFECTO
```

`SI-BRAND-003` continúa habilitando descubrimiento descendente y ascendente.

Un producto observado puede ingresar como oportunidad, pero no crea automáticamente Product Base, Brand Candidate ni Method v2.

## 16. Próxima acción

Abrir, de a uno, el `Brand Candidate Screening` definido en `SI-BRAND-002`.

Orden inicial:

```text
1. FIT-CAND-001
2. FIT-CAND-002
3. FIT-CAND-005
4. FIT-CAND-007
```

Cada screening deberá producir:

```text
Candidate ID
Candidate
Brand
Mission
Problem
Brand-fit rationale
Claims / assumptions to validate
Territory risks
Decision
Decision rationale
Date
```

Estados permitidos:

```text
PASS TO METHOD V2
HOLD — BRAND FIT UNCLEAR
OUTSIDE BRAND TERRITORY
```

No evaluar todavía:

- demanda;
- competencia;
- origen;
- headroom;
- costo puesto en destino;
- margen;
- ROI.

Esos temas pertenecen a Method v2.
