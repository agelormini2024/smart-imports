---
id: si-roadmap-002
title: Project Status and Handoff
description: Estado operativo, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports.
version: 0.9.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-08-05
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
  - si-decision-011
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

Release vigente:
v0.1.0 — Matrix Validator MVP

Matriz operativa vigente:
aut32 → full-matrix-v5 0.7.0
```

Compatibilidad histórica:

```text
aut29 → full-matrix-v3 0.1.0
aut30 → full-matrix-v4 0.6.0
aut31 → full-matrix-v5 0.7.0; checkpoint histórico con EV-0009
aut32 → full-matrix-v5 0.7.0; baseline operativa con EVAL-0009
```

## 2. Snapshot al 2026-08-05

| Campo | Estado |
|---|---|
| Fase | Foundation avanzada / primer MVP técnico publicado |
| Nichos activos | 2 |
| Energía Solar Portátil | Demanda y Competencia revisadas; Margen e Importación preliminares; prioridad pausada |
| Viaje organizado | Demanda y Competencia consolidadas; shortlist de Margen aprobada |
| Matriz vigente | `aut32` |
| Schema vigente | `full-matrix-v5 0.7.0` |
| Release del Engine | `v0.1.0 — Matrix Validator MVP` |
| Commit de release | `9f4125b` |
| Matrix Validator | 19 reglas; 40 archivos de test; 170 tests |
| Gates públicos | 5 casos CLI; 10 fixtures E2E |
| Resultado operativo | `PASS`; 0 errores, 0 warnings, 0 limitaciones |
| Rama técnica vigente | `main` |
| CI remoto | verde |
| Próxima acción principal | Retomar el screening público de Margen Potencial del Nicho 2 |

## 3. Matrix Validator — MVP completado

- Foundation TypeScript, Node 24 y pnpm 11.
- CLI local read-only.
- SheetJS CE como única implementación XLSX mantenida.
- Snapshot desacoplado y SHA-256.
- Schemas v3, v4 y v5.
- Estructura, PK, FK, listas y rangos.
- Formato declarativo de identificadores.
- Detección de duplicados dentro de listas.
- Valores obligatorios y allowed values.
- Fuentes y evidencias normalizadas.
- Resúmenes de Competencia, Margen y Tanda normalizados.
- Tipos y rangos declarativos.
- Obligaciones condicionales.
- Consistencia semántica por fila.
- Vistas derivadas formula-driven.
- Reportes JSON y texto.
- Persistencia mediante `--output`.
- Exit codes documentados.
- Cobertura declarada por schema.
- 40 archivos de test y 170 tests.
- 5 casos CLI públicos.
- 10 fixtures E2E públicos.
- GitHub Actions verde.
- ExcelJS y spikes retirados.
- Release `v0.1.0` publicada.

## 4. Resultado de release

```text
Application: 0.1.0
Schema: full-matrix-v5 0.7.0
Tag: v0.1.0
GitHub Release: Matrix Validator MVP
Commit: 9f4125b
Package publication: none; private true
```

Release pública:

```text
https://github.com/agelormini2024/smart-imports-engine/releases/tag/v0.1.0
```

No quedan bloqueantes técnicos del MVP.

## 5. Matriz aut32

`aut32` conserva la estructura normalizada introducida por `aut31`:

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

La diferencia operativa relevante es la corrección del identificador:

```text
EV-0009 → EVAL-0009
```

Las tablas canónicas son fuentes de verdad. Las vistas son proyecciones formula-driven. Las hojas `Legacy` se conservan sólo como auditoría temporal.

Los resúmenes migrados permanecen `BORRADOR` y requieren revisión humana antes de pasar a `REVISADO`. Esta revisión no bloquea la release técnica.

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
- El Validator ya no bloquea el retorno al screening.
- El siguiente paso es un screening público de precio, logística y diferenciación.
- Sólo deben avanzar a RFQ selectivo las referencias con señal económica suficiente.

Shortlist vigente:

1. Kits de envases recargables:
   - `BASE-TRAVEL-021`
   - `BASE-TRAVEL-022`
2. Bolsas de compresión al vacío:
   - `BASE-TRAVEL-010`
   - `BASE-TRAVEL-012`
   - `BASE-TRAVEL-011` como benchmark premium
3. Kit textil reforzado o premium, condicionado al costo:
   - `BASE-TRAVEL-002`
   - `BASE-TRAVEL-003`

Watchlist:

- `BASE-TRAVEL-006`

## 7. Bloqueos y dependencias

| Tema | Dependencia | Acción |
|---|---|---|
| Margen del Nicho 2 | Precios públicos, referencias comparables y señal logística | Retomar screening antes de RFQ masivo |
| Resúmenes `BORRADOR` | Revisión humana | Revisar antes de cambiar a `REVISADO` |
| Cierre solar | Datos confiables y prioridad comercial | Mantener pausa selectiva |
| Trabajo post-MVP del Engine | Necesidad funcional concreta | No ampliar por anticipación |
| Hojas `Legacy` | Decisión editorial posterior | Mantener temporalmente |

## 8. Prioridades

```text
P1 — Cerrar sincronización documental de v0.1.0
P2 — Retomar screening de Margen Potencial del Nicho 2
P3 — Revisar resúmenes BORRADOR de aut32
P4 — Avanzar a RFQ selectivo sólo si el screening lo justifica
P5 — Priorizar trabajo post-MVP del Engine según necesidad comercial
```

## 9. Protocolo para abrir un nuevo chat

1. Compartir ambos repositorios.
2. Pedir lectura inicial de `SI-ROADMAP-002`.
3. Para código, indicar rama y commit vigentes.
4. Adjuntar `aut32` sólo cuando la tarea requiera datos privados de la matriz.
5. No adjuntar nuevamente PDFs históricos ya consolidados.
6. Adjuntar sólo información nueva o no documentada.
7. Confirmar si la tarea es funcional/negocio (`smart-imports`) o técnica (`smart-imports-engine`).
8. Para la release del Validator, usar `v0.1.0` y el commit `9f4125b` como baseline.

## 10. Próxima acción concreta

```text
Cerrar este checkpoint documental
→ retomar screening público de Margen Potencial
→ descartar referencias sin señal suficiente
→ avanzar a RFQ selectivo sólo con candidatos defendibles
```

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.7.0 | 2026-08-03 | Handoff de v3/v4 y normalización de fuentes. |
| 0.8.0 | 2026-08-04 | Adopción de aut31/v5, 144 tests y cierre técnico de vistas derivadas. |
| 0.9.0 | 2026-08-05 | Adopción de aut32, cierre del MVP y publicación de `v0.1.0`. |
