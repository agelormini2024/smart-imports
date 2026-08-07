---
id: si-agent-001
title: Smart Imports Intelligence Engine
description: Visión funcional, principios, módulos y estado del motor de inteligencia comercial de Smart Imports.
version: 0.4.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-08-07
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
Estado: v0.1.0 publicado / MVP funcional cerrado
Aplicación: 0.1.0
Schema operativo: full-matrix-v5 0.7.0
Baseline de release: aut32 / PASS
Matriz operativa vigente: aut33 / PASS
Tests: 40 archivos / 170 tests
CLI: 5 casos operativos
E2E público: 10 fixtures XLSX
CI: verde
```

`aut32` queda como baseline técnico del release. `aut33` es la matriz comercial vigente y fue validada con cero errores, warnings y limitaciones.

El Validator protege la integridad estructural y semántica de la matriz antes de utilizarla como fuente de trabajo. No debe reabrirse su desarrollo sin una necesidad concreta descubierta por el circuito comercial.

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

| Orden conceptual | Módulo | Propósito | Estado |
|---:|---|---|---|
| 1 | Matrix Validator | Integridad de la matriz. | `v0.1.0` cerrado |
| 2 | Supplier Response Analyzer | Extraer datos, faltantes y contradicciones. | Candidato |
| 3 | Contextual RFQ Generator | RFQ y follow-ups adaptados. | Candidato |
| 4 | Landed Cost and Margin Engine | Headroom, costo puesto, margen, ROI y FOB objetivo. | Contrato en descubrimiento manual |
| 5 | Scoring and Next Action Engine | Score, confianza y próxima acción. | Candidato |
| 6 | Decision Reporter | Reporte ejecutivo determinístico desde una matriz validada. | Diseñar post-Nicho 2 |

Candidatos adicionales: Marketplace Evidence Analyzer, Niche Candidate Normalizer, Claims Validation Gate, Product Quality Specification Builder y Compatibility and Dimension Recommender.

El orden conceptual no obliga a implementar todos los módulos ni fija prioridad definitiva. Cada módulo debe nacer de una fricción observada y un contrato validado manualmente.

## 7. Estrategia de construcción

```text
Primera ejecución → descubrir
Segunda ejecución → estandarizar
Tercera ejecución → automatizar
```

- Energía Solar Portátil: primera ejecución integral.
- Viaje organizado y equipaje funcional: segunda ejecución y prueba de repetibilidad.
- Matrix Validator: primera automatización surgida de errores reales.

El circuito comercial vigente del Nicho 2 es:

```text
Demanda
→ Competencia
→ screening de proveedores/origen
→ comparabilidad
→ Import Cost Headroom
→ Landed Cost sólo para sobrevivientes
→ Simulación Margen
→ shortlist final
→ RFQ profundo / muestra / validación real
```

No se utilizará un multiplicador genérico como sustituto del Landed Cost. Los benchmarks empíricos externos podrán utilizarse únicamente como stress tests y deberán conservar explícitamente su categoría, contexto y nivel de confianza.

Mientras el contrato de Landed Cost siga en descubrimiento, `full-matrix-v5 0.7.0` debe permanecer estable. Si el circuito del Nicho 2 confirma nuevas hojas canónicas, se evaluará una nueva versión de schema después de la retrospectiva.

## 8. Próximas acciones

1. Esperar la respuesta FOB de Xichen para `BASE-TRAVEL-024` en 500 y 1.000 sets.
2. Construir manualmente el primer Landed Cost defendible de `BASE-TRAVEL-024`.
3. Comparar el Landed Cost estimado contra el Headroom aproximado de `5,80x`.
4. Alimentar `Simulación Margen` sólo después de tener un costo puesto suficientemente defendible.
5. Repetir Landed Cost únicamente con los candidatos que sobrevivan el screening.
6. Cerrar el circuito end-to-end del Nicho 2.
7. Realizar retrospectiva metodológica del Nicho 2.
8. Si la experiencia lo confirma, formalizar `Landed Cost`, `Landed Cost Componentes` y `Resumen Landed Cost`.
9. Diseñar el contrato funcional de `Decision Reporter` después de esa retrospectiva.
10. Modificar schema/Engine sólo a partir de requisitos confirmados y luego iniciar nuevos nichos con el método calibrado.

## 9. Changelog

| Version | Date | Change |
|---|---|---|
| 0.4.0 | 2026-08-07 | Matrix Validator v0.1.0 cerrado; aut33 PASS; Headroom, Landed Cost y Decision Reporter incorporados como definiciones del siguiente ciclo. |
