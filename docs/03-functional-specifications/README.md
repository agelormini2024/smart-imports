---
id: docs-03-functional-specifications-readme
title: 03 — Functional Specifications
description: Índice de especificaciones funcionales de la futura plataforma Smart Imports.
version: 0.4.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-10-23
tags:
  - smart-imports
  - documentation
  - functional-specifications
---

# 03 — Functional Specifications

> Esta sección define qué debe hacer la plataforma antes de decidir cómo implementarla.

## 1. Propósito

Documentar el comportamiento funcional de la futura plataforma Smart Imports y de los módulos incrementales del Smart Imports Intelligence Engine.

Las especificaciones de esta carpeta deben:

- Definir usuarios, entradas, procesos y salidas.
- Separar requisitos funcionales de decisiones técnicas.
- Incluir criterios de aceptación.
- Mantener trazabilidad con decisiones, roadmaps y casos reales.
- Evitar ampliar alcance antes de validar el módulo anterior.

## 2. Estado

`SI-FUNC-001` está aprobado. Su implementación es funcional y avanzada, pero el cierre del MVP permanece pendiente por las hojas narrativas, reglas semánticas prioritarias, E2E público y CI.

**Smart Imports v3:** la visión está en `review`. `SI-V3-FUNC-001` (Bloque 1) y `SI-V3-FUNC-002` (Bloque 2) están en `draft`: decisiones acordadas funcionalmente, pendientes de revisión y aprobación documental formal.

## 3. Documentos

| Documento | Estado | Propósito |
|---|---|---|
| [SI-FUNC-001 — Matrix Validator](./si-func-001-matrix-validator.md) | Approved / implementation advanced | Validar estructura, IDs, relaciones, valores y fórmulas de la matriz operativa. |

| [SI-V3-FUNC-001 — Misión y ejecución](./si-v3-func-001-mission-and-execution-mvp.md) | Draft / revisión documental pendiente | Bloque 1 v3: misiones, ejecuciones, preflight, gobierno y `CA-01..CA-10`. |
| [SI-V3-FUNC-002 — Investigación y agentes](./si-v3-func-002-research-and-agents-mvp.md) | Draft / revisión documental pendiente | Bloque 2 v3: `DF-AG-001..016`, H1–H3, investigación y ensayo histórico. |

## 4. Próximos pasos

1. Normalizar las tres hojas `Resumen *`.
2. Actualizar el contrato con el schema posterior a `full-matrix-v4`.
3. Acordar el subconjunto semántico bloqueante para la release.
4. Incorporar fixtures públicos end-to-end.
5. Cerrar los criterios de aceptación aún pendientes.

## 5. Documentos relacionados

- [SI-V3-VISION-001 — Visión de Smart Imports v3](../00-vision/si-v3-vision-001-product-vision-and-initial-scope.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-ROADMAP-001 — Pilot Closure, Niche 2 and Engine MVP](../08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 6. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Placeholder inicial. |
| 0.2.0 | 2026-07-24 | Se incorpora SI-FUNC-001 como primera especificación funcional del Intelligence Engine. |
| 0.3.0 | 2026-08-03 | Se registra la implementación avanzada, los schemas v3/v4 y los bloqueadores de cierre. |
| 0.4.0 | 2026-10-23 | Incorporación de referencias a los Bloques 1 y 2 de Smart Imports v3, preservando los documentos y el historial anteriores. |
