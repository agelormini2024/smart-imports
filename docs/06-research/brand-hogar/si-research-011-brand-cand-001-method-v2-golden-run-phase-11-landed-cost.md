---
id: si-research-011
title: BRAND-CAND-001 — Method v2 Golden Run — Fase 11 Landed Cost
description: Cierre decision-grade de la Fase 11 para BRAND-CAND-001, con escenarios comparables de costo puesto, calidad de evidencia, condiciones abiertas y gate hacia Margin + ROI.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-23
updated: 2026-09-23
tags:
  - smart-imports
  - brand-hogar
  - brand-cand-001
  - method-v2
  - golden-run
  - landed-cost
  - decision-grade
related:
  - si-research-008
  - si-research-009
  - si-research-010
  - si-roadmap-002
---

# SI-RESEARCH-011 — BRAND-CAND-001 — Method v2 Golden Run — Fase 11 Landed Cost

> La precisión del modelo debe ser proporcional a la decisión que tiene que soportar.

## 1. Objetivo

Cerrar la Fase 11 de Method v2 para `BRAND-CAND-001` con un `Landed Cost Screen` suficientemente defendible para decidir si los Productos Base activos deben pasar a Fase 12 — `Margin + ROI`.

Esta fase no busca una liquidación aduanera definitiva ni una cotización logística lista para compra. Busca reducir incertidumbre económica hasta el nivel necesario para la siguiente decisión.

```text
F11 ≠ costo definitivo de importación

F11 =
costo puesto económico decision-grade
+ supuestos explícitos
+ calidad de evidencia
+ sensibilidad suficiente
+ condiciones abiertas
```

## 2. Alcance

La Fase 11 trabaja sobre los tres Productos Base que superaron Fase 10:

| Product Base | Arquitectura | Gate F11 |
|---|---|---|
| `BASE-HOGAR-002` | Detección puntual + válvula central en línea | `PASS TO F12 — CONDITIONED` |
| `BASE-HOGAR-003` | Detección puntual + actuador retrofit | `PASS TO F12 — CONDITIONED` |
| `BASE-HOGAR-006` | Protección automática específica de artefacto | `PASS TO F12 — CONDITIONED` |

`BASE-HOGAR-004` permanece `WATCHLIST`.

`BASE-HOGAR-005` permanece `PAUSED`.

Ninguno de esos estados se modifica por conveniencia de F11.

## 3. Modelo económico

El modelo separa cuatro bloques de costo económico:

```text
A. COSTO DE ORIGEN NORMALIZADO
   producto
 + gastos de origen no incluidos por el Incoterm

B. LOGÍSTICA INTERNACIONAL
   flete internacional
 + seguro

C. COSTOS DE IMPORTACIÓN NO RECUPERABLES
   derechos
 + tasas
 + otros cargos que formen parte del costo económico real

D. NACIONALIZACIÓN Y LOGÍSTICA LOCAL
   terminal / depósito
 + despachante
 + handling
 + transporte local atribuible
 + otros gastos operativos atribuibles

ECONOMIC LANDED COST
= A + B + C + D
```

Los desembolsos fiscales recuperables se mantienen conceptualmente separados.

```text
ECONOMIC LANDED COST
≠
TOTAL CASH OUTLAY
```

Un concepto puede requerir caja al momento de importar sin constituir costo económico definitivo.

## 4. Normalización de Incoterms

F11 no compara `EXW`, `FCA` y `FOB` como si fueran equivalentes.

```text
FOB
→ usar como base sólo cuando el alcance esté confirmado

FCA
→ agregar únicamente los tramos que falten desde el lugar FCA

EXW
→ incorporar retiro, origen y exportación mediante evidencia o proxy explícito
```

Cuando el Incoterm no está confirmado, se utiliza un supuesto conservador de normalización y se registra como `PROXY`.

No se presenta un valor EXW como si fuera FOB.

## 5. Calidad de evidencia

Cada input relevante del modelo se interpreta con uno de estos estados:

```text
VERIFIED
SUPPLIER_CONFIRMED
PUBLIC_CONFIRMED
PROXY
WORKING_ASSUMPTION
```

La cifra resultante no puede interpretarse con mayor precisión que sus inputs.

