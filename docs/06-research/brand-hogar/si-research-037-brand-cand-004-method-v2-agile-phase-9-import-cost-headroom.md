---
id: si-research-037
title: BRAND-CAND-004 — Method v2 Agile — F9 Import Cost Headroom
description: Screening económico de headroom previo a landed cost para los Product Bases activos de monitoreo doméstico del consumo energético.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-25
updated: 2026-09-25
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-004
  - energy-monitoring
  - phase-9
  - headroom
related:
  - si-research-028
  - si-research-029
  - si-research-030
  - si-research-031
  - si-research-032
  - si-research-033
  - si-research-034
  - si-research-035
  - si-research-036
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F9 Import Cost Headroom

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input

F8 quedó formalmente cerrada sobre:

```text
matrix-aut67-brand-cand-004-phase8.xlsx
SHA-256: b5451b383bcad32deb9360ae1adc05a29f975daa3848bd8d2e44d1a6ece096ea
Result: PASS
```

PB activos:

```text
BASE-HOGAR-016
BASE-HOGAR-017
BASE-HOGAR-019
```

## 2. Qué mide F9

```text
HEADROOM
=
MAX ECONOMIC LANDED UNIT COST
÷
COMPARABLE ORIGIN UNIT COST
```

No calcula landed cost real.

```text
HEADROOM ≠ LANDED COST ≠ MARGIN
```

## 3. Supuestos de comparabilidad

Se conserva la baseline del Golden Run:

```text
FX baseline ARS/USD       1.535
channel cost              25%
commercial cost            5%
target margin              25%
max landed / gross price  51,25%
```

El FX 1.535 es un **baseline histórico de proyecto informado por el fundador** y se reutiliza sólo para comparar candidatos bajo una misma referencia. No representa un tipo de cambio actual.

## 4. BASE-HOGAR-016 — Plug-level standalone

Comparable local:

```text
ML-0124
ARS 69.998
16A
```

Comparable origen:

```text
COT-0045
USD 6,12
16A / 230V
plug exacto no confirmado
```

Cálculo:

```text
gross local price USD
= 69.998 / 1.535
≈ USD 45.60

max economic landed cost
= 45.60 × 51,25%
≈ USD 23.37

headroom
= 23.37 / 6,12
≈ 3.82x
```

Resultado:

```text
SURVIVES — STRONG ECONOMIC SIGNAL / COMPOSITE
```

La señal es holgada, pero la comparabilidad todavía es compuesta porque el costo de origen no confirma en este mismo registro el plug Argentina/AU.

## 5. BASE-HOGAR-017 — Smart plug + monitoring

Comparable local:

```text
ML-0128 — Fortitech 16A
ARS 21.999
monitoring explícito
```

Comparable origen:

```text
COT-0047
USD 3,21
16A
AU / Argentina Type I
energy monitoring
```

Cálculo:

```text
gross local price USD
≈ USD 14.33

max economic landed cost
≈ USD 7.34

headroom
≈ 2.29x
```

Resultado:

```text
SURVIVES — FAVORABLE / COMMODITY-CONDITIONED
```

La economía preliminar deja espacio suficiente para F10, pero no resuelve competencia, dependencia Tuya/cloud, precisión ni certificación.

## 6. BASE-HOGAR-019 — DIN direct meter

Comparable local:

```text
ML-0132 — Melech 80A
ARS 26.344
```

Comparable origen:

```text
COT-0049
USD 5,60
80A
DIN
220/230V
```

Cálculo:

```text
gross local price USD
≈ USD 17.16

max economic landed cost
≈ USD 8.80

headroom
≈ 1.57x
```

Resultado:

```text
SURVIVES — CONDITIONED / TIGHTER HEADROOM
```

Sigue vivo, pero con menor colchón. Packing, flete, derechos, certificaciones, seguridad e instalación pueden consumir rápidamente la diferencia.

## 7. Comparación

| Product Base | Precio local usado | Costo origen usado | Max landed económico | Headroom | F9 |
|---|---:|---:|---:|---:|---|
| BASE-HOGAR-016 | ARS 69.998 | USD 6,12 | USD 23.37 | 3.82x | STRONG / COMPOSITE |
| BASE-HOGAR-017 | ARS 21.999 | USD 3,21 | USD 7.34 | 2.29x | FAVORABLE / CONDITIONED |
| BASE-HOGAR-019 | ARS 26.344 | USD 5,60 | USD 8.80 | 1.57x | SURVIVES / TIGHTER |

## 8. Gate F9

Resultado:

```text
PASS
```

Los tres PB continúan a F10.

Prioridad económica:

```text
016 → mayor colchón
017 → colchón favorable, commodity risk alto
019 → colchón menor, requiere dataset logístico disciplinado
```

Esto **no es un ranking final de producto**; sólo describe la holgura económica preliminar de los tres casos.

## 9. Qué debe cerrar F10

Para cada PB activo:

```text
same-SKU cost
MOQ / price tier
packing dimensions
gross weight
units per carton
voltage / frequency
plug / form factor cuando corresponda
metering architecture
certifications / documents declared
```

Especialmente:

```text
016 → cerrar 16A + plug Argentina/AU + packing/peso + accuracy
017 → cerrar same-SKU + packing/peso + platform dependency
019 → cerrar same-SKU + packing/peso + accuracy/class + electrical documentation
```

## 10. Materialización

Se agregan:

```text
EVID-0264
SRC-0437
EVSRC-0540
```

y se actualizan notas F9 de `BASE-HOGAR-016`, `017` y `019`.

Archivo preparado:

```text
matrix-aut68-brand-cand-004-phase9.xlsx
SHA-256: 07b0889646a55f02a844e508935bf292ee2d0b81de41d189f45099bcea737ea1
```

## 11. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut68
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F9 CLOSED
```

Validación oficial:

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: 07b0889646a55f02a844e508935bf292ee2d0b81de41d189f45099bcea737ea1
```

## 12. Próxima acción

F9 queda `CLOSED`. Ejecutar `F10 — Minimum Landed Cost Dataset` en modalidad `AUTO`.

## 13. Changelog

### 2026-09-25 — v0.1.0

- F8 queda formalmente cerrada sobre `aut67 PASS`;
- se aplica el mismo headroom framework del Golden Run;
- 016 ~3.82x;
- 017 ~2.29x;
- 019 ~1.57x;
- los tres PB sobreviven a F10;
- se prepara `matrix-aut68-brand-cand-004-phase9.xlsx`;
- `aut68` obtiene PASS limpio y F9 queda formalmente `CLOSED`;
- siguiente fase: `F10 — Minimum Landed Cost Dataset` en AUTO.
