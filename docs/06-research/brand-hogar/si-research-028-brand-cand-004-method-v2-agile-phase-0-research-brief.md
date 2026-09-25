---
id: si-research-028
title: BRAND-CAND-004 — Method v2 Agile — F0 Research Brief
description: Apertura conceptual de Method v2 Agile para monitoreo doméstico del consumo energético.
version: 0.2.0
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
  - phase-0
related:
  - si-research-027
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F0 Research Brief

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input vigente

`BRAND-CAND-004 — Monitoreo doméstico del consumo energético` entra a Method v2 desde el Brand System como candidato `CORE`, ya admitido a profundización comercial.

Riesgos abiertos heredados del screening:

```text
MEASUREMENT ACCURACY
ACTIONABILITY
COMMERCIAL CLAIM
```

Input de negocio:

```text
docs/07-brand/brands/brand-hogar/candidates/brand-cand-004-domestic-energy-monitoring.md
```

F0 no evalúa todavía demanda local, competencia, origen, costos, margen ni decide qué importar.

Tampoco asume que medir consumo produzca ahorro por sí mismo.

## 2. Pregunta central de investigación

> **¿Qué arquitecturas domésticas de monitoreo del consumo eléctrico permiten medir de forma verificable uno o más niveles de consumo —hogar total, circuito y/o artefacto— con precisión, seguridad, granularidad temporal, continuidad de datos y accionabilidad suficientes para construir una propuesta defendible de Marca Hogar, sin confundir medición con ahorro, conectividad con capacidad de medición ni desagregación inferida con medición directa?**

La pregunta obliga a separar:

```text
BOUNDARY / PUNTO DE MEDICIÓN
→ MÉTODO DE MEDICIÓN
→ MAGNITUD ELÉCTRICA OBSERVADA
→ PRECISIÓN / GRANULARIDAD
→ DATO DISPONIBLE
→ INSIGHT / ACCIÓN
→ OUTCOME
→ CLAIM COMERCIAL
```

## 3. Scope operativo de F0

### Dentro del alcance

- monitoreo de electricidad residencial;
- consumo total del hogar;
- consumo por circuito;
- consumo por artefacto cuando exista medición directa o inferencia claramente identificada;
- potencia instantánea y energía acumulada;
- arquitecturas con medición directa, sensores de corriente, submedición o integración con datos de medidor inteligente;
- desagregación de cargas / NILM como capa inferencial a estudiar;
- granularidad temporal, historial, alertas e insights cuando dependan materialmente de la calidad del dato;
- instalación, seguridad eléctrica y compatibilidad con la red doméstica;
- continuidad de servicio, conectividad, app/cloud y disponibilidad del dato cuando formen parte del ownership;
- capacidad de control sólo cuando cambie materialmente el job y no como sinónimo de monitoreo.

### Fuera del alcance o no asumido

- dispositivos cuyo único job sea control domótico sin medición energética significativa;
- productos que prometan “ahorro de energía” sin una cadena observable entre medición, decisión y resultado;
- asumir que Wi‑Fi, app, IA o dashboard implican precisión de medición;
- tratar una estimación de consumo por artefacto como equivalente a submedición directa;
- facturación fiscal/revenue-grade como requisito por defecto;
- gas, agua u otros consumos no eléctricos dentro de esta primera ejecución;
- sistemas solares o baterías como Product Base del candidato, salvo que aparezcan sólo como condición de medición bidireccional/import-export;
- crear Product Bases en F0.

## 4. Minimum Sufficient Evidence usado en F0

F0 utiliza evidencia pública únicamente para estructurar correctamente el problema. No constituye validación comercial local ni validación positiva de ningún SKU.

### 4.1 Potencia y energía no son la misma magnitud

La EIA distingue entre potencia eléctrica y energía consumida: la potencia se expresa, por ejemplo, en W/kW, mientras que el uso acumulado de energía se expresa en Wh/kWh.

Implicación para Method v2:

```text
W / kW
≠
Wh / kWh
```

