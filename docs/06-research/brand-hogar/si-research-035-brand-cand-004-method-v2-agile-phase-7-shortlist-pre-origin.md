---
id: si-research-035
title: BRAND-CAND-004 — Method v2 Agile — F7 Shortlist pre-origin
description: Shortlist pre-origen de Product Bases para monitoreo doméstico del consumo energético.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-25
updated: 2026-09-25
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-004
  - energy-monitoring
  - phase-7
  - shortlist
related:
  - si-research-028
  - si-research-029
  - si-research-030
  - si-research-031
  - si-research-032
  - si-research-033
  - si-research-034
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F7 Shortlist pre-origin

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input vigente

F6 quedó formalmente cerrada sobre:

```text
matrix-aut65-brand-cand-004-phase6.xlsx
SHA-256: a5e5259dafaf8b88cde7553006bb59d88e09205ef5b95bd116f8e08859f311f8
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Product Bases normalizadas: `BASE-HOGAR-016..023`.

## 2. Objetivo

Reducir el conjunto elegible antes de F8 para no gastar sourcing normal sobre todas las configuraciones plausibles.

```text
GOOD COMMERCIAL OPPORTUNITY ≠ GOOD FIRST PRODUCT
COMPLEXITY = RISK ≠ AUTOMATIC EXCLUSION
SHORTLIST ≠ ALL PLAUSIBLE PRODUCT BASES
```

Sesgo de primera etapa:

```text
simple import / regulation / logistics
low installation friction
manageable safety
low cloud dependency
manageable post-sale
easy-to-explain benefit
```

## 3. Decisiones

### BASE-HOGAR-016 — Medidor enchufable standalone

```text
PASS TO ORIGIN — CORE / FIRST-STAGE FIT
```

Instalación trivial, medición directa, sin dependencia de cloud y job fácil de explicar. F8 debe confirmar 220–240V/50Hz, plug compatible, 16A cuando aplique, memoria/persistencia y especificaciones defendibles.

### BASE-HOGAR-017 — Smart plug + monitoring

```text
PASS TO ORIGIN — CONDITIONED / CORE / COMMODITY CHECK
```

Demanda muy fuerte e instalación simple, pero con commodity risk elevado y dependencia de ecosistemas Tuya/Smart Life. F8 debe verificar si existe una configuración diferenciable más allá de app/precio.

### BASE-HOGAR-018 — Tomacorriente smart embutido

```text
OUT OF SHORTLIST — SUPPORT_PB / ADJACENT
```

Agrega instalación fija y seguridad sin ventaja suficiente frente a 017 para consumir sourcing normal.

### BASE-HOGAR-019 — Medidor DIN directo

```text
PASS TO ORIGIN — CONDITIONED / CORE TECHNICAL
```

Tiene la demanda más directamente atribuible a medición/submedición y baja dependencia digital. Queda condicionado por instalación en tablero, safety, accuracy y certificaciones.

### BASE-HOGAR-020 — Protector DIN smart + monitoring

```text
HOLD
```

La función de protección/corte agrega safety, claims, certificaciones y postventa. No se prioriza mientras 019 cubra el job con menor carga.

### BASE-HOGAR-021 — Split-CT standalone

```text
HOLD / WATCHLIST
```

Interesante técnicamente y sin cloud obligatorio, pero con demanda visible limitada e instalación técnica.

### BASE-HOGAR-022 — Whole-home CT conectado

```text
HOLD
```

Buen service layer potencial, pero menor demanda visible, instalación CT, dependencia digital y mayor soporte.

### BASE-HOGAR-023 — Multi-circuit CT

```text
HOLD — HIGHLY CONDITIONED
```

Demanda visible débil, ticket alto, configuración/instalación e integraciones elevan demasiado el service burden para primera etapa.

## 4. Shortlist activa para F8

```text
CORE
→ BASE-HOGAR-016
→ BASE-HOGAR-019

CONDITIONED CORE / COMMODITY CHECK
→ BASE-HOGAR-017
```

No activos:

```text
OUT OF SHORTLIST
→ BASE-HOGAR-018

HOLD / WATCHLIST
→ BASE-HOGAR-020
→ BASE-HOGAR-021
→ BASE-HOGAR-022
→ BASE-HOGAR-023
```

## 5. Gate F7

Resultado conceptual:

```text
PASS
```

La shortlist reduce siete PB elegibles a tres configuraciones suficientemente distintas para F8:

```text
016 → plug-level simple
017 → plug-level conectado / commodity check
019 → DIN directo / technical trust
```

## 6. Materialización

Se agrega:

```text
EVID-0262 — Shortlist pre-origen
SRC-0429 — análisis interno F7
EVSRC-0532
```

y se actualizan las notas de `BASE-HOGAR-016..023`.

Archivo preparado:

```text
matrix-aut66-brand-cand-004-phase7.xlsx
SHA-256: 4ac98fdeec6d357a6d861de095341c542a216558e3887f14e67aacd7a4798474
```

## 7. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut66
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F7 CLOSED
```

Validación oficial:

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: 4ac98fdeec6d357a6d861de095341c542a216558e3887f14e67aacd7a4798474
```

F8 queda formalmente abierta después de este cierre.

## 8. Próxima acción

F7 queda `CLOSED`. Ejecutar `F8 — Origin Screening` en modalidad `AUTO` sólo para `BASE-HOGAR-016`, `017` y `019`.

## 9. Changelog

### 2026-09-25 — v0.1.0

- F6 queda formalmente cerrada sobre `aut65 PASS`;
- 016 pasa a F8 como CORE / FIRST-STAGE FIT;
- 017 pasa condicionado como CORE / COMMODITY CHECK;
- 019 pasa condicionado como CORE TECHNICAL;
- 018 queda fuera de shortlist;
- 020..023 quedan HOLD/WATCHLIST;
- se prepara `matrix-aut66-brand-cand-004-phase7.xlsx`;
- `aut66` obtiene PASS limpio y F7 queda formalmente `CLOSED`;
- siguiente fase: `F8 — Origin Screening` en AUTO.
