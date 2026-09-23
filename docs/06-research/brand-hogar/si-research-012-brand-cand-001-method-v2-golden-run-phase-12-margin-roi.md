---
id: si-research-012
title: BRAND-CAND-001 — Method v2 Golden Run — Fase 12 Margin + ROI
description: Cierre decision-grade de Fase 12 para BRAND-CAND-001, con interpretación formal de margen, ROI, robustez y gate hacia shortlist final.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-23
updated: 2026-09-23
tags:
  - smart-imports
  - brand-hogar
  - brand-cand-001
  - method-v2
  - golden-run
  - margin
  - roi
  - shortlist
related:
  - si-research-009
  - si-research-010
  - si-research-011
  - si-roadmap-002
---

# SI-RESEARCH-012 — BRAND-CAND-001 — Method v2 Golden Run — Fase 12 Margin + ROI

> Margen positivo no equivale a una oportunidad suficientemente atractiva.

## 1. Objetivo

Cerrar la Fase 12 de Method v2 para `BRAND-CAND-001` interpretando formalmente los resultados de margen y ROI ya derivados de los escenarios de Fase 11.

F12 no recalcula Landed Cost y no abre negociación de compra.

```text
F11
→ modela Economic Landed Cost

F12
→ interpreta Margin + ROI
→ prueba robustez
→ conserva calidad de evidencia y condiciones técnicas
→ decide qué Product Bases justifican llegar a F13
```

## 2. Criterio económico

El indicador económico principal es el margen sobre precio neto.

```text
Precio Neto
= Precio Venta × (1 - costo de canal)

Margen Unitario
= Precio Neto
- Economic Landed Cost
- Costos Comerciales

Margen %
= Margen Unitario / Precio Neto
```

Para esta Golden Run se conserva el objetivo económico utilizado desde Fase 9:

```text
Margen objetivo
= 25 % sobre precio neto
```

Lectura mecánica:

```text
Margen >= objetivo
→ OBJETIVO_CUMPLIDO

Margen > 0 y < objetivo
→ POSITIVO_BAJO_OBJETIVO

Margen <= 0
→ estructura económica negativa
```

## 3. ROI utilizado

La matriz calcula:

```text
ROI SOBRE COSTO ECONÓMICO
= Margen Unitario / Economic Landed Cost
```

Este indicador ayuda a leer eficiencia económica, pero no representa:

- ROI anual del negocio;
- retorno sobre capital total;
- cash-on-cash return;
- rotación de inventario;
- flujo de caja completo;
- recuperabilidad fiscal;
- tiempo hasta recuperar la inversión.

Por lo tanto:

```text
ROI SOBRE COSTO ECONÓMICO
≠
RETORNO SOBRE CAPITAL TOTAL
```

## 4. Margen como indicador primario

El ROI no se convierte en un segundo umbral independiente porque deriva de la misma estructura económica que el margen.

```text
Margen %
→ indicador primario

ROI sobre costo
→ indicador complementario
```

Crear otro threshold rígido para ROI duplicaría parcialmente el mismo criterio.

Este aprendizaje queda registrado para retrospectiva antes de modificar formalmente Method v2.

## 5. Robustez

Cada Product Base se interpreta en dos cantidades:

```text
50 unidades
100 unidades
```

La escala se usa como prueba de robustez, no para elegir automáticamente el escenario más favorable.

```text
50 cumple + 100 cumple
→ economía robusta dentro del rango modelado

50 no cumple + 100 cumple
→ dependencia relevante de escala

50 no cumple + 100 no cumple
→ economía ajustada o débil

margen <= 0
→ señal económica desfavorable
```

Cuando resulta útil, F12 también observa sensibilidad del precio de venta para determinar si la conclusión depende excesivamente de un benchmark local específico.

## 6. Resultado — BASE-HOGAR-003

Arquitectura:

```text
detección puntual
+
actuador retrofit sobre válvula existente
```

Resultado:

- ambos escenarios conservan margen positivo;
- ambos escenarios quedan por debajo del objetivo económico;
- aumentar de 50 a 100 unidades mejora el resultado pero no cambia su naturaleza;
- la estructura económica ajustada se combina con dependencia de `Tuya Cloud`, compatibilidad mecánica e instalación/configuración.

Gate:

```text
F12 → STOP — REOPENABLE
```

No corresponde `HOLD`: la evidencia actual es suficiente para una decisión.

Condiciones de reapertura:

- costo materialmente inferior para la misma arquitectura;
- arquitectura equivalente con operación local/offline;
- evidencia defendible de un precio de venta materialmente superior;
- solución mecánica y operativamente más simple.

La reapertura requiere evidencia nueva que cambie la estructura; no negociación fina destinada solamente a hacer cerrar la planilla.

## 7. Resultado — BASE-HOGAR-006

Arquitectura:

```text
protección automática específica de artefacto
```

Resultado:

- cumple ampliamente el objetivo económico en ambos escenarios;
- la lectura permanece robusta ante una reducción material del precio de venta de referencia;
- el precio de muestra utilizado como proxy de origen es conservador;
- la principal incertidumbre deja de ser económica.

Condiciones abiertas:

- compatibilidad eléctrica para Argentina;
- configuración técnica exacta;
- aspectos regulatorios aplicables;
- precio productivo e Incoterm definitivos.

Gate:

```text
F12 → PASS TO F13 — CONDITIONED
```

