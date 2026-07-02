---
id: si-bim-000
title: Confidence in Evaluations
description: Define el concepto de Confianza dentro de la metodología de evaluación de nichos de Smart Imports.
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-07-02
tags:
  - business-intelligence
  - confidence
  - scoring
  - methodology
  - evaluation
related:
  - si-doc-001
  - si-vision-001
  - si-decision-004
phase: business-intelligence
---

# SI-BIM-000 — Confidence in Evaluations

> **Un score sin confianza puede parecer precisión, pero seguir siendo sólo una suposición.**

---

## 1. Propósito

Este documento define el concepto de **Confianza** dentro de la metodología de evaluación de nichos de Smart Imports.

La Confianza permite diferenciar entre:

- Un puntaje respaldado por evidencia sólida.
- Un puntaje basado en evidencia parcial.
- Un puntaje basado principalmente en hipótesis, intuición o información incompleta.

Este concepto es central para evitar que la matriz de oportunidades genere una falsa sensación de precisión.

---

## 2. Definición

En Smart Imports, **Confianza** representa el grado de solidez de la evidencia que respalda un valor asignado a un criterio de evaluación.

No mide qué tan bueno es el nicho.

No mide probabilidad de éxito.

No mide entusiasmo personal.

Mide qué tan confiable es el puntaje asignado.

---

## 3. Diferencia entre Valor y Confianza

Cada criterio evaluado debe tener, como mínimo, dos dimensiones:

| Dimensión | Pregunta que responde | Ejemplo |
|---|---|---|
| Valor | ¿Qué tan atractivo es este criterio para el nicho? | Demanda = 4 |
| Confianza | ¿Qué tan seguros estamos de que ese valor está bien fundamentado? | Confianza = Alta |

Ejemplo:

| Nicho | Criterio | Valor | Confianza |
|---|---:|---:|---|
| Energía solar portátil | Demanda | 4 | Alta |
| Energía solar portátil | Margen potencial | 3 | Baja |

Interpretación:

- Demanda = 4 significa que el nicho parece tener demanda alta.
- Confianza Alta significa que existen evidencias sólidas que respaldan ese valor.
- Margen potencial = 3 significa que estimamos un margen medio.
- Confianza Baja significa que todavía no hay suficiente evidencia para confiar plenamente en ese valor.

---

## 4. Lo que Confianza no significa

Confianza no significa:

- Que el negocio vaya a funcionar.
- Que el nicho sea necesariamente bueno.
- Que el Founder esté entusiasmado.
- Que el producto sea rentable.
- Que el riesgo sea bajo.
- Que convenga invertir.
- Que el criterio tenga un valor alto.

Un criterio puede tener:

- Valor alto y Confianza baja.
- Valor bajo y Confianza alta.
- Valor medio y Confianza media.

Ejemplo:

| Situación | Interpretación |
|---|---|
| Valor 5 + Confianza Baja | Parece excelente, pero todavía no está probado. |
| Valor 2 + Confianza Alta | Parece poco atractivo y hay evidencia sólida para sostenerlo. |
| Valor 3 + Confianza Media | Evaluación razonable, pero todavía mejorable. |

---

## 5. Escala de Confianza

Smart Imports utilizará inicialmente tres niveles de Confianza:

| Confianza | Significado |
|---|---|
| Baja | El puntaje está basado en intuición, evidencia débil, incompleta o no verificada. |
| Media | Existe evidencia concreta, pero todavía es parcial, limitada o requiere validación adicional. |
| Alta | Existe evidencia suficiente, actual, relevante y consistente para respaldar el puntaje. |

---

## 6. Confianza Baja

### Definición

Se utiliza cuando el puntaje asignado depende principalmente de:

- Intuición.
- Experiencia general.
- Suposiciones.
- Información incompleta.
- Datos no verificados.
- Una sola fuente débil.
- Evidencia antigua.
- Estimaciones sin cálculo.

### Ejemplos

