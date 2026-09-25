---
id: si-research-034
title: BRAND-CAND-004 — Method v2 Agile — F6 Product Bases
description: Normalización de Product Bases comercialmente significativas para monitoreo doméstico del consumo energético.
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
  - phase-6
  - product-bases
related:
  - si-research-028
  - si-research-029
  - si-research-030
  - si-research-031
  - si-research-032
  - si-research-033
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F6 Product Bases

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input vigente

F5 quedó formalmente cerrada sobre:

```text
matrix-aut64-brand-cand-004-phase5.xlsx
SHA-256: 3ea5842b135c800c525133f064b38774915dba210e2874d3da54f07f90e738ba
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Evaluaciones acumuladas:

```text
Demanda             4 / 5 — Media
Competencia         2 / 5 — Media
Potencial de Marca  4 / 5 — Media
```

## 2. Regla de normalización

```text
PUBLICATION ≠ PRODUCT BASE
PRODUCT BASE ≠ COMPETITOR / SKU
FEATURE ≠ PRODUCT BASE
QUERY COHORT ≠ PRODUCT BASE
```

Se crea una Product Base separada cuando existe una diferencia material en una o más de estas dimensiones:

```text
job / segmento
mecanismo o boundary de medición
instalación
service layer
seguridad / regulación
conectividad
postventa
economía / logística
```

No se separa una Product Base sólo por marca, color, app equivalente, amperaje cercano dentro de la misma arquitectura o número de canales como simple variante cuando no cambia estructuralmente el job o la carga operativa.

## 3. Product Bases normalizadas

### BASE-HOGAR-016 — Medidor enchufable standalone de consumo

`CANDIDATE_PB` — `ML-0120..ML-0124`

Core:

```text
artefacto individual
→ medición directa
→ display/local readout
→ no relay/app/cloud required
```

10A/16A, memoria, cálculo de costo y display son variantes.

### BASE-HOGAR-017 — Smart plug enchufable con medición de energía

`CANDIDATE_PB — COMMODITY-RISK` — `ML-0125..ML-0128`

Core:

```text
artefacto individual
→ medición directa
+ relay/control
+ app/connectivity
```

Tuya/Smart Life/Alexa no generan PB diferentes.

### BASE-HOGAR-018 — Tomacorriente smart embutido con monitoring

`SUPPORT_PB / ADJACENT` — `ML-0129`

Se separa de 017 porque el montaje fijo modifica instalación, seguridad, postventa y reversibilidad. La evidencia está más orientada a smart-home/control que a monitoring como job principal.

### BASE-HOGAR-019 — Medidor monofásico DIN de energía — lectura local

`CANDIDATE_PB` — `ML-0130..ML-0132`

Core:

```text
circuito / alimentación
→ medición directa
→ instalación DIN
→ lectura local
```

45A/80A, memoria, pulsos y magnitudes adicionales son variantes.

### BASE-HOGAR-020 — Protector DIN smart con medición de energía

`CANDIDATE_PB — CONDITIONED` — `ML-0133..ML-0134`

Se separa de 019 por:

```text
relay/corte
+ protección configurable
+ connectivity/app
```

Esto cambia safety, claims, evidencia, certificaciones y postventa.

### BASE-HOGAR-021 — Medidor split-CT standalone — agregado de circuito/hogar

`CANDIDATE_PB — CONDITIONED` — `ML-0135`

Core:

```text
circuito / alimentación
→ split-core CT
→ medición agregada
→ display local
```

La evidencia local es limitada, pero el método de instalación/medición lo separa de DIN.

### BASE-HOGAR-022 — Monitor CT whole-home conectado — 1–2 CT

`CANDIDATE_PB — CONDITIONED` — `ML-0138, ML-0139`

Core:

```text
alimentación / hogar
→ 1–2 CT
→ monitoring agregado
→ app/histórico
```

Bidireccionalidad solar y salida dry-contact se mantienen como variantes.

### BASE-HOGAR-023 — Monitor CT multi-circuito — 3+ circuitos

`CANDIDATE_PB — HIGHLY CONDITIONED` — `ML-0136, ML-0137`

Core:

```text
varios circuitos
→ múltiples CT
→ configuración por canal
→ app / integración
```

3, 10 o 20 canales son variantes de capacidad; la carga de instalación/configuración/soporte justifica separarlo de 022.

## 4. Arquitecturas sin Product Base materializada

F1 había identificado:

```text
A5 — Aggregate measurement + NILM / disaggregation
A6 — Smart-meter / utility-data integration
```

F6 no crea Product Bases para ellas porque no existe en la muestra una configuración suficientemente normalizada; A5 es una capa inferencial sobre hardware agregado y A6 depende de infraestructura/utility y puede no implicar un producto físico importable.

```text
ARCHITECTURE EXISTS
≠
PRODUCT BASE MUST EXIST
```

## 5. Mapeo consolidado

| Product Base | Publicaciones | Rol F6 |
|---|---|---|
| BASE-HOGAR-016 | ML-0120..0124 | CANDIDATE_PB |
| BASE-HOGAR-017 | ML-0125..0128 | CANDIDATE_PB — COMMODITY-RISK |
| BASE-HOGAR-018 | ML-0129 | SUPPORT_PB / ADJACENT |
| BASE-HOGAR-019 | ML-0130..0132 | CANDIDATE_PB |
| BASE-HOGAR-020 | ML-0133..0134 | CANDIDATE_PB — CONDITIONED |
| BASE-HOGAR-021 | ML-0135 | CANDIDATE_PB — CONDITIONED |
| BASE-HOGAR-022 | ML-0138..0139 | CANDIDATE_PB — CONDITIONED |
| BASE-HOGAR-023 | ML-0136..0137 | CANDIDATE_PB — HIGHLY CONDITIONED |

## 6. Implicación para F7

Elegibles para shortlist:

```text
BASE-HOGAR-016
BASE-HOGAR-017
BASE-HOGAR-019
BASE-HOGAR-020
BASE-HOGAR-021
BASE-HOGAR-022
BASE-HOGAR-023
```

No elegible como candidato central:

```text
BASE-HOGAR-018
→ SUPPORT_PB / ADJACENT
```

F7 aplicará el sesgo de primera etapa:

```text
simple import/regulation/logistics
low installation friction
manageable safety
low cloud dependency
manageable post-sale
easy-to-explain benefit
```

sin convertir complejidad en exclusión automática.

## 7. Gate F6

Resultado conceptual:

```text
PASS
```

La evidencia permite normalizar configuraciones comercialmente significativas y suficientemente distintas para ejecutar shortlist pre-origen.

## 8. Materialización en matriz

F6 agrega:

```text
Productos Base
→ BASE-HOGAR-016 … BASE-HOGAR-023
```

y mapea `ML-0120..ML-0139` y `COMP-0120..COMP-0139` a sus PB.

Archivo preparado:

```text
matrix-aut65-brand-cand-004-phase6.xlsx
SHA-256: a5e5259dafaf8b88cde7553006bb59d88e09205ef5b95bd116f8e08859f311f8
```

## 9. Estado formal de F6

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut65
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F6 CLOSED
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
SHA-256: a5e5259dafaf8b88cde7553006bb59d88e09205ef5b95bd116f8e08859f311f8
```

F7 queda formalmente abierta después de este cierre.

## 10. Próxima acción

F6 queda `CLOSED`. Ejecutar `F7 — Shortlist pre-origin` en modalidad `AUTO`.

## 11. Changelog

### 2026-09-25 — v0.1.0

- F5 queda formalmente cerrada sobre `aut64 PASS`;
- se materializan BASE-HOGAR-016..023;
- BASE-HOGAR-018 queda SUPPORT_PB / ADJACENT;
- A5 NILM y A6 utility-data permanecen como arquitecturas sin PB materializada;
- se mapean ML-0120..0139 y COMP-0120..0139;
- se prepara `matrix-aut65-brand-cand-004-phase6.xlsx`;
- `aut65` obtiene PASS limpio y F6 queda formalmente `CLOSED`;
- siguiente fase: `F7 — Shortlist pre-origin` en AUTO.
