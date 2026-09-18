---
id: smart-imports-readme
title: Smart Imports
description: Knowledge base, business intelligence methodology and platform documentation for Smart Imports.
version: 1.9.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-09-18
tags:
  - smart-imports
  - knowledge-base
  - business-intelligence
  - documentation
  - brand-system
---
# Smart Imports

> Primero entender. Después invertir.

Smart Imports es un proyecto de inteligencia comercial aplicado al comercio físico y digital. Su objetivo inicial es identificar nichos rentables para importar productos desde China, validar oportunidades con bajo riesgo y construir una empresa que combine investigación sistemática, importación estratégica, e-commerce, automatización, IA, agentes y software propio.

La importación es el primer caso de uso. La visión de largo plazo es una metodología y una plataforma para descubrir, evaluar y ejecutar oportunidades comerciales.

A partir de 2026-09-16, Smart Imports incorpora además un **Brand System reusable** para definir dónde quiere jugar cada marca antes de aplicar Method v2. `Marca Hogar` es la primera implementación real; el marco está diseñado para reutilizarse en futuras marcas con territorios y misiones propios.

## Estado actual


### BRAND-CAND-001 — Golden Run Fases 0–6

La primera ejecución formal `Brand System → Method v2` completó Fases 0–6 sobre detección de fugas + corte automático. El snapshot comercial vigente para este checkpoint es `matrix-aut37-brand-cand-001-phase6.xlsx`, validado con `full-matrix-v5 0.7.0` y resultado `PASS` limpio.

```text
Brand Candidate → Method v2 → Product Bases → aut37 PASS → Fase 7
```

Research: `docs/06-research/brand-hogar/si-research-007-brand-cand-001-method-v2-golden-run-phases-0-to-6.md`.


Smart Imports se encuentra en una etapa de **selección de candidatos, preparación de validación profesional externa y validación práctica del Brand System**.

El primer módulo ejecutable del Intelligence Engine, **Matrix Validator v0.1.0**, permanece cerrado y publicado. Method v2 fue ejecutado internamente hasta `Landed Cost Screen` sobre el Nicho 3.

### Líneas comerciales

1. **Energía Solar Portátil**: piloto histórico. Prioridad pausada selectivamente.
2. **Viaje organizado y equipaje funcional**: Demanda y Competencia cerradas; screening de origen/headroom realizado; candidatos preservados para comparación transversal.
3. **Mascotas — cuidado, bienestar y tecnología**: Fases 0–11 internas ejecutadas. `BASE-PET-003` es el primer `STRONG CANDIDATE — PENDING PROFESSIONAL VALIDATION`; `BASE-PET-004` mantiene una RFQ pendiente de respuesta.

### Baseline tecnológica y comercial

```text
Repositorio ejecutable: smart-imports-engine
Matrix Validator: v0.1.0
Baseline técnica de release: aut32
Matriz comercial vigente: `matrix-aut37-brand-cand-001-phase6.xlsx`
Archivo: matrix-aut37-brand-cand-001-phase6.xlsx
Schema vigente: full-matrix-v5 0.7.0
Resultado aut37: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 219d9954acca9fefda5f6edef2eab18f93bf0b4564e45d3e1442f13d6db39a53
```

`aut32` sigue siendo la baseline técnica de la release. `aut36` se conserva como checkpoint comercial histórico del Nicho 3. `aut37` es el snapshot comercial operativo vigente.

Avances recientes:

- Method v2 validado internamente hasta `Landed Cost Screen`.
- Fases 7–11 del Nicho 3 consolidadas.
- Separación formal entre `Economic Landed Cost` y `Total Cash Outlay`.
- Primer candidato fuerte preparado para validación profesional.
- La revisión del despachante queda definida como gate profesional externo.
- Matrix Validator y `full-matrix-v5 0.7.0` permanecen cerrados.
- Brand System v0.2 definido con arquitectura `territorio → misiones → problemas → soluciones`.
- `Marca Hogar` adoptada como primera implementación, organizada por misiones y no por categorías comerciales.
- Brand Candidate Screening v0.3 operativo; `BRAND-CAND-001` a `BRAND-CAND-005` quedan `PASS TO METHOD V2` y `BRAND-CAND-006` queda `BRAND FIT CONFIRMED` como strong adjacency.

## Fuentes de verdad

| Fuente | Responsabilidad |
|---|---|
| `smart-imports` | Visión, metodología, marca, investigación, decisiones, contratos funcionales y estado integral. |
| `smart-imports-engine` | Código, schemas, reglas, tests, ADR y documentación técnica de implementación. |
| Matriz operativa | Datos estructurados de trabajo y trazabilidad operativa. |

## Documentos principales

