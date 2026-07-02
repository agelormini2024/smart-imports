---
id: si-decision-002
title: Use Hybrid Language Policy
description: Decisión de utilizar metadatos y convenciones técnicas en inglés, pero contenido estratégico, funcional, comercial y operativo en español.
version: 1.0.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-07-02
tags:
  - decision
  - documentation
  - language-policy
related:
  - si-doc-001
  - si-00
phase: foundation
---

# SI-DECISION-002 — Usar política de idioma híbrida

> **La documentación debe ser técnica cuando corresponde, pero comprensible para las personas que toman decisiones.**

---

## 1. Contexto

Smart Imports tendrá documentación técnica y documentación de negocio.

El Founder está acostumbrado a trabajar con documentación técnica en inglés, pero parte de la documentación deberá compartirse con un socio de negocio que no maneja inglés.

Por lo tanto, escribir toda la documentación en inglés dificultaría la comunicación estratégica con personas no técnicas.

Al mismo tiempo, usar español para metadatos, código, nombres de archivos y convenciones técnicas complicaría la integración con herramientas de desarrollo, GitHub, documentación estática y futuros agentes IA.

---

## 2. Decisión

Smart Imports utilizará una política de idioma híbrida:

- **Metadatos, nombres técnicos, nombres de archivos, nombres de carpetas y convenciones de software:** en inglés.
- **Contenido estratégico, funcional, comercial, operativo y documentos para socios:** en español.

---

## 3. Justificación

Esta política permite equilibrar dos necesidades:

1. Mantener compatibilidad técnica con el ecosistema de desarrollo.
2. Asegurar que el contenido estratégico sea entendible para personas de negocio.

La documentación debe alinear personas, no excluirlas.

---

## 4. Alternativas consideradas

### Todo en inglés

Ventaja: mayor estandarización técnica.

Desventaja: dificultaría la lectura para el socio y personas de negocio.

### Todo en español

Ventaja: mayor claridad para el socio.

Desventaja: peor integración con convenciones técnicas, GitHub, código y herramientas de documentación.

### Política híbrida

Ventaja: combina claridad de negocio con compatibilidad técnica.

Desventaja: requiere disciplina para mantener la separación.

---

## 5. Consecuencias

A partir de esta decisión:

- Los YAML front matter usarán claves en inglés.
- Los nombres de archivos y carpetas usarán inglés cuando sea posible.
- El contenido principal de negocio se escribirá en español.
- La documentación técnica podrá mezclar inglés y español según corresponda.
- Los documentos compartibles con el socio deberán priorizar español claro.

---

## 6. Impacto en el proyecto

Impacta sobre:

- Estándar documental.
- Vision docs.
- Business Manual.
- Business Intelligence Manual.
- Decision Log.
- Meeting Notes.
- Functional Specifications.
- Technical Specifications.

---

## 7. Documentos relacionados

- `si-doc-001-documentation-standards.md`
- `si-00-sprint-0-foundation.md`

---

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-02 | Decisión aprobada. |
