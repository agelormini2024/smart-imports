---
id: si-roadmap-002
title: Project Status and Handoff
description: Estado operativo, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports.
version: 0.8.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-08-04
tags:
  - status
  - handoff
  - roadmap
  - continuity
related:
  - si-roadmap-001
  - si-agent-001
  - si-func-001
  - si-tech-001
  - si-tech-002
  - si-decision-009
  - si-decision-010
audience:
  - founder
  - partner
  - developer
  - assistant
phase: foundation
---

# SI-ROADMAP-002 — Estado actual y handoff de Smart Imports

> Punto de entrada operativo obligatorio para retomar el proyecto sin depender de un chat específico.

## 1. Fuentes de verdad

```text
Documentación y negocio:
https://github.com/agelormini2024/smart-imports

Software ejecutable:
https://github.com/agelormini2024/smart-imports-engine

Matriz operativa vigente:
aut31 → full-matrix-v5 0.5.0
```

Compatibilidad histórica:

```text
aut29 → full-matrix-v3 0.1.0
aut30 → full-matrix-v4 0.6.0
aut31 → full-matrix-v5 0.5.0
```

## 2. Snapshot al 2026-08-04

| Campo | Estado |
|---|---|
| Fase | Foundation avanzada / cierre del Matrix Validator MVP |
| Nichos activos | 2 |
| Energía Solar Portátil | Demanda y Competencia revisadas; Margen e Importación preliminares; prioridad pausada |
| Viaje organizado | Demanda y Competencia consolidadas; shortlist de Margen aprobada |
| Matriz vigente | `aut31` |
| Schema vigente | `full-matrix-v5 0.5.0` |
| Matrix Validator | 17 reglas; 35 archivos de test; 144 tests |
| Resultado v5 | 0 errores; 1 warning provisional |
| Rama técnica | `feat/normalize-summary-sheets` |
| Commit técnico | `3ec32ca` |
| Próxima acción | Fixtures públicos E2E y CI, después del checkpoint documental |

## 3. Matrix Validator — trabajo completado

- Foundation TypeScript, Node 24 y pnpm 11.
- CLI local read-only.
- SheetJS CE como lector operativo.
- Snapshot desacoplado y SHA-256.
- Schemas v3, v4 y v5.
- Estructura, PK, FK y listas.
- Valores obligatorios y allowed values.
- Fuentes y evidencias normalizadas.
- Resúmenes de Competencia, Margen y Tanda normalizados.
- Tipos y rangos declarativos.
- Obligaciones condicionales.
- Consistencia semántica por fila.
- Vistas derivadas formula-driven.
- 391 celdas derivadas verificadas.
- 144 tests aprobados.

## 4. Matrix Validator — pendientes de cierre

1. Fixtures públicos válidos e inválidos.
2. Pruebas end-to-end desde XLSX hasta exit code.
3. GitHub Actions.
4. Manual operativo final.
5. Eliminación de ExcelJS y spikes.
6. Decisión sobre agregados cruzados, duplicados en listas y formato de IDs.
7. Revisión humana de resúmenes migrados.
8. Retiro del warning provisional.
9. Release versionada.

## 5. Matriz aut31

`aut31` incorpora:

```text
Fuentes
Evidencia Fuentes
Resumen Competencia
Resumen Competencia Segmentos
Resumen Competencia Vista
Resumen Margen
Resumen Margen Productos
Resumen Margen Vista
Resumen Tanda
Resumen Tanda Etapas
Resumen Tanda Vista
```

Las tablas canónicas son fuentes de verdad. Las vistas son proyecciones formula-driven. Las hojas `Legacy` se conservan sólo como auditoría temporal.

Los resúmenes migrados permanecen `BORRADOR` y requieren revisión humana antes de pasar a `REVISADO`.

## 6. Estado comercial

### Energía Solar Portátil

- No forzar conclusión positiva.
- AT-999 pausado.
- Paneles y demás candidatos permanecen sin desembolso mientras no recuperen prioridad.
- Margen e Importación sólo se cerrarán con información confiable.

### Viaje organizado y equipaje funcional

- Demanda cerrada.
- Competencia cerrada.
- Shortlist de Margen aprobada.
- RFQ masivo no iniciado.
- El screening se retomará con matriz y Validator estabilizados.

## 7. Bloqueos y dependencias

| Bloqueo | Dependencia | Acción |
|---|---|---|
| Release reproducible | Fixtures públicos y CI | Construir E2E sanitizado |
| Retiro del warning | Definition of Done | Clasificar reglas pendientes |
| Adopción operativa de aut31 | Revisión humana | Revisar resúmenes `BORRADOR` |
| Margen del Nicho 2 | Prioridad comercial | Retomar screening después del cierre técnico |
| Cierre solar | Datos confiables | Mantener pausa selectiva |

## 8. Prioridades

```text
P1 — Checkpoint documental
P2 — Fixtures públicos E2E
P3 — GitHub Actions
P4 — Limpieza y manual operativo
P5 — Definition of Done y release
P6 — Screening de Margen del Nicho 2
```

## 9. Protocolo para abrir un nuevo chat

1. Compartir ambos repositorios.
2. Pedir lectura inicial de `SI-ROADMAP-002`.
3. Para código, indicar rama y commit vigente.
4. Adjuntar `aut31` sólo cuando la tarea requiera datos privados de la matriz.
5. No adjuntar nuevamente PDFs históricos ya consolidados.
6. Adjuntar sólo información nueva o no documentada.
7. Confirmar si la tarea es funcional/negocio (`smart-imports`) o técnica (`smart-imports-engine`).

## 10. Próxima acción concreta

```text
Crear fixtures XLSX públicos de full-matrix-v5
→ implementar tests E2E
→ configurar GitHub Actions
```

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.7.0 | 2026-08-03 | Handoff de v3/v4 y normalización de fuentes. |
| 0.8.0 | 2026-08-04 | Adopción de aut31/v5, 144 tests y cierre técnico de vistas derivadas. |
