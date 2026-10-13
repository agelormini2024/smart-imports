---
id: si-bim-readme
title: Business Intelligence Manual Index
description: Índice principal del Business Intelligence Manual de Smart Imports. Organiza la metodología de investigación, evaluación, evidencias, scoring y priorización de nichos.
version: 0.3.5
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-10-10
tags:
  - business-intelligence
  - research
  - methodology
  - scoring
  - matrix
  - smart-imports
related:
  - si-doc-001
  - si-00
  - si-vision-001
  - si-bim-000
phase: business-intelligence
---

# 02 — Business Intelligence Manual

> **El objetivo no es adivinar oportunidades. El objetivo es construir un método para encontrarlas.**

---

## 1. Propósito de esta carpeta

La carpeta `02-business-intelligence-manual` contiene la metodología de investigación, evaluación y priorización de oportunidades de negocio de **Smart Imports**.

Este manual define cómo Smart Imports debe:

- Investigar nichos.
- Registrar evidencias.
- Evaluar criterios.
- Asignar scores.
- Medir confianza.
- Comparar oportunidades.
- Priorizar investigaciones.
- Decidir qué nichos avanzan a fases posteriores.
- Aprender de cada investigación.

Este manual es el corazón metodológico de Smart Imports.

---

## 2. Rol dentro de Smart Imports

Smart Imports no quiere tomar decisiones de importación basadas solamente en intuición, entusiasmo o precio de compra.

El Business Intelligence Manual existe para transformar la investigación comercial en un proceso:

- Ordenado.
- Repetible.
- Auditable.
- Mejorable.
- Documentado.
- Escalable.
- Automatizable en el futuro.

La futura plataforma Smart Imports deberá implementar esta metodología, no reemplazarla.

---

## 3. Principio rector

El principio rector del BIM es:

> **Primero evidencia. Después score. Después decisión.**

En términos prácticos:

```text
Nicho
  ↓
Investigación
  ↓
Evidencias
  ↓
Interpretación
  ↓
Evaluación por criterio
  ↓
Score + Confianza
  ↓
Priorización
  ↓
Próxima acción
```

---

## 4. Relación con la Matriz de Oportunidades

La Matriz de Oportunidades es la herramienta inicial.

El Business Intelligence Manual es la metodología que explica cómo usarla.

La matriz responde:

> ¿Dónde cargamos la información?

El BIM responde:

> ¿Cómo decidimos qué información cargar, cómo interpretarla y qué significa?

---

## 5. Componentes principales

| Componente | Descripción |
|---|---|
| Nichos | Áreas de oportunidad comercial que se investigan antes que productos específicos. |
| Criterios | Dimensiones utilizadas para evaluar cada nicho. |
| Evidencias | Datos, observaciones y fuentes que respaldan una evaluación. |
| Evaluaciones | Valor asignado a un criterio para un nicho, con justificación y confianza. |
| Score | Resultado numérico que permite comparar nichos. |
| Confianza | Nivel de solidez de la evidencia que respalda cada evaluación. |
| Priorización | Clasificación de nichos según atractivo, evidencia y riesgo. |
| Próxima acción | Paso recomendado luego de una evaluación. |

---

## 6. Estado de criterios

| Criterio | Documento | Estado metodológico | Estado en piloto Energía Solar Portátil |
|---|---|---|---|
| Confianza | `criteria/si-bim-000-confidence-in-evaluations.md` | Definido | Aplicado |
| Demanda | `criteria/si-bim-001-demand-evaluation.md` | Definido / review | Aplicado |
| Competencia | `criteria/si-bim-002-competition-evaluation.md` | Definido / review | Aplicado |
| Margen Potencial | `criteria/si-bim-003-margin-potential-evaluation.md` | Draft / en validación | En evaluación |
| Facilidad de Importación | Pendiente | Pendiente | Pendiente |
| Potencial de Marca | Pendiente | Criterio operativo preliminar | Aplicado preliminarmente |
| Venta Impulsiva | Pendiente | Criterio operativo preliminar | Aplicado preliminarmente |
| Recompra | Pendiente | Criterio operativo preliminar | Aplicado preliminarmente |
| Potencial IA | Pendiente | Criterio operativo preliminar | Aplicado preliminarmente |
| Potencial Automatización | Pendiente | Criterio operativo preliminar | Aplicado preliminarmente |
| Afinidad Personal | Pendiente | Criterio operativo preliminar | Aplicado preliminarmente |

---

## 7. Procedimientos operativos

| Procedimiento | Documento | Estado | Propósito |
|---|---|---|---|
| Procesamiento de evidencias marketplace | `procedures/si-bim-proc-001-marketplace-evidence-processing.md` | Review | Convertir PDFs, publicaciones ML y fuentes externas en datos estructurados, productos base, evidencias y análisis competitivo. |
| RFQ y screening de margen | `procedures/si-bim-proc-002-supplier-rfq-and-margin-screening.md` | Draft | Pedir cotizaciones, calcular FOB objetivo, negociar proveedores y validar Margen Potencial. |

---

## 8. Flujo operativo vigente

```text
Fuentes crudas
  ├── Publicaciones ML
  ├── Fuentes Externas
  └── Cotizaciones Proveedores
        ↓
Productos Base
        ↓
Análisis auxiliar
  ├── Competencia ML
  ├── Competencia Externa
  └── Simulación Margen
        ↓
Evidencias
        ↓
Evaluaciones
        ↓
Nichos / Dashboard
```

---

