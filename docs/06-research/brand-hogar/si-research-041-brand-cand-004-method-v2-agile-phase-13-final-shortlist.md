---
id: si-research-041
title: BRAND-CAND-004 — Method v2 Agile — F13 Final Shortlist
description: Cierre de shortlist final para monitoreo doméstico del consumo energético.
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
  - phase-13
  - final-shortlist
related:
  - si-research-040
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F13 Final Shortlist

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input

F12 quedó formalmente cerrada sobre:

```text
matrix-aut71-brand-cand-004-phase12.xlsx
SHA-256: 7a19864d60fff48ef5a8f0a71b00866700b1d9de25f0c28cd437a2fc8b8c1b24
Result: PASS
```

Funnel al abrir F13:

```text
ACTIVE
→ BASE-HOGAR-016

STOP — REOPENABLE
→ BASE-HOGAR-017
→ BASE-HOGAR-019
```

## 2. Regla F13

F13 no recalcula economía, no reabre sourcing y no selecciona proveedor.

Integra:

```text
demanda
+ competencia
+ potencial de marca
+ economía
+ facilidad operativa
+ calidad de evidencia
+ complejidad / riesgo
```

Salida permitida:

```text
FINALIST
FINALIST — CONDITIONED
HOLD
STOP
```

Reglas:

```text
FINALIST ≠ GANADOR
ELIGIBLE FOR PORTFOLIO REVIEW ≠ SELECTED PRODUCT
PORTFOLIO REVIEW READY ≠ PASS TO F14
```

## 3. BASE-HOGAR-016 — Medidor enchufable standalone de consumo

Resultado:

```text
FINALIST — CONDITIONED
ELIGIBLE FOR PORTFOLIO REVIEW
```

### Por qué permanece

El Product Base combina:

```text
demanda observable
medición directa por artefacto
instalación simple
baja dependencia de cloud/app
beneficio fácil de explicar
economía suficiente en 50 y 100 unidades
```

Resultados económicos F12:

```text
50 u
→ margen ~43,06%
→ ROI sobre costo económico ~85,66%

100 u
→ margen ~57,57%
→ ROI sobre costo económico ~161,00%
```

Además, frente a arquitecturas DIN/CT o smart conectadas, tiene una carga inicial menor de instalación y soporte.

### Por qué queda condicionado

La evidencia todavía no alcanza para considerarlo procurement-ready.

Condiciones:

```text
accuracy / test evidence
16A y 220–240V / 50Hz en configuración exacta
plug Argentina/AU exacto
packing/peso same-SKU
memoria / persistencia según propuesta final
documentación y certificaciones
revisión externa / importación
```

La promesa de marca debe mantenerse acotada:

```text
medir
→ comprender
→ decidir

NO:

monitoring
→ ahorro garantizado
```

## 4. BASE-HOGAR-017 — Smart plug + monitoring

Estado confirmado:

```text
STOP — REOPENABLE
```

F12 deja economía negativa en ambos escenarios modelados y el PB conserva commodity risk alto.

No vuelve al camino activo salvo cambio material en:

```text
costo real
escala / consolidación
precio defendible
diferenciación
arquitectura comercial
```

La disponibilidad de Tuya/Smart Life no constituye por sí sola ventaja de marca.

## 5. BASE-HOGAR-019 — Medidor DIN directo

Estado confirmado:

```text
STOP — REOPENABLE
```

Aunque la demanda por submedición es clara y a 100 unidades se aproxima al break-even, el escenario sigue sin alcanzar el objetivo económico.

También permanecen:

```text
safety
accuracy / class
certificación
instalación profesional
```

No se justifica mantenerlo en el recorrido activo sin un cambio económico o técnico material.

## 6. Resultado final del candidato

```text
BRAND-CAND-004

FINALIST — CONDITIONED
→ BASE-HOGAR-016

STOP — REOPENABLE
→ BASE-HOGAR-017
→ BASE-HOGAR-019
```

Los PB 018 y 020–023 permanecen en los estados definidos antes de sourcing:

```text
018 → SUPPORT_PB / ADJACENT
020 → HOLD
021 → HOLD / WATCHLIST
022 → HOLD
023 → HOLD — HIGHLY CONDITIONED
```

## 7. Estado de BRAND-CAND-004

Al obtener PASS del Matrix Validator para `aut72`:

```text
F0–F13 CLOSED
PORTFOLIO REVIEW READY
FREEZE
F14 NOT OPENED
```

No corresponde profundizar procurement, supplier negotiation ni certificación específica antes de la comparación transversal del portfolio y del gate externo.

## 8. Gate F13

Resultado conceptual:

```text
PASS
```

Justificación:

- existe un único PB activo con economía suficiente;
- su arquitectura tiene buen fit para primera etapa;
- las condiciones pendientes están explicitadas;
- las alternativas económicamente débiles quedan fuera del camino activo;
- no se confunde finalist con selección final.

## 9. Materialización

F13 agrega:

```text
EVID-0268
SRC-0444
EVSRC-0561
RES-MARG-0018
```

y actualiza las notas de:

```text
BASE-HOGAR-016
BASE-HOGAR-017
BASE-HOGAR-019
```

Archivo preparado:

```text
matrix-aut72-brand-cand-004-phase13.xlsx
SHA-256: 560fd2073da35327babe7a473c726e012f8d5496223f98c9d4f1dd5212948ced
```

## 10. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut72
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F13 CLOSED
```

## 11. Validación oficial

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: 560fd2073da35327babe7a473c726e012f8d5496223f98c9d4f1dd5212948ced
```

## 12. Próxima acción

`aut72` obtuvo PASS limpio. `BRAND-CAND-004` queda `PORTFOLIO REVIEW READY / FREEZE`; F14 permanece `NOT OPENED`. La siguiente ejecución sólo puede comenzar después de completar el cierre documental del candidato en el repositorio `smart-imports`.

## 13. Changelog

### 2026-09-25 — v0.1.0

- F12 queda formalmente cerrada sobre `aut71 PASS`;
- `BASE-HOGAR-016` queda `FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW`;
- `BASE-HOGAR-017` y `BASE-HOGAR-019` permanecen `STOP — REOPENABLE`;
- BRAND-CAND-004 queda preparado para `PORTFOLIO REVIEW READY / FREEZE`;
- F14 permanece `NOT OPENED`;
- se agrega `RES-MARG-0018`;
- se prepara `matrix-aut72-brand-cand-004-phase13.xlsx`;
- `aut72` obtiene PASS limpio y F13 queda formalmente `CLOSED`;
- `BRAND-CAND-004` queda `PORTFOLIO REVIEW READY / FREEZE`;
- F14 permanece `NOT OPENED`;
- antes de abrir BRAND-CAND-005 debe completarse el cierre documental en `smart-imports`.
