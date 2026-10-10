---
id: si-research-088
title: BRAND-CAND-010 — Post-close Core + Snapshot Reconciliation
description: Reconciliación post-cierre que mantiene el core marketplace vigente y preserva estructuralmente el estado pre-proyección.
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
  - si-research-086
  - si-research-087
  - si-decision-019
  - si-bim-001
  - si-bim-proc-003
---

# SI-RESEARCH-088 — BRAND-CAND-010 — Post-close Core + Snapshot Reconciliation

## 1. Motivo

`aut122` resolvió la inconsistencia operacional detectada en `Publicaciones ML`: las filas `ACTIVE` materializaron Precio ARS, Precio USD y Ventas visibles desde la verificación vigente.

La revisión pre-staging detectó una tensión con otra regla canónica:

```text
CURRENT VERIFICATION ≠ HISTORICAL CAPTURE
```

Al proyectar la verificación vigente sobre el core, valores históricos previos podían dejar de estar disponibles como estructura tabular independiente.

Ejemplo:

```text
ML-0160
estado pre-proyección: +500
verificación vigente: +100
core proyectado: +100
```

## 2. Solución

`aut123` conserva tres capas explícitas:

```text
Snapshot Pre-Proyección ML
→ estado core inmediatamente anterior a la proyección

Verificaciones ML
→ historial temporal append-only

Publicaciones ML
→ proyección operacional vigente
```

Nueva regla:

```text
CURRENT CORE PROJECTION REQUIRES PRE-PROJECTION SNAPSHOT
```

## 3. Resultado

```text
Fitness publications: 26
Snapshot rows: 26
ACTIVE current core: 21
HISTORICAL_ONLY: 5

ML-0160 temporal proof:
pre-projection snapshot = +500
current verified/core = +100
```

Baseline preservada por el snapshot:

```text
matrix-aut121-brand-cand-010-post-close-marketplace-economics-reconciliation-corrected.xlsx
7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc
```

## 4. Validación

`aut123` fue materializada y validada inicialmente con:

```text
Core + Snapshot Fidelity: PASS
Data Fidelity Preflight v2.3: PASS
Matrix Validator full-matrix-v5 0.7.0: PASS
errors: 0
warnings: 0
info: 0
```

Checkpoint final v2.4:

```text
Data Fidelity Preflight v2.4: PASS
Matrix Validator full-matrix-v5 0.7.0: PASS
errors: 0
warnings: 0
info: 0
```

El governance se fortaleció a Data Fidelity Preflight `v2.4`, incorporando reglas `DF-SNP-*`. `aut123` volvió a ejecutar el checkpoint canónico y obtuvo PASS bajo v2.4.

## 5. Lineage

```text
aut121 corrected
→ marketplace economics
→ dual PASS
→ core operativo incompleto/stale
→ SUPERSEDED
→ 7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc

aut122
→ core marketplace materialization
→ v2.3 PASS
→ snapshot pre-proyección no preservado estructuralmente
→ SUPERSEDED
→ 67e850c0a40fb274629429587f9ce5b500eddb51da6580fccb2c48f060dba4ba

aut123
→ core + snapshot
→ Core + Snapshot Fidelity PASS
→ Data Fidelity Preflight v2.4 PASS
→ Matrix Validator PASS / errors 0 / warnings 0 / info 0
→ CURRENT POST-CLOSE BASELINE
→ 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb
```

## 6. Efecto estratégico

No cambia score ni decisión:

```text
EVAL-0029 = 3/5
Confidence = Media

BRAND-CAND-010
→ NO PORTFOLIO FINALIST / FREEZE
→ F0–F13 CLOSED
→ F14 NOT OPENED
```

## 7. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-10 | Preserva estructuralmente el estado pre-proyección y adopta el modelo de tres capas core / verification / snapshot. |