## 9. Caso piloto vigente

El caso piloto actual es:

```text
Energía Solar Portátil
```

Estado del piloto:

| Criterio | Estado |
|---|---|
| Demanda | Cerrado preliminarmente |
| Competencia | Cerrado preliminarmente |
| Recompra | Cerrado preliminarmente |
| Potencial IA | Cerrado preliminarmente |
| Potencial Automatización | Cerrado preliminarmente |
| Afinidad Personal | Cerrado preliminarmente |
| Potencial de Marca | Cerrado preliminarmente |
| Venta Impulsiva | Cerrado preliminarmente |
| Margen Potencial | En evaluación con RFQ de proveedores |
| Facilidad de Importación | Pendiente de datos técnicos y logísticos |

---

## 10. Documentos relacionados

- [SI-DOC-001 — Documentation Standards](../standards/si-doc-001-documentation-standards.md)
- [SI-00 — Sprint 0: Foundation](../00-vision/si-00-sprint-0-foundation.md)
- [SI-BIM-000 — Confidence in Evaluations](./criteria/si-bim-000-confidence-in-evaluations.md)
- [SI-BIM-001 — Demand Evaluation](./criteria/si-bim-001-demand-evaluation.md)
- [SI-BIM-002 — Competition Evaluation](./criteria/si-bim-002-competition-evaluation.md)
- [SI-BIM-003 — Margin Potential Evaluation](./criteria/si-bim-003-margin-potential-evaluation.md)
- [SI-BIM-PROC-001 — Marketplace Evidence Processing](./procedures/si-bim-proc-001-marketplace-evidence-processing.md)
- [SI-BIM-PROC-002 — Supplier RFQ and Margin Screening](./procedures/si-bim-proc-002-supplier-rfq-and-margin-screening.md)

---

## 11. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-02 | Versión inicial del índice del Business Intelligence Manual. |
| 0.2.0 | 2026-07-10 | Se actualizó el índice luego de aplicar Demanda y Competencia al caso piloto y documentar el procedimiento de evidencias. |
| 0.3.0 | 2026-07-15 | Se agregó Margen Potencial, procedimiento RFQ, estado de criterios estratégicos y estado actualizado del piloto. |

<!-- METHOD-V2-EXECUTION-CONTRACT:START -->
## Method v2 — contrato operativo vigente

- `criteria/si-bim-001-demand-evaluation.md` — criterio histórico preservado y fortalecido aditivamente.
- `procedures/si-bim-proc-003-method-v2-execution-contract.md` — contrato operativo aprobado.
- Gate obligatorio: Data Fidelity Preflight PASS + Matrix Validator PASS.
<!-- METHOD-V2-EXECUTION-CONTRACT:END -->

<!-- METHOD-V2-MARKETPLACE-CONTRACT:START -->
## Method v2 — Marketplace economics contract

`SI-BIM-PROC-003 v1.0.3` y `SI-DECISION-019` hacen obligatoria desde F3 la trazabilidad `Precio ARS → FX → Precio USD`, junto con ventas visibles raw y source binding.

La validación semántica se ejecuta mediante `scripts/validate-method-v2-data-fidelity.py` antes del Matrix Validator.
<!-- METHOD-V2-MARKETPLACE-CONTRACT:END -->

<!-- AUT123-SNAPSHOT-BASELINE:START -->
## aut123 — Core + snapshot baseline vigente

```text
aut121 corrected
→ marketplace economics dual PASS
→ SUPERSEDED: core operativo incompleto/stale
→ 7701f6d626905749431fb5836082d2bfbd612e8b6409e668fb6b1bc95ee77dfc

aut122
→ core marketplace materialization
→ Data Fidelity Preflight v2.3 PASS
→ Matrix Validator PASS
→ SUPERSEDED: estado pre-proyección no preservado estructuralmente
→ 67e850c0a40fb274629429587f9ce5b500eddb51da6580fccb2c48f060dba4ba

aut123
→ 21 ACTIVE core complete / synchronized
→ 5 HISTORICAL_ONLY explícitos
→ 26/26 Snapshot Pre-Proyección ML
→ ML-0160 temporal proof: +500 → +100
→ Core + Snapshot Fidelity PASS
→ Data Fidelity Preflight v2.4 PASS
→ Matrix Validator PASS / 0 errors / 0 warnings / 0 info
→ CURRENT POST-CLOSE BASELINE
→ 23099aae25921caab2a223a101e420d4e217dd04701cfb767054e4e6fa2eadbb

F0–F13: CLOSED
F14: NOT OPENED
```

```text
ACTIVE CORE = VERIFIED CURRENT LAYER
CURRENT CORE PROJECTION REQUIRES PRE-PROJECTION SNAPSHOT
CURRENT VERIFICATION ≠ HISTORICAL CAPTURE
```
<!-- AUT123-SNAPSHOT-BASELINE:END -->

<!-- METHOD-V2-F8-COLLABORATIVE:START -->
## F8 — Origin Screening / Alibaba

A partir de `SI-DECISION-020`, F8 se ejecuta en modalidad `COLLABORATIVE`.

```text
Founder participation: REQUIRED
Founder Review: APPROVED → requerido para CLOSE
```

La fase admite automatización interna de búsqueda asistida, normalización, clasificación, materialización y validación, pero no puede cerrarse únicamente por ejecución autónoma.

La regla es prospectiva y no reabre ejecuciones históricas.
<!-- METHOD-V2-F8-COLLABORATIVE:END -->
