---
id: si-roadmap-002
title: Project Status and Handoff
description: Estado operativo, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports.
version: 1.23.2
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-10-10
tags:
  - status
  - handoff
  - roadmap
  - continuity
related:
  - si-roadmap-001
  - si-agent-001
  - si-func-001
  - si-tech-001
  - si-tech-002
  - si-decision-010
  - si-decision-011
  - si-research-005
  - si-decision-014
  - si-research-006
  - si-decision-015
  - si-brand-001
  - si-brand-002
  - si-decision-016
  - si-decision-017
audience:
  - founder
  - partner
  - developer
  - assistant
phase: research
---

# SI-ROADMAP-002 — Estado actual y handoff de Smart Imports

<!-- FITNESS-PRESCREENING-V02:START -->
## Checkpoint operativo — BRAND-CAND-010 Method v2 cerrado / 2026-10-08

```text
SCREENING: CLOSED
METHOD V2: F0–F13 CLOSED
F13 MATRIX: matrix-aut118-brand-cand-010-phase13-final-corrected.xlsx
F13 SHA-256: 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a
POST-CLOSE BASELINE: matrix-aut120-brand-cand-010-post-close-reconciliation.xlsx
POST-CLOSE SHA-256: 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2
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

BRAND-CAND-007 → ELIGIBLE — NOT OPENED
BRAND-CAND-008 → ELIGIBLE — NOT OPENED
BRAND-CAND-009 → ELIGIBLE — NOT OPENED
```

La walking pad queda como principal hipótesis de reapertura porque fue la única arquitectura con demanda local específica defendible, pero el screen de landed cost aéreo la deja fuera de shortlist final. Reabrir exige evidencia logística marítima/LCL decision-grade y validación de requisitos eléctricos, QA y postventa.

`NO FINALIST` no equivale a descartar definitivamente el candidato. Significa que, con la evidencia disponible y los supuestos comparables del Method v2, ninguna Product Base justifica pasar hoy a Portfolio Review como finalista.

Próximo gate de Marca Fitness: cerrar este checkpoint mediante revisión + commit/push humano y recién después seleccionar cuál de `BRAND-CAND-007..009` abrir. No abrir candidatos en paralelo por defecto.
<!-- FITNESS-PRESCREENING-V02:END -->

<!-- HOGAR-PAUSE-AND-OPPORTUNITY-INTAKE:START -->
## Checkpoint operativo — cierre interno Marca Hogar / 2026-10-07

```text
INTERNAL PORTFOLIO REVIEW: COMPLETE
FIRST-STAGE LEAD: BASE-HOGAR-016
BACKUP: BASE-HOGAR-006 — LOCAL DEMAND NOT YET CONFIRMED
SECONDARY: BASE-HOGAR-010 / BASE-HOGAR-002
RESERVE: BASE-HOGAR-028 / BASE-PET-003
BRAND-CAND-002: DEFERRED / PAUSED
EXTERNAL REVIEW: PENDING
PROCUREMENT: NOT OPENED
F14: NOT OPENED
PORTFOLIO BASELINE: FROZEN
```

Portfolio Review: `SI-RESEARCH-071`.
Decisión: `SI-DECISION-017`.

`aut104` permanece como último snapshot de Hogar. Portfolio Review no consume `aut`; `aut105` queda reservado para `BRAND-CAND-010 / Marca Fitness`.

Fuente: `docs/07-brand/brands/brand-hogar/brand-hogar-external-review-pause-checkpoint.md`.

### Mejora metodológica reusable

Se mantiene `SI-BRAND-003 — Ingreso de oportunidades y descubrimiento`.

El sistema admite descubrimiento descendente `territorio → misión → problema → solución → producto` y descubrimiento ascendente `producto → solución → problema → misión → territorio`. Ambas rutas convergen en Brand Candidate Screening antes de Method v2.

```text
ORIGEN DE LA IDEA ≠ CALIDAD DE LA OPORTUNIDAD
```

Fuente: `docs/07-brand/si-brand-003-opportunity-intake-and-discovery.md`.
<!-- HOGAR-PAUSE-AND-OPPORTUNITY-INTAKE:END -->

<!-- BRAND-CAND-006-HANDOFF:START -->
## Checkpoint operativo — BRAND-CAND-006 / 2026-10-05

```text
BRAND-CAND-006
Mode: RETROSPECTIVE + REUSE + RECONCILIATION

F0 CLOSED — aut91 PASS
F1 CLOSED — aut92 PASS
F2 CLOSED — aut93 PASS
F3 CLOSED — aut94 corrected PASS
F4 CLOSED — aut95 PASS
F5 CLOSED — aut96 PASS
F6 CLOSED — aut97 PASS
F7 CLOSED — aut98 PASS
F8 CLOSED — aut99 PASS
F9 CLOSED — aut100 PASS
F10 CLOSED — aut101 PASS
F11 CLOSED — aut102 PASS
F12 CLOSED — aut103 PASS
F13 CLOSED — aut104 PASS
F14 NOT OPENED

Finalist: BASE-PET-003 — FINALIST — CONDITIONED
Portfolio eligibility: ELIGIBLE FOR PORTFOLIO REVIEW
First-stage fit: NOT FIRST-STAGE FIT
Candidate status: PORTFOLIO REVIEW READY / FREEZE
```

Snapshot final:

```text
matrix-aut104-brand-cand-006-phase13.xlsx
SHA-256: a5caeebe1954b59ea1bf37e29b22e8961820305b743584eaf5355b0439cd056e
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Research publicado: `SI-RESEARCH-056..069`.

La identidad de `BASE-PET-003` se preserva `REUSE AS-IS`.

La reconciliación global `aut96..aut104` queda completa. `BRAND-CAND-010 / aut105` queda desbloqueado como siguiente target operativo, todavía pendiente de materialización.
<!-- BRAND-CAND-006-HANDOFF:END -->

<!-- BRAND-CANDIDATE-DOC-CLOSE-RULE:START -->
## Regla obligatoria — cierre documental antes del siguiente Brand Candidate

El cierre operativo de un Brand Candidate **no termina con el PASS de F13**.

Secuencia obligatoria de cierre:

```text
F13 validada con PASS
→ publicar SI-RESEARCH de F0–F13 en smart-imports
→ actualizar expediente del Brand Candidate
→ actualizar índices de Research y Marca Hogar
→ actualizar README raíz
→ actualizar SI-ROADMAP-002
→ ejecutar verificación documental y git diff --check
→ git add / commit / push con aprobación humana
→ recién entonces abrir el siguiente Brand Candidate
```

Reglas derivadas:

- ningún candidato siguiente se abre mientras el anterior esté sólo cerrado en chat/matriz;
- la fuente de continuidad es el repo `smart-imports`, no la conversación;
- `commit` y `push` siguen siendo pasos humanos explícitos;
- un candidato en `FREEZE` no se reabre para sourcing/F14 salvo Portfolio Review, revisión externa o contradicción material.

Esta regla aplica a todos los Brand Candidates actuales y futuros.
<!-- BRAND-CANDIDATE-DOC-CLOSE-RULE:END -->

<!-- BRAND-CAND-005-HANDOFF:START -->
## Checkpoint operativo — BRAND-CAND-005 / 2026-09-30

```text
Method v2 Agile: Fases 0–13 CLOSED
Snapshot comercial vigente: matrix-aut90-brand-cand-005-phase13.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 2bb0e30d75f98d9d90b60942b0b84ea409544e0966b5d5a4fd88e51fc65fbe9e
Finalist: BASE-HOGAR-028 — FINALIST — CONDITIONED
Portfolio eligibility: ELIGIBLE FOR PORTFOLIO REVIEW
First-stage fit: NOT FIRST-STAGE FIT
Portfolio status: PORTFOLIO REVIEW READY
Candidate status: FREEZE
F14: NOT OPENED
```

`BASE-HOGAR-024` queda `STOP — REOPENABLE`. `BASE-HOGAR-025` queda `STOP — REOPENABLE / LOGISTICS GATE`. `BASE-HOGAR-028` sobrevive condicionado por demanda local débil/no visible, postventa de electrodoméstico, compatibilidad eléctrica exacta, filtros/repuestos, warranty, documentación/certificaciones, seguridad y disciplina de claims sobre el output.

Próxima secuencia:

```text
DOCUMENTARY CLOSE BRAND-CAND-005
→ verificación documental / git diff --check
→ git add / commit / push humano
→ BRAND-CAND-006 — residuos de mascotas
→ Portfolio Review global
→ revisión externa
→ selección para profundización
→ decisión sobre F14
```

No reabrir F14 ni tratar el finalista como producto listo antes de Portfolio Review y gate externo.
<!-- BRAND-CAND-005-HANDOFF:END -->

<!-- BRAND-CAND-004-HANDOFF:START -->
## Checkpoint operativo — BRAND-CAND-004 / 2026-09-25

```text
Method v2 Agile: Fases 0–13 CLOSED
Snapshot comercial vigente: matrix-aut72-brand-cand-004-phase13.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 560fd2073da35327babe7a473c726e012f8d5496223f98c9d4f1dd5212948ced
Finalist: BASE-HOGAR-016 — FINALIST — CONDITIONED
Portfolio status: PORTFOLIO REVIEW READY
Candidate status: FREEZE
F14: NOT OPENED
```

`BASE-HOGAR-017` y `BASE-HOGAR-019` quedan `STOP — REOPENABLE`. `BASE-HOGAR-016` sobrevive condicionado por accuracy/test evidence, configuración eléctrica exacta, plug Argentina/AU, packing/peso same-SKU, certificación/requisitos locales y futura revisión externa.

Próxima secuencia:

```text
DOCUMENTARY CLOSE BRAND-CAND-004
→ BRAND-CAND-005
→ BRAND-CAND-006
→ Portfolio Review global
→ revisión externa
→ selección para profundización
→ decisión sobre F14
```
<!-- BRAND-CAND-004-HANDOFF:END -->

<!-- BRAND-CAND-003-HANDOFF:START -->
## Checkpoint operativo — BRAND-CAND-003 / 2026-09-25

```text
Method v2 Agile: Fases 0–13 CLOSED
Snapshot comercial vigente: matrix-aut58-brand-cand-003-phase13.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: ec5c8b8f52cc3ae13c2d759e41b4f90f568948fa03676271ce585894d80c44da
Finalist: BASE-HOGAR-010 — FINALIST — CONDITIONED
Portfolio status: PORTFOLIO REVIEW READY
Candidate status: FREEZE
F14: NOT OPENED
```

`BASE-HOGAR-009` y `BASE-HOGAR-011` quedan `STOP — REOPENABLE`. `BASE-HOGAR-010` sobrevive condicionado por materialidad/capacidad del sorbente, claims, filtros/repuestos, compatibilidad eléctrica y futura revisión externa.

`BRAND-CAND-002` permanece `PASS TO METHOD V2 — DEFERRED / PAUSED`. La pausa responde a una preocupación del founder sobre aprobación/costo regulatorio; requiere revisión externa y **no** se registra como conclusión regulatoria verificada.

`BRAND-CAND-002` permanece `PASS TO METHOD V2 — DEFERRED / PAUSED`. La pausa responde a una preocupación del founder sobre aprobación/costo regulatorio, pendiente de revisión externa; **no se registra como conclusión regulatoria verificada**.

Próxima secuencia obligatoria:

```text
BRAND-CAND-004
→ BRAND-CAND-005
→ BRAND-CAND-006
→ Portfolio Review global
→ revisión externa
→ selección para profundización
→ decisión sobre F14
```
<!-- BRAND-CAND-003-HANDOFF:END -->

<!-- SI-F13-CHECKPOINT:START -->
## Checkpoint operativo — BRAND-CAND-001 / 2026-09-24

```text
Golden Run Method v2: Fases 0–13 CLOSED
Snapshot comercial vigente: matrix-aut44-brand-cand-001-phase13-corrected.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 37b2b37c5c61355efec271b7ecb49df74c2264e2f721830a1c2478858a850f56
Portfolio status: PORTFOLIO REVIEW READY
F14: NOT OPENED
```

F13 conserva `BASE-HOGAR-002` y `BASE-HOGAR-006` como `FINALIST — CONDITIONED`. `BRAND-CAND-001` queda en `FREEZE`: completar los candidatos restantes hasta F13, comparar finalistas y realizar revisión externa —incluido despachante— antes de decidir qué producto abre F14.
<!-- SI-F13-CHECKPOINT:END -->

<!-- SI-F12-CHECKPOINT:START -->
## Checkpoint operativo — BRAND-CAND-001 / 2026-09-23

```text
Golden Run Method v2: Fases 0–12 CLOSED
Snapshot comercial vigente: matrix-aut43-brand-cand-001-phase12.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 5b602747404dce8584c3735552009487607ffe4a642c56bb05b8b9aba0663315
Next gate: F13 — Shortlist final
```

F12 reduce el camino activo a `BASE-HOGAR-002` y `BASE-HOGAR-006`, ambos condicionados. `BASE-HOGAR-003` queda STOP — REOPENABLE. No reabrir sourcing ni negociación fina salvo evidencia material nueva.
<!-- SI-F12-CHECKPOINT:END -->

<!-- SI-F11-CHECKPOINT:START -->
## Checkpoint operativo — BRAND-CAND-001 / 2026-09-23

```text
Golden Run Method v2: Fases 0–11 CLOSED
Snapshot comercial vigente: matrix-aut42-brand-cand-001-phase11.xlsx
Schema: full-matrix-v5 0.7.0
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 6204f672b70d9e4629ee047aac31e25044b93e37037c9db98a303cc95cb6361c
Next gate: F12 — Margin + ROI
```

F11 cerró seis escenarios decision-grade de Landed Cost para `BASE-HOGAR-002`, `BASE-HOGAR-003` y `BASE-HOGAR-006`. Los tres pasan a F12 condicionados. No reabrir sourcing, negociación fina ni Matrix Validator salvo contradicción material o bloqueo real.
<!-- SI-F11-CHECKPOINT:END -->

> Punto de entrada operativo obligatorio para retomar el proyecto sin depender de un chat específico.

## 1. Fuentes de verdad

```text
Documentación y negocio:
https://github.com/agelormini2024/smart-imports

