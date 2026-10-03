---
id: si-research-057
title: BRAND-CAND-006 — Method v2 Agile — Fase 1 — Market / Solution Map
description: Mapa retrospectivo de arquitecturas y sustitutos relevantes para BASE-PET-003.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-03
updated: 2026-10-03
brand: brand-hogar
brand_candidate: brand-cand-006
method: method-v2-agile
phase: F1
---

# SI-RESEARCH-057 — BRAND-CAND-006 — Fase 1 — Market / Solution Map

## 1. Boundary

El mapa no parte de la categoría comercial `Pet Care`, sino del job:

> Gestionar residuos sanitarios de gatos dentro del hogar reduciendo trabajo repetitivo, manipulación y fricción de mantenimiento.

## 2. Arquitecturas

```text
S0 — arenero manual
A1 — arenero automático rotativo cerrado / BASE-PET-002
A2 — arenero automático open-top / BASE-PET-003
A3 — arenero automático de rastrillo / BASE-PET-004
```

`A2` es el active scope de `BRAND-CAND-006`.

## 3. Ejes comparativos

- mecanismo de separación;
- geometría y acceso del gato;
- arquitectura de seguridad;
- manejo de residuo y olor;
- limpieza y mantenimiento;
- experiencia del animal;
- experiencia del usuario.

## 4. Regla metodológica

```text
MISMO JOB ≠ MISMA ARQUITECTURA
MISMA CATEGORÍA ≠ MISMO PRODUCT BASE
```

Las diferencias mecánicas cambian seguridad, adaptación, mantenimiento y postventa; por lo tanto deben conservarse como Product Bases separados.

## 5. Checkpoint

```text
Matrix: matrix-aut92-brand-cand-006-phase1.xlsx
Validator: PASS
SHA-256: 2778f5ed48a883678de94b251832baca34eec0a2ce1180346340d3b060218e55
F1: CLOSED
F14: NOT OPENED
```

## 6. Próximo gate

`F2 — Maturity`.
