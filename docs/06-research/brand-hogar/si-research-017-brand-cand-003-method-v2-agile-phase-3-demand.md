---
id: si-research-017
title: BRAND-CAND-003 — Method v2 Agile — F3 Demand
description: Evaluación de demanda observable para tratamiento doméstico del aire interior.
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
  - phase-3
---

# SI-RESEARCH-017 — BRAND-CAND-003 — Method v2 Agile — F3 Demand

Fecha: 2026-09-24
Estado: `CLOSED`

## 1. Objetivo

Evaluar si existe demanda observable en Argentina para `BRAND-CAND-003 — Tratamiento doméstico del aire interior`, distinguiendo la búsqueda comercial usada en Mercado Libre de la arquitectura tecnológica real de cada publicación.

Principio de normalización:

```text
SEARCH TERM
≠
MARKET SEGMENT
≠
REAL MECHANISM
```

La búsqueda inicial `purificador de aire HEPA` devolvió productos con mecanismos heterogéneos. Por ello F3 conserva por separado:

- query cohort;
- mecanismo real;
- arquitectura normalizada;
- señal de ventas visible;
- observaciones de calidad/limitación de evidencia.

## 2. Cohorts normalizados

### D1 — Filtración mecánica dominante

Representa equipos portátiles donde el mecanismo principal es ventilador + prefiltro + HEPA. Puede existir carbón auxiliar o ionización secundaria sin que eso cambie el mecanismo primario.

Señales observadas:

- Levoit Core Mini: `+100 vendidos`;
- Lumenac AP-18: `+25 vendidos`;
- Lumenac AP-26: `+5 vendidos`;
- otros productos importados/no locales sin contador visible.

Lectura: existe demanda observable para purificación portátil basada en HEPA, aunque la señal visible es menor que en algunos productos activos de bajo ticket.

### D2 — Partículas + gases/olores

Incluye equipos donde la etapa de sorción forma parte material de la propuesta, no simplemente una mención nominal a carbón activado.

Casos especialmente útiles:

- Casiba Brezza 480: HEPA H13 + carbón activado con claim explícito de gases/olores;
- HoMedics Natura: True HEPA + carbón activado con reducción declarada de olores/COV;
- Jafanda JF260: HEPA + `300 g` de carbón activado, CADR declarado `260 m³/h`;
- AIRROMI A2002: orientación a olores/caspa de mascotas;
- Levoit Core Mini: carbón presente, pero capacidad gas-phase menos documentada.

`Sans Mini` queda fuera del core D2 por evidencia insuficiente en el PDF para demostrar que el carbón sea una etapa material de tratamiento de gases/olores.

### D3 — Tecnologías activas

Incluye ionización, ozono, UVGI, fotocatálisis y combinaciones híbridas.

Señales observadas:

- Gadnic ionizador: `+500 vendidos`;
- Gadnic ozonizador: `+1000 vendidos`;
- Ozonizer Life O3: `+1000 vendidos`;
- ESEA Split Germicida: `+100 vendidos`;
- E-CLEANER UV-C/TiO2: `1 vendido`.

Lectura: es el cohort con mayor señal transaccional visible dentro de la muestra, especialmente en productos de menor ticket. Esto no valida eficacia, seguridad ni Brand Fit.

### D4 — HVAC / conductos

Incluye sistemas UV/PCO y tratamiento instalado dentro de aire acondicionado central, split o conductos.

Casos observados:

- IonFactor UV-C: `3 vendidos`;
- D200 doble lámpara UV para conductos: sin contador visible;
- Honeywell AirBRITE: sin contador visible;
- Affectnianly 4 lámparas HVAC: sin contador visible.

Lectura: hay oferta local/importada, pero la señal visible es claramente más débil y especializada que en las arquitecturas portátiles.

## 3. Resultado F3

La demanda del candidato se considera **positiva pero heterogénea**.

```text
D1 — HEPA / partículas                 → demanda observable / moderada
D2 — partículas + gases/olores        → oferta material / señal transaccional desigual
D3 — tecnologías activas              → señal visible fuerte en productos de bajo ticket
D4 — central / HVAC                    → señal local débil / especializada
```

Conclusión metodológica:

```text
VISIBLE SALES ≠ MARKET SIZE
NO VISIBLE SALES ≠ NO DEMAND
DEMAND ≠ EFFICACY / SAFETY
QUERY COHORT ≠ REAL MECHANISM
```

La muestra permite validar que existe mercado para el tratamiento doméstico del aire interior, pero no permite afirmar que todas las arquitecturas tengan igual aceptación ni que la mayor cantidad de ventas visibles identifique la mejor arquitectura para Smart Imports.

## 4. Evaluación en matriz

```text
EVAL-0017
Criterio: Demanda
Valor: 4/5
Confianza: Media
Soporte: EVID-0249
```

Racional:

- múltiples publicaciones con ventas visibles;
- presencia de señal transaccional en más de una arquitectura;
- fuerte heterogeneidad de precio y mecanismo;
- concentración de ventas visibles altas en tecnologías activas de bajo ticket;
- menor señal visible en D4;
- Mercado Libre no permite inferir tamaño total de mercado.

## 5. Materialización

Snapshot preparado:

```text
matrix-aut48-brand-cand-003-phase3.xlsx
SHA-256: e803ae848bb17215c7f58bd2c1c6805f0476299958e38b5413852bce95fe22c3
```

Registros agregados:

```text
Publicaciones ML : ML-0100 ... ML-0119
Fuentes          : SRC-0367 ... SRC-0387
Evidencias       : EVID-0249
Evaluaciones     : EVAL-0017
Evidencia Fuentes: EVSRC-0404 ... EVSRC-0424
```

No se crean Product Bases en F3. La consolidación conceptual de Product Bases permanece en F6.

## 6. Gate

Estado final:

```text
F3 — CLOSED

Validation checkpoint:
matrix-aut48-brand-cand-003-phase3.xlsx
SHA-256: e803ae848bb17215c7f58bd2c1c6805f0476299958e38b5413852bce95fe22c3
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0

NEXT:
F4 — Competition
→ AUTO
→ reutilizar las mismas publicaciones de Mercado Libre
```


## 7. Cierre de validación

El 2026-09-24 `aut48` fue validada con `Matrix Validator 0.1.0` / `full-matrix-v5 0.7.0` y resultado `PASS` limpio. F3 queda formalmente cerrada y F4 se abre en modalidad AUTO.
