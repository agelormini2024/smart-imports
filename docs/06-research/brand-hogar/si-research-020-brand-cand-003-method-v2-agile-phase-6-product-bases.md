---
id: si-research-020
title: BRAND-CAND-003 — Method v2 Agile — F6 Product Bases
description: Consolidación conceptual y materialización de Product Bases para tratamiento doméstico del aire interior.
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
  - phase-6
related:
  - brand-cand-003
  - si-research-014
  - si-research-015
  - si-research-016
  - si-research-017
  - si-research-018
  - si-research-019
phase: business-intelligence
---

# BRAND-CAND-003 — Method v2 Agile — F6 Product Bases

Fecha: 2026-09-24  
Estado: `CLOSED`

## 1. Objetivo

Transformar las arquitecturas comerciales observadas en F0–F5 en `PRODUCT BASES (PRODUCTOS BASE)` suficientemente concretos para comparación de mercado, búsqueda de origen y evaluación económica, sin confundir:

```text
PUBLICATION
≠ PRODUCT BASE

BRAND / SELLER
≠ PRODUCT BASE

FEATURE
≠ PRODUCT BASE

PRODUCT BASE EXISTS
≠ CANDIDATE ELIGIBILITY
```

La frontera de Product Base sigue la regla aprendida en la Golden Run: se separa cuando cambia materialmente el job, mecanismo, arquitectura de instalación, seguridad, service layer, economía/logística, regulación o postventa.

## 2. Input consolidado

F6 recibe:

```text
BRAND-CAND-003
Tratamiento doméstico del aire interior

F0 Research Brief              CLOSED
F1 Solution Map                CLOSED
F2 Maturity                    CLOSED
F3 Demand                      CLOSED
F4 Competition                 CLOSED
F5 Brand Potential             CLOSED
```

El candidato mantiene una regla central:

> `Component specification ≠ System performance.`

Por lo tanto, una etiqueta `HEPA`, `carbón`, `UV`, `ionizador` o `Smart` no crea por sí sola un Product Base distinto.

## 3. Regla de consolidación aplicada

Se consolidan arquitecturas cuando las diferencias observadas son features o variantes que no cambian materialmente la propuesta comercial.

Ejemplos de atributos que **no** crean automáticamente otro PB:

- sensor PM2.5;
- Wi-Fi / app;
- modo automático;
- cantidad de velocidades;
- color o diseño;
- cobertura declarada diferente;
- carbón auxiliar en un purificador cuyo mecanismo dominante sigue siendo filtración de partículas;
- marca o vendedor distinto.

Se separan PB cuando existe diferencia material en:

- objetivo primario: partículas vs partículas + gases/olores;
- mecanismo dominante: filtración física vs tratamiento activo;
- generación intencional de ozono;
- presencia de tratamiento activo complementario con impacto en seguridad/claims;
- ausencia de filtros y dependencia de UVGI/fotocatálisis;
- instalación portátil vs `in-duct` HVAC;
- mantenimiento: filtros/sorbentes vs lámpara UV;
- carga de seguridad, certificación y soporte.

## 4. Resultado conceptual

F6 normaliza siete Product Bases para `BRAND-CAND-003`.

### BASE-HOGAR-009 — Purificador portátil HEPA H13 — partículas

```text
Status: CANDIDATE_PB
Architecture: D1
Primary mechanism: filtración mecánica forzada
Primary job: reducir partículas suspendidas
```

Equipo portátil con ventilador + prefiltro + HEPA/H13 como mecanismo dominante.

Puede incorporar carbón auxiliar, sensor, app o ionizador secundario sin cambiar automáticamente de PB.

Evidencia comercial principal:

```text
ML-0103 — Levoit Core Mini
ML-0105 — Lumenac AP-26
ML-0106 — AIUZLK P260
ML-0109 — Prasky MB-032
```

Frontera crítica:

> `HEPA component ≠ system CADR / room performance`.

Oportunidad de marca: CADR/desempeño verificable, 220 V, sizing, ruido, filtros disponibles, garantía y soporte.

### BASE-HOGAR-010 — Purificador portátil HEPA + carbón activado material

```text
Status: CANDIDATE_PB
Architecture: D2
Primary mechanism: filtración de partículas + adsorción material
Primary job: partículas + determinados gases/olores/COV
```