Una solución puede mostrar potencia instantánea sin que eso pruebe por sí solo la exactitud de la energía acumulada, el costo calculado o la comparabilidad con la factura.

### 4.2 Punto de medición y granularidad son dimensiones estructurales

La EIA describe medidores inteligentes que registran uso eléctrico en intervalos y entregan datos al usuario/utility. ENERGY STAR, por su parte, distingue dispositivos capaces de reportar potencia o energía dentro de sistemas de gestión doméstica.

Implicación:

```text
WHOLE-HOME
≠ CIRCUIT-LEVEL
≠ DEVICE-LEVEL
```

El nivel de granularidad cambia el job, la instalación, la accionabilidad y la carga de evidencia.

### 4.3 Sensor de corriente no equivale automáticamente a medición completa de potencia/energía

Los transformadores de corriente tipo pinza miden corriente mediante acoplamiento magnético. Esa medición puede ser un componente de una arquitectura de energía doméstica, pero F1 deberá verificar qué variables adicionales usa cada sistema —por ejemplo tensión, fase/power factor, frecuencia de muestreo y algoritmo— antes de aceptar claims de potencia o energía.

Regla de investigación:

```text
CURRENT SENSOR PRESENT
≠
REAL POWER / ENERGY ACCURACY VALIDATED
```

### 4.4 Medición directa y desagregación inferida no deben fusionarse

NREL y otras fuentes técnicas distinguen submedición directa de técnicas de desagregación / non-intrusive load monitoring (NILM). NILM intenta identificar cargas individuales a partir de una o pocas mediciones agregadas; la submedición observa circuitos o cargas de forma más directa.

Implicación:

```text
NILM / APPLIANCE ESTIMATE
≠
DIRECT SUBMETERING
```

La desagregación puede aportar valor comercial, pero debe evaluarse como capa inferencial con precisión propia.

### 4.5 Monitoreo, control y ahorro son capas distintas

ENERGY STAR separa la capacidad de reportar consumo de las funciones que sugieren o ejecutan acciones de ahorro. La medición puede habilitar decisiones, reglas o automatizaciones, pero no constituye ahorro garantizado.

Regla:

```text
MONITORING
≠ CONTROL
≠ SAVINGS
```

### 4.6 App, cloud y conectividad son service layer, no mecanismo de medición

Una app puede visualizar, historizar, alertar o automatizar. Sin embargo, la existencia de una app no establece qué se mide, con qué precisión ni durante cuánto tiempo estará disponible el dato.

F1 deberá separar:

```text
MEASUREMENT LAYER
DATA / CONNECTIVITY LAYER
ANALYTICS / INSIGHT LAYER
CONTROL LAYER
```

### 4.7 La instalación en tablero introduce una carga de seguridad propia

Equipos con CTs o conexiones dentro del tablero residencial operan cerca de tensiones peligrosas y pueden requerir instalación calificada según la arquitectura y jurisdicción. La documentación de fabricantes especializados trata explícitamente este riesgo.

Implicación:

> F1/F6 deberán preservar instalación, tensión, fases, protecciones y seguridad como dimensiones estructurales. F0 no emite una conclusión regulatoria argentina.

## 5. Hipótesis estructurales para contrastar en F1

### H1 — La arquitectura nace del boundary de medición y del método

La normalización inicial debe ordenar soluciones por:

```text
WHAT IS MEASURED
→ WHERE IT IS MEASURED
→ HOW IT IS MEASURED
→ WHAT DATA IS PRODUCED
```

No por etiquetas como `smart`, `AI`, `real time` o `Wi‑Fi`.

### H2 — Medición directa a nivel artefacto puede constituir una familia propia

Smart plugs, enchufes medidores y dispositivos equivalentes pueden medir una carga concreta con instalación simple y alta atribución del dato, aunque con cobertura limitada a cargas enchufables compatibles.

### H3 — Monitoreo whole-home mediante sensores en tablero puede constituir una familia propia

Sensores CT y arquitecturas similares pueden observar el consumo agregado del hogar y, según implementación, generación/importación o múltiples fases. Introducen instalación y seguridad mayores que una solución plug-level.