Software ejecutable:
https://github.com/agelormini2024/smart-imports-engine

Snapshot comercial vigente:
matrix-aut58-brand-cand-003-phase13.xlsx
→ full-matrix-v5 0.7.0
→ PASS limpio

Baseline técnica de release:
matrix-aut32-id-formats-corrected.xlsx
→ Matrix Validator v0.1.0
```

No confundir:

- `aut32`: baseline técnica de la release del Validator.
- `aut34`: snapshot comercial histórico correspondiente al cierre de Fase 6 del Nicho 3.
- `aut36`: checkpoint comercial histórico del Nicho 3, con Method v2 materializado hasta Landed Cost Screen.
- `aut37`: snapshot comercial operativo vigente, correspondiente a la Golden Run de `BRAND-CAND-001` cerrada hasta Fase 6.

## 2. Snapshot al 2026-09-18

| Campo | Estado |
|---|---|
| Fase general | Research / validación del método sobre múltiples nichos |
| Matrix Validator | v0.1.0 publicado y cerrado |
| Schema operativo | `full-matrix-v5 0.7.0` |
| Tests | 40 archivos / 170 tests |
| CLI | 5 casos operativos |
| E2E público | 10 fixtures |
| CI | Verde |
| Matriz comercial vigente | `matrix-aut44-brand-cand-001-phase13-corrected.xlsx` |
| Resultado aut44 | PASS / 0 errors / 0 warnings / 0 info / 0 limitations |
| Nicho 1 — Energía Solar Portátil | Pausado selectivamente |
| Nicho 2 — Viaje organizado | Screening de origen/headroom realizado; Landed Cost defendible pendiente |
| Nicho 3 — Mascotas | Method v2 ejecutado internamente hasta Fase 11; primer strong candidate pendiente de validación profesional |
| Próxima acción Golden Run | Fase 11 — Landed Cost de `BRAND-CAND-001` |
| Próxima acción Nicho 3 | Consolidar finalistas y preparar el gate profesional externo |
| Brand System | v0.4; se agrega lifecycle de Hypothesis ID local → `BRAND-CAND-XXX` formal/global, manteniendo `CORE` / `STRONG ADJACENCY` y separación Brand Fit / Method v2 |
| Brand Candidate Screening | v0.4 operativo; `PROSPECTIVE` / `RETROSPECTIVE`; lifecycle Hypothesis ID → `BRAND-CAND-XXX`; 001–005 = `CORE / PASS`; 006 = `STRONG ADJACENCY / BRAND FIT CONFIRMED`; 007–010 = `CORE / PASS TO METHOD V2` |
| Próxima acción Brand | Mantener la prioridad comercial de Marca Hogar; Fitness abrió sólo `BRAND-CAND-010` en F0, pendiente de materialización/Validator; `BRAND-CAND-007..009` permanecen elegibles sin abrir |

## 3. Snapshot histórico del Nicho 3 — 2026-09-17

### Estado general

Smart Imports completó la validación interna de Method v2 hasta `Landed Cost Screen` sobre el Nicho 3.

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Baseline técnica: aut32
Snapshot comercial del checkpoint: aut36
Archivo: matrix-aut36-niche3-method-v2-checkpoint-corrected.xlsx
Resultado: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: 219d9954acca9fefda5f6edef2eab18f93bf0b4564e45d3e1442f13d6db39a53
```

