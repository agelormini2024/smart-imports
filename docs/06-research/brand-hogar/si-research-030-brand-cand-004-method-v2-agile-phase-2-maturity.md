---
id: si-research-030
title: BRAND-CAND-004 — Method v2 Agile — F2 Maturity
description: Evaluación de madurez técnica y operativa de las arquitecturas de monitoreo doméstico del consumo energético.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-25
updated: 2026-09-25
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-004
  - energy-monitoring
  - phase-2
related:
  - si-research-028
  - si-research-029
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F2 Maturity

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input vigente

F1 quedó formalmente cerrada sobre:

```text
matrix-aut60-brand-cand-004-phase1.xlsx
SHA-256: 45a4709794501bf3e5582939dd4cc95ee4682b1aad389bc853a788a905c0ebc1
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Arquitecturas evaluadas:

```text
A1 — Plug-level direct metering
A2 — Panel / DIN-rail direct submetering
A3 — Multi-circuit CT monitoring
A4 — Whole-home aggregate CT monitoring
A5 — Aggregate measurement + NILM / disaggregation
A6 — Smart-meter / utility-data integration
```

F2 evalúa **madurez técnica y operativa**. No evalúa todavía demanda local, competencia, potencial de marca, origen, landed cost, margen ni selección de Product Bases.

## 2. Criterio de madurez

La madurez no se interpreta como popularidad ni como conveniencia comercial automática.

Se observa:

```text
MEASUREMENT PRINCIPLE MATURITY
+ MEASUREMENT / ACCURACY VERIFIABILITY
+ HARDWARE / INSTALLATION MATURITY
+ DATA CONTINUITY
+ EXTERNAL DEPENDENCIES
+ SERVICE / SUPPORT BURDEN
+ CLAIM DISCIPLINE
```

Reglas activas:

```text
TECHNICALLY MATURE ≠ GOOD FIRST PRODUCT
MEASUREMENT AVAILABLE ≠ MEASUREMENT ACCURATE
CURRENT SENSOR ≠ VALIDATED POWER / ENERGY METER
AGGREGATE DATA ≠ APPLIANCE TRUTH
NILM MATURITY ≠ DIRECT-METER EQUIVALENCE
UTILITY DATA AVAILABLE SOMEWHERE ≠ LOCALLY AVAILABLE / ACCESSIBLE
```

## 3. Baseline técnico suficiente

### 3.1 La medición residencial directa es una categoría establecida

ENERGY STAR reconoce explícitamente dispositivos `Plug Load Monitor/Control` capaces de reportar potencia o energía, incluyendo smart plugs, smart power strips y home energy monitors.

NIST documentó un proyecto específico para evaluar sistemas comerciales de monitoreo energético residencial y desarrollar métodos para cuantificar exactitud de medición y desempeño de comunicaciones.

Lectura:

> La existencia de productos comerciales y de marcos de evaluación metrológica indica alta madurez del principio de medición directa; la calidad de implementación sigue siendo SKU-specific.

### 3.2 La exactitud sigue siendo una propiedad a verificar

NIST mantiene servicios y proyectos de metrología para watt, watt-hour y smart meters, y ha demostrado que las condiciones de carga y forma de onda pueden afectar el error de medición de implementaciones concretas.

Lectura:

> `meter exists` no autoriza un claim de precisión. Rango, método, carga, tensión, factor de potencia y condiciones de prueba siguen siendo parte de la evidencia.

### 3.3 AMI / utility data es una infraestructura madura pero externamente dependiente

EIA documenta AMI residencial a gran escala y datos de consumo por intervalos. DOE Green Button permite intercambio de datos de uso, pero la granularidad y forma de acceso dependen de cada utility.

Lectura:

> La arquitectura es técnicamente madura donde existe infraestructura compatible, pero su viabilidad comercial no es portable entre mercados sin revisar acceso local, API/protocolo, permisos y granularidad.

### 3.4 NILM tiene una base de investigación madura, pero no equivalencia con submedición

Las revisiones recientes describen décadas de evolución de NILM y un campo técnicamente maduro en investigación. Sin embargo, siguen señalando desafíos de generalización, evaluación comparativa, datos, interpretabilidad y desempeño real-time.

Lectura:

> NILM puede ser comercialmente relevante, pero su madurez para claims de appliance-level accuracy es menor y más condicionada que la medición directa.

## 4. Evaluación por arquitectura

### A1 — Plug-level direct metering

```text
MATURITY: HIGH
```

Razones:

- principio de medición directa ampliamente establecido;
- instalación simple y boundary claro;
- atribución directa a una carga enchufable;
- potencia y energía son outputs verificables en equipos adecuados;
- categoría reconocida en ecosistemas de gestión energética doméstica.

Riesgos residuales:

- precisión real del SKU;
- cargas inductivas/no lineales;
- tensión/corriente/potencia máxima;
- formato de enchufe y seguridad;
- cloud obligatorio y continuidad de datos;
- relay/control no debe confundirse con medición.

Lectura F2:

> Alta madurez técnica y operativa. Buen candidato para estudiar demanda en F3, sin asumir todavía brand fit ni economía.

### A2 — Panel / DIN-rail direct submetering

```text
MATURITY: HIGH — TECHNICAL / INSTALLATION-SENSITIVE
```

Razones:

- metering/submetering es tecnología establecida;
- boundary por circuito/feeder claro;
- puede medir cargas fijas que A1 no cubre;
- outputs de potencia/energía son directamente atribuibles al punto medido.

Carga adicional:

- instalación dentro del tablero;
- tensión/fases;
- protecciones;
- espacio físico;
- certificaciones y seguridad;
- potencial necesidad de electricista.

Lectura F2:

> Alta madurez técnica, pero con mayor fricción de instalación y postventa. `HIGH maturity` no implica necesariamente buen primer producto.

### A3 — Multi-circuit CT monitoring

```text
MATURITY: HIGH — TECHNICAL / SERVICE-SENSITIVE
```

Razones:

- CTs y medición por canal son principios ampliamente establecidos;
- permite granularidad por circuito;
- hardware multi-canal comercialmente viable;
- puede ofrecer fuerte accionabilidad si el mapeo circuito↔sensor se mantiene correcto.

Riesgos residuales:

- instalación y orientación de CTs;
- referencia de tensión/fase;
- error acumulado del sistema;
- espacio en tablero;
- configuración y onboarding;
- soporte cuando el usuario identifica incorrectamente circuitos.

Lectura F2:

> Alta madurez técnica; complejidad de instalación/configuración mayor que A1 y con service burden relevante.

### A4 — Whole-home aggregate CT monitoring

```text
MATURITY: HIGH — TECHNICAL / AGGREGATE-ONLY
```

Razones:

- arquitectura de pocos sensores;
- medición total del hogar tecnológicamente establecida;
- puede entregar series temporales continuas;
- instalación más contenida que multi-circuit cuando el objetivo es consumo total.

Condición:

```text
AGGREGATE MEASUREMENT
≠
DIRECT APPLIANCE ATTRIBUTION
```

Lectura F2:

> Alta madurez para totalización/monitoring agregado. Cualquier claim por aparato pertenece a A5 y debe evaluarse separadamente.

### A5 — Aggregate measurement + NILM / disaggregation

```text
MATURITY: MEDIUM — INFERENCE-CONDITIONED
```

Fortalezas:

- campo de investigación maduro;
- amplio desarrollo de algoritmos, datasets y machine learning;
- evita instrumentar cada carga;
- puede enriquecer el valor del dato agregado.

Limitaciones estructurales todavía relevantes:

- generalización entre hogares;
- cargas multiestado o variables;
- nuevos aparatos;
- calidad/tasa de muestreo del input;
- necesidad de entrenamiento/calibración;
- comparabilidad de métricas;
- interpretabilidad y real-time deployment;
- diferencia entre detectar estado y medir energía por aparato.

Lectura F2:

> Madurez intermedia para una promesa comercial fuerte. Mantener como arquitectura condicionada y no usarla como sustituto conceptual de submedición directa.

### A6 — Smart-meter / utility-data integration

```text
MATURITY: MEDIUM-HIGH — INFRASTRUCTURE-DEPENDENT
```

Fortalezas:

- AMI y datos intervalados son infraestructura madura en múltiples mercados;
- existen estándares y mecanismos de intercambio como Green Button;
- evita instalar hardware de medición adicional cuando el dato ya existe.

Dependencias:

- disponibilidad local de smart meter;
- resolución temporal;
- API/portal/protocolo;
- permiso del usuario;
- acceso de terceros;
- continuidad del servicio;
- utility lock-in;
- diferencias jurisdiccionales.

Lectura F2:

> Tecnología de infraestructura madura, pero producto comercial dependiente de terceros. Su madurez operativa para Smart Imports debe calificarse por mercado y no extrapolarse.

## 5. Matriz comparativa de madurez

| Arquitectura | Madurez | Principal fortaleza | Principal condición |
|---|---|---|---|
| A1 Plug-level direct | `HIGH` | Boundary y atribución directos | precisión/SKU + seguridad/plug |
| A2 Panel/DIN direct | `HIGH — TECHNICAL` | Submedición directa estable | instalación/tablero |
| A3 Multi-circuit CT | `HIGH — TECHNICAL` | Granularidad por circuito | instalación/configuración/service |
| A4 Whole-home CT | `HIGH — TECHNICAL` | Cobertura total con pocos sensores | dato agregado, no appliance truth |
| A5 NILM | `MEDIUM` | Insight por aparato sin sensor dedicado | inferencia/generalización |
| A6 Utility data | `MEDIUM-HIGH` | Aprovecha infraestructura existente | dependencia utility/local |

## 6. Implicación para primeras etapas de importación

F2 no elimina arquitecturas exclusivamente por complejidad. Sí registra que el sesgo de primera etapa favorece:

- instalación simple;
- seguridad manejable;
- baja dependencia de infraestructura externa;
- medición que pueda demostrarse sin una capa inferencial fuerte;
- soporte y onboarding razonables;
- claim fácil de explicar y verificar.

Bajo ese sesgo:

```text
A1
→ structurally simple for first-stage evaluation

