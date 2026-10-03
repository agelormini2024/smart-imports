---
id: si-agent-002
title: Decision Reporter
description: Especificación funcional preliminar de una vista ejecutiva y trazable derivada de la matriz validada.
version: 0.1.0
status: prototype
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-03
updated: 2026-10-03
tags:
  - intelligence-engine
  - reporting
  - decision-support
  - traceability
related:
  - si-agent-001
  - si-decision-013
  - si-roadmap-002
---

# SI-AGENT-002 — Decision Reporter

## 1. Propósito

Generar una ficha ejecutiva por Product Base a partir de una matriz XLSX validada.

Principio:

> **La matriz es la fuente de verdad. El reporte es una vista derivada.**

El Reporter no crea decisiones comerciales ni completa datos faltantes por inferencia.

## 2. Input mínimo propuesto

```text
matrix_path
product_base_id
```

Ejemplo conceptual:

```text
matrix-autXX.xlsx
BASE-HOGAR-016
```

## 3. Capas de salida

### Capa ejecutiva

Ficha legible para founder / socio:

- identidad;
- decisión;
- señal de mercado;
- economía;
- razones por las que sobrevivió;
- condiciones abiertas;
- siguiente gate.

### Capa de trazabilidad

Para cada dato relevante:

```text
sheet
record ID
source relationship
quality flag
```

La trazabilidad debe utilizar IDs estables y no depender de números absolutos de fila.

## 4. Contrato preliminar

```text
identity
decision
market
economics
evidence_quality
conditions
next_action
lineage
```

## 5. Reglas ya demostradas por prototipos

### Dato ausente

```text
dato ausente ≠ dato inferible
```

Si `First-stage fit` no está declarado:

```text
NO DECLARADO EN MATRIZ
```

### Moneda

La ficha usa USD como moneda principal.

Cuando un benchmark local proviene de ARS:

```text
USD equivalente
(FX baseline utilizado: ARS/USD X)
```

El FX histórico se presenta como baseline del análisis, no como cotización actual.

### Calidad de evidencia

El Reporter debe distinguir, entre otros:

```text
SUPPLIER_DIRECT
SAME_SKU_PUBLIC
SAME_MODEL_PROXY
COMPOSITE_PROXY
SAMPLE_PRICE
DECISION_GRADE
PROCUREMENT_GRADE
```

### Métricas no comparables

Si una métrica histórica usa una fórmula diferente del estándar vigente, no debe copiarse silenciosamente.

Caso probado: `BASE-PET-003`.

La ficha normaliza el ROI al estándar actual cuando los campos necesarios existen y marca el valor como derivado por el Reporter.

## 6. Prototipos manuales realizados

Se probaron fichas para:

- `BASE-HOGAR-016`;
- `BASE-HOGAR-010`;
- `BASE-HOGAR-002`;
- `BASE-HOGAR-006`;
- `BASE-HOGAR-028`;
- `BASE-PET-003`.

Los prototipos se utilizaron para estabilizar el contenido antes de programar.

## 7. Arquitectura futura

```text
Validated XLSX
    ↓
deterministic extraction / resolution
    ↓
Decision Report Model
    ├── JSON
    ├── Markdown
    └── document renderer
```

Una capa narrativa con IA puede existir después, pero debe consumir el modelo estructurado y no sustituirlo.

## 8. Regla de implementación

No programar el módulo mientras la prioridad comercial sea cerrar la primera compra.

El momento recomendado para implementación es el período operativo posterior a la compra, mientras la mercadería se encuentra en tránsito y el flujo manual ya está suficientemente estabilizado.

## 9. CLI conceptual

No contractual:

```bash
decision-report \
  --matrix matrix.xlsx \
  --product BASE-HOGAR-016 \
  --format json|md|docx
```

## 10. Estado

```text
Functional contract: PROTOTYPED
Manual reports: AVAILABLE
Engine implementation: NOT STARTED
Priority: AFTER FIRST PURCHASE / DURING LOGISTICS LEAD TIME
```
