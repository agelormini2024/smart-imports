---
id: si-research-117
title: BRAND-CAND-009 — Method v2 Agile — Fase 0 — Research Brief
description: Apertura prospectiva de movilidad, estabilidad y conservación/recuperación de capacidad física para Marca Fitness.
version: 0.2.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-19
updated: 2026-10-19
brand: brand-fitness
brand_candidate: brand-cand-009
source_hypothesis: FIT-CAND-005
method: method-v2-agile
phase: F0
mode: AUTO
baseline_revision: aut153
baseline_sha256: 4c88c0ac2e4d459f17707da38d8f4b72fb7cdaf0d157dc1d3e8b8c4505b10540
matrix_revision: aut154
matrix_output: matrix-aut154-brand-cand-009-phase0-research-brief.xlsx
matrix_sha256: 04c3ee21055858cca8d439c0130c2a8284b56795aa84d9cbbae9d7eb2ea8ef6c
validation_status: DOUBLE_PASS_CONFIRMED
publication_status: READY_FOR_F0_F3_DOCUMENTARY_CHECKPOINT
---

# SI-RESEARCH-117 — BRAND-CAND-009 — F0: Research Brief

<!-- BRAND-CAND-009-F0-F3-CANONICAL-STATUS:START -->
## Estado canónico al checkpoint documental — 19/10/2026

