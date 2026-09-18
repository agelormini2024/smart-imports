---
id: si-research-007
title: BRAND-CAND-001 — Golden Run Method v2 — Fases 0 a 6
description: Recorrido de referencia de Method v2 desde un Brand Candidate aprobado hasta Product Bases normalizados y materialización en matriz.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-18
updated: 2026-09-18
tags:
  - smart-imports
  - method-v2
  - golden-run
  - brand-hogar
  - brand-cand-001
  - water-leak
  - phase-0-to-6
related:
  - brand-cand-001
  - si-brand-001
  - si-brand-002
  - si-roadmap-002
phase: business-intelligence
---

# BRAND-CAND-001 — Golden Run Method v2 — Fases 0 a 6

> Objetivo de esta ejecución: validar de punta a punta la unión `Brand System → Method v2` sobre una oportunidad comercial real y, al mismo tiempo, producir un checkpoint suficientemente explícito para que una futura automatización no tenga que reconstruir decisiones implícitas.

## 1. Input de negocio

```text
Candidate ID: BRAND-CAND-001
Brand: brand-hogar
Candidate: Detección de fugas + corte automático
Decision: PASS TO METHOD V2
Primary Mission: Usar mejor los recursos
Secondary Mission: Resolver problemas domésticos recurrentes
```

Fuente oficial del input:

```text
docs/07-brand/brands/brand-hogar/candidates/brand-cand-001-water-leak-detection-and-shutoff.md
```

La unidad de entrada de Method v2 es el **Brand Candidate / Solution**, no un Product Base predefinido.

## 2. Regla de idioma de salida

Todos los outputs humanos de Method v2 deben redactarse en español.

Los términos técnicos canónicos, IDs, metadata y valores internos pueden conservarse en inglés cuando corresponda. En cuadros, diagramas y flujos destinados a lectura humana, el término técnico debe acompañarse con traducción al español entre paréntesis.

Ejemplo:

```text
PRODUCT BASE (PRODUCTO BASE)
SHORTLIST (LISTA CORTA)
ORIGIN SCREENING (EVALUACIÓN DE ORIGEN)
```

## 3. Contrato de interacción observado

La Golden Run confirma tres clases de ejecución:

```text
AUTO (AUTOMÁTICO)
→ investigación pública, normalización, análisis y documentación

COLLABORATIVE (COLABORATIVO)
→ Mercado Libre, selección de publicaciones, revisión visual y captura de PDFs

EXTERNAL (EXTERNO)
→ proveedores, documentos privados, despachante, certificaciones y decisión de capital
```

Fases 0–6 observadas:

| Fase | Nombre | Tipo de ejecución | Gate humano nuevo |
|---|---|---|---|
| 0 | Research Brief (Brief de investigación) | AUTO | No |
| 1 | Market / Solution Map (Mapa de mercado / soluciones) | AUTO | No |
| 2 | Maturity (Madurez) | AUTO | No |
| 3 | Demand (Demanda) | COLLABORATIVE | Sí — Mercado Libre |
| 4 | Competition (Competencia) | AUTO + evidencia colaborativa reutilizada | No |
| 5 | Brand Potential (Potencial de marca) | AUTO | No |
| 6 | Product Bases (Productos Base) | AUTO | No |

## 4. Fase 0 — Research Brief (Brief de investigación)

Pregunta central:

> ¿Qué arquitecturas concretas resuelven suficientemente bien la detección y prevención de fugas domésticas de agua y alrededor de cuáles puede existir un negocio defendible?

No se parte de “un sensor Wi-Fi” ni de una marca concreta.

Hipótesis iniciales:

- existen múltiples arquitecturas;
- detectar no equivale a cortar;
- el corte automático aumenta complejidad de instalación y postventa;
- la instalación puede ser una dimensión comercial estructural;
- conectividad y app son atributos, no la propuesta de valor principal.

## 5. Fase 1 — Market / Solution Map (Mapa de mercado y arquitecturas)

Arquitecturas identificadas:

```text
A1 — sensores puntuales + válvula central en línea
A2 — sensores puntuales + actuador retrofit sobre válvula existente
A3 — monitor hidráulico integral + válvula central
A4 — sistema híbrido integral + sensores distribuidos + válvula central
A5 — protección específica de artefacto
A6 — monitor integral sin corte automático [solución parcial]
```

