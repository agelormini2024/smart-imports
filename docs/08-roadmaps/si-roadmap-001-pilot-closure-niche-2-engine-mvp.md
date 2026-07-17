---
id: si-roadmap-001
title: Pilot Closure, Niche 2 and Intelligence Engine MVP Roadmap
description: Plan coordinado para cerrar Energía Solar Portátil, ejecutar Viaje organizado como segundo nicho y construir el primer MVP del Intelligence Engine.
version: 0.3.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-07-17
tags:
  - roadmap
  - portable-solar-energy
  - travel-organization
  - niche-selection
  - intelligence-engine
  - matrix-validator
  - mvp
related:
  - si-agent-001
  - si-research-001
  - si-research-002
  - si-roadmap-002
  - si-decision-005
  - si-decision-006
  - si-decision-007
audience:
  - founder
  - partner
  - developer
phase: foundation
---

# SI-ROADMAP-001 — Cierre del piloto, Nicho 2 e Intelligence Engine MVP

> Cada nuevo nicho debe producir dos resultados: conocimiento comercial y una pieza reutilizable del sistema.

---

## 1. Propósito

Este roadmap coordina tres líneas de trabajo paralelas:

```text
Línea A — Cerrar el piloto Energía Solar Portátil
Línea B — Ejecutar Viaje organizado y equipaje funcional como Nicho 2
Línea C — Construir el primer MVP del Smart Imports Intelligence Engine
```

El objetivo es avanzar sin dispersión, validar que la metodología sea reutilizable y comenzar la automatización a partir de problemas reales observados durante la investigación.

Este documento describe el **plan completo del ciclo**, sus etapas, entregables, métricas y secuencia temporal.

El estado operativo cambiante, los bloqueos, las respuestas pendientes y la próxima acción inmediata se mantienen en:

- [SI-ROADMAP-002 — Project Status and Handoff](./si-roadmap-002-project-status-and-handoff.md)

---

## 2. Separación de responsabilidades documentales

### SI-ROADMAP-001

Documento relativamente estable que define:

- Objetivos de las tres líneas.
- Método de ejecución.
- Alcance.
- Entregables.
- Plan temporal.
- Métricas.
- Criterios de éxito.
- Avance contra el plan original.

### SI-ROADMAP-002

Documento dinámico que registra:

- Estado actual.
- Trabajo completado.
- Trabajo en curso.
- Bloqueos.
- Proveedores y respuestas pendientes.
- Próxima acción.
- Handoff para continuar en otro chat o sesión.

### Documentos de Research

Definen el alcance y los resultados específicos de cada investigación:

- [SI-RESEARCH-001 — Niche 2 Selection](../06-research/si-research-001-niche-2-selection.md)
- [SI-RESEARCH-002 — Travel Organization Scope](../06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md)

---

## 3. Reglas operativas

1. No mantener más de dos nichos activos simultáneamente.
2. No automatizar procesos que todavía no hayan sido comprendidos manualmente.
3. No avanzar a RFQ del Nicho 2 antes de completar el screening inicial y definir su alcance.
4. No iniciar compras o muestras sin precio, documentación y decisión humana.
5. Mantener aprobación humana para negociaciones, muestras, compras y pagos.
6. No forzar una conclusión positiva del piloto solar.
7. Registrar toda decisión relevante en el Decision Log.
8. Actualizar el documento de estado después de cada hito significativo.
9. La matriz XLSX más reciente es la fuente operativa de verdad.
10. GitHub es la fuente documental de verdad.
11. Cada conclusión debe mantener trazabilidad hacia evidencias y fuentes.
12. Toda automatización nueva debe resolver un problema observado en el proceso real.

---

# 4. Línea A — Cierre de Energía Solar Portátil

## 4.1 Objetivo

Cerrar los criterios pendientes y producir una decisión fundamentada sobre el nicho, sus subcategorías, productos y proveedores.

## 4.2 Estado

**En curso / esperando y procesando respuestas de proveedores.**

## 4.3 Criterios pendientes

- Margen Potencial.
- Facilidad de Importación.

Los demás criterios ya cuentan con evaluación preliminar o revisada.

## 4.4 Proceso por respuesta de proveedor

