---
id: si-decision-001
title: Use Markdown as Documentation Format
description: Decisión de utilizar Markdown como formato documental principal para Smart Imports.
version: 1.0.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-07-02
tags:
  - decision
  - documentation
  - markdown
related:
  - si-doc-001
  - si-00
phase: foundation
---

# SI-DECISION-001 — Usar Markdown como formato documental principal

> **La documentación debe ser simple de escribir, fácil de versionar y útil para humanos y sistemas.**

---

## 1. Contexto

Smart Imports comenzó como una conversación estratégica sobre importación, e-commerce, automatización, IA y software propio.

A medida que el proyecto creció, se identificó que el conocimiento no podía quedar únicamente en el chat. Era necesario crear una Knowledge Base estructurada, versionable y preparada para evolucionar hacia un repositorio formal.

Se evaluó que la documentación debía poder ser:

- Escrita rápidamente.
- Versionada con Git.
- Leída en GitHub.
- Convertida a otros formatos si fuese necesario.
- Utilizada en el futuro por agentes de IA o procesos RAG.

---

## 2. Decisión

Smart Imports utilizará **Markdown** como formato documental principal.

---

## 3. Justificación

Markdown permite escribir documentación simple, portable, versionable y compatible con herramientas modernas de desarrollo.

Es especialmente adecuado para Smart Imports porque:

- Funciona muy bien con Git y GitHub.
- No depende de herramientas propietarias.
- Es fácil de leer incluso sin renderizar.
- Permite incluir tablas, código, diagramas y enlaces.
- Puede convertirse a PDF, HTML o sitios de documentación.
- Puede ser procesado por herramientas de IA.

---

## 4. Alternativas consideradas

### Google Docs

Ventaja: fácil de compartir con personas no técnicas.

Desventaja: menor control de versiones, menor integración con Git y menor utilidad futura para documentación técnica.

### Word / DOCX

Ventaja: formato conocido.

Desventaja: poco adecuado para versionado, automatización y repositorios de software.

### Notion

Ventaja: buena experiencia visual.

Desventaja: dependencia de plataforma externa y menor portabilidad.

---

## 5. Consecuencias

A partir de esta decisión:

- Los documentos formales se crearán en `.md`.
- La documentación podrá vivir en un futuro repositorio GitHub.
- Se podrá mantener historial de cambios.
- La Knowledge Base será más fácil de utilizar por futuras herramientas de IA.
- Los documentos compartibles podrán exportarse a PDF cuando sea necesario.

---

## 6. Impacto en el proyecto

Impacta sobre:

- Documentación.
- Knowledge Base.
- Repositorio futuro.
- Especificaciones funcionales.
- Especificaciones técnicas.
- Business Intelligence Manual.
- Decision Log.

---

## 7. Documentos relacionados

- `si-doc-001-documentation-standards.md`
- `si-00-sprint-0-foundation.md`

---

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-02 | Decisión aprobada. |
