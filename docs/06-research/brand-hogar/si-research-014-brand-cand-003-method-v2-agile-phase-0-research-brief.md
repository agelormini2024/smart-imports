---
id: si-research-014
title: BRAND-CAND-003 — Method v2 Agile — F0 Research Brief
description: Research Brief y límites de investigación para tratamiento doméstico del aire interior.
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
  - phase-0
---

# Smart Imports — BRAND-CAND-003 — Method v2 Agile
## F0 — Research Brief

| Campo | Valor |
|---|---|
| Documento | `si-research-014` |
| Brand | `brand-hogar` |
| Brand Candidate | `BRAND-CAND-003 — Tratamiento doméstico del aire interior` |
| Fase | `F0 — Research Brief` |
| Modalidad | `AUTO` |
| Fecha | `2026-09-24` |
| Estado | `CLOSED` |
| Baseline documental | `5b79cd6 — docs(method-v2): close BRAND-CAND-001 phase 13 shortlist` |
| Baseline matriz | `matrix-aut44-brand-cand-001-phase13-corrected.xlsx` |
| Schema | `full-matrix-v5 0.7.0` |
| Validator | `Matrix Validator 0.1.0` |

---

## 1. Objetivo

Abrir la ejecución ágil de Method v2 para `BRAND-CAND-003` sin partir de un dispositivo, una tecnología, una marca ni una publicación determinada.

Definición de solución vigente:

> Tratamiento doméstico del aire interior orientado a mejorar de manera verificable determinadas características de su calidad.

F0 debe establecer una pregunta de investigación, límites, hipótesis estructurales y ejes de observación suficientes para que F1 pueda construir el mapa de mercado sin convertir tecnologías o claims en Product Bases prematuramente.

No corresponde todavía evaluar demanda, competencia, origen, costos, margen ni decidir qué importar.

---

## 2. Pregunta central de investigación

> **¿Qué arquitecturas domésticas de tratamiento del aire interior permiten mejorar de forma verificable una o más condiciones concretas del aire —partículas y/o gases/olores y, sólo cuando corresponda, contaminantes biológicos— con desempeño observable, seguridad, mantenimiento y experiencia de uso suficientemente defendibles para construir una propuesta de Marca Hogar?**

La pregunta obliga a separar:

```text
CONTAMINANTE / CONDICIÓN OBJETIVO
→ MECANISMO REAL
→ CAPACIDAD DEL SISTEMA
→ OUTPUT OBSERVABLE
→ OUTCOME
→ CLAIM COMERCIAL
```

y evita comenzar desde etiquetas comerciales como:

```text
purificador
HEPA
ionizador
UV
plasma
smart
air quality
```

---

## 3. Alcance de F0

### Dentro del alcance

- tratamiento doméstico de partículas suspendidas;
- tratamiento de humo, polvo y polen como problemas de partículas;
- tratamiento de gases, VOCs y olores cuando exista un mecanismo materialmente apto;
- arquitecturas portátiles de ambiente;
- arquitecturas integradas a climatización / HVAC cuando sean comercialmente significativas;
- tecnologías activas o electrónicas sólo como hipótesis a investigar, no como beneficio asumido;
- consumibles, mantenimiento y reposición cuando sean parte estructural de la solución;
- métricas de desempeño, método de prueba, seguridad y subproductos;
- condiciones necesarias para una comunicación comercial defendible.

### Fuera del alcance o no asumido

- aromatizadores, difusores o productos cuyo job principal sea perfumar;
- wellness genérico;
- claims terapéuticos o de salud sin soporte específico;
- asumir que `HEPA`, `UV`, `ionización`, `plasma`, `fotocatálisis` o una app implican por sí mismos un resultado;
- convertir sensores o conectividad en Product Base si no cambian materialmente el job, service layer o arquitectura;
- asumir que una arquitectura resuelve simultáneamente partículas, gases y contaminantes biológicos;
- usar F0 para concluir demanda, competencia o viabilidad económica.

---

## 4. Minimum Sufficient Evidence usado en F0

F0 utiliza evidencia pública técnica únicamente para estructurar correctamente el problema. No constituye validación comercial local ni evidencia positiva de desempeño de ningún SKU.

### 4.1 Partículas y gases son problemas técnicamente distintos

La EPA distingue contaminantes interiores particulados y gaseosos. También señala que muchos equipos están diseñados para partículas **o** gases; cuando se pretende tratar ambos, normalmente se requieren mecanismos diferenciados.

Implicación para Method v2:

> `particle treatment` y `gas / odor treatment` no deben fusionarse por una etiqueta comercial “all-in-one” sin verificar el mecanismo real.

### 4.2 Desempeño del sistema ≠ especificación de un componente

Para partículas, el CADR permite relacionar entrega de aire limpio con tamaño de ambiente. Un filtro de alta eficiencia puede contribuir al resultado, pero el desempeño real también depende del caudal, velocidad de operación, tiempo de uso, sellado, diseño y dimensionamiento.

Implicación:

> `HEPA component specification ≠ complete-system performance`.

### 4.3 El tratamiento de gases requiere otra lógica de evidencia

La EPA indica que el CADR se aplica a partículas y que no existe un sistema de rating de uso amplio equivalente para remoción de gases. Los medios adsorbentes, como carbón activado, dependen entre otras cosas de la cantidad de material disponible.

Implicación:

> una futura comparación de arquitecturas para gases/olores deberá exigir contaminante objetivo, medio real, masa/capacidad cuando esté disponible, condiciones y método de prueba; no basta “filtro de carbón”.

### 4.4 Tecnologías activas requieren análisis de seguridad y subproductos

Ionización, precipitadores electrostáticos, determinadas implementaciones UV, plasma y otras tecnologías activas pueden introducir una dimensión de emisión de ozono o subproductos. La regulación CARB trata específicamente las emisiones de ozono de dispositivos de limpieza de aire.

Implicación:

> tecnología activa no implica exclusión automática, pero sí una carga de evidencia y seguridad mayor.

### 4.5 Mantenimiento y consumibles son parte de la arquitectura comercial

Los filtros requieren reemplazo periódico; saturación, mantenimiento y disponibilidad de consumibles afectan funcionamiento y experiencia de propiedad.

Implicación:

> vida útil, costo, disponibilidad y facilidad de reposición deben observarse como dimensiones estructurales desde F1/F6 y no recién en landed cost.

---

## 5. Hipótesis estructurales para contrastar en F1

### H1 — La arquitectura debe nacer del contaminante y del mecanismo

La normalización inicial debe ordenar soluciones por:

```text
target condition / pollutant
→ treatment mechanism
→ air-delivery / deployment architecture
→ observable performance
```

y no por marketing label.

### H2 — Filtración mecánica de partículas constituye una familia de solución, no una Product Base todavía

Es esperable encontrar soluciones con medios fibrosos de distinta eficiencia, incluidos sistemas que declaran HEPA. F1 debe mapearlas sin asumir que el medio filtrante determina el desempeño total.

### H3 — Partículas + gases/olores puede constituir una arquitectura materialmente distinta

Una solución que combine filtración de partículas con un medio sorbente significativo puede tener capacidad, costo recurrente, peso, service layer y claims distintos de una solución orientada sólo a partículas.

### H4 — Las tecnologías activas/electrónicas forman un espacio de solución con riesgo técnico propio

Ionización, ESP, UVGI, plasma, PCO u otras tecnologías deberán descomponerse en mecanismo, objetivo, desempeño verificable, subproductos y seguridad. No se tratarán como diferenciadores positivos por defecto.

### H5 — Portable single-room e in-duct / HVAC pueden constituir arquitecturas distintas

Aunque compartan un medio filtrante, cambian instalación, dimensionamiento, dependencia de infraestructura, logística, servicio y experiencia de propiedad.

### H6 — Consumibles y mantenimiento pueden cambiar la configuración comercial

Frecuencia de reemplazo, costo recurrente, disponibilidad y facilidad de reposición pueden justificar separaciones posteriores entre Product Bases si modifican materialmente ownership o postventa.

### H7 — Sensores y conectividad son secundarios salvo que modifiquen el job o service layer

`PM2.5 display`, sensores, Wi‑Fi o app no se convertirán en arquitectura ni Product Base por sí solos. Su valor dependerá de precisión, accionabilidad y relación con el funcionamiento real.

### H8 — “All-in-one” debe descomponerse

Una publicación que enumere HEPA + carbón + UV + ionización + sensor no constituye una arquitectura válida hasta separar cada mecanismo, qué condición intenta tratar, qué evidencia existe y qué riesgos introduce.

---

## 6. Ejes de investigación para F1 — Mapa

F1 deberá construir un mapa suficiente para decidir qué familias merecen avanzar, usando al menos estos ejes:

| Eje | Pregunta |
|---|---|
| Condición objetivo | ¿Partículas, humo, polvo, polen, gases/VOCs, olores, biológicos u otra? |
| Mecanismo | ¿Filtración fibrosa, adsorción, electrostática, ionización, UVGI, PCO, plasma u otro? |
| Deployment | ¿Portátil por ambiente, integrado a HVAC, otra configuración doméstica materialmente distinta? |
| Output observable | ¿CADR, airflow, eficiencia por tamaño de partícula, MERV, reducción específica de gas, otro método? |
| Dimensionamiento | ¿Qué relación explícita existe entre capacidad y volumen/superficie del ambiente? |
| Seguridad | ¿Ozono, subproductos, exposición UV, alta tensión u otra dimensión? |
| Ruido / energía | ¿El desempeño útil exige una velocidad o régimen de uso que afecte experiencia y consumo? |
| Ownership | ¿Qué consumibles existen, cuánto duran y cómo se reemplazan? |
| Service layer | ¿Instalación, mantenimiento, calibración, soporte o reposición especializada? |
| Claim defensible | ¿Qué puede afirmarse realmente según mecanismo, medición y método de prueba? |

