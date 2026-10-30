---
id: si-research-workbench-006
title: CP03 — Decision Reports piloto y economía de screening
version: 0.1.0
status: draft
owner: Founder
reviewer: CTO/CSO Virtual
created: 2026-10-30
updated: 2026-10-30
tags: [research-workbench, cp03, decision-reporter, commercial-screening, pilot-001]
related: [si-research-workbench-002, si-research-workbench-003, si-research-workbench-004, si-research-workbench-005]
---
# SI-RESEARCH-WORKBENCH-006 — CP03: Decision Reports piloto

> **Checkpoint documental, no gate de compra.** Registra el producto de trabajo y las decisiones de diseño. No publica documentos sensibles ni reemplaza el corpus histórico de Method v2 o las matrices `autXXX`.

## 1. Propósito y fuente de verdad

Transformar la investigación RW-P001 en informes de oportunidad comercial para evaluar con el socio y llevar **candidatos suficientemente fundamentados** al despachante. La investigación comercial, matriz reducida y el método económico v2 aportan datos y cálculos; el **Decision Report explica el negocio en lenguaje llano**. El objetivo ulterior, tras revisión aduanera y recálculo, es seleccionar **3 o 4 productos** de primera importación; no confundir con cantidad de candidatos al despachante.

El repositorio público describe método, decisiones y estado. El expediente privado conserva fuentes originales, PDFs, mensajes de proveedor, cotizaciones y simulaciones concretas. Ver política en `docs/06-research/README.md`.

## 2. Versiones y alcance de los entregables privados

| Candidato | Reporte privado (referencia documental) | Estado de revisión | Decisión exploratoria |
|---|---|---|---|
| `RW-P001-C08` | Decision Report C08 v0.4 (privado) | v0.4, DRAFT; hipótesis de precio de venta revisada | CONTINUAR CONDICIONADO. Precio objetivo aún no validado por demanda ni costo de importación. |
| `RW-P001-C01` | Decision Report C01 v0.1 (privado) | v0.1, DRAFT | CONTINUAR CONDICIONADO. Kit y precisión sin equivalencia técnica acreditada; holgura preliminar ajustada. |
| `RW-P001-C03` | Decision Report C03 v0.1 (privado) | v0.1, DRAFT | CONTINUAR CONDICIONADO. Diferenciar 5 L, chaleco solo/recipientes y MOQ; no hay oferta exacta plenamente confirmada. |

`C08` pasó por versiones **v0.1 → v0.2 → v0.3 → v0.4**: (a) nueva estructura de informe independiente del Reporter histórico, (b) se añadió simulación, (c) se recuperó la secuencia didáctica presupuesto→headroom→costo puesto→margen/ROI→caja, y (d) se cambió **solo la hipótesis de precio de venta** para evaluar la sensibilidad comercial. No se modificaron cotizaciones, validación de waterproofing ni estado aduanero por ese cambio. Las versiones anteriores son antecedentes privados, no nueva baseline de compra.

Los pilotos **no están certificados por un generador**; fueron producidos con trabajo asistido, sin pruebas automatizadas de consistencia contra un esquema de v3. `CP02` y sus decisiones siguen vigentes.

## 3. Hechos y límites por candidato (sin datos negociados)

| Candidato | Lo que aporta evidencia | Condición que puede cambiar la decisión |
|---|---|---|
| C08 auriculares natación | Publicaciones locales, modelos de origen, respuesta comercial y evidencia **parcial** de IPX8 para S10 | Aceptación de precio local para equivalente; costo puesto plausible; documentación técnica y posventa **a profundizar tras despachante** |
| C01 kit dinamométrico | Benchmark local y dos publicaciones de kits con configuraciones distintas | Equivalencia exacta, precisión/calibración y costo de importación suficiente para preservar margen |
| C03 chaleco hidratación 5 L | Demanda visible; ofertas de origen; restricciones de stock y MOQ | Configuración comparable, cantidad inicial, materiales de recipientes y economía de inventario |

Ninguno es **COMERCIALMENTE VIABLE VALIDADO** ni fue promovido formalmente a shortlist de importación. Precios de ML y contadores visibles no demuestran demanda mensual; las prestaciones publicadas no acreditan calidad o seguridad.

## 4. Novedades desde CP02: proveedores

CP02 congeló un estado histórico de **cuatro respuestas y tres silencios** en su fecha de corte. **Después** se recibió respuesta de `C03-S01` (Xiamen Youk): MOQ declarado de 500 piezas, tres configuraciones cotizables aún sin precios confirmados y declaración comercial de aptitud del bladder para contacto alimentario, sin informe recibido. El estado conocido de la ronda original pasó a **cinco respuestas y dos silencios**, sin reescribir retroactivamente CP02. Tucson aportó también una página adicional de resultado de ensayo IPX8 del modelo S10 (una muestra, 2024, resultado declarado favorable), pero sin profundidad/duración ni informe íntegro. La evidencia permanece **parcial**, no validación técnica del lote.

