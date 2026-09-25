---
id: si-research-018
title: BRAND-CAND-003 — Method v2 Agile — F4 Competition
description: Evaluación de competencia observable para tratamiento doméstico del aire interior.
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
  - phase-4
---

# SI-RESEARCH-018 — BRAND-CAND-003 — Method v2 Agile — F4 Competition

Fecha: 2026-09-24  
Estado: `CLOSED`

## 1. Objetivo

Evaluar la presión competitiva observable de `BRAND-CAND-003 — Tratamiento doméstico del aire interior` reutilizando la evidencia de Mercado Libre capturada en F3, sin ampliar investigación salvo que aparezca una brecha capaz de cambiar el gate.

Principios:

```text
COMPETITION ≠ COUNT OF LISTINGS
LOW COMPETITION ≠ HIGH OPPORTUNITY
PRICE DISPERSION ≠ QUALITY LADDER
QUERY COHORT ≠ REAL MECHANISM
```

F4 no crea Product Bases. La consolidación conceptual permanece en F6.

## 2. Método

Se reutilizan `ML-0100 ... ML-0119` y sus fuentes globales `SRC-0367 ... SRC-0386`.

Cada publicación se normaliza por:

- arquitectura real;
- vendedor y marca;
- presencia o ausencia de importación bajo demanda;
- fortaleza del vendedor;
- presión de precio;
- calidad de la publicación;
- diferenciación visible;
- riesgo técnico / de claims;
- debilidad competitiva;
- oportunidad de diferenciación.

La publicación `ML-0113 — Sans Mini` permanece como benchmark ambiguo y no se cuenta como competidor core D2 por falta de evidencia suficiente sobre materialidad del tratamiento gas-phase.

## 3. Mapa competitivo por arquitectura

### D1 — Filtración mecánica dominante

Muestra core: 4 publicaciones.

Rango de precios observado:

```text
ARS 123.637 — 295.999
mediana aproximada: ARS 223.571
```

Patrón competitivo:

- presencia local de Lumenac en más de una configuración;
- coexistencia con importadores bajo demanda;
- presión de precio moderada/alta en modelos locales;
- documentación técnica desigual;
- 110V, entrega diferida y garantía corta aparecen como fricciones en varios importados.

Lectura:

```text
SATURATION: MEDIA
```

La diferenciación defendible no pasa por declarar simplemente `HEPA H13`, sino por demostrar desempeño sistémico, disponibilidad de filtros, cobertura real, compatibilidad 220V, garantía y soporte.

### D2 — Partículas + gases/olores

Muestra core: 6 publicaciones.

Rango de precios observado:

```text
ARS 199.999 — 884.999
mediana aproximada: ARS 465.999
```

Patrón competitivo:

- Casiba funciona como benchmark técnico/local fuerte;
- Levoit aporta marca y tracción visible;
- Gadnic extiende una marca fuerte hacia una arquitectura híbrida;
- HoMedics, Jafanda y AIRROMI muestran oferta importada de ticket alto;
- la calidad de evidencia sobre carbón activado varía mucho.

El mejor benchmark técnico de sorción dentro de la muestra es Jafanda, que declara `300 g` de carbón activado y CADR `260 m³/h`; esto permite separar una etapa gas-phase material de una mera mención nominal a carbón.

Lectura:

```text
SATURATION: MEDIA
```

Existe espacio competitivo si la propuesta puede sostener con evidencia qué gases/olores trata, materialidad del sorbente, desempeño, consumibles y costo recurrente.

### D3 — Tecnologías activas

Muestra core: 5 publicaciones.

Rango de precios observado:

```text
ARS 57.028 — 471.913
mediana aproximada: ARS 164.900
```

Patrón competitivo:

- Gadnic/Bidcom concentra los benchmarks transaccionales más fuertes de la muestra;
- ionización y ozono compiten en tickets bajos;
- ESEA agrega una arquitectura híbrida compleja con UV-C, ozono, HEPA, carbón y fotocatálisis;
- E-CLEANER representa UVGI + fotocatálisis con declaración ozone-free.

Lectura:

```text
SATURATION: MEDIA/ALTA EN LOW-TICKET
```

Es el frente competitivo más exigente por precio, visibilidad y claims. La diferenciación técnicamente defendible exige seguridad, límites de uso, subproductos, método de prueba y claims disciplinados.

### D4 — HVAC / conductos

Muestra core: 4 publicaciones.

Rango de precios observado:

```text
ARS 161.000 — 1.659.000
mediana aproximada: ARS 573.889
```

Patrón competitivo:

- oferta visible escasa;
- varios productos llegan por importación bajo demanda;
- IonFactor es el benchmark local más claro por 220V, garantía y especialización;
- Honeywell funciona como benchmark premium;
- la instalación y compatibilidad HVAC son parte estructural de la propuesta.

Lectura:

```text
SATURATION: BAJA
DEMAND SIGNAL: DÉBIL / ESPECIALIZADA
```

La baja densidad de oferta no se interpreta como una oportunidad automática: puede reflejar una categoría más técnica, con menor base de compradores y mayor fricción de instalación.

## 4. Patrones transversales

### 4.1 La oferta está fragmentada

No aparece un único competidor dominante en todo el territorio. La presión cambia por arquitectura:

```text
D1 → marcas locales + importados
D2 → marcas especializadas + marcas internacionales + importadores
D3 → fuerte presión low-ticket / marca-vendedor
D4 → pocos especialistas / importación bajo demanda
```

### 4.2 Mercado Libre mezcla competencia real con ruido de catálogo

Importadores generalistas publican productos 110V, de alto ticket y sin señal de ventas visible. Esos listados prueban disponibilidad comercial, pero no deben contarse con el mismo peso que una oferta local con stock, garantía, ventas y repuestos.

### 4.3 El precio no representa una escala de calidad

La dispersión observada responde a diferencias de mecanismo, tamaño, CADR, marca, instalación, importación, filtros, sensores y claims. No debe leerse como `más caro = mejor`.

### 4.4 Los claims forman parte de la competencia

Especialmente en D3, varios competidores venden mediante claims de desinfección, alergias, virus, bacterias, olores o grandes superficies. Smart Imports no debería tomar esa intensidad comercial como evidencia técnica.

## 5. Palancas competitivas detectadas

Sin seleccionar todavía una arquitectura o Product Base, F4 identifica palancas recurrentes:

```text
220–240 V / 50 Hz nativo
stock local real
filtros y consumibles disponibles
CADR / cobertura verificables
masa o capacidad de sorbente cuando aplique
claims separados por mecanismo
método de prueba identificable
garantía clara
manual/documentación en español
soporte posventa
instalación/compatibilidad resueltas cuando aplique
seguridad y subproductos explícitos
```

Estas palancas alimentan F5 — Potencial de Marca; no constituyen todavía una shortlist.

## 6. Evaluación en matriz

```text
EVAL-0018
Criterio: Competencia
Valor: 3/5
Confianza: Media
Soporte: EVID-0250
```

Racional:

- existe competencia real y marcas fuertes;
- D3 low-ticket presenta presión alta;
- D1/D2 no están vacíos, pero tampoco muestran una estructura uniformemente saturada;
- gran parte de la oferta premium es importada bajo demanda;
- D4 tiene baja saturación pero también baja señal de demanda y mayor complejidad;
- hay palancas claras de diferenciación no basadas sólo en precio.

Interpretación de la escala vigente:

```text
1 = saturado
5 = poca competencia
3 = oportunidad intermedia / competencia manejable pero material
```

## 7. Materialización y validación

Snapshot validado:

```text
matrix-aut49-brand-cand-003-phase4.xlsx
SHA-256: e8908e6ef56b05cb5ed24033301c49a2ce63e65134cf4678b87a95b379d92399
```

Registros agregados:

```text
Competencia ML   : COMP-0100 ... COMP-0119
Fuentes          : SRC-0388
Evidencias       : EVID-0250
Evaluaciones     : EVAL-0018
Evidencia Fuentes: EVSRC-0425 ... EVSRC-0445
```

Validación oficial:

```text
Application: Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

No se crean Product Bases en F4.

## 8. Gate

```text
F4 — CLOSED
→ F5 — Brand Potential / Potencial de Marca
→ AUTO
```

## 9. Changelog

### 2026-09-24 — v0.1.1

- `aut49` validada con Matrix Validator 0.1.0 / full-matrix-v5 0.7.0;
- resultado `PASS` limpio, sin errors, warnings, info ni limitations;
- SHA-256 confirmado `e8908e6ef56b05cb5ed24033301c49a2ce63e65134cf4678b87a95b379d92399`;
- F4 declarada formalmente `CLOSED`;
- próximo gate: `F5 — Potencial de Marca`, modalidad `AUTO`.
