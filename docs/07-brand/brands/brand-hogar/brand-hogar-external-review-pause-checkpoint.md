---
id: brand-hogar-external-review-pause-checkpoint
title: Marca Hogar — Pausa operativa para revisión externa
description: Checkpoint previo a reuniones con socio y despachante; conserva estados metodológicos y define condiciones de reentrada.
version: 0.1.0
status: paused-external-review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-05
updated: 2026-10-05
brand: brand-hogar
tags:
  - brand-hogar
  - external-review
  - customs-broker
  - partner-review
  - checkpoint
---

# Marca Hogar — Pausa operativa para revisión externa

## 1. Estado

Marca Hogar entra en:

```text
PAUSA OPERATIVA — REVISIÓN EXTERNA
```

La pausa comienza después de preparar material suficiente para reunión con socio, comparación transversal de finalistas y consulta estructurada con despachante.

No implica cierre definitivo, descarte ni cambio de estado metodológico de los Brand Candidates.

## 2. Estado formal preservado

```text
BRAND-CAND-001 → F0–F13 CLOSED → PORTFOLIO REVIEW READY / FREEZE
BRAND-CAND-002 → PASS TO METHOD V2 → DEFERRED / PAUSED
BRAND-CAND-003 → F0–F13 CLOSED → PORTFOLIO REVIEW READY / FREEZE
BRAND-CAND-004 → F0–F13 CLOSED → PORTFOLIO REVIEW READY / FREEZE
BRAND-CAND-005 → F0–F13 CLOSED → PORTFOLIO REVIEW READY / FREEZE
BRAND-CAND-006 → F0–F4 CLOSED → F5 ANALYSIS COMPLETE / MATERIALIZATION PENDING
F14 → NOT OPENED
```

Para `BRAND-CAND-006`, `aut95` continúa siendo la última matriz validada. La próxima fase formal sigue siendo materializar `aut96`, validar y cerrar F5, pero no se prioriza mientras Marca Hogar permanezca en pausa operativa.

## 3. Entregables operativos preparados

Fuera del repositorio se prepararon dos documentos de trabajo:

1. **Comparativa ejecutiva de finalistas para reunión con socio v0.1**.
2. **Paquete para revisión de despachante v0.1**.

Son vistas operativas derivadas del conocimiento del proyecto. No reemplazan la matriz ni la documentación metodológica como fuente de verdad.

## 4. Priorización para revisión externa

Consulta inicial con despachante:

```text
BASE-HOGAR-002
BASE-HOGAR-006
BASE-HOGAR-010
BASE-HOGAR-016
```

Reserva de cartera / posible segunda etapa:

```text
BASE-HOGAR-028
BASE-PET-003
```

Esta separación es operativa; no constituye un nuevo ranking formal ni modifica decisiones de Method v2.

## 5. Qué no se hará durante la pausa

- no profundizar proveedores por defecto;
- no solicitar datos adicionales sólo por completar campos;
- no abrir nuevas decisiones de compra;
- no abrir F14;
- no descartar finalistas sólo por falta de información externa;
- no recalcular economía sin una causa material nueva.

## 6. Qué sí puede hacerse durante la pausa

La pausa no bloquea el descubrimiento.

Si aparece un producto recomendado, observado o atractivo, puede registrarse mediante `SI-BRAND-003` como **oportunidad detectada** y clasificarse conceptualmente.

```text
NUEVO HALLAZGO
→ INGRESO DE OPORTUNIDAD
→ CLASIFICACIÓN
→ ESTACIONAR / VINCULAR
```

Ese registro:

- no crea automáticamente un Producto Base;
- no crea automáticamente un Brand Candidate;
- no abre Brand Candidate Screening;
- no abre Method v2;
- no modifica los estados congelados de Marca Hogar.

La profundización se decide al retomar formalmente el frente.

## 7. Información esperada del socio

- productos de mayor interés;
- presupuesto máximo inicial;
- tolerancia a complejidad y postventa;
- preferencia por producto único o pequeña familia;
- prioridades de revisión externa.

## 8. Información esperada del despachante

- NCM Argentina;
- derecho de importación;
- tasa estadística;
- cargas relevantes para estimar desembolso;
- intervenciones;
- certificaciones;
- requisitos eléctricos;
- etiquetado;
- restricciones;
- documentación adicional necesaria;
- alertas que puedan modificar materialmente la viabilidad.

```text
HS DECLARADO POR PROVEEDOR
≠
NCM ARGENTINA VALIDADO
```

## 9. Condición de reentrada

Marca Hogar se retoma formalmente cuando exista información suficiente de las reuniones para decidir:

```text
qué productos siguen
→ qué información pedir a proveedores
→ qué economía debe recalcularse
→ qué producto merece profundización de compra
```

La profundización con proveedores será consecuencia de esa revisión, no un requisito previo a ella.

## 10. Relación con Marca Fitness

La pausa de Marca Hogar permite abrir trabajo conceptual de Marca Fitness sin declarar cerrado HOGAR.

Ambos frentes mantienen estados independientes. La experiencia de Hogar y `SI-BRAND-003` sirven como metodología reusable para Fitness y futuras marcas.
