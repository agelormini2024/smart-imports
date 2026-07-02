---
id: si-bim-readme
title: Business Intelligence Manual Index
description: Índice principal del Business Intelligence Manual de Smart Imports. Organiza la metodología de investigación, evaluación, evidencias, scoring y priorización de nichos.
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-07-02
tags:
  - business-intelligence
  - research
  - methodology
  - scoring
  - matrix
  - smart-imports
related:
  - si-doc-001
  - si-00
  - si-vision-001
  - si-bim-000
phase: business-intelligence
---

# 02 — Business Intelligence Manual

> **El objetivo no es adivinar oportunidades. El objetivo es construir un método para encontrarlas.**

---

## 1. Propósito de esta carpeta

La carpeta `02-business-intelligence-manual` contiene la metodología de investigación, evaluación y priorización de oportunidades de negocio de **Smart Imports**.

Este manual define cómo Smart Imports debe:

- Investigar nichos.
- Registrar evidencias.
- Evaluar criterios.
- Asignar scores.
- Medir confianza.
- Comparar oportunidades.
- Priorizar investigaciones.
- Decidir qué nichos avanzan a fases posteriores.
- Aprender de cada investigación.

Este manual es el corazón metodológico de Smart Imports.

---

## 2. Rol dentro de Smart Imports

Smart Imports no quiere tomar decisiones de importación basadas solamente en intuición, entusiasmo o precio de compra.

El Business Intelligence Manual existe para transformar la investigación comercial en un proceso:

- Ordenado.
- Repetible.
- Auditable.
- Mejorable.
- Documentado.
- Escalable.
- Automatizable en el futuro.

La futura plataforma Smart Imports deberá implementar esta metodología, no reemplazarla.

---

## 3. Principio rector

El principio rector del BIM es:

> **Primero evidencia. Después score. Después decisión.**

En términos prácticos:

```text
Nicho
  ↓
Investigación
  ↓
Evidencias
  ↓
Interpretación
  ↓
Evaluación por criterio
  ↓
Score + Confianza
  ↓
Priorización
  ↓
Próxima acción
```

---

## 4. Qué problema resuelve

Sin metodología, el proyecto corre riesgo de:

- Enamorarse de productos atractivos.
- Confundir ventas visibles con negocio rentable.
- Subestimar competencia.
- Sobrestimar márgenes.
- Ignorar complejidad de importación.
- Elegir nichos sin diferenciación.
- Invertir capital demasiado pronto.
- Perder conocimiento en chats o planillas desordenadas.
- Tomar decisiones que no puedan auditarse más adelante.

El BIM busca reducir esos riesgos.

---

## 5. Relación con la Matriz de Oportunidades

La Matriz de Oportunidades es la herramienta inicial.

El Business Intelligence Manual es la metodología que explica cómo usarla.

La matriz responde:

> ¿Dónde cargamos la información?

El BIM responde:

> ¿Cómo decidimos qué información cargar, cómo interpretarla y qué significa?

---

## 6. Componentes principales

El BIM se organiza en los siguientes componentes:

| Componente | Descripción |
|---|---|
| Nichos | Áreas de oportunidad comercial que se investigan antes que productos específicos. |
| Criterios | Dimensiones utilizadas para evaluar cada nicho. |
| Evidencias | Datos, observaciones y fuentes que respaldan una evaluación. |
| Evaluaciones | Valor asignado a un criterio para un nicho, con justificación y confianza. |
| Score | Resultado numérico que permite comparar nichos. |
| Confianza | Nivel de solidez de la evidencia que respalda cada evaluación. |
| Priorización | Clasificación de nichos según atractivo, evidencia y riesgo. |
| Próxima acción | Paso recomendado luego de una evaluación. |

---

## 7. Criterios de evaluación

La matriz original de Smart Imports utiliza los siguientes criterios:

| Criterio | Pregunta principal |
|---|---|
| Demanda | ¿Existe mercado activo para este nicho? |
| Competencia | ¿Qué tan difícil será entrar y diferenciarse? |
| Margen Potencial | ¿Hay espacio para rentabilidad atractiva? |
| Facilidad de Importación | ¿Qué tan simple o complejo es importar productos del nicho? |
| Potencial de Marca | ¿Se puede construir una marca propia o es un commodity? |
| Venta Impulsiva | ¿El cliente puede comprar por deseo, emoción o impulso? |
| Recompra | ¿Existe posibilidad de compras recurrentes? |
| Potencial IA | ¿La IA puede generar valor diferencial para el cliente o el negocio? |
| Potencial Automatización | ¿Se pueden automatizar procesos operativos o comerciales? |
| Afinidad Personal | ¿El Founder tiene interés real en trabajar este nicho durante años? |

