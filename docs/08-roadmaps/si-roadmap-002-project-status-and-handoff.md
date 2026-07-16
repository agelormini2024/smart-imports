---
id: si-roadmap-002
title: Project Status and Handoff
description: Documento vivo que registra el estado actual, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports en un nuevo chat o sesión.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-07-16
tags:
  - status
  - handoff
  - continuity
  - roadmap
  - project-management
related:
  - si-roadmap-001
  - si-agent-001
  - si-decision-005
  - si-decision-006
audience:
  - founder
  - partner
  - assistant
phase: foundation
---

# SI-ROADMAP-002 — Estado actual y handoff de Smart Imports

> Este documento es el punto de entrada operativo para saber dónde está parado el proyecto.

---

## 1. Propósito

Este es un **documento vivo**. Su función es permitir que Smart Imports pueda retomarse sin depender de la memoria de una persona, un chat o una sesión específica.

Debe responder rápidamente:

- ¿Qué estamos construyendo?
- ¿Qué ya está hecho?
- ¿Qué está en curso?
- ¿Qué está bloqueado?
- ¿Qué esperamos de terceros?
- ¿Cuál es la próxima acción?
- ¿Qué documentos deben leerse para recuperar contexto?

---

## 2. Regla de mantenimiento

Actualizar este documento cuando ocurra alguno de estos eventos:

- Se cierra un criterio.
- Se selecciona o descarta un nicho.
- Llega una cotización relevante.
- Se toma una decisión metodológica.
- Se inicia o finaliza un módulo del Intelligence Engine.
- Cambia la próxima acción principal.
- Se abre un nuevo chat o ciclo de trabajo.

No debe registrar cada conversación menor. Debe mantener el **estado operativo consolidado**.

---

## 3. Snapshot

| Campo | Estado |
|---|---|
| Fecha de corte | 2026-07-16 |
| Fase | Foundation avanzada / validación del método |
| Nichos activos | 1 activo y 1 en preparación |
| Piloto activo | Energía Solar Portátil |
| Nicho 2 | Pendiente de selección |
| Intelligence Engine | Visión definida; MVP 1 pendiente de implementación |
| Bloqueo principal | Respuestas y documentación de proveedores |
| Próxima acción principal | Procesar RFQ solares y crear lista larga del Nicho 2 |

---

## 4. Visión vigente

Smart Imports no se define como una importadora tradicional.

Su objetivo es construir una empresa que combine:

- Inteligencia comercial.
- Importación estratégica.
- E-commerce propio.
- Construcción de marca.
- Automatización.
- IA y agentes.
- Software propio.

El activo principal de largo plazo será el **Smart Imports Intelligence Engine**.

---

## 5. Metodología vigente

```text
Nicho
  ↓
Subcategorías
  ↓
Fuentes
  ↓
Productos base
  ↓
Evidencias
  ↓
Evaluaciones
  ↓
Score + confianza
  ↓
Proveedores y RFQ
  ↓
Margen + facilidad de importación
  ↓
Decisión
```

Principios activos:

- Primero entender, después invertir.
- Evaluar nichos antes que productos.
- Evidencia antes que intuición.
- Google Sheets es la herramienta operativa inicial.
- GitHub es la fuente documental de verdad.
- Precio público de Alibaba no equivale a FOB negociado.
- La decisión final requiere trazabilidad y confianza.

---

## 6. Caso piloto — Energía Solar Portátil

### 6.1 Alcance incluido

- Kits solares portátiles.
- Ventiladores solares.
- Power banks solares.
- Paneles solares portátiles pequeños y medianos.

### 6.2 Alcance excluido

- Generadores solares.
- Power stations.
- Sistemas solares completos.
- Soluciones de mayor escala.

Estos productos quedan en backlog para un nicho separado.

### 6.3 Criterios

| Criterio | Score | Confianza | Estado |
|---|---:|---|---|
| Demanda | 4 | Alta | Revisado |
| Competencia | 3 | Alta | Revisado |
| Margen Potencial | 3 preliminar | Baja/Media | En evaluación |
| Facilidad de Importación | 3 preliminar | Baja/Media | En evaluación |
| Potencial de Marca | 4 | Media | Revisado preliminarmente |
| Venta Impulsiva | 3 | Media | Revisado preliminarmente |
| Recompra | 2 | Alta | Revisado |
| Potencial IA | 4 | Alta | Revisado |
| Potencial Automatización | 5 | Alta | Revisado |
| Afinidad Personal | 5 | Alta | Revisado |

