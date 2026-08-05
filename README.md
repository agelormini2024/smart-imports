---
id: smart-imports-readme
title: Smart Imports
description: Knowledge base, business intelligence methodology and platform documentation for Smart Imports.
version: 1.0.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-08-05
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

El proyecto se encuentra en etapa fundacional avanzada. El primer módulo ejecutable del Smart Imports Intelligence Engine, el `Matrix Validator`, cerró su MVP técnico y fue publicado como primera release reproducible.

### Líneas comerciales

1. **Energía Solar Portátil:** Demanda y Competencia revisadas. Margen e Importación continúan preliminares; muestras y negociaciones permanecen pausadas hasta recuperar prioridad.
2. **Viaje organizado y equipaje funcional:** Demanda y Competencia consolidadas. La shortlist de Margen Potencial está aprobada y el screening puede retomarse después del cierre documental de la release.

### Baseline tecnológica

```text
Repositorio ejecutable: smart-imports-engine
Release: v0.1.0 — Matrix Validator MVP
Commit de release: 9f4125b
Matriz vigente: aut32
Schema vigente: full-matrix-v5 0.7.0
Compatibilidad histórica: aut29/v3, aut30/v4 y aut31/v5
Reglas de validación: 19
Test files: 40
Tests: 170
Casos CLI: 5
Fixtures E2E públicos: 10
CI remoto: verde
Resultado aut32: PASS; 0 errores; 0 warnings; 0 limitaciones
```

Avances consolidados:

- SheetJS CE `0.20.3` adoptado como única implementación XLSX mantenida.
- Fuentes y evidencias normalizadas.
- Resúmenes de Competencia, Margen y Tanda normalizados.
- Seis tablas canónicas/de detalle y tres vistas derivadas incorporadas.
- Tipos, rangos, obligaciones condicionales y consistencia por fila implementados.
- Formatos declarativos de identificadores y unicidad interna de listas implementados.
- Cobertura de validación declarada por schema.
- Reportes JSON y texto, persistencia con `--output` y exit codes documentados.
- GitHub Actions, casos CLI y fixtures E2E públicos operativos.
- ExcelJS y los artefactos experimentales retirados.
- Release pública disponible en `smart-imports-engine/releases/tag/v0.1.0`.

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
| `docs/09-decision-log/si-decision-010-adopt-aut31-and-full-matrix-v5.md` | Adopción histórica de los resúmenes normalizados en `aut31`. |
| `docs/09-decision-log/si-decision-011-adopt-aut32-and-release-matrix-validator-v0.1.0.md` | Adopción de `aut32` y formalización de la primera release. |

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

1. Cerrar el checkpoint documental de la release `v0.1.0`.
2. Retomar el screening público de Margen Potencial para la shortlist del Nicho 2.
3. Avanzar a RFQ selectivo sólo con referencias que combinen señal económica, logística suficiente y diferenciación defendible.
4. Revisar humanamente los resúmenes `BORRADOR` de `aut32` antes de marcarlos como `REVISADO`.
5. Mantener el frente solar pausado hasta recuperar prioridad y datos confiables.
6. Priorizar trabajo post-MVP del Engine únicamente cuando responda a una necesidad comercial concreta.

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.8.0 | 2026-08-03 | Estado as-built de schemas v3/v4 y 78 tests. |
| 0.9.0 | 2026-08-04 | Adopción de `aut31`, `full-matrix-v5 0.5.0`, 144 tests, resúmenes normalizados y vistas derivadas. |
| 1.0.0 | 2026-08-05 | Adopción de `aut32`, cierre del Matrix Validator MVP y publicación de la release `v0.1.0`. |
