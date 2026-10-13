---
id: si-research-089
title: BRAND-CAND-007 — Method v2 Agile — Fase 0 — Research Brief
description: Research Brief prospectivo para fuerza accesible y compacta dentro de Marca Fitness.
version: 0.1.1
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-13
updated: 2026-10-13
brand: brand-fitness
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
phase: F0
---

# SI-RESEARCH-089 — BRAND-CAND-007 — Fase 0 — Research Brief

<!-- BRAND-CAND-007-F0-RECONCILIATION:START -->
## Reconciliación de F0 — checkpoint conjunto F0–F3 (2026-10-13)

```text
SI-RESEARCH-089 — F0: CLOSED
Baseline: aut124
SHA-256: 4899f4fc595ebe1e07a4b245e5cf1cf300183f6bcd04c3937916f104a13bf108
Data Fidelity Preflight v2.4: PASS
Matrix Validator full-matrix-v5 0.7.0: PASS / 0 errors / 0 warnings / 0 info
checkpoint-exit: 0
Next lineage: F1 aut125 PASS → F2 aut126 PASS → F3 aut128 PASS
```

El cierre técnico de F0 ocurrió antes de F1. Por la cadencia acordada no se hizo checkpoint documental/commit separado. Esta reconciliación conjunta preserva la secuencia sin rehacer F0 ni crear Product Bases.
<!-- BRAND-CAND-007-F0-RECONCILIATION:END -->

## 1. Estado

```text
BRAND-CAND-007
SCREENING: CLOSED
METHOD V2: OPENED

F0: CLOSED
MATRIX: MATERIALIZED — aut124
DATA FIDELITY PREFLIGHT: PASS
MATRIX VALIDATOR: PASS
F0: CLOSED

PRODUCT BASES: NOT DEFINED
```

Este documento abre Method v2 para `BRAND-CAND-007` sin adelantar Product Bases ni evidencia propia de fases posteriores.

## 2. Input canónico

```text
Candidate ID: BRAND-CAND-007
Source Hypothesis ID: FIT-CAND-001
Candidate: Fuerza accesible y compacta
Brand: brand-fitness
Screening Type: PROSPECTIVE
Primary Mission: Construir y conservar fuerza útil
Territory Relationship: CORE
Brand Candidate Screening: PASS TO METHOD V2
```

Fuente de verdad del candidato:

`docs/07-brand/brands/brand-fitness/candidates/brand-cand-007-accessible-compact-strength.md`

La hipótesis histórica `FIT-CAND-001 — Fuerza compacta para el hogar` evolucionó durante pre-screening y screening hacia el Brand Candidate formal. Por lo tanto, F0 hereda el problema aprobado del Brand Candidate y no vuelve a restringirlo exclusivamente al hogar.

`FIT-CAND-004 — Calistenia y peso corporal` fue absorbido en `FIT-CAND-001`; sus arquitecturas pueden aparecer en el Solution Map sin constituir un candidato separado.

## 3. Problema

> **Construir o conservar fuerza sin depender de un gimnasio completo, mucho espacio ni una colección extensa de equipamiento.**

Interpretación operativa:

- la fuerza es el problema principal;
- deben existir mecanismos razonables para aplicar resistencia;
- la progresión importa;
- las restricciones de espacio, equipamiento o acceso son parte del contexto;
- “accesible” no se redefine en F0 como “barato”;
- el candidato no queda limitado por ubicación física.

## 4. Objetivo y Research Question

### Objetivo

Determinar qué arquitecturas de solución pueden permitir aplicar resistencia y sostener una progresión razonable de fuerza bajo restricciones reales de espacio, equipamiento o acceso a un gimnasio completo, manteniendo coherencia con el contexto cotidiano de Marca Fitness.

### Research Question

> **¿Qué arquitecturas de solución permiten construir o conservar fuerza útil de manera progresiva, segura y funcional bajo restricciones de espacio y equipamiento, sin convertir “fuerza” en autorización para cualquier artículo de gimnasio?**

F0 define el problema y las reglas de investigación. No selecciona productos.

## 5. Arquitecturas conceptuales habilitadas para F1

Las siguientes son familias conceptuales de solución y todavía no Product Bases:

```text
carga externa ajustable
resistencia elástica
peso corporal / calistenia
sistemas híbridos
equipamiento plegable o modular
```

Regla:

```text
ARQUITECTURA DE SOLUCIÓN
≠
PRODUCT BASE
```

F1 podrá ampliar, subdividir o descartar arquitecturas a partir de evidencia. F0 no preselecciona SKU, marca, proveedor ni publicación.

## 6. Fronteras con los demás candidatos Fitness

```text
BRAND-CAND-007 → fuerza
BRAND-CAND-008 → entrenamiento flexible
BRAND-CAND-009 → movilidad / estabilidad / capacidad física
BRAND-CAND-010 → movimiento distribuido durante la jornada
```

La frontera se fija por el problema primario, no por la forma física del producto.

Una solución portátil puede pertenecer a `BRAND-CAND-007` si su razón principal es desarrollar o conservar fuerza. La portabilidad por sí sola no la convierte en `BRAND-CAND-008`.

Una solución de bajo impacto o estabilidad no pertenece a `BRAND-CAND-007` salvo que la función central sea aplicar resistencia para construir o conservar fuerza.