### Matrix Validator — estado cerrado

```text
Application: 0.1.0
Tag: v0.1.0
Schema operativo: full-matrix-v5 0.7.0
Runtime: Node.js 24
Package manager: pnpm 11
Comportamiento: read-only
Test files: 40
Tests: 170
CLI: 5 casos operativos
E2E público: 10 fixtures
CI: verde
Baseline técnica: aut32 / PASS
```

No reabrir el Validator sin un requerimiento comercial concreto y bloqueante.

### Method v2

```text
Fases 0–6  → cerradas
Fase 7     → shortlist pre-origen cerrada
Fase 8     → screening de origen cerrado
Fase 9     → Headroom cerrado
Fase 10    → dataset mínimo ejecutado en sobrevivientes
Fase 11    → primer Landed Cost Screen completado
```

`BASE-PET-003` es el primer `STRONG CANDIDATE — PENDING PROFESSIONAL VALIDATION`.

El 2026-09-16 el proveedor confirmó que la diferencia entre dimensiones de producto y caja se explica porque el producto se envía parcialmente desmontado. El packing queda aclarado y no constituye un bloqueo actual.

`BASE-PET-004` queda pendiente de respuesta de proveedor antes de completar su Fase 10/11.

### Próximo gate

```text
completar 5–6 candidatos firmes
→ negociar FOB/condiciones
→ preparar paquete homogéneo
→ despachante
→ validar NCM / intervenciones / certificaciones / costos
→ recalcular
→ shortlist final
→ decisión de importación
```

La revisión del despachante es una dependencia profesional externa y no requiere reabrir el Matrix Validator.

## 4. Matriz del checkpoint histórico del Nicho 3 — aut36

```text
matrix-aut36-niche3-method-v2-checkpoint-corrected.xlsx
SHA-256:
219d9954acca9fefda5f6edef2eab18f93bf0b4564e45d3e1442f13d6db39a53
```

Validación:

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

`aut36` conserva la materialización de Fase 6 y agrega el recorrido de Method v2 hasta Landed Cost Screen:

- Nicho 29 normalizado.
- 3 Evaluaciones nuevas.
- 8 Productos Base `BASE-PET-*`.
- publicaciones y competencia local normalizadas.
- benchmarks externos.
- evidencias y fuentes trazables.
- cuatro resúmenes de competencia por arquitectura.
- segmentos competitivos, incluidos sustitutos.

No incorpora todavía Landed Cost ni una selección final de proveedores.

## 5. Método vigente — Method v2

Jerarquía:

```text
NICHO
→ NECESIDAD / FAMILIA
→ ARQUITECTURA DE SOLUCIÓN
→ PRODUCTO BASE
```

Reglas consolidadas:

- `publicación ≠ competidor ≠ SKU ≠ Producto Base`;
- normalizar antes de evaluar;
- Demanda y Competencia se evalúan por separado;
- complejidad técnica es riesgo, no descarte automático;
- un sustituto puede ser una combinación de productos;
- `OEM platform ≠ exact supplier`;
- safety claim no equivale a seguridad validada;
- network generation no equivale a network compatibility;
- standby battery no equivale a tracking battery;
- private-label capability no equivale a Potencial de Marca.

## 6. Nicho 3 — estado por arquitectura

| Arquitectura | Estado | Potencial de Marca |
|---|---|---|
| Vacuum Grooming | ADVANCE | MEDIO–ALTO |
| Arenero automático/smart | ADVANCE | ALTO — CONDICIONADO |
| Smart Fountain | ADVANCE | MEDIO–ALTO |
| GPS + Wellness | ADVANCE — CONDITIONAL | ALTO — FUERTEMENTE CONDICIONADO |

Watchlist:

- Dedicated Pet Camera + interaction.
- Mobile Pet Robot.

## 7. Productos Base del Nicho 3

| ID | Producto Base |
|---|---|
| BASE-PET-001 | Vacuum Grooming doméstico integrado |
| BASE-PET-002 | Arenero automático rotativo cerrado |
| BASE-PET-003 | Arenero automático open-top / acceso amplio |
| BASE-PET-004 | Arenero automático de rastrillo |
| BASE-PET-005 | Fuente inteligente automatizada/conectada |
| BASE-PET-006 | Fuente con monitoreo cuantitativo de hidratación |
| BASE-PET-007 | Tracker GPS 4G para mascotas |
| BASE-PET-008 | Tracker GPS + Wellness avanzado |

## 8. Necesidades futuras descubiertas para Matrix vNext

No bloquean el ciclo actual.

