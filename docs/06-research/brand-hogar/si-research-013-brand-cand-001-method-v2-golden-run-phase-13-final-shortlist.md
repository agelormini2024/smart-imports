---
id: si-research-013
title: BRAND-CAND-001 — Method v2 Golden Run — Fase 13 Shortlist final
description: Cierre de Fase 13 con shortlist final condicionada de BRAND-CAND-001 y preparación para Portfolio Review.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-24
updated: 2026-09-24
tags:
  - smart-imports
  - brand-hogar
  - brand-candidate
  - method-v2
  - golden-run
  - shortlist-final
  - portfolio-review
related:
  - si-research-012
  - si-roadmap-002
  - brand-cand-001
---

# SI-RESEARCH-013 — BRAND-CAND-001 — Method v2 Golden Run — Fase 13

## 1. Objetivo

Documentar el cierre de `Fase 13 — Shortlist final` de la Golden Run de `BRAND-CAND-001`.

F13 responde una pregunta específica:

> ¿Qué Product Base merece sobrevivir dentro del Brand Candidate para participar posteriormente de una comparación transversal de portfolio?

F13 no selecciona todavía qué producto importar y no habilita automáticamente F14.

```text
FINALIST
≠ PRODUCT SELECTED
≠ PROCUREMENT READY
≠ PASS TO F14
```

## 2. Input de F13

Después de F12 quedaron activos:

```text
BASE-HOGAR-002 → PASS TO F13 — CONDITIONED
BASE-HOGAR-006 → PASS TO F13 — CONDITIONED
```

Estados preservados:

```text
BASE-HOGAR-003 → STOP — REOPENABLE
BASE-HOGAR-004 → WATCHLIST
BASE-HOGAR-005 → PAUSED
```

F13 no reabre Product Bases descartados o pausados para ampliar artificialmente el funnel.

## 3. Criterio de evaluación

La shortlist se construyó mediante una evaluación cualitativa estructurada, sin score agregado ni ranking automático.

Dimensiones utilizadas:

1. economía;
2. calidad de evidencia;
3. demanda / mercado;
4. diferenciación + Brand Fit;
5. complejidad operativa;
6. riesgo técnico / regulatorio;
7. adecuación a la primera etapa de Smart Imports.

Lecturas posibles por dimensión:

```text
DEFENDIBLE
CONDITIONED
BLOCKING
```

La evaluación no permite compensar matemáticamente un riesgo material con una fortaleza económica.

## 4. Estados de salida de F13

```text
FINALIST
FINALIST — CONDITIONED
HOLD
STOP
```

Para esta Golden Run, un `FINALIST` queda:

```text
ELIGIBLE FOR PORTFOLIO REVIEW
```

Esto no significa autorización para abrir F14.

## 5. BASE-HOGAR-002

Arquitectura:

> detección puntual + válvula central en línea.

### 5.1 Lectura consolidada

| Dimensión | Estado |
|---|---|
| Economía | `DEFENDIBLE` |
| Calidad de evidencia | `CONDITIONED` |
| Demanda / mercado | `DEFENDIBLE — CONDITIONED` |
| Diferenciación + Brand Fit | `DEFENDIBLE` |
| Complejidad operativa | `CONDITIONED` |
| Riesgo técnico / regulatorio | `CONDITIONED` |
| Adecuación a primera etapa | `CONDITIONED` |

La economía permanece suficientemente robusta para sostener la continuidad.

La principal incertidumbre deja de ser económica y pasa a concentrarse en compatibilidad técnica e instalación de la solución de corte central en contexto residencial argentino.

### 5.2 Main Strength

```text
economía robusta
+
problema doméstico claro
+
Brand Fit fuerte
+
capacidad de agregar valor mediante
solución, documentación, soporte e instalación
```

### 5.3 Dominant Condition

```text
compatibilidad técnica e instalación
de la solución de corte central
en contexto residencial argentino
```

### 5.4 Gate

```text
BASE-HOGAR-002
→ FINALIST — CONDITIONED
→ ELIGIBLE FOR PORTFOLIO REVIEW
```

## 6. BASE-HOGAR-006

Arquitectura:

