---
id: si-agent-001
title: Smart Imports Intelligence Engine
description: Visión funcional, principios de diseño, módulos y requisitos observados del motor de inteligencia comercial de Smart Imports.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-07-17
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
  - si-research-001
  - si-decision-006
  - si-decision-007
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

Este documento define la visión funcional inicial del **Smart Imports Intelligence Engine**, el futuro motor de inteligencia comercial que dará soporte a:

- Descubrimiento de oportunidades.
- Investigación de nichos y productos.
- Gestión de evidencias.
- Selección y seguimiento de proveedores.
- Negociación.
- Cálculo económico.
- Scoring y recomendación.
- Conservación y reutilización del conocimiento.

No define todavía una arquitectura técnica definitiva. Su propósito es fijar capacidades, principios, módulos iniciales y requisitos descubiertos mediante trabajo real.

---

## 2. Problema que debe resolver

La investigación comercial suele quedar distribuida entre marketplaces, sitios de proveedores, chats, emails, PDFs, planillas, capturas y cálculos independientes.

Esto genera:

- Duplicación.
- Pérdida de contexto.
- Inconsistencias.
- Claims no verificados.
- Confusión entre datos del producto y del vendedor.
- Dificultad para comparar alternativas.
- Decisiones basadas en información incompleta.

El motor deberá convertir fuentes dispersas en una secuencia trazable:

```text
Fuentes
  ↓
Datos normalizados
  ↓
Evidencias
  ↓
Evaluaciones
  ↓
Score + confianza
  ↓
Recomendación explicada
  ↓
Decisión humana
```

---

## 3. Visión

El Smart Imports Intelligence Engine será una plataforma interna capaz de:

1. Descubrir oportunidades comerciales.
2. Investigar nichos y subcategorías.
3. Normalizar información de distintas fuentes.
4. Construir evidencia trazable.
5. Evaluar con criterios consistentes.
6. Reducir errores operativos.
7. Acelerar consultas y negociaciones.
8. Proteger el capital mediante decisiones informadas.
9. Conservar conocimiento entre personas, chats y ciclos.
10. Mejorar con cada nicho investigado.
11. Recomendar próximas acciones sin sustituir aprobación humana.

---

## 4. Capacidades objetivo

### 4.1 Investigación asistida

- Buscar señales de demanda.
- Detectar competidores y publicaciones relevantes.
- Identificar subcategorías y productos base.
- Comparar fuentes locales y externas.
- Registrar hallazgos con trazabilidad.

### 4.2 Monitoreo y extracción

- Extraer datos desde páginas, PDFs, imágenes, emails y mensajes.
- Monitorear precios, disponibilidad y cambios.
- Distinguir hechos, inferencias y faltantes.

### 4.3 Normalización y evidencias

- Evitar IDs duplicados.
- Resolver relaciones entre fuentes, productos y evaluaciones.
- Identificar productos clonados o equivalentes.
- Conservar fuente, fecha, fragmento y confianza.

### 4.4 Scoring y confianza

- Aplicar criterios y pesos del Business Intelligence Manual.
- Calcular score parcial y final.
- Calcular confianza.
- Detectar criterios pendientes.
- Explicar cada evaluación.

### 4.5 Negociación asistida

- Comparar FOB público, cotizado y objetivo.
- Detectar espacio de negociación.
- Sugerir contraofertas y repreguntas.
- Registrar historial y estado.

### 4.6 Margen y FOB objetivo

- Estimar costo importado.
- Simular escenarios por cantidad.
- Calcular margen, ROI y sensibilidad.
- Determinar FOB máximo aceptable.

### 4.7 Gestión documental y RAG

- Organizar datasheets, cotizaciones, certificados y catálogos.
- Vincular documentos con proveedor, producto y evaluación.
- Recuperar antecedentes y contradicciones.
- Responder utilizando evidencia interna citada.

### 4.8 RFQ contextual

- Adaptar RFQ al tipo de producto.
- Considerar requisitos técnicos, packing y FOB objetivo.
- Evitar repetir preguntas ya respondidas.
- Crear follow-ups desde faltantes reales.

