---
id: si-decision-log-readme
title: Decision Log Index
description: Índice de decisiones estratégicas, metodológicas y técnicas de Smart Imports.
version: 0.5.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-08-07
tags:
  - decision-log
  - governance
  - decisions
  - smart-imports
related:
  - si-doc-001
  - si-00
  - si-vision-001
phase: foundation
---
# 09 — Decision Log

> Una decisión no documentada es una decisión que el proyecto puede olvidar.

## 1. Propósito

El Decision Log conserva las decisiones que afectan de forma relevante:

- Visión.
- Modelo de negocio.
- Metodología.
- Matriz y scoring.
- Investigación.
- Uso de IA.
- Arquitectura técnica.
- Selección o descarte de nichos.
- Uso del capital.
- Roadmap.

Cada decisión debe explicar contexto, decisión, justificación, alternativas y consecuencias.

## 2. Decisiones registradas

| ID | Documento | Decisión | Estado |
|---|---|---|---|
| `si-decision-001` | [`si-decision-001-use-markdown-as-documentation-format.md`](./si-decision-001-use-markdown-as-documentation-format.md) | Usar Markdown como formato documental. | Vigente |
| `si-decision-002` | [`si-decision-002-use-hybrid-language-policy.md`](./si-decision-002-use-hybrid-language-policy.md) | Usar política de idioma híbrida. | Vigente |
| `si-decision-003` | [`si-decision-003-evaluate-niches-before-products.md`](./si-decision-003-evaluate-niches-before-products.md) | Evaluar nichos antes que productos. | Vigente |
| `si-decision-004` | [`si-decision-004-use-evidence-before-intuition.md`](./si-decision-004-use-evidence-before-intuition.md) | Usar evidencia antes que intuición. | Vigente |
| `si-decision-005` | [`si-decision-005-portable-solar-pilot-scope.md`](./si-decision-005-portable-solar-pilot-scope.md) | Limitar el piloto solar portátil y excluir power stations. | `review` |
| `si-decision-006` | [`si-decision-006-build-intelligence-engine-incrementally.md`](./si-decision-006-build-intelligence-engine-incrementally.md) | Construir el Intelligence Engine de forma incremental. | `review` |
| `si-decision-007` | [`si-decision-007-select-travel-organization-as-niche-2.md`](./si-decision-007-select-travel-organization-as-niche-2.md) | Seleccionar Viaje organizado y equipaje funcional como Nicho 2. | Vigente |
| `si-decision-008` | [`si-decision-008-close-niche-2-demand-and-competition.md`](./si-decision-008-close-niche-2-demand-and-competition.md) | Cerrar Demanda y Competencia del Nicho 2 sin forzar la subcategoría de ropa usada. | `approved` |
| `si-decision-009` | [`si-decision-009-separate-knowledge-and-engine-repositories.md`](./si-decision-009-separate-knowledge-and-engine-repositories.md) | Separar el repositorio documental del repositorio ejecutable del Intelligence Engine. | `approved` |
| `si-decision-010` | [`si-decision-010-adopt-aut31-and-full-matrix-v5.md`](./si-decision-010-adopt-aut31-and-full-matrix-v5.md) | Adoptar `aut31` y los resúmenes normalizados; baseline histórica reemplazada operativamente por SI-DECISION-011. | `approved` |
| `si-decision-011` | [`si-decision-011-adopt-aut32-and-release-matrix-validator-v0.1.0.md`](./si-decision-011-adopt-aut32-and-release-matrix-validator-v0.1.0.md) | Adoptar `aut32`, `full-matrix-v5 0.7.0` y la release `v0.1.0`. | `approved` |
| `si-decision-012` | [`si-decision-012-adopt-aut33-and-headroom-first-margin-screening.md`](./si-decision-012-adopt-aut33-and-headroom-first-margin-screening.md) | Adoptar `aut33` e Import Cost Headroom como gate previo al Landed Cost. | `approved` |
| `si-decision-013` | [`si-decision-013-add-decision-reporting-layer-after-niche-2.md`](./si-decision-013-add-decision-reporting-layer-after-niche-2.md) | Diseñar una capa de reporting ejecutivo derivada de la matriz después del Nicho 2. | `approved` |

## 3. Cuándo registrar una decisión

Regla práctica:

> Si dentro de seis meses podríamos preguntarnos “¿por qué hicimos esto?”, debe existir un documento de decisión.

No es necesario registrar correcciones menores, tareas pequeñas o cambios visuales reversibles.

## 4. Estructura obligatoria

```text
Contexto
Decisión
Justificación
Alternativas consideradas
Consecuencias
Impacto
Documentos relacionados
Changelog
```

## 5. Estados

- `draft`: en construcción.
- `review`: lista para revisión.
- `approved`: aceptada explícitamente por el Founder.
- `deprecated`: reemplazada.
- `archived`: conservada como historial.

Una decisión `approved` puede conservar valor histórico aunque una decisión posterior reemplace su baseline operativa. La relación de reemplazo debe quedar explícita en el documento nuevo y en este índice.

## 6. Próximas acciones

- Revisar el estado documental de SI-DECISION-005 y SI-DECISION-006.
- Registrar nuevas decisiones sólo cuando modifiquen arquitectura, seguridad, metodología, baseline operativa o roadmap.
- Mantener SI-DECISION-010 como antecedente histórico de la normalización de resúmenes.
- Usar SI-DECISION-011 como decisión vigente para la matriz y release del Validator.

## 7. Documentos relacionados

- [Documentation Standards](../standards/si-doc-001-documentation-standards.md)
- [Roadmaps](../08-roadmaps/README.md)
- [AI Agents](../05-ai-agents/README.md)

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Versión inicial del índice. |
| 0.2.0 | 2026-07-16 | Se actualizó el índice con decisiones reales hasta SI-DECISION-006. |
| 0.3.0 | 2026-07-23 | Se incorporaron SI-DECISION-007 y SI-DECISION-008. |
| 0.4.0 | 2026-07-24 | Se incorporó SI-DECISION-009 sobre la separación de repositorios. |
| 0.5.0 | 2026-08-05 | Se incorporan SI-DECISION-010 y SI-DECISION-011 y se actualiza la baseline operativa. |
