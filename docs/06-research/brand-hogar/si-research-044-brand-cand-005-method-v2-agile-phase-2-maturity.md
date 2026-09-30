---
id: si-research-044
title: BRAND-CAND-005 — Method v2 Agile — F2 Maturity
description: Evaluación de madurez técnica y operativa de arquitecturas domésticas de compostaje y procesamiento de residuos orgánicos.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-28
updated: 2026-09-28
brand: brand-hogar
brand_candidate: brand-cand-005
method: method-v2-agile
phase: F2
---

# BRAND-CAND-005 — Method v2 Agile — F2 Maturity

Fecha: 2026-09-28  
Estado: `CLOSED`

## 1. Input vigente

F1 quedó formalmente cerrada sobre:

```text
matrix-aut74-brand-cand-005-phase1.xlsx
SHA-256: 9865eade972802b8be924d0647cf779a8e844cca408d6105cf4f5843289216de
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Arquitecturas evaluadas:

```text
A1 — compostaje aeróbico pasivo / estático
A2 — compostaje aeróbico giratorio / tumbler
A3 — vermicompostaje
A4 — bokashi / fermentación anaeróbica
A5 — procesador eléctrico térmico / triturador / deshidratador
A6 — procesador eléctrico biológico / in-vessel
```

`A7 — híbridos / multicámara` permanece como `DESIGN / TOPOLOGY LAYER`, no como arquitectura autónoma.

F2 evalúa **madurez técnica y operativa**. No evalúa todavía demanda local, competencia, potencial de marca, origen, landed cost, margen ni Product Bases.

## 2. Criterio de madurez

La madurez no equivale a popularidad ni a conveniencia comercial automática.

Se observa:

```text
PROCESS MATURITY
+ OUTPUT CLARITY / VERIFIABILITY
+ USER-PROCESS BURDEN
+ HARDWARE / BIOLOGICAL SYSTEM MATURITY
+ CONSUMABLE / SERVICE DEPENDENCY
+ MAINTENANCE / CLEANING
+ ELECTRICAL / MECHANICAL COMPLEXITY
+ CLAIM DISCIPLINE
```

Reglas:

```text
TECHNICALLY MATURE ≠ GOOD FIRST PRODUCT
FAST PROCESS ≠ MATURE COMPOST
LOW-TECH ≠ LOW USER FRICTION
ELECTRIC APPLIANCE ≠ SUPERIOR COMPOSTING
COMMERCIAL CLAIM ≠ VERIFIED OUTPUT
BIOLOGICAL PROCESS ≠ ZERO MAINTENANCE
```

## 3. Baseline técnico suficiente

### 3.1 Compostaje aeróbico doméstico

EPA describe el compostaje doméstico como una práctica establecida basada en equilibrio de carbono/nitrógeno, oxígeno y humedad. En sistemas bien mantenidos, el compost puede estar listo en aproximadamente tres a cinco meses y requiere una etapa de curado.

El manual argentino de compostaje domiciliario reconoce, incluso para espacios reducidos, contenedores estáticos y giratorios.

Lectura:

> El mecanismo es altamente maduro. La incertidumbre relevante no está en la ciencia básica sino en la disciplina de uso, espacio, mezcla, humedad, olores y tiempo.

### 3.2 Vermicompostaje

EPA y UC ANR describen sistemas domésticos simples, aptos para interior/exterior y espacios reducidos, con recipientes, bedding, lombrices y residuos compatibles.

Lectura:

> La tecnología es madura, pero funciona como sistema vivo: temperatura, humedad, alimentación y cuidado del medio biológico forman parte del producto real.

### 3.3 Bokashi

Washington State University describe Bokashi como fermentación anaeróbica en recipiente sellado con inoculante, con procesamiento rápido y aptitud para espacios pequeños.

Condición estructural:

```text
BOKASHI OUTPUT
=
PRE-COMPOST
≠
FINISHED COMPOST
```

El material debe enterrarse o incorporarse a otro sistema para completar la descomposición.

Lectura:

> Proceso maduro y operacionalmente simple, pero con consumible recurrente y post-proceso obligatorio.

### 3.4 Preprocesamiento eléctrico térmico

EPA distingue grinders/dehydrators residenciales de compostaje real: reducen peso y volumen, pero el output no es biológicamente estable y necesita compostaje, curado u otro tratamiento posterior.

Lectura:

> El hardware térmico/mecánico es comercialmente maduro como preprocesador; la madurez baja cuando se pretende sostener el claim `compost in hours`.

### 3.5 Procesamiento eléctrico biológico

Equipos como Reencle combinan mezcla, control ambiental y medio microbiano. La documentación comercial reciente confirma un proceso continuo y recomienda curar el material cosechado aproximadamente tres semanas antes de usarlo con plantas.

Lectura:

> La arquitectura es real y diferenciada, pero más sensible a mantenimiento, estabilidad del medio biológico, partes móviles, operación continua y validación del output.

## 4. Evaluación por arquitectura

### A1 — Compostaje aeróbico pasivo / estático

```text
MATURITY: HIGH — USER-PROCESS-SENSITIVE
```

Fortalezas:

- mecanismo biológico ampliamente establecido;
- hardware extremadamente simple;
- sin electricidad por defecto;
- pocas piezas;
- bajo service burden del producto físico;
- output técnicamente claro cuando el proceso se completa.

Condiciones:

- tiempo de meses;
- balance secos/húmedos;
- humedad;
- aireación;
- mezcla;
- espacio;
- posibles olores/plagas si se opera mal;
- necesidad de curado.

Lectura F2:

> Alta madurez técnica. El riesgo dominante es experiencia de uso, no tecnología.

### A2 — Compostaje aeróbico giratorio / tumbler

```text
MATURITY: HIGH — USER-PROCESS-SENSITIVE
```

Fortalezas:

- mismo mecanismo aeróbico maduro de A1;
- mezcla más cómoda;
- formato cerrado;
- aptitud para patios/balcones según diseño;
- baja complejidad eléctrica y postventa.

Condiciones:

- ejes, bisagras y estructura deben soportar carga;
- tamaño/volumen puede afectar logística;
- el giro no resuelve por sí mismo humedad, balance de materiales ni maduración;
- multicámara puede mejorar continuidad, no acelerar mágicamente la biología.

Lectura F2:

> Alta madurez. El diferencial es UX/topología más que ciencia del proceso.

### A3 — Vermicompostaje

```text
MATURITY: HIGH — LIVING-SYSTEM-SENSITIVE
```

Fortalezas:

- práctica doméstica establecida;
- apta para espacios pequeños;
- sin electricidad;
- output diferenciable: vermicompost/castings;
- mantenimiento relativamente simple una vez estabilizado.

Condiciones:

- organismo vivo;
- temperatura y humedad;
- restricciones de alimento;
- riesgo de sobrealimentación;
- cosecha/separación;
- usuario debe aceptar convivir con lombrices.

Lectura F2:

> Alta madurez, pero la aceptación y el cuidado del sistema vivo son condiciones comerciales relevantes.

### A4 — Bokashi / fermentación anaeróbica

```text
MATURITY: HIGH — POST-PROCESS / CONSUMABLE-SENSITIVE
```

Fortalezas:

- proceso simple y predecible;
- recipiente cerrado;
- baja energía;
- buena adaptación a espacios pequeños;
- acepta una gama de alimentos más amplia que compostaje aeróbico doméstico típico.

Condiciones:

- inoculante recurrente;
- drenaje de líquido;
- sellado correcto;
- material final ácido y activo;
- necesidad obligatoria de suelo o compostaje posterior.

Lectura F2:

> Alta madurez del proceso, pero propuesta incompleta si el usuario no dispone de una vía clara para el post-proceso.

### A5 — Procesador eléctrico térmico / deshidratador

```text
MATURITY: MEDIUM-HIGH — HARDWARE-MATURE / CLAIM-CONDITIONED
```

Fortalezas:

- principios de calentamiento, molienda, mezcla y secado maduros;
- fuerte reducción de masa/volumen;
- ciclo corto;
- operación indoor;
- conveniencia visible.

Condiciones:

- electricidad;
- resistencia/motor/ventilación;
- ruido;
- limpieza;
- filtros;
- capacidad por ciclo;
- desgaste;
- peso y volumen logístico;
- 220–240 V / 50 Hz;
- postventa;
- output no estable por defecto;
- alto riesgo de claim si se vende como compost terminado.

Lectura F2:

> Madurez alta del hardware, intermedia como solución de compostaje. Avanza a demanda como `PREPROCESSOR`, no como sustituto conceptual de A1–A4.

### A6 — Procesador eléctrico biológico / in-vessel

```text
MATURITY: MEDIUM — BIOLOGICAL / SERVICE / CLAIM-CONDITIONED
```

Fortalezas:

- combina automatización con biodegradación real;
- puede admitir alimentación frecuente;
- menor esfuerzo manual que sistemas pasivos;
- propuesta indoor diferenciada.

Condiciones:

- medio microbiano vivo;
- continuidad operacional;
- control térmico/aireación/agitación;
- partes móviles;
- limpieza;
- consumo eléctrico;
- capacidad diaria;
- recuperación ante desequilibrios;
- olor;
- soporte;
- eventual consumible o reposición del medio;
- curado/maduración del output;
- evidencia de estabilidad.

Lectura F2:

> Arquitectura prometedora pero menos madura operacionalmente para una primera importación: concentra complejidad de electrodoméstico + sistema biológico + claim de output.

## 5. Matriz comparativa de madurez

| Arquitectura | Madurez | Fortaleza dominante | Condición dominante |
|---|---|---|---|
| A1 Aeróbica estática | `HIGH` | simplicidad + proceso establecido | fricción de uso / tiempo |
| A2 Tumbler | `HIGH` | UX de mezcla + baja complejidad | tamaño / estructura / proceso |
| A3 Vermicompost | `HIGH` | compacta + output claro | sistema vivo / aceptación |
| A4 Bokashi | `HIGH` | cerrada + rápida + amplia entrada | consumible + post-proceso |
| A5 Térmica/deshidratador | `MEDIUM-HIGH` | conveniencia + reducción rápida | electricidad / partes / claim |
| A6 Biológica in-vessel | `MEDIUM` | automatización + biodegradación | service / biología / claim |

## 6. Implicación para una primera etapa de importación

F2 no elimina arquitecturas sólo por complejidad. Sí registra el sesgo operativo de Smart Imports:

```text
A1 / A2
→ baja complejidad técnica y regulatoria del producto
→ mayor fricción de proceso para el usuario