### 4.9 Seguimiento de conversaciones

- Registrar estado de cada proveedor.
- Detectar mensajes pendientes e incompletos.
- Recomendar siguiente acción.

### 4.10 Recomendación de compra

- Comparar producto, proveedor, margen, riesgo y confianza.
- Recomendar avanzar, negociar, pedir muestra, observar o descartar.
- Mantener aprobación humana.

---

## 5. Requisitos descubiertos durante la selección del Nicho 2

La segunda ejecución metodológica reveló capacidades adicionales que deberán incorporarse progresivamente.

### 5.1 Niche Candidate Normalizer

Debe detectar:

- Nichos duplicados.
- Productos individuales presentados como nichos.
- Candidatos demasiado amplios.
- Subcategorías que pertenecen a un nicho superior.
- Solapamientos por cliente, problema o familia de productos.

Ejemplo:

```text
Lavandería compacta
+ Organización del baño
+ Cocina compacta
        ↓
Problema común: falta de espacio
        ↓
Organización modular para espacios pequeños
```

### 5.2 Marketplace Evidence Analyzer

Debe separar correctamente:

- Ventas visibles del producto.
- Opiniones y calificación del producto.
- Reputación y ventas del vendedor.
- Datos de una ficha consolidada frente a una publicación individual.
- Información explícita frente a inferencias.

Este requisito surgió al comprobar que algunos marketplaces muestran métricas del vendedor cerca de datos del producto.

### 5.3 Claims Validation Gate

Debe identificar términos no confirmados, por ejemplo:

```text
Waterproof
Premium
Heavy duty
Compression
Food grade
BPA free
Indestructible
Antiansiedad
```

Cada claim deberá clasificarse como:

- Declarado por el proveedor.
- Respaldado documentalmente.
- Validado mediante muestra o ensayo.
- No confirmado.
- No utilizable comercialmente.

### 5.4 Product Quality Specification Builder

Debe convertir descripciones genéricas en atributos medibles para RFQ, comparación e inspección.

Para Viaje organizado, por ejemplo:

- Material y gramaje.
- Tipo de cierre.
- Costuras.
- Medidas.
- Peso.
- Solidez de color.
- Resistencia del asa.
- Compresión verificable.
- Packing y CBM.

### 5.5 Compatibility and Dimension Recommender

Deberá poder relacionar medidas de productos con contextos de uso.

Primer caso posible:

- Dimensiones internas de una valija.
- Dimensiones de packing cubes.
- Configuración sugerida.
- Capacidad y compatibilidad con carry-on.

---

## 6. Principios de diseño

### SI-ENGINE-P001 — Human in the loop

El motor no autorizará compras, pagos o compromisos comerciales sin aprobación humana.

### SI-ENGINE-P002 — Evidence before recommendation

Toda recomendación debe poder rastrearse hasta evidencia identificable.

### SI-ENGINE-P003 — Confidence is first-class data

Un dato sin confianza no debe tratarse igual que un dato confirmado.

### SI-ENGINE-P004 — Manual first, automation second

No se automatizará un proceso que todavía no haya sido comprendido manualmente.

### SI-ENGINE-P005 — Incremental delivery

Cada módulo debe resolver un problema real antes de ampliar alcance.

### SI-ENGINE-P006 — Structured outputs

Las salidas deben ser legibles por personas y máquinas.

### SI-ENGINE-P007 — Source preservation

El valor normalizado no reemplaza a la fuente original.

### SI-ENGINE-P008 — Reversibility

Se priorizarán componentes desacoplados y decisiones técnicas reversibles.

### SI-ENGINE-P009 — No automation theater

Toda automatización debe reducir tiempo, errores o riesgo.

### SI-ENGINE-P010 — Claims are not facts

Un claim comercial no se transformará en atributo confirmado sin evidencia suficiente.

---

## 7. Estrategia de construcción

```text
Primera ejecución → descubrir el proceso
Segunda ejecución → estandarizarlo
Tercera ejecución → automatizarlo
```

