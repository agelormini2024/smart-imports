---
id: si-agent-001
title: Smart Imports Intelligence Engine
description: Visión funcional, principios, módulos y estado del motor de inteligencia comercial de Smart Imports.
version: 0.3.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-08-04
tags:
  - intelligence-engine
  - ai-agents
  - automation
  - business-intelligence
  - platform
related:
  - si-func-001
  - si-tech-002
  - si-roadmap-001
  - si-roadmap-002
  - si-decision-006
  - si-decision-010
audience:
  - founder
  - partner
  - developer
phase: foundation
---

# SI-AGENT-001 — Smart Imports Intelligence Engine

> El activo más importante no será una lista de productos: será el sistema que permita descubrir, evaluar y ejecutar oportunidades de manera repetible.

## 1. Propósito

El Intelligence Engine dará soporte a descubrimiento de oportunidades, investigación, evidencias, proveedores, negociación, margen, scoring, recomendaciones y conservación del conocimiento.

No reemplaza la decisión humana ni autoriza compras, pagos o compromisos comerciales.

## 2. Flujo conceptual

```text
Fuentes
→ datos normalizados
→ evidencias
→ evaluaciones
→ score + confianza
→ recomendación explicada
→ decisión humana
```

## 3. Principios

1. Human in the loop.
2. Evidence before recommendation.
3. Confidence as first-class data.
4. Manual first, automation second.
5. Incremental delivery.
6. Structured outputs.
7. Source preservation.
8. Reversibility.
9. No automation theater.
10. Claims are not facts.

## 4. Estado del MVP 1 — Matrix Validator

```text
Estado: núcleo técnico avanzado / cierre operativo
Matriz: aut31
Schema: full-matrix-v5 0.5.0
Reglas: 17
Tests: 144
```

El Validator protege la integridad estructural y semántica de la matriz antes de utilizarla como fuente de trabajo.

## 5. Capacidades objetivo

- Investigación asistida.
- Monitoreo y extracción.
- Normalización y evidencias.
- Scoring y confianza.
- Negociación asistida.
- Margen y FOB objetivo.
- Gestión documental y RAG.
- RFQ contextual.
- Seguimiento de proveedores.
- Recomendación de compra con aprobación humana.

## 6. Módulos

| Orden conceptual | Módulo | Propósito |
|---:|---|---|
| 1 | Matrix Validator | Integridad de la matriz. |
| 2 | Supplier Response Analyzer | Extraer datos, faltantes y contradicciones. |
| 3 | Contextual RFQ Generator | RFQ y follow-ups adaptados. |
| 4 | Margin and FOB Engine | Costo, margen, ROI y FOB objetivo. |
| 5 | Scoring and Next Action Engine | Score, confianza y próxima acción. |

Candidatos adicionales: Marketplace Evidence Analyzer, Niche Candidate Normalizer, Claims Validation Gate, Product Quality Specification Builder y Compatibility and Dimension Recommender.

## 7. Estrategia de construcción

```text
Primera ejecución → descubrir
Segunda ejecución → estandarizar
Tercera ejecución → automatizar
```

- Energía Solar Portátil: primera ejecución integral.
- Viaje organizado: segunda ejecución y prueba de repetibilidad.
- Matrix Validator: primera automatización surgida de errores reales.

## 8. Próximas acciones

1. Cerrar el MVP del Matrix Validator con E2E, CI, limpieza y release.
2. Medir la siguiente fricción operativa de mayor impacto.
3. Elegir el próximo módulo con evidencia de ahorro, riesgo o retrabajo.
4. Mantener Google Sheets como sistema operativo mientras no exista una alternativa claramente superior.