A3
→ baja complejidad eléctrica
→ dependencia de organismo vivo y aceptación del usuario

A4
→ baja complejidad del hardware
→ dependencia de consumible + post-proceso

A5
→ conveniencia alta
→ mayor logística, electricidad, partes móviles, filtros y claim-risk

A6
→ conveniencia potencial alta
→ mayor service burden + sistema biológico + evidencia del output
```

Esto **no es shortlist**. F3 debe observar demanda real por arquitectura antes de inferir qué fricciones acepta el mercado local.

## 7. Gate F2

Pregunta:

> ¿La madurez técnica y operativa de A1–A6 está suficientemente entendida como para iniciar demanda local sin confundir madurez del mecanismo con atractivo comercial?

Resultado conceptual:

```text
PASS
```

Razón:

- A1–A4 tienen procesos maduros y riesgos de uso claramente identificables;
- A5 queda separado como preprocesador de hardware maduro pero claim-sensitive;
- A6 queda como arquitectura biológica automatizada de madurez operacional intermedia;
- se identifican consumibles, post-proceso, electricidad, partes móviles, mantenimiento y service burden;
- no existe una incertidumbre técnica F2 que obligue a ampliar investigación antes de F3.

## 8. Materialización en matriz

Baseline validada:

```text
matrix-aut74-brand-cand-005-phase1.xlsx
SHA-256: 9865eade972802b8be924d0647cf779a8e844cca408d6105cf4f5843289216de
Result: PASS
```

F2 mantiene `MATRIX_SCOPE_ALIAS` ID 35 y actualiza:

- F1 a `CLOSED`;
- madurez por arquitectura A1–A6;
- A7 continúa como `DESIGN / TOPOLOGY LAYER`;
- próxima acción `F3 — Demand`;
- ruta documental `SI-RESEARCH-044`;
- estado F2 pendiente del Matrix Validator.

Archivo preparado:

```text
matrix-aut75-brand-cand-005-phase2.xlsx
SHA-256: 71548058212577e02933ebd5c3377a1b18617a0195507e3626b4fa0558b6869e
```

## 9. Estado formal de F2

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut75
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
SHA-256: 71548058212577e02933ebd5c3377a1b18617a0195507e3626b4fa0558b6869e
```

