---
id: si-research-042
title: BRAND-CAND-005 — Method v2 Agile — Fase 0 — Research Brief
description: Research Brief para compostaje y procesamiento doméstico de residuos orgánicos dentro de Marca Hogar.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-28
updated: 2026-09-28
brand: brand-hogar
brand_candidate: brand-cand-005
method: method-v2-agile
phase: F0
---

# SI-RESEARCH-042 — BRAND-CAND-005 — Fase 0 — Research Brief

Fecha: 2026-09-28  
Estado: `CLOSED`

## 1. Candidato

**BRAND-CAND-005 — Compostaje / procesamiento doméstico de residuos orgánicos**

Misión de Marca Hogar: **Reducir y gestionar residuos**.

El candidato estudia soluciones domésticas capaces de recibir residuos orgánicos del hogar —principalmente restos de alimentos— y reducir, transformar, estabilizar o facilitar su valorización posterior.

La investigación no parte de la premisa de que toda solución comercializada como “compostera” produzca compost terminado.

## 2. Distinción conceptual obligatoria

```text
RESIDUO ORGÁNICO
→ MÉTODO / MECANISMO REAL
→ TRANSFORMACIÓN OBSERVABLE
→ OUTPUT REAL
→ TRATAMIENTO POSTERIOR NECESARIO
→ OUTCOME PARA EL USUARIO
→ CLAIM COMERCIAL
```

Reglas:

```text
REDUCCIÓN DE VOLUMEN ≠ COMPOSTAJE
DESHIDRATACIÓN / TRITURACIÓN ≠ COMPOST TERMINADO
FERMENTACIÓN ≠ COMPOST TERMINADO
PRE-COMPOST ≠ COMPOST MADURO
CONTROL DE OLOR ≠ HIGIENIZACIÓN VALIDADA
PROCESAMIENTO RÁPIDO ≠ ESTABILIZACIÓN BIOLÓGICA
RESIDUO CON ASPECTO DE TIERRA ≠ ENMIENDA VALIDADA
APP / AUTOMATIZACIÓN ≠ PROCESO DE COMPOSTAJE
```

La EPA define compostaje como descomposición biológica aeróbica gestionada y al compost como una enmienda biológicamente estable. También distingue explícitamente los procesadores residenciales que trituran o deshidratan residuos: reducen peso y volumen, pero su output no es compost estable por defecto.

## 3. Pregunta de investigación

> ¿Qué arquitecturas domésticas permiten gestionar residuos orgánicos de forma suficientemente limpia, simple, verificable y defendible para Marca Hogar —ya sea mediante compostaje real, fermentación, vermicompostaje o preprocesamiento— sin confundir reducción de volumen, deshidratación, fermentación o material “tipo tierra” con compost terminado?

## 4. Boundary

### Incluido

- uso doméstico;
- restos de alimentos y otros orgánicos domésticos compatibles;
- soluciones para cocina, balcón, patio o jardín;
- sistemas pasivos y activos;
- equipos mecánicos o eléctricos;
- sistemas con o sin consumibles recurrentes;
- soluciones cuyo output requiera una etapa posterior, siempre que esa dependencia quede explícita;
- soluciones destinadas a reducir volumen, olor, frecuencia de descarte o a generar una salida valorizable.

### Excluido

- plantas municipales o industriales;
- compostaje comercial de gran escala;
- biodigestores de escala no doméstica;
- trituración sanitaria conectada al desagüe como solución primaria;
- gestión de residuos sanitarios de mascotas, que pertenece a BRAND-CAND-006;
- residuos peligrosos, patogénicos o no domiciliarios;
- claims agronómicos, sanitarios o ambientales sin evidencia suficiente.

## 5. Arquitecturas iniciales

F0 abrió siete familias preliminares para F1:

```text
A1 — compostera aeróbica pasiva / estática
A2 — compostera aeróbica giratoria / tumbler
A3 — vermicompostera
A4 — bokashi / fermentación anaeróbica
A5 — procesador eléctrico por calor + trituración / deshidratación
A6 — procesador eléctrico biológico / microbial
A7 — sistemas híbridos / multicámara
```

La frontera entre arquitectura real, variante de diseño y futura Product Base se resuelve en F1–F6.

## 6. Evidencia de contexto

Fuentes oficiales argentinas describen compostaje doméstico en jardín, patio, terraza y espacios reducidos, incluyendo contenedores estáticos o giratorios. INTA AMBA informó en 2024 que aproximadamente el 50 % de los residuos sólidos urbanos corresponde a residuos orgánicos.

Esta relevancia material **no equivale a demanda comercial**.

## 7. Riesgos de investigación

1. Confundir naming comercial con mecanismo real.
2. Tomar reducción de volumen como prueba de compostaje.
3. Aceptar claims del fabricante sin evidencia independiente.
4. Comparar compostera pasiva y electrodoméstico sólo por precio.
5. Ignorar consumibles recurrentes.
6. Ignorar limpieza, mantenimiento, ruido y postventa.
7. Asumir que un output con apariencia de tierra es apto para plantas.
8. Evaluar “sustentabilidad” sin considerar electricidad, filtros, logística y destino final.
9. Crear Product Bases demasiado temprano.
10. Dejar que un producto visualmente atractivo arrastre la investigación.

## 8. Materialización y cierre de F0

Matriz preparada:

```text
matrix-aut73-brand-cand-005-phase0.xlsx
SHA-256: 6707bbcccf298f3249a97ed82cfe5b0494977766fb99ea5bddd695f9832f3c54
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
```

Estado:

```text
CONCEPTUAL ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut73
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F0 CLOSED
```

F1 queda formalmente abierta después de este cierre.

## 9. Fuentes públicas utilizadas

1. U.S. EPA — *Composting At Home*  
   https://www.epa.gov/recycle/composting-home

2. U.S. EPA — *Approaches to Composting*  
   https://www.epa.gov/sustainable-management-food/approaches-composting

3. Argentina.gob.ar — *Manual de compostaje domiciliario*  
   https://www.argentina.gob.ar/sites/default/files/2021/12/anexo_22._manual_de_compost_domiciliario_opds.pdf

4. Argentina.gob.ar / INTA AMBA — *Compost: cómo transformar residuos orgánicos en abono*  
   https://www.argentina.gob.ar/noticias/compost-como-transformar-residuos-organicos-en-abono

5. Washington State University Extension — *Bokashi Composting*  
   https://extension.wsu.edu/kitsap/bokashi-composting/

6. UC Agriculture and Natural Resources — *Vermicomposting & Vermiculture*  
   https://ucanr.edu/site/uc-master-gardeners-orange-county/vermicomposting-vermiculture-orange-county

7. Lomi — documentación pública de producto  
   https://lomi.com/products/lomi-3-food-recycler

8. Reencle — documentación pública de tecnología  
   https://reencle.co/pages/reencle-technology

Las fuentes de fabricantes se usan para identificar arquitecturas, funcionalidades y claims declarados; no constituyen validación independiente del resultado.

## 10. Changelog

### 2026-09-28 — v0.2.0

- `aut73` obtiene PASS limpio;
- se registra SHA-256 final;
- F0 queda formalmente `CLOSED`;
- se abre `F1 — Market / Solution Map` en modalidad `AUTO`.
