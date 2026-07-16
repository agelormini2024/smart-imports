---
id: si-agent-001
title: Smart Imports Intelligence Engine
description: Visión funcional y principios de diseño del motor de inteligencia comercial de Smart Imports.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-07-16
tags:
  - intelligence-engine
  - ai-agents
  - automation
  - business-intelligence
  - platform
related:
  - si-00
  - si-vision-001
  - si-roadmap-001
  - si-roadmap-002
  - si-decision-006
audience:
  - founder
  - partner
  - developer
phase: foundation
---

# SI-AGENT-001 — Smart Imports Intelligence Engine

> El activo más importante de Smart Imports no será una lista de productos: será el sistema que permita descubrir, evaluar y ejecutar oportunidades comerciales de manera repetible.

---

## 1. Propósito

Este documento define la visión inicial del **Smart Imports Intelligence Engine**, el futuro motor de inteligencia comercial que dará soporte a la investigación de nichos, la evaluación de productos, la selección de proveedores, la negociación, el cálculo económico y la toma de decisiones.

No describe todavía una arquitectura técnica definitiva. Su objetivo es fijar:

- Qué problema debe resolver el motor.
- Qué capacidades deberá desarrollar.
- Qué principios deben guiar su construcción.
- Qué partes se construirán primero.
- Qué decisiones continuarán bajo control humano.

---

## 2. Problema que debe resolver

La investigación comercial suele quedar distribuida entre:

- Marketplaces.
- Sitios de proveedores.
- Chats.
- Emails.
- PDFs.
- Planillas.
- Capturas de pantalla.
- Cálculos independientes.
- Opiniones difíciles de rastrear.

Esto genera problemas de consistencia, duplicación, pérdida de contexto y decisiones basadas en información incompleta.

El Intelligence Engine deberá convertir esas fuentes dispersas en una secuencia trazable:

```text
Fuentes
  ↓
Datos normalizados
  ↓
Evidencias
  ↓
Evaluaciones
  ↓
Scoring y confianza
  ↓
Recomendación
  ↓
Decisión humana
```

---

## 3. Visión

El Smart Imports Intelligence Engine será una plataforma interna capaz de ayudar a Smart Imports a:

1. Descubrir oportunidades comerciales.
2. Investigar nichos y subcategorías.
3. Normalizar información proveniente de distintas fuentes.
4. Construir evidencia trazable.
5. Evaluar oportunidades con criterios consistentes.
6. Reducir errores operativos.
7. Acelerar negociaciones con proveedores.
8. Proteger el capital mediante decisiones informadas.
9. Conservar conocimiento entre personas, chats y ciclos de investigación.
10. Mejorar progresivamente con cada nicho investigado.

---

## 4. Capacidades objetivo

### 4.1 Investigación asistida

- Buscar señales de demanda.
- Detectar competidores y publicaciones relevantes.
- Identificar subcategorías y productos base.
- Comparar fuentes locales y externas.
- Registrar hallazgos con trazabilidad.

### 4.2 Monitoreo y extracción de datos

- Monitorear publicaciones, precios y disponibilidad.
- Extraer datos desde páginas, PDFs, imágenes, emails y mensajes.
- Detectar cambios relevantes.
- Distinguir hechos, inferencias y datos faltantes.

### 4.3 Normalización y gestión de evidencias

- Evitar IDs duplicados.
- Resolver relaciones entre fuentes, productos y evaluaciones.
- Identificar productos clonados o equivalentes.
- Conservar la fuente, fecha y nivel de confianza de cada dato.

### 4.4 Scoring y confianza

- Aplicar criterios y pesos definidos en el Business Intelligence Manual.
- Calcular score parcial y final.
- Calcular confianza.
- Detectar criterios pendientes.
- Explicar por qué se asignó cada evaluación.

### 4.5 Negociación asistida

- Comparar FOB público, FOB cotizado y FOB objetivo.
- Detectar espacio de negociación.
- Sugerir contraofertas.
- Proponer repreguntas específicas.
- Registrar el historial de negociación.

### 4.6 Cálculo de margen y FOB objetivo

- Estimar costo importado.
- Simular escenarios por cantidad.
- Calcular margen unitario, margen porcentual y ROI.
- Determinar FOB máximo aceptable.
- Detectar sensibilidad a logística, canal y tipo de cambio.

### 4.7 Gestión documental

- Organizar datasheets, cotizaciones, certificados y catálogos.
- Vincular documentos con proveedor, producto y evaluación.
- Evitar que la información quede aislada en chats o emails.

### 4.8 Knowledge Base y RAG

- Consultar antecedentes de proveedores y productos.
- Recuperar cotizaciones anteriores.
- Comparar contradicciones entre documentos.
- Responder utilizando evidencia interna citada.

### 4.9 Generación contextual de RFQ

- Generar pedidos de cotización según tipo de producto.
- Adaptar preguntas a baterías, certificaciones, packing y logística.
- Evitar repetir preguntas ya respondidas.
- Generar follow-ups a partir de faltantes reales.

### 4.10 Seguimiento de conversaciones

- Registrar el estado de cada proveedor.
- Identificar mensajes pendientes.
- Detectar respuestas incompletas.
- Recomendar la siguiente acción.

### 4.11 Recomendación de compra

- Comparar producto, proveedor, margen, riesgo y confianza.
- Recomendar: avanzar, negociar, pedir muestra, observar o descartar.
- Explicar la recomendación.
- Mantener la decisión final bajo aprobación humana.

