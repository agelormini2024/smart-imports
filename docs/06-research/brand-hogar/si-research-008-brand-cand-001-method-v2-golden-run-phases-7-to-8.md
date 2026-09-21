---
id: si-research-008
title: BRAND-CAND-001 — Method v2 Golden Run — Fases 7 a 8
description: Cierre documental de shortlist pre-origen y screening de origen para BRAND-CAND-001.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-21
updated: 2026-09-21
tags:
  - smart-imports
  - brand-hogar
  - brand-cand-001
  - method-v2
  - golden-run
  - phase-7
  - phase-8
  - origin-screening
---

# BRAND-CAND-001 — Method v2 Golden Run — Fases 7 a 8

## 1. Objetivo

Este documento continúa la Golden Run de `BRAND-CAND-001 — detección de fugas + corte automático` documentada en `SI-RESEARCH-007`.

El objetivo de este checkpoint es cerrar:

```text
Fase 7 — Shortlist pre-origen
Fase 8 — Screening de origen / comparabilidad
```

sin adelantar todavía:

```text
Fase 9 — Headroom
Fase 10 — Minimum Landed Cost Dataset
Fase 11 — Landed Cost
```

La función de Fase 8 no es seleccionar proveedor ni negociar una importación. Su función es demostrar que los Product Bases priorizados tienen oferta real en origen, que existe comparabilidad suficiente y que no aparece un bloqueante estructural que impida continuar.

---

## 2. Matrices y validación

### 2.1 Fase 7

Archivo:

`matrix-aut38-brand-cand-001-phase7.xlsx`

SHA-256:

`5b07d66d87563ab0d6354339756e883f0418b9b99be7018e8f8210dae3f02819`

Validación:

```text
Application: Matrix Validator v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

### 2.2 Fase 8

Archivo:

`matrix-aut39-brand-cand-001-phase8.xlsx`

SHA-256:

`62341e1c202f87a531f96e9573613f9adda588e70e761eee9254e214a30a658c`

Validación:

```text
Application: Matrix Validator v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

`aut39` pasa a ser el snapshot comercial operativo vigente de la Golden Run.

---

## 3. Fase 7 — Shortlist pre-origen

La shortlist no equivale a “todos los Product Bases plausibles”. Su función es podar antes de invertir más tiempo en sourcing.

### 3.1 Shortlist consolidada

| Product Base | Estado Fase 7 | Lectura operativa |
|---|---|---|
| `BASE-HOGAR-003` | ACTIVE — prioridad principal | Sensores puntuales + actuador retrofit sobre válvula existente. Menor intervención hidráulica; riesgo principal: compatibilidad mecánica y arquitectura local/cloud. |
| `BASE-HOGAR-006` | ACTIVE — prioridad principal / posible producto de entrada | Protección automática localizada o específica por artefacto. Problema concreto, explicación comercial simple y menor complejidad sistémica. |
| `BASE-HOGAR-002` | ACTIVE — secundario / condicionado | Sensores puntuales + válvula central inline. Solución integral, pero con mayor fricción de instalación hidráulica. |
| `BASE-HOGAR-004` | WATCHLIST | Monitoreo hidráulico whole-home + cierre central. Alto potencial, pero mayor complejidad de detección, instalación y confiabilidad. |
| `BASE-HOGAR-005` | PAUSED | Arquitectura híbrida. Reintroducir sólo ante OEM integrado maduro; no construir integración propia de subsistemas en esta etapa. |

Orden operativo inicial para screening:

```text
BASE-HOGAR-003
→ BASE-HOGAR-006
→ BASE-HOGAR-002
```

`BASE-HOGAR-004` se observa oportunísticamente y `BASE-HOGAR-005` no abre búsqueda activa.

---

## 4. Fase 8 — Criterio de screening

Clasificación usada:

```text
EXACTA
→ la oferta de origen representa directamente el Product Base.

COMPARABLE
→ conserva la arquitectura esencial, con variaciones no estructurales
   de protocolo, packaging, hub, sensor, configuración o servicio.

BENCHMARK
→ aporta precio, instalación, torque, materiales, operación o
   características útiles, pero no representa por sí sola el Product Base.
```

Regla reforzada durante la ejecución:

```text
mecanismo físico
≠
Product Base
```

Ejemplo:

