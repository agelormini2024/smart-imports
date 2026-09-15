---
id: smart-imports-readme
title: Smart Imports
description: Knowledge base, business intelligence methodology and platform documentation for Smart Imports.
version: 1.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-09-15
tags:
  - smart-imports
  - knowledge-base
  - business-intelligence
  - documentation
---
# Smart Imports

> Primero entender. Después invertir.

Smart Imports es un proyecto de inteligencia comercial aplicado al comercio físico y digital. Su objetivo inicial es identificar nichos rentables para importar productos desde China, validar oportunidades con bajo riesgo y construir una empresa que combine investigación sistemática, importación estratégica, e-commerce, automatización, IA, agentes y software propio.

La importación es el primer caso de uso. La visión de largo plazo es una metodología y una plataforma para descubrir, evaluar y ejecutar oportunidades comerciales.

## Estado actual

Smart Imports se encuentra en una etapa de **selección de candidatos y preparación de validación profesional externa**.

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
Matriz comercial vigente: aut36
Archivo: matrix-aut36-niche3-method-v2-checkpoint-corrected.xlsx
Schema vigente: full-matrix-v5 0.7.0
Resultado aut36: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
SHA-256: 219d9954acca9fefda5f6edef2eab18f93bf0b4564e45d3e1442f13d6db39a53
```

`aut32` sigue siendo la baseline técnica de la release. `aut36` es el snapshot comercial operativo vigente.

Avances recientes:

- Method v2 validado internamente hasta `Landed Cost Screen`.
- Fases 7–11 del Nicho 3 consolidadas.
- Separación formal entre `Economic Landed Cost` y `Total Cash Outlay`.
- Primer candidato fuerte preparado para validación profesional.
- La revisión del despachante queda definida como gate profesional externo.
- Matrix Validator y `full-matrix-v5 0.7.0` permanecen cerrados.

## Fuentes de verdad

| Fuente | Responsabilidad |
|---|---|
| `smart-imports` | Visión, metodología, investigación, decisiones, contratos funcionales y estado integral. |
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
| `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md` | Punto de entrada operativo vigente. |
| `docs/09-decision-log/si-decision-014-adopt-niche3-method-v2-and-aut34.md` | Adopción inicial de Method v2 y `aut34`. |
| `docs/09-decision-log/si-decision-015-adopt-aut36-and-validate-method-v2-through-landed-cost-screen.md` | Adopción de `aut36` y gate profesional externo. |

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

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.8.0 | 2026-08-03 | Estado as-built de schemas v3/v4 y 78 tests. |
| 0.9.0 | 2026-08-04 | Adopción de `aut31`, `full-matrix-v5 0.5.0`, 144 tests, resúmenes normalizados y vistas derivadas. |
| 1.0.0 | 2026-09-11 | Matrix Validator cerrado; `aut34` adoptada; Method v2 y Nicho 3 Fases 0–6 consolidados. |
| 1.1.0 | 2026-09-15 | `aut36` adoptada; Method v2 validado internamente hasta Landed Cost Screen; gate del despachante formalizado. |
| 1.0.0 | 2026-08-05 | Adopción de `aut32`, cierre del Matrix Validator MVP y publicación de la release `v0.1.0`. |
| 1.1.0 | 2026-08-07 | Matrix Validator v0.1.0 cerrado, aut33 PASS, Import Cost Headroom, preparación de Landed Cost y definición de Decision Reporter. |
