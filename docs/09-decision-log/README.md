---
id: si-decision-log-readme
title: Decision Log Index
description: Índice principal de la carpeta 09-decision-log de Smart Imports. Define el propósito, estructura y uso del registro de decisiones estratégicas, funcionales y técnicas.
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-07-02
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

> **Una decisión no documentada es una decisión que el proyecto puede olvidar.**

---

## 1. Propósito de esta carpeta

La carpeta `09-decision-log` contiene el registro formal de decisiones relevantes de **Smart Imports**.

Su objetivo es asegurar que las decisiones importantes del proyecto no queden dispersas en chats, reuniones, planillas o conversaciones informales.

Cada decisión estratégica, funcional, técnica o metodológica relevante debe poder responder:

- Qué se decidió.
- Cuándo se decidió.
- Por qué se decidió.
- Qué alternativas se consideraron.
- Qué consecuencias tiene.
- Qué documentos están relacionados.
- Qué impacto puede tener en el futuro.

---

## 2. Por qué existe el Decision Log

Smart Imports está naciendo como un proyecto de inteligencia comercial, tecnología, importación, automatización e IA.

Eso implica tomar decisiones en muchas dimensiones:

- Estrategia.
- Modelo de negocio.
- Investigación.
- Scoring.
- Metodología.
- Tecnología.
- IA.
- Marca.
- Operación.
- Inversión.
- Documentación.

Si esas decisiones no se registran, el proyecto corre el riesgo de:

- Repetir debates ya resueltos.
- Perder contexto.
- Cambiar criterios sin darse cuenta.
- Contradecir decisiones anteriores.
- Olvidar por qué se eligió un camino.
- Depender demasiado de la memoria del Founder o del chat.

El Decision Log evita ese problema.

---

## 3. Qué tipo de decisiones deben registrarse

Debe registrarse toda decisión que afecte de forma relevante:

- La visión del proyecto.
- El modelo de negocio.
- La metodología de investigación.
- La matriz de oportunidades.
- Los criterios de scoring.
- La estructura documental.
- La futura plataforma.
- El uso de IA.
- La arquitectura técnica.
- La relación con el socio.
- El uso del capital.
- La selección o descarte de nichos.
- La estrategia comercial.
- La marca.
- El roadmap.

---

## 4. Qué decisiones no necesitan registrarse

No es necesario registrar decisiones menores, operativas o reversibles que no afecten la dirección del proyecto.

Ejemplos:

- Cambios menores de redacción.
- Corrección de errores ortográficos.
- Ajustes visuales sin impacto estratégico.
- Orden temporal de tareas pequeñas.
- Pruebas descartadas sin consecuencia.

Regla práctica:

> Si dentro de seis meses podríamos preguntarnos “¿por qué hicimos esto?”, entonces debe registrarse.

---

## 5. Estructura de una decisión

Cada decisión debe documentarse en un archivo Markdown individual.

### 5.1 Patrón de nombre de archivo

```text
si-decision-001-short-title.md
```

Ejemplos:

```text
si-decision-001-use-markdown.md
si-decision-002-hybrid-language-policy.md
si-decision-003-evaluate-niches-before-products.md
```

---

### 5.2 YAML Front Matter

Cada decisión debe incluir metadatos en inglés:

```yaml
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
phase: foundation
---
```

---

### 5.3 Secciones obligatorias

Cada documento de decisión debe incluir:

```markdown
# SI-DECISION-XXX — Título de la decisión

## 1. Contexto

## 2. Decisión

## 3. Justificación

## 4. Alternativas consideradas

## 5. Consecuencias

## 6. Impacto en el proyecto

## 7. Documentos relacionados

## 8. Changelog
```

---

## 6. Estados de una decisión

Las decisiones pueden usar los mismos valores de `status` definidos en `SI-DOC-001`.

| Status | Significado |
|---|---|
| `draft` | Decisión propuesta, todavía no aceptada formalmente. |
| `review` | Lista para revisión. |
| `approved` | Decisión aceptada como referencia vigente. |
| `deprecated` | Decisión reemplazada por otra posterior. |
| `archived` | Decisión histórica, conservada por trazabilidad. |

---

## 7. Relación con documentos

Toda decisión debería enlazar, cuando corresponda, a los documentos que afecta.