F3 queda formalmente abierta después de este cierre.

## 10. Próxima acción

Después de `aut75 PASS`, abrir `F3 — Demand` en modalidad `COLLABORATIVE`.

La recolección debe separar claramente:

```text
PUBLICACIONES
≠
DEMANDA

UNIDADES VENDIDAS / TRACCIÓN
≠
NÚMERO DE LISTINGS

MISMA ARQUITECTURA CON MUCHAS MARCAS
≠
MUCHOS PRODUCTOS BASE
```

## 11. Fuentes públicas utilizadas

1. U.S. EPA — *Composting At Home*  
   https://www.epa.gov/recycle/composting-home

2. U.S. EPA — *Approaches to Composting*  
   https://www.epa.gov/sustainable-management-food/approaches-composting

3. U.S. EPA — *Composting*  
   https://www.epa.gov/sustainable-management-food/composting

4. Argentina.gob.ar — *Manual de compostaje domiciliario*  
   https://www.argentina.gob.ar/sites/default/files/2021/12/anexo_22._manual_de_compost_domiciliario_opds.pdf

5. Argentina.gob.ar / INTA AMBA — *Compost: cómo transformar residuos orgánicos en abono*  
   https://www.argentina.gob.ar/noticias/compost-como-transformar-residuos-organicos-en-abono