### H4 — Submedición por circuito puede constituir una arquitectura materialmente distinta

Agregar sensores o medidores por circuito cambia granularidad, hardware, costo, instalación y capacidad de atribuir consumo.

### H5 — Integración con smart meter / utility data es una arquitectura diferente

Cuando el dato proviene del medidor de la distribuidora o de una interfaz compatible, cambian hardware, dependencia de infraestructura externa, disponibilidad geográfica y control sobre el dato.

### H6 — NILM / desagregación es una capa inferencial, no una medición directa adicional

Puede justificar una configuración distinta si cambia materialmente la propuesta de valor, pero F1 deberá separar precisión inferencial de precisión del sensor base.

### H7 — Monitoreo + control puede cambiar el job

Un producto que además actúa sobre cargas puede pasar de “hacer visible” a “gestionar” consumo. Esa capacidad puede cambiar seguridad, claims, service layer y postventa y deberá tratarse explícitamente.

### H8 — App / cloud / IA no crean una arquitectura por sí solos

Sólo justifican separación futura cuando cambian materialmente accionabilidad, dependencia de servicio, ownership, privacidad o continuidad operativa.

## 6. Ejes de investigación para F1 — Market / Solution Map

| Eje | Pregunta |
|---|---|
| Boundary | ¿Hogar total, fase, circuito, artefacto o dato de utility? |
| Método | ¿CT, medición directa, submeter, smart plug, interfaz de medidor, otro? |
| Magnitud | ¿Corriente, tensión, potencia real/aparente, factor de potencia, energía? |
| Directo vs inferido | ¿El dato del artefacto se mide o se estima mediante desagregación? |
| Precisión | ¿Qué accuracy declara, bajo qué rango y método? |
| Granularidad temporal | ¿Tiempo real, segundos, minutos, intervalos horarios? |
| Instalación | ¿Plug-and-play, tablero, DIN rail, electricista, utility pairing? |
| Compatibilidad eléctrica | ¿220–240 V / 50 Hz, monofásico, trifásico, tipo de tablero y CT? |
| Bidireccionalidad | ¿Mide importación/exportación, solar o flujo inverso cuando corresponda? |
| Continuidad del dato | ¿Funciona localmente, depende de cloud, qué ocurre sin Internet? |
| Service layer | ¿Historial, alertas, tarifa, automatización, exportación de datos? |
| Actionability | ¿El usuario puede identificar qué hacer a partir del dato? |
| Control | ¿Sólo observa o también acciona cargas? |
| Privacidad / seguridad | ¿Qué datos domésticos se almacenan y dónde? |
| Claim defendible | ¿Qué puede afirmarse realmente sobre medición, insights y ahorro? |

F1 aplicará `MINIMUM SUFFICIENT EVIDENCE`: profundidad suficiente para separar las arquitecturas comercialmente significativas sin agotar todos los dispositivos IoT del mercado.

## 7. Reglas conceptuales que quedan activas

Durante todo el candidato:

```text
SMART / AI / APP LABEL
≠ MEASUREMENT METHOD
≠ ACCURACY
≠ GRANULARITY
≠ ACTIONABILITY
≠ SAVINGS
```

Y además:

```text
CURRENT SENSOR ≠ VALIDATED ENERGY ACCURACY
WHOLE-HOME DATA ≠ APPLIANCE-LEVEL TRUTH
NILM ESTIMATE ≠ DIRECT SUBMETERING
MONITORING ≠ CONTROL
MONITORING ≠ GUARANTEED SAVINGS
CLOUD DASHBOARD ≠ MEASUREMENT ARCHITECTURE
```

## 8. Materialización en la matriz vigente

Baseline validada:

```text
matrix-aut58-brand-cand-003-phase13.xlsx
SHA-256: ec5c8b8f52cc3ae13c2d759e41b4f90f568948fa03676271ce585894d80c44da
Result: PASS
```

Siguiendo el patrón validado en BRAND-CAND-001 y BRAND-CAND-003, F0 crea sólo un `MATRIX_SCOPE_ALIAS` en `Nichos`.

