---
id: si-brand-001
title: Reusable Brand System and Home Brand Territory
description: Define el Brand System reutilizable de Smart Imports y su primera implementación real como Marca Hogar.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-16
updated: 2026-09-16
tags:
  - brand
  - brand-system
  - portfolio
  - missions
  - home
  - brand-fit
related:
  - si-brand-002
  - si-decision-016
  - si-roadmap-002
  - si-agent-001
audience:
  - founder
  - partner
  - assistant
phase: brand-strategy
---

# SI-BRAND-001 — Brand System reutilizable y territorio de Marca Hogar

> La marca no debe decirnos qué producto comprar. Debe decirnos qué problemas queremos ser reconocidos por resolver.

## 1. Propósito

Este documento define:

1. un **Brand System reutilizable** para Smart Imports;
2. la primera implementación real de ese sistema: **Marca Hogar v0.1**;
3. la arquitectura de portfolio basada en **misiones y problemas**, no en categorías comerciales;
4. los límites conceptuales que protegen la coherencia de la marca;
5. la separación entre `Brand Fit` y `Method v2`.

No define todavía:

- nombre comercial;
- logo;
- identidad visual;
- slogan público;
- proveedores;
- productos finales;
- decisión de importación.

## 2. Por qué existe un Brand System

Smart Imports necesita evitar dos extremos:

1. encontrar productos comercialmente atractivos y terminar construyendo un portfolio incoherente;
2. enamorarse de una narrativa de marca y forzar productos que no constituyen un negocio defendible.

Por eso se separan dos preguntas:

```text
BRAND FIT
¿Queremos que nuestra marca venda este producto?

METHOD V2
¿Existe realmente un negocio defendible alrededor de este producto?
```

Ninguna sustituye a la otra.

## 3. Arquitectura reusable

La arquitectura general adoptada es:

```text
BRAND
  ↓
BRAND TERRITORY
  ↓
MISSIONS
  ↓
PROBLEMS
  ↓
SOLUTIONS
  ↓
BRAND CANDIDATE SCREENING
  ↓
CANDIDATOS APROBADOS
  ↓
METHOD V2
  ↓
PRODUCT BASES / OPORTUNIDADES EVALUADAS
```

### 3.1 Brand

Es la instancia concreta de una propuesta de mercado.

### 3.2 Brand Territory

Define el espacio estratégico en el que la marca decide jugar.

Debe ser suficientemente amplio para permitir crecimiento, pero suficientemente restrictivo para excluir productos que requieran una explicación artificial.

### 3.3 Missions

Las misiones expresan **qué mejora busca producir la marca**.

No son categorías de marketplace.

Ejemplo incorrecto:

```text
Electrodomésticos
Mascotas
Smart Home
Cocina
```

Ejemplo correcto:

```text
Mejorar condiciones del hogar
Usar mejor los recursos
Reducir y gestionar residuos
Resolver problemas domésticos recurrentes conectados con el núcleo
```

### 3.4 Problems

Cada misión se descompone en problemas concretos y reconocibles.

### 3.5 Solutions

Una solución es una familia conceptual que intenta resolver un problema.

Todavía no es necesariamente un `Product Base`.

### 3.6 Product Base

Cuando Method v2 profundiza y normaliza la solución pueden aparecer una o más arquitecturas/configuraciones comercialmente significativas.

Por lo tanto:

```text
SOLUTION ≠ PRODUCT BASE
```

Ejemplo:

```text
SOLUTION
Detección y prevención de fugas

→ PRODUCT BASE A
Sensor puntual + válvula

→ PRODUCT BASE B
Monitor de caudal central + válvula

→ PRODUCT BASE C
Sistema basado en presión/acústica + corte
```

## 4. El sistema debe ser reutilizable

`Marca Hogar` es la primera implementación.

El Brand System no debe quedar acoplado a Hogar.

Una futura marca podría reutilizar exactamente el mismo patrón:

```text
MARCA FITNESS
  ↓
TERRITORIO PROPIO
  ↓
MISIONES PROPIAS
  ↓
PROBLEMAS
  ↓
SOLUCIONES
  ↓
BRAND CANDIDATE SCREENING
  ↓
METHOD V2
```

Ejemplo conceptual, no decisión vigente:

```text
Territorio:
mejorar la práctica física de forma consistente

Misiones posibles:
- entrenar;
- recuperar;
- medir;
- progresar;
- sostener el hábito.
```

El ejemplo `Mundo Fitness` se conserva deliberadamente para demostrar que la arquitectura no depende del dominio Hogar.

## 5. Primera implementación — Marca Hogar v0.1

### 5.1 Nombre de trabajo

```text
Marca Hogar
```

Es un identificador interno.

No es un nombre comercial ni condiciona el naming futuro.

### 5.2 Descriptor interno

> **Un hogar que funciona mejor.**

El descriptor sirve para orientar decisiones internas.

No se adopta como slogan comercial.

