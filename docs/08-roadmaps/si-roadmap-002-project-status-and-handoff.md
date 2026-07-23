---
id: si-roadmap-002
title: Project Status and Handoff
description: Documento vivo que registra el estado actual, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports en un nuevo chat o sesión.
version: 0.4.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-07-23
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

La matriz más reciente recibida al cierre fue:

```text
Smart Imports - matriz de oportunidades - v3 aut(25).xlsx
```

Se preparó una versión de continuidad que agrega `TIME-0021` y `TIME-0022`:

```text
Smart Imports - matriz de oportunidades - v3 aut(26).xlsx
```

La versión `v3 aut(26)` debe utilizarse en el siguiente chat.

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
| Fecha de corte | 2026-07-23 |
| Fase | Foundation avanzada / validación comparativa del método |
| Nichos activos | 2 |
| Nicho 1 | Energía Solar Portátil — negociación pausada o en espera según proveedor |
| Nicho 2 | Viaje organizado y equipaje funcional — Demanda y Competencia ML cerradas |
| Matriz vigente para continuidad | `Smart Imports - matriz de oportunidades - v3 aut(26).xlsx` |
| Último ID ML | `ML-0069` |
| Último ID Producto Base | `BASE-TRAVEL-026` |
| Último ID Competencia ML | `COMP-0069` |
| Último ID Evidencia | `EVID-0206` |
| Último ID Tiempo | `TIME-0022` |
| Intelligence Engine | Matrix Validator pendiente de especificación e implementación |
| Próxima acción principal | Consolidar Demanda y Competencia del Nicho 2 en Evaluaciones y Nichos |

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
Evaluación consolidada del nicho: pendiente
Margen Potencial: pendiente
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

### Shortlist preliminar para Margen

Debe confirmarse mediante evaluación formal. Candidatos a comparar:

1. Kits de envases recargables.
2. Bolsas de compresión al vacío con bomba.
3. Un kit textil sólo si los costos permiten evitar competencia directa por precio.

## 7.5 Tiempos

- Tiempo activo conocido acumulado: **291 minutos**.
- Equivalente: **4 horas y 51 minutos**.
- `TIME-0012` permanece sin tiempo medido.
- Últimos registros preparados:
  - `TIME-0021`: incorporación de Competencia de organizadores para calzado.
  - `TIME-0022`: screening de bolsas para ropa usada o húmeda.

## 7.6 Próximas acciones del Nicho 2

1. Crear `EVAL` de Demanda consolidada.
2. Crear `EVAL` de Competencia consolidada.
3. Actualizar la fila del Nicho 2 en `Nichos`.
4. Definir shortlist aprobada para Margen Potencial.
5. Decidir entre screening de costos públicos o RFQ.
6. Registrar la decisión de avance o descarte por subcategoría.

# 8. Smart Imports Intelligence Engine

## 8.1 Estado

- Nombre y visión definidos.
- Estrategia incremental aprobada.
- Primer MVP seleccionado: `Matrix Validator`.
- El proceso manual ya produjo suficientes reglas y errores reales para iniciar implementación.

## 8.2 Alcance mínimo del Matrix Validator

- Hojas requeridas.
- Nombres y orden de columnas.
- IDs primarios y formatos.
- IDs duplicados.
- Secuencias y colisiones.
- Referencias a `ID Producto Base`.
- Relaciones entre publicaciones, competencia y evidencias.
- Valores permitidos.
- Filas incompletas.
- Errores bloqueantes y advertencias.

Stack preliminar:

```text
TypeScript
Node.js
Zod
ExcelJS
CLI
Vitest o Jest
```

## 8.3 Orden recomendado

```text
Consolidar Nicho 2
→ actualizar documentación
→ especificar Matrix Validator
→ implementar validaciones mínimas
→ volver a Margen Potencial
```

# 9. Trabajo completado desde el último handoff

- Registro operativo completo del Nicho 2.
- Demanda y Competencia de siete subcategorías.
- Normalización repetida de productos base y variantes.
- Registro sistemático de tiempos.
- Cierre metodológico de una subcategoría por señal insuficiente.
- Respuesta y pausa del proveedor AT-999.
- Aclaración comercial y técnica de Shine Solar.
- Generación de importables compatibles hasta la matriz `v3 aut(25)`.
- Preparación de `v3 aut(26)` para continuidad.
- Creación de `SI-RESEARCH-004` y `SI-DECISION-008`.

# 10. Trabajo en curso

- Evaluación consolidada de Demanda del Nicho 2.
- Evaluación consolidada de Competencia del Nicho 2.
- Shortlist para Margen Potencial.
- Cierre de Margen e Importación del piloto solar.
- Especificación e implementación del Matrix Validator.

# 11. Bloqueos y dependencias