> Un Landed Cost con decimales no implica precisión aduanera equivalente.

## 6. Diseño de escenarios

Para esta Golden Run se modelan dos cantidades comunes por Product Base:

```text
50 unidades
100 unidades
```

Objetivo:

- observar sensibilidad frente a gastos fijos;
- mantener escenarios comparables;
- evitar optimización prematura de una orden;
- detener la investigación cuando la conclusión ya sea suficientemente clara.

Sólo corresponde abrir nuevos escenarios si los existentes dejan una decisión materialmente ambigua.

## 7. Criterio de packing

Cuando existe caja master confirmada, el cálculo respeta unidades por caja y redondea a cajas necesarias salvo que exista packing parcial específico confirmado.

Para bundles de varios componentes se modela el sistema completo, no sólo la suma de precios unitarios.

Esta regla evita subestimar volumen o peso en tandas pequeñas.

## 8. Aduana y clasificación

F11 utiliza una clasificación aduanera de trabajo y supuestos económicos explícitos para screening.

```text
WORKING CUSTOMS CLASSIFICATION
≠
CLASIFICACIÓN ARANCELARIA VALIDADA
```

La posición NCM, intervenciones, certificaciones y costos definitivos deben ser confirmados por el profesional correspondiente antes de una decisión real de importación.

El código HS informado por un proveedor sigue siendo sólo una referencia de origen.

```text
SUPPLIER HS CODE
≠
CLASIFICACIÓN ARANCELARIA VALIDADA
```

## 9. Resultado por Product Base

### 9.1 `BASE-HOGAR-002`

Resultado económico:

- el costo puesto modelado permanece por debajo del máximo económico objetivo en ambos escenarios;
- la sensibilidad adicional no altera la lectura general;
- la incertidumbre dominante deja de ser principalmente económica.

Condiciones abiertas:

- comparabilidad exacta con uso residencial central;
- instalación hidráulica;
- diámetro, rosca y compatibilidad;
- Incoterm definitivo;
- clasificación aduanera profesional.

Gate:

```text
PASS TO F12 — CONDITIONED
```

### 9.2 `BASE-HOGAR-003`

Resultado económico:

- el costo puesto modelado queda por encima del máximo económico objetivo en ambos escenarios;
- el escenario de mayor cantidad mejora la estructura, pero no elimina la condición económica;
- F12 debe interpretar formalmente margen y ROI antes de decidir su continuidad comercial.

Condiciones abiertas:

- economía ajustada;
- dependencia de `Tuya Cloud` para la automatización crítica;
- compatibilidad mecánica;
- precio productivo actualizado;
- normalización definitiva de origen.

Gate:

```text
PASS TO F12 — CONDITIONED
```

El avance a F12 no implica que el PB haya cumplido el objetivo económico. Implica que Margin + ROI es el gate previsto para interpretar formalmente esa estructura.

### 9.3 `BASE-HOGAR-006`

Resultado económico:

- conserva holgura suficiente bajo supuestos conservadores;
- la conclusión no depende de mejorar todavía el precio de compra;
- aumentar precisión de negociación en este punto tendría bajo valor para la decisión actual.

Condiciones abiertas:

- compatibilidad eléctrica para Argentina;
- precio productivo;
- Incoterm;
- documentación técnica y regulatoria definitiva.

Gate:

```text
PASS TO F12 — CONDITIONED
```

## 10. Lectura consolidada

F11 no elimina ninguno de los tres PB activos.

La razón no es la misma en los tres casos:

```text
BASE-HOGAR-002
→ economía suficiente
→ riesgo dominante técnico / instalación / comparabilidad

BASE-HOGAR-003
→ economía ajustada
→ F12 debe interpretar margen + ROI
→ además mantiene riesgo cloud / compatibilidad

BASE-HOGAR-006
→ economía con holgura
→ riesgo dominante técnico / compatibilidad eléctrica
```

No se produce ranking ni selección final de producto en F11.

## 11. Principios observados durante la Golden Run

### 11.1 Profundidad suficiente para decidir

```text
Smart Imports no debe maximizar investigación.
Debe minimizar incertidumbre hasta el punto necesario
para tomar la siguiente decisión.
```

### 11.2 Robustez frente a proxies

