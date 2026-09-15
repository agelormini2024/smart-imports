---
id: si-research-006
title: Cierre de Fases 7–11 y validación interna de Method v2
description: Consolida shortlist pre-origen, screening de origen, Headroom, Minimum Landed Cost Dataset, Landed Cost Screen y retrospectiva del Método v2 sobre el Nicho 3.
version: 1.0.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-15
updated: 2026-09-15
tags:
  - research
  - niche-3
  - method-v2
  - sourcing
  - headroom
  - landed-cost
  - validation
related:
  - si-research-005
  - si-roadmap-002
  - si-decision-014
  - si-decision-015
audience:
  - founder
  - partner
  - assistant
phase: commercial-validation
---

# SI-RESEARCH-006 — Cierre de Fases 7–11 y validación interna de Method v2

## 1. Propósito

Este documento consolida el recorrido del **Nicho 3 — Mascotas: cuidado, bienestar y tecnología** desde la shortlist pre-origen hasta el primer `Landed Cost Screen`.

Su objetivo principal no es declarar una decisión de importación, sino documentar que **Method v2 fue ejecutado internamente de punta a punta hasta el gate profesional externo**.

La validación final de clasificación aduanera, derechos, intervenciones, certificaciones y costos definitivos corresponde a un despachante de aduana y se reserva para una shortlist reducida de candidatos.

## 2. Punto de partida

Fase 6 había cerrado con ocho Productos Base:

| ID | Producto Base |
|---|---|
| `BASE-PET-001` | Vacuum Grooming doméstico integrado |
| `BASE-PET-002` | Arenero automático rotativo cerrado |
| `BASE-PET-003` | Arenero automático open-top / acceso amplio |
| `BASE-PET-004` | Arenero automático de rastrillo |
| `BASE-PET-005` | Fuente inteligente automatizada/conectada |
| `BASE-PET-006` | Fuente con monitoreo cuantitativo de hidratación |
| `BASE-PET-007` | Tracker GPS 4G para mascotas |
| `BASE-PET-008` | Tracker GPS + Wellness avanzado |

La regla aplicada desde ese punto fue:

```text
no profundizar todos los PB por igual
→ reducir
→ validar origen
→ calcular Headroom
→ reunir dataset mínimo
→ estimar Landed Cost sólo en sobrevivientes
```

## 3. Fase 7 — Shortlist pre-origen

Resultado:

```text
BASE-PET-001 → ADVANCE
BASE-PET-002 → ADVANCE — CONDITIONAL
BASE-PET-003 → ADVANCE — CONDITIONAL
BASE-PET-004 → ADVANCE — CONDITIONAL
BASE-PET-005 → ADVANCE
BASE-PET-006 → HOLD
BASE-PET-007 → HOLD
BASE-PET-008 → HOLD
```

La reducción no se realizó por complejidad aislada. Se evaluaron conjuntamente:

- evidencia de demanda;
- estructura competitiva;
- potencial de marca;
- diferenciación;
- riesgo técnico;
- seguridad;
- dependencia de software/backend;
- postventa;
- viabilidad preliminar de origen.

`HOLD` no significa descarte definitivo. Significa que el producto no justifica consumir más costo de investigación en la ronda actual.

## 4. Fase 8 — Screening de origen

La fase de origen separó:

```text
EXACTA
COMPARABLE
BENCHMARK
```

Resultado operativo:

```text
BASE-PET-001 → ORIGIN CONFIRMED
BASE-PET-002 → ORIGIN CONDITIONAL
BASE-PET-003 → ORIGIN CONDITIONAL
BASE-PET-004 → ORIGIN CONDITIONAL
BASE-PET-005 → ORIGIN CONFIRMED
```

La condición de los areneros automáticos no deriva de falta de oferta OEM. Los principales riesgos se concentran en:

- seguridad mecánica;
- sensores;
- QA;
- atasco;
- limpieza;
- firmware/app cuando corresponda;
- repuestos;
- soporte y postventa.

## 5. Fase 9 — Import Cost Headroom

Method v2 mantiene la separación:

```text
Headroom ≠ Landed Cost
```

El Headroom responde:

> ¿Cuánto puede crecer el costo de origen antes de que el negocio deje de cumplir el margen objetivo?

No intenta estimar cuánto costará realmente importar.

Después del screening, sólo dos Productos Base justificaron profundización económica inmediata:

```text
BASE-PET-003 → ADVANCE
BASE-PET-004 → ADVANCE — CONDITIONAL
```

Los demás quedaron en `HOLD`, sin necesidad de calcular un Landed Cost detallado.

## 6. Fase 10 — Minimum Landed Cost Dataset

Antes de estimar Landed Cost se exige, como mínimo:

- producto suficientemente comparable;
- cantidad;
- precio de origen;
- Incoterm;
- unidades por caja;
- dimensiones de caja;
- peso bruto;
- CBM calculable;
- país y punto/puerto de origen;
- clasificación aduanera tentativa.

Estados utilizados:

```text
PROMISING / NOT_READY_FOR_LANDED_COST
PROMISING / NEAR_READY_FOR_LANDED_COST
READY_FOR_LANDED_COST
```

### BASE-PET-003

La respuesta directa del proveedor permitió cerrar el dataset mínimo con suficiente confianza para screening:

```text
READY_FOR_LANDED_COST
```

Quedaron pendientes no bloqueantes para el screening:

- una aclaración final de packing;
- clasificación NCM profesional;
- certificaciones e intervenciones definitivas.

