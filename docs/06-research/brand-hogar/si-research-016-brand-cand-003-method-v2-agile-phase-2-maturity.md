---
id: si-research-016
title: BRAND-CAND-003 — Method v2 Agile — F2 Maturity
description: Evaluación de madurez de las arquitecturas de tratamiento doméstico del aire interior.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-24
updated: 2026-09-24
phase: business-intelligence
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-003
  - indoor-air
  - phase-2
---

# Smart Imports — BRAND-CAND-003 — Method v2 Agile
## F2 — Maturity (Madurez)

| Campo | Valor |
|---|---|
| Documento | `si-research-016` |
| Brand | `brand-hogar` |
| Brand Candidate | `BRAND-CAND-003 — Tratamiento doméstico del aire interior` |
| Fase | `F2 — Maturity` |
| Modalidad | `AUTO` |
| Fecha | `2026-09-24` |
| Estado | `CLOSED` |
| F1 checkpoint | `aut46 PASS clean` |
| Baseline matriz | `matrix-aut46-brand-cand-003-phase1.xlsx` |
| Matriz preparada | `matrix-aut47-brand-cand-003-phase2.xlsx` |
| Schema | `full-matrix-v5 0.7.0` |
| Validator | `Matrix Validator 0.1.0` |

---

## 1. Input vigente

F1 quedó formalmente validada sobre:

```text
matrix-aut46-brand-cand-003-phase1.xlsx
SHA-256: 0b3a85792a8db5c60af4e75c22e69bd29b868e6628c1b8798b9954b45737cce5
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

F1 produjo ocho familias/benchmarks:

```text
A1 — portátil de filtración mecánica de partículas
A2 — portátil combinado: partículas + medio sorbente para gases/olores
A3 — filtración central / HVAC de partículas
A4 — tratamiento central / HVAC combinado de partículas + gases
A5 — captura electrónica / electrostática de partículas
A6 — filtración + UVGI complementaria
A7 — tratamiento reactivo de gases: PCO / plasma / tecnologías afines
A8 — generación intencional de ozono [NEGATIVE BENCHMARK]
```

Pregunta de F2:

> ¿Qué tan estabilizada está cada arquitectura en términos de mecanismo, medición de desempeño, disponibilidad comercial, mantenimiento, seguridad y dependencia de una implementación específica?

F2 no mide todavía demanda argentina, competencia local, Brand Potential, origen ni economía.

---

## 2. Regla de interpretación

`MATURITY (MADUREZ)` no equivale a atractivo comercial.

Se observa cualitativamente:

```text
1. mecanismo técnicamente establecido;
2. métricas / métodos de prueba comparables;
3. formatos comerciales repetibles;
4. modelo de mantenimiento y consumibles conocido;
5. estabilidad de claims defendibles;
6. dependencia de instalación o infraestructura;
7. carga de seguridad / subproductos;
8. heterogeneidad entre implementaciones.
```

No se usa score agregado.

Estados de trabajo:

```text
HIGH
MEDIUM-HIGH
MEDIUM
LOW-MEDIUM / CONDITIONAL
NEGATIVE BENCHMARK
```

---

## 3. Señales de madurez del mercado / tecnología

### 3.1 Portátiles para partículas: fuerte estandarización

La categoría de room air cleaners cuenta con métodos estandarizados de medición de desempeño mediante ANSI/AHAM AC-1 y programas de certificación independiente basados en CADR.

La EPA usa CADR como referencia práctica para dimensionar equipos portátiles para partículas y distingue expresamente esta métrica del desempeño sobre gases.

Lectura:

> La combinación `airflow + eficiencia de captura + CADR + tamaño de ambiente + ruido + consumible` está suficientemente estabilizada como para comparar productos sin depender sólo de claims comerciales.

### 3.2 Gases: mecanismo conocido, comparabilidad menos universal

La adsorción/quimisorción mediante carbón u otros medios es un mecanismo establecido. Sin embargo, la EPA advierte que CADR corresponde a partículas y no constituye una medición de desempeño sobre gases.

AHAM posee además un estándar específico de reducción química (`ANSI/AHAM AC-4-2022`), señal de maduración metodológica, pero esto no implica que el mercado use una única métrica universal equivalente al CADR de partículas.

Lectura:

> La tecnología es madura; la comparación comercial de capacidad real para gases sigue siendo menos directa y más dependiente del medio, masa, contaminante y método de prueba.

### 3.3 HVAC / in-duct: tecnología estable con dependencia de infraestructura

La filtración central residencial y sus ratings MERV están ampliamente establecidos. ASHRAE documenta medios filtrantes, filtros electrónicos, gas-phase filters y consecuencias de presión / airflow.

Lectura:

> La madurez técnica es alta, pero el producto depende más del sistema instalado, compatibilidad, dimensionamiento, runtime e intervención técnica. Eso es complejidad de deployment, no inmadurez del mecanismo.

### 3.4 Tecnologías electrónicas: comerciales y antiguas, pero más heterogéneas

Precipitadores electrostáticos y otras tecnologías electrónicas existen hace tiempo y están formalmente reconocidos por ASHRAE.

Sin embargo, el desempeño depende de la implementación y aparece una dimensión adicional de mantenimiento y emisiones de ozono. CARB exige testing específico de ozono para determinados air cleaners electrónicos.

Lectura:

> Existencia comercial prolongada no elimina el riesgo de evidencia, seguridad ni mantenimiento. La familia es madura como categoría tecnológica, pero menos estandarizada como promesa de producto doméstico simple.

### 3.5 UVGI: mecanismo consolidado, desempeño muy dependiente de diseño

UV-C/UVGI es una tecnología establecida de inactivación microbiológica y puede integrarse en HVAC o equipos standalone. ASHRAE enfatiza que no es un filtro y que su efectividad depende de condiciones de exposición/dosis.

Lectura:

> El principio técnico es maduro; la credibilidad de una implementación residencial específica no puede inferirse de la mera presencia de una lámpara UV.

### 3.6 PCO / plasma / reacción química: madurez menor como producto doméstico defendible

ASHRAE registra estas tecnologías, pero advierte que algunos equipos pueden reducir contaminantes mientras otros resultan poco efectivos y que pueden generarse subproductos por oxidación incompleta.

Lectura:

> Existe mercado y principio técnico, pero la heterogeneidad de resultados y subproductos mantiene la familia en estado condicionado para una propuesta de marca basada en claims verificables.

---

## 4. Resultado por arquitectura

| Arquitectura | Madurez F2 | Lectura |
|---|---|---|
| `A1` Portátil mecánica de partículas | `HIGH` | Categoría estable; CADR y métodos comparables; consumible y mantenimiento conocidos. |
| `A2` Portátil partículas + gases | `MEDIUM-HIGH` | Arquitectura comercial madura; partículas comparables, desempeño gas-phase menos universal y muy dependiente del medio. |
| `A3` Central / HVAC partículas | `HIGH — TECHNICAL` | Filtración y MERV consolidados; mayor dependencia de infraestructura, compatibilidad y runtime. |
| `A4` Central / HVAC partículas + gases | `MEDIUM` | Mecanismos conocidos, pero deployment, pressure drop, sizing y sorbente elevan especialización. |
| `A5` Electrónica / electrostática | `MEDIUM` | Categoría estable pero implementación heterogénea; mantenimiento, desempeño real y ozono requieren control adicional. |
| `A6` Filtración + UVGI | `MEDIUM` | UVGI es tecnológicamente maduro, pero el valor del equipo depende de dosis/geometría y evidencia de implementación. |
| `A7` PCO / plasma / afines | `LOW-MEDIUM / CONDITIONAL` | Existencia comercial sin estabilidad suficiente para aceptar claims amplios; subproductos y eficacia requieren evidencia fuerte. |
| `A8` Ozono intencional | `NEGATIVE BENCHMARK` | No avanza como candidato normal para uso residencial ocupado. |

---

## 5. Conclusión F2

La necesidad de tratamiento del aire y sus mecanismos principales son comercial y técnicamente maduros, pero la madurez no está distribuida uniformemente.

La conclusión operativa es:

```text
PARTICLE MEDIA FILTRATION
→ most standardized / easiest to compare

