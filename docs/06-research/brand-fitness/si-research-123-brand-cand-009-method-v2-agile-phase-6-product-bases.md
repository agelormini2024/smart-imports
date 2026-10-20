---
id: si-research-123
title: BRAND-CAND-009 — Method v2 Agile — Fase 6 — Product Bases
description: Normalización formal de cuatro formatos funcionalmente distintos de movilidad y equilibrio, sin sourcing ni shortlist de origen.
version: 0.2.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-20
updated: 2026-10-20
brand: brand-fitness
brand_candidate: BRAND-CAND-009
source_hypothesis: FIT-CAND-005
scope_alias: 'Marca Fitness — movilidad, estabilidad y conservación/recuperación de capacidad física'
phase: F6
mode: AUTO
baseline_revision: aut163
baseline_sha256: 0d19fd39ca2dad470258e283286ffd443c8d58f9f03e2cffadd71f7ae5d352bd
matrix_revision: aut164
matrix_output: matrix-aut164-brand-cand-009-phase6-product-bases.xlsx
matrix_sha256: 3e39e5e00b2c6b3706ed0b152d6d5a8d7c684df21d3eb5ea5b0d503426315a8c
structural_audit: PASS
validation_status: DOUBLE_PASS_CONFIRMED
publication_status: IN_F4_F6_DOCUMENTARY_CHECKPOINT
---

# SI-RESEARCH-123 — BRAND-CAND-009 — F6: Product Bases

<!-- BRAND-CAND-009-F4-F6-CANONICAL-STATUS:START -->
## Estado canónico al checkpoint F4–F6 — 20/10/2026

**F6 CLOSED / AUTO.** `aut164`: doble PASS canónico, sin errores, advertencias ni limitaciones. Se normalizaron cuatro Product Bases candidatas `BASE-FIT-010..013`, vinculadas a `ML-0189..0192`. A2/A5 sin PB propia y A3 excluida por evidencia insuficiente de seguridad. No hay aprobación de SKU, proveedor, cotización, compra ni homologación.

**Estado documental a esta fecha:** F0–F3 publicado; F4–F6 preparado para su checkpoint documental. **Estado operativo posterior:** F7 ya obtuvo doble PASS en la matriz privada `aut165` (SHA-256 `0630735db2ad9122e4eb93ab196393aa8dd971d1afe8c08cc09cefd781c20aae`), pero su Research `SI-RESEARCH-124` se publicará junto con F8 después de la revisión y aprobación expresa del Founder. **F8 NOT OPENED / F14 NOT OPENED.** Las menciones posteriores de `PENDING_DOUBLE_PASS` o `NOT OPENED` para fases ya validadas son fotografías de la ejecución anterior al log, no su estado actual. Ni la shortlist ni las PB implican autorización de importación.
<!-- BRAND-CAND-009-F4-F6-CANONICAL-STATUS:END -->


## 1. Estado de la ejecución y contrato

**F0–F5 CLOSED.** F5 recibió doble PASS canónico para `aut163` el 20/10/2026: Data Fidelity Preflight v2.4 PASS y Matrix Validator 0.1.0 / `full-matrix-v5 0.7.0` PASS; `errors=0`, `warnings=0`, `limitations=[]`. **F6 AUTO / MATERIALIZED / PENDING_DOUBLE_PASS.** F7 NOT OPENED, F8 COLLABORATIVE, F14 NOT OPENED.

El contrato **SI-BIM-PROC-003 v1.0.6** establece que F6 toma F1–F5 y es **la primera fase que permite crear Product Bases (PB)**. Normalizar un formato funcional no significa haber seleccionado SKU, fabricante, proveedor, calidad demostrada o compra. F7 será la shortlist pre-origin; F8 requiere intervención/aprobación expresa del Founder.

**Pregunta F6:** ¿Qué formatos concretos y funcionalmente distintos de la cohorte F3 cuentan con evidencia suficiente para ser normalizados como candidatos de Product Base, sin inventar equivalencias técnicas ni adelantar sourcing?

## 2. Criterio de selección y alcance

