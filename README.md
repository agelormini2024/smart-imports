---
id: smart-imports-readme
title: Smart Imports
description: Knowledge base, business intelligence methodology and future platform documentation for Smart Imports.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-07-10
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

La importación es el primer caso de uso. La visión de largo plazo es construir una plataforma y metodología para descubrir, evaluar y ejecutar oportunidades comerciales.

---

## Estado actual

El proyecto se encuentra en etapa fundacional, con metodología inicial ya aplicada sobre el caso piloto **Energía Solar Portátil**.

Actualmente se está trabajando en:

- Arquitectura documental.
- Visión estratégica.
- Business Intelligence Manual.
- Matriz de oportunidades.
- Decision Log.
- Caso piloto: Energía Solar Portátil.
- Procedimiento operativo para procesar evidencias de marketplace y fuentes externas.

Avances recientes:

- Se aplicó el criterio **Demanda** al nicho Energía Solar Portátil.
- Se aplicó el criterio **Competencia** al nicho Energía Solar Portátil.
- Se definió una estructura operativa por capas: fuentes, productos base, evidencias, evaluaciones y dashboard.
- Se decidió excluir generadores solares / power stations del nicho Energía Solar Portátil y evaluarlos potencialmente en un nicho separado.

---

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
├── 07-brand/
├── 08-roadmaps/
└── 09-decision-log/
```

---

## Documentos principales

| Documento | Propósito |
|---|---|
| `docs/standards/si-doc-001-documentation-standards.md` | Define el estándar documental del proyecto. |
| `docs/00-vision/si-00-sprint-0-foundation.md` | Define el Sprint 0 — Foundation. |
| `docs/00-vision/si-vision-001-smart-imports-vision.md` | Define la visión estratégica de Smart Imports. |
| `docs/02-business-intelligence-manual/README.md` | Índice del Business Intelligence Manual. |
| `docs/02-business-intelligence-manual/criteria/si-bim-000-confidence-in-evaluations.md` | Define el concepto de Confianza. |
| `docs/02-business-intelligence-manual/criteria/si-bim-001-demand-evaluation.md` | Define el criterio Demanda. |
| `docs/02-business-intelligence-manual/criteria/si-bim-002-competition-evaluation.md` | Define el criterio Competencia. |
| `docs/02-business-intelligence-manual/procedures/si-bim-proc-001-marketplace-evidence-processing.md` | Define el procedimiento operativo provisorio para procesar evidencias de marketplace y fuentes externas. |
| `docs/09-decision-log/README.md` | Índice del Decision Log. |

---

## Caso piloto

El caso piloto actual es:

```text
Energía Solar Portátil
```

Subcategorías analizadas:

- Kits solares portátiles.
- Ventiladores solares.
- Power banks solares.
- Paneles solares portátiles.

Subcategorías excluidas del nicho portátil:

- Generadores solares.
- Power stations.
- Sistemas solares de mayor escala.

Estas últimas podrán evaluarse dentro de un futuro nicho separado, por ejemplo:

```text
Energía solar no portátil
```

---

## Próximos pasos

1. Documentar el criterio `Margen Potencial`.
2. Aplicar Margen Potencial al nicho Energía Solar Portátil.
3. Evaluar la creación de un nuevo nicho: `Energía solar no portátil`.
4. Documentar el procedimiento operativo como base para una futura automatización con n8n.
5. Continuar incorporando aprendizajes del piloto al Business Intelligence Manual.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Versión inicial del README raíz. |
| 0.2.0 | 2026-07-10 | Se actualizó el estado del proyecto luego de aplicar Demanda y Competencia al piloto Energía Solar Portátil y documentar el procedimiento operativo. |
