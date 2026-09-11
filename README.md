---
id: smart-imports-readme
title: Smart Imports
description: Knowledge base, business intelligence methodology and platform documentation for Smart Imports.
version: 1.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-09-11
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

Smart Imports se encuentra en una etapa de **investigación comercial estructurada y validación metodológica sobre múltiples nichos**.

El primer módulo ejecutable del Intelligence Engine, **Matrix Validator v0.1.0**, está cerrado y publicado. La matriz comercial vigente es `aut34`, validada con `full-matrix-v5 0.7.0`.

### Líneas comerciales

1. **Energía Solar Portátil**: piloto histórico. Prioridad pausada selectivamente.
2. **Viaje organizado y equipaje funcional**: Demanda y Competencia cerradas; screening de origen/headroom realizado; Landed Cost defendible pendiente.
3. **Mascotas — cuidado, bienestar y tecnología**: Method v2 ejecutado hasta Fase 6; cuatro arquitecturas avanzan y ocho Productos Base fueron materializados en `aut34`.

### Baseline tecnológica

```text
Repositorio ejecutable: smart-imports-engine
Matrix Validator: v0.1.0
Baseline técnica de release: aut32
Matriz comercial vigente: aut34
Schema vigente: full-matrix-v5 0.7.0
Test files: 40
Tests: 170
CLI: 5 casos
E2E público: 10 fixtures
CI: verde
Resultado aut34: PASS / 0 errors / 0 warnings / 0 info / 0 limitations
```

`aut32` sigue siendo la baseline técnica de la release. `aut34` es el snapshot comercial operativo actual.

Avances recientes:

- Method v2 consolidado sobre el Nicho 3.
- Jerarquía `Nicho → Familia → Arquitectura → Producto Base`.
- Fases 0–6 del Nicho 3 cerradas.
- Ocho `BASE-PET-*` materializados.
- Tres necesidades futuras de Matrix vNext detectadas sin reabrir el Engine.
- Próxima fase comercial: **Fase 7 — shortlist pre-origen**.

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
| `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md` | Punto de entrada operativo vigente. |
| `docs/09-decision-log/si-decision-014-adopt-niche3-method-v2-and-aut34.md` | Adopción de Method v2 y `aut34`. |

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

1. Ejecutar **Fase 7 — shortlist pre-origen** del Nicho 3.
2. Reducir los ocho PB antes de profundizar sourcing.
3. Ejecutar Fase 8 sólo sobre candidatos sobrevivientes.
4. Mantener `full-matrix-v5 0.7.0` estable mientras Matrix vNext no sea bloqueante.
5. No iniciar Landed Cost ni RFQ exhaustivo antes de cerrar la shortlist.
6. Mantener documentadas las hipótesis no validadas: Wellness local, suscripción, seguridad/QA y compatibilidad celular.

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.8.0 | 2026-08-03 | Estado as-built de schemas v3/v4 y 78 tests. |
| 0.9.0 | 2026-08-04 | Adopción de `aut31`, `full-matrix-v5 0.5.0`, 144 tests, resúmenes normalizados y vistas derivadas. |
| 1.0.0 | 2026-09-11 | Matrix Validator cerrado; `aut34` adoptada; Method v2 y Nicho 3 Fases 0–6 consolidados. |
| 1.0.0 | 2026-08-05 | Adopción de `aut32`, cierre del Matrix Validator MVP y publicación de la release `v0.1.0`. |
| 1.1.0 | 2026-08-07 | Matrix Validator v0.1.0 cerrado, aut33 PASS, Import Cost Headroom, preparación de Landed Cost y definición de Decision Reporter. |
