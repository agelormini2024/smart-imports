---
id: docs-06-research-readme
title: 06 — Research
description: Índice de investigaciones de nichos, productos, proveedores, competencia, demanda, márgenes y oportunidades.
version: 0.17.2
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-02
updated: 2026-10-10
tags:
  - smart-imports
  - research
  - niches
  - evidence
---

# 06 — Research

<!-- BRAND-FITNESS-RESEARCH-STATUS:START -->
## Marca Fitness — Research vigente

```text
BRAND-CAND-010
→ F0–F13 CLOSED
→ FINAL F13 MATRIX: aut118 PASS
→ F13 SHA-256: 54ffcb5cb2884141398763b796b5eb0162555a164e0d1c0ca172680bd4d5745a
→ POST-CLOSE BASELINE: aut120 PASS
→ POST-CLOSE SHA-256: 5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2
→ NO PORTFOLIO FINALIST
→ FREEZE
→ F14 NOT OPENED

BRAND-CAND-007..009
→ ELIGIBLE — NOT OPENED
```

Research completo: [`brand-fitness/README.md`](./brand-fitness/README.md).

La serie documental de `BRAND-CAND-010` es `SI-RESEARCH-070`, `SI-RESEARCH-072..084`; `SI-RESEARCH-071` pertenece al Portfolio Review de Marca Hogar y no se reutiliza.
<!-- BRAND-FITNESS-RESEARCH-STATUS:END -->

<!-- BRAND-CAND-006-RESEARCH-STATUS:START -->
## BRAND-CAND-006 — estado de investigación

```text
F0–F13 CLOSED
Snapshot final: matrix-aut104-brand-cand-006-phase13.xlsx
Validator: PASS limpio
SHA-256: a5caeebe1954b59ea1bf37e29b22e8961820305b743584eaf5355b0439cd056e
Finalist: BASE-PET-003 — FINALIST — CONDITIONED
Portfolio eligibility: ELIGIBLE FOR PORTFOLIO REVIEW
First-stage fit: NOT FIRST-STAGE FIT
Portfolio status: PORTFOLIO REVIEW READY
Candidate status: FREEZE
F14: NOT OPENED
```

Documentación completa: `SI-RESEARCH-056` a `SI-RESEARCH-069`.

La identidad histórica `BASE-PET-003` se preserva `REUSE AS-IS`; no se creó un nuevo Product Base por el cambio de contexto de marca.
<!-- BRAND-CAND-006-RESEARCH-STATUS:END -->

<!-- BRAND-CANDIDATE-DOC-CLOSE-RULE:START -->
## Regla de cierre documental de Brand Candidate

Un Brand Candidate no queda operativamente terminado sólo porque F13 tenga `PASS`.

Secuencia obligatoria:

```text
F13 PASS
→ publicar research F0–F13 en smart-imports
→ actualizar expediente del Brand Candidate
→ actualizar índices de Research y Marca Hogar
→ actualizar README raíz y SI-ROADMAP-002
→ verificar diff / enlaces / estado
→ commit + push humano
→ recién entonces abrir el siguiente Brand Candidate
```

Esta regla evita que el estado operativo dependa de un chat o de archivos locales no publicados.
<!-- BRAND-CANDIDATE-DOC-CLOSE-RULE:END -->

<!-- BRAND-HOGAR-RESEARCH-STATUS:START -->
## Marca Hogar — Research vigente

```text
METHOD V2 RELEVANT CANDIDATES → CLOSED / FROZEN
PORTFOLIO REVIEW → COMPLETE — INTERNAL
FIRST-STAGE LEAD → BASE-HOGAR-016
BACKUP → BASE-HOGAR-006
SECONDARY → BASE-HOGAR-010 / BASE-HOGAR-002
RESERVE → BASE-HOGAR-028 / BASE-PET-003
BRAND-CAND-002 → DEFERRED / PAUSED
EXTERNAL REVIEW → PENDING
F14 → NOT OPENED
```

Portfolio Review: [`SI-RESEARCH-071`](./brand-hogar/si-research-071-brand-hogar-portfolio-review.md).

La matriz privada conserva los datos estructurados y simulaciones; el repositorio público conserva metodología, evidencia pública consolidada, estados, decisiones y continuidad.