> protección automática específica de artefacto, con foco en lavarropas.

### 6.1 Lectura consolidada

| Dimensión | Estado |
|---|---|
| Economía | `DEFENDIBLE` |
| Calidad de evidencia | `CONDITIONED` |
| Demanda / mercado | `CONDITIONED` |
| Diferenciación + Brand Fit | `DEFENDIBLE` |
| Complejidad operativa | `DEFENDIBLE — CONDITIONED` |
| Riesgo técnico / regulatorio | `CONDITIONED` |
| Adecuación a primera etapa | `DEFENDIBLE — CONDITIONED` |

La arquitectura conserva una economía robusta, una propuesta de valor localizada y una ventaja operativa relevante: no requiere cloud/app como dependencia funcional crítica.

La condición material dominante es la compatibilidad eléctrica y los requisitos regulatorios aplicables en Argentina.

### 6.2 Main Strength

```text
economía muy robusta
+
propuesta de valor simple
+
arquitectura localizada
+
ausencia de dependencia cloud/app
```

### 6.3 Dominant Condition

```text
compatibilidad eléctrica
+
requisitos regulatorios
aplicables en Argentina
```

### 6.4 Gate

```text
BASE-HOGAR-006
→ FINALIST — CONDITIONED
→ ELIGIBLE FOR PORTFOLIO REVIEW
```

## 7. Shortlist final de BRAND-CAND-001

```text
BRAND-CAND-001

FINALISTS

BASE-HOGAR-002
→ FINALIST — CONDITIONED
→ ELIGIBLE FOR PORTFOLIO REVIEW

BASE-HOGAR-006
→ FINALIST — CONDITIONED
→ ELIGIBLE FOR PORTFOLIO REVIEW
```

No se define un ganador interno.

Los dos PB sobreviven por perfiles diferentes y conservan condiciones diferentes.

```text
FINALIST WITHIN CANDIDATE
≠
BEST PRODUCT IN PORTFOLIO
```

## 8. Funnel consolidado

```text
F6
5 Candidate Product Bases

↓ F7

3 ACTIVE
1 WATCHLIST
1 PAUSED

↓ F8–F11

3 Product Bases con evaluación económica completa

↓ F12

BASE-HOGAR-002 → PASS F13
BASE-HOGAR-003 → STOP — REOPENABLE
BASE-HOGAR-006 → PASS F13

↓ F13

BASE-HOGAR-002 → FINALIST — CONDITIONED
BASE-HOGAR-006 → FINALIST — CONDITIONED

↓
FREEZE
```

## 9. Estado posterior a F13

`BRAND-CAND-001` queda:

```text
METHOD V2 STATUS
→ PHASE 13 CLOSED

PORTFOLIO STATUS
→ PORTFOLIO REVIEW READY

FINALISTS
→ BASE-HOGAR-002
→ BASE-HOGAR-006

REAL VALIDATION STATUS
→ NOT OPENED
```

F14 no se abre en este punto.

## 10. Gate F13 → F14 observado durante la Golden Run

La ejecución mostró que no conviene profundizar automáticamente cada Brand Candidate después de F13.

La secuencia operativa propuesta para evaluación posterior es:

```text
todos los candidatos completan F13
        ↓
comparación transversal de finalistas
        ↓
revisión externa previa
        ↓
selección del producto o productos
        ↓
F14 — Real Validation
```

La revisión externa deberá incluir especialmente la opinión de despachante y, cuando corresponda, validación regulatoria/técnica profesional.

Este flujo se registra como `GOLDEN RUN LEARNING`.

No modifica todavía la definición formal de Method v2.

## 11. External Review Data — preparación

F13 deja identificadas las preguntas que deberán viajar a la futura revisión externa.

### BASE-HOGAR-002

- clasificación aduanera probable;
- intervenciones aplicables;
- certificaciones;
- requisitos eléctricos si correspondieran;
- documentación hidráulica / técnica;
- implicancias de instalación;
- red flags para una primera importación.

### BASE-HOGAR-006

- clasificación aduanera probable;
- intervenciones aplicables;
- seguridad / certificación eléctrica;
- compatibilidad `220–240 V / 50 Hz`;
- requisitos de enchufe y configuración;
- rotulado;
- documentación técnica;
- red flags para una primera importación.

