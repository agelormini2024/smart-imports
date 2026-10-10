---
id: si-bim-proc-003
title: Method v2 Execution Contract
description: Contrato operativo único para ejecutar, validar, cerrar y reconciliar fases de Method v2 de forma repetible y ágil.
version: 1.0.2
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-08
updated: 2026-10-10
tags:
  - method-v2
  - procedure
  - data-fidelity
  - matrix-validator
  - governance
related:
  - si-bim-001
  - si-func-001
  - si-decision-018
phase: business-intelligence
---

# SI-BIM-PROC-003 — Method v2 Execution Contract

## 1. Objetivo

Eliminar variaciones ad hoc en la ejecución de Method v2.

Este documento es el contrato operativo único. Si una práctica anterior contradice este contrato, prevalece este contrato desde su aprobación.

Objetivo práctico:

> **Que Alejandro no tenga que auditar fila por fila para saber si el método fue aplicado de la misma manera.**

## 2. Pipeline obligatorio

```text
1. LOAD VALIDATED PRIOR SNAPSHOT + PHASE CONTRACT
2. CAPTURE / UPDATE PHASE INPUTS
3. NORMALIZE / CLASSIFY
4. INTERPRET
5. SCORE / DECIDE WHEN THE PHASE REQUIRES IT
6. MATERIALIZE MATRIX
7. DATA FIDELITY PREFLIGHT
8. MATRIX VALIDATOR
9. CLOSE GATE
10. DOCUMENTARY CHECKPOINT
```

El orden no se altera.

El `Data Fidelity Preflight` trabaja sobre la matriz ya materializada; por eso nunca se ejecuta antes de la normalización/clasificación ni antes de materializar el XLSX.

## 3. Separación de capas

### Capa A — Raw Evidence
Hechos observables, sin interpretación.

Ejemplos:
- `+1000`;
- `4.8`;
- `433535`;
- `MOQ 50`;
- `17 kg`;
- URL exacta.

### Capa B — Normalization / Classification
Transformaciones controladas:
- `DIRECT`;
- `DIRECT_CONDITIONED`;
- `ADJACENT`;
- `SUBSTITUTE`;
- Product Base desde F6;
- source binding;
- unidades normalizadas.

### Capa C — Interpretation
Qué significa la evidencia:
- demanda concentrada;
- risk gate;
- compatibilidad parcial con job;
- commodity pressure.

### Capa D — Decision
- score;
- confianza;
- PASS / DEFER / STOP;
- finalist;
- reopen condition.

> **Un campo de Capa A nunca puede contener texto de Capa C o D.**

## 4. Contrato por fase

| Fase | Input mínimo | Output | Regla crítica |
|---|---|---|---|
| F0 | Brand Candidate aprobado | Research Brief | no Product Bases |
| F1 | Brief | Solution Map | arquitectura ≠ Product Base |
| F2 | arquitecturas | Maturity | no demanda/competencia/origen |
| F3 | cohort marketplace | Demanda + confianza | COLLABORATIVE; raw evidence literal |
| F4 | misma cohort F3 | Competencia | no recolectar/reinventar demanda |
| F5 | F3/F4 | Brand Potential | no sourcing |
| F6 | F1–F5 | Product Bases | primera fase que crea PB |
| F7 | PBs | shortlist pre-origin | no sourcing exhaustivo |
| F8 | shortlist | Origin Screening | claims source-bound |
| F9 | precio local + origen | Headroom | headroom ≠ landed cost |
| F10 | costo/MOQ/packing/peso | Minimum Landed Dataset | decision-grade ≠ procurement-grade |
| F11 | dataset F10 + supuestos | Landed Cost Screen | no decisión final |
| F12 | F11 | Margin + ROI | interpreta, no recalcula |
| F13 | F3–F12 | Final Shortlist | integra; F14 no se abre implícitamente |

## 5. Regla F6

```text
F0–F5 → Product Base PROHIBIDA
F6     → primera normalización formal de Product Bases
F7+    → PB puede propagarse downstream
```

La frontera se valida en `Publicaciones ML` y en `Productos Base`; no alcanza con controlar sólo referencias downstream.

## 6. Contrato de evidencia cruda de marketplace

`Publicaciones ML.Ventas visibles` admite únicamente:
- un contador visible literal, por ejemplo `+1000`, `+500`, `+5 mil`;
- `No informadas` cuando el contador no existe o no puede vincularse inequívocamente a la URL fuente.

No admite:
- `Demanda visible observada`;
- `Demanda confirmada`;
- `Alta demanda`;
- badges como sustituto del contador;
- reconstrucciones por semejanza entre publicaciones.

Una reverificación posterior no reescribe silenciosamente una captura histórica. Si existe nueva evidencia, se registra con su fecha y trazabilidad correspondiente.

## 7. Source binding

Todo dato material de origen/economía debe poder responder:

```text
¿QUÉ afirmación?
¿DE QUÉ URL/archivo exacto?
¿DE QUÉ modelo/SKU?
¿EN QUÉ fecha?
¿CON QUÉ nivel de confianza?
```

Si precio/MOQ y especificaciones provienen de páginas distintas del mismo modelo, deben declararse ambas fuentes.