Portfolio Review no crea un nuevo snapshot: `aut104` permanece como cierre de Hogar y `aut105` queda reservado para Marca Fitness.
<!-- BRAND-HOGAR-RESEARCH-STATUS:END -->

<!-- SI-F13-CHECKPOINT:START -->
## BRAND-CAND-001 — Golden Run vigente

`SI-RESEARCH-013` cierra Fase 13 — Shortlist final con `aut44` validada. `BRAND-CAND-001` queda `PORTFOLIO REVIEW READY`; F14 no se abre.
<!-- SI-F13-CHECKPOINT:END -->

<!-- SI-F12-CHECKPOINT:START -->
## BRAND-CAND-001 — Golden Run vigente

`SI-RESEARCH-012` cierra Fase 12 — Margin + ROI con `aut43` validada y deja como próximo gate F13 — Shortlist final.
<!-- SI-F12-CHECKPOINT:END -->

<!-- SI-F11-CHECKPOINT:START -->
## BRAND-CAND-001 — Golden Run vigente

`SI-RESEARCH-011` cierra Fase 11 — Landed Cost con `aut42` validada y deja como próximo gate F12 — Margin + ROI.
<!-- SI-F11-CHECKPOINT:END -->

> La investigación concreta prueba y mejora la metodología.

## 1. Propósito

Esta carpeta contiene investigaciones específicas sobre:

- Nichos y subcategorías.
- Demanda y competencia.
- Productos base.
- Proveedores y cotizaciones.
- Margen y facilidad de importación.
- Hallazgos, riesgos y decisiones.

La matriz operativa conserva los datos estructurados. Los documentos Markdown conservan el alcance, el razonamiento, los hallazgos consolidados y la continuidad del trabajo.

## 2. Investigaciones registradas

| Documento | Propósito | Estado |
|---|---|---|
| [`niche-001-portable-solar-energy/README.md`](./niche-001-portable-solar-energy/README.md) | Punto de entrada de las investigaciones del caso piloto Energía Solar Portátil. | `review` |
| [`niche-001-portable-solar-energy/si-research-003-supplier-negotiation-round-01.md`](./niche-001-portable-solar-energy/si-research-003-supplier-negotiation-round-01.md) | Resume la primera ronda de proveedores, validación y próximas acciones. | `review` |
| [`si-research-001-niche-2-selection.md`](./si-research-001-niche-2-selection.md) | Documenta candidatos, filtros, screening, finalistas y selección del Nicho 2. | `review` |
| [`niche-002-travel-organization/README.md`](./niche-002-travel-organization/README.md) | Punto de entrada operativo del Nicho 2. | `review` |
| [`niche-002-travel-organization/si-research-002-travel-organization-scope.md`](./niche-002-travel-organization/si-research-002-travel-organization-scope.md) | Define alcance, subcategorías, exclusiones y plan inicial de investigación. | `review` |
| [`niche-003-pet-care-wellness-technology/README.md`](./niche-003-pet-care-wellness-technology/README.md) | Punto de entrada del Nicho 3: Mascotas — cuidado, bienestar y tecnología. | `review` |
| [`niche-003-pet-care-wellness-technology/si-research-005-niche-3-phases-0-to-6.md`](./niche-003-pet-care-wellness-technology/si-research-005-niche-3-phases-0-to-6.md) | Consolida Method v2 y Fases 0–6 del Nicho 3. | `review` |
| [`niche-003-pet-care-wellness-technology/si-research-006-niche-3-phases-7-to-11-method-v2-validation.md`](./niche-003-pet-care-wellness-technology/si-research-006-niche-3-phases-7-to-11-method-v2-validation.md) | Cierra Fases 7–11 y valida Method v2 internamente hasta Landed Cost Screen. | `review` |

## 3. Investigaciones activas

### Energía Solar Portátil

Estado: prioridad pausada selectivamente; conservar como piloto histórico.

### Viaje organizado y equipaje funcional

Estado: investigación principal cerrada; candidatos y aprendizajes preservados para comparación transversal y eventual shortlist consolidada.

### Mascotas — cuidado, bienestar y tecnología

