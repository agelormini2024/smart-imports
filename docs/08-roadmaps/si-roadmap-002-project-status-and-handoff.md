---
id: si-roadmap-002
title: Project Status and Handoff
description: Documento vivo que registra el estado actual, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports en un nuevo chat o sesión.
version: 0.7.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-08-03
tags:
  - status
  - handoff
  - continuity
  - roadmap
  - project-management
related:
  - si-roadmap-001
  - si-agent-001
  - si-research-001
  - si-research-002
  - si-research-003
  - si-research-004
  - si-decision-005
  - si-decision-006
  - si-decision-007
  - si-decision-008
  - si-func-001
  - si-decision-009
  - si-tech-001
audience:
  - founder
  - partner
  - assistant
phase: foundation
---

# SI-ROADMAP-002 — Estado actual y handoff de Smart Imports

> Este documento es el punto de entrada operativo obligatorio para saber dónde está parado el proyecto y retomar el trabajo sin depender de un chat específico.

## 1. Propósito

Este es un **documento vivo**. Debe responder rápidamente:

- ¿Qué estamos construyendo?
- ¿Qué ya está hecho?
- ¿Qué está en curso?
- ¿Qué está bloqueado?
- ¿Qué esperamos de terceros?
- ¿Cuál es la próxima acción?
- ¿Qué archivos y documentos deben utilizarse como fuente de verdad?
- ¿Qué información debe adjuntarse al abrir un nuevo chat?

No debe registrar cada conversación menor. Debe mantener el **estado operativo consolidado**.

## 2. Fuentes de verdad

### 2.1 Fuente documental

```text
Repositorio GitHub: https://github.com/agelormini2024/smart-imports
```

GitHub contiene la visión, metodología, decisiones, roadmaps y documentos de investigación vigentes.

### 2.2 Fuente operativa

Las matrices de referencia para continuidad son:

```text
aut29 → full-matrix-v3
aut30 → full-matrix-v4 con fuentes normalizadas
```

Secuencia reciente:

- `v3 aut(27)`: consolidación de Demanda y Competencia del Nicho 2.
- `v3 aut(28)`: formalización de la shortlist de Margen Potencial.
- `v3 aut(29)`: corrección de `Evaluaciones!A10`, reemplazando `EV-0009` por `EVAL-0009`.

La corrección no agregó una fila: reemplazó el ID inválido del registro existente.

### 2.3 Reglas operativas vigentes

- No modificar nombres ni orden de columnas existentes.
- Toda columna nueva se agrega al final.
- No duplicar IDs primarios dentro de una hoja.
- Referenciar productos existentes mediante `ID Producto Base`.
- No crear productos base duplicados.
- Generar XLSX importables compatibles con la matriz vigente.
- Las correcciones deben reemplazar filas incorrectas, no agregarse como duplicados.
- Los valores numéricos y fechas deben ser compatibles con configuración regional.
- GitHub es la fuente documental; la matriz es la herramienta operativa.

## 3. Snapshot

| Campo | Estado |
|---|---|
| Fecha de corte | 2026-08-03 |
| Fase | Foundation avanzada / cierre del Matrix Validator MVP |
| Nichos activos | 2 |
| Nicho 1 | Energía Solar Portátil — negociación pausada o en espera según proveedor |
| Nicho 2 | Viaje organizado y equipaje funcional — Demanda y Competencia consolidadas; shortlist de Margen aprobada |
| Matrices de referencia | `aut29` para v3; `aut30` para v4 normalizada |
| Último ID ML registrado | `ML-0069` |
| Último ID Producto Base registrado | `BASE-TRAVEL-026` |
| Último ID Competencia ML registrado | `COMP-0069` |
| Último ID Evidencia registrado | `EVID-0206` |
| Último ID Evaluación registrado | `EVAL-0010` |
| Último ID Tiempo registrado | `TIME-0022` |
| Matrix Validator | Implementación funcional avanzada; 78 tests; schemas v3/v4 |
| Repositorio de software | `agelormini2024/smart-imports-engine` — privado y operativo |
| Próxima acción principal | Normalizar `Resumen Competencia` y avanzar al cierre del MVP |

## 4. Visión vigente

Smart Imports no se define como una importadora tradicional. Su objetivo es construir una empresa que combine:

- Inteligencia comercial.
- Importación estratégica.
- E-commerce propio.
- Construcción de marca.
- Automatización.
- IA y agentes.
- Software propio.

El activo principal de largo plazo será:

```text
Smart Imports Intelligence Engine
```

Principio rector:

> Cada nuevo nicho debe producir conocimiento comercial y una pieza reutilizable del sistema.

