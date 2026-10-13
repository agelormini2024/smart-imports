---
id: brand-fitness
title: Marca Fitness — Screening cerrado / Method v2
description: Estado vigente de Marca Fitness con screening cerrado, BRAND-CAND-010 F0–F13 cerrado, BRAND-CAND-007 F0–F3 cerrado y BRAND-CAND-008..009 elegibles sin abrir.
version: 0.5.6
status: screening-closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-03
updated: 2026-10-13
tags:
  - brand
  - fitness
  - exploration
  - reusable-brand-system
related:
  - si-brand-001
  - si-brand-002
  - si-brand-003
---

# Marca Fitness — Screening cerrado

<!-- BRAND-CAND-007-F0-F3-CHECKPOINT:START -->
## BRAND-CAND-007 — checkpoint F0–F3 (2026-10-13)

**F0–F3 CLOSED / aut128 PASS / Demanda 3/5 / Confianza Media**. F3 ejecutada COLLABORATIVE con aprobación explícita del Founder. Seis publicaciones verificadas y trazables; sin Product Bases. Próximo gate **F4 — Competencia AUTO**, sobre la misma cohorte de F3. Checkpoint siguiente al finalizar F6. Research `SI-RESEARCH-089..092`. SHA-256 de aut128: `3fd9bce9fe32866ea30f33e26e3b3eaf9753a36e3223faf200618f8c8c4aba30`.
<!-- BRAND-CAND-007-F0-F3-CHECKPOINT:END -->

<!-- BRAND-CAND-010-DOCUMENTARY-CHECKPOINT:START -->
## Checkpoint operativo — BRAND-CAND-010 Method v2 cerrado / 2026-10-08

```text
SCREENING: CLOSED
METHOD V2: F0–F13 CLOSED
F13 MATRIX: matrix-aut118-brand-cand-010-phase13-final-corrected.xlsx
F13 SHA-256: 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a
POST-CLOSE BASELINE: matrix-aut123-brand-cand-010-post-close-core-snapshot-reconciliation.xlsx
POST-CLOSE SHA-256: 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb
Data Fidelity Preflight: PASS
Matrix Validator: PASS / errors 0 / warnings 0 / info 0
F14: NOT OPENED

FINAL RESULT: NO PORTFOLIO FINALIST

BASE-FIT-001 — Walking pad compacta under-desk
→ STOP — REOPENABLE / LOGISTICS GATE
→ principal hipótesis de reapertura

BASE-FIT-002 — Pedalera compacta under-desk
→ STOP — REOPENABLE / DEMAND + LOGISTICS GATE

BASE-FIT-003 — Elíptica compacta under-desk
→ DEFER — LOW DEMAND PROOF

BASE-FIT-004 — Balance board para standing desk
→ DEFER — LOW DEMAND PROOF / STANDING-DESK DEPENDENCY

BRAND-CAND-007 → F0–F3 CLOSED / aut128 PASS / F4 NEXT
BRAND-CAND-008 → ELIGIBLE — NOT OPENED
BRAND-CAND-009 → ELIGIBLE — NOT OPENED
```

La walking pad queda como principal hipótesis de reapertura porque fue la única arquitectura con demanda local específica defendible, pero el screen de landed cost aéreo la deja fuera de shortlist final. Reabrir exige evidencia logística marítima/LCL decision-grade y validación de requisitos eléctricos, QA y postventa.

`NO FINALIST` no equivale a descartar definitivamente el candidato. Significa que, con la evidencia disponible y los supuestos comparables del Method v2, ninguna Product Base justifica pasar hoy a Portfolio Review como finalista.

Próximo gate de Marca Fitness: completar la revisión y el commit/push humano del checkpoint F0–F3 de `BRAND-CAND-007`; después continuar **el mismo candidato** en F4–F6 AUTO, con checkpoint documental al terminar F6. `BRAND-CAND-008..009` siguen elegibles sin abrir. No abrir candidatos en paralelo.
<!-- BRAND-CAND-010-DOCUMENTARY-CHECKPOINT:END -->

## 1. Estado vigente

```text
Architecture baseline: v0.2
Territory baseline: FROZEN
Missions baseline: FROZEN
Brand Candidate Screening: CLOSED
Formal candidates: BRAND-CAND-007..010
PASS TO METHOD V2: 4
Method v2: BRAND-CAND-010 F0 OPENED / MATRIX PENDING / NOT CLOSED
Product Bases: NOT DEFINED
Purchase Decision: NONE
```

## 2. Territorio vigente

> **Ayudar a personas a conservar, recuperar y desarrollar capacidad física en una vida cotidiana marcada por sedentarismo, poco tiempo y espacios limitados, mediante soluciones simples, compactas, comprensibles y sostenibles en el tiempo.**

`+50` permanece como contexto/segmento potencial a explorar; no define la marca.

## 3. Misiones

```text
M1 — Construir y conservar fuerza útil
M2 — Incorporar movimiento y entrenamiento en la vida cotidiana
M3 — Conservar y recuperar movilidad, estabilidad y capacidad física
M4 — Entender el progreso y sostener la constancia
```

## 4. Lifecycle de IDs

