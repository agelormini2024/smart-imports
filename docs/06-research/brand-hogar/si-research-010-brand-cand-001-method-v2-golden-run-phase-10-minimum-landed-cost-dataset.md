---
id: si-research-010
title: BRAND-CAND-001 — Method v2 Golden Run — Fase 10 Minimum Landed Cost Dataset
description: Cierre de Fase 10 con dataset mínimo suficiente para abrir Landed Cost en BRAND-CAND-001.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-23
updated: 2026-09-23
tags:
  - smart-imports
  - brand-hogar
  - brand-candidate
  - method-v2
  - golden-run
  - minimum-landed-cost-dataset
related:
  - si-research-007
  - si-research-008
  - si-research-009
  - si-roadmap-002
  - brand-cand-001
---

# SI-RESEARCH-010 — BRAND-CAND-001 — Method v2 Golden Run — Fase 10

## 1. Objetivo

Documentar el cierre de `Fase 10 — Minimum Landed Cost Dataset` (dataset mínimo para costo puesto) de la Golden Run de `BRAND-CAND-001`.

La pregunta de la fase es:

> ¿Existe información suficiente y suficientemente confiable para modelar en Fase 11 un Landed Cost (costo puesto) sin inventar los principales componentes del costo ni la configuración importada?

Fase 10 no calcula todavía el costo puesto.

```text
F10 = reunir datos suficientes para modelar
F11 = calcular Landed Cost (costo puesto)
```

## 2. Baseline de ejecución

```text
Input: BRAND-CAND-001
Fases previas: 0–9 cerradas
Snapshot de entrada: matrix-aut40-brand-cand-001-phase9.xlsx
Snapshot de cierre F10: matrix-aut41-brand-cand-001-phase10.xlsx
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
SHA-256: 73a58052336456ddf09390db8fd6874f5e3e43c9cc9a68b1d139d19d4659d649
```

`aut32` continúa como baseline técnica de release. `aut41` pasa a ser el snapshot comercial vigente de la Golden Run.

## 3. Principio de suficiencia

La Golden Run permitió distinguir dos niveles de información:

```text
DECISION-GRADE DATASET
(dataset suficiente para decidir)

≠

PROCUREMENT-GRADE DATASET
(dataset suficiente para comprar / negociar)
```

En esta etapa Smart Imports necesita el primero.

No se exige cerrar negociación, packaging final, precio definitivo, muestra, certificaciones completas o condiciones finales de compra antes de decidir si un Product Base merece seguir avanzando.

El criterio es `Minimum Sufficient Evidence` (evidencia mínima suficiente):

> Obtener la mínima información confiable que pueda sostener o cambiar la siguiente decisión.

## 4. Calidad de evidencia

Los datos utilizados en F10 se clasifican según su fortaleza:

| Estado | Significado |
|---|---|
| `VERIFIED` | Respaldado por documento formal del proveedor. |
| `SUPPLIER_CONFIRMED` | Confirmado directamente por el proveedor, todavía sin documento formal suficiente. |
| `PUBLIC_CONFIRMED` | Disponible en publicación o documentación pública identificable. |
| `PROXY` | Aproximación conservadora y explícita usada cuando no cambia la naturaleza del Product Base. |
| `MISSING` | No disponible y todavía relevante. |

F11 debe conservar esta calidad de evidencia en cada supuesto.

## 5. Contrato mínimo de datos

Para abrir Landed Cost (costo puesto), el Product Base debe tener información defendible en cuatro bloques:

```text
1. WHAT ARE WE IMPORTING?
   ¿Qué configuración exacta estamos modelando?

2. WHAT DOES IT COST AT ORIGIN?
   ¿Cuál es la referencia de costo y bajo qué base comercial?

3. HOW IS IT PACKED?
   ¿Qué volumen y peso debemos transportar?

4. HOW STRONG IS THE EVIDENCE?
   ¿Cuál es la fuente y calidad de cada dato?
```

Campos típicos:

- configuración exacta;
- componentes incluidos;
- MOQ (cantidad mínima de pedido) o escala aplicable;
- precio de origen de referencia;
- Incoterm (condición internacional de compraventa), cuando esté disponible;
- unidades por caja;
- dimensiones / CBM (metros cúbicos);
- Gross Weight (peso bruto);
- Net Weight (peso neto), cuando aporte al análisis;
- documentación técnica suficiente;
- fuente y calidad de evidencia.

El HS Code (código arancelario sugerido por proveedor) puede servir como referencia, pero no equivale a clasificación aduanera validada en Argentina.

## 6. Resultado por Product Base

### 6.1 BASE-HOGAR-002 — sensores + válvula central en línea

Estado:

```text
PASS TO F11 — WITH PUBLIC DATA
COMPARABILITY CONDITION
```

F10 dispone de una configuración comparable pública, datos logísticos suficientes y referencias de origen para construir un escenario conservador.

Permanece abierta una condición material:

- la equivalencia exacta con una instalación central residencial debe mantenerse explícita;
- las condiciones de origen no documentadas deberán normalizarse mediante un supuesto conservador en F11.

La falta de respuesta de un proveedor no elimina el Product Base ni bloquea el avance cuando existe evidencia pública suficiente para un escenario de decisión.