| Bloqueo | Dependencia | Acción mientras se espera |
|---|---|---|
| Margen solar definitivo | Condiciones y documentación coincidente | Mantener estados preliminares y no comprar muestras sin prioridad |
| AT-999 | Validación técnica real | Mantener pausa; probar unidad local sólo si vuelve a ser prioritario |
| Paneles Shine Solar | Prioridad comercial y decisión de muestra | Mantener candidato aprobado sin desembolso |
| Evaluación final del Nicho 2 | Consolidación de evidencias | Crear EVAL de Demanda y Competencia |
| Shortlist del Nicho 2 | Evaluación consolidada | No iniciar RFQ masivo todavía |
| Matrix Validator | Tiempo de implementación | Extraer reglas desde la matriz real y los importables |

# 12. Prioridades ordenadas

## Prioridad 1 — Consolidar Nicho 2

- Crear evaluación de Demanda.
- Crear evaluación de Competencia.
- Actualizar `Nichos`.
- Definir shortlist.

## Prioridad 2 — Actualizar documentación

- Reemplazar `SI-ROADMAP-002`.
- Incorporar `SI-RESEARCH-004`.
- Incorporar `SI-DECISION-008`.
- Actualizar README e índice del Decision Log.

## Prioridad 3 — Matrix Validator

- Definir contrato de entrada.
- Definir salida de errores y advertencias.
- Implementar validación de hojas, columnas, IDs y relaciones.
- Agregar tests con la matriz vigente.

## Prioridad 4 — Margen Potencial

- Elegir dos o tres subcategorías.
- Definir productos base representativos.
- Obtener costos preliminares.
- Simular landed cost y margen.

## Prioridad 5 — Proveedores solares

- Mantener pausas actuales.
- Procesar únicamente respuestas que cambien una decisión.
- No pagar muestras sin prioridad aprobada.

# 13. Protocolo para abrir un nuevo chat

En el nuevo chat:

1. Compartir el repositorio.
2. Adjuntar `Smart Imports - matriz de oportunidades - v3 aut(26).xlsx`.
3. Pedir que se revise primero `SI-ROADMAP-002`.
4. Pedir que se revise `SI-RESEARCH-004` y `SI-DECISION-008`.
5. No adjuntar nuevamente todos los PDFs históricos.
6. Adjuntar sólo documentos o respuestas nuevas que no estén consolidadas.
7. Confirmar que la próxima acción es consolidar Demanda y Competencia del Nicho 2.

Documentos mínimos a revisar:

```text
README.md
docs/08-roadmaps/si-roadmap-002-project-status-and-handoff.md
docs/08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md
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
- docs/05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md
- docs/06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md
- docs/06-research/niche-002-travel-organization/si-research-004-demand-competition-closure.md
- docs/09-decision-log/si-decision-007-select-travel-organization-as-niche-2.md
- docs/09-decision-log/si-decision-008-close-niche-2-demand-and-competition.md

Tomá SI-ROADMAP-002 como punto de entrada operativo y el repositorio como fuente documental de verdad.

Voy a adjuntar:
Smart Imports - matriz de oportunidades - v3 aut(26).xlsx

Estado resumido:
- Nicho 1, Energía Solar Portátil: Demanda y Competencia cerradas; AT-999 y muestras de paneles están pausados por priorización.
- Nicho 2, Viaje organizado y equipaje funcional: Demanda y Competencia ML cerradas en siete subcategorías.
- TANDA-VIAJE-006 se cerró sin procesamiento formal por oferta relevante insuficiente.
- Próxima acción: consolidar Demanda y Competencia del Nicho 2 en Evaluaciones y Nichos y definir shortlist para Margen Potencial.
- Intelligence Engine: Matrix Validator es el primer MVP pendiente de implementación.

Reglas obligatorias de la matriz:
- Trabajar siempre sobre la versión más reciente adjunta.
- Preservar exactamente nombres y orden de columnas.
- Las columnas nuevas se agregan sólo al final.
- No duplicar IDs primarios.
- Referenciar productos existentes mediante ID Producto Base.
- No crear productos base duplicados.
- Las correcciones reemplazan; no se agregan como filas duplicadas.

No modifiques metodología, IDs, hojas o estructura sin explicar primero el impacto.
No publiques precios objetivo, cotizaciones originales, datos de contacto ni estrategia de negociación en el repositorio público.

Primero confirmá qué documentos revisaste, cuál es la matriz vigente y cuál es la próxima acción. Después proponé el plan inmediato.
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
- [ ] Utilizar `v3 aut(26)` en el nuevo chat.

# 15. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-16 | Snapshot inicial, protocolo de actualización y handoff para nuevas sesiones. |
| 0.2.0 | 2026-07-17 | Selección y alcance del Nicho 2, proveedores y prompt de continuidad. |
| 0.3.0 | 2026-07-20 | Primera ronda de proveedores y matriz v3 aut(12). |
| 0.4.0 | 2026-07-23 | Cierre de Demanda y Competencia del Nicho 2, estado actualizado de AT-999 y Shine Solar, matriz v3 aut(26) y nuevo prompt de continuidad. |