## 5. Metodología vigente

```text
Nicho
↓
Subcategorías
↓
Fuentes
↓
Productos base
↓
Evidencias
↓
Evaluaciones
↓
Score + confianza
↓
Proveedores y RFQ
↓
Margen + facilidad de importación
↓
Decisión
```

Principios activos:

- Primero entender, después invertir.
- Evaluar nichos antes que productos.
- Evidencia antes que intuición.
- La matriz es la herramienta operativa inicial.
- GitHub es la fuente documental de verdad.
- Un dato comercial del proveedor no equivale automáticamente a evidencia técnica validada.
- No automatizar un proceso que todavía no fue comprendido manualmente.
- No forzar una tanda cuando la señal de mercado es insuficiente.
- Las decisiones de negociación, muestra, compra y pago requieren aprobación humana.

# 6. Nicho 1 — Energía Solar Portátil

## 6.1 Alcance

Incluido:

- Kits solares portátiles.
- Ventiladores solares.
- Power banks solares.
- Paneles solares portátiles pequeños y medianos.

Excluido:

- Generadores solares.
- Power stations.
- Sistemas solares completos.
- Soluciones de mayor escala.

## 6.2 Estado de criterios

| Criterio | Score | Confianza | Estado |
|---|---:|---|---|
| Demanda | 4 | Alta | Revisado |
| Competencia | 3 | Alta | Revisado |
| Margen Potencial | Preliminar | Baja/Media | En evaluación |
| Facilidad de Importación | Preliminar | Baja/Media | En evaluación |
| Potencial de Marca | 4 | Media | Revisado preliminarmente |
| Venta Impulsiva | 3 | Media | Revisado preliminarmente |
| Recompra | 2 | Alta | Revisado |
| Potencial IA | 4 | Alta | Revisado |
| Potencial Automatización | 5 | Alta | Revisado |
| Afinidad Personal | 5 | Alta | Revisado |

Margen e Importación no deben considerarse definitivos hasta procesar condiciones reales, documentación aplicable, packing y costos logísticos.

## 6.3 Kits AT-999 — Yiwu HaoYe / DAT

**Estado:** pausa operativa.

Hallazgos vigentes:

- El proveedor afirmó haber producido históricamente una versión OEM para Gadnic mediante una trading company.
- La configuración ofrecida actualmente presenta contradicciones entre batería, potencia y autonomía declaradas.
- El MOQ y el costo de muestra no resultan atractivos para continuar sin validación adicional.
- El proveedor volvió a consultar por la muestra y se respondió que no se avanzará todavía.

Decisión vigente:

> No comprar la muestra por ahora. Si AT-999 vuelve a ser prioridad, comprar primero una unidad Gadnic local como referencia, probarla y luego reabrir la negociación.

No asumir que la configuración interna actual de Gadnic coincide con la unidad ofrecida actualmente por el proveedor.

## 6.4 Paneles plegables — Shenzhen Shine Solar

**Estado:** proveedor comercialmente aceptable; compra de muestras pausada por prioridad.

Condiciones aclaradas:

- Acepta un pedido piloto mixto de 100 unidades, dividido entre dos modelos.
- La entrega al depósito del forwarder en Shenzhen está incluida.
- Las muestras serían idénticas a las unidades de producción.
- El producto terminado es IP67.
- La junction box es IP44.
- El proveedor no recomienda uso bajo lluvia.
- La referencia a “IP68 ETFE” describe la tecnología de laminación, no la clasificación del producto terminado.
- Las condiciones pueden quedar registradas en Trade Assurance.
- El proveedor no realizará una nueva reducción comercial ni del costo de muestras.

Decisión vigente:

> Mantener al proveedor como candidato aprobado, sin comprar muestras todavía. Reabrir sólo si los paneles pasan a la shortlist de productos.

## 6.5 Ventiladores y power banks

No hubo un cambio operativo relevante en el último ciclo.

Mantener como fuente de detalle:

- `SI-RESEARCH-003 — Supplier Negotiation Round 01`.
- La matriz privada y las conversaciones de proveedor.

No publicar en el repositorio:

- Precios objetivo.
- Cotizaciones originales.
- Datos personales o comerciales de contacto.
- Estrategias de negociación.

# 7. Nicho 2 — Viaje organizado y equipaje funcional

## 7.1 Estado general

```text
Demanda por subcategoría: cerrada
Competencia ML por subcategoría: cerrada
Evaluación consolidada de Demanda: 4 / Confianza Media
Evaluación consolidada de Competencia: 2 / Confianza Media
Shortlist de Margen Potencial: aprobada
Screening de Margen Potencial: pendiente
Facilidad de Importación: pendiente
```

