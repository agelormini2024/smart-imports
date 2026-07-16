---
id: si-decision-log-readme
title: Decision Log Index
description: Índice de decisiones estratégicas, metodológicas y técnicas de Smart Imports.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-07-16
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

## 6. Próximas acciones

- Revisar y aprobar SI-DECISION-005.
- Revisar y aprobar SI-DECISION-006.
- Registrar la selección del Nicho 2 cuando se tome la decisión.
- Registrar decisiones arquitectónicas relevantes del Intelligence Engine.

## 7. Documentos relacionados

- [Documentation Standards](../standards/si-doc-001-documentation-standards.md)
- [Roadmaps](../08-roadmaps/README.md)
- [AI Agents](../05-ai-agents/README.md)

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Versión inicial del índice. |
| 0.2.0 | 2026-07-16 | Se actualizó el índice con decisiones reales hasta SI-DECISION-006. |