| Criterio | Valor | Confianza | Motivo |
|---|---:|---|---|
| Margen potencial | 4 | Baja | Hay precio FOB, pero no hay costo nacionalizado. |
| Competencia | 3 | Baja | Se miraron pocas publicaciones de Mercado Libre. |
| Potencial IA | 5 | Baja | La idea parece fuerte, pero no se definió caso de uso concreto. |

### Uso recomendado

La Confianza Baja no invalida el puntaje, pero indica que no debe usarse para decisiones importantes sin investigación adicional.

---

## 7. Confianza Media

### Definición

Se utiliza cuando existe evidencia concreta, pero todavía no es suficiente para cerrar la evaluación.

Puede deberse a:

- Una fuente confiable pero incompleta.
- Datos actuales pero limitados.
- Evidencia de una sola plataforma.
- Falta de comparación entre fuentes.
- Falta de cálculo numérico completo.
- Señales positivas pero no concluyentes.

### Ejemplos

| Criterio | Valor | Confianza | Motivo |
|---|---:|---|---|
| Demanda | 4 | Media | Hay ventas en Mercado Libre, pero falta Google Trends. |
| Competencia | 3 | Media | Hay publicaciones visibles, pero falta analizar concentración de vendedores. |
| Facilidad de importación | 3 | Media | Se identificaron riesgos, pero falta validar regulación. |

### Uso recomendado

La Confianza Media permite avanzar en screening, pero requiere validación antes de inversión.

---

## 8. Confianza Alta

### Definición

Se utiliza cuando el puntaje está respaldado por evidencia suficiente y consistente.

Puede incluir:

- Varias fuentes.
- Datos actuales.
- Evidencia cuantitativa.
- Evidencia cualitativa consistente.
- Validación cruzada.
- Cálculos razonables.
- Observaciones repetibles.
- Documentación clara.

### Ejemplos

| Criterio | Valor | Confianza | Motivo |
|---|---:|---|---|
| Demanda | 4 | Alta | Múltiples productos en Mercado Libre con +1000 ventas y buenas calificaciones. |
| Recompra | 2 | Alta | La naturaleza del producto indica baja recurrencia y no hay consumibles asociados. |
| Potencial IA | 5 | Alta | Existen casos de uso claros: recomendador, calculadora, asistente técnico y soporte. |

### Uso recomendado

La Confianza Alta permite usar el puntaje con mayor peso en decisiones de priorización.

---

## 9. Relación entre Confianza y Evidencias

La Confianza debe derivarse de las evidencias registradas.

En términos funcionales:

```text
Evidencias
  ↓
Interpretación
  ↓
Valor asignado
  ↓
Confianza del valor
```

La hoja o módulo de Evidencias debe registrar los datos que justifican el puntaje.

La hoja o módulo de Evaluaciones debe registrar:

- Valor.
- Confianza.
- Justificación.
- Evidencias relacionadas.
- Próxima acción.

---

## 10. Ejemplo aplicado: Energía solar portátil / Demanda

### Evidencia disponible

Se relevaron productos en Mercado Libre para:

- Kit solar portátil.
- Ventilador solar.
- Power bank solar.
- Panel solar portátil.
- Generador solar portátil.

Se detectaron:

- Varios productos con más de 1000 ventas.
- Varias subcategorías activas.
- Calificaciones entre 4.3 y 4.7.
- Tickets variados.
- Demanda más fuerte en kits, ventiladores y power banks.
- Demanda más débil en paneles portátiles y estaciones de energía.

### Evaluación

| Criterio | Valor | Confianza |
|---|---:|---|
| Demanda | 4 | Alta |

### Justificación

La demanda del nicho está respaldada por evidencia observable en Mercado Libre. Existen múltiples productos y subcategorías con ventas relevantes y buenas calificaciones. Aunque algunas subcategorías tienen menor volumen, el nicho en conjunto presenta señales sólidas de demanda.

---

## 11. Reglas de uso

### Regla 1 — No asignar Confianza Alta sin evidencia

Un puntaje no debe tener Confianza Alta si no existen evidencias claras que lo respalden.

### Regla 2 — La Confianza puede cambiar

La Confianza debe actualizarse cuando se agregan nuevas evidencias.

Ejemplo:

```text
Demanda = 4 / Confianza Media
  ↓
Se agregan datos de Google Trends y Mercado Libre
  ↓
Demanda = 4 / Confianza Alta
```

### Regla 3 — La Confianza no cambia automáticamente el Valor

Agregar evidencia puede aumentar la Confianza sin modificar el Valor.

Ejemplo:

```text
Margen = 3 / Confianza Baja
  ↓
Se calcula costo nacionalizado
  ↓
Margen = 3 / Confianza Alta
```

El valor sigue siendo 3, pero ahora está mejor fundamentado.

### Regla 4 — Score alto con Confianza baja no habilita inversión

Un nicho con score alto pero baja confianza debe investigarse más antes de tomar decisiones de capital.

### Regla 5 — Confianza alta con score bajo puede justificar descarte

Si un nicho tiene puntaje bajo y confianza alta, puede descartarse con mayor seguridad.

---

## 12. Uso en la Matriz de Oportunidades

En la matriz, la Confianza cumple tres funciones:

1. **Auditoría:** permite saber qué tan fundamentado está cada valor.
2. **Priorización:** ayuda a decidir qué nichos requieren más investigación.
3. **Riesgo:** indica dónde una evaluación puede estar basada en datos débiles.

Ejemplo:

| Nicho | Score | Confianza Promedio | Interpretación |
|---|---:|---|---|
| Nicho A | 4.2 | Baja | Prometedor, pero muy incierto. Requiere investigación. |
| Nicho B | 3.6 | Alta | Interesante, con evaluación bastante sólida. |
| Nicho C | 2.4 | Alta | Poco atractivo y probablemente descartable. |

---

## 13. Uso futuro en la plataforma

En la futura plataforma Smart Imports, Confianza debería modelarse como atributo independiente del Valor.

Posible modelo conceptual:

```text
Evaluation
  ├── nicheId
  ├── criterionId
  ├── value
  ├── confidence
  ├── justification
  ├── evidenceIds
  ├── nextAction
  └── status
```

La plataforma podría usar Confianza para:

- Filtrar evaluaciones débiles.
- Detectar criterios que requieren más evidencia.
- Mostrar alertas.
- Priorizar tareas de investigación.
- Calcular un score ajustado por confianza.
- Guiar agentes IA en próximas acciones.

---

## 14. Posible evolución: Score ajustado por Confianza

En una etapa posterior, Smart Imports podría calcular dos scores:

| Score | Descripción |
|---|---|
| Score Ponderado | Promedio ponderado de los valores asignados. |
| Score Ajustado por Confianza | Score que penaliza evaluaciones con baja confianza. |

Ejemplo conceptual:

```text
Score Ponderado = 4.1
Confianza Promedio = Baja
Score Ajustado = 3.2
```

Esto evitaría que un nicho parezca excelente sólo porque asignamos valores altos sin evidencia suficiente.

Esta funcionalidad no es obligatoria en la etapa inicial, pero debe considerarse para la futura plataforma.

---

## 15. Preguntas abiertas

- ¿La Confianza debe medirse como Baja / Media / Alta o con escala numérica?
- ¿Debe convertirse internamente en valores 1, 2 y 3 para cálculos?
- ¿Debe existir un score ajustado por confianza desde la planilla inicial?
- ¿Qué evidencia mínima exige cada criterio para alcanzar Confianza Alta?
- ¿Debe variar la definición de Confianza según el criterio evaluado?

---

## 16. Próximas acciones

1. Incorporar este documento dentro de `docs/02-business-intelligence-manual/criteria/`.
2. Crear el índice `docs/02-business-intelligence-manual/README.md`.
3. Crear el protocolo del criterio Demanda.
4. Aplicar el protocolo a Energía solar portátil.
5. Revisar si la planilla actual necesita una columna `Estado` para evaluaciones preliminares.

---

## 17. Related Documents

- `si-doc-001-documentation-standards.md`
- `si-vision-001-smart-imports-vision.md`
- `si-decision-004-use-evidence-before-intuition.md`

---

## 18. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Versión inicial del documento de Confianza en evaluaciones. |
