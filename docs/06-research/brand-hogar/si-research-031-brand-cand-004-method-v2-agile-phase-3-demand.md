---
id: si-research-031
title: BRAND-CAND-004 — Method v2 Agile — F3 Demand
description: Evaluación de demanda local de monitoreo doméstico del consumo energético mediante evidencia de Mercado Libre normalizada por boundary y arquitectura real.
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
  - phase-3
  - demand
related:
  - si-research-028
  - si-research-029
  - si-research-030
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F3 Demand

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input vigente

F2 quedó formalmente cerrada sobre:

```text
matrix-aut61-brand-cand-004-phase2.xlsx
SHA-256: c693140851f0d5df25e741fe8cf60ba84d3440fe4efde478f4c952b2917c60d3
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

F3 se ejecutó en modalidad `COLLABORATIVE` para la recolección de evidencia local y en `AUTO` para normalización, análisis y materialización.

## 2. Pregunta de F3

> ¿Existe demanda local observable y suficientemente defendible por soluciones domésticas de monitoreo del consumo eléctrico como para justificar continuar a F4, separando medición real de funciones adyacentes de control, automatización y protección?

F3 no estima tamaño total de mercado ni participación potencial.

## 3. Reglas metodológicas

```text
VENTAS VISIBLES ≠ TAMAÑO DE MERCADO

SIN VENTAS VISIBLES ≠ SIN DEMANDA

OFERTA DISPONIBLE ≠ EVIDENCIA DE DEMANDA

QUERY COHORT ≠ PRODUCT BASE

SEARCH TERM ≠ MARKET SEGMENT

SMART-PLUG DEMAND
≠
ENERGY-MONITORING DEMAND

HYBRID SALES
≠
MONITORING-ONLY DEMAND

CONTROL / SCHEDULING SAVINGS
≠
SAVINGS CAUSED BY MEASUREMENT

PROTECTION DEVICE SALES
≠
PURE MONITORING DEMAND