```text
válvula inline
≠ automáticamente BASE-HOGAR-002
```

También deben considerarse:

- alcance de protección;
- arquitectura de detección;
- arquitectura de cierre;
- instalación;
- job comercial;
- dependencia local/cloud;
- composición real del sistema.

---

## 5. Resultado por Product Base

### 5.1 BASE-HOGAR-002 — sensores puntuales + válvula central inline

Estado:

```text
ORIGIN CONFIRMED — CONDITIONAL
```

Evidencia principal:

- `Bornic CWX-15N` — `COMPARABLE FUERTE`.
- `Witzone 800DN15S2` — `BENCHMARK / COMPARABLE`.

Bornic demuestra válvula motorizada inline + sensores de fuga en un mismo sistema y una familia de tamaños suficiente para continuar evaluando. Queda pendiente confirmar mediante documentación la configuración apropiada para entrada principal residencial.

Witzone aporta una referencia útil de arquitectura local/offline sin WiFi ni app, pero su configuración DN15 y el posicionamiento del proveedor reducen su representatividad como solución whole-home central.

No se identifica un bloqueante estructural.

### 5.2 BASE-HOGAR-003 — sensores puntuales + actuador retrofit

Estado:

```text
ORIGIN CONFIRMED
```

Evidencia principal:

- `WALE Tuya Zigbee` — `COMPARABLE FUERTE`.
- `Pushuntai MD100A + SQ400C` — `COMPARABLE FUERTE`.
- `Frankever FK-GS02D` — `COMPARABLE FUERTE`.
- `SMARSECUR JXS / ZB-JXS` — benchmarks/componentes de soporte, sin contarlos como diversidad independiente cuando pertenecen al mismo proveedor.

Hallazgo confirmado con Pushuntai:

```text
SQ400C WiFi leak sensor
→ Tuya / Smart Life Cloud
→ MD100A WiFi retrofit actuator
→ automatic shutoff
```

El proveedor confirmó que sensor y actuador se compran por separado y que ambos requieren acceso a `Tuya/Smart Life Cloud`. Esto confirma la arquitectura funcional, pero registra una dependencia cloud sobre la función crítica.

Frankever queda pendiente de documentación para la variante Zigbee, sensor compatible, gateway y funcionamiento sin Internet.

La disponibilidad de origen y la diversidad de proveedores quedan confirmadas.

### 5.3 BASE-HOGAR-004 — monitoreo hidráulico whole-home

Estado:

```text
ORIGIN CONFIRMED
F7 STATUS: WATCHLIST
```

`Eastpure LP-365` constituye una `EXACTA FUERTE`: solución whole-home con instalación central, detección hidráulica, cierre automático y capa IoT.

Este hallazgo confirma que existe una oferta OEM madura de esta arquitectura, pero no revierte la decisión de Fase 7. El PB permanece en `WATCHLIST` por su mayor complejidad tecnológica, hidráulica y de confiabilidad.

### 5.4 BASE-HOGAR-005 — arquitectura híbrida

Estado:

```text
PAUSED
```

No se ejecuta sourcing activo en Fase 8.

Sólo debe reactivarse si aparece un OEM que entregue una solución híbrida madura e integrada. No se considera deseable construir una integración propia de subsistemas en esta etapa.

### 5.5 BASE-HOGAR-006 — protección específica de artefacto/punto

Estado:

```text
ORIGIN CONFIRMED
```

Evidencia principal:

- `AGSHOME A2C-SC Intelliflow` — `EXACTA FUERTE`, appliance-specific para lavadora.
- `Flomarvel FH-WL` — `COMPARABLE FUERTE`, protección localizada genérica.
- `Witzone` — referencia complementaria de protección localizada simple.

AGSHOME confirmó comercialmente disponibilidad de muestra y opciones de OEM/private label para producto y packaging.

Los valores exactos de precio, MOQ y condiciones comerciales se conservan en la matriz y registros privados, de acuerdo con la regla de confidencialidad del repositorio público.

Quedan pendientes datasheet, user manual y packing list.

Durante Fase 8 apareció una distinción útil:

```text
protección localizada genérica
vs.
protección appliance-specific real
```

No se divide todavía `BASE-HOGAR-006` en nuevos Product Bases. La diferencia queda registrada como hallazgo para la retrospectiva y para evaluar después si cambia materialmente job, instalación, economía o propuesta comercial.

