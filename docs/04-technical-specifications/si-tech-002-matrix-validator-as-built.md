---
id: si-tech-002
title: Matrix Validator As-Built
description: Estado técnico verificable del Matrix Validator después de adoptar aut31 y full-matrix-v5.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-08-04
updated: 2026-08-04
tags:
  - technical-specification
  - matrix-validator
  - as-built
  - full-matrix-v5
related:
  - si-func-001
  - si-tech-001
  - si-roadmap-002
  - si-decision-010
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
Node.js: 24
pnpm: 11
TypeScript: ESM
CLI: Commander
Lector XLSX: SheetJS CE 0.20.3
Schemas: v3 0.1.0 / v4 0.6.0 / v5 0.5.0
Reglas: 17
Tests: 35 archivos / 144 tests
Commit: 3ec32ca
```

## 2. Matrices compatibles

| Matriz | Schema | Uso |
|---|---|---|
| `aut29` | `full-matrix-v3` | Baseline anterior a fuentes globales. |
| `aut30` | `full-matrix-v4` | Fuentes y evidencias normalizadas. |
| `aut31` | `full-matrix-v5` | Resúmenes normalizados y vistas derivadas. |

## 3. Arquitectura

```text
CLI
→ ValidateMatrixUseCase
→ SheetJsWorkbookReader
→ WorkbookSnapshot
→ MatrixSchema + ValidationRule[]
→ ValidationReport
→ JSON / consola / exit code
```

El proceso es read-only. El reporte incorpora versión de aplicación, schema, filename y SHA-256.

## 4. Capacidades declarativas

`MatrixSchema` permite declarar:

- hojas y columnas;
- posiciones;
- PK;
- FK simples y listas;
- allowed values;
- tipos lógicos;
- rangos numéricos;
- valores obligatorios;
- `requiredWhen`;
- `rowConsistency`;
- `normalizedSources`;
- `derivedViews`.

## 5. full-matrix-v5

v5 incorpora nueve hojas de resumen:

- tres cabeceras canónicas;
- tres tablas de detalle;
- tres vistas ejecutivas.

Las vistas proyectan 55 columnas y `aut31` contiene 391 celdas derivadas verificadas.

## 6. Cobertura de reglas

La implementación valida estructura, identidad, referencias, valores, tipos, rangos, condiciones, consistencia por fila, fuentes y vistas. No recalcula fórmulas con un motor de Excel; inspecciona fórmulas y resultados almacenados.

## 7. Deuda técnica

- ExcelJS y pruebas del spike.
- Scripts `spike:xlsx` y `spike:sheetjs`.
- Fixtures públicos E2E.
- CI.
- Agregados cruzados.
- Formato general de IDs.
- Warning provisional.

## 8. Criterio de release

La primera release exige E2E público, CI, manual operativo, limpieza del spike, Definition of Done aprobada y retiro explícito del warning provisional.
