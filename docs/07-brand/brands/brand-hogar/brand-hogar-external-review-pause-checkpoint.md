---
id: brand-hogar-external-review-pause-checkpoint
title: Marca Hogar — Baseline interna cerrada y revisión externa pendiente
description: Checkpoint posterior al Portfolio Review interno; congela la baseline de Marca Hogar y define el gate de revisión externa.
version: 0.2.0
status: internal-closed-external-review-pending
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-05
updated: 2026-10-07
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

Marca Hogar queda en:

```text
INTERNAL PORTFOLIO REVIEW COMPLETE
PORTFOLIO BASELINE FROZEN
EXTERNAL REVIEW PENDING
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

Para `BRAND-CAND-006`, la reconciliación retrospectiva quedó completada hasta `aut104 PASS`, con F0–F13 `CLOSED`, estado `PORTFOLIO REVIEW READY / FREEZE` y F14 `NOT OPENED`. La pausa operativa no modifica ese estado.

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

La prioridad interna queda formalizada por SI-RESEARCH-071 / SI-DECISION-017: `BASE-HOGAR-016` lead, `BASE-HOGAR-006` backup, `BASE-HOGAR-010` y `BASE-HOGAR-002` segunda línea; `BASE-HOGAR-028` y `BASE-PET-003` reserva.

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

Marca Hogar se reabre como workstream primario sólo cuando exista información externa suficiente que justifique modificar el baseline para decidir:

```text
qué productos siguen
→ qué información pedir a proveedores
→ qué economía debe recalcularse
→ qué producto merece profundización de compra
```

La profundización con proveedores será consecuencia de esa revisión, no un requisito previo a ella.

## 10. Relación con Marca Fitness

Marca Hogar queda cerrada internamente y congelada hasta revisión externa. Esto permite que Marca Fitness pase a ser el workstream principal.

Ambos frentes mantienen estados independientes. La experiencia de Hogar y `SI-BRAND-003` sirven como metodología reusable para Fitness y futuras marcas.
