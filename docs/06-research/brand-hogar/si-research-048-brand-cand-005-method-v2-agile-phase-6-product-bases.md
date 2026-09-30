---
id: si-research-048
title: BRAND-CAND-005 — Method v2 Agile — F6 Product Bases
description: Normalización de Product Bases comercialmente significativas para compostaje y procesamiento doméstico de residuos orgánicos.
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
  - phase-6
  - product-bases
phase: business-intelligence
---

# BRAND-CAND-005 — Method v2 Agile — F6 Product Bases

Fecha: 2026-09-28  
Estado: `CLOSED`

## 1. Input vigente

F5 quedó formalmente cerrada sobre:

```text
matrix-aut81-brand-cand-005-phase5.xlsx
SHA-256: 0b0a9351001f3674289d1aaa9542564d5e4a473435b0aee830c50a42c418acf1
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Evaluaciones acumuladas:

```text
Demanda             3 / 5 — Media
Competencia         3 / 5 — Media
Potencial de Marca  4 / 5 — Media
```

## 2. Regla de normalización

```text
PUBLICATION ≠ PRODUCT BASE
PRODUCT BASE ≠ COMPETITOR / SKU
FEATURE ≠ PRODUCT BASE
ARCHITECTURE ≠ PRODUCT BASE
TOPOLOGY ≠ PRODUCT BASE
QUERY COHORT ≠ PRODUCT BASE
```

Se crea una Product Base separada cuando cambia de forma material uno o más de estos elementos:

```text
job / segmento
mecanismo real
carga operativa del usuario
service layer
consumibles / recurrencia
seguridad / regulación
electricidad / conectividad
postventa
economía / logística
```

No se crea una PB nueva sólo por:

- marca;
- color;
- cantidad de módulos;
- starter incluido o no;
- capacidad cercana;
- display/LED;
- auto-clean;
- número de bins cuando el mecanismo y la carga operativa siguen siendo equivalentes.

## 3. Product Bases normalizadas

### BASE-HOGAR-024 — Compostera modular apilable 40–60 L

`CANDIDATE_PB` — `ML-0142, ML-0143, ML-0144`

Core:

```text
contenedor modular doméstico
→ residuos orgánicos
→ operación aeróbica
→ vermicompost-compatible según uso
→ cocina / balcón / patio
```

Se agrupan:

- 40 L / 45 L / 60 L;
- cantidad de módulos;
- mesa/canilla;
- starter;
- lombrices opcionales.

No se separan porque esas diferencias no cambian de forma suficiente el hardware base, la logística ni el job principal.

Condición:

`ML-0144` conserva ambigüedad de mecanismo exacto, pero su configuración física pertenece a esta familia.

### BASE-HOGAR-025 — Compostera giratoria 120 L — doble cámara

`CANDIDATE_PB — FIRST-STAGE FIT CANDIDATE` — `ML-0140`

Core:

```text
compostaje aeróbico
→ recipiente cerrado
→ rotación manual
→ doble cámara
→ operación por lotes
```

Se separa de BASE-HOGAR-024 porque cambia:

- mecanismo de mezcla;
- estructura;
- tamaño/logística;
- montaje;
- durabilidad mecánica;
- experiencia de uso.

Es la Product Base con mayor tracción visible del candidato en F3 (`+1000`).

### BASE-HOGAR-026 — Vermicompostera dedicada ~120 L

`CANDIDATE_PB — USER-EDUCATION-CONDITIONED` — `ML-0141`

Core:

```text
residuos orgánicos
→ lombrices / sistema vivo
→ control de humedad / temperatura
→ cosecha de vermicompost
```

Se separa de BASE-HOGAR-024 porque la dependencia explícita de un organismo vivo cambia:

- onboarding;
- restricciones de operación;
- soporte;
- aceptación del usuario;
- service layer.

### BASE-HOGAR-027 — Kit Bokashi twin-bin + starter

`CANDIDATE_PB — CONDITIONED / LOW-DEMAND-PROOF` — `ML-0145, ML-0146`

Core:

```text
residuos orgánicos
→ fermentación anaeróbica
→ recipiente hermético
→ inoculante / starter
→ pre-compost
→ post-proceso obligatorio
```

Un bin vs dos bins y la cantidad de starter son variantes.

Se separa porque introduce:

- consumible recurrente;
- fermentación;
- drenaje;
- post-proceso;
- claims específicos.

### BASE-HOGAR-028 — Procesador térmico countertop 3–4 L

`CANDIDATE_PB — HIGHLY CONDITIONED / SERVICE-CLAIM-RISK` — `ML-0147..ML-0150`

Core:

```text
residuos de cocina
→ calor / secado
→ molienda / trituración
→ enfriamiento
→ reducción de volumen
→ pre-compost / material procesado
```

Variaciones 3,2–4 L, LED, auto-clean y duración de ciclo no crean PB distintas.

Se separa de A1–A4 porque cambia materialmente:

- electricidad;
- piezas móviles;
- filtros;
- limpieza;
- postventa;
- compatibilidad 220–240 V;
- riesgo de claim;
- economía/logística.

`ML-0148` se mapea provisionalmente aquí por familia comercial, aunque su mecanismo exacto sigue pendiente del PDF.

### BASE-HOGAR-029 — Triturador eléctrico de jardín

`SUPPORT_PB / ADJACENT` — `ML-0151`

Core:

```text
hojas / podas / ramas
→ trituración mecánica
→ reducción de tamaño
→ preparación para tratamiento posterior
```

No resuelve el mismo job de residuos orgánicos de cocina.

Se materializa únicamente para preservar trazabilidad y evitar que vuelva a contaminar la lectura del core.

## 4. Arquitectura sin Product Base

### A6 — biológico / in-vessel

```text
NO PB MATERIALIZED
```

Motivo:

- no apareció una cohorte local diferenciada;
- las búsquedas específicas repitieron equipos A5;
- no hay evidencia suficiente de microorganismos + aireación/agitación + control térmico como configuración comercial observable;
- materializar una PB en este punto sería inventar precisión no soportada por la evidencia.

Regla:

```text
ARCHITECTURE EXISTS
≠
PRODUCT BASE MUST EXIST
```

A6 podrá reabrirse si F8+ o investigación futura aporta un producto comercial concreto y diferenciable.

## 5. Mapeo

| Product Base | Publicaciones | Rol F6 |
|---|---|---|
| BASE-HOGAR-024 | ML-0142, ML-0143, ML-0144 | CANDIDATE_PB |
| BASE-HOGAR-025 | ML-0140 | CANDIDATE_PB — FIRST-STAGE FIT CANDIDATE |
| BASE-HOGAR-026 | ML-0141 | CANDIDATE_PB — USER-EDUCATION-CONDITIONED |
| BASE-HOGAR-027 | ML-0145, ML-0146 | CANDIDATE_PB — CONDITIONED / LOW-DEMAND-PROOF |
| BASE-HOGAR-028 | ML-0147..ML-0150 | CANDIDATE_PB — HIGHLY CONDITIONED / SERVICE-CLAIM-RISK |
| BASE-HOGAR-029 | ML-0151 | SUPPORT_PB / ADJACENT |

`COMP-0140..COMP-0151` queda mapeado con la misma normalización.

## 6. Implicación para F7

Elegibles para shortlist:

```text
BASE-HOGAR-024
BASE-HOGAR-025
BASE-HOGAR-026
BASE-HOGAR-027
BASE-HOGAR-028
```

No elegible como candidato central:

```text
BASE-HOGAR-029
→ SUPPORT_PB / ADJACENT
```

A6 no entra en F7 porque no tiene PB materializada.

F7 aplicará el sesgo de primera etapa:

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
→ BASE-HOGAR-024 … BASE-HOGAR-029
```

y mapea:

```text
Publicaciones ML
→ ML-0140 … ML-0151

Competencia ML
→ COMP-0140 … COMP-0151
```

No se crea PB para A6.

Archivo preparado:

```text
matrix-aut82-brand-cand-005-phase6.xlsx
SHA-256: a6e5526390208e040b601faa5cf2498f024bf361bc482988bdd8887b6b59fd16
```

## 9. Estado formal de F6

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut82
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
SHA-256: a6e5526390208e040b601faa5cf2498f024bf361bc482988bdd8887b6b59fd16
Report: aut82-brand-cand-005-phase6-validation-report.json
```

F7 queda formalmente abierta después de este cierre.

## 10. Próxima acción

Validar `aut82`.

Resultado ejecutado:

```text
F6 CLOSED — aut82 PASS
→ F7 — Shortlist pre-origin
→ AUTO
```
