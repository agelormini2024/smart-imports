---
id: si-roadmap-001
title: Pilot Closure, Niche 2 and Intelligence Engine MVP Roadmap
description: Plan coordinado para cerrar Energía Solar Portátil, seleccionar el segundo nicho y construir el primer MVP del Intelligence Engine.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-07-16
tags:
  - roadmap
  - portable-solar-energy
  - niche-selection
  - intelligence-engine
  - mvp
related:
  - si-agent-001
  - si-roadmap-002
  - si-decision-005
  - si-decision-006
audience:
  - founder
  - partner
  - developer
phase: foundation
---

# SI-ROADMAP-001 — Cierre del piloto, Nicho 2 e Intelligence Engine MVP

> Cada nuevo nicho debe producir dos resultados: conocimiento comercial y una pieza reutilizable del sistema.

---

## 1. Propósito

Este roadmap coordina tres líneas de trabajo paralelas:

```text
Línea A — Cerrar el piloto Energía Solar Portátil
Línea B — Seleccionar y comenzar el Nicho 2
Línea C — Construir el primer MVP del Intelligence Engine
```

El objetivo es avanzar sin dispersión, validar que la metodología sea reutilizable y comenzar la automatización a partir de problemas reales.

---

## 2. Reglas operativas

1. No mantener más de dos nichos activos simultáneamente.
2. No automatizar procesos que no hayan sido comprendidos manualmente.
3. No avanzar a RFQ del Nicho 2 hasta completar su screening inicial.
4. No forzar una conclusión positiva del piloto solar.
5. Registrar toda decisión relevante en el Decision Log.
6. Actualizar el documento de estado después de cada hito significativo.
7. Mantener aprobación humana para negociaciones, muestras, compras y pagos.

---

## 3. Línea A — Cierre de Energía Solar Portátil

### 3.1 Objetivo

Cerrar los criterios pendientes y producir una decisión fundamentada sobre el nicho y sus subcategorías.

### 3.2 Criterios pendientes

- Margen Potencial.
- Facilidad de Importación.

### 3.3 Proceso por respuesta de proveedor

```text
Proveedor responde
  ↓
Validación técnica
  ↓
Validación comercial
  ↓
Detección de faltantes y contradicciones
  ↓
Comparación contra requisitos excluyentes
  ↓
Comparación FOB vs FOB objetivo
  ↓
Repregunta o contraoferta
  ↓
Actualización de matriz y evidencias
  ↓
Recalcular margen y confianza
```

### 3.4 Datos necesarios para Margen Potencial

- FOB por cantidad.
- EXW.
- MOQ.
- Packing.
- Unidades por caja.
- Peso neto y bruto.
- CBM.
- Lead time.
- Precio de venta posible.
- Costos de canal.
- Costos comerciales.
- Costos de importación.

### 3.5 Datos necesarios para Facilidad de Importación

- Composición.
- Tipo de batería.
- Capacidad y Wh.
- MSDS.
- UN38.3.
- HS Code.
- Certificaciones.
- Tipo de cargador y enchufe.
- Restricciones logísticas.
- Peso y volumen.

### 3.6 Resultado esperado

Cada producto y subcategoría deberá terminar en una de estas acciones:

- Avanzar a muestra.
- Continuar negociando.
- Mantener en observación.
- Descartar producto.
- Descartar subcategoría.
- Reformular el nicho.
- Descartar el nicho.

### 3.7 Entregables

- Scoring definitivo del nicho.
- Ranking de subcategorías.
- Ranking de productos.
- Ranking de proveedores.
- Conclusión del piloto.
- Retrospectiva metodológica.
- Decisión de siguiente acción.

---

## 4. Línea B — Selección del Nicho 2

### 4.1 Objetivo

Seleccionar un segundo nicho mediante un proceso reproducible y utilizarlo para probar la metodología fuera de Energía Solar Portátil.

### 4.2 Perfil preferido

- Sin batería o con menor complejidad técnica.
- Peso y volumen moderados.
- Ticket medio.
- Familia de productos relacionada.
- Potencial de marca propia.
- Demanda observable.
- Diferenciación mediante información, diseño, servicio o software.

### 4.3 Etapa 1 — Lista larga

Generar entre 8 y 12 candidatos.

Cada candidato debe representar una familia de productos, no un único artículo.

### 4.4 Etapa 2 — Filtros excluyentes

Descartar candidatos con:

- Regulación sanitaria o médica compleja.
- Alimentos, suplementos o cosméticos.
- Riesgo alto de responsabilidad.
- Dependencia de marcas o falsificaciones.
- Volumen logístico desproporcionado.
- MOQ incompatible con el capital.
- Posventa técnica excesiva.
- Imposibilidad de construir familia y marca.

### 4.5 Etapa 3 — Screening rápido

Criterios iniciales:

| Criterio | Pregunta principal |
|---|---|
| Demanda observable | ¿Existe interés comercial verificable? |
| Competencia | ¿La categoría está saturada o permite entrada? |
| Facilidad de importación | ¿Tiene barreras razonables para el proyecto? |
| Potencial de marca | ¿Permite construir una propuesta coherente? |
| Margen preliminar | ¿La estructura económica parece viable? |

Duración objetivo: 30 a 60 minutos por candidato.

### 4.6 Etapa 4 — Tres finalistas

Cada ficha finalista deberá incluir:

- Descripción del nicho.
- Problema que resuelve.
- Cliente probable.
- Subcategorías iniciales.
- Señales de demanda.
- Riesgos.
- Razones para continuar.

### 4.7 Etapa 5 — Decisión

Elegir un Nicho 2 que contraste con el piloto solar y permita comprobar si la metodología es generalizable.

### 4.8 Entregables

- Matriz de candidatos.
- Tres fichas finalistas.
- Comparación.
- Decisión documentada.
- Alcance del Nicho 2.

---

## 5. Línea C — Intelligence Engine MVP

### 5.1 Objetivo

Construir una primera utilidad interna que reduzca errores reales sin intentar desarrollar todavía la plataforma completa.

### 5.2 MVP seleccionado

**Matrix Validator**.

### 5.3 Alcance funcional inicial

- Validar hojas requeridas.
- Validar nombres y orden de columnas.
- Detectar IDs duplicados.
- Validar formato de IDs.
- Validar relaciones.
- Detectar evidencias sin fuente.
- Detectar evaluaciones sin soporte.
- Detectar productos base posiblemente duplicados.
- Validar valores de criterios, confianza y estado.
- Generar reporte de errores y advertencias.

### 5.4 Stack preliminar

```text
TypeScript
Node.js
Zod
ExcelJS
CLI
Vitest o Jest
```

### 5.5 Interfaz inicial

```bash
npm run validate -- ./data/smart-imports.xlsx
```

### 5.6 Salida esperada

```text
Validation result: FAILED

Blocking errors: 2
Warnings: 4

- Duplicate ID EVID-0090 in Evidencias row 97
- Missing Producto Base BASE-PB-006 referenced by COT-0008
- Warning: possible duplicate product bases BASE-VENT-001 and BASE-VENT-004
```

### 5.7 Entregables

- Repositorio o módulo inicial.
- Esquemas Zod.
- Reglas de validación.
- Tests.
- Reporte de validación.
- Ejecución contra archivos reales.

---

## 6. Medición de eficiencia

Durante el Nicho 2 se registrarán tiempos aproximados para:

| Actividad | Piloto solar | Nicho 2 |
|---|---:|---:|
| Procesar una publicación | Pendiente de línea base | Por medir |
| Registrar producto base | Pendiente de línea base | Por medir |
| Generar evidencia | Pendiente de línea base | Por medir |
| Evaluar criterio | Pendiente de línea base | Por medir |
| Preparar RFQ | Pendiente de línea base | Por medir |
| Procesar cotización | Pendiente de línea base | Por medir |

El objetivo no es precisión científica, sino detectar las actividades que más tiempo y errores generan.

---

## 7. Roadmap de seis semanas

### Semana 1

- Procesar respuestas de proveedores solares.
- Generar lista larga del Nicho 2.
- Confirmar alcance del Intelligence Engine.
- Especificar reglas del Matrix Validator.

### Semana 2

- Aplicar filtros y screening.
- Elegir tres finalistas.
- Seleccionar Nicho 2.
- Crear estructura inicial del validador.

### Semana 3

- Investigar Demanda del Nicho 2.
- Implementar validación de hojas, columnas e IDs.
- Continuar negociación solar.

### Semana 4

- Investigar Competencia del Nicho 2.
- Implementar relaciones y evidencias.
- Crear tests iniciales.

### Semana 5

- Hacer screening de Margen e Importación del Nicho 2.
- Ejecutar el validador contra archivos reales.
- Corregir falsos positivos.

### Semana 6

- Cerrar o encaminar el piloto solar.
- Comparar ambos nichos.
- Documentar retrospectiva.
- Definir Supplier Response Analyzer.

---

## 8. Tablero inicial

### En curso

- Espera y seguimiento de RFQ solares.
- Preparación de selección del Nicho 2.
- Definición del Matrix Validator.

### Próximo

- Crear lista de 8 a 12 candidatos.
- Diseñar tabla de screening.
- Definir esquema XLSX del validador.

### Bloqueado o esperando

- Cierre de Margen Potencial solar.
- Cierre de Facilidad de Importación solar.

Dependencia: respuestas y documentos de proveedores.

### Backlog

- Supplier Response Analyzer.
- Contextual RFQ Generator.
- Margin and FOB Engine.
- Scoring and Next Action Engine.
- RAG de proveedores.
- Monitoreo automatizado.

---

## 9. Criterios de éxito

El ciclo se considerará exitoso cuando:

1. Energía Solar Portátil tenga una decisión clara o un camino de cierre.
2. El Nicho 2 haya sido seleccionado mediante un proceso reproducible.
3. Se haya reducido el tiempo o la fricción respecto del piloto.
4. El Matrix Validator funcione sobre archivos reales.
5. Exista un backlog del Intelligence Engine basado en problemas observados.

---

## 10. Próxima acción

```text
1. Esperar y procesar respuestas de proveedores.
2. Generar la lista larga de candidatos para el Nicho 2.
3. Diseñar la matriz de screening rápido.
4. Especificar el contrato de entrada y salida del Matrix Validator.
```

---

## 11. Documentos relacionados

- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-ROADMAP-002 — Project Status and Handoff](./si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-005 — Portable Solar Pilot Scope](../09-decision-log/si-decision-005-portable-solar-pilot-scope.md)
- [SI-DECISION-006 — Build the Intelligence Engine Incrementally](../09-decision-log/si-decision-006-build-intelligence-engine-incrementally.md)

---

## 12. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-16 | Roadmap inicial de tres líneas y seis semanas. |