1. `Familia` y `Arquitectura` explícitas.
2. `Tipo Competencia = DIRECTA | INDIRECTA | SUSTITUTO | BENCHMARK`.
3. `Nichos.Proxima Accion` alineada con las fases de Method v2.

Mantener `full-matrix-v5 0.7.0` estable mientras estas necesidades no justifiquen un nuevo schema.

## 9. Estado comercial por nicho

### Nicho 1 — Energía Solar Portátil

- AT-999 y compras permanecen pausadas.
- Conservar evidencia histórica.
- No forzar reactivación sin una nueva razón comercial.

### Nicho 2 — Viaje organizado y equipaje funcional

- Demanda y Competencia cerradas.
- Screening de proveedores/origen realizado.
- Headroom screening realizado.
- Landed Cost defendible sigue pendiente.
- No crear snapshots MARG basados en supuestos no defendibles.

### Nicho 3 — Mascotas

- Research Brief: cerrado.
- Madurez: cerrada.
- Demanda: cerrada.
- Competencia: cerrada.
- Potencial de Marca: cerrado.
- Productos Base: cerrados.
- Materialización del checkpoint del Nicho 3: `aut36` PASS.
- Próximo gate: consolidar 5–6 candidatos firmes, negociar condiciones y preparar la validación profesional externa.

## 10. Próxima secuencia del Nicho 3

```text
completar BASE-PET-004 cuando responda el proveedor
→ consolidar aproximadamente 5–6 candidatos firmes
→ negociar FOB y condiciones con los finalistas
→ preparar paquete homogéneo para despachante
→ validar NCM / derechos / intervenciones / certificaciones / costos
→ actualizar Landed Cost con datos profesionales
→ construir shortlist final
→ decisión real de importación
```

Las Fases 7–11 ya forman parte del recorrido interno cerrado de Method v2. No deben reaparecer como trabajo futuro salvo que nueva evidencia obligue a reabrir un candidato concreto.

## 11. Nuevo frente — Brand System

El 2026-09-16 se formaliza una nueva capa estratégica previa a Method v2.

Principio:

```text
BRAND FIT
¿Queremos que nuestra marca venda este producto?

METHOD V2
¿Existe realmente un negocio defendible alrededor de este producto?
```

Arquitectura reusable:

```text
BRAND
→ BRAND TERRITORY
→ MISSIONS
→ PROBLEMS
→ SOLUTIONS
→ BRAND CANDIDATE SCREENING
→ METHOD V2
```

`Marca Hogar` es la primera implementación real, con el descriptor interno:

> **Un hogar que funciona mejor.**

El portfolio se organiza por misiones y problemas, no por categorías comerciales.

Misiones v0.1:

1. mejorar las condiciones del hogar;
2. usar mejor los recursos;
3. reducir y gestionar residuos;
4. resolver problemas domésticos recurrentes conectados con el núcleo.

El sistema debe ser reusable para futuras marcas con territorios y misiones propios. `Mundo Fitness` queda registrado como ejemplo conceptual de esa reusabilidad, no como una marca decidida.

Primer candidato:

```text
BRAND-CAND-001
Sistema doméstico de detección de fugas de agua con corte automático
→ PASS TO METHOD V2
```

El Brand System no requirió modificar `full-matrix-v5 0.7.0` ni Matrix Validator v0.1.0. La ejecución de `BRAND-CAND-001` generó `aut37` como nuevo snapshot comercial vigente, preservando `aut36` como checkpoint histórico del Nicho 3. Las necesidades futuras de modelado de Brand, Territory, Mission, Problem, Solution y Brand Fit se registran conceptualmente antes de decidir Matrix vNext o cambios del Intelligence Engine.

## 12. Bloqueos y dependencias

| Tema | Estado | Acción |
|---|---|---|
| Matrix Validator | Cerrado | No reabrir sin requerimiento comercial |
| Matrix vNext | No bloqueante | Registrar requisitos y diferir |
| Brand System | v0.3 consolidado; arquitectura reusable con `CORE` / `STRONG ADJACENCY`, category-creep protection y separación Brand Fit / Method v2 |
| Validación profesional externa | En preparación | Consolidar 5–6 candidatos, negociar condiciones y preparar revisión con despachante |
| Niche 3 origin | Screening cerrado en sobrevivientes | Reabrir sólo si aparece un nuevo candidato firme |
| Landed Cost Niche 3 | Screening preliminar iniciado | Completar sólo en finalistas y validar profesionalmente |
| Wellness local | Hipótesis abierta | Mantener como condición |
| Seguridad areneros | Riesgo crítico posterior | Evaluar en sourcing/QA |
| Compatibilidad GPS | Riesgo crítico posterior | Exigir variante/bandas documentadas |

## 13. Protocolo para abrir un nuevo chat

1. Compartir ambos repositorios.
2. Pedir lectura inicial de `SI-ROADMAP-002`.
3. Para tareas del Nicho 3, consultar `SI-RESEARCH-005`.
4. Para Fases 7–11 y estado de Method v2, consultar `SI-RESEARCH-006` y `SI-DECISION-015`.
5. Para tareas de marca, consultar `SI-BRAND-001`, `SI-BRAND-002`, `SI-BRAND-003` y `SI-DECISION-016`.
6. Adjuntar `aut96` cuando la tarea requiera el snapshot comercial validado más reciente. Usar snapshots anteriores sólo para reproducir checkpoints históricos concretos.
7. No volver a adjuntar PDFs históricos ya consolidados.
8. Mantener separadas tareas de negocio (`smart-imports`) y técnicas (`smart-imports-engine`).
9. No reabrir decisiones técnicas cerradas salvo que el flujo comercial descubra un bloqueo real.

