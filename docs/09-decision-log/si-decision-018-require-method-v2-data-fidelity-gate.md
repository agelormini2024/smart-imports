---
id: si-decision-018
title: Require Method v2 Data Fidelity Gate
description: Decisión de exigir un preflight de fidelidad semántica además del Matrix Validator antes de cerrar checkpoints de Method v2.
version: 1.0.2
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-08
updated: 2026-10-10
tags:
  - decision
  - method-v2
  - data-fidelity
  - governance
related:
  - si-bim-001
  - si-bim-proc-003
  - si-func-001
---

# SI-DECISION-018 — Require Method v2 Data Fidelity Gate

## Contexto

Durante la revisión post-cierre de `BRAND-CAND-010`, se detectó que algunos registros de `Publicaciones ML.Ventas visibles` contenían interpretación en lugar del dato crudo observado.

Matrix Validator había dado PASS porque esa inconsistencia era semántica y no estructural.

## Decisión

Desde el checkpoint de governance del 2026-10-10:

> **Ningún gate de Method v2 puede cerrarse sólo con Matrix Validator PASS.**

Se exige:

```text
Method v2 Data Fidelity Preflight PASS
+
Matrix Validator PASS
=
checkpoint elegible para CLOSED
```

Además:
- raw evidence y análisis se separan;
- datos ambiguos no se reconstruyen por inferencia;
- Product Bases permanecen prohibidas antes de F6;
- la frontera F6 se controla tanto en `Publicaciones ML` como en `Productos Base`;
- una reverificación posterior no reescribe silenciosamente una captura histórica;
- correcciones post-cierre se materializan como nuevo snapshot;
- si una corrección puede cambiar una decisión, se reabre la fase más temprana afectada.

## Consecuencias

1. `SI-BIM-001 — Demand Evaluation` se conserva como criterio histórico y se fortalece aditivamente.
2. Se incorpora `SI-BIM-PROC-003 — Method v2 Execution Contract`.
3. Se incorpora `scripts/validate-method-v2-data-fidelity.py`.
4. Se incorpora `scripts/validate-method-v2-checkpoint.sh`.
5. `BRAND-CAND-010` queda reconciliado en `aut120` con dual PASS.
6. `aut118` permanece como snapshot histórico de cierre F13.
7. `aut119 corrected` queda superseded antes de publicación.
8. `aut120` pasa a ser la baseline vigente post-cierre.
9. Matrix Validator v0.1.0 no se reabre en este momento.

## Criterio de éxito

Alejandro no necesita revisar manualmente cada celda para confirmar que se aplicó la convención acordada.

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.2 | 2026-10-10 | Adopta aut120 dual PASS y corrige el contrato de trazabilidad temporal/F6. |
| 1.0.1 | 2026-10-10 | Registra aut119 corrected dual PASS como reconciliación intermedia. |
| 1.0.0 | 2026-10-08 | Decisión inicial. |
