---
id: si-decision-011
title: Adopt aut32 and release Matrix Validator v0.1.0
description: Decisión de adoptar aut32 como matriz operativa, full-matrix-v5 0.7.0 como schema vigente y v0.1.0 como primera release del Matrix Validator.
version: 0.1.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-08-05
updated: 2026-08-05
tags:
  - decision
  - matrix-validator
  - aut32
  - full-matrix-v5
  - release
related:
  - si-func-001
  - si-tech-002
  - si-roadmap-002
  - si-decision-009
  - si-decision-010
audience:
  - founder
  - partner
  - developer
  - assistant
phase: foundation
---
# SI-DECISION-011 — Adoptar aut32 y publicar Matrix Validator v0.1.0

## Contexto

SI-DECISION-010 adoptó `aut31` y `full-matrix-v5 0.5.0` después de normalizar las hojas de resumen. Esa decisión resolvió la estructura tabular y permitió validar cabeceras, detalles y vistas derivadas.

El cierre del MVP incorporó posteriormente:

- formatos declarativos de identificadores;
- detección de duplicados dentro de listas de referencias;
- cobertura declarada por schema;
- reporte de texto y persistencia mediante `--output`;
- cinco casos operativos de CLI;
- diez fixtures XLSX públicos end-to-end;
- GitHub Actions;
- retiro de ExcelJS y artefactos experimentales;
- corrección de `EV-0009` por `EVAL-0009` en una nueva matriz `aut32`.

La aplicación ya estaba versionada como `0.1.0`. El schema v5 alcanzó la versión `0.7.0` y `aut32` obtuvo un resultado limpio.

## Decisión

Se adopta formalmente:

```text
Matriz operativa vigente: aut32
Schema ejecutable vigente: full-matrix-v5 0.7.0
Aplicación: 0.1.0
Tag: v0.1.0
GitHub Release: Matrix Validator MVP
Commit de release: 9f4125b
```

La release oficial es:

```text
https://github.com/agelormini2024/smart-imports-engine/releases/tag/v0.1.0
```

El paquete mantiene `private: true` y no se publica en npm. La release representa una versión reproducible del código fuente en GitHub.

## Baseline verificable

```text
Test files: 40 passed
Tests: 170 passed
CLI cases: 5 passed
Public E2E fixtures: 10 passed
Remote CI: green
```

Resultado de la matriz operativa:

```text
aut32
full-matrix-v5 0.7.0
PASS
Errors: 0
Warnings: 0
Limitations: 0
```

## Compatibilidad

```text
aut29 → full-matrix-v3 0.1.0
aut30 → full-matrix-v4 0.6.0
aut31 → full-matrix-v5 0.7.0; checkpoint histórico con EV-0009
aut32 → full-matrix-v5 0.7.0; baseline operativa con EVAL-0009
```

Los schemas v3/v4 conservan warnings explícitos de cobertura parcial. `full-matrix-v5 0.7.0` declara cobertura completa para el MVP.

## Relación con SI-DECISION-010

SI-DECISION-010 permanece como registro histórico de la normalización de los resúmenes y del modelo cabecera-detalle-vista.

Esta decisión reemplaza su baseline operativa:

```text
aut31 / full-matrix-v5 0.5.0
↓
aut32 / full-matrix-v5 0.7.0
```

No se revierte la arquitectura de resúmenes aprobada en SI-DECISION-010.

## Justificación

- `aut32` corrige el único identificador inválido conocido de `aut31`.
- v5 retorna `PASS` sin warnings ni limitaciones.
- La cobertura del MVP es explícita y reproducible.
- Los gates públicos y privados fueron ejecutados en la rama de trabajo y nuevamente sobre `main`.
- El tag, la CLI y `package.json` comparten la versión `0.1.0`.
- La release permite cerrar el bloque técnico sin confundir trabajo post-MVP con bloqueantes.

## Alternativas consideradas

### Mantener aut31 como matriz vigente

Descartada porque conserva `EV-0009`, que incumple el formato declarativo de IDs de evaluación.

### Crear una versión de aplicación adicional antes de la release

Descartada porque la aplicación ya estaba correctamente versionada como `0.1.0`.

### Usar un tag especial distinto de la versión

Descartada para mantener alineados paquete, CLI y tag.

### Postergar la release hasta completar todos los puntos post-MVP

Descartada porque la revisión editorial, los agregados cruzados y la secuencia global de IDs no bloquean la cobertura técnica acordada.

## Consecuencias

### Positivas

- Existe una baseline operativa única y documentada.
- El MVP queda cerrado con evidencia reproducible.
- El repositorio documental y el repositorio ejecutable vuelven a estar alineados.
- El proyecto puede retomar el trabajo comercial del Nicho 2.
- Los desarrollos posteriores pueden evaluarse contra una release estable.

### Costos y riesgos

- Los resúmenes `BORRADOR` aún requieren revisión humana.
- Las matrices históricas necesitan sus schemas o condiciones de cobertura correspondientes.
- Las hojas `Legacy` permanecen temporalmente.
- Una nueva versión deberá actualizar código, schema, matriz, release y documentación coordinadamente.

## Trabajo post-MVP no bloqueante

- Recálculo de agregados cruzados.
- Secuencia global y detección de huecos de IDs.
- Controles históricos adicionales.
- Revisión editorial de resúmenes.
- Decisión final sobre hojas `Legacy`.

## Criterio de vigencia

Una matriz o release futura reemplazará esta baseline sólo cuando:

1. tenga schema compatible y versionado;
2. pase los gates aplicables;
3. conserve trazabilidad de migración;
4. actualice la documentación as-built;
5. sea declarada vigente mediante una nueva decisión o actualización formal del handoff.

## Documentos relacionados

- [SI-FUNC-001 — Matrix Validator](../03-functional-specifications/si-func-001-matrix-validator.md)
- [SI-TECH-002 — Matrix Validator As-Built](../04-technical-specifications/si-tech-002-matrix-validator-as-built.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-010 — Adopt aut31 and full-matrix-v5](./si-decision-010-adopt-aut31-and-full-matrix-v5.md)

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-08-05 | Adopción de `aut32`, `full-matrix-v5 0.7.0` y release `v0.1.0`. |
