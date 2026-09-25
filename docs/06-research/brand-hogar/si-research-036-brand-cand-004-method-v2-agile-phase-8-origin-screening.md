---
id: si-research-036
title: BRAND-CAND-004 — Method v2 Agile — F8 Origin Screening
description: Screening público de origen para Product Bases activos de monitoreo doméstico del consumo energético.
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
  - phase-8
  - origin-screening
related:
  - si-research-028
  - si-research-029
  - si-research-030
  - si-research-031
  - si-research-032
  - si-research-033
  - si-research-034
  - si-research-035
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F8 Origin Screening

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input

F7 quedó formalmente cerrada sobre:

```text
matrix-aut66-brand-cand-004-phase7.xlsx
SHA-256: 4ac98fdeec6d357a6d861de095341c542a216558e3887f14e67aacd7a4798474
Result: PASS
```

Shortlist activa:

```text
BASE-HOGAR-016 — CORE / FIRST-STAGE FIT
BASE-HOGAR-017 — CONDITIONED / CORE / COMMODITY CHECK
BASE-HOGAR-019 — CONDITIONED / CORE TECHNICAL
```

## 2. Reglas

```text
ORIGIN CONFIRMED ≠ SUPPLIER SELECTED
PUBLIC LISTING ≠ COMMERCIAL QUOTE
LISTING ATTRIBUTE ≠ MEASUREMENT VALIDATED
AU/ARGENTINA TYPE-I CLAIM ≠ LOCAL CERTIFICATION VERIFIED
CE / ROHS / IEC DECLARED ≠ DOCUMENTS VERIFIED
```

F8 busca disponibilidad y comparabilidad pública de origen, no supplier due diligence ni procurement-grade dataset.

## 3. BASE-HOGAR-016 — Medidor enchufable standalone

### COT-0045 — cost / architecture comparator

Proveedor: Ningbo Meng Qili Electrical Technology Co., Ltd.  
Plataforma: Alibaba.

Evidencia pública:

```text
16A
230V
LCD power / energy meter socket
USD 6,12
MOQ 100
```

Limitación:

> El resultado capturado no cierra el estándar de enchufe exacto.

### COT-0046 — AU plug technical comparator

Proveedor: Ningbo Cowell Electronics & Technology Co., Ltd.  
Modelo: PMB05-AU.

Evidencia pública:

```text
AU plug
LCD
power / energy monitoring
10A
MOQ 100
CE / RoHS declarados
```

### Resultado F8

```text
ORIGIN CONFIRMED
— COMPOSITE PUBLIC EVIDENCE
— CORE
```

Existe origen claramente comparable, pero el target ideal:

```text
16A
+ plug Argentina/AU
+ 220–240V / 50Hz
+ memoria/persistencia
+ accuracy documentada
```

todavía no está cerrado en un mismo SKU público. Esa necesidad se traslada a F10.

## 4. BASE-HOGAR-017 — Smart plug + monitoring

### COT-0047 — SIXWGH AU/AR Type I

Proveedor: Shenzhen Wenhui Technology Development Co., Ltd.

Evidencia pública:

```text
16A
100–240V
AU / Argentina Type I
energy monitoring
Tuya / Smart Life
USD 3,21–3,74
MOQ 30
```

### COT-0048 — Aomytech Argentina/AU

Proveedor: Jiujiang Aomytech Co., Limited.

Evidencia pública:

```text
16A
Argentina / AU form factor
energy monitoring
Wi-Fi / Smart Life
USD 4,60–5,50
MOQ 50
```

### Resultado F8

```text
ORIGIN CONFIRMED
— CONDITIONED
— COMMODITY RISK
```

La disponibilidad es abundante. La propia abundancia confirma el problema competitivo: `Tuya + 16A + energy monitoring` es altamente replicable.

Gates abiertos:

- precisión real;
- persistencia/histórico;
- comportamiento sin Internet;
- dependencia de plataforma;
- certificación local;
- seguridad;
- diferenciación no superficial.

## 5. BASE-HOGAR-019 — Medidor DIN directo

### COT-0049 — Tongzheng 80A DIN

Proveedor: Zhejiang Tongzheng Electric Co., Ltd.

Evidencia pública:

```text
single-phase
DIN rail
80A
220 / 230V
50 / 60Hz
LCD
USD 5,60–5,80
MOQ 1
```

### COT-0050 — Stron STE18-D1-W

Proveedor: Hunan Stron Smart Co., Ltd.

Evidencia pública:

```text
230V
50Hz
DIN35
Class 1.0
hasta 80A
LCD
IEC62052-11 / IEC62053-21 declarados
```

### Resultado F8

```text
ORIGIN CONFIRMED
— CONDITIONED
— CORE TECHNICAL
```

La disponibilidad técnica es clara. Los gates relevantes no son existencia de producto sino:

- accuracy verificable;
- certificaciones/documentos;
- instalación y seguridad;
- compatibilidad local;
- memoria/retención;
- requisitos regulatorios/importación.

## 6. Resultado consolidado

```text
BASE-HOGAR-016
ORIGIN CONFIRMED — COMPOSITE PUBLIC EVIDENCE / CORE

BASE-HOGAR-017
ORIGIN CONFIRMED — CONDITIONED / COMMODITY RISK

BASE-HOGAR-019
ORIGIN CONFIRMED — CONDITIONED / CORE TECHNICAL
```

Los tres PB permanecen activos para F9.

## 7. Gate F8

Resultado:

```text
PASS
```

Razón:

- los tres Product Bases tienen disponibilidad pública de origen;
- 017 y 019 cuentan con comparables fuertes y de bajo MOQ público;
- 016 dispone de evidencia compuesta suficiente para continuar, con un gap explícito de exact-match;
- no hace falta contactar proveedores para decidir si existe origen comparable.

## 8. Materialización

Se agregan:

```text
COT-0045 … COT-0050
SRC-0430 … SRC-0436
EVID-0263
EVSRC-0533 … EVSRC-0539
```

Archivo preparado:

```text
matrix-aut67-brand-cand-004-phase8.xlsx
SHA-256: b5451b383bcad32deb9360ae1adc05a29f975daa3848bd8d2e44d1a6ece096ea
```

## 9. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut67
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F8 CLOSED
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
SHA-256: b5451b383bcad32deb9360ae1adc05a29f975daa3848bd8d2e44d1a6ece096ea
```

## 10. Próxima acción

F8 queda `CLOSED`. Ejecutar `F9 — Import Cost Headroom` en modalidad `AUTO`.

F9 aplicará la misma disciplina del Golden Run:

```text
HEADROOM ≠ LANDED COST ≠ MARGIN
```

y utilizará la baseline de proyecto para comparabilidad entre candidatos, no como cotización FX actual.

## 11. Fuentes públicas principales

- Alibaba — Ningbo Meng Qili: 16A / 230V LCD power meter socket, USD 6,12, MOQ 100.
- Alibaba — Ningbo Cowell PMB05-AU: AU plug power meter, 10A, CE/RoHS declarados.
- Alibaba — Shenzhen Wenhui SIXWGH: AU/Argentina Type I, 16A, energy monitoring, USD 3,21–3,74, MOQ 30.
- Alibaba — Jiujiang Aomytech: Argentina/AU 16A energy monitoring smart plug, USD 4,60–5,50, MOQ 50.
- Alibaba — Zhejiang Tongzheng: DIN single-phase 80A, 220/230V, 50/60Hz, USD 5,60–5,80, MOQ 1.
- Alibaba — Hunan Stron STE18-D1-W: DIN 230V/50Hz, Class 1.0, hasta 80A, estándares IEC declarados.

## 12. Changelog

### 2026-09-25 — v0.1.0

- F7 queda formalmente cerrada sobre `aut66 PASS`;
- se ejecuta sourcing público sólo para BASE-HOGAR-016/017/019;
- se registran COT-0045..0050;
- los tres PB confirman origen;
- 016 queda con evidencia pública compuesta;
- 017 confirma origen abundante y commodity risk;
- 019 confirma origen técnico comparable;
- se prepara `matrix-aut67-brand-cand-004-phase8.xlsx`;
- `aut67` obtiene PASS limpio y F8 queda formalmente `CLOSED`;
- siguiente fase: `F9 — Import Cost Headroom` en AUTO.
