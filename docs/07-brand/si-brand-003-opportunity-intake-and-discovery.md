---
id: si-brand-003
title: Ingreso de oportunidades y descubrimiento
description: Puerta de entrada reusable para oportunidades descubiertas fuera de la investigación sistemática y convergencia de descubrimiento descendente y ascendente antes del Brand Candidate Screening.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-05
updated: 2026-10-05
tags:
  - brand-system
  - opportunity-intake
  - discovery
  - reusable-method
related:
  - si-brand-001
  - si-brand-002
---

# SI-BRAND-003 — Ingreso de oportunidades y descubrimiento

## 1. Propósito

Smart Imports debe poder incorporar oportunidades que no nacen de una investigación sistemática.

Un producto puede llamar la atención porque lo recomienda un socio, lo muestra un proveedor, aparece en un marketplace, se observa durante un viaje, surge de una conversación con un cliente o simplemente resulta atractivo al fundador.

Ese origen es una forma válida de descubrimiento. No es, por sí mismo, evidencia de calidad comercial.

```text
ORIGEN DE LA IDEA ≠ CALIDAD DE LA OPORTUNIDAD
```

## 2. Ingreso de oportunidad

Un hallazgo espontáneo entra primero como una **oportunidad detectada**.

Todavía no se asume que sea una nueva Publicación, un nuevo Producto Base, un nuevo Brand Candidate ni una oportunidad apta para Method v2.

```text
DESCUBRIMIENTO
→ INGRESO DE OPORTUNIDAD
→ CLASIFICACIÓN DEL HALLAZGO
→ MAPEO HACIA EL BRAND SYSTEM
→ BRAND CANDIDATE SCREENING, si corresponde
→ METHOD v2, sólo después del screening
```

## 3. Dos rutas de descubrimiento

### Descubrimiento descendente

```text
territorio
→ misión
→ problema
→ solución
→ producto / arquitectura
```

### Descubrimiento ascendente

```text
producto descubierto
→ solución que representa
→ problema que resuelve
→ misión
→ territorio
```

La ruta ascendente utiliza **mapeo inverso** para determinar dónde encaja el hallazgo.

Ambas rutas convergen antes de abrir Brand Candidate Screening.

## 4. Preguntas mínimas de clasificación

1. ¿Qué vimos realmente: una publicación, un SKU, un producto, una arquitectura o una solución?
2. ¿Qué problema del usuario resuelve?
3. ¿Ese problema ya existe en el sistema?
4. ¿La solución ya está representada por un Producto Base?
5. ¿La arquitectura es suficientemente distinta como para justificar otro Producto Base?
6. ¿Con qué misión se relaciona?
7. ¿Encaja en el territorio de una marca existente?
8. ¿Abre una hipótesis de Brand Candidate nueva?
9. ¿Debe quedar estacionado para otra marca o revisión futura?

## 5. Resultados posibles

### A. Evidencia de un Producto Base existente

El hallazgo se incorpora como publicación, proveedor o evidencia adicional. No se crea un nuevo Producto Base.

### B. Nueva arquitectura para un problema existente

Puede justificar un nuevo Producto Base si existen diferencias materiales de funcionamiento, experiencia, seguridad, economía u operación.

### C. Nuevo problema o nueva misión dentro de una marca

Puede originar una hipótesis de Brand Candidate, que debe atravesar Brand Candidate Screening antes de Method v2.

### D. No encaja en la marca actual

```text
NO ENCAJA EN LA MARCA ACTUAL
≠
MALA OPORTUNIDAD
```

Puede quedar estacionada, asociada a otra marca, reservada para una futura marca o descartada por otra razón explícita.

## 6. Reglas de integridad

```text
PUBLICACIÓN ≠ PRODUCTO BASE
PRODUCTO BASE ≠ BRAND CANDIDATE
BRAND CANDIDATE ≠ PRODUCTO
CATEGORÍA ≠ BRAND FIT
ORIGEN DE LA IDEA ≠ CALIDAD DE LA OPORTUNIDAD
```

`ME GUSTA`, `RECOMENDADO`, `VIRAL`, `NOVEDOSO` o `ATRACTIVO` son razones para mirar, no razones para aprobar.

## 7. Metadatos conceptuales del ingreso

Una futura implementación puede registrar:

```text
Discovery Source
Discovery Reason
Observed Artifact
Source / Evidence
Candidate Problem
Candidate Mission
Candidate Territory
Intake Status
```

Fuentes conceptuales posibles:

```text
METHOD_RESEARCH
FOUNDER
PARTNER
SUPPLIER
CUSTOMER
MARKETPLACE
TRAVEL
TRADE_SHOW
SOCIAL_MEDIA
OTHER
```

Estos valores describen procedencia; no otorgan puntaje. La convención final de IDs y su representación en matriz quedan pendientes hasta que exista una necesidad operativa real.

## 8. Relación con Method v2

`SI-BRAND-003` no reemplaza ni acorta Method v2.

```text
hallazgo libre
→ ingreso estructurado
→ clasificación
→ Brand Candidate Screening
→ PASS
→ Method v2
```

No se abre Method v2 directamente porque un producto resulte atractivo.

## 9. Uso futuro en el Intelligence Engine

Cuando exista suficiente historial, el sistema podrá analizar qué fuentes originan mejores oportunidades, cuántos hallazgos terminan como evidencia de Productos Base existentes, cuántos generan nuevas arquitecturas y cuántos llegan a finalista o compra.

El objetivo es conservar la serendipia comercial sin renunciar a trazabilidad ni rigor.