**F0 CLOSED / AUTO**: `aut154` obtuvo el **doble PASS canónico** el 19/10/2026, según `validation-aut154-brand-cand-009-f0.sh` y log aportado por Founder. SHA-256: `04c3ee21055858cca8d439c0130c2a8284b56795aa84d9cbbae9d7eb2ea8ef6c`. Data Fidelity Preflight v2.4 **PASS** y Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` **PASS**, sin errores, advertencias ni limitaciones.

Los renglones posteriores que digan `PENDING_DOUBLE_PASS`, `F0 NOT CLOSED` o `F1 NOT OPENED` describen **el estado histórico del borrador previo a validar**, no el estado operativo vigente. **F0–F3 están CLOSED** tras aprobación explícita del Founder en F3; **F4 AUTO / NOT OPENED; F14 NOT OPENED**. No se modifica la matriz `aut154` ni su SHA al actualizar este Research.
<!-- BRAND-CAND-009-F0-F3-CANONICAL-STATUS:END -->

## 1. Identidad y estado

```text
SCREENING: CLOSED — PASS TO METHOD V2
BRAND CANDIDATE: BRAND-CAND-009
SOURCE HYPOTHESIS: FIT-CAND-005
BRAND: Marca Fitness
PRIMARY MISSION: Conservar y recuperar movilidad, estabilidad y capacidad física
TERRITORY RELATIONSHIP: CORE
SCREENING TYPE: PROSPECTIVE
F0 MODE: AUTO
F0 BRIEF: PREPARED
F0 MATRIX: aut154 MATERIALIZED — LOCAL STRUCTURAL AUDIT PASS
DATA FIDELITY PREFLIGHT v2.4: PENDING
MATRIX VALIDATOR 0.1.0 / full-matrix-v5 0.7.0: PENDING
F0: NOT CLOSED
F1: NOT OPENED
F14: NOT OPENED
```

La apertura comienza después de publicar el cierre documental de `BRAND-CAND-008` en el commit `c411015` de `main`. No se reabre `008`, `007` ni `010`; no se modifica la prioridad comercial de otros territorios.

## 2. Fuentes normativas y trazabilidad de la decisión

- Expediente de screening aprobado: `docs/07-brand/brands/brand-fitness/candidates/brand-cand-009-mobility-stability-physical-capacity.md`, versión `0.1.0`: misión, hipótesis `FIT-CAND-005`, límites de claims y `PASS TO METHOD V2`.
- Contrato vigente: `docs/02-business-intelligence-manual/procedures/si-bim-proc-003-method-v2-execution-contract.md`, versión `1.0.6`: F0 `Research Brief`, F1 `Solution Map`, F3/F8 colaborativas, Product Bases sólo desde F6, doble PASS.
- Fuente de verdad del estado: `docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md` (cierre de `BRAND-CAND-008` publicado).
- Regla operativa adicional: `docs/02-business-intelligence-manual/procedures/si-method-note-001-materializacion-y-validacion-de-matrices.md`: el asistente prepara el XLSX completo y el Founder ejecuta un solo comando de validación.
- Antecedentes metodológicos, **no evidencia transferible de demanda**: `SI-RESEARCH-070` (F0 de `010`) y `SI-RESEARCH-103` (F0 de `008`).

## 3. Problema aprobado y pregunta central

**Problema aprobado por screening**: conservar o recuperar movilidad, estabilidad y capacidad física de modo progresivo y comprensible, en el ámbito fitness no clínico. Puede involucrar rigidez cotidiana, variedad limitada de movimiento, retorno gradual a una práctica física o mantenimiento de capacidad, pero **no** se define como rehabilitación, diagnóstico ni tratamiento.

**Pregunta de investigación de F0**:

> ¿Qué arquitecturas de solución permiten practicar movilidad, estabilidad y control físico de forma comprensible y progresiva en contextos cotidianos, con requisitos de seguridad e instrucciones defendibles, sin depender de promesas clínicas ni confundir accesorios genéricos con una propuesta de marca útil?

La investigación parte del **problema y del mecanismo funcional**, no de un SKU, proveedor, tecnología, precio ni marca preseleccionados.

## 4. Hipótesis iniciales (todavía NO verificadas)

### H1 — Diversidad real de mecanismos

Podrían existir varias arquitecturas físicamente diferentes para ejercitar rango de movimiento, control o estabilidad. En F1 se diferenciarán por mecanismo, experiencia y finalidad principal; colores, tamaños o bundles no justifican arquitecturas distintas.

### H2 — Progresión comprensible

La posibilidad de graduar dificultad y seguir instrucciones puede reducir la fricción de adopción. F1 observará si la progresión es concreta y segura; en F0 no se presume eficacia.

### H3 — Seguridad como condición de entrada

Riesgos de caída, apoyo, agarre, estabilidad, intensidad, materiales y límites de usuario pueden ser determinantes. Los claims de seguridad y resistencia deberán verificarse con evidencia específica más adelante.

### H4 — Función central, no bienestar genérico

Una solución debe servir de forma central para practicar movilidad, estabilidad o capacidad física. Su mera asociación a descanso, automasaje, comodidad, estilo de vida saludable o bienestar comercial no basta para pertenecer a `009`.

### H5 — Experiencia de marca

Rutinas, progresiones, instrucciones, claridad de uso y soporte podrían constituir diferenciación; por ahora son hipótesis y no ventajas competitivas demostradas. Su atractivo se comprobará en F3–F5.

### H6 — Retorno progresivo distinto de rehabilitación clínica

La práctica física gradual no autoriza afirmar tratamiento de lesiones, cura del dolor, reducción de inflamación o recuperación terapéutica. Cualquier claim eventual requerirá soporte apropiado a su naturaleza.

### H7 — Tecnología subordinada al objetivo

Apps, sensores, contadores o sistemas conectados sólo aportan si mejoran una práctica física real. Incorporar electrónica no es un criterio de Brand Fit ni de oportunidad de negocio por sí solo.

## 5. Fronteras con candidatos vecinos

| Candidato | Problema primario | Regla de separación |
|---|---|---|
| `BRAND-CAND-007` — Fuerza accesible y compacta | Construir o conservar fuerza útil | Un accesorio de fuerza no pasa a `009` sólo porque participe en calentamientos o estiramientos. |
| `BRAND-CAND-008` — Entrenamiento flexible y portátil | Mantener entrenamiento intencional entre contextos | Portabilidad y sesiones completas no reemplazan el problema central de movilidad/estabilidad. |
| **`BRAND-CAND-009` — Movilidad y estabilidad** | Practicar capacidad física, movilidad y control de manera progresiva | Guardar la frontera no clínica y exigir función física central. |
| `BRAND-CAND-010` — Movimiento en jornada sedentaria | Microactividad distribuida durante el día | Un objeto cercano al escritorio o que fomente pausas no pertenece automáticamente a `009`. |

`FIT-CAND-003 — Recuperación y movilidad` fue absorbido por `FIT-CAND-005` **antes** del screening formal; no se reabre como candidato separado ni genera evidencia propia transferible.

Si se observan familias funcionales compartidas, **no duplicar Product Bases**: su normalización ocurre recién en F6, después de determinar el problema primario.

## 6. Alcance y contrato para F1 — Market / Solution Map

F1 podrá explorar y diferenciar familias de soluciones según:

1. mecanismo central de movilidad, estabilidad o control;
2. secuencia de uso, ajustes y posibilidad de progresión;
3. condiciones del entorno (suelo, pared, superficies, equilibrio y espacio);
4. claridad de instrucciones y límites de uso;
5. riesgos de estabilidad, carga, apoyos y materiales;
6. conveniencia en el contexto cotidiano, sin asumir portabilidad como requisito universal;
7. potencial de marca, sin atribuir demanda o eficacia todavía.

No se fija una lista de productos a investigar ni un número obligatorio de arquitecturas. Se aplicará **Minimum Sufficient Evidence**. Las arquitecturas conceptuales de F1 **no equivalen a Product Bases**.

**Fuera de alcance**: promesas de rehabilitación, fisioterapia o intervención médica; aparatos o productos cuya función principal sea clínica; wellness genérico no ligado a movimiento físico; masajes cuya única propuesta sea alivio subjetivo; soluciones sin función material de movilidad/control; inferencias sobre salud no documentadas.

## 7. Disciplina de claims y evidencia

```text
PRACTICAR / MEJORAR MOVILIDAD ≠ TRATAR UNA LESIÓN
AUTOMASAJE / RECUPERACIÓN PERCIBIDA ≠ TERAPIA CLÍNICA
EXPERIENCIA DE MARCA POTENCIAL ≠ EFICACIA O DEMANDA COMPROBADA
```

No se transfieren scores, publicaciones, ventas, proveedores, márgenes, tasas de importación ni seguridad de `007`, `008` o `010`. El carácter no clínico constituye una frontera de selección comercial y también obliga a consultar regulaciones aplicables más adelante, cuando existan productos concretos y evaluación externa.

## 8. Exclusiones explícitas de F0

```text
PRODUCT BASES: NO — prohibidas hasta F6
PUBLICACIONES ML / COHORTE DE DEMANDA: NO
COMPETENCIA / POTENCIAL DE MARCA: NO SCORE
FUENTES ALIBABA / COTIZACIONES: NO
PROVEEDORES HOMOLOGADOS / RFQ / MUESTRAS: NO
FOB / EXW / LANDED / MARGEN / ROI: NO
AUTORIZACIÓN DE IMPORTACIÓN / F14: NO
```

F3 y F8 mantienen gates `COLLABORATIVE` y requieren intervención/aprobación del Founder cuando correspondan. La investigación profunda de proveedores, muestras y homologaciones permanece diferida hasta discutir prioridades con el socio y el despachante de aduana.

## 9. Materialización de matriz y lineage

**Baseline global previa, validada**:

```text
Matriz: matrix-aut153-brand-cand-008-phase13-final-shortlist.xlsx
SHA-256: 4c88c0ac2e4d459f17707da38d8f4b72fb7cdaf0d157dc1d3e8b8c4505b10540
Estado: BRAND-CAND-008 F13 CLOSED / DOUBLE PASS / NO FINALIST / FREEZE — REOPENABLE
```

**Nuevo snapshot propuesto**:

```text
Matriz: matrix-aut154-brand-cand-009-phase0-research-brief.xlsx
SHA-256: 04c3ee21055858cca8d439c0130c2a8284b56795aa84d9cbbae9d7eb2ea8ef6c
MATRIX_SCOPE_ALIAS: Marca Fitness — movilidad, estabilidad y conservación/recuperación de capacidad física
Nicho ID: 40
Rango: Nichos!A41:AF41
Nuevo Research: SI-RESEARCH-117
```

El alias `Nichos` es una adaptación legacy de la matriz, **no cambia la identidad del Brand Candidate**.

**Delta exacto auditado:** sólo se incorporaron `Nichos!A41:C41` y `Nichos!AD41:AF41`; los scores quedaron vacíos. Se conservaron 29 hojas, 1.942 fórmulas, todas las celdas no vacías anteriores y los enlaces históricos. El ZIP XLSX conserva 37 miembros sin pérdida de componentes y pasó verificación de integridad.

La auditoría estructural local no sustituye las dos validaciones canónicas. Se utilizará el wrapper oficial sobre el archivo `aut154` íntegro, sin alterar el anterior.

## 10. Gate F0 y continuidad

**Pregunta de aceptación**:

> ¿Quedaron suficientemente delimitados el problema, las hipótesis, las fronteras no clínicas y la investigación de arquitecturas para iniciar F1 sin preseleccionar un producto?

**Resultado conceptual propuesto:** `PASS TO CANONICAL VALIDATION`. Sólo si `Data Fidelity Preflight v2.4 = PASS` **y** `Matrix Validator 0.1.0 / full-matrix-v5 0.7.0 = PASS` podrá declararse F0 `CLOSED`.

```text
F0: MATERIALIZED / LOCAL AUDIT PASS / DOUBLE PASS PENDING
F1: NOT OPENED
F3: COLLABORATIVE, todavía no abierta
F8: COLLABORATIVE, todavía no abierta
F14: NOT OPENED
DOCUMENTARY CHECKPOINT: F0–F3, después de los cierres técnicos correspondientes
```

**Próxima acción única**: ejecutar el script del paquete de `aut154` en Warp y compartir el log. No publicar el Research ni el XLSX en Git en esta fase. Las matrices, scripts, capturas y logs quedan privados; `SI-RESEARCH-117` se incorporará a Git en el checkpoint documental F0–F3.