La diferencia con BASE-HOGAR-009 no es “tener carbón”, sino que la etapa sorbente sea suficientemente material y forme parte real de la propuesta de tratamiento.

Evidencia:

```text
ML-0101 — Casiba Brezza 480
ML-0110 — AIRROMI A2002
ML-0111 — HoMedics Natura
ML-0112 — Jafanda JF260
ML-0113 — Sans Mini [evidencia débil / ambiguous]
```

`ML-0112` es particularmente útil como benchmark porque declara `300 g` de carbón y CADR, mientras otros casos sólo mencionan carbón sin cuantificar su materialidad.

Condición estructural:

```text
ACTIVATED CARBON PRESENT
≠
GAS-PHASE CAPABILITY DEMONSTRATED
```

### BASE-HOGAR-011 — Purificador portátil multietapa HEPA + tratamiento activo complementario

```text
Status: CANDIDATE_PB — CONDITIONED
Architecture: filtration + active-secondary
Primary mechanism: filtración mecánica
Secondary mechanism: UV-C y/o ionización
Intentional ozone: excluded from PB
```

Evidencia:

```text
ML-0107 — Lumenac AP-18
ML-0108 — Gadnic PURAIR02
```

Se separa de 009/010 porque la capa activa cambia materialmente seguridad, evidencia, claims y postventa.

La multiplicación de tecnologías no debe interpretarse como mayor desempeño ni mayor Brand Potential.

### BASE-HOGAR-012 — Purificador activo UV-C / fotocatálisis — ozone-free

```text
Status: CANDIDATE_PB — HIGHLY CONDITIONED
Architecture: D3 active treatment
Primary mechanism: UVGI / fotocatálisis
HEPA: no requerido como mecanismo principal
Intentional ozone: no
```

Evidencia principal:

```text
ML-0117 — E-CLEANER OZ2
```

Este PB cambia simultáneamente mecanismo, mantenimiento y carga de evidencia. No requiere filtros reemplazables como un D1/D2, pero depende de seguridad de cámara, fuente UV, reemplazo de lámpara, subproductos y demostración de eficacia aplicable.

Claims microbiológicos no se aceptan por descripción comercial: requieren validación independiente y revisión regulatoria/profesional cuando corresponda.

### BASE-HOGAR-013 — Ionizador standalone sin filtración física

```text
Status: SUPPORT_PB / ACTIVE_ONLY
Architecture: D3
Primary mechanism: ionización
```

Evidencia:

```text
ML-0102 — Gadnic IOAIR001
Visible sales: +500
```

La alta señal transaccional se conserva como dato de mercado, pero no convierte el PB automáticamente en candidato defendible de Marca Hogar.

Razones para mantenerlo como soporte:

- baja diferenciación estructural;
- fuerte presión de precio;
- eficacia sistémica no demostrada por la etiqueta de ionización;
- necesidad de evaluar subproductos y seguridad;
- propuesta menos compatible con la disciplina técnica definida en F5.

No ingresa automáticamente a F7.

### BASE-HOGAR-014 — Generador de ozono / sistema activo con ozono intencional

```text
Status: SUPPORT_PB / NEGATIVE_BENCHMARK
Architecture: D3 / A8
Primary or material secondary mechanism: intentional ozone generation
```

Evidencia:

```text
ML-0100 — Ozonizer Life O3 / ozono + ionización
ML-0104 — Gadnic ozonizador
ML-0114 — ESEA Split germicida / híbrido con ozono
```

La generación intencional de ozono constituye una frontera propia porque cambia materialmente riesgo, condiciones de uso, comunicación y validación de seguridad.

La señal de demanda `+1000` observada en algunos productos se conserva como evidencia comercial, pero:

```text
DEMAND
≠ EFFICACY
≠ SAFETY
≠ BRAND ELIGIBILITY
```

Por diseño de F6, este PB queda fuera de la shortlist automática de F7 salvo reapertura explícita basada en evidencia externa suficiente.

### BASE-HOGAR-015 — Tratamiento UV-C en conducto HVAC / aire acondicionado

```text
Status: CANDIDATE_PB — CONDITIONED
Architecture: D4
Deployment: in-duct / HVAC / central-split
Primary mechanism: UV-C / UVGI
```

Evidencia:

```text
ML-0115 — D200 PCO
ML-0116 — Honeywell AirBRITE
ML-0118 — Affectnianly 2000-1
ML-0119 — IonFactor UV-C
```

La instalación en conductos constituye una diferencia comercial estructural: cambia usuario/instalador, compatibilidad, seguridad, soporte, logística y servicio.

D4 presenta menor saturación visible, pero eso no se interpreta como ventaja automática porque la demanda observada también es débil/especializada.

Oportunidad: 220 V, kit de instalación seguro, documentación de sizing/dosis, repuestos de lámpara y soporte técnico local.

## 5. Product Bases elegibles para F7

F6 no ejecuta la shortlist, pero debe separar existencia de elegibilidad.

### `CANDIDATE_PB`

```text
BASE-HOGAR-009
BASE-HOGAR-010
BASE-HOGAR-011 — CONDITIONED
BASE-HOGAR-012 — HIGHLY CONDITIONED
BASE-HOGAR-015 — CONDITIONED
```

Estos cinco pueden ser considerados por F7.

### `SUPPORT_PB`

```text
BASE-HOGAR-013 — ACTIVE_ONLY / ionización standalone
BASE-HOGAR-014 — NEGATIVE_BENCHMARK / ozono intencional
```

No pasan a F7 por inercia.

## 6. Normalización de publicaciones

Las 20 publicaciones de F3/F4 quedan asignadas a un Product Base real.

Esto corrige una limitación deliberada de las fases anteriores, donde `ID Producto Base` permanecía vacío hasta contar con consolidación conceptual suficiente.

Regla aplicada:

```text
QUERY COHORT
→ REAL MECHANISM
→ NORMALIZED PRODUCT BASE
```

Ejemplo relevante:

```text
ML-0103 Levoit Core Mini
Query / cohort previo: D2 por HEPA + carbón
F6 normalized PB: BASE-HOGAR-009
Reason: la evidencia disponible no demuestra que el carbón sea una etapa gas-phase material;
        la arquitectura comercial defendible observada es HEPA-dominant.
```

Esto no contradice F3: F3 medía demanda y conservaba incertidumbre; F6 resuelve la frontera conceptual necesaria para Product Base.

## 7. Matriz vigente y compatibilidad

La matriz continúa usando el adapter legacy:

```text
Nicho ID: 33
Nicho: Marca Hogar — tratamiento doméstico del aire interior
Type: MATRIX_SCOPE_ALIAS
```

El input de negocio real sigue siendo:

```text
BRAND-CAND-003
```

No se modifica `full-matrix-v5 0.7.0`.

F6 materializa Product Bases mediante las estructuras existentes:

- `Productos Base`;
- `Publicaciones ML.Producto Base`;
- `Publicaciones ML.ID Producto Base`;
- `Competencia ML.Producto Base`;
- `Competencia ML.ID Producto Base`.

## 8. Materialización aut51

Snapshot preparado:

```text
matrix-aut51-brand-cand-003-phase6.xlsx
SHA-256: 0c0e195c05d7ae5da368f46e6e1f43dc095e36c413e54e7baa2563a9b291e3e6
```

Incorporaciones principales:

```text
+ 7 Product Bases normalizados
  BASE-HOGAR-009 ... BASE-HOGAR-015

+ 20 relaciones Publicación ML → Product Base
+ 20 relaciones Competencia ML → Product Base
+ actualización MATRIX_SCOPE_ALIAS para checkpoint F6
```

No se crea una nueva Evaluación ni Evidencia artificial para “Product Bases”, porque F6 no corresponde a un criterio del catálogo `Criterios`.

La normalización queda trazada mediante Product Bases, publicaciones, competencia y este documento.

## 9. Gate

Estado actual:

```text
F6 — CLOSED

Validation checkpoint:
matrix-aut51-brand-cand-003-phase6.xlsx
SHA-256: 0c0e195c05d7ae5da368f46e6e1f43dc095e36c413e54e7baa2563a9b291e3e6
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0

NEXT:
F7 — Shortlist pre-origen
→ AUTO
```

F7 deberá comparar inicialmente sólo:

```text
BASE-HOGAR-009
BASE-HOGAR-010
BASE-HOGAR-011
BASE-HOGAR-012
BASE-HOGAR-015
```

sin permitir que una fortaleza económica futura compense automáticamente un bloqueo técnico o de seguridad.
