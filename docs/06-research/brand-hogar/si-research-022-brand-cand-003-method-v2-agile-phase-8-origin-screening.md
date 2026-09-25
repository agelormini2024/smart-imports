---
id: si-research-022
title: BRAND-CAND-003 — Method v2 Agile — F8 Origin Screening
description: Screening público de disponibilidad y comparabilidad de origen para los Product Bases activos de tratamiento doméstico del aire interior.
version: 0.2.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-25
updated: 2026-09-25
phase: business-intelligence
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-003
  - indoor-air
  - phase-8
---

# BRAND-CAND-003 — Method v2 Agile — F8 Screening de origen

Estado: `CLOSED`

## 1. Objetivo

Confirmar si los Product Bases que sobrevivieron F7 existen realmente en origen con configuraciones suficientemente comparables como para justificar el siguiente screen económico.

F8 confirma disponibilidad y comparabilidad pública de origen. No selecciona proveedor, no valida certificaciones, no negocia condiciones y no convierte un listing público en cotización firme.

```text
ORIGIN CONFIRMED
≠ SUPPLIER SELECTED

PUBLIC LISTING
≠ COMMERCIAL QUOTE

LISTING ATTRIBUTE
≠ PERFORMANCE VALIDATED
```

## 2. Scope heredado de F7

```text
CORE
BASE-HOGAR-009
BASE-HOGAR-010

SECONDARY / HIGHLY CONDITIONED
BASE-HOGAR-011
```

Fuera del flujo normal de F8:

```text
HOLD
BASE-HOGAR-012
BASE-HOGAR-015

OUT OF SHORTLIST
BASE-HOGAR-013
BASE-HOGAR-014
```

## 3. Resultado ejecutivo

```text
BASE-HOGAR-009
ORIGIN CONFIRMED

BASE-HOGAR-010
ORIGIN CONFIRMED — CONDITIONED

BASE-HOGAR-011
ORIGIN CONFIRMED — HIGHLY CONDITIONED
```

Los tres PB activos muestran oferta pública suficiente para justificar continuidad metodológica. La calidad y las condiciones de esa confirmación no son equivalentes.

## 4. BASE-HOGAR-009 — Filtración portátil de partículas

La evidencia pública confirma múltiples configuraciones OEM comparables con filtración HEPA/H13, métricas de desempeño declaradas, variantes de tensión internacional y formatos domésticos compactos.

Lectura:

```text
ORIGIN CONFIRMED
```

Gaps que permanecen abiertos:

- CADR y método aplicable por modelo exacto;
- 220–240 V / 50 Hz y plug;
- documentación del medio HEPA;
- filtros de reposición;
- packing productivo;
- certificaciones aplicables;
- precio e Incoterm productivos.

## 5. BASE-HOGAR-010 — Filtración portátil de partículas + gases/olores

La oferta pública confirma configuraciones OEM que combinan filtración de partículas con carbón activado/sorbente y que declaran métricas separadas o claims específicos de tratamiento gas-phase.

Lectura:

```text
ORIGIN CONFIRMED — CONDITIONED
```

La condición de F7 sigue abierta:

```text
CARBON PRESENT
≠ MATERIAL SORBENT VALIDATED
```

Antes de una comparación productiva deben resolverse, según la configuración exacta:

- masa/configuración del sorbente;
- espesor o arquitectura del medio;
- filtro combinado vs. independiente;
- método de medición aplicable;
- contaminantes objetivo;
- vida útil y reposición.

## 6. BASE-HOGAR-011 — Filtración + tratamiento activo complementario

La evidencia pública confirma la existencia de variantes OEM que combinan HEPA, sorbente y funciones activas como ionización, UV o fotocatálisis. También existen claims comerciales `ozone-free` en parte de la oferta.

Lectura:

```text
ORIGIN CONFIRMED — HIGHLY CONDITIONED
```

Gaps que permanecen explícitos:

- `ozone-free` verificable;
- subproductos bajo operación real;
- posibilidad de desactivar funciones activas;
- arquitectura eléctrica compatible;
- interlocks y seguridad UV cuando corresponda;
- evidencia independiente para claims microbiológicos;
- costo/beneficio incremental frente a arquitecturas pasivas.

## 7. Lectura comparativa

```text
009
ORIGIN CONFIRMED
→ arquitectura madura
→ mejor encaje de primera etapa

010
ORIGIN CONFIRMED — CONDITIONED
→ disponibilidad clara
→ valor adicional posible
→ materialidad del sorbente sigue siendo gate técnico

011
ORIGIN CONFIRMED — HIGHLY CONDITIONED
→ oferta real
→ complejidad/safety crece más rápido que el valor demostrado
```

F8 no encuentra un bloqueo de origen.

Mantiene explícita la separación:

```text
HEPA
≠ HEPA + MATERIAL SORBENT
≠ HEPA + ACTIVE TREATMENT
```

## 8. Materialización y validación

La matriz privada conserva la trazabilidad completa de comparables, fuentes y atributos comerciales.

```text
COT-0037 ... COT-0042
SRC-0391 ... SRC-0397
EVID-0253
EVSRC-0455 ... EVSRC-0461

MATRIX
matrix-aut53-brand-cand-003-phase8.xlsx

SHA-256
a894d983874fe175da353c7eac5ef10b3f21d97bf84fd7560b68af65f0b9431e

RESULT
PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

## 9. Confidencialidad

El repositorio público conserva método, gaps, estados y decisiones. Identidad detallada de proveedores, URLs de sourcing, precios, MOQ, packing exacto y demás datos comerciales permanecen en la matriz operativa privada.

## 10. Cierre

```text
F8 CLOSED
→ F9 — Import Cost Headroom
```

F9 utiliza Headroom como screen y no como margen ni Landed Cost.
