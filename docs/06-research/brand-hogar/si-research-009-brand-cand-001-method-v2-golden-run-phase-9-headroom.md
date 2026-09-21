---
id: si-research-009
title: BRAND-CAND-001 — Method v2 Golden Run — Fase 9 Headroom
description: Cierre conceptual y operativo de Fase 9 — Import Cost Headroom de BRAND-CAND-001.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-21
updated: 2026-09-21
tags:
  - smart-imports
  - brand-hogar
  - brand-candidate
  - method-v2
  - golden-run
  - headroom
related:
  - si-research-007
  - si-research-008
  - si-roadmap-002
  - brand-cand-001
---

# SI-RESEARCH-009 — BRAND-CAND-001 — Method v2 Golden Run — Fase 9 Headroom

## 1. Objetivo

Documentar el cierre de `Fase 9 — Import Cost Headroom` de la Golden Run de `BRAND-CAND-001 — detección doméstica de fugas + corte automático`.

El objetivo de esta fase no es estimar todavía el costo real de importación. El Headroom funciona como filtro previo para decidir qué Product Bases justifican invertir tiempo en el `Minimum Landed Cost Dataset` de Fase 10.

Principio operativo:

```text
Import Cost Headroom
=
costo puesto máximo compatible con el margen objetivo
÷
costo de origen comparable
```

El indicador responde:

> ¿Cuánto espacio económico existe antes de que el costo puesto deje de ser compatible con el margen objetivo?

No responde cuánto costará efectivamente importar.

## 2. Baseline de ejecución

```text
Input: BRAND-CAND-001
Fases previas: 0–8 cerradas
Snapshot de entrada: matrix-aut39-brand-cand-001-phase8.xlsx
Snapshot de cierre F9: matrix-aut40-brand-cand-001-phase9.xlsx
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
SHA-256: 525e8aefb5db96a30b8d5565f05fd9c1ac283f1a8eafffbbd7d5f75f9ecc4512
```

`aut32` continúa siendo la baseline técnica de release. `aut40` pasa a ser el snapshot comercial vigente de la Golden Run.

## 3. Alcance

Se evaluaron únicamente los tres Product Bases activos que sobrevivieron Fases 7 y 8:

```text
BASE-HOGAR-002
BASE-HOGAR-003
BASE-HOGAR-006
```

No se ejecutó Headroom activo para:

```text
BASE-HOGAR-004 → WATCHLIST
BASE-HOGAR-005 → PAUSED
```

La ausencia de cálculo en estos PB es deliberada y no representa falta de evidencia.

## 4. Reglas aplicadas

### 4.1 Headroom no es arbitraje de precios

```text
PRECIO LOCAL ÷ PRECIO ORIGEN ≠ IMPORT COST HEADROOM
```

El cálculo debe partir del costo puesto máximo compatible con el margen objetivo.

### 4.2 Comparabilidad antes del ratio

No se considera válido comparar sin ajuste conceptual:

```text
componente local
vs.
solución completa de origen
```

ni:

```text
kit local completo
vs.
actuador de origen aislado
```

La arquitectura comparada debe ser defendiblemente equivalente o estar declarada como proxy.

### 4.3 Calidad de evidencia

Un Headroom aparentemente alto basado en una publicación premium/importada sin señal transaccional no tiene la misma fuerza que una referencia respaldada por demanda observable.

La evidencia económica se interpreta junto con:

- comparabilidad;
- calidad de fuente;
- señal comercial;
- complejidad técnica;
- instalación;
- dependencia de ecosistema/cloud;
- confiabilidad del cierre.

## 5. Resultado por Product Base

### 5.1 BASE-HOGAR-002 — sensores puntuales + válvula central en línea

Estado F9:

```text
SURVIVES
PASS TO F10
CONDITION: TECHNICAL / INSTALLATION
```

La señal de Headroom es fuerte incluso usando un escenario conservador de referencia local y costo de origen.

El principal riesgo del PB no aparece hoy en el espacio económico sino en:

- intervención hidráulica;
- compatibilidad de rosca/diámetro;
- instalación central;
- comportamiento fail-safe;
- confiabilidad de la válvula;
- responsabilidad de soporte y posventa.

Conclusión:

> `BASE-HOGAR-002` justifica reunir el dataset mínimo de Landed Cost. El gate siguiente debe concentrarse en configuración exacta, packing, logística y compatibilidad técnica, no en ampliar discovery.

### 5.2 BASE-HOGAR-003 — sensores puntuales + actuador retrofit