Nueva fila preparada:

```text
ID: 34
Nicho: Marca Hogar — monitoreo doméstico del consumo energético
Estado: En evaluación
```

`Proxima Accion`:

> Ejecutar Fase 1 — mapa de mercado / soluciones en AUTO; separar punto de medición, granularidad y método sin confundir conectividad, control o desagregación inferida con medición directa.

No se crean todavía:

- Product Bases;
- Evaluaciones;
- Evidencias artificiales;
- Fuentes Externas huérfanas sólo para registrar bibliografía conceptual.

La nueva snapshot también actualiza únicamente la nota de cierre de `BRAND-CAND-003` para reflejar el PASS ya obtenido en `aut58`; no modifica su decisión comercial.

Archivo preparado:

```text
matrix-aut59-brand-cand-004-phase0.xlsx
SHA-256: c2a7fb4a3deddacfd286677fd749514bf2934143e3b7fb1cdd12001806f45206
```

## 9. Gate F0

### Análisis conceptual

```text
PASS
```

Existe definición suficiente de:

- pregunta central;
- scope y no-scope;
- separación entre medición directa e inferida;
- separación entre monitoreo, control y ahorro;
- hipótesis estructurales para F1;
- ejes de precisión, instalación, compatibilidad y service layer;
- disciplina de claims.

No existe una incertidumbre conceptual F0 que justifique investigación adicional antes del mapa de soluciones.

### Estado formal de la fase

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut59
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
SHA-256: c2a7fb4a3deddacfd286677fd749514bf2934143e3b7fb1cdd12001806f45206
```

F0 queda formalmente `CLOSED` y habilita `F1 — Market / Solution Map`.

## 10. Próxima acción

F0 queda `CLOSED`. Ejecutar `F1 — Market / Solution Map` en `AUTO`.

## 11. Fuentes públicas utilizadas para el baseline técnico de F0

1. Smart Imports — `BRAND-CAND-004 — Monitoreo doméstico del consumo energético`  
   https://github.com/agelormini2024/smart-imports/blob/main/docs/07-brand/brands/brand-hogar/candidates/brand-cand-004-domestic-energy-monitoring.md

2. U.S. Energy Information Administration — *Measuring electricity*  
   https://www.eia.gov/energyexplained/electricity/measuring-electricity.php

3. U.S. Energy Information Administration — *How many smart meters are installed in the United States, and who has them?*  
   https://www.eia.gov/tools/faqs/faq.php?id=108

4. ENERGY STAR — *Smart Home Energy Management Systems Key Product Criteria*  
   https://www.energystar.gov/products/shems_key_product_criteria

5. Fluke — *Inside Current Transformer (ac) Clamp Meters*  
   https://www.fluke.com/en-us/learn/blog/clamps/inside-current-transformer-ac-clamp-meters

6. NREL — *Innovations in Sensors and Controls for Building Energy Management*  
   https://docs.nrel.gov/docs/fy20osti/75601.pdf

7. International Energy Agency — *Better energy efficiency policy with digital tools*  
   https://www.iea.org/articles/better-energy-efficiency-policy-with-digital-tools

8. Emporia Energy — *Vue 3 Home Energy Monitor Installation Guide*  
   https://cdn.emporiaenergy.com/products/vue3/Vue3-Installation-Guide-EN-110525.pdf

## 12. Changelog

### 2026-09-25 — v0.1.0

- se abre `BRAND-CAND-004` en Method v2 Agile;
- se completa el análisis conceptual de F0;
- se define la pregunta central y el scope operativo eléctrico;
- se separan medición, desagregación, control, conectividad y ahorro;
- se establecen ocho hipótesis estructurales para F1;
- se prepara `MATRIX_SCOPE_ALIAS` ID 34;
- se materializa `matrix-aut59-brand-cand-004-phase0.xlsx`;
- `aut59` obtiene PASS limpio del Matrix Validator;
- F0 queda formalmente `CLOSED`;
- siguiente fase: `F1 — Market / Solution Map` en AUTO.
