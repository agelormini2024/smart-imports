---
id: docs-04-technical-specifications-readme
title: 04 — Technical Specifications
description: Índice de especificaciones técnicas de Smart Imports y del Smart Imports Intelligence Engine.
version: 0.4.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-08-05
tags:
  - smart-imports
  - documentation
  - technical-specifications
  - architecture
related:
  - si-func-001
  - si-decision-009
  - si-decision-011
  - si-tech-001
  - si-tech-002
phase: foundation
---
# 04 — Technical Specifications

> Esta sección define cómo implementar los comportamientos aprobados sin mezclar decisiones técnicas con metodología de negocio.

## 1. Propósito

Documentar:

- Arquitectura.
- Stack.
- Módulos.
- Interfaces.
- Schemas ejecutables.
- Persistencia.
- APIs.
- Infraestructura.
- Seguridad.
- Testing.
- Integraciones.
- Operación del Smart Imports Intelligence Engine.

## 2. Estado

El primer módulo técnico, el `Matrix Validator`, cerró su MVP y fue publicado como release reproducible `v0.1.0`.

La documentación detallada de implementación, ADR, reglas, fixtures y CI permanece en `smart-imports-engine`. Esta sección conserva el contrato técnico de alto nivel y el estado as-built verificable para el repositorio integral.

## 3. Documentos

| Documento | Estado | Propósito |
|---|---|---|
| [`SI-TECH-001 — Matrix Validator Architecture`](./si-tech-001-matrix-validator-architecture.md) | `review` | Definir repositorio, stack, módulos, ports/adapters, schemas, CLI, testing, seguridad y evolución del MVP. |
| [`SI-TECH-002 — Matrix Validator As-Built`](./si-tech-002-matrix-validator-as-built.md) | `review` | Registrar la baseline verificable de `aut32`, `full-matrix-v5 0.7.0` y la release `v0.1.0`. |

## 4. Reglas de esta sección

- Una especificación técnica debe implementar una necesidad funcional aprobada.
- Las decisiones de negocio no se redefinen aquí.
- Los ejemplos de código pueden estar en inglés.
- Los secretos y datos operativos no deben documentarse.
- Las versiones reales de dependencias se fijan mediante lockfiles.
- Las decisiones irreversibles o de alto impacto deben registrarse también en Decision Log.
- El detalle ejecutable pertenece a `smart-imports-engine`; este repositorio conserva síntesis, contratos y trazabilidad integral.

## 5. Próximos pasos

1. Mantener `SI-TECH-002` alineado con cada release relevante del Engine.
2. Abrir trabajo post-MVP sólo cuando exista una necesidad comercial o de operación claramente identificada.
3. Evitar ampliar el Validator por anticipación sin evidencia de uso.
4. Evaluar futuros módulos del Intelligence Engine de forma incremental.

## 6. Documentos relacionados

- [SI-FUNC-001 — Matrix Validator](../03-functional-specifications/si-func-001-matrix-validator.md)
- [SI-DECISION-009 — Separate Knowledge and Engine Repositories](../09-decision-log/si-decision-009-separate-knowledge-and-engine-repositories.md)
- [SI-DECISION-011 — Adopt aut32 and release Matrix Validator v0.1.0](../09-decision-log/si-decision-011-adopt-aut32-and-release-matrix-validator-v0.1.0.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 7. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Placeholder inicial. |
| 0.2.0 | 2026-07-24 | Se incorpora SI-TECH-001 como primera especificación técnica del Intelligence Engine. |
| 0.2.1 | 2026-07-24 | Se actualiza SI-TECH-001 para utilizar pnpm como package manager. |
| 0.3.0 | 2026-08-03 | Se registra la arquitectura as-built con SheetJS, schemas v3/v4 y estado de cierre. |
| 0.4.0 | 2026-08-05 | Se registra SI-TECH-002 alineado con `aut32` y la release `v0.1.0`. |
