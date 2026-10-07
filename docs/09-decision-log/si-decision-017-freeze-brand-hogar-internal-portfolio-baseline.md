---
id: si-decision-017
title: Freeze Marca Hogar Internal Portfolio Baseline
description: Cierra el Portfolio Review interno de Marca Hogar, define lead de primera etapa y congela el baseline hasta revisión externa.
version: 1.0.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-07
updated: 2026-10-07
tags:
  - decision
  - brand-hogar
  - portfolio
  - first-stage
  - external-review
  - freeze
related:
  - si-decision-016
  - si-research-071
  - si-roadmap-002
phase: brand-strategy
---

# SI-DECISION-017 — Congelar baseline interno de Portfolio de Marca Hogar

## 1. Contexto

Marca Hogar completó Brand Candidate Screening y los Brand Candidates relevantes llegaron a F13 o quedaron explícitamente diferidos.

El Portfolio Review debe responder una pregunta diferente de Method v2:

> ¿En qué orden queremos concentrar nuestra primera validación externa y eventual primera importación?

## 2. Decisión

Se decide:

1. cerrar el `Portfolio Review` interno de Marca Hogar;
2. adoptar `BASE-HOGAR-016` como `INTERNAL FIRST-STAGE LEAD`;
3. adoptar `BASE-HOGAR-006` como `FIRST-STAGE BACKUP`;
4. mantener `BASE-HOGAR-010` y `BASE-HOGAR-002` como segunda línea de portfolio, sujetos a revisión externa;
5. mantener `BASE-HOGAR-028` y `BASE-PET-003` como reserva / segunda etapa por `NOT FIRST-STAGE FIT`;
6. mantener `BRAND-CAND-002` `DEFERRED / PAUSED`;
7. no abrir F14 ni procurement por esta decisión;
8. mantener `aut104` como snapshot final de Method v2 para Marca Hogar;
9. no crear un nuevo snapshot de matriz para Portfolio Review;
10. reservar `aut105` para la materialización de F0 de `BRAND-CAND-010` en Marca Fitness;
11. congelar Marca Hogar como baseline interna hasta revisión externa o contradicción material;
12. permitir que el workstream principal pase a Marca Fitness.

## 3. Justificación

`BASE-HOGAR-016` combina el mejor balance documentado entre:

- demanda observable;
- propuesta fácil de explicar;
- instalación simple;
- baja dependencia tecnológica externa;
- economía fuerte;
- carga operativa razonable para primera etapa.

`BASE-HOGAR-006` conserva una economía muy robusta y una arquitectura localizada, pero la demanda local todavía no está demostrada. A ese gap se suman la compatibilidad eléctrica y el gate regulatorio; por eso permanece como backup inmediato condicionado y no comparte el rol de lead.

`BASE-HOGAR-010` y `BASE-HOGAR-002` siguen siendo oportunidades defendibles, aunque presentan una carga mayor de claims/filtros o instalación/compatibilidad.

`BASE-HOGAR-028` y `BASE-PET-003` ya fueron clasificados explícitamente como `NOT FIRST-STAGE FIT`.

## 4. Alternativas consideradas

### No seleccionar un lead hasta hablar con el despachante

Descartada como baseline interna porque impediría capturar el aprendizaje ya generado por Method v2 y mantendría abierto un frente que ya tiene información suficiente para priorizar.

### Elegir sólo por margen

Descartada. Primera etapa también exige considerar regulación, instalación, compatibilidad, postventa y responsabilidad técnica.

### Abrir F14 ahora

Descartada. Portfolio Review no sustituye el gate externo.

## 5. Consecuencias

### Positivas

- Marca Hogar deja de competir por atención con Fitness.
- El despachante recibe una prioridad clara.
- Se conserva un backup inmediato.
- Se mantiene una segunda línea sin descartarla.
- Se evita profundizar seis finalistas a la vez.

### Riesgos

- la revisión externa puede invertir el orden;
- un dato técnico material puede degradar al lead;
- el mercado puede cambiar antes de procurement.

Estos riesgos se aceptan porque la decisión es una baseline interna, no una compra.

## 6. Estado resultante

```text
MARCA HOGAR
→ INTERNAL PORTFOLIO REVIEW COMPLETE
→ INTERNAL FIRST-STAGE LEAD: BASE-HOGAR-016
→ BACKUP: BASE-HOGAR-006
→ SECONDARY: BASE-HOGAR-010 / BASE-HOGAR-002
→ RESERVE: BASE-HOGAR-028 / BASE-PET-003
→ EXTERNAL REVIEW PENDING
→ PROCUREMENT NOT OPENED
→ F14 NOT OPENED
→ PORTFOLIO BASELINE FROZEN
```

## 7. Relación con Matrix / Engine

No se modifica:

```text
Matrix Validator v0.1.0
full-matrix-v5 0.7.0
aut104
```

Portfolio Review no consume `aut105`.

`aut105` permanece como siguiente snapshot global para Marca Fitness.

## 8. Reapertura

El baseline de Hogar sólo se reabre por:

- resultado de despachante/revisión externa;
- contradicción material;
- cambio significativo de costos o regulación;
- decisión explícita del Founder.

No se reabren automáticamente F0–F13.

## 9. Documentos relacionados

- [SI-RESEARCH-071 — Portfolio Review Marca Hogar](../06-research/brand-hogar/si-research-071-brand-hogar-portfolio-review.md)
- [Marca Hogar](../07-brand/brands/brand-hogar/README.md)
- [SI-DECISION-016](./si-decision-016-adopt-mission-based-brand-architecture-and-screening.md)
- [SI-ROADMAP-002](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 10. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-07 | Se cierra Portfolio Review interno de Marca Hogar, se adopta BASE-HOGAR-016 como lead, BASE-HOGAR-006 como backup y se congela el baseline hasta revisión externa. |