Documentos principales:

- `SI-RESEARCH-001 — Niche 2 Selection`.
- `SI-RESEARCH-002 — Travel Organization Scope`.
- `SI-RESEARCH-004 — Niche 2 Demand and Competition Closure`.
- `SI-DECISION-007 — Select Travel Organization as Niche 2`.
- `SI-DECISION-008 — Close Niche 2 Demand and Competition`.

## 7.2 Subcategorías procesadas

| Tanda | Subcategoría | Estado |
|---|---|---|
| `TANDA-VIAJE-001` | Sets organizadores estándar para valija | Demanda y Competencia cerradas |
| `TANDA-VIAJE-002A` | Packing cubes de compresión | Demanda y Competencia cerradas |
| `TANDA-VIAJE-002B` | Bolsas de compresión al vacío con bomba | Demanda y Competencia cerradas |
| `TANDA-VIAJE-003` | Organizadores tecnológicos | Demanda y Competencia cerradas |
| `TANDA-VIAJE-004A` | Neceseres compartimentados | Demanda y Competencia cerradas |
| `TANDA-VIAJE-004B` | Kits de envases recargables | Demanda y Competencia cerradas |
| `TANDA-VIAJE-005` | Organizadores para calzado | Demanda y Competencia cerradas |

## 7.3 Subcategoría cerrada sin procesamiento

`TANDA-VIAJE-006 — Bolsas para ropa usada o húmeda`

- Screening manual: 20 minutos.
- Oferta relevante insuficiente.
- No se generaron publicaciones, productos base ni evidencias.
- Se cerró porque no modifica materialmente la evaluación del nicho.
- Puede reconsiderarse como SKU complementario si aparece nueva evidencia.

## 7.4 Síntesis preliminar

### Demanda

- Existe demanda real en varias subcategorías.
- Los mejores volúmenes se concentran generalmente en productos económicos y disponibles localmente.
- La demanda premium no quedó validada.

### Competencia

- Alta o muy alta en la mayoría de las subcategorías.
- Pocos productos base reales y muchos vendedores sobre bases equivalentes.
- Gran presión de precio y baja barrera técnica.
- La marca por sí sola no compensa una propuesta genérica.

### Diferenciación

Las oportunidades más defendibles se relacionan con:

- Calidad verificable.
- Mejor configuración del kit.
- Cierres, costuras y materiales.
- Dimensiones reales.
- Impermeabilidad o control de pérdidas.
- Instrucciones, rotulado y garantía.
- Sistema de productos y cross-selling.

### Shortlist aprobada para screening de Margen

1. **Kits de envases recargables**
   - `BASE-TRAVEL-021`
   - `BASE-TRAVEL-022`
2. **Bolsas de compresión al vacío**
   - Manual: `BASE-TRAVEL-010`
   - Eléctrica: `BASE-TRAVEL-012`
   - Benchmark premium: `BASE-TRAVEL-011`
3. **Kit textil reforzado o premium, condicionado al costo**
   - `BASE-TRAVEL-002`
   - `BASE-TRAVEL-003`

Watchlist:

- `BASE-TRAVEL-006`: competencia local baja, pero demanda todavía insuficientemente validada.

Regla de avance:

> No iniciar RFQ masivo. Primero realizar screening público y avanzar sólo con referencias que combinen señal económica, logística suficiente y diferenciación defendible.

## 7.5 Tiempos

- Tiempo activo conocido acumulado: **291 minutos**.
- Equivalente: **4 horas y 51 minutos**.
- `TIME-0012` quedó cerrado como actividad completada con tiempo no medido; no se inventó una duración.
- Últimos registros preparados:
  - `TIME-0021`: incorporación de Competencia de organizadores para calzado.
  - `TIME-0022`: screening de bolsas para ropa usada o húmeda.

## 7.6 Próximas acciones del Nicho 2

1. Mantener la shortlist como referencia aprobada.
2. No iniciar RFQ masivo todavía.
3. Cerrar operativamente el Matrix Validator.
4. Realizar screening público de costos según la prioridad comercial y con la matriz validada.
5. Comparar manual y eléctrica como propuestas distintas.
6. Registrar la decisión de avance o descarte por subcategoría.

# 8. Smart Imports Intelligence Engine

## 8.1 Estado