Estado F9:

```text
SURVIVES — CONDITIONED
PASS TO F10
CONDITION: ECONOMIC + INTEGRATION
```

La lectura conservadora muestra un Headroom sensiblemente más estrecho que en `BASE-HOGAR-002`.

El PB conserva interés porque su propuesta de valor no es vender un actuador aislado sino una solución:

```text
detección
+ corte automático
+ instalación retrofit
+ compatibilidad clara
+ automatización confiable
+ soporte local
```

El benchmark premium de sistema completo se conserva como referencia superior, pero no se usa como señal económica primaria.

Riesgos principales:

- precio defendible;
- compatibilidad mecánica;
- arquitectura sensor → actuador;
- dependencia cloud/local según proveedor;
- integración y experiencia de instalación.

Conclusión:

> `BASE-HOGAR-003` sobrevive F9, pero F10 debe verificar si la configuración funcional completa mantiene una economía defendible una vez incorporados packing, logística y condiciones comerciales reales.

### 5.3 BASE-HOGAR-006 — protección específica de artefacto

Estado F9:

```text
SURVIVES
PASS TO F10
VARIANT TO PRIORITIZE: APPLIANCE-SPECIFIC
```

La variante `appliance-specific` conserva suficiente espacio económico para justificar profundización aun usando una referencia de origen desfavorable para screening.

El benchmark local utilizado es premium/importado y no se interpreta como demanda transaccional validada.

Durante la fase se refuerza una distinción ya observada en F8:

```text
GENERIC LOCALIZED PROTECTION
≠
APPLIANCE-SPECIFIC PROTECTION
```

La diferencia empieza a mostrar impacto económico además de funcional.

No se divide todavía `BASE-HOGAR-006`. La posible separación queda reservada para la retrospectiva final de la Golden Run.

Conclusión:

> F10 debe priorizar la variante appliance-specific y obtener condiciones comerciales, packing y documentación suficientes para un Landed Cost defendible.

## 6. Decisión consolidada de Fase 9

```text
BASE-HOGAR-002 → SURVIVES / PASS TO F10
BASE-HOGAR-003 → SURVIVES — CONDITIONED / PASS TO F10
BASE-HOGAR-006 → SURVIVES / PASS TO F10

BASE-HOGAR-004 → WATCHLIST / no F9 activa
BASE-HOGAR-005 → PAUSED / no F9 activa
```

Ningún PB activo queda eliminado en Fase 9.

Esto no constituye selección de producto final, proveedor ni decisión de compra.

## 7. Aprendizajes de Golden Run

Registrar para la retrospectiva, sin modificar todavía Method v2 ni el Engine:

```text
HEADROOM ≠ PRICE ARBITRAGE
```

```text
HEADROOM REQUIRES COMPARABLE ARCHITECTURE
```

```text
HEADROOM MUST CARRY EVIDENCE QUALITY
```

También queda reforzado:

```text
GENERIC LOCALIZED PROTECTION
≠
APPLIANCE-SPECIFIC PROTECTION
```

No se formalizan umbrales universales de aprobación a partir de una sola Golden Run.

## 8. Confidencialidad

Los ratios exactos, precios, MOQ, cotizaciones, simulaciones y condiciones comerciales utilizados para materializar F9 permanecen en la matriz operativa y registros privados.

El repositorio público conserva:

- definición metodológica;
- estado;
- conclusiones consolidadas;
- riesgos;
- decisiones de gate;
- próxima acción.

## 9. Gate siguiente

Fase 9 queda documentalmente cerrada con `aut40` validada.

Siguiente gate:

```text
F10 — Minimum Landed Cost Dataset
```

Para cada PB sobreviviente se debe reunir, como mínimo:

- configuración exacta;
- Incoterm aplicable;
- MOQ/tier relevante;
- packing;
- unidades por caja;
- dimensiones de caja;
- CBM;
- peso bruto/neto;
- datos técnicos/documentales necesarios para clasificación y logística.

No abrir `Landed Cost` hasta disponer de un dataset mínimo defendible.

## 10. Estado final del checkpoint

```text
Fase 9 conceptual → COMPLETADA
Materialización → aut40
Matrix Validator → PASS limpio
Checkpoint documental → SI-RESEARCH-009
Próximo gate → Fase 10
```

## 11. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-21 | Cierre documental de Fase 9 — Import Cost Headroom de BRAND-CAND-001; aut40 PASS y siguiente gate Fase 10. |