La holgura económica no neutraliza una incertidumbre técnica capaz de volver inviable el producto.

## 8. Resultado — BASE-HOGAR-002

Arquitectura:

```text
detección puntual
+
válvula central en línea
```

Resultado:

- cumple el objetivo económico en ambos escenarios;
- la escala mejora la estructura pero no es necesaria para rescatarla;
- la economía conserva margen de seguridad frente a sensibilidades razonables;
- la incertidumbre dominante es técnica y operativa.

Condiciones abiertas:

- comparabilidad exacta para uso residencial central;
- diámetro y rosca;
- compatibilidad hidráulica;
- instalación;
- confiabilidad de la válvula;
- aspectos regulatorios y de postventa.

Gate:

```text
F12 → PASS TO F13 — CONDITIONED
```

## 9. Product Bases fuera del análisis económico activo

No se alteran estados anteriores por conveniencia de F12:

```text
BASE-HOGAR-004
→ WATCHLIST

BASE-HOGAR-005
→ PAUSED
```

No se incorporan artificialmente a la shortlist para alcanzar una cantidad predeterminada.

## 10. Funnel resultante

```text
Fase 6
→ 5 CANDIDATE_PB

Fase 7
→ 3 ACTIVE
→ 1 WATCHLIST
→ 1 PAUSED

Fases 8–11
→ 3 PB completan evaluación económica

Fase 12
→ BASE-HOGAR-002: PASS TO F13 — CONDITIONED
→ BASE-HOGAR-006: PASS TO F13 — CONDITIONED
→ BASE-HOGAR-003: STOP — REOPENABLE
```

F13 recibe activamente dos Product Bases.

Esto no equivale a elegir un ganador ni a decidir una compra.

## 11. Aprendizajes para retrospectiva

### 11.1 Margen positivo no alcanza

```text
MARGEN > 0
≠
OPORTUNIDAD ECONÓMICAMENTE ATRACTIVA
```

`BASE-HOGAR-003` demuestra que una unidad económica puede ser positiva y aun así no justificar capital, complejidad operativa y tiempo frente a alternativas mejores.

### 11.2 Cumplir margen tampoco significa listo para importar

```text
OBJETIVO ECONÓMICO CUMPLIDO
≠
PRODUCTO LISTO PARA COMPRA
```

`BASE-HOGAR-002` y `BASE-HOGAR-006` mantienen condiciones técnicas materiales.

### 11.3 Robustez importa

Una conclusión que resiste más de un escenario es más útil que un resultado dependiente de un único punto favorable de la planilla.

### 11.4 No duplicar métricas

Una métrica derivada no debe transformarse automáticamente en un criterio independiente cuando mide esencialmente la misma relación económica que el indicador principal.

## 12. Simplicidad temprana

Durante la Golden Run se mantiene como observación emergente el sesgo hacia productos con menor complejidad innecesaria en:

- importación;
- regulación;
- logística;
- instalación;
- compatibilidad;
- seguridad;
- postventa;
- dependencia de app/cloud.

Este criterio todavía no modifica formalmente Method v2.

Debe evaluarse en la retrospectiva después de completar la Golden Run.

## 13. Materialización

Snapshot:

```text
matrix-aut43-brand-cand-001-phase12.xlsx
```

SHA-256:

```text
5b602747404dce8584c3735552009487607ffe4a642c56bb05b8b9aba0663315
```

Validación:

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

La materialización agrega:

- consolidación formal de F12;
- evidencia `Margin + ROI`;
- interpretación por Product Base;
- `STOP — REOPENABLE` para `BASE-HOGAR-003`;
- `PASS TO F13 — CONDITIONED` para `BASE-HOGAR-002` y `BASE-HOGAR-006`;
- actualización del estado acumulado de los Product Bases.

No crea nuevas simulaciones económicas porque F12 interpreta las ya materializadas en F11.

## 14. Confidencialidad

Este documento público conserva:

- método;
- criterios;
- resultados cualitativos;
- gates;
- condiciones abiertas;
- aprendizajes.

No publica:

- precios de compra privados;
- cotizaciones privadas;
- detalle exacto de simulaciones comerciales;
- condiciones negociadas;
- estrategia de negociación;
- datos de contacto;
- documentos originales de proveedor.

La matriz operativa conserva el detalle estructurado de trabajo.

## 15. Estado de Fase 12

```text
F12 conceptual
→ COMPLETE

materialización
→ aut43

Matrix Validator
→ PASS limpio

checkpoint documental
→ SI-RESEARCH-012

gate
→ BASE-HOGAR-002: PASS TO F13 — CONDITIONED
→ BASE-HOGAR-003: STOP — REOPENABLE
→ BASE-HOGAR-006: PASS TO F13 — CONDITIONED
```

## 16. Próximo paso

Abrir:

```text
F13 — Shortlist final
```

F13 debe consolidar, sin decidir todavía una compra:

- economía;
- calidad de evidencia;
- complejidad de importación;
- complejidad de instalación;
- riesgo técnico/regulatorio;
- postventa;
- Brand Fit;
- facilidad de explicar y vender;
- condiciones abiertas.

Input activo de F13:

```text
BASE-HOGAR-002
BASE-HOGAR-006
```

`BASE-HOGAR-003` queda fuera del camino activo y sólo se reabre ante evidencia material nueva.
