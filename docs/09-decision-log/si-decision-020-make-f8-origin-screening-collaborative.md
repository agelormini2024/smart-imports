---
id: si-decision-020
title: Make F8 Origin Screening Collaborative
description: Decisión de convertir F8 — Origin Screening / Alibaba en una fase colaborativa con participación y revisión explícita del Founder.
version: 1.0.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-13
updated: 2026-10-13
scope: method-v2
effective: prospective
related:
  - si-bim-proc-003
  - si-roadmap-002
  - si-decision-019
---

# SI-DECISION-020 — F8 Origin Screening / Alibaba = COLLABORATIVE

## 1. Contexto

F8 existe para comprobar que los Product Bases priorizados en F7 tienen oferta real en origen, comparabilidad suficiente y ausencia de bloqueantes estructurales.

Históricamente algunas ejecuciones de F8 fueron documentadas como `AUTO`.

La experiencia del Method v2 mostró que Alibaba no es sólo una fuente de datos. Durante el discovery de origen aparecen:

- variantes no previstas;
- arquitecturas alternativas;
- OEM equivalentes;
- diferencias de calidad aparente;
- packaging y dimensiones;
- MOQ;
- configuraciones;
- señales de madurez o saturación;
- oportunidades que pueden modificar la lectura de un Product Base.

Por eso F8 requiere criterio comercial conjunto y no debe ejecutarse como una caja negra autónoma.

## 2. Decisión

A partir de esta decisión:

```text
F8 — Origin Screening / Alibaba
Execution Mode: COLLABORATIVE
Founder participation: REQUIRED
```

Una ejecución futura de F8 debe declarar:

```text
phase: F8
mode: COLLABORATIVE
```

## 3. Qué significa COLLABORATIVE

`COLLABORATIVE` no significa que cada tarea sea manual.

```text
PHASE MODE = COLLABORATIVE
≠
EVERY TASK = MANUAL
```

### Founder / Alejandro

Participa explícitamente en:

- búsqueda exploratoria en Alibaba;
- aporte de productos, listings o proveedores relevantes;
- revisión de variantes y arquitecturas encontradas;
- lectura comercial de los resultados;
- revisión del shortlist de origen;
- aprobación explícita del cierre de F8.

### ChatGPT / Method v2

Puede ejecutar de forma autónoma:

- estrategia de búsqueda y keywords;
- ampliación de búsquedas;
- triage inicial;
- normalización;
- deduplicación;
- detección de posibles OEM/equivalencias;
- comparación contra Product Bases;
- clasificación y síntesis;
- extracción de atributos públicos;
- materialización de evidencias;
- actualización de matriz;
- validaciones automáticas.

### External

Permanece fuera del gate colaborativo de discovery:

- contacto real con proveedores;
- RFQ;
- negociación;
- cotización privada;
- documentación enviada por proveedor.

La falta de respuesta de un proveedor no controla el cierre de F8 si el objetivo de Origin Screening ya fue demostrado con evidencia pública suficiente.

## 4. Gate de cierre F8

F8 no puede cerrarse únicamente por ejecución autónoma del agente.

El cierre requiere:

```text
FOUNDER REVIEW: APPROVED
+
ORIGIN EVIDENCE: SOURCE-BOUND
+
ORIGIN SHORTLIST: MATERIALIZED
+
CANONICAL VALIDATION: PASS
=
F8 ELIGIBLE FOR CLOSED
```

`Founder Review: APPROVED` significa que el Founder revisó el resultado colaborativo de búsqueda y el shortlist de origen; no implica que deba inspeccionar personalmente cada resultado descartado.

## 5. Límites semánticos

Se mantienen:

```text
ORIGIN CONFIRMED ≠ SUPPLIER SELECTED
PUBLIC LISTING ≠ FORMAL QUOTE
PUBLIC ALIBABA PRICE ≠ NEGOTIATED FOB
DECISION-GRADE ≠ PROCUREMENT-GRADE
```

F8 sigue siendo screening de origen, no selección final de proveedor ni negociación de importación.

## 6. Aplicación histórica

Esta decisión es prospectiva.

```text
HISTORICAL AUTO EXECUTION
≠
RETROACTIVE INVALIDATION
```

Los candidatos y snapshots ya cerrados no se reabren únicamente porque F8 haya sido redefinida como `COLLABORATIVE`.

Los documentos históricos que registran `AUTO` conservan ese valor porque describen cómo se ejecutó realmente la fase en ese momento.

## 7. Aplicación futura

Todo nuevo Brand Candidate que alcance F8 debe heredar este contrato.

Antes de cerrar F8:

1. se realiza discovery de origen colaborativo;
2. Alejandro participa en búsqueda/revisión;
3. se normalizan y materializan los hallazgos;
4. se presenta el shortlist de origen;
5. Alejandro confirma `Founder Review: APPROVED`;
6. se ejecuta la validación canónica;
7. recién entonces F8 puede quedar `CLOSED`.

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-13 | Formaliza F8 — Origin Screening / Alibaba como COLLABORATIVE y exige Founder Review explícita para el close gate. |
