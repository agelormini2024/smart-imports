---
id: si-roadmap-002
title: Project Status and Handoff
description: Estado operativo, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports.
version: 1.0.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-09-11
tags:
  - status
  - handoff
  - roadmap
  - continuity
related:
  - si-roadmap-001
  - si-agent-001
  - si-func-001
  - si-tech-001
  - si-tech-002
  - si-decision-010
  - si-decision-011
  - si-research-005
  - si-decision-014
audience:
  - founder
  - partner
  - developer
  - assistant
phase: research
---

# SI-ROADMAP-002 — Estado actual y handoff de Smart Imports

> Punto de entrada operativo obligatorio para retomar el proyecto sin depender de un chat específico.

## 1. Fuentes de verdad

```text
Documentación y negocio:
https://github.com/agelormini2024/smart-imports

Software ejecutable:
https://github.com/agelormini2024/smart-imports-engine

Snapshot comercial vigente:
matrix-aut34-niche3-phase6-corrected.xlsx
→ full-matrix-v5 0.7.0
→ PASS limpio

Baseline técnica de release:
matrix-aut32-id-formats-corrected.xlsx
→ Matrix Validator v0.1.0
```

No confundir:

- `aut32`: baseline técnica de la release del Validator.
- `aut34`: snapshot comercial operativo vigente.

## 2. Snapshot al 2026-09-11

| Campo | Estado |
|---|---|
| Fase general | Research / validación del método sobre múltiples nichos |
| Matrix Validator | v0.1.0 publicado y cerrado |
| Schema operativo | `full-matrix-v5 0.7.0` |
| Tests | 40 archivos / 170 tests |
| CLI | 5 casos operativos |
| E2E público | 10 fixtures |
| CI | Verde |
| Matriz comercial vigente | `aut34` |
| Resultado aut34 | PASS / 0 errors / 0 warnings / 0 info / 0 limitations |
| Nicho 1 — Energía Solar Portátil | Pausado selectivamente |
| Nicho 2 — Viaje organizado | Screening de origen/headroom realizado; Landed Cost defendible pendiente |
| Nicho 3 — Mascotas | Fases 0–6 cerradas; 8 PB materializados |
| Próxima acción | Fase 7 — shortlist pre-origen del Nicho 3 |

## 3. Matrix Validator — estado cerrado

```text
Application: 0.1.0
Tag: v0.1.0
Schema: full-matrix-v5 0.7.0
Runtime: Node.js 24
Package manager: pnpm 11
Comportamiento: read-only
```

Estado consolidado:

- 40 archivos de test.
- 170 tests.
- 5 casos CLI.
- 10 fixtures E2E públicos.
- `aut32` PASS limpio.
- CI remoto verde.
- release publicada.

No reabrir el Validator sin un requerimiento comercial concreto.

## 4. Matriz operativa vigente — aut34

```text
matrix-aut34-niche3-phase6-corrected.xlsx
SHA-256:
ad791f8d5fe5c0bb0b18994d4c12d45b187499216f3dbd90cd42e4a9b08f9bf5
```