Estado: Method v2 ejecutado internamente hasta Fase 11 — `Landed Cost Screen`. `aut36` validada sin hallazgos. Próxima etapa: completar candidatos firmes y preparar validación profesional externa.

## 4. Regla de investigación

Todo documento debe separar:

```text
Evidencia
Interpretación
Score
Confianza
Próxima acción
```

Los scores definitivos deben registrarse en la matriz. Los documentos no deben crear una segunda fuente operativa contradictoria.

## 5. Regla de confidencialidad

El repositorio público conserva:

- Método.
- Hallazgos consolidados.
- Estado.
- Decisiones.
- Próximas acciones.

Los datos comerciales exactos permanecen en sistemas privados:

- Cotizaciones.
- FOB objetivo.
- Simulaciones.
- Documentos originales.
- Datos de contacto.
- Estrategia de negociación.

## 6. Próximos documentos previstos

- Paquete consolidado de 5–6 candidatos para revisión profesional.
- Validación aduanera/regulatoria externa cuando intervenga el despachante.
- Actualización de Landed Cost con valores profesionales.
- Shortlist final y decisión de importación.
- Retrospectiva transversal del método después del gate profesional.

## 7. Changelog

| Version | Date | Change |
|---|---|---|
| 0.17.1 | 2026-10-08 | Se publica el cierre completo de BRAND-CAND-010 F0–F13; aut118 PASS, NO FINALIST, FREEZE y F14 NOT OPENED. |
| 0.17.0 | 2026-10-07 | SI-RESEARCH-071 cierra Portfolio Review interno de Marca Hogar; BASE-HOGAR-016 lead, BASE-HOGAR-006 backup, baseline congelada y revisión externa pendiente. |
| 0.16.0 | 2026-10-05 | BRAND-CAND-006 completa F0–F13; SI-RESEARCH-062..069 documentan la reconciliación aut97–aut104 PASS; BASE-PET-003 queda finalista condicionado y el candidato PORTFOLIO REVIEW READY / FREEZE. |
| 0.15.0 | 2026-10-05 | BRAND-CAND-006 cierra F5 sobre aut96 PASS; EVAL-0028 formaliza Potencial de Marca 4/5 Media; siguiente gate F6. |
| 0.14.0 | 2026-10-05 | Se abre Method v2 para BRAND-CAND-010 con SI-RESEARCH-070 F0; análisis completo, materialización/Validator pendientes y aut105 reservado después del lineage aut96..aut104. |
| 0.13.0 | 2026-10-03 | Se incorpora BRAND-CAND-006 SI-RESEARCH-056 a SI-RESEARCH-061; F0–F4 CLOSED sobre aut91–aut95 PASS; F5 análisis completo con materialización pendiente. |
| 0.12.0 | 2026-09-30 | Se incorpora BRAND-CAND-005 completo mediante SI-RESEARCH-042 a SI-RESEARCH-055; aut90 PASS; candidato PORTFOLIO REVIEW READY / FREEZE; siguiente ejecución BRAND-CAND-006 después del cierre documental. |
| 0.11.0 | 2026-09-25 | Se incorpora BRAND-CAND-004 completo mediante SI-RESEARCH-028 a SI-RESEARCH-041 y se formaliza el cierre documental obligatorio antes de abrir el siguiente candidato. |
| 0.10.0 | 2026-09-25 | Se incorpora el índice de Marca Hogar y el cierre completo de BRAND-CAND-003 mediante SI-RESEARCH-014 a SI-RESEARCH-027. |
| 0.9.0 | 2026-09-23 | Se incorpora SI-RESEARCH-010 con cierre de Fase 10 de BRAND-CAND-001. |
| 0.8.0 | 2026-09-21 | Se incorpora SI-RESEARCH-009 con cierre de Fase 9 de BRAND-CAND-001. |
| 0.7.0 | 2026-09-21 | Se incorpora SI-RESEARCH-008 con cierre de Fases 7–8 de BRAND-CAND-001. |
| 0.6.0 | 2026-09-18 | Se incorpora Research de Marca Hogar y SI-RESEARCH-007 como primera Golden Run Brand System → Method v2. |
| 0.1.0 | 2026-07-02 | Placeholder inicial. |
| 0.2.0 | 2026-07-17 | Se activó la sección con la selección y el alcance del Nicho 2. |
| 0.3.0 | 2026-07-20 | Se creó el punto de entrada del Nicho 1 y se documentó la primera ronda de proveedores. |