```text
Proveedor responde
  ↓
Extracción de datos técnicos y comerciales
  ↓
Validación
  ↓
Detección de faltantes y contradicciones
  ↓
Comparación contra requisitos excluyentes
  ↓
Comparación FOB vs FOB objetivo
  ↓
Repregunta o contraoferta
  ↓
Actualización de matriz y evidencias
  ↓
Recalcular margen, puntaje y confianza
  ↓
Recomendación de siguiente acción
```

## 4.5 Datos necesarios para Margen Potencial

- FOB por cantidad.
- EXW.
- MOQ.
- Packing.
- Unidades por caja.
- Dimensiones de caja.
- Peso neto y bruto.
- CBM.
- Lead time.
- Precio de venta posible.
- Costos de canal.
- Costos comerciales.
- Costos de importación.
- Costo importado estimado.
- Margen unitario.
- Margen porcentual.
- ROI.
- FOB máximo aceptable.
- Reducción requerida respecto del FOB ofrecido.

## 4.6 Datos necesarios para Facilidad de Importación

- Composición.
- Tipo de batería.
- Capacidad, voltaje y Wh.
- MSDS.
- UN38.3.
- HS Code.
- Certificaciones disponibles.
- Tipo de cargador y enchufe.
- Restricciones logísticas.
- Peso y volumen.
- Fragilidad.
- Complejidad de inspección.
- Posibles requisitos regulatorios o aduaneros.
- Riesgo de posventa.

## 4.7 Requisitos excluyentes ya identificados

- No avanzar con baterías de plomo-ácido para los productos evaluados.
- Exigir confirmación de batería de litio cuando corresponda.
- Exigir MSDS y UN38.3 para productos con batería de litio.
- No aceptar capacidades, autonomías o potencias como confirmadas sin documentación.
- No cerrar margen definitivo usando únicamente precios públicos de Alibaba.
- No avanzar a muestra sin conocer packing, CBM y costo logístico preliminar.

## 4.8 Resultados posibles

Cada producto y subcategoría deberá terminar en una de estas acciones:

- Avanzar a muestra.
- Continuar negociando.
- Mantener en observación.
- Descartar producto.
- Descartar proveedor.
- Descartar subcategoría.
- Reformular el nicho.
- Descartar el nicho.

## 4.9 Entregables

- Scoring definitivo del nicho.
- Ranking de subcategorías.
- Ranking de productos.
- Ranking de proveedores.
- Margen recalculado con cotizaciones reales.
- Evaluación de Facilidad de Importación.
- Conclusión del piloto.
- Retrospectiva metodológica.
- Decisión de siguiente acción.
- Actualización del backlog del Intelligence Engine.

---

# 5. Línea B — Ejecución del Nicho 2

## 5.1 Objetivo

Aplicar por segunda vez el método completo en un nicho diferente y medir:

- Repetibilidad.
- Tiempo.
- Errores.
- Calidad de decisión.
- Información faltante.
- Automatizaciones de mayor impacto.

## 5.2 Perfil utilizado para seleccionar el Nicho 2

El candidato preferido debía cumplir, en lo posible, con estas características:

- Sin batería o con menor complejidad técnica.
- Peso y volumen moderados.
- Ticket medio.
- Familia de productos relacionada.
- Potencial de marca propia.
- Demanda observable.
- Diferenciación mediante información, diseño, servicio o software.
- Contraste suficiente con Energía Solar Portátil.

## 5.3 Proceso de selección aplicado

### Etapa 1 — Lista larga

- [x] Generar entre 8 y 12 candidatos.
- [x] Exigir que cada candidato represente una familia de productos.
- [x] Evitar productos individuales presentados artificialmente como nichos.

### Etapa 2 — Filtros excluyentes

- [x] Regulación sanitaria o médica compleja.
- [x] Alimentos, suplementos o cosméticos.
- [x] Riesgo alto de responsabilidad.
- [x] Dependencia de marcas o falsificaciones.
- [x] Volumen logístico desproporcionado.
- [x] MOQ incompatible con el capital.
- [x] Posventa técnica excesiva.
- [x] Imposibilidad de construir familia y marca.

### Etapa 3 — Normalización

- [x] Detectar candidatos duplicados.
- [x] Absorber subcategorías dentro de un nicho superior.
- [x] Reducir la lista a seis candidatos comparables.

### Etapa 4 — Screening rápido

Criterios utilizados:

