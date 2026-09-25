---
id: si-research-015
title: BRAND-CAND-003 — Method v2 Agile — F1 Market / Solution Map
description: Mapa de arquitecturas y soluciones comercialmente significativas para tratamiento doméstico del aire interior.
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
  - phase-1
---

# Smart Imports — BRAND-CAND-003 — Method v2 Agile
## F1 — Market / Solution Map

| Campo | Valor |
|---|---|
| Documento | `si-research-015` |
| Brand | `brand-hogar` |
| Brand Candidate | `BRAND-CAND-003 — Tratamiento doméstico del aire interior` |
| Fase | `F1 — Market / Solution Map` |
| Modalidad | `AUTO` |
| Fecha | `2026-09-24` |
| Estado | `CLOSED` |
| F0 checkpoint | `aut45 PASS clean` |
| Baseline matriz | `matrix-aut45-brand-cand-003-phase0.xlsx` |
| Matriz preparada | `matrix-aut46-brand-cand-003-phase1.xlsx` |
| Schema | `full-matrix-v5 0.7.0` |
| Validator | `Matrix Validator 0.1.0` |

---

## 1. Input vigente

F0 quedó formalmente validada sobre:

```text
matrix-aut45-brand-cand-003-phase0.xlsx
SHA-256: a4615e6b69f8e4c55cd3e7941c6e79bb04635567b16ab121ca269198cc40196e
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Pregunta de continuidad:

> ¿Qué arquitecturas domésticas de tratamiento del aire interior son comercialmente significativas y suficientemente diferentes como para merecer evaluación posterior, sin confundir tecnologías, componentes, atributos o claims con Product Bases?

F1 no evalúa todavía demanda local, competencia, origen, landed cost ni margen.

---

## 2. Principio de normalización

La unidad correcta del mapa no es la etiqueta comercial `air purifier` ni un componente aislado.

Se normaliza mediante:

```text
TARGET CONDITION / POLLUTANT
→ REAL TREATMENT MECHANISM
→ AIR HANDLING / DEPLOYMENT ARCHITECTURE
→ OBSERVABLE PERFORMANCE
→ OWNERSHIP / SERVICE CONSEQUENCES
```

Reglas:

```text
HEPA ≠ SOLUTION ARCHITECTURE
ACTIVATED CARBON ≠ VERIFIED GAS PERFORMANCE
UV ≠ VERIFIED MICROBIAL PERFORMANCE
IONIZATION ≠ VERIFIED PARTICLE PERFORMANCE
SMART / WIFI / APP ≠ SOLUTION ARCHITECTURE
SENSOR ≠ TREATMENT MECHANISM
```

Sensores, displays, conectividad, cantidad de velocidades, app, automatizaciones y estética pueden cambiar experiencia o service layer, pero no crean por sí solos una arquitectura distinta.

---

## 3. Ejes del mapa

### 3.1 Condición / contaminante objetivo

```text
P1 — partículas finas / humo
P2 — polvo / polen / partículas más grandes
G1 — gases / VOCs específicos
G2 — olores asociados a compuestos gaseosos
B1 — bioaerosoles / microorganismos, sólo cuando exista mecanismo y evidencia aplicable
```

No se presupone que una misma arquitectura trate eficazmente todos los grupos.

### 3.2 Mecanismo real

```text
M1 — filtración mecánica / medio fibroso
M2 — adsorción / quimisorción de gases
M3 — captura electrostática / electrónica de partículas
M4 — UVGI / inactivación microbiológica complementaria
M5 — reacción química / oxidación: PCO, plasma u otras variantes
M6 — generación intencional de ozono
```

### 3.3 Deployment / manejo del aire

```text
D1 — portátil / recirculación por ambiente
D2 — central / in-duct / HVAC
D3 — personal / near-field
```

`D3` se conserva como benchmark del mercado amplio, pero no se prioriza dentro del territorio actual porque su job principal no es necesariamente mejorar una condición del ambiente doméstico completo.

---

## 4. Arquitecturas comercialmente significativas

### A1 — Portátil de filtración mecánica de partículas

```text
Target: P1 / P2
Mechanism: M1
Deployment: D1
```

Descripción:

Equipo recirculante de ambiente cuyo mecanismo principal es forzar aire a través de medios filtrantes para capturar partículas. Puede utilizar HEPA u otros medios de alta eficiencia, pero la arquitectura se evalúa por desempeño completo del sistema.

Variables estructurales:

- CADR / airflow efectivo;
- tamaño de ambiente;
- ruido a velocidad útil;
- sellado y bypass;
- consumo;
- vida útil y costo del filtro;
- disponibilidad de repuestos.

Lectura F1:

> Arquitectura base claramente madura y medible para partículas; merece avanzar a F2.

---

### A2 — Portátil combinado: partículas + medio sorbente para gases/olores

```text
Target: P1 / P2 + G1 / G2
Mechanism: M1 + M2
Deployment: D1
```

Descripción:

Equipo portátil que combina captura de partículas con un medio sorbente o quimisorbente —por ejemplo carbón activado u otro material específico— para determinados gases u olores.

Diferencia material frente a A1:

- segundo mecanismo real;
- consumible/capacidad adicional;
- desempeño gas-phase específico y más difícil de comparar;
- mayor riesgo de claims genéricos no soportados;
- posible cambio en peso, presión, costo recurrente y service layer.

Regla:

> Una lámina nominal de carbón no alcanza para considerar que el sistema tenga capacidad significativa sobre gases.

Lectura F1:

> Arquitectura distinta y comercialmente relevante; merece avanzar a F2.

---

### A3 — Filtración central / HVAC de partículas

```text
Target: P1 / P2
Mechanism: M1
Deployment: D2
```

Descripción:

Medios filtrantes instalados en un sistema central de climatización/ventilación. El desempeño depende de eficiencia del filtro, compatibilidad con el sistema, presión, sellado y tiempo real de operación del ventilador HVAC.

Diferencias materiales frente a A1:

- depende de infraestructura instalada;
- puede servir múltiples ambientes;
- introduce instalación/compatibilidad;
- cambia logística y postventa;
- la operación del HVAC condiciona el tratamiento.

Lectura F1:

> Arquitectura real y diferenciada; avanzar a F2, pero con atención a su encaje práctico en viviendas objetivo y primera importación.

---

### A4 — Tratamiento central / HVAC combinado de partículas + gases

```text
Target: P1 / P2 + G1 / G2
Mechanism: M1 + M2
Deployment: D2
```

Descripción:

Configuración central que combina filtración particulada con medios adsorbentes/quimisorbentes.

Diferencias materiales:

- mayor exigencia de sizing y presión;
- masa/capacidad del sorbente;
- compatibilidad con HVAC;
- mantenimiento especializado;
- desempeño gas-phase no reducible a CADR.

Lectura F1:

> Arquitectura válida, aunque probablemente más compleja operacionalmente; mantener para F2 sin priorizarla todavía.

---

### A5 — Captura electrónica / electrostática de partículas

```text
Target: principalmente P1
Mechanism: M3
Deployment: D1 o D2
```

Incluye precipitadores electrostáticos, ionización con colección y otras implementaciones electrónicas donde el mecanismo principal depende de carga eléctrica de partículas.

Variables estructurales:

- CADR/remoción real;
- existencia o no de etapa colectora;
- limpieza/mantenimiento;
- emisiones de ozono;
- seguridad eléctrica;
- desempeño a lo largo del tiempo.

No normalizar como una sola promesa comercial a productos que sólo comparten la palabra `ion`.

Lectura F1:

> Arquitectura comercialmente existente, pero con carga de evidencia y seguridad mayor; avanzar a F2 como familia condicionada.

---

### A6 — Filtración + UVGI complementaria

```text
Target: partículas + objetivo microbiológico específico
Mechanism: M1 + M4
Deployment: D1 o D2
```

UVGI se trata como mecanismo complementario de inactivación y no como sustituto automático de la captura de partículas.

Variables estructurales:

- dosis/intensidad UV;
- tiempo de contacto;
- geometría del flujo;
- longitud de onda;
- exposición del usuario;
- emisión potencial de ozono según implementación;
- método de prueba microbiológico aplicable.

Lectura F1:

> Arquitectura diferenciada sólo cuando UVGI sea una función real y verificable del sistema. Avanza a F2 condicionada; no se asume beneficio microbiológico por presencia nominal de una lámpara.

---

### A7 — Tratamiento reactivo de gases: PCO / plasma / tecnologías afines

```text
Target: principalmente G1 / G2 y claims complementarios
Mechanism: M5
Deployment: D1 o D2
```

Descripción:

Familia de tecnologías que intenta transformar contaminantes mediante reacción química, fotocatálisis, plasma u otros procesos activos.

Riesgos estructurales:

- desempeño residencial difícil de verificar;
- claims amplios;
- productos de reacción/subproductos;
- posible generación de ozono;
- necesidad de evidencia de implementación concreta, no sólo del principio físico.

Lectura F1:

> Mantener en el mapa por existencia comercial, pero con prioridad baja para profundización salvo evidencia convincente en F2/F5. No se interpreta sofisticación tecnológica como ventaja.

---

### A8 — Generación intencional de ozono

```text
Target declarado: gases / olores / biológicos
Mechanism: M6
Deployment: D1 o D2
```

Tratamiento F1:

```text
NEGATIVE BENCHMARK
NOT NORMAL CANDIDATE FOR OCCUPIED RESIDENTIAL USE
```

La EPA recomienda no usar generadores de ozono en espacios ocupados. CARB regula específicamente las emisiones de ozono de dispositivos de limpieza de aire y diferencia los equipos intencionalmente productores de ozono para usos particulares/no ocupados.

Lectura:

> No avanzar como arquitectura comercial normal de Marca Hogar para uso cotidiano en espacios ocupados. Se conserva sólo para evitar que un futuro sourcing la reintroduzca como supuesto diferenciador.

---

## 5. Soluciones adyacentes que NO se convierten en Product Base de este candidato

### Source control / control de fuente

Eliminar o reducir la fuente del contaminante puede ser más efectivo que tratar continuamente el aire. Es una condición de contexto, no una arquitectura importable de este candidato por sí misma.

### Ventilación

La ventilación con aire exterior limpio es parte de la estrategia general de calidad de aire. No se absorbe automáticamente dentro de `BRAND-CAND-003` porque puede constituir otra solución/infraestructura con economics e instalación propios.

### Aromatización / difusión

Perfumar, humidificar o generar una experiencia sensorial no equivale a remover o reducir contaminantes. Permanece fuera del territorio salvo que exista una función de tratamiento ambiental verificable independiente.

### Sensores standalone

Un monitor de PM2.5/VOC/CO2 mide una condición; no la trata. Puede convertirse en componente o en otro Brand Candidate, pero no se transforma en Product Base de tratamiento sólo por estar asociado a un purificador.

---

## 6. Aprendizaje estructural de F1

La arquitectura del candidato puede expresarse como:

```text
SOLUTION ARCHITECTURE
=
TARGET CONDITION / POLLUTANT
+
TREATMENT MECHANISM
+
AIR HANDLING / DEPLOYMENT
+
OWNERSHIP / SERVICE CONSEQUENCES
```

El desempeño observable se evalúa después sobre esa arquitectura.

Esto evita dos errores:

```text
TECHNOLOGY LABEL → PRODUCT BASE
FEATURE BUNDLE → PRODUCT BASE
```

La frontera de Product Base se resolverá formalmente en F6, no en F1.

---

## 7. Métricas y evidencia que F2–F6 deberán preservar

### Para partículas

- CADR cuando corresponda;
- airflow;
- eficiencia por tamaño de partícula / HEPA / MERV según contexto;
- room size y supuestos de altura/ACH;
- desempeño a velocidad de uso real.

### Para gases / olores

- contaminante objetivo específico;
- tipo y masa/capacidad del sorbente;
- tiempo de breakthrough / vida útil cuando exista;
- caudal y tiempo de contacto;
- condiciones de humedad/temperatura;
- método de prueba específico.

### Para tecnologías activas

- mecanismo implementado;
- desempeño del equipo completo;
- subproductos;
- ozono;
- seguridad eléctrica/UV;
- método de prueba aplicable;
- certificaciones pertinentes.

---

## 8. Gate F1

### Pregunta de gate

> ¿Existe un mapa suficientemente discriminante de arquitecturas comerciales como para pasar a evaluar madurez, sin convertir prematuramente tecnologías o features en Product Bases?

Resultado conceptual:

```text
PASS
```

Razón:

- se identificaron mecanismos principales;
- se separó portable vs. central/HVAC;
- se distinguió partículas vs. gases;
- se aislaron tecnologías activas de mayor riesgo;
- se preservó UVGI como complemento condicionado;
- se dejó ozono intencional como benchmark negativo;
- sensores, app y conectividad no se confundieron con arquitecturas;
- no se requiere investigación adicional para abrir F2.

---

## 9. Materialización en matriz vigente

`full-matrix-v5 0.7.0` no tiene una entidad nativa `Solution Architecture`.

No se modifica el schema.

No se crean:

- Product Bases prematuros;
- Evaluaciones de criterios aún no ejecutados;
- Evidencias con criterio artificial;
- Fuentes globales activas huérfanas.

La materialización de F1 se hace mediante el `MATRIX_SCOPE_ALIAS` existente (`Nicho ID 33`):

- `Documento Research` apunta a `si-research-015`;
- `Proxima Accion` queda preparada para F2 después del validator;
- `Notas` registra el cierre validado de F0, el resultado conceptual de F1 y la fricción de schema para Matrix vNext.

Archivo:

```text
matrix-aut46-brand-cand-003-phase1.xlsx
```

SHA-256 previo al validator local:

```text
0b3a85792a8db5c60af4e75c22e69bd29b868e6628c1b8798b9954b45737cce5
```

---

## 10. Estado formal

```text
F0 — CLOSED
F1 — CLOSED
```

Validación oficial de F1:

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: 0b3a85792a8db5c60af4e75c22e69bd29b868e6628c1b8798b9954b45737cce5
```