Ejemplos:

| Decisión | Documento afectado |
|---|---|
| Usar Markdown | `si-doc-001` |
| Usar política de idioma híbrida | `si-doc-001` |
| Evaluar nichos antes que productos | `si-vision-001`, `si-bim-*` |
| Crear matriz de oportunidades | `si-bim-*`, Google Sheet |
| No invertir todo el capital en stock | `si-business-*`, `si-roadmap-*` |

---

## 8. Decisiones iniciales detectadas

Durante la etapa fundacional ya se identificaron varias decisiones que deberían convertirse en archivos formales:

| ID propuesto | Decisión | Estado sugerido |
|---|---|---|
| `si-decision-001` | Usar Markdown como formato documental principal. | `approved` |
| `si-decision-002` | Usar metadatos y convenciones técnicas en inglés. | `approved` |
| `si-decision-003` | Usar contenido estratégico, funcional, comercial y operativo en español. | `approved` |
| `si-decision-004` | Organizar la documentación como Knowledge Base. | `approved` |
| `si-decision-005` | Trabajar por Sprints documentales y estratégicos. | `approved` |
| `si-decision-006` | Evaluar nichos antes que productos. | `approved` |
| `si-decision-007` | Usar evidencia antes que intuición para decisiones relevantes. | `approved` |
| `si-decision-008` | No desarrollar la plataforma antes de validar manualmente la metodología. | `approved` |
| `si-decision-009` | Usar Google Sheets como herramienta inicial de investigación y scoring. | `approved` |
| `si-decision-010` | Tratar la futura plataforma como implementación de una metodología, no como copia de una planilla. | `approved` |

---

## 9. Criterio para aprobar una decisión

Una decisión puede considerarse `approved` cuando:

- El Founder está de acuerdo.
- La decisión es consistente con la visión.
- El impacto está comprendido.
- La justificación está documentada.
- No contradice una decisión previa vigente.
- Si contradice una decisión previa, la reemplaza explícitamente.

---

## 10. Flujo recomendado

```text
Idea o discusión relevante
  ↓
Se identifica una decisión
  ↓
Se redacta un documento si-decision-XXX
  ↓
Se revisa con el Founder
  ↓
Se aprueba o ajusta
  ↓
Se referencia desde documentos relacionados
```

---

## 11. Plantilla base

```markdown
---
id: si-decision-xxx
title: Decision Title
description: Descripción breve de la decisión.
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - decision
related:
  - related-doc-id
phase: foundation
---

# SI-DECISION-XXX — Título de la decisión

## 1. Contexto

Describir la situación que originó la decisión.

## 2. Decisión

Explicar claramente qué se decidió.

## 3. Justificación

Explicar por qué se tomó esta decisión.

## 4. Alternativas consideradas

Listar alternativas evaluadas, incluso si fueron descartadas.

## 5. Consecuencias

Explicar qué cambia a partir de esta decisión.

## 6. Impacto en el proyecto

Indicar si afecta estrategia, documentación, investigación, plataforma, tecnología, IA, marca u operación.

## 7. Documentos relacionados

- `document-id`

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | YYYY-MM-DD | Initial draft. |
```

---

## 12. Preguntas abiertas

- ¿Todas las decisiones iniciales deben crearse como archivos individuales ahora o sólo las más relevantes?
- ¿Cuándo una decisión pasa formalmente de `draft` a `approved`?
- ¿Conviene usar una numeración estrictamente secuencial o agrupar decisiones por área?
- ¿Las decisiones sobre nichos deben vivir en Decision Log o en Research?
- ¿Qué decisiones deben compartirse con el socio y cuáles son sólo internas?

---

## 13. Próximos pasos

1. Crear `si-decision-001-use-markdown-as-documentation-format.md`.
2. Crear `si-decision-002-use-hybrid-language-policy.md`.
3. Crear `si-decision-003-evaluate-niches-before-products.md`.
4. Crear `si-decision-004-use-evidence-before-intuition.md`.
5. Definir cuándo un documento de decisión pasa de `draft` a `approved`.

---

## 14. Related Documents

- `si-doc-001-documentation-standards.md`
- `si-00-sprint-0-foundation.md`
- `si-vision-001-smart-imports-vision.md`

---

## 15. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Versión inicial del índice de Decision Log. |
