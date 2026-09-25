---
id: si-research-029
title: BRAND-CAND-004 — Method v2 Agile — F1 Market / Solution Map
description: Mapa de arquitecturas comercialmente significativas para monitoreo doméstico del consumo energético.
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
  - phase-1
related:
  - si-research-028
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F1 Market / Solution Map

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input vigente

F0 quedó formalmente cerrada sobre:

```text
matrix-aut59-brand-cand-004-phase0.xlsx
SHA-256: c2a7fb4a3deddacfd286677fd749514bf2934143e3b7fb1cdd12001806f45206
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Pregunta de continuidad:

> **¿Qué arquitecturas domésticas de monitoreo del consumo eléctrico son comercialmente significativas y materialmente distintas como para merecer evaluación de madurez, sin confundir punto de medición, inferencia, conectividad, control o analytics con la capacidad de medición propiamente dicha?**

F1 no evalúa todavía demanda local, competencia, origen, costos, margen ni selección de Product Bases.

## 2. Principio de normalización

La unidad correcta del mapa no es la etiqueta `smart energy monitor`, `AI energy saver`, `Wi‑Fi meter` ni una app aislada.

Se normaliza mediante:

```text
MEASUREMENT BOUNDARY
→ MEASUREMENT METHOD
→ ELECTRICAL QUANTITY
→ DIRECT vs INFERRED DATA
→ TEMPORAL / CHANNEL GRANULARITY
→ INSTALLATION / INFRASTRUCTURE
→ DATA / SERVICE LAYER
→ ACTIONABILITY
```

Reglas:

```text
SMART / WIFI / APP ≠ MEASUREMENT ARCHITECTURE
CONTROL ≠ MONITORING
MONITORING ≠ SAVINGS
CURRENT SENSOR ≠ VALIDATED POWER / ENERGY ACCURACY
WHOLE-HOME AGGREGATE ≠ APPLIANCE-LEVEL TRUTH
NILM ESTIMATE ≠ DIRECT SUBMETERING
```

La EIA distingue potencia instantánea en W/kW de energía acumulada en Wh/kWh. Esa separación queda activa para todo el candidato.

## 3. Ejes del mapa

### 3.1 Boundary de medición

```text
B1 — artefacto / carga enchufable
B2 — circuito / ramal
B3 — múltiples circuitos
B4 — hogar completo / acometida principal
B5 — medidor de utility / intervalo externo
```

### 3.2 Método de obtención del dato

```text
M1 — medición inline directa
M2 — medidor/submeter instalado en tablero
M3 — sensores CT por circuito o conductor
M4 — lectura/interfaz de smart meter o utility data
M5 — inferencia / desagregación sobre señal agregada
```

### 3.3 Tipo de dato

```text
D1 — potencia instantánea
D2 — energía acumulada
D3 — serie temporal / intervalos
D4 — estimación por carga o categoría
D5 — tarifa / costo calculado como capa derivada
```

## 4. Arquitecturas comercialmente significativas

### A1 — Plug-level direct metering

```text
Boundary: B1
Method: M1
Primary output: D1 + D2, a veces D3
```

Incluye enchufes medidores, smart plugs con medición y dispositivos inline equivalentes que atribuyen el consumo a una carga enchufable concreta.

Variables estructurales:

- rango de tensión/corriente/potencia;
- precisión declarada;
- tipo de carga compatible;
- medición de potencia y energía;
- consumo propio;
- memoria local vs cloud;
- presencia opcional de relay/control;
- seguridad eléctrica y formato de enchufe.

ENERGY STAR incluye smart plugs, smart power strips y home energy monitors dentro de `Plug Load Monitor/Control` cuando son capaces de reportar potencia o energía. DOE también describe smart outlets que pueden medir uso de energía además de controlar la alimentación.

Lectura F1:

> Arquitectura directa, atribuible y de instalación simple; merece avanzar a F2. La función de control no crea por sí sola una arquitectura de medición diferente.

### A2 — Panel / DIN-rail direct submetering

```text
Boundary: B2 o B4
Method: M2
Primary output: D1 + D2 + D3
```

Incluye medidores compactos, submeters y equipos instalados en tablero que miden directamente un circuito, feeder o alimentación mediante conexión eléctrica y/o sensor dedicado.

Diferencias materiales frente a A1:

- instalación fija;
- mayor carga de seguridad eléctrica;
- compatibilidad con tablero, tensión, fases y protecciones;
- puede medir cargas no enchufables;
- potencial mayor estabilidad del dato;
- postventa e instalación más exigentes.

Lectura F1:

> Arquitectura diferenciada y comercialmente relevante; avanzar a F2 con foco en seguridad, precisión, formato de instalación y compatibilidad local.

### A3 — Multi-circuit CT monitoring

```text
Boundary: B3
Method: M3
Primary output: D1 + D2 + D3 por canal
```

Sistema de tablero con múltiples CTs u otros sensores destinados a medir varios circuitos de manera paralela.

Variables estructurales:

- número de canales;
- rango y diámetro de CT;
- mapeo físico circuito↔sensor;
- referencia de tensión/fase usada para calcular potencia;
- precisión por canal;
- instalación y espacio en tablero;
- expansión modular;
- continuidad local/cloud.

Lectura F1:

> Arquitectura con alta granularidad y atribución directa por circuito. Merece avanzar a F2 separada de whole-home aggregate porque cambia hardware, instalación, costo y accionabilidad.

### A4 — Whole-home aggregate CT monitoring

```text
Boundary: B4
Method: M3
Primary output: D1 + D2 + D3 agregados
```

Sistema que observa uno o más conductores principales para medir el consumo total del hogar —y eventualmente flujos bidireccionales— sin instrumentar cada circuito.

Fortalezas estructurales:

- cobertura amplia con pocos sensores;
- hardware relativamente contenido;
- series temporales de alta frecuencia posibles según implementación.

Limitación estructural:

```text
WHOLE-HOME AGGREGATE
≠
DIRECT APPLIANCE ATTRIBUTION
```

Lectura F1:

> Arquitectura real y diferenciada; avanzar a F2. La atribución de consumos individuales debe tratarse por separado si depende de inferencia.

### A5 — Aggregate measurement + NILM / disaggregation

```text
Base measurement: A4 o dato agregado equivalente
Additional layer: M5
Output: D4 inferido
```

La desagregación o `Non-Intrusive Load Monitoring` intenta inferir consumos de aparatos individuales a partir de una señal agregada. IEEE la describe como un problema de descomposición de la carga total en contribuciones de aparatos; la literatura reciente continúa tratándola como inferencia sobre señal agregada y no como submedición directa.

Variables estructurales:

- tasa de muestreo y features disponibles;
- clases de cargas reconocibles;
- entrenamiento/calibración;
- precisión por tipo de aparato;
- generalización entre hogares;
- dependencia de cloud/modelo;
- tratamiento de cargas variables o multiestado.

Regla:

```text
APPLIANCE ESTIMATE
≠
DIRECT MEASUREMENT
```

Lectura F1:

> Mantener como arquitectura comercial diferenciada cuando la inferencia sea parte central de la propuesta de valor, pero con carga de evidencia propia. Avanza a F2 condicionada por precisión y generalización.

### A6 — Smart-meter / utility-data integration

```text
Boundary: B5
Method: M4
Primary output: D2 + D3 según utility
```

Arquitectura en la que el producto o servicio consume datos provenientes del medidor de la distribuidora, una interfaz de Home Area Network o una API/estándar de intercambio.

DOE documenta Green Button como una forma de acceso del cliente a datos de uso energético y aclara que la granularidad puede variar —por ejemplo 15 minutos, hora, día o mes— según la utility y la infraestructura disponible.

Variables estructurales:

- disponibilidad local del smart meter;
- protocolo/interfaz soportada;
- granularidad;
- latencia;
- autenticación y consentimiento;
- dependencia de utility/terceros;
- continuidad del servicio;
- privacidad.

Lectura F1:

> Arquitectura válida, pero fuertemente dependiente de infraestructura externa y disponibilidad jurisdiccional. Avanzar a F2 como familia condicionada, no asumir portabilidad al mercado argentino.

## 5. Capas que NO se convierten en arquitectura independiente por sí solas

### Control / relay / automatización

Controlar una carga puede cambiar el job comercial, pero no reemplaza la definición de cómo se mide. `MONITOR + CONTROL` deberá distinguirse en F6 sólo si cambia materialmente seguridad, service layer o propuesta de valor.

### App / dashboard / cloud

Visualizan, almacenan o procesan datos. No establecen precisión ni método de medición.

### Tarifa / costo estimado

Convertir kWh en dinero requiere tarifa, estructura de precios e impuestos. Es una capa derivada, no una magnitud eléctrica medida.

### IA / recomendaciones

Pueden mejorar clasificación o accionabilidad, pero no convierten por sí mismas un producto en una arquitectura distinta.

### Home automation platform

Una plataforma generalista puede integrar medidores, smart plugs o controles, pero su amplitud funcional no constituye una Product Base de monitoreo energético por sí sola.

## 6. Soluciones adyacentes que quedan fuera del mapa principal

- analizadores profesionales de calidad de energía;
- instrumentos portátiles de electricista;
- medidores revenue-grade como requisito universal;
- equipos solares, inversores o baterías cuyo job principal sea generación/almacenamiento;
- cargadores EV cuyo job principal sea carga;
- dispositivos de ahorro o corrección de factor de potencia vendidos al consumidor sin una arquitectura defendible de medición;
- monitoreo de gas/agua dentro de esta ejecución.

Pueden reaparecer como comparables o condiciones técnicas, no como Product Bases automáticas de `BRAND-CAND-004`.

## 7. Aprendizaje estructural de F1

El espacio comercial puede representarse como:

```text
SOLUTION ARCHITECTURE
=
MEASUREMENT BOUNDARY
+
MEASUREMENT METHOD
+
DIRECT / INFERRED STATUS
+
INSTALLATION / INFRASTRUCTURE DEPENDENCY
+
DATA CONTINUITY / SERVICE CONSEQUENCES
```

La granularidad y accionabilidad se evalúan después sobre esa arquitectura.

Esto evita los atajos:

```text
SMART FEATURE → PRODUCT BASE
APP → PRODUCT BASE
AI DISAGGREGATION → DIRECT MEASUREMENT
CONTROL CAPABILITY → MEASUREMENT ARCHITECTURE
```

La frontera formal de Product Base se resolverá en F6.

## 8. Métricas y evidencia que F2–F6 deberán preservar

### Medición

- magnitud medida y calculada;
- rango de tensión/corriente/potencia;
- precisión declarada;
- intervalo de muestreo/registro;
- tratamiento de factor de potencia y fase cuando aplique;
- energía acumulada;
- bidireccionalidad cuando corresponda.

### Granularidad

- hogar total;
- fase;
- circuito;
- carga directa;
- estimación por aparato/categoría.

### Instalación y seguridad

- plug-and-play vs tablero;
- DIN rail / CT / conexión directa;
- monofásico/trifásico;
- 220–240 V / 50 Hz;
- protecciones y requerimiento de instalador;
- espacio físico y compatibilidad de tablero.

### Ownership / service layer

- funcionamiento offline;
- cloud obligatorio u opcional;
- retención/exportación de datos;
- app y soporte;
- actualizaciones;
- privacidad;
- dependencia de utility o protocolo externo.

### Claims

- no transformar precisión de sensor en ahorro garantizado;
- distinguir datos medidos de inferidos;
- distinguir costo estimado de medición eléctrica;
- verificar método/rango antes de usar claims de exactitud.

## 9. Gate F1

### Pregunta de gate

> ¿Existe un mapa suficientemente discriminante de arquitecturas comerciales como para pasar a evaluar madurez, sin convertir features, analytics, control o inferencia en medición directa?

Resultado conceptual:

```text
PASS
```

Razón:

- se separó artefacto, circuito, multi-circuito, hogar total y utility data;
- se separaron medición inline, submeter, CT, utility interface e inferencia;
- se aisló NILM como capa inferencial con carga de evidencia propia;
- se preservó control como capacidad distinta del monitoreo;
- se distinguieron app/cloud/IA de la arquitectura de medición;
- se registraron instalación, precisión y dependencia externa como ejes estructurales.

## 10. Materialización en matriz

Baseline validada:

```text
matrix-aut59-brand-cand-004-phase0.xlsx
SHA-256: c2a7fb4a3deddacfd286677fd749514bf2934143e3b7fb1cdd12001806f45206
Result: PASS
```

F1 no crea Product Bases ni evidencia comercial artificial. Actualiza el `MATRIX_SCOPE_ALIAS` ID 34 para registrar:

- F0 `CLOSED`;
- mapa de arquitecturas de F1;
- siguiente gate `F2 — Maturity`;
- ruta documental `SI-RESEARCH-029`;
- estado de F1 pendiente de Matrix Validator.

Archivo preparado:

```text
matrix-aut60-brand-cand-004-phase1.xlsx
SHA-256: 45a4709794501bf3e5582939dd4cc95ee4682b1aad389bc853a788a905c0ebc1
```

## 11. Estado formal de F1

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut60
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F1 CLOSED
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
SHA-256: 45a4709794501bf3e5582939dd4cc95ee4682b1aad389bc853a788a905c0ebc1
```