- Primer MVP: `Matrix Validator`.
- Repositorio privado creado y consolidado en `main`.
- CLI local read-only operativa.
- SheetJS CE aceptado como lector XLSX.
- `full-matrix-v3 0.1.0` y `full-matrix-v4 0.6.0` registrados.
- `aut29` y `aut30` validados con cero errores.
- Fuentes normalizadas mediante `Fuentes` y `Evidencia Fuentes`.
- 23 archivos de pruebas y 78 tests aprobados.
- Implementación funcional avanzada; cierre operativo pendiente.

## 8.2 Cobertura actual

Implementado:

- Hojas, columnas y posiciones.
- Claves primarias faltantes y duplicadas.
- Referencias simples y listas de evidencias.
- Valores permitidos y obligatorios seleccionados.
- Consistencia de fuentes globales.
- Reporte JSON, checksum y exit codes.

Pendiente:

- Hojas `Resumen *` normalizadas.
- Formato/secuencia general de IDs.
- Tipos, rangos y fórmulas prioritarias.
- E2E público y GitHub Actions.
- Limpieza de ExcelJS y release.

## 8.3 Orden recomendado

```text
Actualizar documentación
→ normalizar Resumen Competencia
→ extender a las otras hojas Resumen
→ crear aut31 y full-matrix-v5
→ completar E2E y CI
→ publicar release del Matrix Validator
→ continuar con el siguiente módulo del Engine
```

# 9. Trabajo completado desde el último handoff

- Repositorio privado `smart-imports-engine` creado.
- Foundation TypeScript con Node 24 y pnpm 11.
- Spike ExcelJS ejecutado y descartado para matrices reales.
- SheetJS CE aceptado mediante ADR-0001.
- Snapshot sparse y verificación SHA-256.
- CLI, reportes y exit codes implementados.
- Reglas estructurales, IDs, referencias, valores y consistencia implementadas.
- Normalización de fuentes aceptada mediante ADR-0002.
- `aut30` creada con `Fuentes` y `Evidencia Fuentes`.
- `full-matrix-v4` evolucionado hasta `0.6.0`.
- 78 tests aprobados.
- Rama de feature integrada mediante fast-forward a `main`.
- Documentación de estado y roadmap de cierre preparada.

# 10. Trabajo en curso

- Actualización coordinada de la documentación pública y privada.
- Diseño de normalización de las tres hojas `Resumen *`.
- Definición del subconjunto semántico requerido para la release.
- Preparación de fixtures públicos end-to-end y CI.
- Cierre de Margen e Importación del piloto solar cuando exista información confiable.
- Screening de Margen del Nicho 2 según prioridades comerciales.

# 11. Bloqueos y dependencias

| Bloqueo | Dependencia | Acción |
|---|---|---|
| Cierre del Matrix Validator | Normalización de `Resumen *` | Diseñar `Resumen Competencia` primero y validar el patrón |
| Release reproducible | Fixtures públicos y CI | Crear E2E sanitizado y GitHub Actions |
| Retiro del warning provisional | Cobertura acordada completa | Definir DoD y cerrar reglas bloqueantes |
| Margen solar definitivo | Condiciones y documentación coincidente | Mantener estados preliminares |
| AT-999 | Validación técnica real | Mantener pausa |
| Paneles Shine Solar | Prioridad comercial | Mantener candidato sin desembolso |
| Screening de Margen del Nicho 2 | Prioridad comercial y matriz estable | Mantener shortlist; no iniciar RFQ masivo |

# 12. Prioridades ordenadas

## Prioridad 1 — Actualización documental

- Alinear README, SI-FUNC-001, SI-TECH-001, SI-AGENT-001 y roadmaps.
- Mantener un estado técnico específico en el repositorio privado.

## Prioridad 2 — Hojas Resumen

- Inventariar `Resumen Competencia`.
- Diseñar estructura tabular.
- Migrar y validar.
- Extender a `Resumen Margen` y `Resumen Tanda`.

## Prioridad 3 — Cierre técnico del Validator

- Crear `aut31` y `full-matrix-v5`.
- Completar reglas semánticas prioritarias.
- Incorporar E2E público y CI.
- Eliminar ExcelJS y spikes.
- Retirar el warning provisional y publicar release.

## Prioridad 4 — Margen Potencial del Nicho 2

- Mantener la shortlist aprobada.
- Realizar screening público según prioridad.
- Avanzar a RFQ sólo con finalistas.

## Prioridad 5 — Cierre del piloto solar

- Completar Margen e Importación únicamente con información confiable.
- Mantener muestras y proveedores pausados hasta recuperar prioridad.

# 13. Protocolo para abrir un nuevo chat

En el nuevo chat:

1. Compartir el repositorio.
2. Adjuntar la matriz necesaria para la tarea: `aut29` para v3 o `aut30` para v4.
3. Pedir que se revise primero `SI-ROADMAP-002`.
4. Pedir que se revise `SI-RESEARCH-004` y `SI-DECISION-008`.
5. No adjuntar nuevamente todos los PDFs históricos.
6. Adjuntar sólo documentos o respuestas nuevas que no estén consolidadas.
7. Confirmar que la próxima acción es cerrar el Matrix Validator, comenzando por las hojas `Resumen *`.

Documentos mínimos a revisar:

```text
README.md
docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md
docs/08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md
docs/03-functional-specifications/si-func-001-matrix-validator.md
docs/04-technical-specifications/si-tech-001-matrix-validator-architecture.md
docs/09-decision-log/si-decision-009-separate-knowledge-and-engine-repositories.md
docs/05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md
docs/06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md
docs/06-research/niche-002-travel-organization/si-research-004-demand-competition-closure.md
docs/09-decision-log/si-decision-007-select-travel-organization-as-niche-2.md
docs/09-decision-log/si-decision-008-close-niche-2-demand-and-competition.md
```

## 13.1 Prompt sugerido

```text
Estamos continuando el proyecto Smart Imports.

Repositorio:
https://github.com/agelormini2024/smart-imports

Antes de proponer cambios, revisá especialmente:
- README.md
- docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md
- docs/08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md
- docs/03-functional-specifications/si-func-001-matrix-validator.md
- docs/05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md
- docs/06-research/niche-002-travel-organization/si-research-004-demand-competition-closure.md
- docs/09-decision-log/si-decision-008-close-niche-2-demand-and-competition.md

Tomá SI-ROADMAP-002 como punto de entrada operativo y el repositorio como fuente documental de verdad.

Voy a adjuntar la matriz necesaria para la tarea:
- aut29 para compatibilidad v3, o
- aut30 para fuentes normalizadas v4

Estado resumido:
- Nicho 1: Demanda y Competencia cerradas; Margen e Importación siguen en evaluación; proveedores y muestras pausados por prioridad.
- Nicho 2: Demanda 4 / Confianza Media y Competencia 2 / Confianza Media consolidadas.
- Shortlist aprobada: kits de envases recargables, compresión manual y eléctrica, y kit textil condicional.
- No iniciar RFQ masivo antes del screening público.
- Matrix Validator: implementación funcional avanzada; 78 tests; cierre operativo pendiente.
- aut(29) corrige el ID EV-0009 por EVAL-0009 reemplazando la fila existente.

Reglas obligatorias:
- Trabajar sobre la matriz más reciente adjunta.
- Preservar nombres y orden de columnas.
- Agregar columnas nuevas sólo al final.
- No duplicar IDs.
- Mantener relaciones mediante ID Producto Base.
- Las correcciones reemplazan filas.
- No publicar información comercial confidencial.

Primero confirmá los documentos revisados, la matriz vigente y la próxima acción.
Después continuá con el cierre del Matrix Validator, priorizando la normalización de las hojas Resumen.
```

# 14. Checklist de cierre de sesión

- [x] Actualizar fecha de corte.
- [x] Confirmar matriz vigente.
- [x] Registrar trabajo completado.
- [x] Actualizar trabajo en curso.
- [x] Actualizar estado de proveedores relevantes.
- [x] Definir próxima acción principal.
- [x] Registrar decisión nueva.
- [x] Preparar prompt de continuidad.
- [ ] Subir documentos actualizados a GitHub.
- [ ] Adjuntar `aut29` o `aut30` según el schema requerido.

# 15. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-16 | Snapshot inicial, protocolo de actualización y handoff para nuevas sesiones. |
| 0.2.0 | 2026-07-17 | Selección y alcance del Nicho 2, proveedores y prompt de continuidad. |
| 0.3.0 | 2026-07-20 | Primera ronda de proveedores y matriz v3 aut(12). |
| 0.4.0 | 2026-07-23 | Cierre de Demanda y Competencia del Nicho 2, estado actualizado de AT-999 y Shine Solar, matriz v3 aut(26) y nuevo prompt de continuidad. |
| 0.5.0 | 2026-07-24 | Consolidación y shortlist del Nicho 2, matriz v3 aut(29), primer caso real del Validator y creación de SI-FUNC-001. |
| 0.6.0 | 2026-07-24 | SI-FUNC-001 aprobado, separación de repositorios aprobada y SI-TECH-001 preparado. |
| 0.6.1 | 2026-07-24 | Se adopta pnpm 11 como package manager del Engine. |
| 0.7.0 | 2026-08-03 | Handoff actualizado con Matrix Validator funcional, schemas v3/v4, 78 tests y prioridades de cierre. |