GAS-PHASE SORPTION
→ established mechanism / weaker universal comparability

HVAC DEPLOYMENT
→ technically mature / infrastructure-dependent

ELECTRONIC + UVGI
→ established mechanisms / implementation-specific evidence burden

PCO / PLASMA
→ commercially present / higher evidence and by-product uncertainty

INTENTIONAL OZONE
→ negative benchmark for normal occupied-home use
```

Aprendizaje estructural:

> `TECHNOLOGY MATURITY (MADUREZ DE TECNOLOGÍA) ≠ PRODUCT CLAIM MATURITY (MADUREZ DEL CLAIM DEL PRODUCTO)`.

Un principio físico puede estar muy estudiado y, aun así, una implementación comercial particular requerir evidencia propia.

---

## 6. Consecuencias para fases posteriores

### F3 — Demanda

La evidencia de demanda debe capturarse separando al menos:

```text
D1 — purificadores portátiles de partículas / HEPA como arquitectura comercial dominante
D2 — portátiles partículas + gases/olores cuando el medio sorbente sea material
D3 — sistemas HVAC / in-duct si existe oferta local relevante
D4 — tecnologías electrónicas/UV/reactivas sólo como capas competitivas o segmentos distinguibles
```

No inferir demanda por:

```text
cantidad de resultados de búsqueda
existencia de estándares
presencia de marcas globales
cantidad de tecnologías posibles
```

F3 debe usar evidencia transaccional / comercial local siguiendo las reglas de la Golden Run.

### F5 — Brand Potential

La madurez sugiere una tensión útil:

- arquitecturas muy maduras facilitan explicación, validación y postventa;
- también pueden tener menor diferenciación por tecnología;
- tecnologías activas pueden parecer más diferenciadas, pero trasladan una carga mayor de prueba y riesgo de claim.

No resolver esta tensión en F2.

### F6 — Product Bases

No crear Product Bases todavía.

Las fronteras deberán considerar no sólo mecanismo sino también diferencias materiales en:

- contaminante / job;
- deployment;
- consumibles;
- mantenimiento;
- seguridad;
- instalación;
- economía;
- postventa.

---

## 7. Gate F2

Pregunta:

> ¿La madurez de las arquitecturas está suficientemente caracterizada como para investigar demanda sin seguir ampliando tecnología por curiosidad?

Resultado conceptual:

```text
PASS
```

Razones:

- A1/A2 poseen suficiente estabilidad conceptual y comercial;
- HVAC está suficientemente entendido como deployment distinto;
- electrónicas y UVGI pueden seguirse como familias condicionadas;
- PCO/plasma no requieren investigación técnica adicional antes de F3;
- ozono permanece cerrado como benchmark negativo;
- investigación adicional de principios físicos no cambiaría el siguiente gate.

Aplicación de `MINIMUM SUFFICIENT EVIDENCE`:

> detener investigación de madurez y abrir Demanda.

---

## 8. Materialización en matriz vigente

`full-matrix-v5 0.7.0` no tiene una entidad nativa para `Solution Architecture` ni `Architecture Maturity`.

No se modifica el schema.

No se crean:

- Product Bases prematuros;
- scores de madurez artificiales;
- Evaluaciones sobre criterios comerciales todavía no ejecutados;
- Evidencias forzadas a un criterio que no corresponde;
- fuentes activas huérfanas.

La materialización de F2 se realiza mediante el `MATRIX_SCOPE_ALIAS` existente (`Nicho ID 33`):

- `Documento Research` apunta a `si-research-016`;
- `Proxima Accion` deja preparado el gate colaborativo F3;
- `Notas` registra F1 CLOSED, el resultado de madurez F2 y la fricción de schema para Matrix vNext.

Archivo:

```text
matrix-aut47-brand-cand-003-phase2.xlsx
```

---

## 9. Estado formal

```text
F0 — CLOSED
F1 — CLOSED