| Criterio | Peso | Pregunta principal |
|---|---:|---|
| Demanda observable | 25% | ¿Existe interés comercial verificable? |
| Competencia favorable | 20% | ¿La categoría permite una entrada razonable? |
| Facilidad de importación | 20% | ¿Tiene barreras manejables para el proyecto? |
| Potencial de marca | 20% | ¿Permite construir una propuesta coherente? |
| Margen preliminar | 15% | ¿La estructura económica parece viable? |

- [x] Evaluar seis candidatos.
- [x] Seleccionar tres finalistas.

### Etapa 5 — Validación profunda

- [x] Validar Jardinería urbana y balcones.
- [x] Validar Mascotas en departamentos.
- [x] Validar Viaje organizado y equipaje funcional.
- [x] Comparar demanda, competencia, importación, marca y margen.
- [x] Documentar riesgos y oportunidades.

### Etapa 6 — Decisión

- [x] Seleccionar formalmente Viaje organizado y equipaje funcional.
- [x] Registrar la decisión en SI-DECISION-007.
- [x] Documentar el alcance inicial en SI-RESEARCH-002.

## 5.4 Nicho seleccionado

```text
Viaje organizado y equipaje funcional
```

## 5.5 Alcance inicial resumido

Subcategorías incluidas:

- Sets organizadores estándar.
- Packing cubes de compresión.
- Organizadores tecnológicos.
- Organizadores para calzado.
- Neceseres compartimentados.
- Bolsas para ropa usada.

Exclusiones iniciales:

- Valijas y mochilas completas.
- Candados y elementos de seguridad.
- Balanzas electrónicas.
- Adaptadores eléctricos.
- Productos rígidos o voluminosos.
- Productos cuya única diferenciación sea un estampado.

El alcance detallado se mantiene en:

- [SI-RESEARCH-002 — Travel Organization Scope](../06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md)

## 5.6 Hitos próximos

- [ ] Registrar el nicho en la matriz.
- [ ] Definir y cargar términos de búsqueda.
- [ ] Preparar la primera tanda de PDFs de Mercado Libre.
- [ ] Procesar Demanda por subcategoría.
- [ ] Procesar Competencia por subcategoría.
- [ ] Identificar productos base.
- [ ] Registrar evidencias.
- [ ] Generar evaluaciones preliminares.
- [ ] Hacer screening público de proveedores y margen.
- [ ] Evaluar Facilidad de Importación.
- [ ] Comparar resultados con el piloto solar.
- [ ] Documentar la retrospectiva del segundo ciclo.

## 5.7 Entregables

- Registro del Nicho 2 en la matriz.
- Publicaciones y fuentes externas.
- Productos base deduplicados.
- Evidencias de Demanda.
- Evidencias de Competencia.
- Evaluaciones preliminares.
- Screening de proveedores.
- Screening de Margen Potencial.
- Evaluación preliminar de Facilidad de Importación.
- Comparación Solar vs Viaje.
- Retrospectiva metodológica.
- Requisitos nuevos para el Intelligence Engine.

---

# 6. Línea C — Intelligence Engine MVP

## 6.1 Objetivo

Construir una primera utilidad interna que reduzca errores reales sin intentar desarrollar todavía la plataforma completa.

## 6.2 MVP seleccionado

```text
Matrix Validator
```

## 6.3 Estado

**Pendiente de especificación técnica detallada e implementación.**

## 6.4 Alcance funcional inicial

- Validar hojas requeridas.
- Validar nombres de columnas.
- Validar orden de columnas.
- Detectar IDs primarios duplicados.
- Validar formato de IDs.
- Validar relaciones entre hojas.
- Detectar referencias a productos base inexistentes.
- Detectar evidencias sin fuente.
- Detectar evaluaciones sin soporte.
- Detectar productos base posiblemente duplicados.
- Validar criterios reconocidos.
- Validar valores de puntaje.
- Validar valores de confianza.
- Validar estados.
- Detectar filas obligatorias incompletas.
- Generar errores bloqueantes.
- Generar advertencias.
- Producir un resumen de integridad.

## 6.5 Stack preliminar

```text
TypeScript
Node.js
Zod
ExcelJS
CLI
Vitest o Jest
```

## 6.6 Interfaz inicial

```bash
npm run validate -- ./data/smart-imports.xlsx
```

## 6.7 Ejemplo de salida