MARKETPLACE ATTRIBUTE
≠
TECHNICAL SPECIFICATION VERIFIED
```

## 4. Muestra

Se normalizaron **20 publicaciones únicas** de Mercado Libre Argentina:

```text
ML-0120 … ML-0139
```

Distribución:

```text
D1 — Plug-level direct meter — standalone      5
D2 — Smart plug + energy monitoring            5
D3 — Installed / DIN-rail direct meter         5
D4 — CT whole-home / multi-circuit             5
TOTAL                                           20
```

No se crearon Product Bases en F3. Esa frontera corresponde a F6.

## 5. D1 — Plug-level direct meter — standalone

### Resultado

```text
DEMAND SIGNAL: POSITIVE
CONFIDENCE: MEDIUM
MINIMUM SUFFICIENT EVIDENCE: REACHED
```

Casos:

| ML ID | Producto / referencia | Ventas visibles SKU | Lectura |
|---|---|---:|---|
| ML-0120 | Paefair plug-level 10A | +50 | Medición directa por artefacto; V/A/W/kWh y otras magnitudes |
| ML-0121 | Genérico plug-level 10A | +50 | Segunda señal positiva; producto cercano al anterior |
| ML-0122 | Estink Power Meter Plug | No informadas | Diversidad de marca/precio; no atribuir ventas de tienda al SKU |
| ML-0123 | EnergiaPlus WattView 2000 | No informadas | Memoria y cálculo de costo; ficha con inconsistencias técnicas |
| ML-0124 | Mecheer JK-PM07-US 16A | No informadas | Variante de mayor capacidad con medición y memoria |

Lectura:

- existe un job-to-be-done simple y comprensible: medir cuánto consume/cuesta un artefacto;
- hay señal transaccional real;
- la evidencia no es suficientemente amplia para inferir tamaño de mercado;
- 10A vs 16A, memoria ante corte y compatibilidad física con la red argentina aparecen como criterios potenciales para fases posteriores.

## 6. D2 — Smart plug + energy monitoring

### Resultado

```text
DEMAND SIGNAL: POSITIVE
CONFIDENCE: MEDIUM-HIGH
MINIMUM SUFFICIENT EVIDENCE: REACHED
```

Casos:

| ML ID | Producto / referencia | Ventas visibles SKU | Clasificación |
|---|---|---:|---|
| ML-0125 | Smartis 16A | +10000 | SUPPORT — CONTROL-DOMINANT |
| ML-0126 | DOMOTIQ 20A | +100 | SUPPORT — CONTROL-DOMINANT |
| ML-0127 | Demasled domo-54 | +500 | CORE — monitoring explícito |
| ML-0128 | Fortitech 16A | +1000 | CORE — monitoring explícito |
| ML-0129 | Geneve doble smart | +500 | SUPPORT — ADJACENT / EMBEDDED |

Lectura:

- existe fuerte actividad comercial de smart plugs;
- Demasled y Fortitech muestran demanda donde la medición de consumo está explícitamente integrada;
- Smartis, DOMOTIQ y Geneve demuestran que la demanda híbrida puede estar impulsada por control remoto, programación, voz o diseño;
- por lo tanto, las ventas de smart plugs no se atribuyen automáticamente al monitoring.

## 7. D3 — Installed / DIN-rail direct meter

### Resultado

```text
DEMAND SIGNAL: STRONG POSITIVE
CONFIDENCE: MEDIUM-HIGH
MINIMUM SUFFICIENT EVIDENCE: REACHED
```

Casos:

| ML ID | Producto / referencia | Ventas visibles SKU | Clasificación |
|---|---|---:|---|
| ML-0130 | Genérico DIN 80A | +500 | CORE — DIRECT METERING |
| ML-0131 | Pronext WA-1000 45A | +1000 | CORE — DIRECT METERING |
| ML-0132 | Melech GML064/GML131 80A | +1000 | CORE — DIRECT METERING |
| ML-0133 | Geneve GE-PTD63 | +1000 | SUPPORT — PROTECTION + MONITORING |
| ML-0134 | TBCin TDP-263T | +1000 | SUPPORT — PROTECTION + MONITORING |

Jobs observados en opiniones:

```text
medir consumo de departamento / unidad
dividir factura entre vecinos
separar consumo de local o alquiler
controlar kWh acumulados
```

Lectura:

> D3 aporta la señal más limpia y directamente atribuible al problema de medición/submedición del candidato.

Los casos Geneve/TBCin se conservan como evidencia híbrida porque protección y control también pueden explicar parte de las ventas.

## 8. D4 — CT whole-home / multi-circuit

### Resultado

```text
DEMAND SIGNAL: LIMITED POSITIVE
CONFIDENCE: MEDIUM
MINIMUM SUFFICIENT EVIDENCE: REACHED
```

Casos:

| ML ID | Producto / referencia | Ventas visibles SKU | Arquitectura |
|---|---|---:|---|
| ML-0135 | Peacefair / PZEM-061 split CT | +5 | 1 CT / direct meter |
| ML-0136 | PC321-Z-TY 120A | No informadas | 3 CT / Zigbee / multi-circuit |
| ML-0137 | Sungrass eMonHub HA20 | No informadas | multi-circuit / Home Assistant |
| ML-0138 | Blindsmart 2×120A CT | No informadas | whole-home / bidirectional |
| ML-0139 | Sonoff POW CT 100A | +25 | 1 CT / Wi-Fi / monitoring + control |

Lectura:

- la arquitectura existe en el mercado local;
- hay al menos dos señales transaccionales visibles;
- aparecen soluciones de uno, dos, tres y múltiples circuitos;
- la tracción observable es muy inferior a D2/D3;
- varias ofertas son especializadas, importadas o de ticket alto;
- D4 se trata como nicho real y no como mercado masivo demostrado.

## 9. Comparación de cohorts

| Cohort | Señal | Confianza | Lectura |
|---|---|---|---|
| D1 Plug-level standalone | `POSITIVE` | `MEDIUM` | job simple, señal moderada |
| D2 Smart plug hybrid | `POSITIVE` | `MEDIUM-HIGH` | fuerte actividad, attribution problem |
| D3 DIN direct meter | `STRONG POSITIVE` | `MEDIUM-HIGH` | señal más directamente atribuible |
| D4 CT whole-home/multi-circuit | `LIMITED POSITIVE` | `MEDIUM` | nicho técnico real, menor tracción |

## 10. Evaluación de demanda del candidato

Se materializa:

```text
EVAL-0020
Criterio: Demanda
Score: 4 / 5
Confianza: Media
Evidencia: EVID-0259
```

Interpretación:

> La demanda local del candidato es alta pero heterogénea. Existe evidencia observable en varios boundaries —artefacto, circuito/alimentación y hogar—, con una señal particularmente sólida para medidores DIN directos. La actividad de smart plugs refuerza el interés comercial, pero debe descontarse el efecto de control/automatización. CT whole-home/multi-circuit permanece como segmento especializado.

El score 4/5 **no** significa:

- mercado masivo cuantificado;
- atractivo económico confirmado;
- baja competencia;
- Product Base seleccionado;
- aptitud automática como primer producto.

## 11. Gate F3

Pregunta:

> ¿La evidencia de demanda es suficiente para justificar F4 — Competencia?

Resultado conceptual:

```text
PASS
```

Razón:

- cuatro cohorts comercialmente observables;
- D1 y D3 muestran demanda directamente vinculada a medición;
- D2 agrega volumen comercial con una incertidumbre de atribución explícitamente controlada;
- D4 confirma una capa técnica/nicho sin necesidad de sobreinterpretarla;
- ya no es necesario ampliar la recolección antes de analizar competencia.

## 12. Materialización en matriz

Baseline validada:

```text
matrix-aut61-brand-cand-004-phase2.xlsx
SHA-256: c693140851f0d5df25e741fe8cf60ba84d3440fe4efde478f4c952b2917c60d3
Result: PASS
```

F3 agrega:

```text
Publicaciones ML
→ ML-0120 … ML-0139

