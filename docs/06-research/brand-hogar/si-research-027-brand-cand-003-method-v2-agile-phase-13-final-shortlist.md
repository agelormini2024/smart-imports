---
id: si-research-027
title: BRAND-CAND-003 — Method v2 Agile — F13 Shortlist final
description: Cierre de Fase 13 con finalista condicionado de BRAND-CAND-003 y preparación para Portfolio Review.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-25
updated: 2026-09-25
phase: business-intelligence
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-003
  - indoor-air
  - phase-13
  - portfolio-review
related:
  - si-research-026
  - si-roadmap-002
  - brand-cand-003
---

# SI-RESEARCH-027 — BRAND-CAND-003 — Method v2 Agile — Fase 13

## 1. Objetivo

Documentar el cierre de `Fase 13 — Shortlist final` de `BRAND-CAND-003`.

F13 responde:

> ¿Qué Product Base merece sobrevivir dentro del Brand Candidate para participar posteriormente de una comparación transversal de portfolio?

```text
FINALIST
≠ PRODUCT SELECTED
≠ PROCUREMENT READY
≠ PASS TO F14
```

## 2. Input de F13

Después de F12 quedó activo:

```text
BASE-HOGAR-010
→ PASS TO F13 — CONDITIONED
```

Estados preservados:

```text
BASE-HOGAR-009 → STOP — REOPENABLE
BASE-HOGAR-011 → STOP — REOPENABLE
```

F13 no reabre candidatos sólo para ampliar el funnel.

## 3. Criterio de evaluación

Evaluación cualitativa estructurada, sin score agregado ni ranking automático.

Dimensiones:

1. economía;
2. calidad de evidencia;
3. demanda / mercado;
4. diferenciación + Brand Fit;
5. complejidad operativa;
6. riesgo técnico / regulatorio;
7. adecuación a la primera etapa de Smart Imports.

Una fortaleza económica no compensa un bloqueo material.

## 4. BASE-HOGAR-010 — lectura consolidada

Arquitectura:

> purificador portátil con filtración mecánica de partículas y una etapa de carbón activado/sorbente suficientemente material para sostener una propuesta explícita sobre determinados olores, gases o COV.

Lectura:

| Dimensión | Estado |
|---|---|
| Economía | `DEFENDIBLE` |
| Calidad de evidencia | `CONDITIONED` |
| Demanda / mercado | `DEFENDIBLE — CONDITIONED` |
| Diferenciación + Brand Fit | `DEFENDIBLE` |
| Complejidad operativa | `DEFENDIBLE — CONDITIONED` |
| Riesgo técnico / regulatorio | `CONDITIONED` |
| Adecuación a primera etapa | `DEFENDIBLE — CONDITIONED` |

### Main Strength

```text
economía suficiente
+
problema doméstico comprensible
+
Brand Fit fuerte
+
propuesta sin dependencia obligatoria de tecnología activa
+
posibilidad de valor mediante sizing, filtros/repuestos,
claims transparentes, documentación y soporte
```

### Dominant Condition

```text
materialidad / capacidad real del sorbente
+
claims gas-phase defendibles
```

No alcanza con una capa nominal de carbón.

## 5. Gate

```text
BASE-HOGAR-010
→ FINALIST — CONDITIONED
→ ELIGIBLE FOR PORTFOLIO REVIEW
```

## 6. Product Bases no finalistas

### BASE-HOGAR-009

```text
STOP — REOPENABLE
```

Motivo dominante: estructura económica desfavorable bajo el modo logístico evaluado, con peso volumétrico material.

### BASE-HOGAR-011

```text
STOP — REOPENABLE
```

Motivos: economía fuertemente desfavorable + safety/ozone/subproductos/claims.

Una mejora económica sola no habilita la arquitectura.

## 7. Estado posterior a F13

```text
BRAND-CAND-003

METHOD V2 STATUS
→ PHASE 13 CLOSED

PORTFOLIO STATUS
→ PORTFOLIO REVIEW READY

FINALIST
→ BASE-HOGAR-010
→ FINALIST — CONDITIONED

REAL VALIDATION STATUS
→ NOT OPENED
```

F14 no se abre.

## 8. External Review Data — preparación

Para `BASE-HOGAR-010` la futura revisión deberá cubrir:

- clasificación arancelaria probable;
- intervenciones aplicables;
- certificaciones;
- compatibilidad `220–240 V / 50 Hz`;
- enchufe/configuración;
- rotulado;
- CADR / sizing por configuración exacta;
- masa/capacidad/configuración del sorbente;
- método de prueba y contaminantes objetivo;
- filtros de reposición, vida útil y costo;
- red flags para una primera importación.

## 9. Principio de adecuación a primera etapa

```text
BUENA OPORTUNIDAD COMERCIAL
≠ BUEN PRIMER PRODUCTO PARA SMART IMPORTS
```

La primera etapa debe considerar margen, volumen logístico, regulación, compatibilidad, postventa y responsabilidad técnica.

## 10. Materialización en matriz

```text
matrix-aut58-brand-cand-003-phase13.xlsx
```

Schema:

```text
full-matrix-v5 0.7.0
```

La matriz preserva:

- `BASE-HOGAR-010` como finalista condicionado;
- `BASE-HOGAR-009` y `011` como `STOP — REOPENABLE`;
- `PORTFOLIO REVIEW READY`;
- `FREEZE`;
- `F14 NOT OPENED`;
- Main Strength, Dominant Condition y necesidades de revisión externa.

## 11. Fricción de schema

La columna legacy `Resumen Margen.Etapa Análisis` no dispone de un valor específico `SHORTLIST_FINAL`.

Se utiliza el valor de compatibilidad:

```text
SHORTLIST_PRE_SCREENING
```

Esto no redefine F13 ni reabre pre-screening. Es una fricción de representación para retrospectiva / eventual Matrix vNext.

## 12. Validación técnica

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
matrix-aut58-brand-cand-003-phase13.xlsx
```

SHA-256:

```text
ec5c8b8f52cc3ae13c2d759e41b4f90f568948fa03676271ce585894d80c44da
```

## 13. Confidencialidad

Este documento conserva conclusiones decision-grade y estado metodológico.

No publica:

- cotizaciones privadas completas;
- objetivos de negociación;
- contactos;
- documentación privada de proveedores;
- simulaciones comerciales sensibles.

La matriz continúa siendo el soporte operativo privado.

## 14. Cierre

```text
F13 — SHORTLIST FINAL
→ CLOSED

BRAND-CAND-003
→ PORTFOLIO REVIEW READY
→ FREEZE

BASE-HOGAR-010
→ FINALIST — CONDITIONED
→ ELIGIBLE FOR PORTFOLIO REVIEW

F14
→ NOT OPENED
```

## 15. Próxima acción

```text
NEXT
→ BRAND-CAND-004 — Monitoreo doméstico de energía
→ luego BRAND-CAND-005
→ luego BRAND-CAND-006
→ Portfolio Review global
→ revisión externa
→ selección para profundización
→ decisión de apertura de F14
```

Principio vigente:

> Profundidad suficiente para decidir; no profundidad máxima posible.
