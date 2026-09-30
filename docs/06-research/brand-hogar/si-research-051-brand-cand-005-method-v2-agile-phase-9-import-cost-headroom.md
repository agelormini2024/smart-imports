---
id: si-research-051
title: BRAND-CAND-005 — Method v2 Agile — F9 Import Cost Headroom
description: Screening económico de headroom previo a landed cost para Product Bases activos de compostaje y procesamiento doméstico de residuos orgánicos.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-28
updated: 2026-09-28
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-005
  - organic-waste
  - phase-9
  - headroom
phase: business-intelligence
---

# BRAND-CAND-005 — Method v2 Agile — F9 Import Cost Headroom

Fecha: 2026-09-28  
Estado: `CLOSED`

## 1. Input

F8 quedó formalmente cerrada sobre:

```text
matrix-aut84-brand-cand-005-phase8.xlsx
SHA-256: 6968ac9aca61e2ef9be85bafaffa6a81c417ab1fe310c7baecb69c57431b3bf0
Result: PASS
```

PB activos:

```text
BASE-HOGAR-024
BASE-HOGAR-025
BASE-HOGAR-028
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

Se conserva la baseline histórica del proyecto:

```text
FX baseline ARS/USD       1.535
channel cost              25%
commercial cost            5%
target margin              25%
max landed / gross price  51,25%
```

El FX `1.535` se reutiliza únicamente para comparabilidad transversal entre candidatos. No representa un tipo de cambio actual.

## 4. BASE-HOGAR-024 — Compostera modular

Comparable local:

```text
ML-0143
ARS 94.558
60 L modular
lombrices opcionales / A3-compatible
```

Comparable origen:

```text
COT-0054
USD 24,29
5-tray modular worm composter
MOQ 50
```

Cálculo:

```text
gross local price USD
= 94.558 / 1.535
≈ USD 61,60

max economic landed cost
= 61,60 × 51,25%
≈ USD 31,57

headroom
= 31,57 / 24,29
≈ 1,30x
```

Resultado:

```text
SURVIVES — TIGHT / COMPOSITE
```

La señal es estrecha y además compuesta.

F10 debe cerrar:

- exact-match 40–60 L;
- dimensiones;
- peso;
- nesting;
- unidades/caja;
- volumen real;
- MOQ/tier comparable.

Un flete volumétrico desfavorable puede consumir rápidamente la diferencia.

## 5. BASE-HOGAR-025 — Tumbler 120 L

Comparable local:

```text
ML-0140
ARS 188.340
120 L
doble cámara
+1000 vendidos visibles
```

Comparable origen:

```text
COT-0056
USD 28,80
120 L
dual chamber
package 62 × 56 × 20 cm
11 kg
MOQ 439
```

Cálculo:

```text
gross local price USD
= 188.340 / 1.535
≈ USD 122,70

max economic landed cost
≈ USD 62,88

headroom
= 62,88 / 28,80
≈ 2,18x
```

Resultado:

```text
SURVIVES — FAVORABLE / LOGISTICS-CONDITIONED
```

La holgura preliminar es favorable, pero el producto es grande y pesado.

F10 debe preservar la evidencia pública de packing y validar si ese packing corresponde al same-SKU exacto y al tier de costo utilizado.

## 6. BASE-HOGAR-028 — Food recycler térmico

Comparable local:

```text
ML-0149 — Fryline 4 L
ARS 1.101.000
```

Se usa el menor precio local visible entre los tres comparables con precio recuperado para evitar una lectura optimista.

Comparable origen:

```text
COT-0058 — Cleesink MLT-450
USD 140
4,5 L
220 V
50/60 Hz
package 39 × 33,8 × 33,8 cm
7,3 kg
```

Cálculo:

```text
gross local price USD
= 1.101.000 / 1.535
≈ USD 717,26

max economic landed cost
≈ USD 367,60

headroom
= 367,60 / 140
≈ 2,63x
```

Resultado:

```text
SURVIVES — STRONG PRELIMINARY / TECH-SERVICE-CONDITIONED
```

La señal económica preliminar es holgada.

Eso no resuelve:

- 220–240 V / 50 Hz exactos;
- homologación/certificaciones;
- ruido real;
- filtros;
- repuestos;
- motor/cuchillas;
- garantía;
- defect rate;
- service burden;
- consumo eléctrico;
- claims sobre output.

Por lo tanto:

```text
STRONG HEADROOM
≠
GOOD FIRST PRODUCT
```

## 7. Comparación

| Product Base | Precio local usado | Costo origen usado | Max landed económico | Headroom | F9 |
|---|---:|---:|---:|---:|---|
| BASE-HOGAR-024 | ARS 94.558 | USD 24,29 | USD 31,57 | 1,30x | TIGHT / COMPOSITE |
| BASE-HOGAR-025 | ARS 188.340 | USD 28,80 | USD 62,88 | 2,18x | FAVORABLE / LOGISTICS-CONDITIONED |
| BASE-HOGAR-028 | ARS 1.101.000 | USD 140 | USD 367,60 | 2,63x | STRONG PRELIMINARY / TECH-SERVICE-CONDITIONED |

Esto no constituye un ranking final de producto.

Describe únicamente la holgura económica preliminar antes del landed cost real.

## 8. Gate F9

Resultado:

```text
PASS
```

Los tres PB continúan a F10.

Lectura:

```text
024 → sobrevive con colchón estrecho; el packing puede definir su continuidad
025 → holgura favorable, pero logística física domina el próximo gate
028 → holgura alta, pero complejidad técnica/postventa permanece dominante
```

## 9. Qué debe cerrar F10

Para cada PB activo:

```text
same-SKU cost
MOQ / price tier
packing dimensions
gross weight
units per carton
CBM / volumetric weight
material / mechanism exacto
relevant certifications declared
```

Especialmente:

```text
024
→ exact-match 40–60 L
→ packing / nesting
→ peso
→ material
→ drainage
→ MOQ

025
→ confirmar same-SKU packing
→ confirmar tier USD 28,80
→ MOQ real
→ estructura desmontada / units per carton

028
→ 220–240V / 50Hz exactos
→ same-SKU cost
→ packing / weight
→ filter availability / cost
→ repuestos
→ certifications declared
→ warranty / service-relevant specs
```

## 10. Materialización

Se agregan:

```text
SRC-0472
EVID-0278
EVSRC-0610
```

y se actualizan las notas de:

```text
BASE-HOGAR-024
BASE-HOGAR-025
BASE-HOGAR-028
```

Archivo preparado:

```text
matrix-aut85-brand-cand-005-phase9.xlsx
SHA-256: 7fb8169ecbc12ad31f4ad35e62be54a77107ab8f5c649c2d46081669ce50c2e1
```

## 11. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut85
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
SHA-256: 7fb8169ecbc12ad31f4ad35e62be54a77107ab8f5c649c2d46081669ce50c2e1
Report: aut85-brand-cand-005-phase9-validation-report.json
```

F10 queda formalmente abierta después de este cierre.

## 12. Próxima acción

Validar `aut85`.

Resultado ejecutado:

```text
F9 CLOSED — aut85 PASS
→ F10 — Minimum Landed Cost Dataset
→ AUTO
```
