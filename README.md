---
id: smart-imports-readme
title: Smart Imports
description: Knowledge base, business intelligence methodology and future platform documentation for Smart Imports.
version: 0.8.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-08-03
tags:
  - smart-imports
  - knowledge-base
  - business-intelligence
  - documentation
---

# Smart Imports

> Primero entender. Después invertir.

Smart Imports es un proyecto de inteligencia comercial aplicado al comercio físico y digital.

Su objetivo inicial es identificar nichos de negocio rentables para importar productos desde China, validar oportunidades con bajo riesgo y construir una empresa que combine investigación sistemática, importación estratégica, e-commerce propio, automatización, inteligencia artificial, agentes IA, software propio y construcción de marca.

La importación es el primer caso de uso. La visión de largo plazo es construir una metodología y una plataforma para descubrir, evaluar y ejecutar oportunidades comerciales.

## Estado actual

El proyecto se encuentra en etapa fundacional avanzada. El Matrix Validator ya funciona como primer módulo ejecutable del Intelligence Engine y se encuentra en fase de cierre operativo del MVP.

Existen dos líneas comerciales activas:

1. **Energía Solar Portátil:** Demanda y Competencia revisadas; Margen e Importación continúan en evaluación. Las muestras y negociaciones principales están pausadas hasta que un producto recupere prioridad.
2. **Viaje organizado y equipaje funcional:** Demanda y Competencia consolidadas. La shortlist para screening de Margen Potencial quedó aprobada; el screening permanece coordinado con el cierre del Matrix Validator.

El principal activo tecnológico de largo plazo continúa siendo el:

```text
Smart Imports Intelligence Engine
```

Su primer MVP es el `Matrix Validator`.

### Avances recientes

- Repositorio privado `smart-imports-engine` creado e integrado en `main`.
- Node.js 24, pnpm 11, TypeScript, Commander y Vitest operativos.
- SheetJS CE `0.20.3` aceptado como lector XLSX después de descartar ExcelJS para matrices reales.
- `full-matrix-v3 0.1.0` validado contra `aut29`.
- `full-matrix-v4 0.6.0` validado contra `aut30`.
- Normalización de fuentes implementada mediante `Fuentes` y `Evidencia Fuentes`.
- Reglas de estructura, posiciones, claves primarias, referencias, vocabularios y valores obligatorios implementadas.
- 23 archivos de pruebas y 78 tests aprobados.
- Ambas matrices privadas finalizan con 0 errores; permanece un warning provisional de cobertura parcial.
- Principal bloqueo de cierre: normalizar `Resumen Competencia`, `Resumen Margen` y `Resumen Tanda`.
- Demanda y Competencia ML del Nicho 2 cerradas y shortlist de Margen aprobada.
- Matriz operativa evolucionada desde `aut29` a `aut30` para incorporar fuentes normalizadas.

## Estructura del repositorio

```text
docs/
├── standards/
├── 00-vision/
├── 01-business-manual/
├── 02-business-intelligence-manual/
│   ├── criteria/
│   └── procedures/
├── 03-functional-specifications/
├── 04-technical-specifications/
├── 05-ai-agents/
├── 06-research/
│   ├── niche-001-portable-solar-energy/
│   └── niche-002-travel-organization/
├── 07-brand/
├── 08-roadmaps/
└── 09-decision-log/
```

## Documentos principales