F2 — CLOSED

Validation checkpoint:
matrix-aut47-brand-cand-003-phase2.xlsx
SHA-256: 4bfa28d24031853d5ec16ef6cae05b6aeaa6f346d4a653a0c56c85a7468b0ba5
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0

NEXT:
F3 — Demand
→ COLLABORATIVE
→ primer gate humano de este candidato
```

Esto coincide con el contrato observado en la Golden Run: F0–F2 AUTO; F3 Demanda requiere colaboración para evidencia de Mercado Libre.

---

## 10. Fuentes públicas — Minimum Sufficient Evidence

1. Smart Imports — Golden Run Method v2 F0–F6  
   https://github.com/agelormini2024/smart-imports/blob/main/docs/06-research/brand-hogar/si-research-007-brand-cand-001-method-v2-golden-run-phases-0-to-6.md

2. U.S. EPA — *Guide to Air Cleaners in the Home*  
   https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home

3. U.S. EPA — *Indoor Air Filtration*  
   https://www.epa.gov/wildfires/indoor-air-filtration

4. ASHRAE — *Position Document on Filtration and Air Cleaning*  
   https://www.ashrae.org/file%20library/about/position%20documents/pd-on-filtration-and-air-cleaning-english.pdf

5. ASHRAE Handbook — *Air Cleaners for Particulate Contaminants*  
   https://handbook.ashrae.org/Handbooks/S24/IP/s24_ch29/s24_ch29_ip.aspx

6. ASHRAE Handbook — *In-Room Air Cleaners*  
   https://handbook.ashrae.org/Handbooks/A23/IP/A23_Ch66/a23_ch66_ip.aspx

7. AHAM — `ANSI/AHAM AC-1-2020` — Portable Electric Room Air Cleaners  
   https://www.aham.org/itemdetail?category=padstd&iproductcode=30002

8. AHAM — standards chart (`AC-1`, `AC-4`, `AC-5`, `AC-7`)  
   https://www.aham.org/AHAM/Standard_Chart_Page.aspx

9. AHAM Verifide — Directory of Certified Room Air Cleaners  
   https://ahamverifide.org/directory-of-air-cleaners/

10. California Air Resources Board — Air Cleaner Regulation / ozone  
    https://ww2.arb.ca.gov/resources/documents/indoor-air-cleaning-devices-regulation

11. California Air Resources Board — Air Cleaner Information for Manufacturers  
    https://ww2.arb.ca.gov/ForAirCleanerManufacturers

---

## 11. Changelog

### 2026-09-24 — v0.1.1

- `aut47` validada con Matrix Validator 0.1.0 / full-matrix-v5 0.7.0;
- resultado `PASS` limpio, sin errors, warnings, info ni limitations;
- SHA-256 confirmado `4bfa28d24031853d5ec16ef6cae05b6aeaa6f346d4a653a0c56c85a7468b0ba5`;
- F2 declarada formalmente `CLOSED`;
- próximo gate: `F3 — Demand`, modalidad `COLLABORATIVE`.

### 2026-09-24 — v0.1.0

- F1 incorporada como checkpoint validado `aut46 PASS clean`;
- madurez caracterizada por arquitectura sin score agregado;
- A1 clasificada como arquitectura de mayor estandarización;
- A2 separada por menor comparabilidad gas-phase;
- HVAC tratado como maduro técnicamente pero dependiente de infraestructura;
- tecnologías electrónicas y UVGI mantenidas como familias condicionadas;
- PCO/plasma conservadas con madurez baja-media y mayor carga de evidencia;
- ozono intencional preservado como benchmark negativo;
- F3 identificado como próximo gate `COLLABORATIVE`.
