---
id: si-bim-proc-003
title: Method v2 Execution Contract
description: Contrato operativo único para ejecutar, validar, cerrar y reconciliar fases de Method v2 de forma repetible y ágil.
version: 1.0.7
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-08
updated: 2026-10-20
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
  - si-decision-019
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
| F8 | shortlist | Origin Screening | COLLABORATIVE; Founder Review required; claims source-bound |
| F9 | precio local + origen | Headroom | headroom ≠ landed cost |
| F10 | costo/MOQ/packing/peso | Minimum Landed Dataset | decision-grade ≠ procurement-grade |
| F11 | dataset F10 + supuestos | Landed Cost Screen | no decisión final |
| F12 | F11 | Margin + ROI | interpreta, no recalcula |
| F13 | F3–F12 | Final Shortlist | integra; F14 no se abre implícitamente |

<!-- METHOD-V2-F8-COLLABORATIVE:START -->
### 4.1 F8 — Origin Screening / Alibaba — COLLABORATIVE

F8 es un gate deliberadamente colaborativo.

```text
F8 — Origin Screening / Alibaba
mode: COLLABORATIVE
Founder participation: REQUIRED
```

La búsqueda de origen no debe tratarse como una recolección autónoma cerrada. Alibaba puede revelar variantes, OEM, arquitecturas, packaging, MOQ y alternativas que requieren lectura comercial conjunta.

#### Participación del Founder

El Founder participa en:

- discovery exploratorio en Alibaba;
- aporte y revisión de listings/productos/proveedores;
- revisión de variantes y arquitecturas;
- evaluación del shortlist de origen;
- aprobación explícita del cierre.

#### Automatización permitida

Dentro de F8 pueden permanecer `AUTO`:

- preparación de keywords;
- ampliación y triage de búsquedas;
- normalización;
- deduplicación;
- detección de equivalencias/OEM;
- extracción de atributos públicos;
- comparación contra Product Bases;
- materialización de evidencias/matriz;
- validación automática.

```text
PHASE MODE = COLLABORATIVE
≠
EVERY TASK = MANUAL
```

#### Close gate

```text
FOUNDER REVIEW: APPROVED
+
ORIGIN EVIDENCE: SOURCE-BOUND
+
ORIGIN SHORTLIST: MATERIALIZED
+
CANONICAL VALIDATION: PASS
=
F8 ELIGIBLE FOR CLOSED
```

F8 no puede declararse `CLOSED` únicamente por ejecución autónoma del agente.

Se mantienen:

```text
ORIGIN CONFIRMED ≠ SUPPLIER SELECTED
PUBLIC LISTING ≠ FORMAL QUOTE
PUBLIC ALIBABA PRICE ≠ NEGOTIATED FOB
DECISION-GRADE ≠ PROCUREMENT-GRADE
```

Esta regla es prospectiva. Las ejecuciones históricas documentadas como `AUTO` conservan su valor histórico y no se reabren sólo por este cambio de governance.

Toda nueva documentación F8 debe declarar en frontmatter:

```text
phase: F8
mode: COLLABORATIVE
```
<!-- METHOD-V2-F8-COLLABORATIVE:END -->

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

<!-- METHOD-V2-MARKETPLACE-ECONOMICS:START -->
## 13.1 Marketplace Commercial + FX Capture Contract

Desde el governance checkpoint del `2026-10-10`, toda evidencia marketplace utilizada desde F3 debe ser económicamente reconstruible.

### 13.1.1 Campos mínimos de captura

Toda publicación activa debe conservar:

```text
ML ID
Fecha de captura / verificación
Producto / modelo
URL exacta o source binding explícito
Tipo de Publicación
Precio ARS
Ventas visibles | No informadas
FX ARS/USD
FX Fecha
FX Fuente / Basis
Precio USD
Observaciones
```

La conversión canónica es:

```text
Precio USD = ROUND(Precio ARS / FX ARS/USD, 2)
```

`Precio USD` sin `FX`, fecha y fuente/basis no constituye evidencia USD válida.

### 13.1.2 Regla de ventas

```text
SELLER SALES ≠ PRODUCT SALES
BADGE ≠ VISIBLE SALES
```

`Ventas visibles` sólo puede contener:

- contador literal del producto/publicación; o
- `No informadas`.

No se transfiere al producto el volumen total del vendedor, tienda, categoría o listing vecino.

### 13.1.3 Regla de precio

El precio debe pertenecer al mismo producto/modelo y source binding utilizado por la evidencia.

No se permite:

```text
precio de listing A + ventas de listing B
```

Si aparecen precio general y promoción personalizada/cupón, se usa por defecto el precio no personalizado salvo que el estudio modele explícitamente la promoción.

### 13.1.4 Trazabilidad temporal

```text
CURRENT VERIFICATION ≠ HISTORICAL CAPTURE
```

Una reverificación posterior genera una observación fechada separada.

La matriz mantiene una hoja `Verificaciones ML` como ledger temporal **append-only**.

Reglas del ledger:

- `Verificación ID` es único;
- un `ML ID` puede tener múltiples verificaciones a lo largo del tiempo;
- nunca se elimina ni sobreescribe una verificación anterior para registrar una nueva;
- la capa de verificación vigente en `Publicaciones ML` debe coincidir con la verificación más reciente del ledger para ese `ML ID`;
- la verificación más reciente se determina por `Fecha Verificación`; si existen varias el mismo día, al menos una debe coincidir exactamente con la capa vigente y todas deben conservar `Verificación ID` único.

Si la fuente histórica no puede recuperarse:

```text
Estado Evidencia ML = HISTORICAL_ONLY
Binding Verificación ML = SOURCE_UNAVAILABLE
Precio ARS Verificado = No verificable
Precio USD Verificado = No verificable
Ventas visibles Verificadas = No informadas
```

Si se necesita reemplazar esa evidencia, el comparable recibe un nuevo `ML ID`.

### 13.1.5 Nuevas capturas

Para cualquier publicación capturada desde la fecha efectiva de esta regla:

- `Precio ARS` es obligatorio;
- `Precio USD` es obligatorio;
- `Ventas visibles` es obligatorio como dato raw o `No informadas`;
- el ledger `Verificaciones ML` es obligatorio desde F3;
- el FX debe ser numérico y mayor que cero;
- `FX Fecha` es obligatorio;
- `FX Fuente / Basis` es obligatorio.

### 13.1.6 Gate

El Data Fidelity Preflight debe comprobar:

1. completitud del ledger;
2. vocabulario de estado/binding;
3. ventas raw;
4. precio ARS;
5. precio USD;
6. FX;
7. fecha y source/basis FX;
8. aritmética `ARS / FX = USD`;
9. source binding;
10. tratamiento explícito de `HISTORICAL_ONLY`;
11. ausencia de Product Bases antes de F6.

> **Un Matrix Validator PASS sin este preflight no habilita CLOSED.**

### 13.1.7 Responsabilidad del agente

El agente que ejecuta Method v2 no debe pedir al Founder que detecte manualmente estas inconsistencias.

Antes de presentar un checkpoint debe verificar:

```text
RAW FACT
→ SOURCE BINDING
→ PRICE + SALES
→ FX TRACEABILITY
→ USD RECONSTRUCTION
→ CLASSIFICATION
→ INTERPRETATION
→ SCORE / DECISION
```

Si un dato no puede sostenerse, se declara la limitación; no se completa por inferencia.
<!-- METHOD-V2-MARKETPLACE-ECONOMICS:END -->

<!-- METHOD-V2-ACTIVE-CORE-PROJECTION:START -->
### 13.1.8 Active Core Projection + Pre-Projection Snapshot

`Verificaciones ML` es el historial temporal append-only.

Las columnas core de `Publicaciones ML` son la proyección operacional vigente.

Para una fila `ACTIVE`:

```text
Precio ARS = Precio ARS Verificado
Precio USD = Precio USD Verificado
Ventas visibles = Ventas visibles Verificadas
```

Cuando al menos una fila cumple `Fecha Verificación ML > Fecha Relevamiento`, antes de proyectar la reverificación al core debe generarse un snapshot completo del scope en `Snapshot Pre-Proyección ML`: exactamente una fila por cada publicación marketplace del scope, preservando el estado core inmediatamente anterior.

Contrato mínimo del snapshot:

- `Snapshot ID` único;
- fecha del snapshot;
- baseline pre-proyección;
- SHA-256 de esa baseline;
- `ML ID`;
- fecha de relevamiento;
- scope;
- producto;
- Precio ARS/USD core previos;
- Ventas visibles core previas;
- baseline, SHA-256 y fecha de snapshot consistentes para todo el scope;
- identidad (`ML ID`, fecha de relevamiento, producto y subcategoría) consistente con `Publicaciones ML`.

El preflight debe fallar con `DF-CORE-*` ante core vigente vacío/divergente y con `DF-SNP-*` ante snapshot ausente, incompleto, duplicado u huérfano.

```text
ACTIVE CORE = VERIFIED CURRENT LAYER
CURRENT CORE PROJECTION REQUIRES PRE-PROJECTION SNAPSHOT
CURRENT VERIFICATION ≠ HISTORICAL CAPTURE
```
<!-- METHOD-V2-ACTIVE-CORE-PROJECTION:END -->

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

## 16.1 Cadencia documental y Governance Preflight
<!-- METHOD-V2-GOVERNANCE-CADENCE:START -->

La publicación documental se agrupa por bloques para conservar trazabilidad sin exigir un commit por cada fase. **El cierre técnico de cada fase sigue requiriendo Data Fidelity Preflight y Matrix Validator PASS**, aun cuando su documentación se publique después.

| Bloque | Cierre documental | Requisito de revisión |
|---|---|---|
| F0–F3 | Después de F3 | F3 COLLABORATIVE: aprobación expresa del Founder |
| F4–F6 | Después de F6 | AUTO, previa doble validación por fase |
| F7–F8 | Después de F8 | F7 AUTO; F8 COLLABORATIVE: aprobación expresa del Founder |
| F9–F13 | Después de F13 | Sólo si se autoriza continuar después de F8; no se abre F14 por inferencia |

**Preflight preventivo:** antes de comenzar un nuevo bloque se verifican el contrato aprobado, el estado operativo y documental del candidato, los checkpoints previos publicados, la última baseline privada con SHA-256 y doble PASS, los modos de fase y el estado de Git. Si alguna prueba relevante es incongruente o no hay evidencia, el resultado es `BLOCKED`; no se completan datos ni autorizaciones por inferencia.

El comprobador de gobernanza de `scripts/method-v2-governance/` complementa al Data Fidelity Preflight y al Matrix Validator; **no los sustituye**, no valida la veracidad de las fuentes y no equivale a aprobación comercial o aduanera.

Las excepciones de cadencia requieren **aprobación expresa del Founder**, motivo, alcance y evidencia escrita incorporada al expediente. Ningún cambio en un archivo JSON constituye por sí mismo una autorización. Esta cadencia se aplica prospectivamente; los checkpoints históricos se conservan y las regularizaciones se registran sin reabrir fases técnicas ya validadas.

<!-- METHOD-V2-GOVERNANCE-CADENCE:END -->

## 17. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.7 | 2026-10-20 | Formaliza la cadencia documental F0–F3 / F4–F6 / F7–F8 / F9–F13 y el Governance Preflight preventivo fail-closed. |
| 1.0.6 | 2026-10-13 | Formaliza F8 — Origin Screening / Alibaba como COLLABORATIVE y exige Founder Review explícita para cerrar la fase. |
| 1.0.5 | 2026-10-10 | Exige Snapshot Pre-Proyección ML y reglas DF-SNP cuando una reverificación posterior se proyecta al core. |
| 1.0.4 | 2026-10-10 | Agrega Active Core Projection y reglas DF-CORE para impedir core marketplace vacío/stale cuando existe verificación ACTIVE. |
| 1.0.3 | 2026-10-10 | Formaliza Marketplace Commercial + FX Capture Contract: precio ARS/USD, ventas raw, FX trazable, Verificaciones ML y manejo HISTORICAL_ONLY. |
| 1.0.2 | 2026-10-10 | Corrige orden ejecutable del pipeline, amplía boundary F6 y formaliza trazabilidad temporal. |
| 1.0.1 | 2026-10-10 | Aprobado tras aut119 corrected dual PASS; documenta cobertura real y límites del preflight. |
| 1.0.0 | 2026-10-08 | Contrato único creado tras auditoría post-cierre de BRAND-CAND-010. |
