---
id: si-research-050
title: BRAND-CAND-005 — Method v2 Agile — F8 Origin Screening
description: Screening público de origen para Product Bases activos de compostaje y procesamiento doméstico de residuos orgánicos.
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
  - phase-8
  - origin-screening
phase: business-intelligence
---

# BRAND-CAND-005 — Method v2 Agile — F8 Origin Screening

Fecha: 2026-09-28  
Estado: `CLOSED`

## 1. Input

F7 quedó formalmente cerrada sobre:

```text
matrix-aut83-brand-cand-005-phase7.xlsx
SHA-256: 1dae4557ecd0de4182d47fb3bae0d11d0feeb3aef901e5b4e2abdfdfb7d04fdb
Result: PASS
```

Shortlist activa:

```text
BASE-HOGAR-024 — CORE / FIRST-STAGE FIT
BASE-HOGAR-025 — CONDITIONED / CORE / LOGISTICS CHECK
BASE-HOGAR-028 — CONDITIONED / TECH-SERVICE-ECONOMICS CHECK
```

## 2. Reglas

```text
ORIGIN CONFIRMED ≠ SUPPLIER SELECTED
PUBLIC LISTING ≠ COMMERCIAL QUOTE
PUBLIC PRICE ≠ NEGOTIATED FOB
DECLARED CERTIFICATION ≠ DOCUMENT VERIFIED
SIMILAR ARCHITECTURE ≠ EXACT-MATCH SKU
PASS F8 ≠ PRODUCT READY
```

F8 busca disponibilidad y comparabilidad pública de origen, no due diligence de proveedor ni dataset procurement-grade.

## 3. BASE-HOGAR-024 — Compostera modular apilable 40–60 L

### COT-0054 — Welsource 5-tray

Proveedor: Yangjiang Welsource Plastic Products Factory.  
Plataforma: Made-in-China.

Evidencia pública:

```text
5 trays
liquid-collecting base
spigot
coir starter
manual
USD 24,29
MOQ 50
```

Limitación:

> Es un sistema claramente vermicompost-oriented y no cierra por sí solo el target genérico 40–60 L aeróbico/vermicompost-compatible.

### COT-0055 — Shanghai Worth 4-tray

Proveedor: Shanghai Worth International Co., Ltd.  
Plataforma: Alibaba.

Evidencia pública:

```text
4-tray household worm farm
USD 18,80–19,99
MOQ 2
```

Resultado F8:

```text
ORIGIN CONFIRMED
— COMPOSITE PUBLIC EVIDENCE
— FIRST-STAGE FIT
```

La oferta pública confirma disponibilidad de sistemas apilables domésticos, pero F10 deberá cerrar:

- capacidad real;
- dimensiones;
- peso;
- nesting/packing;
- material;
- estabilidad;
- drenaje;
- branding/MOQ.

Fuentes:
- https://www.made-in-china.com/showroom/wsgardenwares/product-detailUAlrSpKvbXRW/China-5-Tray-Square-Plastic-Worm-Composter-Worm-Compost-Bin-Set-Worm-Composting.html
- https://www.alibaba.com/pla/Worm-Farm-4-Tray-Composter-Worm-Compost_1601731610016.html?biz=pla&mark=google_shopping&pcy=es_en&product_id=1601731610016&searchText=waste+bins

## 4. BASE-HOGAR-025 — Compostera giratoria 120 L doble cámara

### COT-0056 — Vertak TG4204011

Proveedor: Ningbo Vertak Mechanical & Electronic Co., Ltd.  
Plataforma: Alibaba.

Evidencia pública:

```text
120 L / 32 gallon
dual chamber
modified PP
BPA-free
anti-UV / anti-frost
64 × 61,3 × 75,5 cm producto
62 × 56 × 20 cm paquete
11 kg gross
USD 28,80 en 439–910 u
USD 25,80 desde 1117 u
logo/packaging custom desde 1000 u
```

Esta es la evidencia pública más cercana a un exact-match del PB.

### COT-0057 — Shanghai Worth 120 L

Proveedor: Shanghai Worth International Co., Ltd.  
Plataforma: Alibaba.

Evidencia pública:

```text
120 L
rotating barrel
dual door
USD 26,90–32,36
MOQ 1092
```

Resultado F8:

```text
ORIGIN CONFIRMED
— STRONG EXACT COMPARATOR
— LOGISTICS CHECK
```

La disponibilidad de origen no es el problema. El gate dominante pasa a ser:

```text
packing
+ peso volumétrico
+ MOQ
+ calidad de estructura/eje/cierres
+ costo puesto
```