| Documento | Propósito |
|---|---|
| `docs/standards/si-doc-001-documentation-standards.md` | Estándar documental. |
| `docs/03-functional-specifications/si-func-001-matrix-validator.md` | Contrato funcional del Matrix Validator. |
| `docs/04-technical-specifications/si-tech-001-matrix-validator-architecture.md` | Arquitectura técnica base. |
| `docs/04-technical-specifications/si-tech-002-matrix-validator-as-built.md` | Estado técnico as-built de v5. |
| `docs/05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md` | Visión y módulos del Intelligence Engine. |
| `docs/06-research/niche-003-pet-care-wellness-technology/si-research-005-niche-3-phases-0-to-6.md` | Consolidación del Nicho 3 hasta Fase 6. |
| `docs/06-research/niche-003-pet-care-wellness-technology/si-research-006-niche-3-phases-7-to-11-method-v2-validation.md` | Cierre de Fases 7–11 y validación interna de Method v2. |
| `docs/07-brand/si-brand-001-reusable-brand-system.md` | Brand System reusable para cualquier instancia de marca. |
| `docs/07-brand/si-brand-002-brand-candidate-screening-method.md` | Método reusable de Brand Candidate Screening previo a Method v2. |
| `docs/07-brand/brands/brand-hogar/README.md` | Territorio, misiones, límites y Candidate Register de Marca Hogar. |
| `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md` | Punto de entrada operativo vigente. |
| `docs/09-decision-log/si-decision-014-adopt-niche3-method-v2-and-aut34.md` | Adopción inicial de Method v2 y `aut34`. |
| `docs/09-decision-log/si-decision-015-adopt-aut36-and-validate-method-v2-through-landed-cost-screen.md` | Adopción de `aut36` y gate profesional externo. |
| `docs/09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md` | Adopción del Brand System por misiones y Brand Candidate Screening. |

## Estructura del repositorio

```text
docs/
├── standards/
├── 00-vision/
├── 01-business-manual/
├── 02-business-intelligence-manual/
├── 03-functional-specifications/
├── 04-technical-specifications/
├── 05-ai-agents/
├── 06-research/
├── 07-brand/
├── 08-roadmaps/
└── 09-decision-log/
```

## Próximos pasos

1. Procesar la respuesta pendiente de `BASE-PET-004`.
2. Continuar el screening sólo hasta reunir aproximadamente **5–6 candidatos firmes**.
3. Negociar FOB y condiciones con los proveedores finalistas.
4. Preparar un paquete homogéneo para el despachante.
5. Validar profesionalmente NCM, intervenciones, certificaciones y costos definitivos.
6. Actualizar `Landed Cost` y construir la shortlist final para decisión de importación.
7. Mantener Matrix Validator v0.1.0 y `full-matrix-v5 0.7.0` cerrados salvo requerimiento comercial bloqueante.
8. Mantener Brand System v0.3 en observación empírica y aplicar el screening a nuevas oportunidades reales cuando aparezcan.
9. Mantener diferidos naming comercial, identidad visual y expansión fuera del hogar hasta acumular experiencia real.

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.9.0 | 2026-09-18 | Golden Run de BRAND-CAND-001 cerrada hasta Fase 6; aut37 PASS y lista para shortlist pre-origen. |
| 0.8.0 | 2026-08-03 | Estado as-built de schemas v3/v4 y 78 tests. |
| 0.9.0 | 2026-08-04 | Adopción de `aut31`, `full-matrix-v5 0.5.0`, 144 tests, resúmenes normalizados y vistas derivadas. |
| 1.0.0 | 2026-09-11 | Matrix Validator cerrado; `aut34` adoptada; Method v2 y Nicho 3 Fases 0–6 consolidados. |
| 1.1.0 | 2026-09-15 | `aut36` adoptada; Method v2 validado internamente hasta Landed Cost Screen; gate del despachante formalizado. |
| 1.2.0 | 2026-09-16 | Se incorpora Brand System reusable, Marca Hogar v0.1 y Brand Candidate Screening v0.1. |
| 1.3.0 | 2026-09-17 | Refactor Brand System: metodología separada de instancias/candidatos; BRAND-CAND-002 PASS. |
| 1.4.0 | 2026-09-17 | BRAND-CAND-003 documentado como PASS TO METHOD V2; próximo screening BRAND-CAND-004. |
| 1.5.0 | 2026-09-17 | BRAND-CAND-004 documentado como PASS TO METHOD V2; próximo screening BRAND-CAND-005. |
| 1.6.0 | 2026-09-17 | BRAND-CAND-005 documentado como PASS TO METHOD V2; próximo screening retrospectivo BRAND-CAND-006. |
| 1.7.0 | 2026-09-17 | BRAND-CAND-006 confirma Brand Fit retrospectivamente; se completa el bloque inicial de seis screenings. |
| 1.0.0 | 2026-08-05 | Adopción de `aut32`, cierre del Matrix Validator MVP y publicación de la release `v0.1.0`. |
| 1.1.0 | 2026-08-07 | Matrix Validator v0.1.0 cerrado, aut33 PASS, Import Cost Headroom, preparación de Landed Cost y definición de Decision Reporter. |

| 1.8.0 | 2026-09-17 | Se consolida Brand System v0.3 y se migran los seis screenings a Territory Relationship + Screening Type. |