Los valores de Margen e Importación no deben considerarse definitivos hasta procesar RFQ y documentación.

---

## 7. Estado de proveedores solares

### 7.1 Kits AT-999 y DT-138 — DAT / Yiwu HaoYe

Estado: **esperando respuesta**.

Hallazgo principal:

- La cotización de AT-999 informó batería sellada de plomo-ácido 6V 4500mAh.
- Smart Imports definió batería de litio como condición excluyente para esta evaluación.

Última acción:

- Se pidió versión de litio para AT-999 y DT-138.
- Se pidieron MSDS, UN38.3, FOB por cantidad, EXW, packing y comparación técnica.
- Se comunicó un objetivo FOB aproximado de USD 7,20 a 7,60 para 1000–3000 unidades, sujeto a especificaciones.

Próxima acción:

- Validar si existe variante de litio.
- Comparar FOB con FOB objetivo.
- Descartar la variante de plomo.

### 7.2 Power banks — Shenzhen Nulike Technology

Estado: **esperando información y cotización**.

Modelos solicitados:

- 30.000 mAh.
- 50.000 mAh.
- 60.000 mAh como referencia opcional.

Se solicitó:

- Capacidad real y nominal.
- Tipo de celda.
- Voltaje y Wh.
- Peso por modelo.
- FOB, EXW, MOQ y packing.
- MSDS y UN38.3.
- Certificaciones y HS Code.

Próxima acción:

- Validar claims de capacidad.
- Comparar peso y energía.
- Evitar modelos de alta capacidad sin documentación técnica suficiente.

### 7.3 Ventiladores — Shenzhen Ani Technology

Estado: **esperando cotización y fichas técnicas**.

Modelos solicitados:

- LD-008.
- LD-6008.
- LD-2512.
- LD-633.
- LD-312 sólo si existe versión con batería de litio.

Criterio excluyente:

- No avanzar con baterías de plomo-ácido.

Próxima acción:

- Comparar variantes 8", 12" y premium LiFePO4.
- Revisar FOB, autonomía, panel incluido, packing y documentación de batería.

### 7.4 Paneles plegables

Estado: **RFQ enviados; esperando respuestas completas**.

Referencias principales investigadas:

- Panel plegable genérico ETFE 30W/40W/50W.
- Proveedor Shine Solar como referencia competitiva.
- Proveedor MWISH como referencia de mayor precio.

Próxima acción:

- Obtener FOB exacto por potencia y cantidad.
- Confirmar USB-A, USB-C PD, QC3.0 y DC.
- Confirmar ETFE, medidas, peso, waterproof limitations, packing y certificaciones.

---

## 8. Nicho 2

Estado: **preparación**.

Objetivo inmediato:

1. Crear una lista larga de 8 a 12 nichos.
2. Aplicar filtros excluyentes.
3. Realizar screening rápido.
4. Seleccionar tres finalistas.
5. Elegir un nicho que contraste con Energía Solar Portátil.

Preferencias:

- Sin batería o con menor complejidad.
- Volumen moderado.
- Ticket medio.
- Familia de productos.
- Potencial de marca.
- Demanda observable.

No iniciar todavía RFQ del Nicho 2.

---

## 9. Intelligence Engine

### 9.1 Estado

- Nombre definido: Smart Imports Intelligence Engine.
- Visión y capacidades iniciales documentadas.
- Estrategia: construcción incremental a partir de procesos manuales validados.
- Primer MVP seleccionado: Matrix Validator.

### 9.2 MVP 1 — Matrix Validator

Estado: **pendiente de especificación técnica e implementación**.

Alcance inicial:

- Hojas y columnas.
- IDs.
- Relaciones.
- Evidencias.
- Evaluaciones.
- Duplicaciones.
- Valores permitidos.
- Reporte de errores y advertencias.

Stack preliminar:

```text
TypeScript + Node.js + Zod + ExcelJS + CLI + tests
```

### 9.3 Backlog priorizado

1. Matrix Validator.
2. Supplier Response Analyzer.
3. Contextual RFQ Generator.
4. Margin and FOB Engine.
5. Scoring and Next Action Engine.
6. RAG de proveedores y documentos.
7. Monitoreo y scraping asistido.

---

## 10. Trabajo completado

- Sprint 0 y visión estratégica.
- Estructura documental.
- Business Intelligence Manual inicial.
- Criterios Demanda, Competencia y Margen Potencial documentados.
- Procedimiento de evidencias.
- Procedimiento de RFQ y screening de margen.
- Matriz operativa por capas.
- Demanda y Competencia del piloto.
- Criterios estratégicos preliminares.
- Decision Log hasta SI-DECISION-005.
- Documento ejecutivo para socio e inversores.
- RFQ iniciales a proveedores solares.
- Conceptualización del Intelligence Engine.

---

## 11. Trabajo en curso

- RFQ y negociación de kits.
- RFQ de ventiladores.
- RFQ de power banks.
- RFQ de paneles.
- Margen Potencial.
- Facilidad de Importación.
- Preparación del Nicho 2.
- Especificación inicial del Matrix Validator.

---

## 12. Bloqueos y dependencias

| Bloqueo | Dependencia | Acción mientras se espera |
|---|---|---|
| Margen definitivo | FOB, packing y logística | Seleccionar Nicho 2 y diseñar validador |
| Facilidad de Importación | Batería, certificados y HS Code | Documentar requisitos y riesgos |
| Ranking de proveedores | Respuestas comparables | Mantener estructura de evaluación |
| Decisión de muestras | Precio y documentación | No comprometer capital todavía |

---

## 13. Próximas acciones ordenadas

### Prioridad 1

Procesar cada respuesta de proveedor con el mismo flujo:

```text
Extraer → validar → detectar faltantes → repreguntar → negociar → registrar → recalcular
```

### Prioridad 2

Crear la lista larga de candidatos para el Nicho 2.

### Prioridad 3

Diseñar la tabla de screening rápido.

### Prioridad 4

Especificar entradas, salidas y reglas del Matrix Validator.

### Prioridad 5

Cerrar el piloto solar y documentar retrospectiva.

---

## 14. Protocolo para abrir un nuevo chat

En un nuevo chat, compartir el repositorio y pedir que se revisen primero estos documentos:

1. `README.md`
2. `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md`
3. `docs/08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md`
4. `docs/05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md`
5. Documento de investigación específico del nicho en curso.

Prompt sugerido:

```text
Estamos continuando el proyecto Smart Imports.

El repositorio es:
https://github.com/agelormini2024/smart-imports

Antes de proponer cambios o continuar el trabajo, revisá especialmente:

- README.md
- docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md
- docs/08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md
- docs/05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md

Tomá el documento de estado como punto de entrada operativo y la documentación del repo como fuente de verdad. No modifiques la metodología, los IDs ni la estructura de la matriz sin detectar y explicar primero el impacto.
```

---

## 15. Checklist de cierre de sesión

Antes de cerrar una etapa importante:

- [ ] Actualizar fecha de corte.
- [ ] Registrar trabajo completado.
- [ ] Actualizar trabajo en curso.
- [ ] Actualizar bloqueos.
- [ ] Definir próxima acción principal.
- [ ] Registrar decisiones nuevas.
- [ ] Vincular documentos o archivos creados.
- [ ] Verificar que el README o índices relevantes apunten a los documentos vigentes.

---

## 16. Documentos relacionados

- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-ROADMAP-001 — Pilot Closure, Niche 2 and Engine MVP](./si-roadmap-001-pilot-closure-niche-2-engine-mvp.md)
- [SI-DECISION-005 — Portable Solar Pilot Scope](../09-decision-log/si-decision-005-portable-solar-pilot-scope.md)
- [SI-DECISION-006 — Build the Intelligence Engine Incrementally](../09-decision-log/si-decision-006-build-intelligence-engine-incrementally.md)

---

## 17. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-16 | Snapshot inicial, protocolo de actualización y handoff para nuevas sesiones. |
