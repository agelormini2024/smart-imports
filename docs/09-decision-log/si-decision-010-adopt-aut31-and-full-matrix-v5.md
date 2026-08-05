---
id: si-decision-010
title: Adopt aut31 and full-matrix-v5
description: Decisión de adoptar aut31 como matriz operativa normalizada y full-matrix-v5 como contrato ejecutable asociado.
version: 0.1.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-08-04
updated: 2026-08-04
tags:
  - decision
  - matrix-validator
  - aut31
  - full-matrix-v5
  - summary-sheets
related:
  - si-func-001
  - si-tech-002
  - si-roadmap-002
  - si-decision-009
audience:
  - founder
  - partner
  - developer
  - assistant
phase: foundation
---

# SI-DECISION-010 — Adoptar aut31 y full-matrix-v5

## Contexto

Las matrices anteriores conservaban las hojas `Resumen Competencia`, `Resumen Margen` y `Resumen Tanda` como estructuras narrativas. Esto impedía validar formalmente sus registros, relaciones, métricas y fórmulas.

La normalización produjo `aut31` y `full-matrix-v5 0.5.0`, con cabeceras canónicas, tablas de detalle y vistas ejecutivas derivadas.

## Decisión

Se adopta:

```text
aut31 como matriz operativa vigente
full-matrix-v5 0.5.0 como schema ejecutable asociado
```

Se preserva compatibilidad histórica:

```text
aut29 → full-matrix-v3
aut30 → full-matrix-v4
aut31 → full-matrix-v5
```

## Modelo de resúmenes

| Dominio | Cabecera | Detalle | Vista |
|---|---|---|---|
| Competencia | `Resumen Competencia` | `Resumen Competencia Segmentos` | `Resumen Competencia Vista` |
| Margen | `Resumen Margen` | `Resumen Margen Productos` | `Resumen Margen Vista` |
| Tanda | `Resumen Tanda` | `Resumen Tanda Etapas` | `Resumen Tanda Vista` |

Las cabeceras y detalles son fuentes de verdad. Las vistas no aceptan datos manuales y deben ser proyecciones formula-driven.

## Hojas legacy

Las hojas narrativas originales se conservan temporalmente como `* Legacy` para auditoría. No forman parte del contrato operativo de v5. Su retiro se decidirá después de la revisión humana de los registros migrados.

## Consecuencias

### Positivas

- Los resúmenes son validables.
- La trazabilidad queda expresada mediante IDs.
- Se detectan fórmulas faltantes, referencias incorrectas y filas desalineadas.
- El schema se convierte en contrato reproducible.

### Costos y riesgos

- Los registros migrados requieren revisión humana.
- Las matrices anteriores necesitan sus schemas históricos.
- La evolución futura debe respetar versionado explícito.

## Criterio de vigencia

Una matriz futura sólo reemplazará a `aut31` cuando:

1. tenga schema compatible y versionado;
2. pase las reglas bloqueantes;
3. conserve trazabilidad de migración;
4. sea declarada vigente mediante decisión o actualización formal del handoff.