## 5. Método económico consolidado

Se recuperaron `Headroom`, `Landed Cost`, margen, ROI económico y caja de Method v2 y de la **Guía económica didáctica v0.4** (evidencia privada). Contrato de cálculo y denominadores: `SI-RESEARCH-WORKBENCH-005`.

Puntos de control: precio local bruto observado **vs propuesto**, moneda/TC fechado, deducción del canal, objetivo de margen aplicado sobre ingreso **neto**, gastos comerciales sobre **bruto**, costo máximo permitido, precio origen comparable, holgura, factores de sensibilidad **no calibrados**, margen/ROI derivados y desembolso total de caja **separado**. Un resultado positivo en sensibilidad no es landed confirmado. Factores heredados no son probabilidades ni cotizaciones del despachante.

La matriz CP03 reducida y las fichas de hoja de cálculo previas son **prototipos no validados por Engine**; no se publican como reemplazo de `aut171`, cuya referencia de Method v2 debe permanecer intacta.

## 6. Prioridad operativa y separación de actores

**Antes del despachante:** evidencia suficiente para una oportunidad, comparables argentinos, proveedores de referencia, costos de origen exploratorios, escenarios conservadores plausibles, riesgos y preguntas profesionales. Se acepta incertidumbre señalada. **No** ejecutar ahora muestras, homologación, auditorías de fábrica, negociación extensa, compras ni investigación exhaustiva de un proveedor.

**Despachante:** revisar NCM, intervenciones, documentación de baterías/contacto alimentario cuando corresponda, transporte y costo nacionalizado; determinar si vale la pena continuar.

**Después del visto bueno:** profundizar fabricante/proveedor, pruebas técnicas, QA, muestras y negociación para los productos que superen el filtro externo.

## 7. Incidencias y aprendizaje v3

- Un reporte para socio debe comunicar decisión, cifras interpretables y razones, no volcar la matriz completa.
- Una publicación puede mezclar modelos o declarar certificaciones que no prueban el SKU; separar modelo, variante, anunciante, fabricante potencial y evidencia del ensayo.
- Guardar cambios de hipótesis de precio **sin** borrar resultados de versiones anteriores.
- Mostrar sensibilidad como multiplicación del **precio de origen**, con explicación de cada escenario, no etiquetarla como costos reales.
- Diferenciar comparables del mercado realmente equivalentes; precio objetivo superior requiere evidencia de aceptación, no inferir demanda del precio de publicación.
- Una métrica de margen no reemplaza demanda, riesgo de garantía, MOQ, caja ni primera etapa.
- Registrar tiempo activo y retrabajo si se mide; **no hay tiempos comprobados para CP03**.

## 8. Pendientes explícitos

1. Revisar con Eduardo las tres fichas; registrar preguntas de comprensión y correcciones solicitadas.
2. Reexaminar referencias argentinas de C08 y señales acumuladas de venta; contrastar **calidad/equivalencia** frente a una hipótesis de ticket superior. El Founder observó anuncios superiores a sus referencias iniciales y una publicación cara con contador acumulado alto; requiere captura fechada y comprobación.
3. Evitar profundizar proveedores antes del despachante. Si surge un dato exploratorio espontáneo, incorporarlo como declaración, no homologación.
4. Someter oportunidades suficientemente sustentadas a revisión aduanera, estimar landed con datos profesionales y recalcular economía/caja.
5. Refinar formato/plantilla y controles de reproducción para v3 **después** del aprendizaje comercial; no iniciar una implementación amplia ahora.
6. Integrar estos documentos a `main` mediante revisión de diffs y aprobación humana; **hasta commit+push verificado, checkpoint documental pendiente de publicación**.

## 9. Control y trazabilidad documental

- Anterior: `SI-RESEARCH-WORKBENCH-002` (screening), `003` (pipeline), `004` (C01–C15) y `SI-ROADMAP-002`.
- Nuevo contrato: `SI-RESEARCH-WORKBENCH-005`.
- Matriz Method v2 `aut171` y guía económica v0.4: fuentes históricas privadas; no se sobrescriben.
- Informes C01/C03/C08, sus versiones editables, cálculos originales, cotizaciones y capturas: privado `~/Desktop/smart-imports-evidencias-privadas/RW-P001/CP03/`.
- La continuidad detallada para otro chat está en un **handoff privado separado**, no en el repo público. Incorporar después el SHA del commit y el resultado remoto verificado.

## Changelog

- **2026-10-30 · v0.1.0 DRAFT** — Checkpoint de los primeros tres Decision Reports del Workbench; formato, método económico y gates documentados, publicación Git aún pendiente.
