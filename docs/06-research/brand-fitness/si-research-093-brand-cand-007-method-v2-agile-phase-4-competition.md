---
id: si-research-093
title: BRAND-CAND-007 — Method v2 — F4 Competencia
version: 0.1.1
status: closed
phase: F4
mode: AUTO
brand: brand-fitness
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
scope_alias: Nicho ID 38
scope_value: Marca Fitness — fuerza accesible y compacta
baseline: aut128
matrix: aut129
created: 2026-10-13
updated: 2026-10-14
related:
  - si-bim-proc-003
  - si-decision-019
  - si-research-092
---

# SI-RESEARCH-093 — BRAND-CAND-007 — F4 Competencia

## 1. Alcance y regla de continuidad

F4 se ejecuta **AUTO** sobre la cohorte cerrada en F3 (`ML-0178..ML-0183`), dos referencias por arquitectura. No se crean nuevos registros de `Publicaciones ML`, no se modifican los precios ni los contadores históricos y no se evalúa de nuevo la demanda `3/5 / Media`. Se reutilizan las seis fuentes originales `SRC-0525..SRC-0530` y los PDF de captura del 13/10/2026.

Objetivo: identificar estructura competitiva observable, diferencias funcionales, barreras y posibles espacios de diferenciación de una marca orientada a **construir y conservar fuerza útil** sin gimnasio completo, mucho espacio ni equipamiento excesivo.

**F4 no demuestra saturación de mercado ni rentabilidad.** Seis productos no son un censo ni una muestra estadísticamente representativa.

## 2. Capa A — Hechos crudos documentados (captura F3 del 2026-10-13)

| ML ID | Arquitectura | Marca | Precio ARS en PDF | Calificación | Calificaciones | Fuente |
|---|---|---|---:|---:|---:|---|
| ML-0178 | Bandas con agarres/anclaje | Gadnic | $39.999,00 | 4,8 | 830 | `SRC-0525` / PDF Gadnic |
| ML-0179 | Bandas tipo loop | Alpina | $30.185,28 | 4,9 | 1.349 | `SRC-0526` / PDF Alpina |
| ML-0180 | Mancuerna/barra ajustable 20 kg | GMP | $93.018,00 | 4,7 | 454 | `SRC-0527` / PDF GMP |
| ML-0181 | Mancuernas/barra ajustables 20 kg | BS Fit | $64.999,00 | 4,8 | 1.755 | `SRC-0528` / PDF BS Fit |
| ML-0182 | Suspensión regulable | MrGym | $18.919,12 | 4,1 | 126 | `SRC-0529` / PDF MrGym |
| ML-0183 | Suspensión con anclaje de acero | FIT MARK | $55.797,14 | 4,8 | 1.409 | `SRC-0530` / PDF FIT MARK |

Fuentes exactas, PDF completos, URL de producto/catálogo y número de publicación constan en `Publicaciones ML`, `Fuentes` y `Verificaciones ML` de `aut128`; para F4 se reaprovechan esos mismos bindings. Los precios y ratings citados describen el **momento de la captura**, no precios vigentes garantizados. Las calificaciones pueden incluir otros países o variantes según la interfaz de Mercado Libre: no son una prueba independiente de calidad.

**Diferencias relevantes mostradas en las fichas:** Gadnic anuncia bandas de cinco niveles con agarres y anclaje de puerta; Alpina presenta cinco bandas loop con usos de fuerza, asistencia y movilidad. GMP y BS Fit ofrecen sets ajustables con disco/barra, pero difieren en detalles de composición y materiales. MrGym declara 120 kg soportados; FIT MARK declara 200 kg y anclaje metálico: ambos son claims comerciales sin certificación externa examinada. El resumen automático de opiniones de MrGym advierte sobre costuras y empuñaduras; es una señal cualitativa, **no** una tasa verificada de fallas.

## 3. Capa B — Clasificación