---

## 5. Principios de diseño

### SI-ENGINE-P001 — Human in the loop

El motor asistirá decisiones, pero no autorizará compras, pagos o compromisos comerciales sin aprobación humana.

### SI-ENGINE-P002 — Evidence before recommendation

Toda recomendación debe poder rastrearse hasta evidencia identificable.

### SI-ENGINE-P003 — Confidence is first-class data

Un dato sin nivel de confianza no debe tratarse igual que un dato validado por documentación formal.

### SI-ENGINE-P004 — Manual first, automation second

No se automatizará un proceso que todavía no haya sido comprendido mediante ejecución manual.

### SI-ENGINE-P005 — Incremental delivery

Cada módulo debe resolver un problema operativo real antes de ampliar alcance.

### SI-ENGINE-P006 — Structured outputs

Las salidas deben ser legibles por personas y máquinas.

### SI-ENGINE-P007 — Source preservation

El valor normalizado no reemplaza a la fuente original. Ambos deben conservarse.

### SI-ENGINE-P008 — Reversibility

Durante la etapa inicial se priorizarán decisiones técnicas reversibles y componentes desacoplados.

### SI-ENGINE-P009 — No automation theater

No se construirá una automatización únicamente porque sea técnicamente atractiva. Debe reducir tiempo, errores o riesgo.

---

## 6. Estrategia de construcción

Se seguirá esta regla:

```text
Primera ejecución  → descubrir el proceso
Segunda ejecución  → estandarizarlo
Tercera ejecución  → automatizarlo
```

El piloto **Energía Solar Portátil** representa la primera ejecución integral.

El **Nicho 2** deberá servir para:

- Validar qué partes del método son realmente repetibles.
- Identificar datos innecesarios o faltantes.
- Medir tiempos.
- Detectar errores recurrentes.
- Seleccionar automatizaciones con impacto comprobable.

---

## 7. Primeros módulos

### MVP 1 — Matrix Validator

Validará archivos XLSX antes de incorporarlos a la matriz.

Validaciones iniciales:

- Nombres y orden de columnas.
- IDs primarios duplicados.
- Formatos de IDs.
- Relaciones inexistentes.
- Evidencias sin fuente.
- Evaluaciones sin evidencia.
- Productos base posiblemente duplicados.
- Valores fuera de escala.
- Estados, criterios y confianzas no reconocidos.

Salida:

```text
Resultado general
Errores bloqueantes
Advertencias
Filas afectadas
Correcciones recomendadas
```

### MVP 2 — Supplier Response Analyzer

Procesará mensajes, PDFs, emails y cotizaciones de proveedores.

Salida esperada:

```text
Datos recibidos
Datos faltantes
Contradicciones
Riesgos
Condiciones excluyentes
FOB por cantidad
Packing y logística
Certificaciones
Repregunta sugerida
Contraoferta sugerida
Filas estructuradas para la matriz
```

### MVP 3 — Contextual RFQ Generator

Generará RFQ y follow-ups adaptados al producto, documentación existente, requisitos técnicos y FOB objetivo.

### MVP 4 — Margin and FOB Engine

Calculará costo importado, margen, ROI, sensibilidad y FOB objetivo.

### MVP 5 — Scoring and Next Action Engine

Generará score, confianza, criterios pendientes y próxima acción explicada.

---

## 8. Alcance excluido inicialmente

No forma parte de los primeros MVP:

- Scraping masivo sin supervisión.
- Agentes negociando de forma autónoma.
- Compras automáticas.
- Selección final de productos sin revisión humana.
- Arquitectura de plataforma completa antes de validar módulos.
- Reemplazo inmediato de Google Sheets.

---

## 9. Datos mínimos trazables

Cada dato relevante debería poder conservar:

| Campo | Propósito |
|---|---|
| Valor normalizado | Dato utilizado por el sistema |
| Fuente | Origen del dato |
| Documento o URL | Evidencia primaria |
| Fecha | Vigencia temporal |
| Nivel de confianza | Calidad de la evidencia |
| Fragmento de soporte | Texto o sección que respalda el valor |
| Estado de revisión | Pendiente, revisado o confirmado |

---

## 10. Indicadores de éxito

El Intelligence Engine deberá demostrar que puede:

- Reducir tiempo de procesamiento.
- Reducir duplicaciones y errores.
- Mejorar trazabilidad.
- Detectar contradicciones.
- Evitar decisiones prematuras.
- Reutilizar conocimiento entre nichos.
- Producir recomendaciones explicables.

---

## 11. Próximas acciones

1. Construir el Matrix Validator.
2. Utilizar el Nicho 2 para validar repetibilidad.
3. Medir tiempos manuales antes de automatizar.
4. Definir el modelo estructurado de respuesta de proveedores.
5. Diseñar el Supplier Response Analyzer después de cerrar el primer ciclo de cotizaciones solares.

---

## 12. Documentos relacionados

- [SI-00 — Sprint 0: Foundation](../00-vision/si-00-sprint-0-foundation.md)
- [SI-VISION-001 — Smart Imports Vision](../00-vision/si-vision-001-smart-imports-vision.md)
- [SI-ROADMAP-001 — Pilot Closure, Niche 2 and Engine MVP](../08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-006 — Build the Intelligence Engine Incrementally](../09-decision-log/si-decision-006-build-intelligence-engine-incrementally.md)

---

## 13. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-16 | Definición inicial de visión, capacidades, principios y primeros MVP del Intelligence Engine. |