- **Energía Solar Portátil** representa la primera ejecución integral.
- **Viaje organizado y equipaje funcional** representa la segunda ejecución y deberá validar repetibilidad, tiempos y reglas.

---

## 8. Módulos iniciales

### MVP 1 — Matrix Validator

Validará:

- Hojas requeridas.
- Nombres y orden de columnas.
- IDs y relaciones.
- Evidencias y evaluaciones.
- Valores permitidos.
- Posibles duplicaciones.

### MVP 2 — Supplier Response Analyzer

Procesará mensajes, PDFs, emails y cotizaciones para obtener datos, faltantes, contradicciones, riesgos y follow-ups.

### MVP 3 — Contextual RFQ Generator

Generará RFQ y repreguntas adaptadas al producto, requisitos y documentación existente.

### MVP 4 — Margin and FOB Engine

Calculará costo importado, margen, ROI, sensibilidad y FOB objetivo.

### MVP 5 — Scoring and Next Action Engine

Generará score, confianza, criterios pendientes y próxima acción explicada.

### Módulos candidatos surgidos del Nicho 2

- Marketplace Evidence Analyzer.
- Niche Candidate Normalizer.
- Claims Validation Gate.
- Product Quality Specification Builder.
- Compatibility and Dimension Recommender.

Su prioridad definitiva dependerá de la fricción medida durante Demanda y Competencia de Viaje organizado.

---

## 9. Alcance excluido inicialmente

- Scraping masivo sin supervisión.
- Agentes negociando autónomamente.
- Compras automáticas.
- Selección final sin revisión humana.
- Plataforma completa antes de validar módulos.
- Reemplazo inmediato de Google Sheets.

---

## 10. Datos mínimos trazables

| Campo | Propósito |
|---|---|
| Valor normalizado | Dato utilizado por el sistema. |
| Fuente | Origen del dato. |
| Documento o URL | Evidencia primaria. |
| Fecha | Vigencia temporal. |
| Nivel de confianza | Calidad de la evidencia. |
| Fragmento de soporte | Texto o sección que respalda el valor. |
| Estado de revisión | Pendiente, revisado o confirmado. |
| Tipo de dato | Hecho, inferencia, claim o estimación. |

---

## 11. Indicadores de éxito

El motor deberá demostrar que puede:

- Reducir tiempo de procesamiento.
- Reducir duplicaciones y errores.
- Mejorar trazabilidad.
- Detectar contradicciones y claims no confirmados.
- Evitar decisiones prematuras.
- Reutilizar conocimiento entre nichos.
- Producir recomendaciones explicables.

---

## 12. Próximas acciones

1. Especificar e implementar el Matrix Validator.
2. Medir tiempos durante Demanda y Competencia de Viaje organizado.
3. Registrar errores repetitivos del procesamiento de publicaciones.
4. Definir el contrato mínimo del Marketplace Evidence Analyzer.
5. Diseñar el Supplier Response Analyzer después del ciclo solar de cotizaciones.

---

## 13. Documentos relacionados

- [SI-00 — Sprint 0: Foundation](../00-vision/si-00-sprint-0-foundation.md)
- [SI-VISION-001 — Smart Imports Vision](../00-vision/si-vision-001-smart-imports-vision.md)
- [SI-RESEARCH-001 — Niche 2 Selection](../06-research/si-research-001-niche-2-selection.md)
- [SI-RESEARCH-002 — Travel Organization Scope](../06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md)
- [SI-ROADMAP-001 — Pilot Closure, Niche 2 and Engine MVP](../08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-006 — Build the Intelligence Engine Incrementally](../09-decision-log/si-decision-006-build-intelligence-engine-incrementally.md)
- [SI-DECISION-007 — Select Travel Organization as Niche 2](../09-decision-log/si-decision-007-select-travel-organization-as-niche-2.md)

---

## 14. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-16 | Definición inicial de visión, capacidades y primeros MVP. |
| 0.2.0 | 2026-07-17 | Se incorporaron requisitos descubiertos durante la selección y validación del Nicho 2. |