---

## 8. Documentos de criterios

Cada criterio deberá tener su propio documento metodológico.

Carpeta sugerida:

```text
docs/02-business-intelligence-manual/criteria/
```

Documentos previstos:

| Documento | Criterio | Estado |
|---|---|---|
| `si-bim-000-confidence-in-evaluations.md` | Confianza | Creado |
| `si-bim-001-demand-evaluation.md` | Demanda | Pendiente |
| `si-bim-002-competition-evaluation.md` | Competencia | Pendiente |
| `si-bim-003-margin-potential-evaluation.md` | Margen Potencial | Pendiente |
| `si-bim-004-import-feasibility-evaluation.md` | Facilidad de Importación | Pendiente |
| `si-bim-005-brand-potential-evaluation.md` | Potencial de Marca | Pendiente |
| `si-bim-006-impulse-purchase-evaluation.md` | Venta Impulsiva | Pendiente |
| `si-bim-007-repeat-purchase-evaluation.md` | Recompra | Pendiente |
| `si-bim-008-ai-potential-evaluation.md` | Potencial IA | Pendiente |
| `si-bim-009-automation-potential-evaluation.md` | Potencial Automatización | Pendiente |
| `si-bim-010-founder-affinity-evaluation.md` | Afinidad Personal | Pendiente |

---

## 9. Estructura estándar de un criterio

Cada documento de criterio deberá incluir:

1. Propósito.
2. Definición.
3. Pregunta principal.
4. Qué mide.
5. Qué no mide.
6. Fuentes recomendadas.
7. Evidencias requeridas.
8. Escala de Valor.
9. Escala de Confianza aplicada al criterio.
10. Ejemplos.
11. Casos límite.
12. Uso en la matriz.
13. Uso futuro en la plataforma.
14. Preguntas abiertas.
15. Changelog.

---

## 10. Escala de Valor

Los criterios se evaluarán inicialmente con una escala de 1 a 5.

| Valor | Significado general |
|---:|---|
| 1 | Muy bajo / muy desfavorable |
| 2 | Bajo / desfavorable |
| 3 | Medio / aceptable |
| 4 | Alto / favorable |
| 5 | Muy alto / muy favorable |

Regla general:

> En todos los criterios, un valor más alto debe significar una situación más atractiva para Smart Imports.

Ejemplo:

En Competencia, 5 no significa “mucha competencia”.  
Significa “baja competencia o competencia manejable”.

Esto evita confusión al calcular scores.

---

## 11. Confianza

La Confianza se documenta en:

```text
criteria/si-bim-000-confidence-in-evaluations.md
```

Definición resumida:

> Confianza mide qué tan sólida es la evidencia que respalda un valor asignado a un criterio.

No mide atractivo del nicho.

No mide probabilidad de éxito.

No mide entusiasmo personal.

Escala inicial:

| Confianza | Significado |
|---|---|
| Baja | Evidencia débil, incompleta o basada principalmente en intuición. |
| Media | Evidencia concreta pero parcial o pendiente de validación. |
| Alta | Evidencia suficiente, actual, relevante y consistente. |

---

## 12. Evidencias

Las evidencias son datos u observaciones que respaldan evaluaciones.

Ejemplos:

- Producto de Mercado Libre con más de 1000 ventas.
- Tendencia creciente en Google Trends.
- Comunidad activa de Facebook.
- Cotización FOB de proveedor.
- Costo estimado de importación.
- Cantidad de vendedores relevantes.
- Review negativa recurrente.
- Problema frecuente mencionado por usuarios.
- Certificación requerida.
- Alta concentración de competencia.

Regla:

> Un score sin evidencia es sólo una opinión.

---

## 13. Evaluaciones

Una evaluación representa la asignación de un valor a un criterio para un nicho.

Ejemplo:

```text
Nicho: Energía Solar Portátil
Criterio: Demanda
Valor: 4
Confianza: Alta
Justificación: Existen múltiples productos con +1000 ventas en Mercado Libre...
```

Una evaluación debe tener:

- Fecha.
- Nicho.
- Criterio.
- Valor.
- Confianza.
- Justificación.
- Evidencias asociadas.
- Próxima acción.
- Estado.

---

