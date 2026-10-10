---
id: si-research-087
title: BRAND-CAND-010 — Post-close Core Marketplace Materialization
description: Reconciliación post-cierre que materializa en Publicaciones ML los campos core Precio ARS, Precio USD y Ventas visibles desde la capa de verificación vigente.
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
  - si-decision-019
  - si-bim-001
  - si-bim-proc-003
---

# SI-RESEARCH-087 — BRAND-CAND-010 — Post-close Core Marketplace Materialization

## 1. Motivo

La revisión humana de `aut121 corrected` detectó una inconsistencia de representación:

- la capa de verificación marketplace `AB:AM` estaba completa;
- pero las columnas core de `Publicaciones ML` —`Precio ARS`, `Precio USD`, `Ventas visibles`— seguían incompletas o desactualizadas para varias publicaciones Fitness.

El dato existía, pero la hoja principal no lo materializaba.

## 2. Regla corregida

```text
ACTIVE CORE = VERIFIED CURRENT LAYER
```

Para una publicación `ACTIVE`:

```text
Precio ARS core = Precio ARS Verificado
Precio USD core = Precio USD Verificado
Ventas visibles core = Ventas visibles Verificadas
```

`Verificaciones ML` conserva el historial temporal append-only.

Para `HISTORICAL_ONLY / SOURCE_UNAVAILABLE` no se inventa un precio actual.

## 3. Resultado materializado

```text
ML-0152..ML-0177
26 publicaciones Fitness

ACTIVE: 21
→ core Precio ARS completo: 21/21
→ core Precio USD completo: 21/21
→ core Ventas visibles completo: 21/21
→ core sincronizado con capa verificada: 21/21

HISTORICAL_ONLY: 5
→ ML-0159
→ ML-0166
→ ML-0173
→ ML-0174
→ ML-0175
→ Precio ARS/USD no inventado
→ Ventas visibles = No informadas
```

## 4. Efecto sobre demanda

```text
EVAL-0029 = 3/5
Confidence = Media
```

No cambia score ni decisión.

## 5. Lineage

```text
matrix-aut121-brand-cand-010-post-close-marketplace-economics-reconciliation-corrected.xlsx
→ marketplace economics reconciliation
→ dual PASS
→ verificación económica completa
→ core de Publicaciones ML incompleto
→ SUPERSEDED
→ 7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc

matrix-aut122-brand-cand-010-post-close-core-marketplace-reconciliation.xlsx
→ core marketplace materialization
→ Core Marketplace Fidelity: PASS
→ Data Fidelity Preflight v2.3: PASS
→ Matrix Validator: PASS
→ errors 0 / warnings 0 / info 0
→ SUPERSEDED BY aut123
→ 67e850c0a40fb274629429587f9ce5b500eddb51da6580fccb2c48f060dba4ba
```

## 6. Defensa de regresión

Data Fidelity Preflight sube a `v2.3`.

Toda fila `ACTIVE` debe satisfacer:

```text
core Precio ARS = verified Precio ARS
core Precio USD = verified Precio USD
core Ventas visibles = verified Ventas visibles
```

Una matriz con el patrón de `aut121 corrected` debe fallar automáticamente con reglas `DF-CORE-*`.

## 7. Estado estratégico

```text
BRAND-CAND-010 → NO PORTFOLIO FINALIST / FREEZE
F0–F13 → CLOSED
F14 → NOT OPENED
```

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-10 | Materializa core marketplace y agrega defensa de regresión v2.3. |


## Supersession

`matrix-aut122-brand-cand-010-post-close-core-marketplace-reconciliation.xlsx` / `67e850c0a40fb274629429587f9ce5b500eddb51da6580fccb2c48f060dba4ba` queda `SUPERSEDED` por `aut123`.

Motivo: `aut122` materializó correctamente el core vigente, pero no preservó como estructura tabular independiente el estado core pre-proyección.

`aut123` agrega `Snapshot Pre-Proyección ML`.

No cambia score ni decisión.