6. Washington State University Extension — *Bokashi Composting*  
   https://extension.wsu.edu/kitsap/bokashi-composting/

7. UC Agriculture and Natural Resources — *Vermicomposting & Vermiculture*  
   https://ucanr.edu/site/uc-master-gardeners-orange-county/vermicomposting-vermiculture-orange-county

8. Reencle Help Center — *How Does the 30-Day Composting Process Work?*  
   https://help.reencle.co/en-US/how-does-the-30-day-composting-process-work-8068332

9. Reencle Help Center — *Why Should I Cure Reencle Compost Before Using It?*  
   https://help.reencle.co/en-US/why-should-i-cure-reencle-compost-before-using-it-8073388

Las fuentes de fabricante describen funcionamiento y claims declarados; no sustituyen validación independiente del output.

## 12. Changelog

### 2026-09-28 — v0.1.0

- F1 queda formalmente cerrada sobre `aut74 PASS`;
- se evalúa madurez A1–A6;
- A1–A4 quedan `HIGH` con distintas sensibilidades operativas;
- A5 queda `MEDIUM-HIGH — HARDWARE-MATURE / CLAIM-CONDITIONED`;
- A6 queda `MEDIUM — BIOLOGICAL / SERVICE / CLAIM-CONDITIONED`;
- se materializa `matrix-aut75-brand-cand-005-phase2.xlsx`;
- `aut75` obtiene PASS limpio y F2 queda formalmente `CLOSED`;
- siguiente fase: `F3 — Demand` en modalidad `COLLABORATIVE`.