Fuentes:
- https://www.alibaba.com/product-detail/Winslow-Ross-120L-capacity-organic-compost_1600977589621.html
- https://www.alibaba.com/countrysearch/CN/food-waste-composting.html

## 5. BASE-HOGAR-028 — Food recycler térmico 3–4 L

### COT-0058 — CLEESINK MLT-450

Proveedor: Hangzhou Cleesink Mechanical & Electrical Co., Ltd.  
Plataforma: Made-in-China.

Evidencia pública:

```text
4,5 L
220 V
50/60 Hz
650 W
drying / microbial / self-cleaning modes declarados
carbon bag
35 dB declarado
85–95 % reducción declarada
USD ~139–140
package 39 × 33,8 × 33,8 cm
gross weight 7,3 kg
CE / FCC / CB / RoHS / KC declarados
```

La publicación presenta una inconsistencia de MOQ:

```text
catálogo del proveedor → MOQ 10
tabla del producto     → MOQ 100
```

Para el screening se adopta `MOQ 100` de forma conservadora.

### COT-0059 — Oushine SHL-23A

Proveedor: Foshan Oushine Technology Co., Ltd.  
Plataforma: Made-in-China.

Evidencia pública:

```text
3,8 / 4,8 L
220 V
550 W
dry / grind / cool
SS304 + ceramic coating
auto-clean
CB / CE / ETL / GS declarados
```

El costo/packing exactos no quedaron capturados en esta evidencia.

Resultado F8:

```text
ORIGIN CONFIRMED
— CONDITIONED
— TECH / SERVICE / ECONOMICS CHECK
```

La disponibilidad técnica es clara. Los gates relevantes son:

- 220–240 V / 50 Hz exactos;
- peso y volumen;
- consumo;
- ruido real;
- motor/cuchillas;
- filtros y reposición;
- limpieza;
- garantía;
- certificaciones;
- repuestos;
- claims sobre output.

Fuentes:
- https://cleesink.en.made-in-china.com/product/SgVUzrWxJJkC/China-4-5L-220V-Kitchen-Food-Waste-Garbage-Recycler-for-Family-Usage.html
- https://es.made-in-china.com/co_oushine-tech/product_Home-Appliance-Food-Composter-Smart-Kitchen-Composter-Kitchen-Food-Garbage-Disposal-Electric-Waste-Food-Recycling-Machine-Composting_yueguionsg.html

## 6. Resultado consolidado

```text
BASE-HOGAR-024
ORIGIN CONFIRMED
— COMPOSITE PUBLIC EVIDENCE / FIRST-STAGE FIT

BASE-HOGAR-025
ORIGIN CONFIRMED
— STRONG EXACT COMPARATOR / LOGISTICS CHECK

BASE-HOGAR-028
ORIGIN CONFIRMED
— CONDITIONED / TECH-SERVICE-ECONOMICS CHECK
```

Los tres PB permanecen activos para F9.

La calidad de evidencia no es igual:

```text
024 → origen claro, exact-match incompleto
025 → exact-match público fuerte + packing
028 → exact-match técnico/logístico fuerte, pero alta complejidad
```

## 7. Gate F8

Resultado conceptual:

```text
PASS
```

Razón:

- los tres Product Bases tienen disponibilidad pública de origen;
- 024 dispone de dos comparables modulares suficientes para demostrar fabricabilidad y rango de costo;
- 025 tiene un exact-match 120 L dual chamber con costo y packing públicos;
- 028 tiene al menos un comparable 220 V con costo, peso y dimensiones públicos, más un segundo comparable técnico;
- no hace falta contactar proveedores para decidir si existe origen comparable.

## 8. Materialización

Se agregan:

```text
COT-0054 … COT-0059
SRC-0465 … SRC-0471
EVID-0277
EVSRC-0603 … EVSRC-0609
```

Archivo preparado:

```text
matrix-aut84-brand-cand-005-phase8.xlsx
SHA-256: 6968ac9aca61e2ef9be85bafaffa6a81c417ab1fe310c7baecb69c57431b3bf0
```

## 9. Estado formal

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut84
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
SHA-256: 6968ac9aca61e2ef9be85bafaffa6a81c417ab1fe310c7baecb69c57431b3bf0
Report: aut84-brand-cand-005-phase8-validation-report.json
```

F9 queda formalmente abierta después de este cierre.

## 10. Próxima acción

Validar `aut84`.

Resultado ejecutado:

```text
F8 CLOSED — aut84 PASS
→ F9 — Import Cost Headroom
→ AUTO
```

F9 conservará la disciplina:

```text
HEADROOM ≠ LANDED COST ≠ MARGIN
```

y utilizará el baseline histórico del proyecto sólo para comparabilidad transversal, no como FX actual.
