---
id: si-research-049
title: BRAND-CAND-005 — Method v2 Agile — F7 Shortlist pre-origin
description: Shortlist pre-origen de Product Bases para compostaje y procesamiento doméstico de residuos orgánicos.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-28
updated: 2026-09-28
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-005
  - organic-waste
  - phase-7
  - shortlist
phase: business-intelligence
---

# BRAND-CAND-005 — Method v2 Agile — F7 Shortlist pre-origin

Fecha: 2026-09-28  
Estado: `CLOSED`

## 1. Input vigente

F6 quedó formalmente cerrada sobre:

```text
matrix-aut82-brand-cand-005-phase6.xlsx
SHA-256: a6e5526390208e040b601faa5cf2498f024bf361bc482988bdd8887b6b59fd16
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Product Bases normalizadas:

```text
BASE-HOGAR-024
BASE-HOGAR-025
BASE-HOGAR-026
BASE-HOGAR-027
BASE-HOGAR-028
BASE-HOGAR-029
```

`BASE-HOGAR-029` ya llega como `SUPPORT_PB / ADJACENT`.

## 2. Objetivo

Reducir el conjunto elegible antes de F8 para no consumir sourcing normal sobre todas las configuraciones plausibles.

```text
GOOD COMMERCIAL OPPORTUNITY ≠ GOOD FIRST PRODUCT
COMPLEXITY = RISK ≠ AUTOMATIC EXCLUSION
SHORTLIST ≠ ALL PLAUSIBLE PRODUCT BASES
LOW COMPETITION ≠ HIGH OPPORTUNITY
```

Sesgo de primera etapa:

```text
simple import / regulation / logistics
low fragility
manageable size / weight
simple installation / use
low electrical complexity
low cloud dependency
manageable post-sale
easy-to-explain benefit
```

## 3. Decisiones

### BASE-HOGAR-024 — Compostera modular apilable 40–60 L

```text
PASS TO ORIGIN — CORE / FIRST-STAGE FIT
```

Razones:

- demanda local observable;
- arquitectura simple;
- sin electricidad;
- baja carga regulatoria esperable;
- buena compatibilidad con cocina/balcón/patio;
- posibilidad de modularidad y bundle;
- service layer manejable.

Condiciones para F8:

- disponibilidad de moldes/configuraciones OEM;
- posibilidad de nesting/packing eficiente;
- dimensiones y peso reales;
- materiales;
- drenaje/canilla;
- estabilidad de módulos;
- MOQ y branding.

### BASE-HOGAR-025 — Compostera giratoria 120 L doble cámara

```text
PASS TO ORIGIN — CONDITIONED / CORE / LOGISTICS CHECK
```

Razones:

- mayor tracción visible del candidato (`+1000`);
- mecanismo maduro;
- beneficio fácil de explicar;
- sin electricidad ni cloud;
- diferenciación posible por estructura y experiencia de uso.

Condiciones:

- volumen logístico;
- packing desarmado;
- eje/cierres;
- estructura/base;
- durabilidad UV;
- montaje;
- calidad del plástico;
- MOQ.

No se asume que la mayor venta local compense cualquier costo logístico.

### BASE-HOGAR-026 — Vermicompostera dedicada

```text
HOLD / WATCHLIST
```

Razones:

- living-system dependency;
- mayor fricción de onboarding;
- necesidad de temperatura/humedad adecuadas;
- restricciones de alimento;
- logística separada del starter/lombrices;
- señal de demanda menos fuerte;
- solapamiento parcial con BASE-HOGAR-024, que puede ser vermicompost-compatible.

Reabrir si:

- origen muestra una configuración claramente superior;
- 024 no ofrece una experiencia viable;
- se confirma un starter/service layer local simple.

### BASE-HOGAR-027 — Bokashi twin-bin + starter

```text
HOLD / WATCHLIST
```

Razones:

- demanda local débil;
- oferta observada principalmente importada;
- dependencia de inoculante;
- post-proceso obligatorio;
- riesgo de claims;
- necesidad de asegurar reposición.

La baja competencia visible no justifica sourcing normal en esta etapa.

### BASE-HOGAR-028 — Procesador térmico countertop 3–4 L

```text
PASS TO ORIGIN — CONDITIONED / TECH-SERVICE-ECONOMICS CHECK
```

Este PASS no significa first-stage fit.

Razones para consumir un screening público limitado:

- ticket local observado > ARS 1 M;
- job claramente distinto de A1–A4;
- potencial de reducción fuerte de fricción;
- posibilidad de descubrir una brecha económica material si el costo OEM es muy inferior al retail importado.

Condiciones críticas:

- 220–240 V / 50 Hz;
- consumo;
- peso y volumen;
- ruido;
- filtro de carbón;
- costo/reposición de filtros;
- motor/cuchillas;
- limpieza;
- ciclo;
- garantía;
- MOQ;
- repuestos;
- claims de output.

Regla:

```text
PASS TO ORIGIN
≠
PASS AS FIRST PRODUCT
```

F8 debe determinar si la economía potencial siquiera justifica mantenerla viva.

### BASE-HOGAR-029 — Triturador de jardín

```text
OUT OF SHORTLIST — SUPPORT_PB / ADJACENT
```

No resuelve el core de residuos orgánicos de cocina.

Permanece sólo como benchmark y trazabilidad.

## 4. Shortlist activa para F8

```text
BASE-HOGAR-024
→ CORE / FIRST-STAGE FIT

