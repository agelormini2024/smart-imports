---
id: si-research-021
title: BRAND-CAND-003 — Method v2 Agile — F7 Shortlist pre-origen
description: Shortlist pre-origen de Product Bases para tratamiento doméstico del aire interior.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-24
updated: 2026-09-24
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-003
  - indoor-air
  - phase-7
related:
  - brand-cand-003
  - si-research-020
phase: business-intelligence
---

# BRAND-CAND-003 — Method v2 Agile — F7 Shortlist pre-origen

Fecha: 2026-09-24  
Estado: `CLOSED`

## 1. Objetivo

Responder:

> ¿Qué Product Bases merecen consumir esfuerzo de sourcing y comparabilidad de origen en F8?

F7 no selecciona qué importar ni anticipa economía de origen.

Reglas:

```text
PRODUCT BASE EXISTS
≠ PASS TO ORIGIN

DEMAND
≠ SAFETY

MORE TECHNOLOGY
≠ MORE BRANDABILITY

LOW COMPETITION
≠ OPPORTUNITY

COMPLEXITY = RISK
```

No se usa score agregado. Una señal comercial fuerte no compensa automáticamente una condición técnica, de seguridad o de primera etapa.

## 2. Input

```text
BRAND-CAND-003

F0 Research Brief       CLOSED
F1 Solution Map         CLOSED
F2 Maturity             CLOSED
F3 Demand               CLOSED
F4 Competition          CLOSED
F5 Brand Potential      CLOSED
F6 Product Bases        CLOSED
```

Product Bases evaluados en F7:

```text
BASE-HOGAR-009
BASE-HOGAR-010
BASE-HOGAR-011
BASE-HOGAR-012
BASE-HOGAR-015
```

Support PB trazables pero fuera de shortlist automática:

```text
BASE-HOGAR-013 — ionizador standalone
BASE-HOGAR-014 — ozono intencional / negative benchmark
```

## 3. Criterios cualitativos de F7

Se consideran conjuntamente:

- señal de demanda observada;
- presión competitiva;
- madurez de la arquitectura;
- potencial de marca;
- verificabilidad del beneficio;
- complejidad técnica;
- seguridad y claims;
- instalación;
- postventa y consumibles;
- adecuación al bias de primera etapa.

No se ponderan numéricamente.

## 4. Resultado

### BASE-HOGAR-009 — Purificador portátil HEPA H13 — partículas

```text
F7: PASS TO ORIGIN
Priority inside F8: CORE
```

**Razones**

- arquitectura madura y comparable;
- mecanismo fácil de explicar;
- menor carga de seguridad que tecnologías activas;
- oportunidad de marca en CADR, sizing, ruido, filtros, 220 V, repuestos y soporte;
- logística e instalación relativamente simples;
- permite construir claims técnicos más acotados y verificables.

**Condiciones para F8**

- encontrar configuraciones comparables por CADR/cobertura;
- separar HEPA declarado de desempeño sistémico;
- verificar filtro reemplazable y disponibilidad;
- preferir 220–240 V / 50 Hz;
- obtener dimensiones, peso, ruido y consumo.

---

### BASE-HOGAR-010 — Purificador portátil HEPA + carbón activado material

```text
F7: PASS TO ORIGIN — CONDITIONED
Priority inside F8: CORE
```

**Razones**

- amplía el job hacia determinados olores/gases;
- buena coherencia con Marca Hogar;
- posibilidad de diferenciación más defendible que agregar features digitales;
- sigue apoyándose en una arquitectura de filtración madura.

**Condición dominante**

> La etapa de carbón debe ser material y documentable.

F8 debe evitar normalizar como equivalente cualquier OEM que sólo agregue una lámina testimonial de carbón.

**Datos mínimos buscados**

- masa / espesor / configuración del sorbente;
- reemplazo independiente o integrado;
- CADR de partículas separado de cualquier claim gas-phase;
- claims de VOC/olores respaldados por método de prueba cuando existan;
- 220–240 V / 50 Hz.

---

### BASE-HOGAR-011 — Purificador multietapa HEPA + tratamiento activo complementario

```text
F7: PASS TO ORIGIN — HIGHLY CONDITIONED
Priority inside F8: SECONDARY / COMPARABILITY CHECK
```

No se elimina todavía porque puede existir como variante del mismo ecosistema OEM de 009/010 y F8 puede resolver esa comparabilidad a bajo costo de investigación.

Pero no debe desplazar a 009/010 por sumar UV-C o ionización.

**Condiciones**

- sin generación intencional de ozono;
- tecnología activa claramente identificada;
- preferencia por función opcional/desactivable;
- evidencia de seguridad y subproductos;
- no usar claims microbiológicos como driver comercial sin soporte independiente;
- el costo/complexity premium debe ser visible y justificable.

