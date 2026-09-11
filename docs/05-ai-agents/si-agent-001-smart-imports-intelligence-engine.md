---
id: si-agent-001
title: Smart Imports Intelligence Engine
description: Visión funcional, principios, módulos y estado del motor de inteligencia comercial de Smart Imports.
version: 0.4.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-09-11
tags:
  - intelligence-engine
  - ai-agents
  - automation
  - business-intelligence
  - platform
related:
  - si-decision-014
  - si-research-005
  - si-func-001
  - si-tech-002
  - si-roadmap-001
  - si-roadmap-002
  - si-decision-006
  - si-decision-010
  - si-decision-011
  - si-decision-012
  - si-decision-013
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
Estado: cerrado y publicado
Application: 0.1.0
Tag: v0.1.0
Schema operativo: full-matrix-v5 0.7.0
Baseline técnica: aut32 / PASS
Snapshot comercial vigente: aut34 / PASS
Tests: 40 archivos / 170 tests
CLI: 5 casos
E2E público: 10 fixtures
CI: verde
```

El Validator protege la integridad estructural y semántica de la matriz y permanece cerrado mientras no exista un requerimiento comercial bloqueante.

## 5. Capacidades objetivo

- Investigación asistida.
- Monitoreo y extracción.
- Normalización y evidencias.
- Scoring y confianza.
- Negociación asistida.
- **Import Cost Headroom** como gate de screening previo al costo puesto.
- **Landed Cost** por escenario, separando costo económico y desembolso financiero.
- Margen, ROI y FOB objetivo.
- Gestión documental y RAG.
- RFQ contextual.
- Seguimiento de proveedores.
- Recomendación de compra con aprobación humana.
- **Decision Reporter** determinístico para transformar una matriz validada en una vista ejecutiva explicable.

Definiciones descubiertas durante el Nicho 2:

```text
Import Cost Headroom
=
Costo puesto económico unitario máximo compatible con el margen objetivo
/
Costo unitario de origen
```

El Headroom mide tolerancia económica; **no es una estimación del costo de importación**.

El futuro modelo de Landed Cost deberá distinguir:

```text
Costo puesto económico
!=
Desembolso financiero total
```

La matriz validada seguirá siendo la fuente de verdad. Los reportes serán vistas derivadas y no bases de datos paralelas.

## 6. Módulos

| Estado | Módulo | Propósito |
|---|---|---|
| Cerrado | Matrix Validator v0.1.0 | Integridad de la matriz. |
| Candidato | Supplier Response Analyzer | Extraer datos, faltantes y contradicciones. |
| Candidato | Contextual RFQ Generator | RFQ y follow-ups adaptados. |
| Futuro | Landed Cost / Margin Engine | Costo puesto, margen, ROI y sensibilidad. |
| Futuro | Scoring and Next Action Engine | Score, confianza y próxima acción. |

Requisitos/capacidades descubiertos por Method v2 y el Nicho 3:

- Niche / Architecture / Product Base Normalizer.
- Competition Relation Classifier: `DIRECTA | INDIRECTA | SUSTITUTO | BENCHMARK`.
- Claims Validation Gate.
- Connectivity Compatibility Gate.
- Service Continuity Risk Analyzer.
- Measurement Validity Gate.
- Product Quality Specification Builder.
- Brand Potential Evaluator.

Estas capacidades son backlog funcional. No implican implementación inmediata.

## 7. Estrategia de construcción

```text
Primera ejecución → descubrir
Segunda ejecución → estandarizar
Tercera ejecución → tensionar el método con mayor complejidad
Luego → automatizar sólo capacidades estabilizadas
```

- Energía Solar Portátil: primera ejecución integral.
- Viaje organizado: segunda ejecución y estandarización de matriz/evidencia.
- Mascotas — cuidado, bienestar y tecnología: tercera ejecución; incorpora IoT, seguridad, software, servicios recurrentes y Wellness.
- Matrix Validator: primera automatización surgida de errores reales y ya cerrada como v0.1.0.

## 8. Próximas acciones

1. Ejecutar Fase 7 — shortlist pre-origen del Nicho 3.
2. Medir la siguiente fricción operativa de mayor impacto.
3. Mantener Matrix Validator v0.1.0 cerrado.
4. No implementar Matrix vNext hasta que Familia/Arquitectura, Tipo Competencia o Next Action sean bloqueantes.
5. Mantener Landed Cost, Supplier Response Analyzer, RFQ contextual, conectividad, continuidad de servicio y validez de mediciones como capacidades candidatas hasta que el trabajo real justifique su implementación.
6. Mantener Google Sheets + XLSX como sistema operativo mientras no exista una alternativa claramente superior.