### 5.3 Territorio

> **Marca Hogar desarrolla y selecciona soluciones que mejoran de forma tangible cómo funciona el hogar: sus condiciones ambientales, el uso de recursos y la gestión de residuos y problemas domésticos recurrentes.**

La marca se mantiene deliberadamente centrada en el hogar.

Por ahora no se extiende a consumo responsable general fuera del hogar. La experiencia futura podrá justificar una expansión, pero esa expansión deberá decidirse explícitamente.

## 6. Principios del territorio

### 6.1 La tecnología es un medio, no el propósito

Un producto no obtiene Brand Fit por tener:

- Wi-Fi;
- aplicación;
- sensores;
- IA;
- automatización;
- conectividad.

La tecnología debe contribuir al resultado.

```text
SMART ≠ BRAND FIT
```

### 6.2 La mejora debe ser tangible

Conveniencia no equivale automáticamente a mejora.

Ejemplo:

```text
"puedo encenderlo desde el celular"
```

no es suficiente.

En cambio:

```text
"detecta una fuga y corta el suministro"
```

representa una intervención tangible sobre un problema.

### 6.3 El vínculo debe ser central

No alcanza con un beneficio accesorio.

Una cafetera puede consumir menos agua o energía, pero su razón principal de existencia continúa siendo preparar café.

La relación con el territorio debe estar conectada con la función central de la solución.

### 6.4 La mejora debería poder sostenerse con evidencia

La marca debe favorecer claims que puedan eventualmente demostrarse.

Ejemplos:

- reducción de consumo;
- detección de pérdida;
- filtración;
- control de humedad;
- reducción de volumen de residuos;
- eliminación o reducción de determinados contaminantes bajo condiciones documentadas.

Se evita usar `sustentable`, `saludable` o `responsable` como justificaciones genéricas sin evidencia.

### 6.5 El territorio debe ser capaz de excluir

Una arquitectura que permite justificar cualquier producto no aporta identidad.

La prueba central es:

> **¿Este producto entra naturalmente dentro de la marca o tenemos que inventar una explicación para justificarlo?**

Cuando la explicación se vuelve artificial, se encontró un límite.

## 7. Misiones de Marca Hogar v0.1

### 7.1 Misión 1 — Mejorar las condiciones del hogar

Busca mejorar condiciones físicas relevantes del ambiente doméstico.

Puede incluir problemas relacionados con:

- calidad del aire;
- humedad;
- determinados contaminantes;
- calidad del agua utilizada en el hogar;
- olores cuando existe una intervención real sobre su causa;
- condiciones específicas de higiene vinculadas con el ambiente.

No convierte a la marca en una marca genérica de `wellness`.

Quedan fuera por defecto:

- masaje;
- fitness;
- sueño;
- ergonomía personal;
- cosmética;
- bienestar personal sin relación directa con el funcionamiento del hogar.

### 7.2 Misión 2 — Usar mejor los recursos

Busca medir, reducir, optimizar o evitar desperdicio de:

- agua;
- energía;
- consumibles domésticos;
- otros recursos relevantes cuando exista una relación directa y verificable.

Ejemplos conceptuales:

- detección de fugas;
- monitorización de consumo;
- optimización energética;
- control eficiente de climatización.

### 7.3 Misión 3 — Reducir y gestionar residuos

Busca mejorar la forma en que el hogar:

- reduce;
- separa;
- trata;
- reaprovecha;
- contiene;
- gestiona residuos.

Ejemplos conceptuales:

- compostaje;
- tratamiento de residuos orgánicos;
- reducción de volumen;
- soluciones que reduzcan determinados descartables.

El mero contacto con residuos no es suficiente.

Un tacho que sólo abre automáticamente no obtiene Brand Fit por ese motivo.

### 7.4 Misión 4 — Resolver problemas domésticos recurrentes conectados con el núcleo

Es una misión adyacente y deliberadamente restrictiva.

Permite incorporar soluciones que no encajan limpiamente en las tres misiones centrales, siempre que:

1. resuelvan un problema doméstico recurrente;
2. tengan conexión fuerte con ambiente, recursos, residuos o higiene;
3. la mejora sea central y tangible;
4. su aceptación no expanda el territorio de forma arbitraria.

`BASE-PET-003` es el caso de referencia conceptual:

```text
residuo biológico recurrente
+ higiene
+ olor
+ gestión doméstica
```

No entra por pertenecer a `Pet Care`.

Esto implica que un GPS para mascotas puede quedar fuera aunque pertenezca al mismo nicho comercial.

## 8. Núcleo, adyacencias y exclusiones

### 8.1 Núcleo

```text
CONDICIONES DEL HOGAR
RECURSOS
RESIDUOS
```

### 8.2 Adyacencias

Sólo se aceptan cuando están conectadas con el núcleo.

Ejemplo:

```text
higiene doméstica especializada
```

puede ser adyacente.

