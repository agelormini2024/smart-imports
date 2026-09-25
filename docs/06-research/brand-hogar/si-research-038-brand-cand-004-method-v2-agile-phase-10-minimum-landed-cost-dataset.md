---
id: si-research-038
title: BRAND-CAND-004 — Method v2 Agile — F10 Minimum Landed Cost Dataset
description: Dataset público mínimo decision-grade para modelar landed cost de los Product Bases activos de monitoreo doméstico del consumo energético.
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
  - phase-10
  - landed-cost-dataset
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
  - si-research-037
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F10 Minimum Landed Cost Dataset

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input

F9 quedó formalmente cerrada sobre:

```text
matrix-aut68-brand-cand-004-phase9.xlsx
SHA-256: 07b0889646a55f02a844e508935bf292ee2d0b81de41d189f45099bcea737ea1
Result: PASS
```

PB activos:

```text
BASE-HOGAR-016
BASE-HOGAR-017
BASE-HOGAR-019
```

## 2. Regla F10

```text
DECISION-GRADE ≠ PROCUREMENT-GRADE
SAME-SKU > COMPOSITE PROXY
PUBLIC PRICE ≠ FORMAL QUOTE
```

El dataset mínimo busca habilitar un **screen económico F11**, no cerrar una orden de compra.

Campos deseables:

```text
cost
MOQ / tier
packing volume
gross weight
units per carton
voltage / frequency
plug / mounting format
measurement architecture
certifications / documents declared
```

## 3. BASE-HOGAR-016 — plug-level standalone

### Exact-match técnico/costo — COT-0052

TOPEAST KWE-PMB03:

```text
230V / 50Hz
16A max
AU plug opcional
V / Hz / A / PF / W / kWh / costo
memoria mediante batería Ni-MH interna
USD 2,80–4,00
MOQ 100
```

Para modelado se toma conservadoramente:

```text
origin cost = USD 4,00/u
```

### Logistics proxy — COT-0051

Peacefair JGQ1S-01, mismo PB 16A plug-level:

```text
package 18×8×9 cm
CBM/u = 0,001296
gross weight = 0,250 kg/u
```

### Quality flag

```text
DECISION-GRADE
— COMPOSITE PUBLIC PROXY
```

El costo/configuración exacta y la logística todavía no provienen del mismo SKU. El proxy es suficientemente cercano para F11, pero debe permanecer visible.

## 4. BASE-HOGAR-017 — smart plug + monitoring

COT-0048 / Aomytech AUMS01:

```text
AU standard
16A
100–240V / 50–60Hz
energy monitoring
Smart Life
package 10×10×8 cm
CBM/u = 0,000800
gross weight = 0,300 kg/u
```

Se conserva el benchmark comercial público capturado en F8:

```text
origin cost = USD 4,60/u
MOQ benchmark = 50
```

La misma página pública confirma configuración y packing, pero Alibaba puede cambiar moneda/tier/MOQ visible según fecha o locale.

### Quality flag

```text
DECISION-GRADE
— SAME-LISTING PUBLIC CONFIRMED
— COMMERCIAL-DYNAMIC
```

F11 puede modelar con estos datos; antes de procurement debe revalidarse el tier comercial.

## 5. BASE-HOGAR-019 — DIN direct meter

### Cost benchmark — COT-0049

Alibaba / Zhejiang Tongzheng:

```text
80A
single phase
DIN rail
220/230V
50/60Hz
USD 5,60–5,80
MOQ 1
```

Para F11:

```text
origin cost = USD 5,60/u
```

### Logistics/spec mirror — COT-0053

Mirror público del mismo proveedor/producto:

```text
TOMZN / Tongzheng
model SDM220-EC
80A
220/230V
50/60Hz
Class 1
35mm DIN
0,125 kg/u
288 cm³/u
```

### Quality flag

```text
DECISION-GRADE
— SAME-SUPPLIER CROSS-PLATFORM PUBLIC PROXY
```

El costo y la logística no salen de la misma página, pero corresponden al mismo proveedor y configuración de 80A DIN.

## 6. Resumen operativo F11

| Product Base | Cost input | Logistics input | Quality |
|---|---:|---|---|
| BASE-HOGAR-016 | USD 4,00 | 0,001296 m³ / 0,250 kg | COMPOSITE PUBLIC PROXY |
| BASE-HOGAR-017 | USD 4,60 | 0,000800 m³ / 0,300 kg | SAME-LISTING / DYNAMIC |
| BASE-HOGAR-019 | USD 5,60 | 0,000288 m³ / 0,125 kg | SAME-SUPPLIER CROSS-PLATFORM |

Los tres quedan `DECISION-GRADE` para F11.

## 7. Gates que permanecen abiertos

### 016

- packing same-SKU;
- documentación de accuracy;
- validación plug Argentina/AU exacto;
- certificación local.

### 017

- precisión de medición;
- continuidad/histórico;
- cloud dependency;
- seguridad/certificación local;
- revalidación de MOQ/tier comercial.

### 019

- documentación de accuracy/Class;
- certificaciones y requisitos locales;
- seguridad de instalación;
- revisión de uso en tablero y montaje profesional.

## 8. Gate F10

Resultado:

```text
PASS
```

Los tres PB tienen dataset suficiente para modelar Economic Landed Cost con quality flags explícitos.

## 9. Materialización

F10 agrega/completa:

```text
COT-0048 → packaging/peso same-listing
COT-0051 → BASE-HOGAR-016 logistics proxy
COT-0052 → BASE-HOGAR-016 exact-match técnico/costo
COT-0053 → BASE-HOGAR-019 same-supplier logistics mirror

SRC-0438 … SRC-0441
EVID-0265
EVSRC-0541 … EVSRC-0546
```

Archivo preparado:

```text
matrix-aut69-brand-cand-004-phase10-corrected.xlsx
SHA-256: 5707b57c230246ead43d0f0198174cdc5380e8a6d77802fe33bbafcd34d9903e
```

## 10. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut69
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F10 CLOSED
```

## 11. Próxima acción

F10 queda `CLOSED`. Ejecutar `F11 — Landed Cost Screen` en modalidad `AUTO`.

## 12. Changelog

### 2026-09-25 — v0.1.0

- F9 queda formalmente cerrada sobre `aut68 PASS`;
- se completa COT-0048 con packaging/peso;
- se agregan COT-0051..0053;
- 016 queda decision-grade mediante composite public proxy;
- 017 queda decision-grade mediante same-listing public dataset con tier dinámico;
- 019 queda decision-grade mediante same-supplier cross-platform proxy;
- se prepara `matrix-aut69-brand-cand-004-phase10-corrected.xlsx`;
- corrección de aut69: `EVID-0265.Criterio` se normaliza a `Facilidad de Importación`, criterio válido y consistente con F10 del Golden Run;
- `aut69 corrected` obtiene PASS limpio y F10 queda formalmente `CLOSED`;
- siguiente fase: `F11 — Landed Cost Screen` en AUTO.