La futura ficha para despachante deberá reunir además producto representativo, uso, imágenes/ficha técnica, materiales, alimentación, presencia de batería o wireless, dimensiones/peso, cantidad tentativa, valor aproximado y documentación disponible.

## 12. Principio de adecuación a primera etapa

F13 hizo explícita una distinción observada durante la Golden Run:

```text
BUENA OPORTUNIDAD COMERCIAL
≠
BUEN PRIMER PRODUCTO PARA SMART IMPORTS
```

La primera etapa debe considerar no sólo margen, sino también complejidad de importación, regulación, instalación, compatibilidad, postventa y responsabilidad técnica.

Este criterio permanece como aprendizaje emergente hasta la retrospectiva.

## 13. Materialización en matriz

F13 fue materializada en:

```text
matrix-aut44-brand-cand-001-phase13-corrected.xlsx
```

Schema:

```text
full-matrix-v5 0.7.0
```

La matriz preserva:

- los dos finalistas condicionados;
- los estados de `BASE-HOGAR-003`, `004` y `005`;
- el estado `PORTFOLIO REVIEW READY`;
- la indicación explícita de que F14 no fue abierto;
- Main Strength y Dominant Condition;
- necesidades de revisión externa.

No se agregaron nuevas simulaciones económicas ni se reabrieron F9–F12.

## 14. Fricción de schema detectada

La columna legacy `Resumen Margen.Etapa Análisis` no admite un valor específico para `SHORTLIST_FINAL`.

El vocabulario permitido por `full-matrix-v5 0.7.0` obliga a utilizar:

```text
SHORTLIST_PRE_SCREENING
```

como valor de compatibilidad en el registro F13.

Esta decisión:

```text
NO redefine F13
NO reabre el pre-screening
NO modifica Method v2
```

Es una fricción de representación del schema vigente y debe registrarse para la retrospectiva / eventual Matrix vNext.

No se modifica el Validator durante la Golden Run.

## 15. Validación técnica

Resultado:

```text
Matrix Validator: 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

Snapshot:

```text
matrix-aut44-brand-cand-001-phase13-corrected.xlsx
```

SHA-256:

```text
37b2b37c5c61355efec271b7ecb49df74c2264e2f721830a1c2478858a850f56
```

## 16. Grado de automatización

### AUTO

- consolidación del criterio F13;
- evaluación estructurada;
- preparación de shortlist;
- materialización en matriz;
- validación estructural;
- preparación documental.

### COLLABORATIVE

- interpretación de adecuación a primera etapa;
- decisión de preservar más de un finalista;
- definición del futuro gate de portfolio;
- criterio de consulta al despachante.

### EXTERNAL

Queda pendiente para una etapa posterior:

- despachante;
- validaciones regulatorias;
- confirmaciones técnicas críticas;
- muestras;
- negociación fina;
- decisión de capital.

## 17. Confidencialidad

Este documento conserva únicamente conclusiones decision-grade y estado metodológico.

No publica:

- cotizaciones privadas completas;
- objetivos de negociación;
- contactos;
- documentación privada de proveedores;
- simulaciones comerciales sensibles.

La matriz continúa siendo el soporte operativo privado.

## 18. Cierre de F13

Con la materialización de `aut44`, su validación limpia y este checkpoint documental:

```text
F13 — SHORTLIST FINAL
→ CLOSED

BRAND-CAND-001
→ PORTFOLIO REVIEW READY

BASE-HOGAR-002
→ FINALIST — CONDITIONED

BASE-HOGAR-006
→ FINALIST — CONDITIONED

F14
→ NOT OPENED
```

## 19. Próxima acción

```text
FREEZE BRAND-CAND-001
```

Continuar los Brand Candidates restantes hasta F13.

Cuando el conjunto relevante de candidatos tenga F13 cerrada:

```text
Portfolio Review
→ fichas de finalistas
→ revisión con despachante
→ selección para profundización
→ decisión de apertura de F14
```

Principio vigente:

> Profundidad suficiente para decidir; no profundidad máxima posible.
