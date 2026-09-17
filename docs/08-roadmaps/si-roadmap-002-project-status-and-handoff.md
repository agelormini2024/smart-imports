---
id: si-roadmap-002
title: Project Status and Handoff
description: Estado operativo, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports.
version: 1.3.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-09-17
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
audience:
  - founder
  - partner
  - developer
  - assistant
phase: research
---

# SI-ROADMAP-002 — Estado actual y handoff de Smart Imports

> Punto de entrada operativo obligatorio para retomar el proyecto sin depender de un chat específico.

## 1. Fuentes de verdad

```text
Documentación y negocio:
https://github.com/agelormini2024/smart-imports

Software ejecutable:
https://github.com/agelormini2024/smart-imports-engine

Snapshot comercial vigente:
matrix-aut36-niche3-method-v2-checkpoint-corrected.xlsx
→ full-matrix-v5 0.7.0
→ PASS limpio

Baseline técnica de release:
matrix-aut32-id-formats-corrected.xlsx
→ Matrix Validator v0.1.0
```

No confundir:

- `aut32`: baseline técnica de la release del Validator.
- `aut34`: snapshot comercial anterior, correspondiente al cierre de Fase 6 del Nicho 3.
- `aut36`: snapshot comercial operativo vigente, con Method v2 materializado hasta Landed Cost Screen.

## 2. Snapshot al 2026-09-16

| Campo | Estado |
|---|---|
| Fase general | Research / validación del método sobre múltiples nichos |
| Matrix Validator | v0.1.0 publicado y cerrado |
| Schema operativo | `full-matrix-v5 0.7.0` |
| Tests | 40 archivos / 170 tests |
| CLI | 5 casos operativos |
| E2E público | 10 fixtures |
| CI | Verde |
| Matriz comercial vigente | `aut36` |
| Resultado aut36 | PASS / 0 errors / 0 warnings / 0 info / 0 limitations |
| Nicho 1 — Energía Solar Portátil | Pausado selectivamente |
| Nicho 2 — Viaje organizado | Screening de origen/headroom realizado; Landed Cost defendible pendiente |
| Nicho 3 — Mascotas | Method v2 ejecutado internamente hasta Fase 11; primer strong candidate pendiente de validación profesional |
| Próxima acción comercial | consolidación de finalistas y preparación del gate profesional externo del Nicho 3 |
| Brand System | v0.2 definido; `Marca Hogar` como primera implementación reusable |
| Brand Candidate Screening | v0.2 operativo; `BRAND-CAND-001`, `BRAND-CAND-002` y `BRAND-CAND-003` = `PASS TO METHOD V2` |
| Próxima acción Brand | `BRAND-CAND-004 — Monitor de consumo energético` |

## 3. Snapshot operativo — 2026-09-17

### Estado general

Smart Imports completó la validación interna de Method v2 hasta `Landed Cost Screen` sobre el Nicho 3.

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Baseline técnica: aut32
Snapshot comercial vigente: aut36
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

## 4. Matriz operativa vigente — aut36

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
- Materialización operativa vigente: `aut36` PASS.
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

El Brand System no modifica `aut36`, `full-matrix-v5 0.7.0` ni Matrix Validator v0.1.0. Las necesidades futuras de modelado de Brand, Territory, Mission, Problem, Solution y Brand Fit se registran conceptualmente antes de decidir Matrix vNext o cambios del Intelligence Engine.

## 12. Bloqueos y dependencias

| Tema | Estado | Acción |
|---|---|---|
| Matrix Validator | Cerrado | No reabrir sin requerimiento comercial |
| Matrix vNext | No bloqueante | Registrar requisitos y diferir |
| Brand System | Validación práctica | Continuar Brand Candidate Screening y ajustar por evidencia de uso real |
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
5. Para tareas de marca, consultar `SI-BRAND-001`, `SI-BRAND-002` y `SI-DECISION-016`.
6. Adjuntar `aut36` sólo cuando la tarea requiera datos privados de la matriz.
7. No volver a adjuntar PDFs históricos ya consolidados.
8. Mantener separadas tareas de negocio (`smart-imports`) y técnicas (`smart-imports-engine`).
9. No reabrir decisiones técnicas cerradas salvo que el flujo comercial descubra un bloqueo real.

## 14. Próxima acción concreta

```text
Nicho 3
→ consolidación de finalistas y preparación del gate profesional externo
→ completar y consolidar los finalistas antes de la validación profesional
```

```text
Marca Hogar
→ continuar Brand Candidate Screening
→ próximo caso: BRAND-CAND-002 — Purificación de agua doméstica
→ ajustar el filtro sólo a partir de evidencia de uso real
```

No iniciar Landed Cost ni RFQ exhaustivo antes de cerrar la shortlist comercial del Nicho 3.

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

## 16. Changelog

| Version | Date | Change |
|---|---|---|
| 0.7.0 | 2026-08-03 | Handoff de v3/v4 y normalización de fuentes. |
| 0.8.0 | 2026-08-04 | Adopción de aut31/v5, 144 tests y cierre técnico de vistas derivadas. |
| 1.0.0 | 2026-09-11 | Matrix Validator cerrado; `aut34` adoptada; Method v2 y Fases 0–6 del Nicho 3 consolidadas. |
| 1.1.0 | 2026-09-16 | Se incorpora Brand System reusable, Marca Hogar v0.1, Brand Candidate Screening y aclaración de packing de PET-003. |
| 1.2.0 | 2026-09-17 | Se separan Brand System e instancia Marca Hogar; BRAND-CAND-002 queda PASS y se formalizan expedientes por candidato. |
| 1.3.0 | 2026-09-17 | BRAND-CAND-003 queda PASS TO METHOD V2 y se registra su handoff; próximo screening BRAND-CAND-004. |
