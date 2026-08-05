---
id: si-tech-002
title: Matrix Validator As-Built
description: Estado técnico verificable del Matrix Validator después de adoptar aut32 y publicar la release v0.1.0.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-08-04
updated: 2026-08-05
tags:
  - technical-specification
  - matrix-validator
  - as-built
  - full-matrix-v5
  - release
related:
  - si-func-001
  - si-tech-001
  - si-roadmap-002
  - si-decision-010
  - si-decision-011
audience:
  - founder
  - developer
  - assistant
phase: foundation
---
# SI-TECH-002 — Matrix Validator as-built

## 1. Baseline verificable

```text
Aplicación: 0.1.0
Release GitHub: v0.1.0 — Matrix Validator MVP
Commit de release: 9f4125b
Node.js: 24
pnpm: 11
TypeScript: ESM
CLI: Commander
Lector XLSX: SheetJS CE 0.20.3
Schemas: v3 0.1.0 / v4 0.6.0 / v5 0.7.0
Reglas de validación: 19
Tests: 40 archivos / 170 tests
Casos CLI: 5
Fixtures E2E públicos: 10
CI remoto: verde
Comportamiento: read-only
Publicación npm: ninguna; package private
```

Release pública:

```text
https://github.com/agelormini2024/smart-imports-engine/releases/tag/v0.1.0
```

## 2. Matrices compatibles

| Matriz | Schema | Uso | Resultado verificado |
|---|---|---|---|
| `aut29` | `full-matrix-v3 0.1.0` | Baseline anterior a fuentes globales. | 0 errores; warning de cobertura parcial. |
| `aut30` | `full-matrix-v4 0.6.0` | Fuentes y evidencias normalizadas. | 0 errores; warning de cobertura parcial. |
| `aut31` | `full-matrix-v5 0.7.0` | Checkpoint histórico de resúmenes normalizados. | 1 error conocido por `EV-0009`. |
| `aut32` | `full-matrix-v5 0.7.0` | Matriz operativa vigente. | `PASS`; 0 errores, 0 warnings y 0 limitaciones. |

`aut32` no agrega una evaluación nueva: corrige el identificador inválido `EV-0009` por `EVAL-0009`.

## 3. Arquitectura

```text
CLI / Commander
↓
ValidateMatrixUseCase
↓
19 ValidationRule
↓
ValidationReport
↑
WorkbookReaderPort
↑
SheetJsWorkbookReader
↑
XLSX exportado desde Google Sheets
```

El proceso es read-only. El reporte incorpora versión de aplicación, schema, filename y SHA-256. El dominio no depende de Commander ni de SheetJS.

## 4. Capacidades declarativas

`MatrixSchema` permite declarar y validar:

- hojas, columnas y posiciones;
- claves primarias faltantes, duplicadas y con formato inválido;
- claves foráneas simples;
- listas de referencias y rangos;
- unicidad interna de listas;
- allowed values;
- tipos lógicos;
- rangos numéricos;
- valores obligatorios;
- `requiredWhen`;
- `rowConsistency`;
- `normalizedSources`;
- `derivedViews`;
- cobertura de validación por schema.

## 5. full-matrix-v5

v5 incorpora nueve hojas normalizadas de resumen:

- tres cabeceras canónicas;
- tres tablas de detalle;
- tres vistas ejecutivas.

Las cabeceras y detalles son fuentes de verdad. Las vistas son proyecciones formula-driven y no aceptan carga manual.

La cobertura completa del MVP corresponde a `full-matrix-v5 0.7.0`. Los schemas históricos v3/v4 conservan warnings explícitos de cobertura parcial.

## 6. CLI y trazabilidad

La CLI soporta:

- reporte JSON;
- reporte de texto;
- persistencia mediante `--output`;
- modo estricto;
- exit codes `0`, `1`, `2` y `3`;
- SHA-256 del archivo validado.

Baseline operativa:

```text
Test files: 40 passed
Tests: 170 passed
CLI cases: 5 passed
Public E2E fixtures: 10 passed
Remote CI: green
```

## 7. Gates de release

La release fue validada mediante:

```bash
pnpm install --frozen-lockfile
pnpm typecheck
pnpm exec tsc -p tests/tsconfig.json --noEmit
pnpm test
pnpm build
pnpm test:cli
pnpm test:e2e
```

Además, `aut32` fue validada localmente contra `full-matrix-v5` con resultado `PASS` limpio.

## 8. Trabajo no bloqueante post-MVP

No bloquean `v0.1.0`:

- revisión humana de resúmenes `BORRADOR`;
- recálculo de agregados cruzados;
- secuencia global y detección de huecos de IDs;
- controles históricos adicionales;
- decisión editorial final sobre hojas `Legacy`.

Estos puntos sólo deben priorizarse cuando exista valor operativo o comercial suficiente.

## 9. Criterio de evolución

Una nueva versión del Validator deberá:

1. responder a una necesidad funcional documentada;
2. mantener schemas versionados;
3. conservar compatibilidad o declarar explícitamente la ruptura;
4. incluir tests y fixtures reproducibles;
5. pasar CI;
6. actualizar `SI-TECH-002`, `SI-ROADMAP-002` y Decision Log cuando cambie la baseline operativa.

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-08-04 | Baseline de `aut31`, `full-matrix-v5 0.5.0` y 144 tests. |
| 0.2.0 | 2026-08-05 | Baseline de `aut32`, `full-matrix-v5 0.7.0` y release `v0.1.0`. |
