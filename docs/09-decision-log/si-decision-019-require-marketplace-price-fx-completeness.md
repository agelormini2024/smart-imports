---
id: si-decision-019
title: Require Marketplace Price + FX Completeness
description: Decisión de exigir trazabilidad completa de precio local, conversión USD, FX y ventas visibles para toda evidencia marketplace utilizada por Method v2.
version: 1.0.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-10
updated: 2026-10-10
tags:
  - decision
  - method-v2
  - marketplace
  - data-fidelity
  - fx
  - pricing
  - governance
related:
  - si-bim-001
  - si-bim-proc-003
  - si-decision-018
  - si-research-086
---

# SI-DECISION-019 — Require Marketplace Price + FX Completeness

## Contexto

La reconciliación post-cierre de `BRAND-CAND-010` mostró una segunda brecha metodológica.

`SI-DECISION-018` ya exigía fidelidad semántica de evidencia y dual gate, pero no obligaba de manera suficientemente explícita y automatizable a que toda publicación marketplace conservara:

- precio local;
- conversión USD;
- tipo de cambio utilizado;
- fecha/baseline del tipo de cambio;
- fuente o basis del tipo de cambio;
- ventas visibles verificadas.

La brecha también existe en evidencia histórica de Marca Hogar.

## Decisión

Desde este checkpoint:

> **Una evidencia marketplace no está completa si su precio USD no puede reconstruirse desde el precio ARS y un FX trazable.**

El contrato mínimo es:

```text
PRODUCT / MODEL
+ EXPLICIT SOURCE BINDING (`EXACT_SOURCE` | `EXACT_MODEL_CURRENT`)
+ CAPTURE / VERIFICATION DATE
+ PRECIO ARS
+ VENTAS VISIBLES | NO INFORMADAS
+ FX ARS/USD
+ FX DATE
+ FX SOURCE / BASIS
+ PRECIO USD
+ DIRECT | DIRECT_CONDITIONED | ADJACENT | SUBSTITUTE
```

La conversión canónica es:

```text
Precio USD = ROUND(Precio ARS / FX ARS/USD, 2)
```

## Reglas vinculantes

```text
SELLER SALES ≠ PRODUCT SALES
BADGE ≠ VISIBLE SALES
CURRENT VERIFICATION ≠ HISTORICAL CAPTURE
PRICE WITHOUT FX TRACEABILITY ≠ VALID USD EVIDENCE
OFFER AVAILABILITY ≠ DEMAND EVIDENCE
```

Además:

1. una reverificación posterior nunca sobreescribe silenciosamente la captura histórica;
2. si una fuente histórica no puede recuperarse con binding suficiente, queda `HISTORICAL_ONLY / SOURCE_UNAVAILABLE`;
3. un comparable nuevo recibe un nuevo `ML ID`; nunca se hace pasar por la publicación histórica;
4. el precio de una publicación no puede combinarse con las ventas de otra;
5. para nuevas capturas, `Precio ARS` y `Precio USD` son obligatorios desde F3;
6. `Verificaciones ML` es una capa append-only de trazabilidad temporal: `Verificación ID` es único, un `ML ID` puede acumular múltiples verificaciones y la capa vigente debe corresponder a la fecha de verificación más reciente;
7. el Data Fidelity Preflight debe comprobar aritmética, FX, fechas, source binding y estado de la evidencia.

## Aplicación a BRAND-CAND-010

```text
matrix-aut118-brand-cand-010-phase13-final-corrected.xlsx
→ F13 histórico
→ 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a

matrix-aut120-brand-cand-010-post-close-reconciliation.xlsx
→ baseline post-close previa
→ 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2
→ SUPERSEDED

matrix-aut121-brand-cand-010-post-close-marketplace-economics-reconciliation-corrected.xlsx
→ marketplace economics reconciliation
→ Data Fidelity Preflight v2.2: PASS
→ Matrix Validator: PASS
→ errors 0 / warnings 0 / info 0
→ BASELINE VIGENTE
→ 7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc
```

La reconciliación no cambia score ni decisión:

```text
EVAL-0029 = 3/5
Confidence = Media
BRAND-CAND-010 = NO PORTFOLIO FINALIST / FREEZE
F0–F13 = CLOSED
F14 = NOT OPENED
```

## Deuda histórica — Marca Hogar

La auditoría detectó 63 publicaciones `ML-0089..ML-0151` con deuda de trazabilidad USD/FX.

No se permite backfill silencioso.

Cada Brand Candidate de Hogar debe reconciliarse preservando su captura histórica y usando el FX correspondiente a la captura/reverificación real.

## Criterio de éxito

Un agente que reciba sólo el repo puede determinar:

- qué campos debe capturar;
- qué no puede inferir;
- cómo convertir ARS a USD;
- cómo registrar el FX;
- cómo manejar una fuente histórica perdida;
- qué debe validar antes de cerrar F3 o fases posteriores.

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-10 | Exige completitud marketplace ARS/USD/FX/ventas y adopta aut121 corrected como baseline vigente. |