Se priorizan **A1 (movilidad articular guiada)** y **A4 (equilibrio con desafío graduable)** conforme a F5 (`EVAL-0038`, potencial de marca **3/5, confianza baja**). Se eligen cuatro mecanismos físicos suficientemente distintos respaldados por cuatro publicaciones individuales con fuente explícita. **No existe una obligación de generar una PB por arquitectura ni por publicación.**

- **A1:** cinta textil con asas/bucles ≠ plataforma inclinada con posiciones regulables. Se normalizan por separado: guía de tracción frente a apoyo inclinado.
- **A4:** disco inflable y flexible ≠ tabla rígida oscilante. Se normalizan por separado: deformación/neumática frente a basculación rígida.
- **A2 y A5:** los deslizadores y la escalera de coordinación siguen documentados como **secundarios y condicionados**. No se les asigna Product Base en este cierre F6 por la superposición con fuerza/agilidad deportiva y la insuficiente hipótesis de diferenciación propia, **no por inexistencia de oferta o demanda observable**. Siguen conservadas sus publicaciones ML-0193/0194 y fuentes, sin modificarlas.
- **A3:** referencia de barra de ballet sólo contextual; no acredita carga, estabilidad ni seguridad para asistencias y transferencias. **Sin Product Base.**

## 3. Product Bases normalizadas — decisiones de Capa B

| Product Base | Arquitectura | Mecanismo / definición independiente de marca | Publicación y source binding | Señal observada de una sola publicación | Gate de seguridad / diferenciación |
|---|---|---|---|---|---|
| **BASE-FIT-010** | A1 | Cinta de elongación no elástica con asas y bucles graduados | `ML-0189` / `SRC-0544` / Expert | ARS 7.990; `+1000`; rating 4,4 (103 calificaciones) | Costuras y carga/tracción con ensayos; progresión comprensible; no mezclar con bandas de fuerza de `007` |
| **BASE-FIT-011** | A1 | Plataforma inclinada ajustable de elongación | `ML-0190` / `SRC-0545` / GMP | ARS 28.233,05; `+50`; rating 3,9 (12 calificaciones) | Angulación inicial realmente accesible, estabilidad antideslizante, trabas y límites de usuario |
| **BASE-FIT-012** | A4 | Disco inflable texturado de equilibrio | `ML-0191` / `SRC-0546` / PMG | ARS 21.990; `+1000`; rating 4,0 (2 calificaciones) | Carga y materiales ensayados, control de presión, superficie y prevención operativa de caídas (sin claim comercial) |
| **BASE-FIT-013** | A4 | Tabla rígida oscilante tipo Freeman | `ML-0192` / `SRC-0547` / New Plast | ARS 19.990; `+50`; rating 2,6 (5 calificaciones) | Riesgo alto: fricción, falla estructural y apoyo/entorno. Reseñas no equivalen a ensayo |

**Regla interpretativa:** las marcas Expert, GMP, PMG y New Plast pertenecen a las evidencias de mercado. **No** definen la identidad de las PB ni prueban equivalencia OEM. Una publicación por PB permite caracterizar el formato, pero **no** dimensiona el mercado, garantiza la calidad ni prueba disposición a pagar por nuestra marca.

**URLs originales de evidencia vinculada:**

- `ML-0189`: https://articulo.mercadolibre.com.ar/MLA-776567826-cinta-de-elongacion-pilates-yoga-tela-colores-el-rey-_JM?searchVariation=34984704980
- `ML-0190`: https://articulo.mercadolibre.com.ar/MLA-1375597897-elongador-piernas-yoga-tabla-inclinada-14n-flexibilidad-gmp-_JM
- `ML-0191`: https://articulo.mercadolibre.com.ar/MLA-620026985-disco-propiocepcion-equilibrio-balance-pinches-bosu-el-rey-_JM
- `ML-0192`: https://articulo.mercadolibre.com.ar/MLA-780628597-tabla-de-equilibrio-freeman-propiocepcion-disco-balance-_JM

Las URLs se preservan literalmente en `Publicaciones ML!O190:O193`. La documentación funcional de origen está en `SI-RESEARCH-120` (F3), `SI-RESEARCH-121` (F4) y `SI-RESEARCH-122` (F5); no se transfiere evidencia de otros Brand Candidates.