Hallazgo adicional posterior:

```text
POINT SENSOR + ALERT
(SENSOR PUNTUAL + ALERTA)
```

sin corte automático, relevante como solución parcial/benchmark.

Aprendizaje estructural:

```text
Solution Architecture (Arquitectura de solución)
=
Detection Architecture (Arquitectura de detección)
+
Shutoff Architecture (Arquitectura de corte)
+
Installation Architecture (Arquitectura de instalación)
```

Conectividad (`Wi-Fi`, `Zigbee`, `LoRa`, `Matter`) no crea por sí sola una arquitectura distinta.

## 6. Fase 2 — Maturity (Madurez)

Conclusión:

- la necesidad y los mecanismos básicos son comercialmente maduros;
- la capa mecánica/local está más estabilizada;
- la capa de inteligencia —algoritmos, app, nube, ecosistemas— presenta mayor dependencia de proveedor y postventa;
- `LOCAL SAFETY FUNCTION (FUNCIÓN DE SEGURIDAD LOCAL)` debe distinguirse de funciones dependientes de nube/Internet;
- `INSTALLATION FRICTION (FRICCIÓN DE INSTALACIÓN)` es una dimensión comercial estructural.

## 7. Fase 3 — Demand (Demanda)

### 7.1 Evidencia directa — sensores standalone

Publicaciones seleccionadas:

| ML ID | Producto | Ventas visibles | Precio ARS aprox. |
|---|---|---:|---:|
| ML-0089 | Demasled domo-24 | +500 | 25.410 |
| ML-0090 | TP-Link Tapo T300 | +50 | 38.466 |
| ML-0091 | SMARTa / Tuya WiFi | +100 | 36.648 |
| ML-0092 | EZVIZ T10C | +100 | 35.990 |

Conclusión:

> Existe demanda observable en Mercado Libre Argentina por detección puntual de fugas/inundaciones.

### 7.2 Sistemas completos — detección + corte

Publicaciones seleccionadas:

| ML ID | Producto | Ventas visibles | Precio ARS aprox. |
|---|---|---:|---:|
| ML-0093 | JAXPETY HG61K0210 | no observadas | 512.707 |
| ML-0094 | GXFCHYL JZUFWH-000000US | no observadas | 295.521 |
| ML-0095 | U.S. Solid USS-LDV00008 | no observadas | 468.665 |
| ML-0096 | YoLink Smart Water Leak Protection System Kit | no observadas | 2.020.027 |

Conclusión correcta:

> Existe oferta de sistemas completos, pero la evidencia recolectada no demuestra todavía demanda transaccional visible de la solución completa.

No debe registrarse como “sin demanda”.

### 7.3 Componentes inteligentes

| ML ID | Producto | Ventas visibles | Uso metodológico |
|---|---|---:|---|
| ML-0097 | Latin Domo WC1420 | +500 | actuador retrofit / componente |
| ML-0098 | MOES ZWV-YC-US-GY-MS | +25 | válvula Zigbee / componente |
| ML-0099 | Blindsmart PF-PM02D | no observadas | actuador retrofit / componente |

La demanda del componente no equivale a demanda de la solución final.

Principios registrados:

```text
VISIBLE SALES (VENTAS VISIBLES) ≠ MARKET SIZE (TAMAÑO DE MERCADO)
COMPONENT DEMAND (DEMANDA DE COMPONENTE) ≠ FINAL SOLUTION DEMAND (DEMANDA DE SOLUCIÓN FINAL)
OFFER AVAILABILITY (DISPONIBILIDAD DE OFERTA) ≠ DEMAND EVIDENCE (EVIDENCIA DE DEMANDA)
NO VISIBLE SALES (SIN VENTAS VISIBLES) ≠ NO DEMAND (SIN DEMANDA)
```

## 8. Fase 4 — Competition (Competencia)

Tres capas competitivas:

```text
C1 — sensores standalone
C2 — sistemas completos con corte automático
C3 — componentes inteligentes capaces de formar una solución modular
```

Lectura:

- C1: competencia alta, precios bajos, marcas y genéricos, entrega local;
- C2: competencia directa visible baja/moderada, tickets altos e importación bajo demanda;
- C3: sustitución modular relevante mediante sensores + actuadores + ecosistemas.

Principios:

```text
PUBLICATION (PUBLICACIÓN) ≠ COMMERCIAL PRODUCT (PRODUCTO COMERCIAL)
DIRECT COMPETITION (COMPETENCIA DIRECTA) ≠ SOLUTION SUBSTITUTION (SUSTITUCIÓN DE SOLUCIÓN)
LOW COMPETITION (BAJA COMPETENCIA) ≠ HIGH OPPORTUNITY (ALTA OPORTUNIDAD)
```

## 9. Fase 5 — Brand Potential (Potencial de marca)

Lectura cualitativa:

| Arquitectura | Potencial de marca |
|---|---|
| Sensor standalone | medio-bajo |
| Sistema inline con corte | medio-alto |
| Sistema retrofit con corte | alto |
| Sistema modular por ecosistema | medio-alto |
| Monitor integral | alto teórico / alta complejidad |
| Sistema híbrido | alto teórico / muy alta complejidad |

Hipótesis de propuesta de valor emergente:

> Sistema doméstico de protección contra fugas que detecta agua y corta automáticamente el suministro, con instalación retrofit sobre una válvula existente, configuración clara, operación confiable y soporte local.

Principios:

```text
BRANDABILITY (CAPACIDAD DE MARCA) ≠ PRIVATE LABELABILITY (CAPACIDAD DE PONER MARCA PROPIA)
INSTALLATION FRICTION (FRICCIÓN DE INSTALACIÓN) puede convertirse en BRAND VALUE (VALOR DE MARCA)
MORE TECHNOLOGY (MÁS TECNOLOGÍA) ≠ MORE BRAND POTENTIAL (MÁS POTENCIAL DE MARCA)
```

## 10. Fase 6 — Product Bases (Productos Base)

### 10.1 Resultado conceptual

Cinco Product Bases cumplen potencialmente el handoff de `BRAND-CAND-001`:

```text
BASE-HOGAR-002 — sistema puntual + válvula central en línea
BASE-HOGAR-003 — sistema puntual + actuador retrofit
BASE-HOGAR-004 — monitor hidráulico integral + corte central
BASE-HOGAR-005 — sistema híbrido integral + sensores + corte
BASE-HOGAR-006 — protección automática específica de artefacto
```

### 10.2 Product Bases de soporte

Para mantener trazabilidad completa de las publicaciones observadas, se materializan además:

```text
BASE-HOGAR-001 — sensor standalone / solución parcial
BASE-HOGAR-007 — actuador retrofit standalone / componente
BASE-HOGAR-008 — válvula inteligente inline standalone / componente
```

Estos tres PB son `SUPPORT_PB` y **no deben ingresar automáticamente a Fase 7**.

### 10.3 Motivo de esta separación

`full-matrix-v5 0.7.0` exige que cada fila de `Publicaciones ML` tenga `ID Producto Base`.

Por lo tanto, una futura automatización debe distinguir dos conceptos:

```text
PRODUCT BASE EXISTS
(EXISTE COMO PRODUCTO BASE NORMALIZADO)

≠

CANDIDATE ELIGIBILITY
(ELEGIBILIDAD PARA EL BRAND CANDIDATE ACTIVO)
```

Estados conceptuales observados:

```text
CANDIDATE_PB
SUPPORT_PB
```

No se modifica todavía el schema para incorporar este campo. En `aut37` la clasificación queda registrada en `Productos Base.Observaciones`.

## 11. Regla de frontera de Product Base

No separar un PB sólo porque cambia:

- marca;
- vendedor;
- publicación;
- color;
- protocolo de conectividad;
- app;
- cantidad menor de accesorios.

Separarlo cuando cambia materialmente:

```text
Detection Mechanism (Mecanismo de detección)
Protection Scope (Alcance de protección)
Shutoff Mechanism (Mecanismo de corte)
Installation Architecture (Arquitectura de instalación)
User / Service Model (Modelo de uso / servicio)
```