A2 / A3 / A4
→ technically mature but installation-sensitive

A5
→ evidence-heavy inference layer

A6
→ externally dependent
```

Esto **no es todavía shortlist**. La frontera comercial se evaluará después de demanda, competencia, potencial de marca y definición de Product Bases.

## 7. Gate F2

Pregunta:

> ¿Las arquitecturas mapeadas tienen madurez suficientemente entendida como para iniciar demanda local sin confundir madurez técnica con atractivo comercial?

Resultado conceptual:

```text
PASS
```

Razón:

- A1–A4 tienen principios de medición maduros y riesgos operativos identificables;
- A5 queda correctamente separada como inferencia con madurez condicionada;
- A6 queda separada como infraestructura externa dependiente;
- precisión, instalación, continuidad y service burden quedan incorporados como ejes;
- no existe una incertidumbre técnica F2 que justifique ampliar investigación antes de F3.

## 8. Materialización en matriz

Baseline validada:

```text
matrix-aut60-brand-cand-004-phase1.xlsx
SHA-256: 45a4709794501bf3e5582939dd4cc95ee4682b1aad389bc853a788a905c0ebc1
Result: PASS
```

F2 mantiene `MATRIX_SCOPE_ALIAS` ID 34 y actualiza:

- F1 a `CLOSED`;
- madurez por arquitectura;
- próxima acción `F3 — Demand`;
- ruta documental `SI-RESEARCH-030`;
- estado F2 pendiente de Matrix Validator.

Archivo preparado:

```text
matrix-aut61-brand-cand-004-phase2.xlsx
SHA-256: c693140851f0d5df25e741fe8cf60ba84d3440fe4efde478f4c952b2917c60d3
```

## 9. Estado formal de F2

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut61
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F2 CLOSED
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
SHA-256: c693140851f0d5df25e741fe8cf60ba84d3440fe4efde478f4c952b2917c60d3
```