Cuando un resultado permanece claramente viable bajo proxies conservadores, mejorar precisión antes del siguiente gate tiene bajo retorno.

Cuando el resultado queda cerca del límite, la calidad de evidencia y la sensibilidad ganan importancia.

### 11.3 Decision-grade antes de procurement-grade

```text
DECISION-GRADE DATASET
≠
PROCUREMENT-GRADE DATASET
```

F11 necesita el primero.

Cotización final, negociación fina, packing definitivo, muestras, contratos y liquidación profesional pertenecen a etapas posteriores.

## 12. Fricciones detectadas para retrospectiva

### 12.1 Campo legacy `Costo FOB USD`

La hoja `Simulación Margen` conserva un campo denominado `Costo FOB USD`.

En F11 algunos costos de origen son EXW o tienen Incoterm pendiente.

Por compatibilidad con el schema vigente, el campo aloja el costo de origen de referencia, pero esto no redefine el Incoterm.

```text
FIELD NAME LEGACY
≠
SEMÁNTICA COMERCIAL REAL
```

Registrar para retrospectiva y eventual `Matrix vNext`.

No modificar `full-matrix-v5 0.7.0` durante la Golden Run salvo bloqueo real.

### 12.2 Margen y ROI materializados antes de F12

El schema vigente exige consistencia cuando existen escenarios de `Simulación Margen`.

Por esa razón, `aut42` materializa los valores matemáticos de margen y ROI requeridos por la estructura.

Sin embargo:

```text
CÁLCULO MECÁNICO EN F11
≠
INTERPRETACIÓN FORMAL DE F12
```

La interpretación comercial, comparación y decisión de Margin + ROI continúan perteneciendo a F12.

## 13. Ejecución y grado de automatización

### `AUTO`

- consolidación del modelo;
- investigación pública de parámetros;
- normalización de inputs;
- cálculos;
- sensibilidades;
- materialización de la matriz;
- preparación documental.

### `COLLABORATIVE`

- revisión de criterios;
- validación local de `aut42`;
- confirmación de gates y continuidad.

### `EXTERNAL`

- no se requirió nuevo contacto externo para cerrar F11;
- las respuestas previas de proveedores se reutilizaron como evidencia cuando correspondía;
- validación aduanera profesional permanece fuera del gate actual.

Este reparto debe conservarse para la retrospectiva de la Golden Run.

## 14. Materialización en matriz

Snapshot:

```text
matrix-aut42-brand-cand-001-phase11.xlsx
```

SHA-256:

```text
6204f672b70d9e4629ee047aac31e25044b93e37037c9db98a303cc95cb6361c
```

Validación:

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

La materialización incluye:

- seis escenarios comparables de Landed Cost;
- dos cantidades por cada uno de los tres PB activos;
- fuentes y evidencia de F11;
- condiciones abiertas;
- gates hacia F12;
- campos derivados exigidos por el schema.

## 15. Confidencialidad

Este documento público conserva método, supuestos generales, resultados consolidados, gates y aprendizajes.

No publica:

- cotizaciones comerciales privadas;
- condiciones negociadas;
- datos de contacto;
- estrategia de negociación;
- detalle privado de simulaciones;
- documentación original de proveedores.

La matriz operativa sigue siendo la fuente estructurada para los datos de trabajo.

## 16. Estado de Fase 11

```text
F11 conceptual
→ COMPLETE

materialización
→ aut42

Matrix Validator
→ PASS limpio

checkpoint documental
→ SI-RESEARCH-011

gate
→ BASE-HOGAR-002: PASS TO F12 — CONDITIONED
→ BASE-HOGAR-003: PASS TO F12 — CONDITIONED
→ BASE-HOGAR-006: PASS TO F12 — CONDITIONED
```

## 17. Próximo paso

Abrir:

```text
F12 — Margin + ROI
```

Objetivo de F12:

- interpretar formalmente los márgenes y ROI ya derivados por los escenarios;
- distinguir señal económica robusta de señal ajustada;
- mantener visibles las condiciones técnicas y de evidencia;
- evitar negociación fina antes de saber qué PB justifica profundización;
- preparar el gate hacia la shortlist final sin confundir cálculo económico con decisión de compra.