La integración con la jornada cotidiana tampoco es suficiente para pertenecer a `BRAND-CAND-007`; debe mantenerse la fuerza como razón principal de existencia.

## 7. Claims / supuestos a validar

Method v2 deberá validar, cuando corresponda por arquitectura o Product Base:

- capacidad real de aplicar resistencia de forma estable;
- mecanismo de progresión;
- seguridad de uso;
- límites de carga o resistencia verificables;
- materiales, uniones y mecanismos adecuados para uso repetido;
- que la condición compacta no destruya funcionalidad o durabilidad;
- facilidad real de montaje, guardado y uso;
- cualquier promesa específica de desempeño.

La credibilidad deberá demostrarse arquitectura por arquitectura y Product Base por Product Base.

## 8. Guardrails

```text
CATEGORY CREEP
fuerza → cualquier artículo de gimnasio

PERFORMANCE CREEP
fuerza cotidiana → equipamiento profesional / alto rendimiento

FEATURE CREEP
sensor / app → Brand Fit automático
```

Regla superior:

> **La solución debe ayudar de manera central a construir o conservar fuerza y ser coherente con el contexto cotidiano definido por la marca.**

Tecnología, sensores, apps, métricas o feedback pueden actuar como capacidades transversales, pero no crean Brand Fit por sí mismos.

## 9. Scope inicial de F1 — Market / Solution Map

F1 deberá investigar el espacio de soluciones antes de normalizar Product Bases.

Preguntas iniciales:

1. ¿Qué arquitecturas resuelven de manera defendible el problema central?
2. ¿Qué mecanismos de resistencia y progresión existen?
3. ¿Qué soluciones reducen espacio o cantidad de equipamiento sin destruir funcionalidad?
4. ¿Qué arquitecturas presentan riesgos relevantes de seguridad, durabilidad, montaje o almacenamiento?
5. ¿Dónde existe evidencia suficiente para continuar hacia fases de demanda y competencia?
6. ¿Qué soluciones deben excluirse por category creep, performance creep o feature creep?

F1 no debe:

- contactar proveedores;
- abrir RFQ;
- tratar publicaciones como Product Bases;
- crear escenarios de margen;
- inferir origen;
- adelantar F8;
- producir recomendación de importación.

## 10. Governance heredado

La ejecución hereda el governance vigente de Method v2.

```text
SI-BIM-PROC-003: v1.0.6
SI-DECISION-019: vigente
SI-DECISION-020: vigente
Data Fidelity Preflight: v2.4
```

Orden de capas:

```text
evidencia cruda
→ clasificación
→ interpretación
→ score
→ decisión
```

Reglas relevantes:

```text
PUBLICATION ≠ PRODUCT BASE
PRODUCT BASE ≠ COMPETITOR / SKU
DEMAND ≠ COMPETITION
DECISION-GRADE ≠ PROCUREMENT-GRADE
```

F8 queda explícitamente heredada como:

```text
F8 — Origin Screening / Alibaba
mode: COLLABORATIVE
Founder participation: REQUIRED
Founder Review: REQUIRED FOR CLOSE
```

Esto no altera F0, pero evita que una ejecución posterior del candidato vuelva a tratar F8 como autónoma.

## 11. Materialización en matriz

Baseline heredada:

```text
matrix-aut123-brand-cand-010-post-close-core-snapshot-reconciliation.xlsx
SHA-256: 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb
```

Scope reservado:

```text
Nicho ID target: 38
Nicho: Marca Fitness — fuerza accesible y compacta
Role: MATRIX_SCOPE_ALIAS
Brand Candidate: BRAND-CAND-007
Source Hypothesis: FIT-CAND-001
Target matrix: aut124
```

Regla:

```text
MATRIX_SCOPE_ALIAS
≠
REDEFINIR BRAND-CAND-007 COMO NICHO
```

Patrón de F0 heredado de `BRAND-CAND-010 / aut105`:

- `ID`, `Nicho` y `Estado`: materializados;
- `Proxima Accion`, `Documento Research` y `Notas`: materializados;
- criterios, scores y confianzas: vacíos;
- no se crean Product Bases;
- no se crean Publicaciones ML;
- no se crea Competencia ML;
- no se crean Cotizaciones;
- no se crean escenarios de margen;
- no se crean Evaluaciones score.

## 12. Gate de cierre de F0 — registro histórico anterior al PASS

Estado registrado después de materializar aut124, ANTES de su validación (histórico):

```text
F0 ANALYSIS COMPLETE
+
aut124 MATERIALIZED
+
DATA FIDELITY PREFLIGHT PENDING
+
MATRIX VALIDATOR PENDING
=
F0 NOT CLOSED
```

F0 sólo podrá declararse `CLOSED` después de las validaciones canónicas aplicables.

No debe abrirse F1 formalmente antes de ese cierre.

## 13. Próximo gate — proyección histórica anterior al cierre de F0

Con validaciones limpias:

```text
F0 CLOSED
→ F1 — MARKET / SOLUTION MAP
```

Antes del cierre técnico de F0 (registro histórico):

```text
BRAND-CAND-007
→ METHOD V2 OPENED
→ F0 NOT CLOSED

BRAND-CAND-008
BRAND-CAND-009
→ ELIGIBLE — NOT OPENED
```

No abrir candidatos Fitness en paralelo por defecto.