- **A1, resistencia elástica**: `ML-0178` DIRECT / `ML-0179` DIRECT_CONDITIONED (usos múltiples). No equiparar tubos con agarres y bandas loop como idénticos.
- **A2, carga ajustable**: `ML-0180` y `ML-0181` DIRECT. Ambos anuncian 20 kg, pero no se presume equivalencia técnica de componentes, materiales o garantía.
- **A3, suspensión**: `ML-0182` y `ML-0183` DIRECT_CONDITIONED por dependencia crítica del sistema de anclaje y calidad de ensamblado.
- Los seis son competidores **dentro del pequeño conjunto observado**; `Competidor Real = Sí` identifica comparabilidad respecto del problema, no presencia exhaustiva de competidores en el mercado.
- `Nivel de Saturación = No determinada`: la muestra no permite medirlo. `Competencia Precio` y `Fortaleza Vendedor` son interpretaciones cualitativas basadas en las fichas y no cifras de market share.

## 4. Capa C — Interpretación competitiva

| Arquitectura | Presión observable | Riesgos de entrada | Espacio de marca hipotético |
|---|---|---|---|
| A1 Bandas | Dos marcas visibles con tiendas oficiales y calificaciones elevadas, formatos diferentes | Percepción de commodity; resistencia variable; anclaje y desgaste | Instrucción real de progresión, calidad verificada, accesorios útiles y reposición |
| A2 Ajustables | Dos kits de 20 kg y diferencia importante de precio en la misma captura | Peso/logística, retención de discos y mecanismo a rosca, marcas con reseñas | Progresión clara, ergonomía, bloqueo seguro, piezas y garantía |
| A3 Suspensión | Dos posicionamientos de precio, evaluación cualitativa de seguridad | Consecuencias de falla de anclaje/costura, montaje incorrecto, claims de carga | Pruebas documentadas de resistencia, instalación segura, manual y garantía |

La diferencia de precio entre dos productos **no prueba** disposición a pagar un premium de marca. Los contadores de ventas ya usados en F3 no se reinterpretan como cuota de mercado ni se suman como competencia. Este análisis no evalúa origen, sourcing ni landed cost.

## 5. Capa D — Evaluación AUTO de F4

**Competencia registrada: `3/5` — Confianza `Media`.**

Justificación: presencia de marcas y vendedores fuertes con ofertas funcionalmente pertinentes, pero diferenciación potencial en seguridad, confiabilidad, progresión, educación y posventa. No corresponde asignar presión competitiva extrema por una muestra pequeña, ni calificarla como baja porque existen claros comparables.

`EVAL-0033` representa la interpretación agregada. Los registros `COMP-0176..COMP-0181` reflejan la cohorte completa; seis nuevas evidencias `EVID-0306..EVID-0311` derivan de las fuentes F3 y se vinculan mediante `EVSRC-0722..EVSRC-0727` sin alterarlas.

La evaluación **no constituye** decisión de portafolio, producto, proveedor ni importación. F5 evaluará Potencial de Marca y F6 es la primera fase que puede normalizar Product Bases.

## 6. Materialización, doble PASS y cierre de F4

```text
Baseline validada: aut128 / F3 CLOSED
F4: COMP-0176..COMP-0181
Evidencias: EVID-0306..EVID-0311
Bindings: EVSRC-0722..EVSRC-0727 → SRC-0525..SRC-0530
Evaluación: EVAL-0033 = Competencia 3/5 / Confianza Media
Matriz: matrix-aut129-brand-cand-007-phase4-competition-pre-gate.xlsx
SHA-256: 287d0f6bd93ce167b92f8967c2cf1690d0a620d58829e8cb827f13481983294f
Data Fidelity Preflight v2.4: PASS (6 publicaciones, 6 verificaciones, 0 Product Bases)
Matrix Validator full-matrix-v5 0.7.0: PASS (0 errores / 0 warnings / 0 info)
F4: CLOSED — AUTO
Next: F5, ejecutada AUTO; checkpoint documental conjunto después de F6.
```

El doble PASS fue confirmado en el log consolidado de validación F4–F6 mediante el script consolidado. La denominación técnica `pre-gate` del XLSX se conserva por trazabilidad y no significa que la validación continúe pendiente.