F3 queda formalmente abierta después de este cierre.

## 10. Próxima acción

F2 queda `CLOSED`. Abrir `F3 — Demand` en modalidad `COLLABORATIVE` para recolectar evidencia local de Mercado Libre y clasificarla sin confundir oferta con demanda.

## 11. Fuentes públicas utilizadas

1. ENERGY STAR — *Smart Home Energy Management Systems Key Product Criteria*  
   https://www.energystar.gov/products/shems_key_product_criteria

2. NIST — *Energy Measurements for Existing Residential Buildings Project*  
   https://www.nist.gov/programs-projects/energy-measurements-existing-residential-buildings-project

3. NIST — *Power and Energy Measurements Low Frequency Calibrations*  
   https://www.nist.gov/calibrations/power-and-energy-measurements-low-frequency-calibrations

4. NIST — *Advanced Metering in Smart Distribution Grids*  
   https://www.nist.gov/programs-projects/advanced-metering-smart-distribution-grids

5. NIST — *A NIST Testbed for Examining the Accuracy of Smart Meters under High Harmonic Waveform Loads*  
   https://www.nist.gov/publications/nist-testbed-examining-accuracy-smart-meters-under-high-harmonic-waveform-loads

6. U.S. Energy Information Administration — *An Assessment of Interval Data and Their Potential Application to Residential Electricity End-Use Modeling*  
   https://www.eia.gov/consumption/residential/reports/smartmetering/

7. U.S. Department of Energy — *Green Button*  
   https://www.energy.gov/data/green-button

8. Dash, S.; Sahoo, N.C. — *Electric energy disaggregation via non-intrusive load monitoring: A state-of-the-art systematic review*  
   https://www.sciencedirect.com/science/article/pii/S0378779622007398

9. Rafiq, H. et al. — *A review of current methods and challenges of advanced deep learning-based non-intrusive load monitoring (NILM) in residential context*  
   https://www.sciencedirect.com/science/article/pii/S0378778824000069

## 12. Changelog

### 2026-09-25 — v0.1.0

- F1 queda formalmente cerrada sobre `aut60 PASS`;
- se evalúa madurez técnica y operativa de A1–A6;
- A1 se clasifica `HIGH`;
- A2–A4 se clasifican `HIGH — TECHNICAL` con condiciones de instalación/service;
- A5 se clasifica `MEDIUM — INFERENCE-CONDITIONED`;
- A6 se clasifica `MEDIUM-HIGH — INFRASTRUCTURE-DEPENDENT`;
- se materializa `matrix-aut61-brand-cand-004-phase2.xlsx`;
- `aut61` obtiene PASS limpio y F2 queda formalmente `CLOSED`;
- siguiente fase: `F3 — Demand` en modalidad `COLLABORATIVE`.
