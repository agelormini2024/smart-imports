---
id: si-research-094
title: BRAND-CAND-007 — Method v2 — F5 Potencial de Marca
version: 0.1.1
status: closed
phase: F5
mode: AUTO
brand: brand-fitness
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
scope_alias: Nicho ID 38
baseline: aut129
matrix: aut130
created: 2026-10-13
updated: 2026-10-14
related:
  - si-bim-proc-003
  - si-research-092
  - si-research-093
---

# SI-RESEARCH-094 — BRAND-CAND-007 — F5 Potencial de Marca

## 1. Pregunta

¿Puede existir una plataforma de marca defendible para **construir y conservar fuerza útil** bajo restricciones de espacio y equipamiento, más allá de imprimir un nombre propio en productos de gimnasio genéricos?

La misión y el problema proceden de `BRAND-CAND-007 / FIT-CAND-001` y de F0–F2. F5 utiliza la demanda aprobada F3 (`3/5`, confianza Media; `EVAL-0032`) y la evaluación de competencia F4 (`3/5`, confianza Media; `EVAL-0033`). No reabre las ventas capturadas, no vuelve a buscar proveedores ni define Product Bases: eso comienza en F6.

## 2. Evidencia previa — límite factual

Se reutiliza la misma cohorte de **seis PDF de Mercado Libre**, capturados por el Founder el 13/10/2026, con `ML-0178..ML-0183`, `SRC-0525..SRC-0530` y `EVID-0300..0311` (F3+F4):

- Bandas: Gadnic, Alpina. Dos mecanismos de uso y accesorios diferentes; precio, marca y reputación observados no prueban efectividad de una nueva marca.
- Carga externa: GMP, BS Fit. Ofertas establecidas de kits de 20 kg, con precios diferentes y materiales no idénticos.
- Suspensión: MrGym, FIT MARK. Distintas propuestas comerciales; anclajes, costuras, capacidad y seguridad son **claims de publicación**, no resultados de ensayo independiente. En MrGym existe una advertencia cualitativa derivada del resumen automático de opiniones, **no** una tasa verificable de fallas.

Los documentos de F3/F4 contienen URLs y trazabilidad a PDF/ID. `OFFER AVAILABILITY ≠ DEMAND EVIDENCE`; `BRAND PLATFORM ≠ PRIVATE LABEL`.

## 3. Hipótesis de plataforma (interpretación, no hecho probado)

La propuesta no es «vender equipamiento fitness». Es **reducir las barreras prácticas para progresar en fuerza**, con sistemas que sean utilizables, estables y fáciles de guardar.

Palancas hipotéticas:

1. Progresión explícita y comprensible: selección de resistencia/carga, ejercicios y evolución sin depender de equipamiento numeroso.
2. Seguridad como propiedad verificable: ensayo de materiales, anclajes, cierres, costuras, uso y límites de carga; manuales y advertencias claros.
3. Durabilidad y soporte: trazabilidad de lote, piezas sustituibles cuando proceda, garantía y atención de posventa.
4. Arquitectura de cartera por misión/problema, no por categoría de marketplace.

No se demostró todavía que el consumidor valore económicamente estas diferencias, ni que podamos suministrarlas con calidad y costos compatibles con el negocio. Las palancas son **hipótesis para las siguientes fases**.

## 4. Evaluación F5 (capa D)

```text
Potencial de Marca: 3/5
Confianza: Baja
Evaluación: EVAL-0034
Estado: CLOSED / AUTO — Data Fidelity Preflight + Matrix Validator PASS
```

**Justificación:** existe una narrativa de misión coherente y riesgos cotidianos concretos que podrían justificar diferenciarse por progresión, seguridad y servicio. Pero buena parte del hardware es replicable; una marca blanca con marketing genérico no constituye ventaja. La cohorte de seis referencias no verifica disposición a pagar más, menor siniestralidad, menor devolución, calidad de fábrica ni economía de garantía. **Confianza Baja** es deliberada: este resultado es una hipótesis estratégica, no un atributo comercial validado.

Se utiliza evidencia `EVID-0306..EVID-0311` ya vinculada a las seis fuentes capturadas; **no se crean nuevas evidencias artificiales ni se reescriben capturas**. La evaluación queda en `Evaluaciones!A35:K35`, y el score/Confianza de Marca en `Nichos!L39:M39`.

## 5. Materialización, doble PASS y cierre de F5

```text
F4: aut129 — doble PASS / CLOSED
F5: matrix-aut130-brand-cand-007-phase5-brand-potential-pre-gate.xlsx
SHA-256: 8ba9d75fa09c0bf03a78372d4b9255190af27825f2272f77458f326cfbbdd106
Evaluación: EVAL-0034 = Potencial de Marca 3/5 / Confianza Baja
Data Fidelity Preflight v2.4: PASS (6 publicaciones, 6 verificaciones, 0 Product Bases)
Matrix Validator full-matrix-v5 0.7.0: PASS (0 errores / 0 warnings / 0 info)
F5: CLOSED — AUTO
Next: F6, ejecutada AUTO; checkpoint documental conjunto después de F6.
```

La evaluación es una hipótesis estratégica con confianza Baja y no debe confundirse con disposición a pagar comprobada. El doble PASS fue confirmado en el log consolidado de validación F4–F6.