### BASE-PET-004

La arquitectura quedó confirmada con una referencia concreta de rastrillo/pala y se envió RFQ para fijar:

- configuración exacta;
- precio por volumen;
- Incoterm;
- puerto;
- packing;
- pesos;
- seguridad;
- private label.

Estado al cierre de este documento:

```text
AWAITING_SUPPLIER_RESPONSE
```

## 7. Fase 11 — Landed Cost Screen

Se formaliza una distinción fundamental:

```text
Economic Landed Cost ≠ Total Cash Outlay
```

### Economic Landed Cost

Incluye el costo económico no recuperable necesario para poner el producto en Argentina:

```text
origen
+ logística internacional
+ seguro
+ derechos/tasas no recuperables
+ terminal / despacho / operación local estimada
```

### Total Cash Outlay

Agrega adelantos fiscales y otros conceptos que afectan caja pero pueden ser recuperables o computables:

```text
Economic Landed Cost
+ IVA importación
+ percepciones / pagos a cuenta
```

Esta separación evita confundir rentabilidad económica con necesidad financiera.

## 8. Resultado de BASE-PET-003

`BASE-PET-003` fue el primer Producto Base del Nicho 3 en completar un `Landed Cost Screen` defendible.

Resultado metodológico:

```text
STRONG CANDIDATE — PENDING PROFESSIONAL VALIDATION
```

No equivale a `GO`.

Significa que:

- sobrevivió Demanda y Competencia;
- sobrevivió shortlist pre-origen;
- tiene origen comercial viable;
- sobrevivió Headroom;
- reunió dataset mínimo;
- mantiene margen suficiente en escenarios preliminares de costo puesto;
- justifica gastar tiempo profesional de despachante.

Los valores comerciales detallados permanecen en la matriz privada y en evidencia operativa; no se reproducen en este documento público.

## 9. Gate profesional externo

Después del `Landed Cost Screen`, Method v2 no intenta sustituir al profesional aduanero.

El gate externo debe validar, para los candidatos finalistas:

- NCM;
- derecho de importación;
- tasa estadística;
- intervenciones;
- certificaciones;
- restricciones;
- tratamiento fiscal;
- terminal;
- despachante;
- transporte local;
- costos reales de nacionalización.

Flujo adoptado:

```text
screening comercial
→ 5–6 candidatos firmes
→ negociación FOB
→ despachante
→ validación profesional
→ actualización económica
→ shortlist final
→ decisión real de importación
```

## 10. Validación de Method v2

El Nicho 3 permitió ejecutar internamente:

```text
Fase 0  — Research Brief
Fase 1  — Mapa del nicho
Fase 2  — Madurez
Fase 3  — Demanda
Fase 4  — Competencia
Fase 5  — Potencial de Marca
Fase 6  — Product Bases
Fase 7  — Shortlist pre-origen
Fase 8  — Screening de origen
Fase 9  — Import Cost Headroom
Fase 10 — Minimum Landed Cost Dataset
Fase 11 — Landed Cost Screen
```

Conclusión:

> **Method v2 queda validado internamente hasta Landed Cost Screen.**

La revisión del despachante se considera deliberadamente un **gate profesional externo**, no una carencia metodológica pendiente de resolver dentro del Intelligence Engine.

## 11. Lecciones consolidadas

1. `publication ≠ Product Base ≠ competitor`.
2. Normalizar arquitectura antes de comparar.
3. Demanda y Competencia deben permanecer separadas.
4. Complejidad es riesgo, no exclusión automática.
5. Origen debe distinguir `EXACTA / COMPARABLE / BENCHMARK`.
6. Headroom filtra antes de Landed Cost.
7. No usar multiplicadores genéricos de importación.
8. No mezclar datos de OEM/modelos distintos.
9. Un RFQ debe congelar configuración antes de cotizar economía.
10. `Economic Landed Cost` y `Cash Outlay` responden preguntas distintas.
11. La precisión profesional se compra sólo para una shortlist pequeña.
12. La negociación de proveedor tiene más valor después del screening económico.
13. El método debe producir descartes y `HOLD` tempranos para evitar investigación innecesaria.
14. El Engine no debe automatizar una fase hasta que la fricción sea repetible y estable.

## 12. Estado operativo al cierre

```text
Matriz comercial vigente:
matrix-aut36-niche3-method-v2-checkpoint-corrected.xlsx

Schema:
full-matrix-v5 0.7.0

Validator:
PASS
errors: 0
warnings: 0
info: 0
limitations: 0

SHA-256:
219d9954acca9fefda5f6edef2eab18f93bf0b4564e45d3e1442f13d6db39a53
```

`aut32` continúa siendo la baseline técnica de Matrix Validator v0.1.0.

`aut36` pasa a ser el snapshot comercial operativo.

## 13. Próximas acciones

1. Procesar la respuesta pendiente de `BASE-PET-004`.
2. Continuar screening sólo hasta reunir aproximadamente 5–6 candidatos firmes.
3. Negociar precio y condiciones con esos proveedores finalistas.
4. Preparar un paquete homogéneo para el despachante.
5. Validar NCM, intervenciones, certificaciones y costos definitivos.
6. Actualizar Landed Cost con datos profesionales.
7. Construir la shortlist final para decisión de importación.
8. Mantener Matrix Validator y `full-matrix-v5 0.7.0` cerrados salvo requerimiento comercial bloqueante.
