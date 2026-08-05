---
id: smart-imports-readme
title: Smart Imports
description: Knowledge base, business intelligence methodology and platform documentation for Smart Imports.
version: 0.9.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-08-04
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

El proyecto se encuentra en etapa fundacional avanzada. El primer módulo ejecutable del Smart Imports Intelligence Engine es el `Matrix Validator`, cuyo núcleo técnico está avanzado y se encuentra en cierre operativo del MVP.

### Líneas comerciales

1. **Energía Solar Portátil:** Demanda y Competencia revisadas. Margen e Importación continúan preliminares; muestras y negociaciones permanecen pausadas hasta recuperar prioridad.
2. **Viaje organizado y equipaje funcional:** Demanda y Competencia consolidadas. La shortlist de Margen Potencial está aprobada; el screening continúa coordinado con el cierre del Validator.

### Baseline tecnológica

```text
Repositorio ejecutable: smart-imports-engine
Matriz vigente: aut31
Schema vigente: full-matrix-v5 0.5.0
Compatibilidad: aut29/v3 y aut30/v4
Reglas registradas: 17
Test files: 35
Tests: 144
Resultado aut31: 0 errores; 1 warning provisional
```

Avances:

- SheetJS CE `0.20.3` adoptado como lector XLSX.
- Fuentes y evidencias normalizadas.
- Resúmenes de Competencia, Margen y Tanda normalizados.
- Seis tablas canónicas/de detalle y tres vistas derivadas incorporadas.
- Tipos, rangos, obligaciones condicionales y consistencia por fila implementados.
- 391 celdas derivadas verificadas mediante fórmulas.
- Repositorio `smart-imports-engine` temporalmente visible para revisión técnica.

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
| `docs/08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md` | Plan coordinado histórico. |
| `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md` | Punto de entrada operativo vigente. |
| `docs/09-decision-log/si-decision-010-adopt-aut31-and-full-matrix-v5.md` | Adopción de aut31 y v5. |

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

1. Completar el checkpoint documental coordinado.
2. Crear fixtures XLSX públicos end-to-end.
3. Configurar GitHub Actions.
4. Completar el manual operativo y limpiar ExcelJS/spikes.
5. Decidir el alcance bloqueante de agregados e IDs pendientes.
6. Revisar humanamente los resúmenes migrados de `aut31`.
7. Retirar el warning provisional y publicar la primera release.
8. Retomar el screening de Margen del Nicho 2 según prioridad comercial.

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.8.0 | 2026-08-03 | Estado as-built de schemas v3/v4 y 78 tests. |
| 0.9.0 | 2026-08-04 | Adopción de `aut31`, `full-matrix-v5 0.5.0`, 144 tests, resúmenes normalizados y vistas derivadas. |