| Hypothesis ID | Formal Candidate ID | Candidate | Territory Relationship | Decision |
|---|---|---|---|---|
| `FIT-CAND-001` | [`BRAND-CAND-007`](./candidates/brand-cand-007-accessible-compact-strength.md) | Fuerza accesible y compacta | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-002` | [`BRAND-CAND-008`](./candidates/brand-cand-008-flexible-portable-training.md) | Entrenamiento flexible y portátil | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-005` | [`BRAND-CAND-009`](./candidates/brand-cand-009-mobility-stability-physical-capacity.md) | Movilidad, estabilidad y conservación/recuperación de capacidad física | `CORE` | `PASS TO METHOD V2` |
| `FIT-CAND-007` | [`BRAND-CAND-010`](./candidates/brand-cand-010-integrated-movement-sedentary-day.md) | Movimiento integrado a la jornada sedentaria | `CORE` | `PASS TO METHOD V2` |

## 5. Hipótesis no promovidas

```text
FIT-CAND-003 → MERGED INTO FIT-CAND-005 → sin ID formal propio
FIT-CAND-004 → MERGED INTO FIT-CAND-001 → sin ID formal propio
FIT-CAND-006 → TRANSVERSAL CAPABILITY: Medición + feedback + constancia → sin ID formal propio
```

Los IDs históricos se preservan y no se reutilizan.

## 6. Documentos

- [`Candidate Hypotheses v0.1`](./fitness-candidate-hypotheses-v0.1.md) — historial de hipótesis.
- [`Pre-screening Architecture v0.2`](./fitness-pre-screening-architecture-v0.2.md) — baseline del screening.
- [`Brand Candidates`](./candidates/README.md) — índice vigente y expedientes.
- [`SI-BRAND-002`](../../si-brand-002-brand-candidate-screening-method.md) — método reusable de screening.
- [`SI-BRAND-003`](../../si-brand-003-opportunity-intake-and-discovery.md) — ingreso de futuras oportunidades.

## 7. Ejecución Method v2

```text
BRAND-CAND-010
→ FIRST FITNESS CANDIDATE
→ F0 ANALYSIS COMPLETE
→ MATRIX MATERIALIZATION PENDING
→ F0 NOT CLOSED

BRAND-CAND-007 → F0–F3 CLOSED / aut128 PASS / F4 NEXT
BRAND-CAND-008..009 → ELIGIBLE — NOT OPENED
```

Research vigente: [`SI-RESEARCH-070`](../../../06-research/brand-fitness/si-research-070-brand-cand-010-method-v2-agile-phase-0-research-brief.md).

BRAND-CAND-010 creó formalmente `BASE-FIT-001`..`BASE-FIT-004` en F6; ninguno quedó seleccionado como portfolio finalist. La prioridad comercial inmediata de Marca Hogar no cambia.

## Changelog

| Version | Fecha | Cambio |
|---|---|---|
| 0.5.6 | 2026-10-13 | Checkpoint BRAND-CAND-007 F0–F3, aut128 PASS, F4 siguiente. |
| 0.5.0 | 2026-10-05 | Se abre Method v2 para BRAND-CAND-010: F0 Research Brief completo en SI-RESEARCH-070; materialización y Validator pendientes; 007–009 permanecen elegibles sin abrir. |
| 0.4.0 | 2026-10-05 | Se cierra el primer bloque de Brand Candidate Screening: FIT-CAND-001/002/005/007 promueven a BRAND-CAND-007..010, todos CORE / PASS TO METHOD V2; Method v2 permanece sin abrir. |
| 0.3.0 | 2026-10-05 | Se congela Fitness v0.2 como baseline pre-screening: territorio revisado, cuatro misiones, cuatro candidatos activos, FIT-CAND-003/004 absorbidos y FIT-CAND-006 reclasificado como capacidad transversal. |
| 0.2.0 | 2026-10-05 | Se integra SI-BRAND-003 y se habilitan rutas de descubrimiento descendente y ascendente antes del Brand Candidate Screening. |
| 0.1.0 | 2026-10-03 | Se abre Marca Fitness como exploración reusable del Brand System. |

<!-- BRAND-CAND-010-RECONCILIATION:START -->
## BRAND-CAND-010 — baseline reconciliada vigente

`matrix-aut123-brand-cand-010-post-close-core-snapshot-reconciliation.xlsx` / `23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb` es la baseline post-close vigente tras Data Fidelity Preflight v2.4 PASS + Matrix Validator PASS.

```text
aut118 → F13 histórico / 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a
aut119 corrected → reconciliación intermedia / superseded before publication
aut120 → data-fidelity baseline / 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2 / SUPERSEDED
aut121 → primera materialización / Matrix Validator FAIL por vocabulario
aut121 corrected → marketplace economics / dual PASS / SUPERSEDED / 7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc
aut122 → current-core materialization / v2.3 PASS / SUPERSEDED / 67e850c0a40fb274629429587f9ce5b500eddb51da6580fccb2c48f060dba4ba
aut123 → core + pre-projection snapshot / CURRENT / 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb
```

`aut123` conserva snapshot pre-proyección, ledger de verificaciones y core vigente.

Resultado estratégico sin cambios: NO PORTFOLIO FINALIST / FREEZE / F14 NOT OPENED.
<!-- BRAND-CAND-010-RECONCILIATION:END -->
