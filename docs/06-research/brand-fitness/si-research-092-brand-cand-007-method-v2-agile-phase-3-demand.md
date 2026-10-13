---
id: si-research-092
title: BRAND-CAND-007 — Method v2 — F3 Demand + Confidence
version: 1.0.0
status: closed
phase: F3
mode: COLLABORATIVE
candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
scope_alias: Nicho ID 38
founder_review: APPROVED
updated: 2026-10-13
related:
  - si-bim-proc-003
  - si-decision-019
  - si-research-089
  - si-research-090
  - si-research-091
---

# SI-RESEARCH-092 — BRAND-CAND-007 — F3: Demanda y confianza

## 1. Resultado colaborativo y cierre

```text
BRAND-CAND-007 / FIT-CAND-001
Problema: Fuerza accesible y compacta
Scope: Nicho ID 38 — Marca Fitness — fuerza accesible y compacta
Mode: COLLABORATIVE
Founder Review: APPROVED (2026-10-13)
Demanda: 3/5
Confianza Demanda: Media
Evaluación: EVAL-0032
Prior snapshot: aut127 corrected / CANONICAL PASS
Final F3 decision snapshot: aut128 / CANONICAL PASS
F3: CLOSED
Next: F4 — Competencia (AUTO), MISMA COHORTE F3
Product Bases: 0 (prohibidas hasta F6)
```

La evaluación se decidió colaborativamente con Alejandro el **2026-10-13**. El cierre exige el doble PASS canónico de la matriz `aut128`; este archivo se publica mediante un script que **bloquea la actualización documental si ese PASS no está comprobado**.

## 2. Evidencia cruda — cohorte equilibrada

Alejandro obtuvo directamente de Mercado Libre Argentina seis PDF de páginas de producto/catálogo y confirmó fecha de captura **2026-10-13**. Las URLs y archivos exactos se conservan en las hojas `Publicaciones ML`, `Fuentes`, `Evidencias`, `Evidencia Fuentes` y `Verificaciones ML` de la matriz privada.

| Arquitectura | ML ID | Referencia exacta | Precio ARS en captura | Ventas visibles literales | Evidencia |
|---|---|---|---:|---|---|
| Resistencia elástica progresiva | ML-0178 | Gadnic, kit de cinco niveles con anclajes | 39.999,00 | `+1000` | EVID-0300 |
| Resistencia elástica progresiva | ML-0179 | Alpina, kit X5 bandas elásticas | 30.185,28 | `+5 mil` | EVID-0301 |
| Carga externa ajustable | ML-0180 | GMP, set mancuerna/barra 20 kg | 93.018,00 | `+500` | EVID-0302 |
| Carga externa ajustable | ML-0181 | BS Fit, kit ajustable 20 kg | 64.999,00 | `+10 mil` | EVID-0303 |
| Peso corporal / suspensión | ML-0182 | MrGym, banda de suspensión | 18.919,12 | `+500` | EVID-0304 |
| Peso corporal / suspensión | ML-0183 | FIT MARK, suspensión con anclaje de acero | 55.797,14 | `+5 mil` | EVID-0305 |

**Reglas de interpretación de los datos crudos:** contadores visibles acumulados de producto/catálogo **no** equivalen a ventas por período, volumen total del mercado ni ventas de un vendedor específico. En URLs de catálogo, el número de publicación mostrado en PDF y el identificador del catálogo se conservan como entidades distintas. Las ventas generales de tienda no se transfieren al producto.

### Capa económica y de verificación

- FX declarado para las capturas: **ARS 1.535/USD**, dólar billete vendedor de Banco Nación, 2026-10-13; la fuente y base de conversión se conservan en la matriz.
- Conversión canónica: `Precio USD = ROUND(Precio ARS / 1535, 2)`.
- Primera captura y primera verificación son del mismo día: no hay reverificación posterior ni actualización retroactiva del core.
- Ledger append-only: `MLV-0027..MLV-0032`, una primera verificación por cada ML ID.
- Fuentes: `SRC-0525..SRC-0530`; evidencias: `EVID-0300..EVID-0305`; bindings: `EVSRC-0716..EVSRC-0721`.
- Capa `Publicaciones ML` para las seis observaciones `ACTIVE` concordante con el ledger más reciente.

## 3. Clasificación, interpretación y límites

