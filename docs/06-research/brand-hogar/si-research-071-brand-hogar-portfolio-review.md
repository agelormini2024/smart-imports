---
id: si-research-071
title: Marca Hogar — Portfolio Review transversal y baseline interna
description: Comparación transversal de finalistas de Marca Hogar y cierre de la prioridad interna previa a revisión externa.
version: 0.1.0
status: complete
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-07
updated: 2026-10-07
brand: brand-hogar
phase: portfolio-review
tags:
  - brand-hogar
  - portfolio-review
  - internal-decision
  - first-stage-fit
  - external-review
---

# SI-RESEARCH-071 — Marca Hogar — Portfolio Review transversal

## 1. Estado

```text
PORTFOLIO REVIEW: COMPLETE — INTERNAL
PORTFOLIO BASELINE: FROZEN
EXTERNAL REVIEW: PENDING
PROCUREMENT: NOT OPENED
F14: NOT OPENED
```

Este review no reabre F0–F13 y no recalcula economía. Integra los resultados cerrados de los Brand Candidates de Marca Hogar.

## 2. Universo comparado

Finalistas elegibles:

```text
BASE-HOGAR-002 — FINALIST — CONDITIONED
BASE-HOGAR-006 — FINALIST — CONDITIONED
BASE-HOGAR-010 — FINALIST — CONDITIONED
BASE-HOGAR-016 — FINALIST — CONDITIONED
BASE-HOGAR-028 — FINALIST — CONDITIONED / NOT FIRST-STAGE FIT
BASE-PET-003   — FINALIST — CONDITIONED / NOT FIRST-STAGE FIT
```

Fuera del review activo:

```text
BRAND-CAND-002 — DEFERRED / PAUSED
```

La pausa de `BRAND-CAND-002` se mantiene como gate externo pendiente y no se interpreta como conclusión regulatoria.

## 3. Criterio transversal

Se comparan:

1. adecuación a primera etapa;
2. economía ya validada por Method v2;
3. demanda / claridad del problema;
4. complejidad operativa;
5. riesgo técnico / regulatorio;
6. instalación y compatibilidad local;
7. postventa;
8. Brand Fit y capacidad de agregar valor.

Regla:

```text
FINALIST
≠
FIRST-STAGE LEAD
≠
PURCHASE AUTHORIZATION
```

## 4. Lectura consolidada

### BASE-HOGAR-016 — Lead interno

Fortalezas ya documentadas:

- demanda observable;
- medición directa por artefacto;
- instalación simple;
- baja dependencia de cloud/app;
- beneficio fácil de explicar;
- economía suficiente en 50 y 100 unidades;
- buen fit explícito para primera etapa.

Condiciones:

- accuracy / test evidence;
- configuración exacta 16A / 220–240V / 50Hz;
- plug Argentina/AU;
- packing/peso same-SKU;
- documentación/certificaciones;
- revisión externa de importación.

Resultado:

```text
INTERNAL FIRST-STAGE LEAD
EXTERNAL REVIEW REQUIRED
F14 NOT OPENED
```

### BASE-HOGAR-006 — Backup de primera etapa

Fortalezas:

- economía muy robusta;
- propuesta de valor simple;
- arquitectura localizada;
- ausencia de dependencia cloud/app crítica;
- adecuación operativa a primera etapa `DEFENDIBLE — CONDITIONED`.

Señal de demanda local:

```text
MERCADO LIBRE OFFER SIGNAL: VERY LIMITED / NO DIRECT LOCAL CATEGORY OBSERVED
MERCADO LIBRE DEMAND SIGNAL: WEAK / NOT DEMONSTRATED
```

El micro-review posterior al Portfolio Review no encontró una categoría local visible de soluciones equivalentes de `detección de fuga + corte automático` destinadas específicamente a proteger un artefacto. Las búsquedas tienden a devolver electroválvulas/repuestos de lavarropas, que no son comparables funcionales y no deben contarse como evidencia de demanda de `BASE-HOGAR-006`.

Condiciones dominantes:

- validar demanda local real;
- compatibilidad eléctrica;
- requisitos regulatorios aplicables en Argentina.

Resultado:

```text
FIRST-STAGE BACKUP — CONDITIONED
ECONOMICS STRONG
LOCAL DEMAND SIGNAL NOT YET CONFIRMED
EXTERNAL REVIEW REQUIRED
F14 NOT OPENED
```

### BASE-HOGAR-010 — Segunda línea

Fortalezas:

- economía suficiente;
- problema doméstico comprensible;
- Brand Fit fuerte;
- propuesta sin dependencia obligatoria de tecnología activa.

Condiciones:

- capacidad/materialidad real del sorbente;
- claims gas-phase defendibles;
- filtros/repuestos;
- sizing/CADR;
- compatibilidad eléctrica y certificación.