## 14. Próxima acción concreta

```text
MARCA HOGAR
→ INTERNAL PORTFOLIO REVIEW COMPLETE
→ PORTFOLIO BASELINE FROZEN
→ EXTERNAL REVIEW PENDING
→ F14 NOT OPENED

PRIMARY WORKSTREAM
→ MARCA FITNESS
→ BRAND-CAND-010
→ materializar aut105
→ Matrix Validator PASS
→ cerrar F0
→ continuar Method v2
```

Marca Hogar sólo se reabre por gate externo, contradicción material o decisión explícita. No se reabren F0–F13 por defecto.

## 15. Documentos relacionados

- [SI-RESEARCH-005 — Niche 3 Phases 0–6](../06-research/niche-003-pet-care-wellness-technology/si-research-005-niche-3-phases-0-to-6.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-DECISION-014 — Adopt Niche 3 Method v2 and aut34](../09-decision-log/si-decision-014-adopt-niche3-method-v2-and-aut34.md)
- [SI-RESEARCH-006 — Niche 3 Phases 7–11 / Method v2 validation](../06-research/niche-003-pet-care-wellness-technology/si-research-006-niche-3-phases-7-to-11-method-v2-validation.md)
- [SI-DECISION-015 — Adopt aut36 and validate Method v2](../09-decision-log/si-decision-015-adopt-aut36-and-validate-method-v2-through-landed-cost-screen.md)
- [SI-BRAND-001 — Brand System reusable](../07-brand/si-brand-001-reusable-brand-system.md)
- [SI-BRAND-002 — Brand Candidate Screening](../07-brand/si-brand-002-brand-candidate-screening-method.md)
- [Marca Hogar — territorio y Candidate Register](../07-brand/brands/brand-hogar/README.md)
- [SI-DECISION-016 — Arquitectura de marca por misiones](../09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md)

<!-- ECONOMIC-BRIEFING-PENDING:START -->
## Pendiente futuro — Documento didáctico de evaluación económica para reunión con socio

### Estado

```text
TRIGGER MET
MEETING MATERIAL — PREPARE WHEN NEEDED
Brand Candidates relevantes completados hasta F13
→ Portfolio Review interno completo
```

### Objetivo

Preparar un documento simple, muy didáctico y completamente en español para explicar al socio cómo Smart Imports evalúa económicamente una oportunidad de producto.

No debe enseñar finanzas en abstracto. Debe mostrar, utilizando **uno o más productos reales investigados por Smart Imports y números propios de las matrices**, cómo una oportunidad pasa de:

```text
“parece interesante”
→
“económicamente defendible o no”
```

### Recorrido pedagógico obligatorio

```text
Precio local
→ Headroom
→ Costo de origen
→ Landed Cost
→ Margen
→ ROI
→ significado para la decisión
```

### Conceptos a explicar en lenguaje sencillo

```text
HEADROOM
→ ¿hay espacio económico suficiente para investigar la importación?

LANDED COST
→ ¿cuánto estimamos que cuesta realmente poner el producto en Argentina?

MARGEN
→ ¿cuánto queda económicamente después del costo puesto y los costos comerciales?

ROI
→ ¿qué retorno unitario obtenemos respecto del costo económico invertido?
```

### Distinciones obligatorias

```text
Headroom ≠ Landed Cost

Economic Landed Cost ≠ Total Cash Outlay

ROI sobre costo económico
≠
ROI total del negocio / capital total invertido
```

### Selección de ejemplos

Usar uno o más Product Bases reales investigados por Smart Imports y sus números reales.

Cuando el portfolio esté completo, priorizar ejemplos que permitan contrastar, por ejemplo:

```text
economía holgada
vs.
economía ajustada o no defendible
```

La selección definitiva debe hacerse recién después de completar los Brand Candidates relevantes hasta F13, para elegir casos pedagógicamente representativos del portfolio real.

### Regla de activación

El trigger ya fue cumplido. El entregable permanece como material de reunión a preparar cuando se necesite, sin bloquear el cambio de workstream a Fitness.
<!-- ECONOMIC-BRIEFING-PENDING:END -->

## 16. Changelog