Nunca asumir:

```text
same family = same SKU
same title = same listing
search snippet = exact source page
public price = formal quote
```

## 8. Decision-grade vs procurement-grade

### Decision-grade
Suficiente para decidir si vale la pena continuar.

Puede usar:
- información pública;
- proxies explícitos;
- comparables;
- supuestos conservadores documentados.

### Procurement-grade
Suficiente para comprometer compra/capital.

Requiere confirmar, cuando corresponda:
- precio vigente;
- MOQ/tier;
- Incoterm;
- packing;
- gross weight;
- voltaje/frecuencia;
- certificaciones/documentos;
- lead time;
- warranty;
- QA;
- repuestos/postventa.

> **DECISION-GRADE ≠ PROCUREMENT-GRADE**

## 9. Doble validación obligatoria

Un checkpoint sólo puede cerrarse con:

```text
DATA FIDELITY PREFLIGHT: PASS
AND
MATRIX VALIDATOR: PASS
```

### Data Fidelity Preflight
Valida invariantes semánticas automatizables que el schema no puede inferir.

Cobertura vigente:
- existencia de publicaciones del candidato desde F3;
- `Ventas visibles` como dato crudo cuantificado o `No informadas`;
- URL y `Fuente Global ID`;
- clasificación `DIRECT | DIRECT_CONDITIONED | ADJACENT | SUBSTITUTE`;
- prohibición de Product Bases antes de F6 en `Publicaciones ML`;
- prohibición de registros del candidato en `Productos Base` antes de F6.

> **DATA FIDELITY PREFLIGHT PASS ≠ FACTUAL TRUTH OF EXTERNAL SOURCES.**

### Matrix Validator
Valida estructura, IDs, tipos, referencias y reglas declarativas.

Un PASS no sustituye al otro.

## 10. Auditoría factual obligatoria del asistente

Hasta que más invariantes puedan automatizarse, antes de cerrar una fase el asistente debe revisar:
- source binding de inputs decisivos;
- fecha de captura/reverificación;
- precio/MOQ/tier;
- modelo/SKU;
- packing/peso;
- proxies y supuestos que puedan alterar la decisión.

Esta responsabilidad no se delega al Founder.

## 11. Un solo comando

```bash
bash scripts/validate-method-v2-checkpoint.sh <matrix.xlsx> "<MATRIX_SCOPE_ALIAS>" <phase>
```

El wrapper ejecuta:

```text
Data Fidelity Preflight
→ si FAIL: STOP
→ Matrix Validator
→ si PASS: checkpoint elegible para cierre
```

## 12. Post-close corrections

### Tipo A — Data fidelity / traceability correction
No cambia score ni decisión.

```text
autN CLOSED
→ autN+1 POST-CLOSE RECONCILIATION
→ dual PASS
→ nueva baseline vigente
→ fases permanecen CLOSED
```

### Tipo B — Decision-impacting correction
Puede cambiar score/gate/resultado.

```text
identificar fase más temprana afectada
→ REOPEN
→ rematerializar esa fase
→ propagar downstream
→ validar cada gate nuevamente
```

Nunca editar silenciosamente una baseline congelada.

## 13. Regla de agilidad

Method v2 aplica `Minimum Sufficient Evidence`.

No se exige:
- catálogo exhaustivo;
- capturar cada listing;
- completar datos que no son decisivos;
- profundizar procurement antes de justificarlo.

Sí se exige:
- fidelidad de los datos que sí se usan;
- boundary explícito;
- source binding;
- trazabilidad de cualquier proxy;
- detener investigación cuando evidencia adicional no cambiaría score/confianza/decisión.

## 14. One-candidate-at-a-time

Por defecto:

```text
1 Brand Candidate abierto
→ ejecutar hasta stop/freeze/checkpoint
→ documentar
→ recién después abrir el siguiente
```

## 15. Acceptance criteria de cada gate

Un gate está `CLOSED` sólo si:

1. contrato de fase cumplido;
2. no existen datos de otra capa en campos raw;
3. `Data Fidelity Preflight = PASS`;
4. `Matrix Validator = PASS`;
5. research refleja el estado real;
6. siguiente gate queda explícito;
7. no se abre F14 por inferencia.

## 16. Responsabilidad del asistente

Antes de pedir revisión al Founder, el asistente debe:
- ejecutar/revisar el preflight;
- revisar source binding de inputs decisivos;
- verificar que no haya contradicciones entre research y matrix;
- no reconstruir datos dudosos;
- distinguir hecho / inferencia / proxy;
- preservar fechas históricas de captura;
- declarar cualquier limitación que pueda alterar una decisión.

El Founder no debe actuar como validador manual de consistencia.

## 17. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.2 | 2026-10-10 | Corrige orden ejecutable del pipeline, amplía boundary F6 y formaliza trazabilidad temporal. |
| 1.0.1 | 2026-10-10 | Aprobado tras aut119 corrected dual PASS; documenta cobertura real y límites del preflight. |
| 1.0.0 | 2026-10-08 | Contrato único creado tras auditoría post-cierre de BRAND-CAND-010. |
