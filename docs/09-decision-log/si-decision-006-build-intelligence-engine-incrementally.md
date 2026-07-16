---
id: si-decision-006
title: Build the Intelligence Engine Incrementally
description: Decisión de construir el Smart Imports Intelligence Engine por módulos, a partir de procesos manuales validados en investigaciones reales.
version: 1.0.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-07-16
tags:
  - decision
  - intelligence-engine
  - automation
  - ai-agents
  - incremental-development
related:
  - si-agent-001
  - si-roadmap-001
  - si-roadmap-002
phase: foundation
---

# SI-DECISION-006 — Build the Intelligence Engine Incrementally

## 1. Contexto

Durante el piloto **Energía Solar Portátil**, Smart Imports comenzó a desarrollar una metodología para:

- Investigar demanda y competencia.
- Normalizar fuentes y productos.
- Construir evidencias.
- Evaluar criterios.
- Consultar proveedores.
- Calcular FOB objetivo y margen.
- Preparar repreguntas y negociaciones.

A medida que el proceso avanzó, se identificó que el principal activo de largo plazo no será una lista de productos ni una planilla, sino un motor de inteligencia comercial capaz de reutilizar el conocimiento y asistir decisiones.

Al mismo tiempo, intentar construir una plataforma completa demasiado pronto podría producir software basado en supuestos todavía no validados.

---

## 2. Decisión

Smart Imports decide construir el **Smart Imports Intelligence Engine** de forma incremental y guiada por procesos reales.

Se aplicará la siguiente secuencia:

```text
Primera ejecución  → descubrir el proceso
Segunda ejecución  → estandarizarlo
Tercera ejecución  → automatizarlo
```

La construcción comenzará con módulos internos pequeños.

Primer módulo seleccionado:

```text
Matrix Validator
```

El segundo nicho será utilizado para validar qué partes de la metodología son realmente repetibles antes de automatizarlas.

---

## 3. Justificación

### 3.1 Reduce riesgo de construir el sistema equivocado

El método todavía está evolucionando. Automatizar demasiado pronto podría fijar estructuras incorrectas.

### 3.2 Prioriza utilidad real

Cada módulo deberá resolver un problema observado:

- Errores de IDs.
- Relaciones inconsistentes.
- Información faltante.
- Duplicaciones.
- Procesamiento repetitivo.
- Pérdida de trazabilidad.

### 3.3 Mantiene flexibilidad

Módulos pequeños y desacoplados permiten corregir la metodología sin reescribir toda una plataforma.

### 3.4 Produce aprendizaje acumulativo

Cada nicho investigado deberá mejorar simultáneamente:

- El conocimiento comercial.
- El Business Intelligence Manual.
- La matriz.
- El backlog técnico.
- Los módulos del Intelligence Engine.

### 3.5 Protege el capital

La automatización se utilizará primero para mejorar calidad y reducir errores, no para acelerar compras prematuras.

---

## 4. Alternativas consideradas

### 4.1 Construir inmediatamente una plataforma web completa

Descartada por alto riesgo de sobredesarrollo antes de validar la metodología.

### 4.2 Mantener todo manual hasta encontrar un producto ganador

Descartada porque prolongaría errores repetitivos y no desarrollaría el activo tecnológico diferencial.

### 4.3 Automatizar primero scraping masivo

Postergada porque la normalización, deduplicación y trazabilidad todavía necesitan mayor madurez.

### 4.4 Usar agentes autónomos desde el inicio

Descartada para la etapa actual por riesgo comercial y falta de controles suficientes.

---

## 5. Consecuencias

- El proyecto tendrá una línea técnica paralela a la investigación comercial.
- No se desarrollarán módulos sin caso de uso validado.
- El Matrix Validator será el primer MVP.
- El Nicho 2 funcionará como segunda ejecución metodológica.
- Las decisiones comerciales sensibles mantendrán aprobación humana.
- Se medirán tiempos y errores para priorizar automatizaciones.
- La futura plataforma se construirá sobre una metodología documentada, no como réplica directa de Google Sheets.

---

## 6. Impacto en el proyecto

### Estrategia

El Intelligence Engine se reconoce como el activo principal de largo plazo.

### Investigación

Cada investigación deberá producir aprendizajes reutilizables.

### Tecnología

Se priorizarán componentes modulares, trazables y reversibles.

### IA

La IA asistirá extracción, análisis y recomendación, pero no reemplazará aprobación humana.

### Roadmap

Se incorporan tres líneas paralelas:

- Cierre del piloto solar.
- Selección del Nicho 2.
- Construcción del MVP técnico.

---

## 7. Documentos relacionados

- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-ROADMAP-001 — Pilot Closure, Niche 2 and Engine MVP](../08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

---

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-16 | Decisión inicial de construcción incremental del Intelligence Engine. |