| Version | Date | Change |
|---|---|---|
| 1.23.1 | 2026-10-08 | BRAND-CAND-010 completa Method v2 F0–F13 sobre aut105–aut118 PASS; NO FINALIST / FREEZE; BASE-FIT-001 queda principal reapertura por logistics gate; F14 no se abre. |
| 1.23.0 | 2026-10-07 | Marca Hogar cierra Portfolio Review interno; BASE-HOGAR-016 lead, BASE-HOGAR-006 backup; baseline congelada, revisión externa pendiente y workstream principal cambia a Marca Fitness / aut105. |
| 1.22.0 | 2026-10-05 | BRAND-CAND-006 completa F6–F13 sobre aut97–aut104 PASS; BASE-PET-003 queda FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW / NOT FIRST-STAGE FIT; candidato PORTFOLIO REVIEW READY / FREEZE; aut105 queda desbloqueado para BRAND-CAND-010. |
| 1.21.0 | 2026-10-05 | BRAND-CAND-006 cierra F5 sobre aut96 PASS; EVAL-0028 = 4/5 Media; siguiente gate F6 y aut97. |
| 1.20.0 | 2026-10-05 | Marca Fitness abre Method v2 únicamente para BRAND-CAND-010; SI-RESEARCH-070 deja F0 analysis complete / matrix pending / not closed, con Nicho ID 37 y aut105 reservados tras el lineage aut96..aut104. |
| 1.19.0 | 2026-10-05 | Marca Fitness cierra screenings: BRAND-CAND-007..010 = CORE / PASS TO METHOD V2; Brand System y Screening formalizan la trazabilidad desde FIT-CAND y el próximo gate es decidir el orden de Method v2. |
| 1.18.0 | 2026-10-05 | Marca Fitness congela baseline pre-screening v0.2 con territorio/misiones revisados, candidatos activos 001/002/005/007, 003/004 absorbidos y 006 reclasificado; siguiente gate FIT-CAND-001. |
| 1.17.0 | 2026-10-05 | Marca Hogar queda en pausa operativa hasta reuniones con socio y despachante; se documentan entregables de revisión externa y SI-BRAND-003 para ingreso reusable de oportunidades descendentes/ascendentes. |
| 1.16.0 | 2026-10-03 | BRAND-CAND-006 queda F0–F4 CLOSED sobre aut91–aut95 PASS; F5 análisis completo pero no cerrado. Se registra Decision Reporter prototipado, prioridad primera compra/revisión externa y apertura exploratoria de Marca Fitness. |
| 1.15.0 | 2026-09-30 | BRAND-CAND-005 completa F0–F13; aut90 PASS; BASE-HOGAR-028 FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW / NOT FIRST-STAGE FIT; candidato PORTFOLIO REVIEW READY / FREEZE; siguiente ejecución BRAND-CAND-006 después del cierre documental. |
| 1.13.0 | 2026-09-25 | Se registra como pendiente futuro el documento didáctico para reunión con socio sobre Precio local → Headroom → Costo de origen → Landed Cost → Margen → ROI, usando ejemplos reales de Smart Imports y activado sólo después de completar los candidatos relevantes hasta F13. |
| 1.12.0 | 2026-09-25 | BRAND-CAND-003 completa F0–F13; aut58 PASS; BASE-HOGAR-010 FINALIST — CONDITIONED; candidato PORTFOLIO REVIEW READY / FREEZE; siguiente ejecución BRAND-CAND-004. |
| 1.11.0 | 2026-09-23 | BRAND-CAND-001 completa Fase 10; aut41 PASS y próxima acción Fase 11 — Landed Cost. |
| 1.10.0 | 2026-09-21 | BRAND-CAND-001 completa Fase 9; aut40 PASS y próxima acción Fase 10 — Minimum Landed Cost Dataset. |
| 1.9.0 | 2026-09-21 | BRAND-CAND-001 completa Fases 7–8; aut39 PASS y próxima acción Fase 9 — Headroom. |
| 1.8.0 | 2026-09-18 | BRAND-CAND-001 completa Golden Run hasta Fase 6; aut37 PASS y próxima acción Fase 7. |
| 0.7.0 | 2026-08-03 | Handoff de v3/v4 y normalización de fuentes. |
| 0.8.0 | 2026-08-04 | Adopción de aut31/v5, 144 tests y cierre técnico de vistas derivadas. |
| 1.0.0 | 2026-09-11 | Matrix Validator cerrado; `aut34` adoptada; Method v2 y Fases 0–6 del Nicho 3 consolidadas. |
| 1.1.0 | 2026-09-16 | Se incorpora Brand System reusable, Marca Hogar v0.1, Brand Candidate Screening y aclaración de packing de PET-003. |
| 1.2.0 | 2026-09-17 | Se separan Brand System e instancia Marca Hogar; BRAND-CAND-002 queda PASS y se formalizan expedientes por candidato. |
| 1.3.0 | 2026-09-17 | BRAND-CAND-003 queda PASS TO METHOD V2 y se registra su handoff; próximo screening BRAND-CAND-004. |
| 1.4.0 | 2026-09-17 | BRAND-CAND-004 queda PASS TO METHOD V2 y se registra su handoff; próximo screening BRAND-CAND-005. |
| 1.5.0 | 2026-09-17 | BRAND-CAND-005 queda PASS TO METHOD V2 y se registra su handoff; próximo screening retrospectivo BRAND-CAND-006. |
| 1.6.0 | 2026-09-17 | BRAND-CAND-006 confirma Brand Fit retrospectivamente; próximo paso: consolidar aprendizajes del bloque de seis screenings. |

| 1.7.0 | 2026-09-17 | Se consolida Brand System v0.3: Territory Relationship, Screening Type y soporte formal de screening retrospectivo. |
| 1.14.0 | 2026-09-25 | BRAND-CAND-004 completa F0–F13; aut72 PASS; BASE-HOGAR-016 FINALIST — CONDITIONED; candidato PORTFOLIO REVIEW READY / FREEZE; se formaliza la regla obligatoria de cierre documental + commit/push antes de abrir el siguiente Brand Candidate. |
## Golden Run BRAND-CAND-001 — Fases 0–6

Estado:

```text
Input: BRAND-CAND-001
Method v2: Fases 0–6 COMPLETADAS
Matrix: matrix-aut37-brand-cand-001-phase6.xlsx
SHA-256: 6c0f1524fe102fe5c531edb890639bb9fa9845fbc4cc1b9e046ce9ceb96387ff
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
Next Action: Fase 7 — shortlist pre-origen
```

Cinco Product Bases pasan al gate de Fase 7: `BASE-HOGAR-002` a `BASE-HOGAR-006`. `BASE-HOGAR-001`, `BASE-HOGAR-007` y `BASE-HOGAR-008` son PB de soporte y no avanzan automáticamente.

La matriz usa el Nicho ID 32 como `MATRIX_SCOPE_ALIAS` exclusivamente por compatibilidad con `full-matrix-v5 0.7.0`. El input conceptual sigue siendo `BRAND-CAND-001`; esta fricción queda registrada para Matrix vNext / Intelligence Engine, sin reabrir ahora el schema ni el Validator.

