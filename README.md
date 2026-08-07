---
id: smart-imports-readme
title: Smart Imports
description: Knowledge base, business intelligence methodology and platform documentation for Smart Imports.
version: 1.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-08-07
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

El proyecto se encuentra en etapa fundacional avanzada, con el primer módulo ejecutable cerrado y el foco nuevamente puesto en validar el método comercial de punta a punta.

### Líneas comerciales

1. **Energía Solar Portátil:** primera ejecución integral del método. Demanda y Competencia fueron revisadas; la línea permanece en pausa selectiva y no se fuerza una conclusión positiva.
2. **Viaje organizado y equipaje funcional:** Demanda y Competencia cerradas; screening de proveedores/origen e Import Cost Headroom completados; próxima etapa: Landed Cost de los candidatos sobrevivientes.

### Baseline tecnológica

```text
Repositorio ejecutable: smart-imports-engine
Matrix Validator: v0.1.0 publicado
Baseline de release: aut32
Matriz operativa vigente: aut33
Schema vigente: full-matrix-v5 0.7.0
Test files: 40
Tests: 170
CLI: 5 casos operativos
E2E público: 10 fixtures XLSX
CI: verde
Resultado aut33: PASS / 0 errores / 0 warnings / 0 limitaciones
SHA-256 aut33: fb1905260ad24fd4bb0a8284082f1bebb92473de99c46963fb65c1228837bfd1
```

### Estado comercial del Nicho 2

El screening de origen incorporó **Import Cost Headroom**, definido como cuánto puede crecer el costo de origen antes de dejar de cumplir el margen objetivo. Es un filtro de priorización, no una estimación del costo real de importación.

Candidatos actuales para Landed Cost:

| Prioridad | Producto | Headroom aprox. | Estado |
|---:|---|---:|---|
| 1 | `BASE-TRAVEL-024` | `5,80x` | Esperando FOB para 500/1.000 sets |
| 2 | `BASE-TRAVEL-022` | `3,19x` | Profundizar |
| 3 | `BASE-TRAVEL-010` | `2,22x` | Profundizar |
| 4 | `BASE-TRAVEL-018` | `2,06x` | Profundizar |
| Condicional | `BASE-TRAVEL-023` | `3,15x` si se confirma composición | Esperar dato |

`BASE-TRAVEL-021`, `003` y `013` quedaron frágiles bajo el screening de headroom. Las fuentes no comparables no se fuerzan dentro de una simulación.

No se adopta un multiplicador genérico como sustituto del Landed Cost. La referencia anecdótica `FOB × 2,60` de un importador de sillas de oficina se conserva sólo como stress test externo y específico de esa categoría.

### Definiciones post-Nicho 2

Después de completar el circuito del Nicho 2 se formalizarán dos necesidades descubiertas durante el trabajo real:

- un modelo normalizado de `Landed Cost`, `Landed Cost Componentes` y `Resumen Landed Cost`;
- un módulo de Smart Imports Engine con nombre de trabajo `Decision Reporter`, capaz de generar un reporte ejecutivo determinístico a partir de una matriz validada.

La matriz seguirá siendo la fuente de verdad. El reporte será una vista derivada y no una base de datos paralela.

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
| `docs/04-technical-specifications/si-tech-002-matrix-validator-as-built.md` | Estado técnico verificable de la release `v0.1.0`. |
| `docs/05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md` | Visión y módulos del Intelligence Engine. |
| `docs/08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md` | Plan coordinado histórico. |
| `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md` | Punto de entrada operativo vigente. |
| `docs/09-decision-log/si-decision-010-adopt-aut31-and-full-matrix-v5.md` | Adopción histórica de aut31 y v5. |
| `docs/09-decision-log/si-decision-011-adopt-aut32-and-release-matrix-validator-v0.1.0.md` | Baseline aut32 y cierre del Matrix Validator v0.1.0. |
| `docs/09-decision-log/si-decision-012-adopt-aut33-and-headroom-first-margin-screening.md` | aut33 e Import Cost Headroom como gate previo al Landed Cost. |
| `docs/09-decision-log/si-decision-013-add-decision-reporting-layer-after-niche-2.md` | Capa de reporting ejecutivo post-Nicho 2. |

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

1. Esperar la respuesta FOB de Xichen para `BASE-TRAVEL-024` en escalas de 500 y 1.000 sets.
2. Construir el primer Landed Cost defendible y compararlo contra el headroom `5,80x`.
3. Alimentar `Simulación Margen` sólo cuando exista un costo puesto suficientemente defendible.
4. Repetir Landed Cost únicamente con los candidatos que sobrevivan el screening.
5. Cerrar el circuito end-to-end del Nicho 2.
6. Realizar retrospectiva metodológica del Nicho 2.
7. Formalizar el modelo normalizado de Landed Cost si el circuito manual lo confirma.
8. Diseñar el contrato funcional de `Decision Reporter`.
9. Actualizar schema/Engine sólo a partir de requisitos confirmados por el proceso manual.
10. Iniciar la investigación de nuevos nichos con el método ya calibrado.

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.8.0 | 2026-08-03 | Estado as-built de schemas v3/v4 y 78 tests. |
| 0.9.0 | 2026-08-04 | Adopción de `aut31`, `full-matrix-v5 0.5.0`, 144 tests, resúmenes normalizados y vistas derivadas. |
| 1.0.0 | 2026-08-05 | Adopción de `aut32`, cierre del Matrix Validator MVP y publicación de la release `v0.1.0`. |
| 1.1.0 | 2026-08-07 | Matrix Validator v0.1.0 cerrado, aut33 PASS, Import Cost Headroom, preparación de Landed Cost y definición de Decision Reporter. |
