---
id: si-research-119
title: BRAND-CAND-009 — Method v2 Agile — Fase 2 — Maturity
description: Evaluación de madurez de mecanismos y arquitecturas de movilidad, estabilidad y capacidad física; sin inferir oportunidad comercial ni crear Product Bases.
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
phase: F2
mode: AUTO
scope_alias: Nicho ID 40
baseline: matrix-aut155-brand-cand-009-phase1-market-solution-map.xlsx
baseline_sha256: 607a97df651d6c78914e0880c70b40d13509d45e73c17026b45dea02fb762208
matrix_revision: aut156
matrix_output: matrix-aut156-brand-cand-009-phase2-maturity.xlsx
matrix_sha256: ad35b330bdafb64d64ec3eeff13e72df71c95819026eab68038d1ac648119fd1
structural_audit: PASS
validation_status: DOUBLE_PASS_CONFIRMED
publication_status: READY_FOR_F0_F3_DOCUMENTARY_CHECKPOINT
---

# SI-RESEARCH-119 — BRAND-CAND-009 — F2: Maturity

<!-- BRAND-CAND-009-F0-F3-CANONICAL-STATUS:START -->
## Estado canónico al checkpoint documental — 19/10/2026

**F2 CLOSED / AUTO**: `aut156` obtuvo Data Fidelity Preflight v2.4 **PASS** y Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` **PASS** (0 errores, 0 advertencias, 0 limitaciones). SHA-256: `ad35b330bdafb64d64ec3eeff13e72df71c95819026eab68038d1ac648119fd1`. La madurez de los mecanismos **no prueba la seguridad ni la viabilidad comercial de implementos concretos**.

Cualquier `PENDING_DOUBLE_PASS`, `F2 NOT CLOSED` o `F3 NOT OPENED` posterior pertenece **al borrador histórico previo a validar**. Estado vigente: **F0–F3 CLOSED; F4 AUTO / NOT OPENED; F14 NOT OPENED**. La matriz `aut156` permanece intacta.
<!-- BRAND-CAND-009-F0-F3-CANONICAL-STATUS:END -->

## 1. Estado, pregunta y contrato

- `BRAND-CAND-009 / FIT-CAND-005 / Marca Fitness — CORE`.
- `F0 CLOSED / aut154 DOUBLE PASS`: SHA-256 `04c3ee21055858cca8d439c0130c2a8284b56795aa84d9cbbae9d7eb2ea8ef6c`.
- `F1 CLOSED / aut155 DOUBLE PASS`: SHA-256 `607a97df651d6c78914e0880c70b40d13509d45e73c17026b45dea02fb762208`. Validación del 19/10/2026, según log aportado por Founder: Data Fidelity Preflight v2.4 PASS y Matrix Validator 0.1.0 (`full-matrix-v5 0.7.0`) PASS, `errors=0`, `warnings=0`, `limitations=[]`.
- `F2 AUTO`: madurez interpretativa evaluada; **cierre técnico pendiente de doble PASS de aut156**.
- `F3 COLLABORATIVE / NOT OPENED`; `F8 COLLABORATIVE / NOT OPENED`; `F14 NOT OPENED`.

**Contrato canónico:** `SI-BIM-PROC-003 v1.0.6` — F2: *arquitecturas → Maturity; no demanda, competencia u origen*; las Product Bases están prohibidas antes de F6. La regla de `Minimum Sufficient Evidence` impide exigir un catálogo exhaustivo en esta fase.

**Pregunta F2:** ¿Qué tan establecidos y reproducibles son los cinco mecanismos funcionales de F1, qué variabilidad y dependencia del entorno presentan, y dónde el grado de madurez del ejercicio **no** alcanza para demostrar la utilidad, seguridad o diferenciación de un accesorio comercial?

## 2. Método y escala cualitativa

Se evalúan siete ejes: (1) principio funcional documentado; (2) implementaciones genéricas reconocibles; (3) progresión inteligible; (4) dependencia del soporte y superficie; (5) mantenimiento y durabilidad por demostrar; (6) fallos de uso y seguridad; (7) límites de la función frente a otros candidatos.

**Escala declarativa:** `ESTABLECIDO` para el principio de ejercicio conocido y documentado; `CONDICIONADO` cuando la solución física depende de una implementación no probada; `NO DEMOSTRADO` cuando las fuentes no permiten acreditar un componente o valor específico. **Confianza en mecanismo e implementación se declara por separado.** Las calificaciones aquí son inferencias de investigación, **no puntuaciones de demanda, competencia, negocio ni efectividad clínica**.

## 3. Matriz de madurez F2 (hipótesis conceptuales, NO Product Bases)

| Arquitectura F1 | Madurez evaluada | Confianza mecanismo / implementación | Principal condición operativa |
|---|---|---|---|
| **A1 — Movilidad articular guiada** | **ESTABLECIDO (movilidad/estiramiento asistido); IMPLEMENTACIÓN CONDICIONADA** | **MEDIA / BAJA** | Tensión excesiva y deriva a tratamiento médico; definir diferencia respecto de estiramiento pasivo genérico. |
| **A2 — Deslizamiento controlado** | **ESTABLECIDO (deslizamiento como ejercicio); FIT DE 009 CONDICIONADO** | **MEDIA / BAJA** | Deslizamiento involuntario y caídas; verificar que movilidad/control, no fuerza genérica, sea el trabajo central. |
| **A3 — Apoyo estable y transferencias** | **ESTABLECIDO (ejercicios funcionales); ACCESORIO COMERCIAL NO DEMOSTRADO** | **ALTA / BAJA** | GATE SEGURIDAD CRÍTICO: estabilidad, anclaje, carga/vuelco; silla/pared doméstica ≠ pieza importable. |
| **A4 — Equilibrio con desafío graduable** | **ESTABLECIDO (equilibrio con superficie variable); IMPLEMENTACIÓN CONDICIONADA** | **MEDIA / BAJA** | GATE SEGURIDAD CRÍTICO: caída, peso máximo, fricción, deformación/ángulo y usuario elegible; no suponer mejoría de salud atribuible a producto. |
| **A5 — Coordinación de pasos y desplazamientos** | **ESTABLECIDO (patrones de paso); IMPLEMENTO / DIFERENCIACIÓN CONDICIONADOS** | **ALTA / BAJA** | Bordes, tropiezos, técnica y espacio; diferenciar de agilidad deportiva de alto rendimiento o microactividad laboral. |

### Lectura por mecanismo y fuente

**A1 — Movilidad articular guiada.** Progresión gradual y control de asistencia; la correa por sí sola no demuestra una experiencia de marca o un sistema de movilidad activa. **Límite:** Tensión excesiva y deriva a tratamiento médico; definir diferencia respecto de estiramiento pasivo genérico. **Fuente de referencia funcional:** https://www.acefitness.org/resources/pros/expert-articles/5678/strengthen-your-ankles-with-these-4-stability-and-mobility-exercises/

**A2 — Deslizamiento controlado.** Implementos deslizantes documentados; gran diferencia según superficie, fricción y postura, posible predominio del entrenamiento de fuerza. **Límite:** Deslizamiento involuntario y caídas; verificar que movilidad/control, no fuerza genérica, sea el trabajo central. **Fuente de referencia funcional:** https://www.acefitness.org/certifiednewsarticle/2583/what-s-in-a-top-trainer-s-toolkit-six-elite-fitness-pros-share-their-favorite-equipment-and-exercises/

**A3 — Apoyo estable y transferencias.** Transferencias y equilibrio con apoyos estables forman ejercicios repetibles; no se demuestra necesidad de vender estructura dedicada. **Límite:** GATE SEGURIDAD CRÍTICO: estabilidad, anclaje, carga/vuelco; silla/pared doméstica ≠ pieza importable. **Fuente de referencia funcional:** https://www.nhs.uk/live-well/exercise/strength-exercises/

**A4 — Equilibrio con desafío graduable.** Almohadillas/tablas y superficies inestables se mencionan en práctica supervisada; características concretas muy heterogéneas. **Límite:** GATE SEGURIDAD CRÍTICO: caída, peso máximo, fricción, deformación/ángulo y usuario elegible; no suponer mejoría de salud atribuible a producto. **Fuente de referencia funcional:** https://www.rnoh.nhs.uk/patients-and-visitors/patient-information-guides/functional-fitness-exercise-pack

**A5 — Coordinación de pasos y desplazamientos.** Secuencias y desplazamientos conocidos; marcadores y escaleras de coordinación documentados, pero no imprescindibles para la práctica. **Límite:** Bordes, tropiezos, técnica y espacio; diferenciar de agilidad deportiva de alto rendimiento o microactividad laboral. **Fuente de referencia funcional:** https://www.acefitness.org/resources/everyone/exercise-library/170/agility-ladder-lateral-shuffle/

**Fuentes complementarias:** NHS describe equilibrio con progresión prudente y apoyo de pared/silla estable (https://www.nhs.uk/live-well/exercise/balance-exercises/); NHS también describe sentarse/levantarse con silla apropiada como ejercicio de fuerza y función (https://www.nhs.uk/live-well/exercise/strength-exercises/). ACE documenta secuencias de escalera y advierte que son ejercicios avanzados en su ejemplo (https://www.acefitness.org/resources/everyone/exercise-library/170/agility-ladder-lateral-shuffle/). Son referencias para mecanismos, **no avales de una marca, un producto o población usuaria universales**.

**Alcance y limitaciones de las fuentes:** literatura institucional, educativa y programas de ejercicios describen prácticas funcionales y accesorios ilustrativos; no hay ensayos, certificados, comparativas independientes ni pruebas de seguridad de los hipotéticos SKU de 009. Algunas fuentes son de rehabilitación/uso clínico: se citan únicamente para reconocer la existencia de mecanismos, sin importar sus claims terapéuticos al territorio de marca Fitness no clínica. La fecha de consulta de las fuentes web es 19/10/2026.

## 4. Interpretación operativa y fronteras

- **A1:** el estiramiento asistido es conocido; el valor de una guía que invite a control activo frente a una correa genérica sigue sin verificarse. No confundir amplitud asistida con tratamiento de lesión.
- **A2:** sliders son conocidos en ejercicio físico, pero los ejemplos públicos disponibles pueden corresponder principalmente a fuerza/core. Continuar sólo si el mecanismo sirve de forma primaria para movilidad/estabilidad, sin asumirlo por nombre de producto.
- **A3:** los ejercicios de transferencias funcionan aun con silla/pared estable; por tanto, *ejercicio maduro ≠ oportunidad de importar soporte*. No considerar apoyo no certificado ni piezas portátiles improvisadas aptas por inferencia.
- **A4:** mecanismos y accesorios de equilibrio son reconocibles, pero el peligro de caída implica una condición de seguridad crítica por diseño y usuario. No inferir beneficios de prevención de caídas ni claims sanitarios de un accesorio.
- **A5:** el desplazamiento coordinado es conocido; para el core de 009 deben priorizarse control y progresión, no velocidad/agilidad deportiva ni rutinas de escritorio de 010.

Los mecanismos se pueden combinar dentro de una misma experiencia; **cinco arquitecturas no implican cinco mercados ni cinco Product Bases**. No se transfiere ningún dato de demanda, ventas, precios, calidad, origen o márgenes de BRAND-CAND-007/008/010.

## 5. Decisión interpretativa F2

**Propuesta:** `READY FOR F3 — CONDITIONED ON CANONICAL VALIDATION`.

Se conoce suficientemente el repertorio conceptual para contrastar la representación comercial **en F3**, sin declarar ninguna arquitectura ganadora. Los bloqueos de seguridad de **A3/A4**, el fit condicional de **A2** y la posibilidad de que **A3/A5 no necesiten accesorio específico** quedan expresamente abiertos. No se necesitan más referencias para repetir que los ejercicios existen; la incertidumbre decisiva pasa a evidencias de solución observable y demanda argentina, con revisión Founder en F3.

No se establecen demanda, competencia, diferenciación, importe de producto, origen, viabilidad regulatoria, landed, margen, ROI, fabricante, proveedor ni compras. **La madurez mecánica no acredita idoneidad comercial o de seguridad de un SKU.**

## 6. Preparación de F3 — COLLABORATIVE (sin abrirla)

F3 deberá acordar con el Founder una cohorte suficientemente variada de publicaciones reales de Mercado Libre Argentina, asociando **cada publicación al mecanismo primario**. La participación y aprobación explícita del Founder son obligatorias antes de cerrar F3; no trasladar demanda de candidatos anteriores.

Se preservarán URL exacta, fecha de captura, producto/modelo, clasificación (`DIRECT`, `DIRECT_CONDITIONED`, `ADJACENT`, `SUBSTITUTE`), precio ARS/USD, ventas visibles literales o `No informadas`, FX ARS/USD, fecha y fuente del FX, y `Verificaciones ML` append-only. Sin precios inferidos, contadores reconstruidos, resultados de búsqueda que suplanten fuentes originales ni Product Bases antes de F6.

## 7. Materialización F2 y gate técnico

- **Baseline inmutable:** `aut155` doble PASS, SHA-256 `607a97df651d6c78914e0880c70b40d13509d45e73c17026b45dea02fb762208`.
- **Nuevo snapshot:** `matrix-aut156-brand-cand-009-phase2-maturity.xlsx`, SHA-256 `ad35b330bdafb64d64ec3eeff13e72df71c95819026eab68038d1ac648119fd1`.
- **Delta autorizado:** sólo `Nichos!AD41:AF41`, fila `Nicho ID 40`; reporte de madurez y trazabilidad en `SI-RESEARCH-119`. No se modifican otras filas, Product Bases ni evidencias.
- **Auditoría estructural previa:** `PASS`: 29 hojas, 1.942 fórmulas, 331,266 celdas; únicamente `Nichos!AD41:AF41` alteradas; 36/37 partes del XLSX idénticas a la baseline; 0 filas nuevas del scope en `Publicaciones ML`, `Verificaciones ML` o `Productos Base`.
- **Validación canónica:** PENDIENTE. Cerrar F2 sólo después de revisar log donde `Data Fidelity Preflight v2.4 = PASS` **y** `Matrix Validator 0.1.0 / full-matrix-v5 0.7.0 = PASS`.
- **Git / publicación:** no hacer commit ni push ahora. Publicar Research `117–120` más índices/roadmap al completar checkpoint F0–F3 y aprobación expresa del Founder en F3.

`F2 PENDING_DOUBLE_PASS / F3 NOT OPENED / F14 NOT OPENED`.