Continuidad:

```text
F1 CLOSED
→ F2 — Maturity
→ AUTO
```

No apareció una acción `COLLABORATIVE` o `EXTERNAL` durante F1.

---

## 11. Fuentes públicas — Minimum Sufficient Evidence

1. Smart Imports — `BRAND-CAND-003 — Tratamiento doméstico del aire interior`  
   https://github.com/agelormini2024/smart-imports/blob/main/docs/07-brand/brands/brand-hogar/candidates/brand-cand-003-domestic-air-treatment.md

2. U.S. EPA — *Guide to Air Cleaners in the Home*  
   https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home

3. U.S. EPA — *Air Cleaners and Air Filters in the Home*  
   https://www.epa.gov/indoor-air-quality-iaq/air-cleaners-and-air-filters-home

4. U.S. EPA — *Residential Air Cleaners — A Technical Summary, 3rd Edition*  
   https://www.epa.gov/sites/default/files/2018-07/documents/residential_air_cleaners_-_a_technical_summary_3rd_edition.pdf

5. ASHRAE Handbook — *Air Cleaners for Particulate Contaminants*  
   https://handbook.ashrae.org/Handbooks/S24/IP/s24_ch29/s24_ch29_ip.aspx

6. AHAM Verifide — *Air Filtration Standards*  
   https://ahamverifide.org/ahams-air-filtration-standards/

7. California Air Resources Board — *Regulation for Limiting Ozone Emissions from Air Cleaning Devices*  
   https://ww2.arb.ca.gov/resources/documents/indoor-air-cleaning-devices-regulation

---

## 12. Changelog

### 2026-09-24 — v0.1.0

- se cierra conceptualmente F1;
- se normaliza el mapa por contaminante + mecanismo + deployment;
- se identifican ocho familias/benchmarks relevantes;
- se separan arquitecturas de features y claims;
- se registra ozono intencional como benchmark negativo;
- se preservan tecnologías activas como familias condicionadas, no descartadas por sofisticación;
- se prepara `aut46` sin modificar schema;
- `aut46` validada con PASS limpio; F1 queda formalmente `CLOSED`; siguiente fase: `F2 — Maturity` en AUTO.
