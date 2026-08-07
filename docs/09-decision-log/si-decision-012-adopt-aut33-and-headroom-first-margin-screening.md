---
id: si-decision-012
title: Adopt aut33 and headroom-first margin screening
description: Decisión metodológica de adoptar aut33 y utilizar Import Cost Headroom como filtro previo al Landed Cost y a la simulación definitiva de margen.
version: 0.1.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-08-07
updated: 2026-08-07
tags:
  - decision
  - aut33
  - margin
  - landed-cost
  - headroom
related:
  - si-decision-010
  - si-decision-011
  - si-roadmap-002
  - si-agent-001
audience:
  - founder
  - partner
  - developer
  - assistant
phase: foundation
---
# SI-DECISION-012 — Adoptar aut33 y screening de margen basado en headroom

## Contexto

El screening de proveedores del Nicho 2 mostró que un precio de origen bajo no alcanza para decidir qué producto conviene importar.

Durante el análisis se consideró utilizar un factor de importación uniforme para construir simulaciones preliminares. Esa aproximación fue descartada como criterio de decisión porque productos con distinto volumen, peso, Incoterm, NCM y estructura logística pueden tener costos puestos muy diferentes.

Durante la revisión surgió una pregunta más útil antes de calcular el Landed Cost:

> ¿Cuánto puede crecer el costo de origen antes de que el producto deje de cumplir el margen objetivo?

## Decisión

Se adopta `aut33` como matriz operativa comercial vigente y se incorpora el **Import Cost Headroom** como gate de screening previo al Landed Cost.

```text
Import Cost Headroom
=
Costo puesto económico unitario máximo compatible con el margen objetivo
÷
Costo unitario de origen
```

El indicador no representa un factor de importación real. Es una medida de tolerancia económica.

La secuencia metodológica pasa a ser:

```text
Demanda
→ Competencia
→ Costo de origen / RFQ liviano
→ Comparabilidad de producto
→ Import Cost Headroom
→ Landed Cost sólo para sobrevivientes
→ Simulación de margen
→ Shortlist final
→ RFQ profundo / muestra / validación real
```

## Baseline aut33

Archivo:

```text
matrix-aut33-supplier-screening-headroom-corrected.xlsx
```

Validación:

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
SHA-256: fb1905260ad24fd4bb0a8284082f1bebb92473de99c46963fb65c1228837bfd1
```

`aut32` permanece como baseline técnica de la release `Matrix Validator v0.1.0`. `aut33` la reemplaza únicamente como matriz operativa comercial vigente.

No se crearon nuevas filas `MARG-*` porque todavía no existe un costo puesto suficientemente defendible.

## Resultado del screening

Candidatos para Landed Cost:

| Producto | Headroom aprox. | Estado |
|---|---:|---|
| `BASE-TRAVEL-024` | `5,80x` | Prioridad 1 |
| `BASE-TRAVEL-022` | `3,19x` | Profundizar |
| `BASE-TRAVEL-010` | `2,22x` | Profundizar |
| `BASE-TRAVEL-018` | `2,06x` | Profundizar |
| `BASE-TRAVEL-023` | `3,15x` condicional | Esperar composición exacta |

Casos frágiles:

```text
BASE-TRAVEL-021 ≈ 1,52x
BASE-TRAVEL-003 ≈ 1,40x
BASE-TRAVEL-013 ≈ 1,35x
```

## Comparabilidad

El headroom sólo puede utilizarse de forma fuerte cuando la unidad comercial de origen es exacta o suficientemente comparable con el benchmark local.

Las fuentes deberán clasificarse conceptualmente como:

```text
EXACTA
COMPARABLE
BENCHMARK
```

No se utilizará una fuente `BENCHMARK` como si fuera una cotización exacta del Producto Base.

## Benchmark externo 2,60x

Se registró como referencia anecdótica la experiencia de un importador de sillas de oficina que estima su costo puesto agregando aproximadamente 160% al FOB, equivalente a `FOB × 2,60`.

Se decide:

- conservarlo como **stress test empírico externo**;
- identificarlo como específico de una categoría voluminosa;
- no utilizarlo como factor oficial de Smart Imports;
- reemplazar progresivamente referencias genéricas por factores históricos reales del propio proyecto.

## Consecuencias

### Positivas

- Evita hacer cálculos aduaneros detallados para productos sin suficiente espacio económico.
- Evita descartar productos sólo porque no se conoce todavía el costo puesto real.
- Reduce falsa precisión.
- Permite comparar sensibilidad entre productos antes del Landed Cost.

### Límites

- No determina ganadores.
- No reemplaza NCM, flete, seguro, derechos, tasas ni gastos locales.
- No convierte EXW en FOB.
- No resuelve diferencias de composición entre productos comparados.

## Próxima validación

El primer caso completo será `BASE-TRAVEL-024`, comparando el headroom aproximado de `5,80x` contra un Landed Cost estimado para escalas de 500 y 1.000 sets.

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-08-07 | Decisión inicial. |