### 6.2 BASE-HOGAR-003 — sensores + actuador retrofit

Estado:

```text
PASS TO F11 — WITH PUBLIC PRICE
```

La configuración funcional quedó suficientemente definida:

```text
1 × actuador retrofit
3 × sensores de fuga
gateway/hub → no requerido para la configuración evaluada
```

La respuesta directa del proveedor permitió mejorar la calidad de evidencia sobre configuración, compatibilidad y logística.

Permanece como riesgo técnico:

```text
AUTOMATIC SHUTOFF OFFLINE
→ NOT DEMONSTRATED

ARCHITECTURE
→ CLOUD-DEPENDENT
```

La dependencia cloud no impide calcular Landed Cost, pero debe permanecer como condición explícita de evaluación del producto.

### 6.3 BASE-HOGAR-006 — protección específica de artefacto

Estado:

```text
PASS TO F11 — WITH PROXY
```

La variante priorizada continúa siendo:

```text
APPLIANCE-SPECIFIC
(específica para artefacto)
```

Existe suficiente evidencia pública de configuración y logística para construir un escenario conservador.

El costo de origen disponible no representa una condición productiva final y debe usarse únicamente como proxy conservador en F11.

Queda además abierta la compatibilidad eléctrica aplicable a Argentina. Este punto no impide el cálculo económico de screening, pero sí deberá resolverse antes de considerar el producto procurement-ready (listo para compra).

## 7. Resultado consolidado

```text
BASE-HOGAR-002
→ PASS TO F11 — WITH PUBLIC DATA / COMPARABILITY CONDITION

BASE-HOGAR-003
→ PASS TO F11 — WITH PUBLIC PRICE
→ technical condition: cloud dependency

BASE-HOGAR-006
→ PASS TO F11 — WITH PROXY
→ technical condition: electrical compatibility unresolved

BASE-HOGAR-004
→ WATCHLIST

BASE-HOGAR-005
→ PAUSED
```

Los tres PB activos pueden abrir `Fase 11 — Landed Cost`.

Esto no selecciona proveedor, no constituye decisión de compra y no implica que el dataset sea suficiente para una operación real de importación.

## 8. Protocolo de proveedor observado

La Golden Run produjo un aprendizaje operativo importante:

```text
SUPPLIER RESPONSE
≠
PHASE PROGRESS
```

El contacto con proveedores debe enriquecer el dataset, no controlar el camino crítico del proyecto.

Cuando falta un dato:

```text
SUPPLIER / DOCUMENT
→ PUBLIC EVIDENCE
→ CONSERVATIVE PROXY
→ HOLD sólo si el faltante cambia materialmente la decisión
```

No se continuará persiguiendo proveedores ni iniciando negociación fina únicamente para mejorar un dataset que ya es suficiente para decisión.

## 9. Clases de ejecución observadas

F10 permite distinguir claramente:

| Clase | Ejemplos en F10 |
|---|---|
| `AUTO` (automática) | Gap analysis, búsqueda pública, normalización, cálculos logísticos, consolidación y matriz. |
| `COLLABORATIVE` (colaborativa) | Revisión de respuestas/imágenes y envío coordinado de mensajes. |
| `EXTERNAL` (externa) | Respuestas del proveedor, documentación privada y condiciones comerciales directas. |

Esta clasificación se conserva como aprendizaje de Golden Run para la retrospectiva final.

## 10. Criterio estratégico emergente

Para la etapa inicial de Smart Imports conviene priorizar productos operativamente simples:

```text
EARLY-STAGE PRODUCT SIMPLICITY
(simplicidad de producto para etapa inicial)
```

Favorecer productos con menor complejidad de:

- importación;
- regulación;
- logística;
- instalación;
- compatibilidad;
- seguridad;
- soporte posventa.

Este criterio queda registrado para la retrospectiva. No modifica todavía formalmente Method v2.

## 11. Confidencialidad

El repositorio público conserva:

- método;
- calidad de evidencia;
- decisiones de gate;
- riesgos;
- aprendizajes;
- próxima acción.

Los precios exactos, cotizaciones, condiciones comerciales particulares, cantidades negociadas, simulaciones y documentos privados permanecen en la matriz operativa y registros privados.

## 12. Gate siguiente

Fase 10 queda cerrada con `aut41` validada.

Siguiente gate:

```text
F11 — Landed Cost
(costo puesto)
```

F11 deberá:

- normalizar EXW / FCA / FOB cuando corresponda;
- utilizar escenarios conservadores;
- identificar claramente datos confirmados, públicos y proxy;
- mantener Economic Landed Cost (costo puesto económico) separado de Total Cash Outlay (desembolso total de caja);
- evitar negociación fina antes de que la decisión comercial la justifique.

## 13. Estado final del checkpoint

```text
Fase 10 conceptual → COMPLETADA
Materialización → aut41
Matrix Validator → PASS limpio
Checkpoint documental → SI-RESEARCH-010
Próximo gate → Fase 11
```

## 14. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-23 | Cierre documental de Fase 10 — Minimum Landed Cost Dataset; aut41 PASS y siguiente gate Fase 11 — Landed Cost. |