Resultado:

```text
SECONDARY PORTFOLIO CANDIDATE
EXTERNAL REVIEW REQUIRED
NO FIRST-STAGE PREFERENCE OVER TIER A
```

### BASE-HOGAR-002 — Segunda línea

Fortalezas:

- economía robusta;
- problema doméstico claro;
- Brand Fit fuerte;
- valor potencial mediante solución, documentación, soporte e instalación.

Condición dominante:

- compatibilidad técnica e instalación del corte central en contexto residencial argentino.

Resultado:

```text
SECONDARY PORTFOLIO CANDIDATE
INSTALLATION / EXTERNAL REVIEW GATE
NO FIRST-STAGE PREFERENCE OVER TIER A
```

### BASE-HOGAR-028 — Reserva

F13 ya lo clasifica:

```text
NOT FIRST-STAGE FIT
```

Razones dominantes: demanda local débil/no visible, carga de electrodoméstico y postventa, compatibilidad eléctrica, filtros/repuestos, warranty, certificaciones y disciplina de claims.

Resultado:

```text
PORTFOLIO RESERVE / SECOND STAGE
```

### BASE-PET-003 — Reserva

F13 ya lo clasifica:

```text
NOT FIRST-STAGE FIT
```

Condiciones dominantes: demanda, safety, QA, logística, postventa y validación profesional de importación.

Resultado:

```text
PORTFOLIO RESERVE / SECOND STAGE
```

## 5. Baseline interna

```text
TIER A — FIRST-STAGE
1. BASE-HOGAR-016 — INTERNAL LEAD
2. BASE-HOGAR-006 — BACKUP

TIER B — SECONDARY / EXTERNAL REVIEW
- BASE-HOGAR-010
- BASE-HOGAR-002

TIER C — PORTFOLIO RESERVE / SECOND STAGE
- BASE-HOGAR-028
- BASE-PET-003

DEFERRED
- BRAND-CAND-002
```

Dentro de Tier B no se fuerza un ranking adicional antes del gate externo.

La posición de `BASE-HOGAR-006` como backup no implica demanda validada. Su fortaleza proviene principalmente de economía y operabilidad; la señal de demanda local permanece `WEAK / NOT DEMONSTRATED`.

## 6. Qué significa esta decisión

Se decide internamente dónde concentrar atención cuando llegue la revisión externa.

No se decide:

- proveedor;
- orden de compra;
- cantidad final;
- F14;
- procurement-grade sourcing;
- NCM definitivo;
- requisitos regulatorios definitivos.

## 7. Gate externo

El gate externo debe verificar prioritariamente:

```text
BASE-HOGAR-016
→ BASE-HOGAR-006
→ BASE-HOGAR-010 / BASE-HOGAR-002 según necesidad
```

`BASE-HOGAR-028` y `BASE-PET-003` no requieren prioridad para primera importación.

La revisión externa puede:

- confirmar el lead;
- promover el backup;
- bajar un candidato por regulación/compatibilidad;
- solicitar datos puntuales.

No reabre automáticamente Method v2.

## 8. Relación con la matriz

Portfolio Review es una capa transversal posterior a F13 y no está modelada como fase de `full-matrix-v5 0.7.0`.

Por lo tanto:

```text
NO NEW HOGAR MATRIX SNAPSHOT
aut104 = FINAL HOGAR METHOD V2 SNAPSHOT
aut105 = RESERVED FOR BRAND-CAND-010 / MARCA FITNESS
```

No se consume un `aut` para representar una decisión documental de portfolio.

## 9. Estado de Marca Hogar

```text
BRAND CANDIDATE SCREENING: COMPLETE
METHOD V2 RELEVANT CANDIDATES: COMPLETE
PORTFOLIO REVIEW: COMPLETE — INTERNAL
PORTFOLIO BASELINE: FROZEN
EXTERNAL REVIEW: PENDING
PROCUREMENT: NOT OPENED
F14: NOT OPENED
PRIMARY WORKSTREAM MAY SHIFT TO MARCA FITNESS
```

## 10. Fuentes

- `SI-RESEARCH-013` — BRAND-CAND-001 F13.
- `SI-RESEARCH-027` — BRAND-CAND-003 F13.
- `SI-RESEARCH-041` — BRAND-CAND-004 F13.
- `SI-RESEARCH-055` — BRAND-CAND-005 F13.
- `SI-RESEARCH-069` — BRAND-CAND-006 F13.
- Marca Hogar — pausa operativa para revisión externa.

## 11. Cierre

La decisión interna está suficientemente madura para congelar Marca Hogar como frente primario de investigación.

La próxima modificación material de este baseline debe provenir de:

```text
revisión externa
o
contradicción material nueva
```

Mientras tanto, el trabajo principal puede pasar a Marca Fitness.