- **A1 — Resistencia elástica:** señal positiva directa en Gadnic y Alpina; Alpina también tiene usos anunciados de movilidad/asistencia, por lo que no todas las ventas prueban de manera exclusiva la misión de fuerza.
- **A2 — Carga ajustable:** dos señales positivas, con el contador más alto de la cohorte para BS Fit. La progresión de carga es funcionalmente consistente con el problema; el contador no demuestra preferencia por una marca nueva.
- **A3 — Suspensión:** hay señal positiva en MrGym y FIT MARK, condicionada a seguridad de anclajes, costuras, empuñaduras y montaje. Las capacidades de carga son claims de vendedores, no ensayos independientes. El resumen IA de opiniones de MrGym apunta a preocupaciones de calidad, sin permitir cuantificar incidencias.

Las tres arquitecturas cuentan con evidencia comercial observable. La cohorte de **seis referencias no es una muestra representativa ni longitudinal**; no se infiere ventas mensuales, tamaño de mercado, tendencia, saturación competitiva, margen u oportunidad de importación. `OFFER AVAILABILITY ≠ DEMAND EVIDENCE` y `ADJACENT SALES ≠ JOB-SPECIFIC DEMAND`.

## 4. Decisión F3 — Capa D

**Demanda 3/5 / Confianza Media** — aprobado por el Founder el 2026-10-13.

La calificación `3/5` refleja señales comerciales visibles positivas en las tres arquitecturas, suficientes para continuar con F4, pero no para afirmar demanda alta o generalizar al mercado completo. La confianza `Media` reconoce el respaldo documental directo (6 PDF, URL/modelo, captura fechada, precio ARS/USD, FX trazable, ledger), limitado por el tamaño de cohorte, los contadores acumulados de catálogo/producto y la falta de serie temporal y representatividad.

Evaluación estructurada: `EVAL-0032` (`Nicho ID 38`, criterio `Demanda`, valor `3`, confianza `Media`, estado `Revisado`, evaluador `Alejandro + ChatGPT`), vinculada a `EVID-0300..EVID-0305`.

Esta evaluación **no** fija todavía competencia ni potencial de marca, no autoriza sourcing, no define Product Bases y no implica recomendación de importación.

## 5. Trazabilidad de matrices y gates

| Gate | Matriz | SHA-256 | Resultado |
|---|---|---|---|
| F0 | `aut124` | `4899f4fc595ebe1e07a4b245e5cf1cf300183f6bcd04c3937916f104a13bf108` | Dual PASS |
| F1 | `aut125` | `b3b51eec44716a9d55e17a7d8adf7347bf06adc6a894afd5fb9afec417029aac` | Dual PASS |
| F2 | `aut126` | `f55bdc6b4eb08c377e50dba79952f23955fcb7e1e7bb40c640313905ae32c0f1` | Dual PASS |
| F3, pre-review | `aut127` corrected | `190423828f50bf6204224c2a8a1794aa737ff32b1dec84de2faf67c465bde0de` | Dual PASS; sin score |
| F3, Founder approved | `aut128` | `3fd9bce9fe32866ea30f33e26e3b3eaf9753a36e3223faf200618f8c8c4aba30` | Dual PASS **requerido para publicación** |

La matriz `aut128` modifica únicamente la decisión de F3: `Nichos!D39:E39`, su trazabilidad y la nueva fila de `Evaluaciones!A33:K33`. La evidencia estructurada de F3 queda sin cambios. Las dos fórmulas vacías de plantilla de esa nueva evaluación (`A33`, `D33`) se sustituyen por los valores literales `EVAL-0032` y la denominación exacta del candidato; las demás fórmulas están preservadas.

## 6. Handoff operativo

Tras el doble PASS de `aut128` y el checkpoint documental:

```text
F0–F3 CLOSED
→ F4 Competencia, AUTO, misma cohort F3
→ F5 Potencial de Marca, AUTO
→ F6 Product Bases, AUTO (primera fase permitida)
→ checkpoint documental F4–F6
→ F7 AUTO
→ F8 COLLABORATIVE / Founder Review REQUIRED
```

No abrir candidatos paralelos, no modificar retroactivamente los contadores capturados, no volver a recolectar la demanda de F3 al evaluar competencia en F4, no hacer sourcing en F4–F6 y no hacer commit/push en nombre del Founder.
