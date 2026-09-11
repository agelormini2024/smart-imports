---
id: si-decision-014
title: Adopt Niche 3 Method v2 and aut34
description: Adopta Method v2 para el Nicho 3, aut34 como snapshot comercial vigente y difiere cambios de schema hasta que exista un requerimiento bloqueante.
version: 1.0.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-11
updated: 2026-09-11
tags:
  - decision
  - method-v2
  - niche-003
  - matrix
  - governance
related:
  - si-roadmap-002
  - si-research-005
  - si-agent-001
  - si-decision-011
  - si-decision-012
  - si-decision-013
phase: research
---

# SI-DECISION-014 — Adopt Niche 3 Method v2 and aut34

## 1. Contexto

La investigación del Nicho 3 — **Mascotas: cuidado, bienestar y tecnología** — se ejecutó con una metodología más madura que la utilizada en los primeros dos nichos.

El trabajo reveló la necesidad de separar explícitamente:

```text
NICHO
→ NECESIDAD / FAMILIA
→ ARQUITECTURA DE SOLUCIÓN
→ PRODUCTO BASE
```

También confirmó que la matriz operativa y `full-matrix-v5 0.7.0` pueden soportar el ciclo actual sin reabrir inmediatamente el Matrix Validator, aunque existen necesidades de modelado futuras.

La Fase 6 fue materializada en:

```text
matrix-aut34-niche3-phase6-corrected.xlsx
```

y validada con Matrix Validator v0.1.0 sin errores, warnings, info ni limitaciones.

## 2. Decisión

Se decide:

1. adoptar **Method v2** como metodología operativa vigente para el Nicho 3;
2. adoptar `matrix-aut34-niche3-phase6-corrected.xlsx` como **snapshot comercial operativo vigente**;
3. mantener `full-matrix-v5 0.7.0` estable durante el ciclo actual;
4. no reabrir Matrix Validator mientras las nuevas necesidades de schema no bloqueen el trabajo comercial;
5. registrar tres necesidades para Matrix vNext:
   - `Familia` y `Arquitectura` explícitas;
   - `Tipo Competencia` explícito;
   - `Proxima Accion` alineada con fases de Method v2;
6. continuar con **Fase 7 — shortlist pre-origen**.

## 3. Justificación

### 3.1 El método ya fue probado sobre evidencia real

No surge de un diseño teórico aislado. Las reglas fueron descubiertas y ajustadas al analizar:

- Vacuum Grooming;
- areneros automáticos/smart;
- Smart Fountain;
- GPS + Wellness.

### 3.2 El schema actual no bloquea el ciclo

Las limitaciones detectadas pueden representarse temporalmente sin perder integridad:

- `Subcategoría` representa Arquitectura;
- sustitutos y benchmarks se preservan en evidencia y resúmenes;
- la próxima acción metodológica se documenta aunque la fórmula legacy de `Nichos` continúe vigente.

### 3.3 Evitar cambios prematuros protege el Engine

Modificar schema, reglas, fixtures y documentación técnica ahora ampliaría alcance sin un bloqueo operativo real.

Se mantiene el principio:

> **Manual first → standardize → automate.**

### 3.4 aut34 pasó el gate técnico

```text
Application: 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
SHA-256:
ad791f8d5fe5c0bb0b18994d4c12d45b187499216f3dbd90cd42e4a9b08f9bf5
```

## 4. Alternativas consideradas

### A. Reabrir Matrix Validator antes de materializar Nicho 3

Rechazada.

Habría introducido cambios de schema antes de comprobar si eran realmente bloqueantes.

### B. Mantener la metodología legacy de Nicho 2

Rechazada.

No representa correctamente arquitecturas, sustitutos, capas de servicio y Productos Base observados en un nicho tecnológicamente más complejo.

### C. No materializar todavía en la matriz

Rechazada.

Después de Fase 6 ya existe suficiente normalización para conservar evidencia y PB en la fuente operativa.

## 5. Consecuencias

### Positivas

- Method v2 queda formalizado a partir de trabajo real.
- `aut34` se convierte en nueva fuente operativa comercial.
- el Engine permanece estable;
- se preserva la separación entre investigación, matriz y software;
- la Fase 7 puede comenzar con ocho PB trazables.

### Costos / limitaciones

- `Subcategoría` continúa sobrecargada temporalmente;
- la matriz no expresa canónicamente tipos de competencia;
- `Nichos.Proxima Accion` no representa todavía el flujo Method v2.

Estas limitaciones deben permanecer visibles, no ocultarse.

## 6. Impacto

### Smart Imports

- nuevo snapshot comercial vigente: `aut34`;
- Nicho 3 avanza a Fase 7;
- se crea `SI-RESEARCH-005`.

### Smart Imports Engine

- no hay cambio de código;
- no hay cambio de schema;
- no hay nueva release;
- `aut32` sigue siendo baseline técnica de v0.1.0;
- `full-matrix-v5 0.7.0` sigue siendo schema operativo.

## 7. Documentos relacionados

- [SI-RESEARCH-005 — Niche 3 Phases 0–6](../06-research/niche-003-pet-care-wellness-technology/si-research-005-niche-3-phases-0-to-6.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-DECISION-010 — Adopt aut31 and full-matrix-v5](./si-decision-010-adopt-aut31-and-full-matrix-v5.md)

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-11 | Adopción de Method v2, `aut34` y estrategia de diferir Matrix vNext. |