Validación:

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
```

`aut34` conserva lo anterior e incorpora la materialización de Fase 6 del Nicho 3:

- Nicho 29 normalizado.
- 3 Evaluaciones nuevas.
- 8 Productos Base `BASE-PET-*`.
- publicaciones y competencia local normalizadas.
- benchmarks externos.
- evidencias y fuentes trazables.
- cuatro resúmenes de competencia por arquitectura.
- segmentos competitivos, incluidos sustitutos.

No incorpora todavía Landed Cost ni una selección final de proveedores.

## 5. Método vigente — Method v2

Jerarquía:

```text
NICHO
→ NECESIDAD / FAMILIA
→ ARQUITECTURA DE SOLUCIÓN
→ PRODUCTO BASE
```

Reglas consolidadas:

- `publicación ≠ competidor ≠ SKU ≠ Producto Base`;
- normalizar antes de evaluar;
- Demanda y Competencia se evalúan por separado;
- complejidad técnica es riesgo, no descarte automático;
- un sustituto puede ser una combinación de productos;
- `OEM platform ≠ exact supplier`;
- safety claim no equivale a seguridad validada;
- network generation no equivale a network compatibility;
- standby battery no equivale a tracking battery;
- private-label capability no equivale a Potencial de Marca.

## 6. Nicho 3 — estado por arquitectura

| Arquitectura | Estado | Potencial de Marca |
|---|---|---|
| Vacuum Grooming | ADVANCE | MEDIO–ALTO |
| Arenero automático/smart | ADVANCE | ALTO — CONDICIONADO |
| Smart Fountain | ADVANCE | MEDIO–ALTO |
| GPS + Wellness | ADVANCE — CONDITIONAL | ALTO — FUERTEMENTE CONDICIONADO |

Watchlist:

- Dedicated Pet Camera + interaction.
- Mobile Pet Robot.

## 7. Productos Base del Nicho 3

| ID | Producto Base |
|---|---|
| BASE-PET-001 | Vacuum Grooming doméstico integrado |
| BASE-PET-002 | Arenero automático rotativo cerrado |
| BASE-PET-003 | Arenero automático open-top / acceso amplio |
| BASE-PET-004 | Arenero automático de rastrillo |
| BASE-PET-005 | Fuente inteligente automatizada/conectada |
| BASE-PET-006 | Fuente con monitoreo cuantitativo de hidratación |
| BASE-PET-007 | Tracker GPS 4G para mascotas |
| BASE-PET-008 | Tracker GPS + Wellness avanzado |

## 8. Necesidades futuras descubiertas para Matrix vNext

No bloquean el ciclo actual.

1. `Familia` y `Arquitectura` explícitas.
2. `Tipo Competencia = DIRECTA | INDIRECTA | SUSTITUTO | BENCHMARK`.
3. `Nichos.Proxima Accion` alineada con las fases de Method v2.

Mantener `full-matrix-v5 0.7.0` estable mientras estas necesidades no justifiquen un nuevo schema.

## 9. Estado comercial por nicho

### Nicho 1 — Energía Solar Portátil

- AT-999 y compras permanecen pausadas.
- Conservar evidencia histórica.
- No forzar reactivación sin una nueva razón comercial.

### Nicho 2 — Viaje organizado y equipaje funcional

- Demanda y Competencia cerradas.
- Screening de proveedores/origen realizado.
- Headroom screening realizado.
- Landed Cost defendible sigue pendiente.
- No crear snapshots MARG basados en supuestos no defendibles.

### Nicho 3 — Mascotas

- Research Brief: cerrado.
- Madurez: cerrada.
- Demanda: cerrada.
- Competencia: cerrada.
- Potencial de Marca: cerrado.
- Productos Base: cerrados.
- Materialización: `aut34` PASS.
- Próxima fase: shortlist pre-origen.

## 10. Próxima secuencia del Nicho 3

```text
Fase 7 — shortlist pre-origen
→ Fase 8 — origin screening + comparability
→ Fase 9 — Headroom
→ Fase 10 — Minimum Landed Cost Dataset
→ Fase 11 — Landed Cost
→ Fase 12 — Margin + ROI
→ Fase 13 — final shortlist
→ Fase 14 — validación real
```

## 11. Bloqueos y dependencias

| Tema | Estado | Acción |
|---|---|---|
| Matrix Validator | Cerrado | No reabrir sin requerimiento comercial |
| Matrix vNext | No bloqueante | Registrar requisitos y diferir |
| Niche 3 shortlist | Pendiente | Ejecutar Fase 7 |
| Niche 3 origin | No iniciado formalmente | Esperar Fase 8 |
| Landed Cost Niche 3 | No iniciado | No adelantar |
| Wellness local | Hipótesis abierta | Mantener como condición |
| Seguridad areneros | Riesgo crítico posterior | Evaluar en sourcing/QA |
| Compatibilidad GPS | Riesgo crítico posterior | Exigir variante/bandas documentadas |

## 12. Protocolo para abrir un nuevo chat

1. Compartir ambos repositorios.
2. Pedir lectura inicial de `SI-ROADMAP-002`.
3. Para tareas del Nicho 3, consultar `SI-RESEARCH-005`.
4. Adjuntar `aut34` sólo cuando la tarea requiera datos privados de la matriz.
5. No volver a adjuntar PDFs históricos ya consolidados.
6. Mantener separadas tareas de negocio (`smart-imports`) y técnicas (`smart-imports-engine`).
7. No reabrir decisiones técnicas cerradas salvo que el flujo comercial descubra un bloqueo real.

## 13. Próxima acción concreta

```text
Nicho 3
→ Fase 7 — shortlist pre-origen
→ reducir los 8 PB antes de profundizar sourcing
```

No iniciar Landed Cost ni RFQ exhaustivo antes de cerrar esa shortlist.

## 14. Documentos relacionados

- [SI-RESEARCH-005 — Niche 3 Phases 0–6](../06-research/niche-003-pet-care-wellness-technology/si-research-005-niche-3-phases-0-to-6.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-DECISION-014 — Adopt Niche 3 Method v2 and aut34](../09-decision-log/si-decision-014-adopt-niche3-method-v2-and-aut34.md)

## 15. Changelog

| Version | Date | Change |
|---|---|---|
| 0.7.0 | 2026-08-03 | Handoff de v3/v4 y normalización de fuentes. |
| 0.8.0 | 2026-08-04 | Adopción de aut31/v5, 144 tests y cierre técnico de vistas derivadas. |
| 1.0.0 | 2026-09-11 | Matrix Validator cerrado; `aut34` adoptada; Method v2 y Fases 0–6 del Nicho 3 consolidadas. |
