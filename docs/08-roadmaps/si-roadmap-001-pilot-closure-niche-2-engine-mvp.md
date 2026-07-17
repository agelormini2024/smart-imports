---
id: si-roadmap-001
title: Pilot Closure, Niche 2 and Intelligence Engine MVP Roadmap
description: Plan coordinado para cerrar Energía Solar Portátil, ejecutar el segundo nicho y construir el primer MVP del Intelligence Engine.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-07-17
tags:
  - roadmap
  - portable-solar-energy
  - travel-organization
  - intelligence-engine
  - mvp
related:
  - si-agent-001
  - si-research-001
  - si-research-002
  - si-roadmap-002
  - si-decision-005
  - si-decision-006
  - si-decision-007
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

Coordinar tres líneas paralelas:

```text
Línea A — Cerrar Energía Solar Portátil
Línea B — Ejecutar Viaje organizado como Nicho 2
Línea C — Construir el primer MVP del Intelligence Engine
```

---

## 2. Reglas operativas

1. No mantener más de dos nichos activos simultáneamente.
2. No automatizar procesos no comprendidos manualmente.
3. No iniciar compras o muestras sin precio, documentación y decisión humana.
4. No forzar una conclusión positiva del piloto solar.
5. Registrar decisiones relevantes en el Decision Log.
6. Actualizar el documento de estado después de cada hito.
7. La matriz más reciente es la fuente operativa de verdad.
8. GitHub es la fuente documental de verdad.

---

## 3. Línea A — Energía Solar Portátil

### Objetivo

Cerrar Margen Potencial y Facilidad de Importación para producir una decisión fundamentada.

### Estado

**En curso / esperando respuestas de proveedores.**

### Criterios pendientes

- Margen Potencial.
- Facilidad de Importación.

### Proceso por respuesta

```text
Extraer
  ↓
Validar
  ↓
Detectar faltantes y contradicciones
  ↓
Comparar requisitos excluyentes
  ↓
Comparar FOB vs FOB objetivo
  ↓
Repreguntar o negociar
  ↓
Registrar
  ↓
Recalcular
```

### Resultado esperado

- Avanzar a muestra.
- Continuar negociando.
- Mantener en observación.
- Descartar producto o subcategoría.
- Reformular o descartar el nicho.

---

## 4. Línea B — Viaje organizado y equipaje funcional

### Objetivo

Aplicar por segunda vez el método completo en un nicho distinto y medir repetibilidad, tiempo, errores y calidad de decisión.

### Hitos completados

- [x] Lista larga de 12 candidatos.
- [x] Filtros excluyentes.
- [x] Normalización a seis candidatos.
- [x] Screening rápido.
- [x] Selección de tres finalistas.
- [x] Validación profunda.
- [x] Selección del Nicho 2.
- [x] Alcance inicial documentado.

### Nicho seleccionado

```text
Viaje organizado y equipaje funcional
```

### Hitos próximos

- [ ] Registrar el nicho en la matriz.
- [ ] Preparar términos de búsqueda y PDFs.
- [ ] Procesar Demanda.
- [ ] Procesar Competencia.
- [ ] Identificar productos base.
- [ ] Hacer screening preliminar de proveedores y margen.
- [ ] Evaluar Facilidad de Importación.
- [ ] Comparar resultados con el piloto solar.

### Subcategorías iniciales

- Sets organizadores estándar.
- Packing cubes de compresión.
- Organizadores tecnológicos.
- Organizadores para calzado.
- Neceseres compartimentados.
- Bolsas para ropa usada.

### Medición

Registrar tiempo aproximado para:

| Actividad | Solar | Viaje |
|---|---:|---:|
| Procesar publicación | Línea base pendiente | Por medir |
| Registrar producto base | Línea base pendiente | Por medir |
| Crear evidencia | Línea base pendiente | Por medir |
| Detectar duplicaciones | Línea base pendiente | Por medir |
| Generar XLSX importable | Línea base pendiente | Por medir |
| Validar importable | Línea base pendiente | Por medir |

---

## 5. Línea C — Intelligence Engine MVP

### MVP seleccionado

```text
Matrix Validator
```

### Estado

**Pendiente de especificación técnica e implementación.**

### Alcance inicial

- Hojas requeridas.
- Nombres y orden de columnas.
- IDs primarios.
- Relaciones.
- Evidencias y evaluaciones.
- Valores permitidos.
- Duplicaciones potenciales.
- Reporte de errores y advertencias.

### Stack preliminar

```text
TypeScript
Node.js
Zod
ExcelJS
CLI
Vitest o Jest
```

### Requisitos observados para módulos posteriores

- Marketplace Evidence Analyzer.
- Niche Candidate Normalizer.
- Claims Validation Gate.
- Product Quality Specification Builder.
- Supplier Response Analyzer.

---

## 6. Tablero actual

### En curso

- Espera y seguimiento de RFQ solares.
- Registro operativo de Viaje organizado.
- Preparación de la primera tanda de Demanda.
- Especificación inicial del Matrix Validator.

### Próximo

- Procesar publicaciones de viaje.
- Crear productos base y evidencias.
- Medir tiempos.
- Aplicar Demanda y Competencia.

### Bloqueado o esperando

- Margen solar definitivo.
- Facilidad de Importación solar definitiva.
- Ranking final de proveedores solares.

Dependencia: respuestas, certificados y packing de proveedores.

---

## 7. Criterios de éxito del ciclo

1. Energía Solar Portátil tiene una decisión clara o camino de cierre.
2. Viaje organizado completa Demanda y Competencia formal.
3. Se mide al menos una línea base de tiempos y errores.
4. El Matrix Validator funciona sobre archivos reales.
5. El backlog del Intelligence Engine refleja problemas observados.
6. La metodología puede compararse entre dos nichos diferentes.

---

## 8. Próxima acción principal

```text
1. Obtener la matriz XLSX más reciente.
2. Registrar Viaje organizado como Nicho 2.
3. Recolectar la primera tanda de publicaciones ML.
4. Procesar Demanda por subcategoría.
5. Continuar procesando respuestas solares cuando lleguen.
```

---

## 9. Documentos relacionados

- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-RESEARCH-001 — Niche 2 Selection](../06-research/si-research-001-niche-2-selection.md)
- [SI-RESEARCH-002 — Travel Organization Scope](../06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md)
- [SI-ROADMAP-002 — Project Status and Handoff](./si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-007 — Select Travel Organization as Niche 2](../09-decision-log/si-decision-007-select-travel-organization-as-niche-2.md)

---

## 10. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-16 | Roadmap inicial de tres líneas. |
| 0.2.0 | 2026-07-17 | Se completó la selección del Nicho 2 y se actualizó el roadmap hacia su ejecución formal. |