Fuentes
→ SRC-0406 … SRC-0426

Evidencias
→ EVID-0259

Evidencia Fuentes
→ EVSRC-0482 … EVSRC-0502

Evaluaciones
→ EVAL-0020 — Demanda = 4/5 — confianza Media
```

`Nichos` ID 34 queda con:

```text
Demanda: 4
Confianza Demanda: Media
Criterios evaluados: 1/10
Score parcial: 4
```

Archivo preparado:

```text
matrix-aut62-brand-cand-004-phase3.xlsx
SHA-256: 2975a20df2c0f76f6e1e10ffeb9c4e1176137d5bac91030e1796b7cfb4ee8854
```

## 13. Estado formal de F3

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut62
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F3 CLOSED
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
SHA-256: 2975a20df2c0f76f6e1e10ffeb9c4e1176137d5bac91030e1796b7cfb4ee8854
```

F4 queda formalmente abierta después de este cierre.

## 14. Próxima acción

F3 queda `CLOSED`. Ejecutar `F4 — Competition` en modalidad `AUTO`.

F4 reutilizará estas 20 publicaciones para evaluar presión competitiva por arquitectura, propuesta, precio y service layer, manteniendo:

```text
COMPETITION ≠ COUNT OF LISTINGS
LOW COMPETITION ≠ HIGH OPPORTUNITY
PRICE DISPERSION ≠ QUALITY LADDER
```

## 15. Changelog

### 2026-09-25 — v0.1.0

- se completa recolección colaborativa D1–D4;
- se normalizan 20 publicaciones como ML-0120..ML-0139;
- D1 queda `POSITIVE / MEDIUM`;
- D2 queda `POSITIVE / MEDIUM-HIGH`, con atribución híbrida;
- D3 queda `STRONG POSITIVE / MEDIUM-HIGH`;
- D4 queda `LIMITED POSITIVE / MEDIUM`;
- se materializa EVAL-0020 = 4/5, confianza Media;
- se prepara `matrix-aut62-brand-cand-004-phase3.xlsx`;
- `aut62` obtiene PASS limpio y F3 queda formalmente `CLOSED`;
- siguiente fase: `F4 — Competition` en AUTO.
