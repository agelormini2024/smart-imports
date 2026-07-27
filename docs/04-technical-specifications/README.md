---
id: docs-04-technical-specifications-readme
title: 04 — Technical Specifications
description: Índice de especificaciones técnicas de Smart Imports y del Smart Imports Intelligence Engine.
version: 0.2.1
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-07-24
tags:
  - smart-imports
  - documentation
  - technical-specifications
  - architecture
related:
  - si-func-001
  - si-decision-009
  - si-tech-001
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

La sección deja de funcionar como placeholder.

El primer documento técnico corresponde al `Matrix Validator`, primer MVP del Intelligence Engine.

## 3. Documentos

| Documento | Estado | Propósito |
|---|---|---|
| [SI-TECH-001 — Matrix Validator Architecture](./si-tech-001-matrix-validator-architecture.md) | Review | Definir repositorio, stack, módulos, ports/adapters, schemas, CLI, testing, seguridad y evolución del MVP. |

## 4. Reglas de esta sección

- Una especificación técnica debe implementar una necesidad funcional aprobada.
- Las decisiones de negocio no se redefinen aquí.
- Los ejemplos de código pueden estar en inglés.
- Los secretos y datos operativos no deben documentarse.
- Las versiones reales de dependencias se fijan mediante lockfiles.
- Las decisiones irreversibles o de alto impacto deben registrarse también en Decision Log.

## 5. Próximos pasos

1. Revisar y aprobar `SI-TECH-001`.
2. Crear el repositorio privado `smart-imports-engine`.
3. Inicializar Node.js 24 y pnpm 11.
4. Ejecutar el spike del adapter XLSX.
5. Implementar las reglas estructurales del Matrix Validator.
6. Agregar tests sintéticos y tests privados locales.

## 6. Documentos relacionados

- [SI-FUNC-001 — Matrix Validator](../03-functional-specifications/si-func-001-matrix-validator.md)
- [SI-DECISION-009 — Separate Knowledge and Engine Repositories](../09-decision-log/si-decision-009-separate-knowledge-and-engine-repositories.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 7. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Placeholder inicial. |
| 0.2.0 | 2026-07-24 | Se incorpora SI-TECH-001 como primera especificación técnica del Intelligence Engine. |
| 0.2.1 | 2026-07-24 | Se actualiza SI-TECH-001 para utilizar pnpm como package manager. |