F1 no necesita agotar todas las tecnologías existentes. Aplicará `MINIMUM SUFFICIENT EVIDENCE`: profundidad suficiente para distinguir las arquitecturas comercialmente significativas y descartar ruido conceptual.

---

## 7. Reglas de claims y evidencia que quedan activas

Durante todo el candidato:

```text
DECLARED ATTRIBUTE / COMMERCIAL LABEL
≠ REAL MECHANISM
≠ SYSTEM CAPABILITY
≠ OBSERVABLE OUTPUT
≠ OUTCOME
≠ COMMERCIAL CLAIM
```

En particular:

- `HEPA` no prueba por sí solo CADR ni desempeño del sistema;
- `activated carbon` no prueba por sí solo capacidad relevante para gases;
- `sensor PM2.5` no prueba precisión ni eficacia de tratamiento;
- `UV`, `ion`, `plasma` o `PCO` no prueban eficacia ni seguridad por la mera presencia del componente;
- certificación o eficiencia energética no debe reinterpretarse como certificación de eficacia de purificación;
- evitar `aire saludable`, `elimina toxinas`, beneficios médicos o microbiológicos genéricos salvo evidencia y soporte regulatorio específicos.

---

## 8. Materialización prevista en la matriz vigente

La matriz `aut44` usa el modelo legacy `Nicho → Product Base`. Siguiendo el patrón validado en la Golden Run de `BRAND-CAND-001`, F0 se materializa creando sólo un `MATRIX_SCOPE_ALIAS` para `BRAND-CAND-003` en `Nichos`.

Nueva fila preparada:

```text
ID: 33
Nicho: Marca Hogar — tratamiento doméstico del aire interior
Estado: En evaluación
```

`Proxima Accion`:

> Ejecutar Fase 1 — mapa de mercado / soluciones en AUTO; normalizar arquitecturas sin convertir tecnologías o claims en Product Bases prematuramente.

No se crean todavía:

- Product Bases;
- Evaluaciones;
- Evidencias artificiales con un criterio inexistente;
- Fuentes Externas huérfanas sólo para registrar bibliografía de F0.

Las fuentes públicas de este Research Brief sirven como baseline conceptual/técnico. La evidencia comercial se incorporará cuando exista un criterio y una fase que la requiera.

Archivo preparado:

```text
matrix-aut45-brand-cand-003-phase0.xlsx
```

---

## 9. Gate de F0

### Análisis conceptual

```text
PASS
```

Existe definición suficiente de:

- pregunta central;
- scope;
- no-scope;
- hipótesis estructurales;
- ejes de F1;
- disciplina de claims;
- tratamiento de riesgo técnico.

No existe una incertidumbre F0 que justifique investigación adicional antes de construir el mapa.

### Estado formal de la fase

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut45
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F0 CLOSED
```

Validación oficial:

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: a4615e6b69f8e4c55cd3e7941c6e79bb04635567b16ab121ca269198cc40196e
```

Por disciplina de cierre de Method v2, **F1 no se declara formalmente abierta hasta obtener `PASS` limpio del Matrix Validator y completar el checkpoint documental**.

---

## 10. Próxima acción

F0 queda `CLOSED`. El siguiente gate es `F1 — Market / Solution Map`, ejecutado en `AUTO` con `MINIMUM SUFFICIENT EVIDENCE`.

---

## 11. Fuentes públicas utilizadas para el baseline técnico de F0

1. Smart Imports — `BRAND-CAND-003 — Tratamiento doméstico del aire interior`  
   https://github.com/agelormini2024/smart-imports/blob/main/docs/07-brand/brands/brand-hogar/candidates/brand-cand-003-domestic-air-treatment.md

2. U.S. EPA — *Guide to Air Cleaners in the Home*  
   https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home

3. U.S. EPA — *Residential Air Cleaners — A Technical Summary, 3rd Edition*  
   https://www.epa.gov/sites/default/files/2018-07/documents/residential_air_cleaners_-_a_technical_summary_3rd_edition.pdf

4. AHAM Verifide — *Find a Certified Room Air Cleaner*  
   https://ahamverifide.org/directory-of-air-cleaners/

5. California Air Resources Board — *Regulation for Limiting Ozone Emissions from Air Cleaning Devices*  
   https://ww2.arb.ca.gov/resources/documents/indoor-air-cleaning-devices-regulation

---

## 12. Changelog

### 2026-09-24 — v0.1.0

- se abre `BRAND-CAND-003` en ejecución ágil;
- se completa análisis conceptual de F0;
- se define la pregunta central y los límites de investigación;
- se establecen ocho hipótesis estructurales para F1;
- se formaliza la separación entre contaminante, mecanismo, capacidad, output y claim;
- se prepara `MATRIX_SCOPE_ALIAS` en `aut45`;
- `aut45` validada con PASS limpio;
- F0 queda formalmente `CLOSED`;
- siguiente fase: `F1 — Market / Solution Map` en AUTO.