F2 queda formalmente abierta después de este cierre.

## 12. Próxima acción

F1 queda `CLOSED`. Ejecutar `F2 — Maturity` en `AUTO`.

## 13. Fuentes públicas utilizadas para el baseline técnico de F1

1. U.S. Energy Information Administration — *Measuring electricity*  
   https://www.eia.gov/energyexplained/electricity/measuring-electricity.php

2. ENERGY STAR — *Smart Home Energy Management Systems Key Product Criteria*  
   https://www.energystar.gov/products/shems_key_product_criteria

3. U.S. Department of Energy — *Smart Outlets: Wireless Meter and Control Systems for Plug and Process Loads*  
   https://betterbuildingssolutioncenter.energy.gov/resources/smart-outlets-wireless-meter-and-control-systems-plug-and-process-loads

4. U.S. Department of Energy — *Green Button*  
   https://www.energy.gov/data/green-button

5. NIST — *A NIST Testbed for Examining the Accuracy of Smart Meters under High Harmonic Waveform Loads*  
   https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8248.pdf

6. IEEE Technology Navigator — *Load monitoring / Non-Intrusive Load Monitoring*  
   https://technav.ieee.org/topic/load-monitoring/

7. IEEE — *Sequence-to-point learning methods for Non Intrusive Load Disaggregation: A Review*  
   https://ieeexplore.ieee.org/document/10775789/

## 14. Changelog

### 2026-09-25 — v0.1.0

- F0 queda formalmente cerrada sobre `aut59 PASS`;
- se construye el mapa F1 con seis arquitecturas comercialmente significativas;
- se separan medición directa, medición agregada, submedición e inferencia;
- se mantiene NILM como capa comercial condicionada por precisión/generalización;
- se registran app/cloud/IA y control como capas no equivalentes al método de medición;
- se materializa `matrix-aut60-brand-cand-004-phase1.xlsx`;
- `aut60` obtiene PASS limpio y F1 queda formalmente `CLOSED`;
- siguiente fase: `F2 — Maturity` en AUTO.