## 14. Estados sugeridos para evaluaciones

Se recomienda que cada evaluación tenga un estado.

| Estado | Significado |
|---|---|
| Borrador | Evaluación inicial, todavía incompleta. |
| Validada | Evaluación respaldada por evidencia suficiente. |
| Revisar | Evaluación que requiere actualización o nueva evidencia. |
| Descartada | Evaluación anulada o reemplazada. |

Este campo será especialmente útil en la futura plataforma.

---

## 15. Score

El score permite comparar nichos.

Inicialmente podrá calcularse como:

- Promedio simple.
- Promedio ponderado.
- Score ajustado por confianza.

La primera versión operativa puede usar promedio ponderado por criterio.

Sin embargo, el score nunca debe interpretarse aislado de la confianza.

Regla:

> Score alto con confianza baja no debe habilitar inversión.

---

## 16. Priorización

La priorización debe considerar:

- Score.
- Confianza promedio.
- Riesgos.
- Potencial estratégico.
- Facilidad de validación.
- Capital requerido.
- Afinidad del Founder.
- Próxima acción recomendada.

Ejemplo:

| Caso | Interpretación |
|---|---|
| Score alto + confianza alta | Candidato fuerte para avanzar. |
| Score alto + confianza baja | Investigar más antes de decidir. |
| Score medio + confianza alta | Nicho interesante pero no prioritario. |
| Score bajo + confianza alta | Posible descarte. |
| Score bajo + confianza baja | Investigación insuficiente o baja prioridad. |

---

## 17. Caso piloto

El primer nicho utilizado para validar la metodología será:

```text
Energía Solar Portátil
```

Este nicho será utilizado para:

- Probar la matriz.
- Documentar el criterio Demanda.
- Registrar evidencias.
- Evaluar confianza.
- Detectar mejoras en la planilla.
- Diseñar futuros módulos de plataforma.

---

## 18. Relación con Google Sheets

Durante la etapa inicial, Google Sheets será la herramienta operativa para cargar y calcular datos.

La documentación Markdown será la fuente metodológica.

Relación:

| Herramienta | Rol |
|---|---|
| Google Sheets | Operación, carga y cálculo inicial. |
| Markdown | Metodología, decisiones, criterios y documentación. |
| Futura plataforma | Implementación escalable de la metodología validada. |

---

## 19. Relación con la futura plataforma

La plataforma Smart Imports deberá implementar la metodología definida en el BIM.

No debe limitarse a copiar la planilla.

Debe convertir la metodología en software.

Entidades conceptuales futuras:

```text
Niche
  ├── Evidence
  ├── Evaluation
  ├── Criterion
  ├── Score
  ├── Confidence
  ├── Product
  ├── Supplier
  └── Decision
```

---

## 20. Relación con agentes IA

Los futuros agentes IA podrán utilizar el BIM para:

- Sugerir evidencias faltantes.
- Resumir investigaciones.
- Comparar nichos.
- Detectar contradicciones.
- Proponer scores preliminares.
- Generar próximas acciones.
- Explicar decisiones.
- Auditar evaluaciones.

Para que esto sea posible, la metodología debe estar claramente documentada.

---

## 21. Preguntas abiertas

- ¿Cada criterio debe tener evidencia mínima obligatoria?
- ¿La confianza debe transformarse en número para cálculo?
- ¿Debe existir un score ajustado por confianza desde la primera planilla?
- ¿Qué criterios deberían tener mayor peso?
- ¿Cuándo un nicho pasa de screening a investigación profunda?
- ¿Cuándo una evaluación se considera validada?
- ¿Cómo se vincularán evidencias con evaluaciones en la futura plataforma?
- ¿Qué datos quedarán en Google Sheets y cuáles en Markdown?

---

## 22. Próximos pasos

1. Crear `criteria/si-bim-001-demand-evaluation.md`.
2. Aplicar el criterio Demanda al nicho Energía Solar Portátil.
3. Registrar evidencias de Mercado Libre.
4. Definir escala específica de Demanda.
5. Revisar si la planilla necesita columna `Estado` en Evaluaciones.
6. Crear documentos de criterios restantes.

---

## 23. Related Documents

- `si-doc-001-documentation-standards.md`
- `si-00-sprint-0-foundation.md`
- `si-vision-001-smart-imports-vision.md`
- `criteria/si-bim-000-confidence-in-evaluations.md`

---

## 24. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Versión inicial del índice del Business Intelligence Manual. |