| Documento | Propósito |
|---|---|
| `docs/standards/si-doc-001-documentation-standards.md` | Estándar documental. |
| `docs/00-vision/si-00-sprint-0-foundation.md` | Sprint 0 — Foundation. |
| `docs/00-vision/si-vision-001-smart-imports-vision.md` | Visión estratégica. |
| `docs/02-business-intelligence-manual/criteria/si-bim-001-demand-evaluation.md` | Criterio Demanda. |
| `docs/02-business-intelligence-manual/criteria/si-bim-002-competition-evaluation.md` | Criterio Competencia. |
| `docs/02-business-intelligence-manual/criteria/si-bim-003-margin-potential-evaluation.md` | Criterio Margen Potencial. |
| `docs/02-business-intelligence-manual/procedures/si-bim-proc-001-marketplace-evidence-processing.md` | Procedimiento de evidencias. |
| `docs/02-business-intelligence-manual/procedures/si-bim-proc-002-supplier-rfq-and-margin-screening.md` | Procedimiento de RFQ y margen. |
| `docs/03-functional-specifications/si-func-001-matrix-validator.md` | Especificación funcional aprobada del Matrix Validator. |
| `docs/04-technical-specifications/si-tech-001-matrix-validator-architecture.md` | Arquitectura técnica mínima del Matrix Validator. |
| `docs/05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md` | Visión del Intelligence Engine. |
| `docs/06-research/si-research-001-niche-2-selection.md` | Selección del Nicho 2. |
| `docs/06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md` | Alcance del Nicho 2. |
| `docs/06-research/niche-002-travel-organization/si-research-004-demand-competition-closure.md` | Cierre de Demanda y Competencia del Nicho 2. |
| `docs/08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md` | Roadmap coordinado. |
| `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md` | Punto de entrada operativo y handoff. |
| `docs/09-decision-log/si-decision-008-close-niche-2-demand-and-competition.md` | Decisión de cierre del Nicho 2. |
| `docs/09-decision-log/si-decision-009-separate-knowledge-and-engine-repositories.md` | Separación entre conocimiento público y Engine privado. |

## Nichos activos

### 1. Energía Solar Portátil

Incluye:

- Kits solares portátiles.
- Ventiladores solares.
- Power banks solares.
- Paneles solares portátiles pequeños y medianos.

Excluye power stations, generadores y sistemas completos.

### 2. Viaje organizado y equipaje funcional

Procesado:

- Sets organizadores estándar.
- Packing cubes de compresión.
- Bolsas de compresión al vacío con bomba.
- Organizadores tecnológicos.
- Organizadores para calzado.
- Neceseres compartimentados.
- Kits de envases recargables.

Bolsas compactas para ropa usada quedaron en backlog por oferta relevante insuficiente.

## Próximos pasos

1. Actualizar y alinear la documentación pública y privada.
2. Normalizar `Resumen Competencia` como primer patrón tabular.
3. Aplicar el patrón a `Resumen Margen` y `Resumen Tanda`.
4. Crear la próxima matriz operativa y `full-matrix-v5`.
5. Completar validaciones semánticas prioritarias.
6. Crear fixtures públicos end-to-end y GitHub Actions.
7. Documentar la operación de la CLI y limpiar ExcelJS/spikes.
8. Retirar el warning provisional y publicar la primera release del Matrix Validator.
9. Retomar el screening de Margen del Nicho 2 según las prioridades comerciales.

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Versión inicial. |
| 0.2.0 | 2026-07-10 | Estado posterior a Demanda y Competencia del piloto. |
| 0.3.0 | 2026-07-15 | Margen Potencial, RFQ y criterios estratégicos. |
| 0.4.0 | 2026-07-17 | Selección de Viaje organizado como Nicho 2. |
| 0.5.0 | 2026-07-23 | Cierre de Demanda y Competencia del Nicho 2 y actualización del handoff. |
| 0.6.0 | 2026-07-24 | Consolidación del Nicho 2, shortlist de Margen, matriz aut(29) y especificación funcional del Matrix Validator. |
| 0.7.0 | 2026-07-24 | Aprobación de SI-FUNC-001, separación de repositorios y creación de SI-TECH-001. |
| 0.7.1 | 2026-07-24 | Se adopta pnpm como package manager del Smart Imports Intelligence Engine. |
| 0.8.0 | 2026-08-03 | Estado as-built del Matrix Validator, schemas v3/v4, 78 tests y roadmap de cierre operativo. |