Fuente de ejecución: [SI-RESEARCH-007](../06-research/brand-hogar/si-research-007-brand-cand-001-method-v2-golden-run-phases-0-to-6.md).
## Golden Run BRAND-CAND-001 — Fases 7–8

Estado:

```text
Input: BRAND-CAND-001
Method v2: Fases 0–8 COMPLETADAS
Matrix vigente: matrix-aut39-brand-cand-001-phase8.xlsx
SHA-256: 62341e1c202f87a531f96e9573613f9adda588e70e761eee9254e214a30a658c
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
Next Action: Fase 9 — Headroom
```

Shortlist / origen:

```text
BASE-HOGAR-003 → ACTIVE / ORIGIN CONFIRMED
BASE-HOGAR-006 → ACTIVE / ORIGIN CONFIRMED
BASE-HOGAR-002 → ACTIVE SECONDARY / ORIGIN CONFIRMED — CONDITIONAL
BASE-HOGAR-004 → WATCHLIST / ORIGIN CONFIRMED
BASE-HOGAR-005 → PAUSED
```

Las respuestas documentales pendientes de proveedores no bloquean el gate ya demostrado. Se actualiza sólo la evidencia afectada; Fase 8 se reabre únicamente ante una contradicción estructural.

Fuente de ejecución: [SI-RESEARCH-008](../06-research/brand-hogar/si-research-008-brand-cand-001-method-v2-golden-run-phases-7-to-8.md).
## Golden Run BRAND-CAND-001 — Fase 9

Estado:

```text
Input: BRAND-CAND-001
Method v2: Fases 0–9 COMPLETADAS
Matrix vigente: matrix-aut40-brand-cand-001-phase9.xlsx
SHA-256: 525e8aefb5db96a30b8d5565f05fd9c1ac283f1a8eafffbbd7d5f75f9ecc4512
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
Next Action: Fase 10 — Minimum Landed Cost Dataset
```

Resultado del gate:

```text
BASE-HOGAR-002 → SURVIVES / PASS TO F10
BASE-HOGAR-003 → SURVIVES — CONDITIONED / PASS TO F10
BASE-HOGAR-006 → SURVIVES / PASS TO F10
BASE-HOGAR-004 → WATCHLIST
BASE-HOGAR-005 → PAUSED
```

`HEADROOM ≠ LANDED COST`. Los ratios y datos comerciales exactos permanecen en la matriz operativa y registros privados.

Fase 10 debe reunir configuración exacta, Incoterm, tier/MOQ aplicable, packing, unidades por caja, dimensiones/CBM, pesos y documentación técnica mínima antes de abrir Landed Cost.

Fuente de ejecución: [SI-RESEARCH-009](../06-research/brand-hogar/si-research-009-brand-cand-001-method-v2-golden-run-phase-9-headroom.md).
## Golden Run BRAND-CAND-001 — Fase 10

Estado:

```text
Input: BRAND-CAND-001
Method v2: Fases 0–13 COMPLETADAS
Matrix vigente: matrix-aut44-brand-cand-001-phase13-corrected.xlsx
SHA-256: 37b2b37c5c61355efec271b7ecb49df74c2264e2f721830a1c2478858a850f56
Validator: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
Next Action: FREEZE BRAND-CAND-001 / continuar candidatos restantes hasta F13 / Portfolio Review futuro
```

Resultado del gate:

```text
BASE-HOGAR-002 → FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW
BASE-HOGAR-003 → STOP — REOPENABLE
BASE-HOGAR-006 → FINALIST — CONDITIONED / ELIGIBLE FOR PORTFOLIO REVIEW
BASE-HOGAR-004 → WATCHLIST
BASE-HOGAR-005 → PAUSED

BRAND-CAND-001 → PORTFOLIO REVIEW READY / FREEZE
F14 → NOT OPENED
```

Principios observados:

```text
DECISION-GRADE ≠ PROCUREMENT-GRADE
SUPPLIER RESPONSE ≠ PHASE PROGRESS
```

El contacto con proveedores enriquece la evidencia, pero no debe controlar el camino crítico cuando datos públicos o proxies conservadores permiten una decisión defendible.

F13 consolidó la shortlist final. `BRAND-CAND-001` queda en freeze hasta Portfolio Review; la revisión externa previa deberá incluir al despachante antes de decidir qué producto abre F14.

Fuente de ejecución vigente: [SI-RESEARCH-013 — Fase 13 Shortlist final](../06-research/brand-hogar/si-research-013-brand-cand-001-method-v2-golden-run-phase-13-final-shortlist.md).

<!-- METHOD-V2-GOVERNANCE-2026-10-10:START -->
## Governance Method v2 + BRAND-CAND-010 reconciliado — 2026-10-10

```text
DATA FIDELITY PREFLIGHT PASS
+
MATRIX VALIDATOR PASS

F13 HISTORICAL SNAPSHOT: matrix-aut118-brand-cand-010-phase13-final-corrected.xlsx
F13 SHA-256: 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a

CURRENT POST-CLOSE BASELINE: matrix-aut120-brand-cand-010-post-close-reconciliation.xlsx
CURRENT SHA-256: 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2

aut119 corrected: SUPERSEDED BEFORE PUBLICATION
Reconciliation: PASS / no decision change
F0–F13: CLOSED
F14: NOT OPENED
```

Antes de abrir `BRAND-CAND-007..009`, este contrato y sus scripts deben quedar documentados y publicados.
<!-- METHOD-V2-GOVERNANCE-2026-10-10:END -->
