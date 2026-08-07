---
id: si-decision-013
title: Add decision reporting layer after Niche 2
description: Decisión de diseñar después del cierre del Nicho 2 una capa de reporting ejecutivo derivada de la matriz validada.
version: 0.1.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-08-07
updated: 2026-08-07
tags:
  - decision
  - reporting
  - decision-support
  - intelligence-engine
  - matrix
related:
  - si-decision-006
  - si-decision-011
  - si-decision-012
  - si-roadmap-002
  - si-agent-001
audience:
  - founder
  - partner
  - developer
  - assistant
phase: foundation
---
# SI-DECISION-013 — Incorporar una capa de reporting de decisiones después del Nicho 2

## Contexto

La matriz operativa se está convirtiendo en una base de datos analítica extensa. Esta profundidad mejora la trazabilidad, pero reduce la capacidad de obtener una lectura ejecutiva rápida durante una reunión con socios o una revisión de portfolio.

Las hojas `Resumen *` resuelven parte del problema, pero no sustituyen un artefacto ejecutivo orientado a explicar:

- qué se investigó;
- qué productos avanzan;
- cuáles se pausan o descartan;
- qué evidencia sostiene la decisión;
- qué números importan;
- qué riesgos y faltantes permanecen.

## Decisión

Después de cerrar el circuito completo del Nicho 2 y realizar su retrospectiva, se diseñará un módulo de Smart Imports Engine con nombre de trabajo:

```text
Decision Reporter
```

El módulo recibirá una matriz previamente validada y generará un reporte ejecutivo derivado.

## Principio central

> La matriz es la fuente de verdad. El reporte es una vista de esa fuente de verdad, nunca otra base de datos paralela.

## Primera versión

La primera versión será determinística.

```text
Matriz XLSX validada
→ lectura estructurada
→ reglas de selección de campos
→ reporte ejecutivo
```

No deberá decidir autónomamente qué importar. Si el reporte muestra `PAUSAR`, `PROFUNDIZAR` o `DESCARTAR`, esa decisión debe estar registrada explícitamente en la matriz.

El Reporter podrá utilizar reglas determinísticas y documentadas para seleccionar, ordenar, agregar o presentar información, pero no para crear una nueva decisión comercial.

## Contenido esperado

Como mínimo:

- Estado del nicho.
- Cantidad de productos investigados.
- Candidatos y descartes.
- Demanda.
- Competencia.
- Import Cost Headroom.
- Landed Cost cuando exista.
- Margen y ROI cuando existan.
- Riesgo y confianza.
- Argumentos a favor y en contra.
- Próxima acción.
- Pendientes críticos.

## IA narrativa

Una futura capa con IA podrá ayudar a redactar la explicación, pero deberá separar claramente:

```text
Datos estructurados
Decisiones registradas
Narrativa generada
```

Un LLM no será la fuente de verdad de la decisión.

## Momento de implementación

No se implementará durante el circuito actual del Nicho 2.

Motivo:

- todavía se está descubriendo qué información necesita una decisión ejecutiva;
- falta completar Landed Cost y Margen;
- diseñarlo ahora podría congelar prematuramente una vista incompleta del método.

La retrospectiva del Nicho 2 definirá el contrato funcional de la primera versión.

## Relación con Landed Cost

La necesidad de reporting refuerza la futura normalización de:

```text
Landed Cost
Landed Cost Componentes
Resumen Landed Cost
```

El Reporter consumirá esos datos una vez que el modelo haya sido validado manualmente.

## Posible interfaz futura

Sólo como hipótesis, no como contrato actual:

```bash
smart-imports report matrix.xlsx \
  --type decision \
  --niche 2 \
  --format html
```

HTML/PDF y otras salidas se definirán durante el diseño del módulo.

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-08-07 | Decisión inicial. |