```text
limpieza general
```

no habilita automáticamente toda la categoría de electrodomésticos.

### 8.3 Exclusiones iniciales

Quedan fuera del territorio por defecto:

- seguridad personal o patrimonial;
- entretenimiento;
- decoración;
- wellness personal genérico;
- automatización por mera conveniencia;
- Pet Care genérico;
- Smart Home genérico;
- consumo responsable general fuera del hogar.

Una exclusión de Brand Fit no implica que el producto sea una mala oportunidad comercial.

## 9. Pruebas de frontera consolidadas

| Producto | Lectura de Brand Fit | Razón |
|---|---|---|
| Detector de fugas + corte | Natural | Interviene directamente sobre agua, desperdicio y prevención. |
| Purificador de aire | Natural | Modifica una condición ambiental central. |
| Compostera | Natural | Cambia la gestión de residuos. |
| Monitor energético | Natural | Interviene directamente sobre uso de energía. |
| `BASE-PET-003` | Adyacente defendible | Higiene + residuo + problema doméstico recurrente. |
| GPS para mascotas | Fuera | Ubicación/seguridad del animal no pertenece al núcleo. |
| Cámara Wi-Fi | Fuera | Seguridad patrimonial. |
| Cerradura inteligente | Fuera | Seguridad/acceso. |
| Tira LED RGB | Fuera | Decoración/entretenimiento. |
| Robot aspirador | Borde | Riesgo de abrir cleaning appliances genéricos. |
| Almohada ergonómica | Fuera | Wellness personal. |
| Botella reutilizable | Fuera por foco actual | Consumo responsable fuera del sistema hogar. |

## 10. Arquitectura de portfolio

El portfolio debe organizarse por misiones y problemas, no por taxonomías de marketplace.

Ejemplo:

| Producto | Categoría comercial | Misión de marca |
|---|---|---|
| Detector de fugas | Smart Home | Usar mejor los recursos |
| Purificador de aire | Calidad ambiental | Mejorar condiciones del hogar |
| Compostera | Gestión de residuos | Reducir y gestionar residuos |
| `BASE-PET-003` | Pet Care | Problemas domésticos recurrentes |

La diversidad de categorías comerciales no constituye incoherencia cuando existe una misión común y defendible.

## 11. Relación con Method v2

```text
BRAND SYSTEM
¿Dónde queremos jugar?

→ Brand Territory
→ Missions
→ Problems
→ Solutions
→ Brand Candidate Screening

METHOD V2
¿Dónde existe negocio?

→ Demand
→ Competition
→ Product Base normalization
→ Origin
→ Headroom
→ Minimum Landed Cost Dataset
→ Landed Cost Screen
→ Decision
```

El Brand System no modifica las reglas vigentes de Method v2.

`Brand Candidate Screening v0.1` se considera la primera forma operativa del futuro `Brand Product Filter`. La formalización de ese filtro deberá surgir de evidencia acumulada usando candidatos reales, no de reglas abstractas fijadas prematuramente.

## 12. Consecuencias futuras para Intelligence Engine

Sin modificar todavía matriz, schema ni Engine, se registran necesidades conceptuales potenciales:

```text
BRAND
BRAND_TERRITORY
MISSION
PROBLEM
SOLUTION
BRAND_FIT_EVALUATION
BRAND_TERRITORY_VERSION
```

`PRODUCT_BASE` deberá poder relacionarse tanto con evaluaciones de Method v2 como con evaluaciones de Brand Fit.

Ejemplo futuro:

```text
PRODUCT_BASE
├── METHOD_V2_EVALUATION
└── BRAND_FIT_EVALUATION
    └── BRAND_TERRITORY_VERSION
```

Esto permitiría consultas RAG del tipo:

> Encontrá Product Bases con demanda interesante, competencia favorable, Headroom suficiente y Brand Fit alto con una misión determinada.

Estas entidades son necesidades de modelado futuras, no cambios autorizados sobre `full-matrix-v5 0.7.0`.

## 13. Preguntas abiertas

- ¿Cuándo conviene convertir las misiones v0.1 en una taxonomía formal?
- ¿Qué evidencia mínima debe exigirse para considerar `Brand Credibility` validada?
- ¿Cómo versionar evaluaciones de Brand Fit cuando cambie el territorio?
- ¿Cuándo una adyacencia justifica convertirse en una misión propia?
- ¿Qué señal real justificaría expandir Marca Hogar fuera del hogar?

## 14. Documentos relacionados

- [SI-BRAND-002 — Brand Candidate Screening](./si-brand-002-brand-candidate-screening-method.md)
- [SI-DECISION-016 — Arquitectura de marca por misiones](../09-decision-log/si-decision-016-adopt-mission-based-brand-architecture-and-screening.md)
- [SI-ROADMAP-002 — Estado actual y handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)

## 15. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-16 | Primera definición del Brand System reusable y de Marca Hogar v0.1. |