```text
Validation result: FAILED

Blocking errors: 2
Warnings: 4

- Duplicate ID EVID-0090 in Evidencias row 97
- Missing Producto Base BASE-PB-006 referenced by COT-0008
- Warning: possible duplicate product bases BASE-VENT-001 and BASE-VENT-004
- Warning: evidence EVID-0102 has no source reference
```

## 6.8 Entregables

- Repositorio o módulo inicial.
- Contrato de entrada y salida.
- Esquemas Zod.
- Catálogo de reglas de validación.
- Implementación CLI.
- Tests automatizados.
- Reporte de validación.
- Ejecución contra archivos reales.
- Registro de falsos positivos.
- Backlog de mejoras.

## 6.9 Módulos posteriores detectados

- Marketplace Evidence Analyzer.
- Niche Candidate Normalizer.
- Claims Validation Gate.
- Product Quality Specification Builder.
- Supplier Response Analyzer.
- Contextual RFQ Generator.
- Margin and FOB Engine.
- Scoring and Next Action Engine.
- Compatibility and Dimension Recommender.
- RAG de proveedores.
- Monitoreo automatizado.

---

# 7. Medición de eficiencia

Durante Viaje organizado se registrarán tiempos aproximados para comparar el segundo ciclo con el piloto solar.

El objetivo no es obtener precisión científica, sino detectar las actividades que más tiempo, errores y retrabajo generan.

## 7.1 Investigación comercial

| Actividad | Piloto solar | Nicho 2 |
|---|---:|---:|
| Procesar una publicación | Pendiente de línea base | Por medir |
| Registrar producto base | Pendiente de línea base | Por medir |
| Crear evidencia | Pendiente de línea base | Por medir |
| Evaluar criterio | Pendiente de línea base | Por medir |
| Preparar RFQ | Pendiente de línea base | Por medir |
| Procesar cotización | Pendiente de línea base | Por medir |

## 7.2 Procesamiento operativo

| Actividad | Piloto solar | Nicho 2 |
|---|---:|---:|
| Detectar duplicaciones | Pendiente de línea base | Por medir |
| Generar XLSX importable | Pendiente de línea base | Por medir |
| Validar importable | Pendiente de línea base | Por medir |
| Corregir errores de esquema | Pendiente de línea base | Por medir |
| Conciliar IDs y relaciones | Pendiente de línea base | Por medir |
| Actualizar documentación | Pendiente de línea base | Por medir |

## 7.3 Métricas cualitativas

También se registrará:

- Cantidad de errores detectados.
- Cantidad de retrabajos.
- Duplicaciones evitadas.
- Datos faltantes frecuentes.
- Evidencias ambiguas.
- Claims no verificables.
- Decisiones que requirieron intervención humana.
- Automatizaciones que habrían generado mayor ahorro.

---

# 8. Roadmap de seis semanas

La planificación original se conserva para mantener trazabilidad entre lo previsto y lo ejecutado.

Las semanas representan bloques de trabajo relativos, no fechas calendario rígidas. Las tareas pueden adelantarse o desplazarse según respuestas de proveedores y disponibilidad de evidencias.

| Semana | Plan original | Estado al 2026-07-17 | Observación |
|---:|---|---|---|
| 1 | Procesar proveedores solares, generar lista larga, confirmar alcance del Engine y especificar reglas del Matrix Validator | **Parcialmente completada** | La selección de candidatos avanzó más rápido; el Matrix Validator sigue pendiente de especificación |
| 2 | Aplicar filtros y screening, elegir finalistas, seleccionar Nicho 2 y crear estructura inicial del validador | **Selección completada** | Viaje organizado fue seleccionado; la estructura técnica del validador todavía no fue creada |
| 3 | Investigar Demanda del Nicho 2, implementar validación de hojas, columnas e IDs y continuar negociación solar | **Próxima** | Requiere la matriz XLSX más reciente y primera tanda formal de publicaciones |
| 4 | Investigar Competencia, implementar relaciones y evidencias y crear tests iniciales | **Pendiente** | Se ejecutará después de cerrar la primera tanda de Demanda |
| 5 | Hacer screening de Margen e Importación, ejecutar el validador contra archivos reales y corregir falsos positivos | **Pendiente** | Depende de proveedores y de la primera versión funcional del validador |
| 6 | Cerrar o encaminar el piloto solar, comparar ambos nichos, documentar retrospectiva y definir Supplier Response Analyzer | **Pendiente** | Cierre del ciclo coordinado |

## 8.1 Detalle del plan original