BASE-HOGAR-025
→ CONDITIONED / CORE / LOGISTICS CHECK

BASE-HOGAR-028
→ CONDITIONED / TECH-SERVICE-ECONOMICS CHECK
```

Watchlist:

```text
BASE-HOGAR-026
BASE-HOGAR-027
```

Fuera de shortlist:

```text
BASE-HOGAR-029
```

## 5. Implicación para F8

F8 debe buscar disponibilidad pública de origen y comparables suficientes para:

### 024

```text
modular / stackable compost bin
40–60 L
drainage / tap
nesting / packing
material
MOQ
branding
```

### 025

```text
tumbling composter
~120 L
dual chamber
knock-down packing
frame / axle
UV-resistant plastic
MOQ
```

### 028

```text
electric food recycler
3–4 L
220–240 V / 50 Hz
drying + grinding + cooling
carbon filter
noise / power
weight / dimensions
MOQ
public price
```

F8 no debe dedicar sourcing normal a 026/027 salvo que aparezca evidencia incidental material.

## 6. Gate F7

Resultado conceptual:

```text
PASS
```

La shortlist conserva:

- dos Product Bases con fuerte encaje de primera etapa o demanda observable;
- una Product Base tecnológica de mayor riesgo, retenida sólo porque el ticket local justifica verificar si existe una brecha económica material.

Esto mantiene el método disciplinado sin convertir complejidad en exclusión automática.

## 7. Materialización en matriz

F7 agrega:

```text
Fuentes
→ SRC-0464

Evidencias
→ EVID-0276

Evidencia Fuentes
→ EVSRC-0602
```

No agrega una nueva evaluación de los 10 criterios.

Archivo preparado:

```text
matrix-aut83-brand-cand-005-phase7.xlsx
SHA-256: 1dae4557ecd0de4182d47fb3bae0d11d0feeb3aef901e5b4e2abdfdfb7d04fdb
```

## 8. Estado formal de F7

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut83
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
SHA-256: 1dae4557ecd0de4182d47fb3bae0d11d0feeb3aef901e5b4e2abdfdfb7d04fdb
Report: aut83-brand-cand-005-phase7-validation-report.json
```

F8 queda formalmente abierta después de este cierre.

## 9. Próxima acción

Validar `aut83`.

Resultado ejecutado:

```text
F7 CLOSED — aut83 PASS
→ F8 — Origin Screening
→ AUTO
```