---

## 6. Supplier contact — aprendizaje operativo

La primera aproximación mediante cuestionarios largos mostró una fricción innecesaria.

La secuencia que funcionó mejor fue:

```text
DOCUMENTATION FIRST
→ GAP ANALYSIS
→ TARGETED QUESTIONS
→ COMMERCIAL VALIDATION
```

Principio derivado:

```text
SUPPLIER QUESTIONNAIRE ≠ FIRST CONTACT
```

No conviene preguntarle al proveedor algo que puede resolverse primero con datasheet, manual, packing list o material técnico.

La ausencia de documentación técnica también constituye información sobre madurez de proveedor/producto.

Este aprendizaje se registra para la retrospectiva de la Golden Run. No modifica todavía Method v2 ni el Engine.

---

## 7. Pendientes no bloqueantes

Al momento del cierre de Fase 8 permanecen abiertas respuestas o documentación de:

| Proveedor | Pendiente |
|---|---|
| Bornic / Bonica | Datasheet, manual, packing list y confirmación de configuración central residencial. |
| Frankever | Documentación Zigbee, sensor, gateway y operación sensor→actuador sin Internet. |
| AGSHOME | Datasheet, user manual y packing list de A2C-SC. |
| Flomarvel | Documentación técnica y comercial solicitada. |
| WALE | Respuesta/documentación si el proveedor la envía. |

Estas respuestas pueden mejorar o corregir la clasificación de una oferta concreta.

Regla de mantenimiento:

```text
nueva respuesta
→ ¿contradice algo estructural?
   ├─ NO → actualizar evidencia/fila afectada
   └─ SÍ → revisar únicamente el Product Base afectado
```

No se reabre discovery general salvo contradicción estructural.

---

## 8. Gate de Fase 8

El gate se considera satisfecho porque, para los Product Bases activos:

- existe oferta real en origen;
- existe comparabilidad suficiente;
- el mapeo `producto de origen ↔ Product Base` es explícito;
- no aparece un bloqueante estructural que obligue a detener el PB;
- los gaps documentales restantes están identificados.

Resultado:

```text
BASE-HOGAR-002 → PASS CONDITIONAL
BASE-HOGAR-003 → PASS
BASE-HOGAR-004 → ORIGIN CONFIRMED / WATCHLIST
BASE-HOGAR-005 → PAUSED / NOT SCREENED BY DESIGN
BASE-HOGAR-006 → PASS
```

`ORIGIN CONFIRMED` no significa proveedor seleccionado ni autorización de compra.

---

## 9. Próximo gate

Con Fases 7–8 materializadas y `aut39` validada:

```text
BRAND-CAND-001
→ Method v2 Fases 0–8 cerradas
→ próximo gate: Fase 9 — Headroom
```

En Fase 9 se evaluará espacio económico preliminar antes de construir el dataset completo de Landed Cost.

---

## 10. Hallazgos para retrospectiva de Golden Run

Registrar para revisión posterior, sin modificar todavía el método:

1. `Documentation first → gap analysis → targeted questions → commercial validation`.
2. La clasificación de origen necesita explícitamente alcance de protección además del mecanismo físico.
3. Un producto físico puede soportar más de una arquitectura de uso, pero `PRODUCT CAPABILITY ≠ SOLUTION ARCHITECTURE EVIDENCED`.
4. `Many suppliers ≠ good PB` y `few suppliers ≠ bad PB`.
5. `ORIGIN CONFIRMED ≠ proveedor seleccionado`.
6. Respuestas pendientes no deberían bloquear un gate ya demostrado, salvo contradicción estructural.

---

## 11. Documentos relacionados

- `docs/06-research/brand-hogar/si-research-007-brand-cand-001-method-v2-golden-run-phases-0-to-6.md`
- `docs/07-brand/brands/brand-hogar/candidates/brand-cand-001-water-leak-detection-and-shutoff.md`
- `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md`
- `matrix-aut38-brand-cand-001-phase7.xlsx`
- `matrix-aut39-brand-cand-001-phase8.xlsx`

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-21 | Cierre documental de Fases 7–8 de la Golden Run de BRAND-CAND-001; aut38/aut39 PASS y próximo gate Fase 9 — Headroom. |