### Semana 1

- Procesar respuestas de proveedores solares.
- Generar lista larga del Nicho 2.
- Confirmar alcance del Intelligence Engine.
- Especificar reglas del Matrix Validator.

### Semana 2

- Aplicar filtros y screening.
- Elegir tres finalistas.
- Seleccionar Nicho 2.
- Crear estructura inicial del validador.

### Semana 3

- Investigar Demanda del Nicho 2.
- Implementar validación de hojas, columnas e IDs.
- Continuar negociación solar.

### Semana 4

- Investigar Competencia del Nicho 2.
- Implementar validación de relaciones y evidencias.
- Crear tests iniciales.

### Semana 5

- Hacer screening de Margen e Importación del Nicho 2.
- Ejecutar el validador contra archivos reales.
- Corregir falsos positivos.

### Semana 6

- Cerrar o encaminar el piloto solar.
- Comparar ambos nichos.
- Documentar retrospectiva.
- Definir Supplier Response Analyzer.

---

# 9. Tablero actual resumido

El detalle operativo se mantiene en SI-ROADMAP-002.

## En curso

- Espera y seguimiento de RFQ solares.
- Registro operativo de Viaje organizado.
- Preparación de la primera tanda formal de Demanda.
- Especificación inicial del Matrix Validator.

## Próximo

- Obtener la matriz XLSX más reciente.
- Registrar Viaje organizado.
- Procesar publicaciones por subcategoría.
- Crear productos base y evidencias.
- Medir tiempos.
- Implementar validación de hojas, columnas e IDs.

## Bloqueado o esperando

- Margen solar definitivo.
- Facilidad de Importación solar definitiva.
- Ranking final de proveedores solares.

Dependencia principal: respuestas, certificados, packing y condiciones comerciales de proveedores.

## Backlog

- Supplier Response Analyzer.
- Contextual RFQ Generator.
- Margin and FOB Engine.
- Scoring and Next Action Engine.
- RAG de proveedores.
- Monitoreo automatizado.

---

# 10. Criterios de éxito del ciclo

El ciclo se considerará exitoso cuando:

1. Energía Solar Portátil tenga una decisión clara o un camino de cierre.
2. Viaje organizado complete Demanda y Competencia formal.
3. Se obtenga al menos una línea base de tiempos y errores.
4. El Matrix Validator funcione sobre archivos reales.
5. Exista un backlog del Intelligence Engine basado en problemas observados.
6. La metodología pueda compararse entre dos nichos diferentes.
7. Las decisiones mantengan trazabilidad hacia evidencias.
8. Se reduzca el retrabajo respecto del piloto inicial.
9. El próximo módulo del Engine se elija a partir de impacto observado.

---

# 11. Próxima acción principal

```text
1. Obtener la matriz XLSX más reciente.
2. Registrar Viaje organizado como Nicho 2.
3. Definir la estructura de medición de tiempos.
4. Recolectar la primera tanda de publicaciones de Mercado Libre.
5. Procesar Demanda por subcategoría.
6. Continuar procesando respuestas solares cuando lleguen.
7. Especificar el contrato de entrada y salida del Matrix Validator.
```

---

# 12. Documentos relacionados

- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-RESEARCH-001 — Niche 2 Selection](../06-research/si-research-001-niche-2-selection.md)
- [SI-RESEARCH-002 — Travel Organization Scope](../06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md)
- [SI-ROADMAP-002 — Project Status and Handoff](./si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-005 — Portable Solar Pilot Scope](../09-decision-log/si-decision-005-portable-solar-pilot-scope.md)
- [SI-DECISION-006 — Build the Intelligence Engine Incrementally](../09-decision-log/si-decision-006-build-intelligence-engine-incrementally.md)
- [SI-DECISION-007 — Select Travel Organization as Niche 2](../09-decision-log/si-decision-007-select-travel-organization-as-niche-2.md)

---

# 13. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-16 | Roadmap inicial de tres líneas y seis semanas. |
| 0.2.0 | 2026-07-17 | Actualización del estado después de seleccionar Viaje organizado como Nicho 2. La simplificación eliminó contenido estructural que debía conservarse. |
| 0.3.0 | 2026-07-17 | Fusión de la estructura completa de v0.1.0 con los avances de v0.2.0. Se restauraron planificación, entregables, métricas, alcance del Matrix Validator y separación de responsabilidades documentales. |