La diferencia debe producir una consecuencia comercial significativa en propuesta de valor, instalación, costo, riesgo, soporte o experiencia del usuario.

## 12. Adapter de compatibilidad con la matriz vigente

La matriz vigente sigue el modelo legacy:

```text
NICHO → ... → PRODUCT BASE
```

El flujo nuevo parte de:

```text
BRAND CANDIDATE → METHOD V2 → PRODUCT BASE
```

Para no modificar `full-matrix-v5 0.7.0`, `aut37` crea el scope operativo:

```text
Nicho ID: 32
Nicho: Marca Hogar — protección doméstica contra fugas de agua
```

Esta fila es un `MATRIX_SCOPE_ALIAS`.

**No significa** que `BRAND-CAND-001` haya sido redefinido como un nicho en Brand System.

El input real continúa siendo el expediente `BRAND-CAND-001`.

Esta fricción debe quedar registrada para Matrix vNext / Intelligence Engine, pero no justifica reabrir hoy el schema ni el Validator.

## 13. Materialización aut37

Archivo:

```text
matrix-aut37-brand-cand-001-phase6.xlsx
```

Validación oficial:

```text
Application: Matrix Validator v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
SHA-256: 6c0f1524fe102fe5c531edb890639bb9fa9845fbc4cc1b9e046ce9ceb96387ff
```

La normalización de Fase 6 se conserva en `Productos Base` y en este documento; no se crea una evidencia con criterio artificial `Method v2`, porque `Evidencias.Criterio` referencia el catálogo vigente de `Criterios`. Las 28 fuentes globales nuevas quedan relacionadas activamente mediante `Evidencia Fuentes` para mantener trazabilidad y evitar fuentes activas huérfanas.

Incorporaciones principales:

```text
+ 1 scope operativo / MATRIX_SCOPE_ALIAS
+ 3 Evaluaciones
+ 3 Evidencias consolidadas
+ 11 Publicaciones ML
+ 8 Productos Base
+ 11 registros de Competencia ML
+ 3 Fuentes Externas
+ 28 Fuentes globales
+ 28 relaciones Evidencia Fuentes
```

No se crean registros de `Registro Tiempos` porque el tiempo activo no fue medido de forma defendible. No se reconstruyen tiempos retrospectivamente.

## 14. Hallazgos de Golden Run para próximo checkpoint metodológico

Registrar para evolución futura de Method v2:

1. `Brand Candidate` como input primario oficial de Method v2.
2. Contrato de ejecución por fase: `INPUT → ACTIVITIES → SOURCES → EVIDENCE → OUTPUT → GATE → STOP CONDITIONS`.
3. Clasificación de actividades `AUTO / COLLABORATIVE / EXTERNAL`.
4. Mercado Libre y Alibaba como gates colaborativos explícitos.
5. Output humano en español; traducción entre paréntesis en diagramas/cuadros.
6. `Marketplace structured attribute ≠ verified product characteristic`.
7. `Search saturation` es evidencia de cobertura de oferta, no prueba de ausencia de demanda.
8. Soluciones pueden emerger de combinación de componentes aunque no exista una publicación única del sistema.
9. `Candidate Eligibility` debe separarse de existencia de Product Base.
10. La futura automatización no debe contar publicaciones como productos ni componentes como solución final.
11. No formalizar todavía scores, ponderaciones ni cambios de Engine derivados de una sola Golden Run.

## 15. Próximo gate

No iniciar Fase 7 hasta cumplir:

```text
materialización aut37 ✓
→ Matrix Validator PASS ✓
→ checkpoint documental actualizado ✓
→ Fase 6 formalmente cerrada ✓
→ Fase 7 — shortlist pre-origen
```

En Fase 7 sólo deben competir inicialmente:

```text
BASE-HOGAR-002
BASE-HOGAR-003
BASE-HOGAR-004
BASE-HOGAR-005
BASE-HOGAR-006
```

Los PB de soporte permanecen trazables, pero no pasan por inercia a la shortlist.

## 16. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-18 | Checkpoint formal de Golden Run Fases 0–6; aut37 validada con PASS limpio y Fase 6 cerrada antes de iniciar shortlist pre-origen. |