## 4. Separación de hechos, clasificación e interpretación

**Capa A (raw, inmutable):** se conservan por publicación las ventas visibles literales, PVP histórico, fecha, FX, URL, archivo PDF, opiniones y ledger. No se generan nuevas publicaciones, capturas ni verificaciones en F6, ni se reescriben los campos raw.

**Capa B (normalización):** se asignan cuatro nuevos IDs `BASE-FIT-010..013` a `Productos Base!A107:N110`; las relaciones operativas `Producto Base` / `ID Producto Base` se incorporan a `Publicaciones ML!Q190:R193` exclusivamente. No se asignan PB a ML-0193/0194.

**Capa C (interpretación):** las oportunidades de diferenciación derivan de fricciones observadas (costuras, ángulo inicial, fricción, fragilidad) y permanecen como **hipótesis condicionadas**, no prestaciones verificadas ni evidencia de prima de precio. Las reseñas sobre seguridad son indicios, no informes de laboratorio.

**Capa D (decisión):** F6 deja cuatro **CANDIDATE_PB**, no una shortlist aprobada. **F7** decidirá cuáles merecen un pase condicionado a F8 o deberían diferirse. No asignamos ranking económico, NCM, costos FOB/EXW, fletes, aranceles, landed, margen ni ROI.

## 5. Riesgos transversales y fronteras

- **A4 es un gate de seguridad alto**, aun cuando su implementación parezca simple. No se puede asumir resistencia, adherencia o prevención de caídas sin evidencia técnica de la variante exacta.
- **A1 requiere límites de tracción y progresión**; no promover promesas de tratamiento, fisioterapia o prevención de lesiones.
- `BASE-FIT-012/013` no son equivalentes a `BASE-FIT-004` de standing desk: el **problema central**, el contexto de uso y la progresión evaluada son distintos. Se conserva la alerta de semejanza funcional para prevenir duplicados al desarrollar catálogo comercial.
- Las señales `+1000` y `+50` son contadores visibles históricos de las publicaciones, **no ventas mensuales** ni proyecciones.
- La normalización no constituye autorización de origen, RFQ, muestras, homologación o compra. Continúan diferidas hasta la reunión con el socio y el despachante las profundizaciones de proveedores.

## 6. Materialización e integridad del snapshot

**Baseline F5 validada:** `matrix-aut163-brand-cand-009-phase5-brand-potential.xlsx` — SHA-256 `0d19fd39ca2dad470258e283286ffd443c8d58f9f03e2cffadd71f7ae5d352bd`.

**Snapshot F6:** `matrix-aut164-brand-cand-009-phase6-product-bases.xlsx` — SHA-256 `3e39e5e00b2c6b3706ed0b152d6d5a8d7c684df21d3eb5ea5b0d503426315a8c`.

**Cambios permitidos y auditados:** `Nichos!AD41:AF41` (3 celdas), `Publicaciones ML!Q190:R193` (8 celdas), `Productos Base!A107:N110` (56 celdas). **67 cambios en total**, todos en el scope autorizado; 0 celdas históricas alteradas fuera de ese alcance. Se preservan **29 hojas**, **37 componentes OOXML** y **1.958 fórmulas**, sin modificaciones de datos de F3/F4/F5. No se crean nuevas fuentes, evidencias, competencia ni evaluaciones.

## 7. Gate y continuidad

**Resultado propuesto:** `F6 MATERIALIZED / STRUCTURAL AUDIT PASS / PENDING_DOUBLE_PASS`. Para cerrar F6 son obligatorios **Data Fidelity Preflight v2.4 PASS + Matrix Validator 0.1.0 (`full-matrix-v5 0.7.0`) PASS** en Warp y revisión del log.

Sólo entonces: `F6 CLOSED / F7 NEXT (AUTO)`. F8 sigue COLLABORATIVE con revisión explícita del Founder; F14 NOT OPENED. La publicación documental F4–F6 se regulariza en este checkpoint. F7 se documentará junto con F8 después de su cierre colaborativo, aprobación expresa del Founder y doble PASS. Las matrices privadas, PDFs, scripts y logs permanecen fuera de Git.
