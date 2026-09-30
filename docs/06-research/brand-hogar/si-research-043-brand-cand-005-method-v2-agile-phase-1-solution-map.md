---
id: si-research-043
title: BRAND-CAND-005 — Method v2 Agile — F1 Market / Solution Map
description: Mapa de arquitecturas comercialmente significativas para compostaje y procesamiento doméstico de residuos orgánicos.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-28
updated: 2026-09-28
brand: brand-hogar
brand_candidate: brand-cand-005
method: method-v2-agile
phase: F1
---

# BRAND-CAND-005 — Method v2 Agile — F1 Market / Solution Map

Fecha: 2026-09-28  
Estado: `CLOSED`

## 1. Input vigente

F0 quedó formalmente cerrada sobre:

```text
matrix-aut73-brand-cand-005-phase0.xlsx
SHA-256: 6707bbcccf298f3249a97ed82cfe5b0494977766fb99ea5bddd695f9832f3c54
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Pregunta de continuidad:

> **¿Qué arquitecturas domésticas de gestión de residuos orgánicos son comercialmente significativas y materialmente distintas como para merecer evaluación de madurez, sin confundir formato del recipiente, automatización, reducción de volumen o naming comercial con el proceso real y el output obtenido?**

F1 no evalúa todavía demanda local, competencia, origen, landed cost, margen ni selección de Product Bases.

## 2. Principio de normalización

La unidad correcta del mapa no es la etiqueta `smart composter`, `food recycler`, `electric composter`, `fertilizer maker` ni `odorless bin`.

Se normaliza mediante:

```text
INPUT ACEPTADO
→ PROCESO / MECANISMO REAL
→ CONDICIONES DE OPERACIÓN
→ TRANSFORMACIÓN OBSERVABLE
→ OUTPUT REAL
→ POST-PROCESO NECESARIO
→ USER WORK / SERVICE CONSEQUENCES
→ CLAIM DEFENDIBLE
```

Reglas:

```text
REDUCCIÓN DE VOLUMEN ≠ COMPOSTAJE
DRY / GRIND ≠ COMPOST
FERMENTACIÓN ≠ COMPOST TERMINADO
PRE-COMPOST ≠ COMPOST MADURO
CONTENEDOR MULTICÁMARA ≠ PROCESO NUEVO
APP / SENSOR ≠ ARQUITECTURA DE TRATAMIENTO
RÁPIDO ≠ BIOLÓGICAMENTE ESTABLE
```

La EPA define compost como un producto biológicamente estable de descomposición aeróbica gestionada y señala que los procesadores residenciales que trituran/deshidratan generan una mezcla que requiere tratamiento posterior. Esa distinción es el eje de normalización de F1.

## 3. Ejes del mapa

### 3.1 Proceso dominante

```text
P1 — biodegradación aeróbica gestionada
P2 — biodegradación con lombrices + microbiota
P3 — fermentación anaeróbica
P4 — preprocesamiento térmico / mecánico
P5 — biodegradación controlada in-vessel con asistencia eléctrica
```

### 3.2 Output

```text
O1 — compost maduro / estable
O2 — vermicompost / castings
O3 — material fermentado / pre-compost
O4 — mezcla seca / triturada / deshidratada
O5 — output biológicamente procesado cuyo grado de estabilidad debe demostrarse
```

### 3.3 Carga operativa del usuario

- separación de inputs;
- balance de materiales;
- aireación / volteo;
- control de humedad;
- manejo de lixiviado;
- incorporación de inoculante;
- alimentación y cuidado de organismos;
- limpieza;
- retiro / maduración / curado;
- consumo eléctrico;
- filtros, aditivos o consumibles.

## 4. Arquitecturas normalizadas

### A1 — Compostaje aeróbico pasivo / estático

```text
Process: P1
Typical output: O1 después de tiempo y maduración suficientes
Energy: no eléctrica por defecto
User work: medio/alto
```

Contenedor, pila o módulo ventilado donde microorganismos descomponen materiales con oxígeno, humedad y relación adecuada entre materiales ricos en carbono y nitrógeno.

Variables estructurales:

- ventilación;
- drenaje/lixiviados;
- volumen;
- relación secos/húmedos;
- frecuencia de mezcla;
- clima / ubicación;
- tiempo de maduración;
- control de olores y plagas mediante operación correcta.

Lectura F1:

> Arquitectura núcleo de compostaje real, técnicamente simple y de baja complejidad de producto, pero con mayor carga de aprendizaje y operación para el usuario.

### A2 — Compostaje aeróbico giratorio / tumbler

```text
Process: P1
Mixing architecture: tambor rotatorio / volteo simplificado
Typical output: O1 después de proceso + maduración
Energy: manual por defecto
User work: medio
```

Comparte la biología de A1, pero el recipiente giratorio cambia de forma material la experiencia de mezcla, aislamiento del suelo, ergonomía y control del proceso.

El manual argentino de compostaje domiciliario reconoce contenedores estáticos y giratorios como soluciones domésticas para espacios reducidos.

Lectura F1:

> Se conserva separada en F1 por su arquitectura de operación y UX, aunque F6 deberá decidir si justifica una Product Base distinta o sólo una variante del compostaje aeróbico.

### A3 — Vermicompostaje

```text
Process: P2
Typical output: O2
Energy: no eléctrica por defecto
User work: medio
Living system: sí
```

Usa lombrices —habitualmente red wigglers— y microbiota asociada para procesar residuos compatibles. Puede operar en recipientes compactos y es viable en espacios reducidos.

Variables estructurales:

- especie/población de lombrices;
- cama;
- temperatura;
- humedad;
- ventilación;
- carga diaria;
- restricciones de alimento;
- cosecha del vermicompost;
- manejo de exceso de humedad.

Lectura F1:

> Arquitectura biológica diferenciada por organismo, restricciones de input, cuidado y tipo de output. Avanza a F2.

### A4 — Bokashi / fermentación anaeróbica

```text
Process: P3
Typical output: O3
Energy: no eléctrica por defecto
Consumable: inoculante / bran
Post-process: obligatorio
```

Sistema sellado que fermenta residuos mediante inoculante microbiano. Washington State University describe el resultado como `pre-compost`: no es compost terminado y debe enterrarse o incorporarse a otro sistema para completar la descomposición.

Variables estructurales:

- hermeticidad;
- inoculante;
- compactación;
- drenaje de líquido;
- tiempo de fermentación;
- necesidad de suelo/compost posterior;
- aceptación de alimentos que otros sistemas suelen excluir.

Lectura F1:

> Arquitectura comercial claramente diferenciada por fermentación, consumible recurrente y post-proceso obligatorio. Avanza a F2.

### A5 — Procesador eléctrico térmico / triturador / deshidratador

```text
Process: P4
Typical output: O4
Energy: eléctrica
User work: bajo/medio
Post-process: normalmente necesario para claim de compost
```

Equipo de cocina que aplica calor, trituración, mezcla y circulación de aire para reducir humedad, peso y volumen.

La EPA establece explícitamente que los procesadores residenciales de este tipo **no producen compost** por el solo hecho de triturar/deshidratar; su material debe compostarse, curarse o tratarse posteriormente. Lomi, como ejemplo comercial, describe su propio output como `pre-compost`.

Variables estructurales:

- tiempo de ciclo;
- reducción de masa/volumen;
- potencia y consumo;
- ruido;
- capacidad;
- filtros;
- olor;
- limpieza;
- resistencia, motor y partes móviles;
- 220–240 V / 50 Hz;
- destino real del output.

Lectura F1:

> Arquitectura de alta conveniencia y claim-risk elevado. Mantener separada de compostaje real. Avanza a F2 como `PREPROCESSOR`.

### A6 — Procesador eléctrico biológico / in-vessel

```text
Process: P5
Declared output: O5
Energy: eléctrica
Living microbial system: sí
User work: bajo/medio
```

Equipo cerrado que combina mezcla, aireación, control térmico y una comunidad microbiana para degradar residuos de forma continua o semiconsolidada.

Reencle declara una arquitectura basada en mezcla + microorganismos Bacillus y comercializa el resultado como compost. En Method v2 esa etiqueta **no basta**: F2–F6 deberán verificar tiempo, estabilidad, necesidad de maduración, comportamiento del sistema biológico, inputs permitidos y evidencia independiente del output.

Variables estructurales:

- cultivo/inóculo;
- capacidad diaria;
- temperatura;
- aireación;
- agitación;
- humedad;
- continuidad del proceso;
- retiro/cosecha;
- mantenimiento;
- consumo eléctrico;
- olor;
- partes móviles;
- reemplazo o recuperación del medio biológico;
- documentación del output.

Lectura F1:

> Arquitectura diferenciada y potencialmente atractiva por conveniencia, pero de alta complejidad técnica, postventa y de evidencia. Avanza a F2 condicionada.

## 5. A7 de F0 — híbridos / multicámara

F0 abrió provisionalmente:

```text
A7 — sistemas híbridos / multicámara
```

F1 concluye que **multicámara no constituye una arquitectura independiente por sí sola**.

Puede ser:

- dos cámaras estáticas A1;
- dos tambores A2;
- módulo de fermentación A4;
- cámara de proceso + maduración;
- combinación de preprocesamiento A5 con etapa biológica posterior;
- topología interna de A6.

Regla:

```text
TOPOLOGÍA / NÚMERO DE CÁMARAS
≠
MECANISMO DE TRATAMIENTO
```

Por lo tanto A7 queda como `DESIGN / TOPOLOGY LAYER` y no avanza a F2 como familia autónoma.

## 6. Capas que NO crean una arquitectura independiente

### App / conectividad / sensor

Pueden mostrar estado, programar ciclos o avisar mantenimiento, pero no cambian por sí solas el proceso real.

### Filtro de carbón / control de olor

Es una capa de experiencia o mantenimiento. No convierte un deshidratador en compostera.

### “Fertilizer maker”

Es un claim comercial. Debe probarse qué material produce y qué tratamiento posterior requiere.

### Velocidad de ciclo

Un ciclo de horas puede ser comercialmente valioso, pero no demuestra estabilidad biológica.

### Multicámara

Es topología física; sólo cambia arquitectura cuando las cámaras implementan procesos materialmente distintos.

## 7. Soluciones adyacentes fuera del mapa principal

- trituradores de residuos conectados a desagüe;
- biodigestión doméstica orientada principalmente a biogás;
- compostaje institucional/comercial de mayor escala;
- contenedores de basura sin tratamiento;
- bolsas compostables;
- trituradoras de jardín cuyo job principal sea reducción de ramas;
- gestión de residuos de mascotas, reservada a BRAND-CAND-006.

Pueden reaparecer como comparables o restricciones, no como Product Bases automáticas.

## 8. Aprendizaje estructural de F1

El espacio comercial puede representarse como:

```text
SOLUTION ARCHITECTURE
=
PROCESS / MECHANISM
+
INPUT ENVELOPE
+
OPERATING CONDITIONS
+
REAL OUTPUT
+
POST-PROCESS
+
USER WORK
+
ENERGY / CONSUMABLE DEPENDENCY
```

Esto evita:

```text
SMART FEATURE → PRODUCT BASE
DRY DIRT-LIKE OUTPUT → COMPOST
MULTICHAMBER → NUEVO PROCESO
FAST CYCLE → MATURE COMPOST
ODOR FILTER → HYGIENIZATION
```

La frontera formal de Product Base se resolverá en F6.

## 9. Qué deberá medir F2 — Maturity

Para cada arquitectura A1–A6:

- madurez técnica del mecanismo;
- madurez comercial;
- estabilidad y claridad del output;
- tiempo de proceso;
- inputs aceptados/restringidos;
- espacio necesario;
- carga operativa del usuario;
- olores, plagas y lixiviados;
- consumibles;
- dependencia eléctrica;
- partes móviles;
- limpieza/mantenimiento;
- complejidad de importación;
- postventa;
- riesgo de claims;
- evidencia independiente disponible.

## 10. Gate F1

Pregunta:

> ¿Existe un mapa suficientemente discriminante para evaluar madurez sin confundir formato, marketing, automatización o reducción de volumen con compostaje y output estable?

Resultado conceptual:

```text
PASS
```

Razón:

- se separaron cinco procesos dominantes;
- se distinguieron compost, vermicompost, pre-compost, mezcla seca y output biológico condicionado;
- se aisló el post-proceso como parte estructural de la solución;
- se separaron sistemas eléctricos de preprocesamiento y sistemas eléctricos biológicos;
- se normalizó multicámara como topología y no como mecanismo;
- se preservaron carga de usuario, consumibles, energía y service layer como ejes para F2.

## 11. Materialización en matriz

Baseline validada:

```text
matrix-aut73-brand-cand-005-phase0.xlsx
SHA-256: 6707bbcccf298f3249a97ed82cfe5b0494977766fb99ea5bddd695f9832f3c54
Result: PASS
```

F1 no crea Product Bases ni evidencia comercial artificial. Actualiza `MATRIX_SCOPE_ALIAS` ID 35 para registrar:

- F0 `CLOSED`;
- mapa normalizado A1–A6;
- A7 como `DESIGN / TOPOLOGY LAYER`;
- siguiente gate `F2 — Maturity`;
- ruta documental `SI-RESEARCH-043`;
- estado de F1 pendiente de Matrix Validator.

Archivo preparado:

```text
matrix-aut74-brand-cand-005-phase1.xlsx
SHA-256: 9865eade972802b8be924d0647cf779a8e844cca408d6105cf4f5843289216de
```

## 12. Estado formal de F1

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut74
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
SHA-256: 9865eade972802b8be924d0647cf779a8e844cca408d6105cf4f5843289216de
```

F2 queda formalmente abierta después de este cierre.

## 13. Fuentes públicas utilizadas

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

8. Lomi — *Lomi 3 Food Recycler*  
   https://lomi.com/products/lomi-3-food-recycler

9. Reencle — *Reencle Technology*  
   https://reencle.co/pages/reencle-technology

Las fuentes de fabricante describen funcionamiento y claims declarados; no sustituyen validación independiente del output.

## 14. Changelog

### 2026-09-28 — v0.1.0

- F0 queda formalmente cerrada sobre `aut73 PASS`;
- se normalizan seis arquitecturas A1–A6;
- A7 híbrida/multicámara se reclasifica como capa de diseño/topología;
- se separa preprocesamiento térmico de tratamiento biológico;
- se incorpora explícitamente el `post-process` al mapa;
- se materializa `matrix-aut74-brand-cand-005-phase1.xlsx`;
- `aut74` obtiene PASS limpio y F1 queda formalmente `CLOSED`;
- siguiente fase: `F2 — Maturity` en `AUTO`.
