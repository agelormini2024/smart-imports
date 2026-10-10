---
id: si-research-086
title: BRAND-CAND-010 — Post-close Marketplace Economics Reconciliation
description: Reconciliación post-cierre de ventas visibles, precios ARS/USD, FX y source binding de marketplace para BRAND-CAND-010.
version: 1.0.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-10
updated: 2026-10-10
brand: brand-fitness
brand_candidate: brand-cand-010
method: method-v2-agile
phase: post-close-reconciliation
related:
  - si-research-085
  - si-decision-019
  - si-bim-proc-003
---

# SI-RESEARCH-086 — BRAND-CAND-010 — Post-close Marketplace Economics Reconciliation

## 1. Motivo

Después de `SI-RESEARCH-085`, se detectó que la captura de marketplace todavía no garantizaba de forma sistemática:

- `Precio ARS`;
- `Precio USD`;
- FX utilizado;
- fecha/baseline del FX;
- fuente/basis del FX;
- `Ventas visibles` verificadas para cada publicación.

La brecha era metodológica y transversal; también aparece en Marca Hogar.

## 2. Clasificación

```text
TYPE: MARKETPLACE ECONOMICS / DATA FIDELITY / TRACEABILITY
EARLIEST AFFECTED PHASE: F3 — Demand
DECISION IMPACT: REVIEWED / NO CHANGE
REOPEN F3–F13: NO
RECONCILIATION TYPE: POST-CLOSE / NON-DECISION-IMPACTING
F14: NOT OPENED
```

## 3. Política aplicada

La captura histórica no se reescribe.

```text
HISTORICAL CAPTURE
+
DATED VERIFICATION EVENT
=
TRACEABLE CURRENT SNAPSHOT
```

`Verificaciones ML` se conserva como ledger append-only: una publicación puede acumular múltiples eventos de verificación con `Verificación ID` único; la capa vigente en `Publicaciones ML` debe corresponder a la fecha más reciente.

Cada verificación activa conserva:

```text
ML ID
Fecha Verificación ML
Estado Evidencia ML
Binding Verificación ML
Precio ARS Verificado
Precio USD Verificado
Ventas visibles Verificadas
FX ARS/USD
FX Fecha
FX Fuente / Basis
Fuente Verificación ML
Observaciones Verificación ML
```

## 4. Resultado de la auditoría Fitness

Scope:

```text
BRAND-CAND-010
ML-0152..ML-0175 historical set
+ ML-0176..ML-0177 replacement DIRECT rows
```

Resultado materializado:

```text
Publications audited: 26
Verification ledger rows: 26
Product Bases: 4
```

Las fuentes históricas que no pudieron recuperarse con source binding suficiente se conservaron como:

```text
HISTORICAL_ONLY
SOURCE_UNAVAILABLE
Precio = No verificable
Ventas = No informadas
```

No se copiaron precios ni contadores desde listings similares.

## 5. A4 — reemplazos actuales

Las publicaciones históricas directas de A4 sin source binding actual suficiente no fueron adulteradas.

Se incorporaron nuevos `ML ID`:

```text
ML-0176
ML-0177
```

como replacements DIRECT actuales, con precio/FX verificables y sin transferir ventas del vendedor al producto.

## 6. FX utilizado

Para esta reconciliación se usa la baseline ya registrada en el proyecto:

```text
ARS/USD = 1535
FX baseline date = 2026-09-21
Basis = baseline histórica de proyecto informada por Founder
```

No se presenta como cotización de mercado del 2026-10-10.

Fórmula:

```text
Precio USD = ROUND(Precio ARS / 1535, 2)
```

## 7. Deuda histórica detectada — Marca Hogar

| Scope | Rango | Filas | ARS faltante histórico | USD faltante histórico | Ventas en blanco | Ventas interpretativas |
|---|---|---:|---:|---:|---:|---:|
| Protección doméstica contra fugas | ML-0089..ML-0099 | 11 | 0 | 11 | 5 | 0 |
| Tratamiento doméstico del aire | ML-0100..ML-0119 | 20 | 0 | 20 | 10 | 0 |
| Monitoreo doméstico del consumo energético | ML-0120..ML-0139 | 20 | 0 | 20 | 0 | 0 |
| Compostaje / residuos orgánicos | ML-0140..ML-0151 | 12 | 2 | 12 | 0 | 1 |
| **TOTAL** | **ML-0089..ML-0151** | **63** | **2** | **63** | **15** | **1** |

La deuda queda explícita como backlog metodológico.

En particular, no corresponde aplicar retrospectivamente FX 1535 a publicaciones capturadas antes del 2026-09-21 como si ese FX hubiese pertenecido a la captura original.

## 8. Resultado estratégico ratificado

```text
EVAL-0029
Demand = 3/5
Confidence = Media
RATIFIED

BASE-FIT-001 → STOP — REOPENABLE / LOGISTICS GATE
BASE-FIT-002 → STOP — REOPENABLE / DEMAND + LOGISTICS GATE
BASE-FIT-003 → DEFER — LOW DEMAND PROOF
BASE-FIT-004 → DEFER — LOW DEMAND PROOF / STANDING-DESK DEPENDENCY

BRAND-CAND-010 → NO PORTFOLIO FINALIST / FREEZE
F14 → NOT OPENED
```

## 9. Lineage

```text
aut118
→ F13 historical snapshot
→ 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a

aut119 corrected
→ intermediate reconciliation
→ superseded before publication

aut120
→ post-close data-fidelity baseline
→ dual PASS
→ superseded by aut121 corrected
→ 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2

aut121
→ first marketplace-economics materialization
→ Data Fidelity v2 PASS
→ Matrix Validator FAIL only because Evidencia Fuentes.Rol used SOPORTE

aut121 corrected
→ changes EVSRC-0711..0713 Rol: SOPORTE → PRINCIPAL
→ no factual/economic/decision change
→ dual PASS
→ CURRENT POST-CLOSE BASELINE
→ 7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc
```

## 10. Validación final

```text
Data Fidelity Preflight v2.2
Result: PASS
Publications audited: 26
Verification ledger rows: 26
Product Bases found for scope: 4
Exit code: 0

Matrix Validator
Application: 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Findings: []
Limitations: []
Exit code: 0
```

## 11. Consecuencia de proceso

Se aprueba `SI-DECISION-019` y `SI-BIM-PROC-003` se amplía con el contrato obligatorio de marketplace economics.

`aut121 corrected` no representa F14 ni una nueva fase comercial.

F0–F13 permanecen `CLOSED`.

## 12. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-10 | Cierra marketplace economics reconciliation con aut121 corrected dual PASS. |


## 13. Supersession

`matrix-aut121-brand-cand-010-post-close-marketplace-economics-reconciliation-corrected.xlsx` / `7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc` queda `SUPERSEDED` por `aut122`.

Motivo: la capa de verificación estaba completa, pero el core `Precio ARS`, `Precio USD` y `Ventas visibles` no reflejaba la evidencia vigente en todas las filas `ACTIVE`.

La corrección se documenta en `SI-RESEARCH-087`.

No cambia score ni decisión.