| 0.4.0 | 2026-09-11 | Se incorporó el Nicho 3, Method v2 y su consolidación hasta Fase 6. |
| 0.5.0 | 2026-09-15 | Se incorporó SI-RESEARCH-006 y se cerró la validación interna de Method v2 hasta Landed Cost Screen. |


## Research originado desde Brand System

| Brand | Documento | Estado |
|---|---|---|
| Marca Hogar | [SI-RESEARCH-007 — BRAND-CAND-001 Golden Run Fases 0–6](./brand-hogar/si-research-007-brand-cand-001-method-v2-golden-run-phases-0-to-6.md) | `aut37` PASS / Fase 6 cerrada / listo para Fase 7 |

> Estos research parten de un Brand Candidate aprobado. No deben modelarse conceptualmente como nuevos nichos aunque la matriz legacy requiera un `MATRIX_SCOPE_ALIAS`.

## Golden Run BRAND-CAND-001 — continuación

| Brand | Documento | Estado |
|---|---|---|
| Marca Hogar | [SI-RESEARCH-008 — BRAND-CAND-001 Golden Run Fases 7–8](./brand-hogar/si-research-008-brand-cand-001-method-v2-golden-run-phases-7-to-8.md) | `aut39` PASS / Fase 8 cerrada / próximo gate Fase 9 — Headroom |

## Golden Run BRAND-CAND-001 — Fase 9

| Brand | Documento | Estado |
|---|---|---|
| Marca Hogar | [SI-RESEARCH-009 — BRAND-CAND-001 Fase 9 Headroom](./brand-hogar/si-research-009-brand-cand-001-method-v2-golden-run-phase-9-headroom.md) | `aut40` PASS / Fase 9 cerrada / siguiente gate Fase 10 — Minimum Landed Cost Dataset |

## Golden Run BRAND-CAND-001 — Fase 10

| Brand | Documento | Estado |
|---|---|---|
| Marca Hogar | [SI-RESEARCH-010 — BRAND-CAND-001 Fase 10 Minimum Landed Cost Dataset](./brand-hogar/si-research-010-brand-cand-001-method-v2-golden-run-phase-10-minimum-landed-cost-dataset.md) | `aut41` PASS / Fase 10 cerrada / siguiente gate Fase 11 — Landed Cost |
| Marca Hogar | [SI-RESEARCH-011 — BRAND-CAND-001 Fase 11 Landed Cost](./brand-hogar/si-research-011-brand-cand-001-method-v2-golden-run-phase-11-landed-cost.md) | `aut42` PASS / Fase 11 cerrada / siguiente gate Fase 12 — Margin + ROI |
| Marca Hogar | [SI-RESEARCH-012 — BRAND-CAND-001 Fase 12 Margin + ROI](./brand-hogar/si-research-012-brand-cand-001-method-v2-golden-run-phase-12-margin-roi.md) | `aut43` PASS / Fase 12 cerrada / siguiente gate Fase 13 — Shortlist final |
| Marca Hogar | [SI-RESEARCH-013 — BRAND-CAND-001 Fase 13 Shortlist final](./brand-hogar/si-research-013-brand-cand-001-method-v2-golden-run-phase-13-final-shortlist.md) | `aut44` PASS / Fase 13 cerrada / Portfolio Review Ready / F14 no abierto |

<!-- BRAND-CAND-010-RECONCILIATION:START -->
### SI-RESEARCH-085 — BRAND-CAND-010 Post-close Evidence Reconciliation

Cerrada sobre `matrix-aut120-brand-cand-010-post-close-reconciliation.xlsx` / `5d52146d5011a72ed52d24df069346d2c063a5e8e918cb92bcc5aa110f4b10e2` con dual PASS.

`aut118` conserva su identidad y SHA como cierre histórico F13. `aut119 corrected` queda superseded antes de publicación. `aut120` es la baseline post-close vigente. No cambia score ni resultado; F14 permanece NOT OPENED.
<!-- BRAND-CAND-010-RECONCILIATION:END -->