Si F8 muestra que sólo agrega marketing, riesgo o costo, pasa a `HOLD`.

---

### BASE-HOGAR-012 — Purificador activo UV-C / fotocatálisis — ozone-free

```text
F7: HOLD
Do not source in normal F8 flow
```

**Razones**

- señal local de demanda débil frente a filtración convencional;
- mayor carga de prueba de eficacia;
- claims microbiológicos sensibles;
- dependencia de geometría, dosis, tiempo de exposición y mantenimiento de lámpara;
- riesgo de subproductos en sistemas fotoquímicos;
- peor adecuación a primera etapa.

Puede reabrirse sólo si aparece evidencia externa suficientemente fuerte o una oportunidad de origen claramente diferenciada.

---

### BASE-HOGAR-015 — Tratamiento UV-C en conducto HVAC

```text
F7: HOLD
Do not source in normal F8 flow
```

**Razones**

- demanda visible débil/especializada;
- instalación modifica la experiencia comercial y de postventa;
- requiere compatibilidad con HVAC/split y posiblemente instalador;
- mayor carga técnica y de soporte;
- peor adecuación al bias de primera importación.

No se invalida como oportunidad futura; simplemente no merece sourcing prioritario ahora.

---

## 5. Support Product Bases

### BASE-HOGAR-013 — Ionizador standalone

```text
F7: OUT OF SHORTLIST
Reason: SUPPORT_PB
```

La señal transaccional se conserva, pero el producto presenta baja diferenciación estructural, presión de precio y menor defendibilidad técnica.

### BASE-HOGAR-014 — Ozono intencional

```text
F7: OUT OF SHORTLIST / NEGATIVE BENCHMARK
```

La demanda visible no compensa el cambio material en riesgo, condiciones de uso, claims y seguridad.

No pasa a sourcing normal de F8.

## 6. Shortlist pre-origen

Resultado:

```text
PASS TO ORIGIN
→ BASE-HOGAR-009

PASS TO ORIGIN — CONDITIONED
→ BASE-HOGAR-010

PASS TO ORIGIN — HIGHLY CONDITIONED
→ BASE-HOGAR-011

HOLD
→ BASE-HOGAR-012
→ BASE-HOGAR-015

OUT OF SHORTLIST
→ BASE-HOGAR-013
→ BASE-HOGAR-014
```

La shortlist operativa de F8 queda deliberadamente concentrada en:

```text
009
010
011
```

con 009/010 como núcleo y 011 únicamente como control de comparabilidad/variante.

## 7. Principio decisional

La F7 confirma una señal emergente importante:

```text
MEJOR PRIMERA ARQUITECTURA
≈
MENOR CARGA DE PRUEBA
+ BENEFICIO EXPLICABLE
+ REPUESTOS MANEJABLES
+ INSTALACIÓN SIMPLE
```

No se transforma todavía en regla formal de Method v2; queda como aprendizaje de Golden Run / Agile Run.

## 8. Próximo gate

Disciplina obligatoria:

```text
ANÁLISIS CONCEPTUAL
→ MATERIALIZACIÓN EN MATRIZ
→ MATRIX VALIDATOR
→ CHECKPOINT DOCUMENTAL
→ F7 CLOSED
```

Estado actual:

```text
F7
ANALYSIS COMPLETE
→ SHORTLIST DEFINED
→ MATRIX MATERIALIZATION PENDING
→ MATRIX VALIDATOR PENDING
→ NOT CLOSED
```

La materialización de `aut52` debe registrar la shortlist sin abrir F8 antes del PASS.

## 9. Materialización aut52

Estado actual:

```text
F7
ANALYSIS COMPLETE
→ SHORTLIST DEFINED
→ MATRIX MATERIALIZATION PREPARED
→ MATRIX VALIDATOR PENDING
→ NOT CLOSED
```

Materialización preparada:

```text
matrix-aut52-brand-cand-003-phase7.xlsx
SHA-256: 5a6d6a3023ca32b0fc06f8b38a86a67ce657405321c6f671c7e8dccc0b14140a
```

La matriz registra:

```text
EVID-0252
SRC-0390
EVSRC-0454
```

y actualiza `Productos Base` con los estados F7 de `BASE-HOGAR-009` a `BASE-HOGAR-015`.

No abrir F8 hasta obtener `PASS` limpio del Matrix Validator.


## 10. Cierre formal de F7

```text
MATRIX
matrix-aut52-brand-cand-003-phase7.xlsx

SHA-256
5a6d6a3023ca32b0fc06f8b38a86a67ce657405321c6f671c7e8dccc0b14140a

VALIDATOR
Matrix Validator 0.1.0
full-matrix-v5 0.7.0

RESULT
PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Estado final:

```text
F7 CLOSED
→ F8 — Screening de origen
→ AUTO
```
