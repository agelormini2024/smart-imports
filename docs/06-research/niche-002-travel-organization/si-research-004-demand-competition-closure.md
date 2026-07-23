---
id: si-research-004
title: Niche 2 Demand and Competition Closure
description: Cierra la primera ejecución de Demanda y Competencia ML del nicho Viaje organizado y equipaje funcional y registra sus principales hallazgos.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-23
updated: 2026-07-23
tags:
  - research
  - niche-002
  - travel-organization
  - demand
  - competition
  - closure
related:
  - si-research-001
  - si-research-002
  - si-roadmap-001
  - si-roadmap-002
  - si-decision-007
  - si-decision-008
phase: business-intelligence
---

# SI-RESEARCH-004 — Cierre de Demanda y Competencia del Nicho 2

> El objetivo de esta etapa fue comprender el mercado antes de avanzar hacia proveedores, margen y decisión de importación.

## 1. Propósito

Registrar el cierre de la primera investigación operativa de **Demanda** y **Competencia en Mercado Libre** para:

```text
Viaje organizado y equipaje funcional
```

Este documento no asigna todavía el score definitivo del nicho. Consolida lo investigado, documenta el alcance realmente ejecutado y define la siguiente etapa.

## 2. Fuente operativa

La matriz utilizada al cierre fue:

```text
Smart Imports - matriz de oportunidades - v3 aut(25).xlsx
```

Luego del cierre de sesión debe utilizarse la versión que incorpore `TIME-0021` y `TIME-0022`.

La matriz conserva el detalle de publicaciones, productos base, evidencias, competencia y tiempos. Este documento registra sólo el resultado consolidado.

## 3. Subcategorías procesadas

| Tanda | Subcategoría | Demanda | Competencia ML | Estado |
|---|---|---|---|---|
| `TANDA-VIAJE-001` | Sets organizadores estándar para valija | Procesada | Procesada | Cerrada |
| `TANDA-VIAJE-002A` | Packing cubes de compresión | Procesada | Procesada | Cerrada |
| `TANDA-VIAJE-002B` | Bolsas de compresión al vacío con bomba | Procesada | Procesada | Cerrada |
| `TANDA-VIAJE-003` | Organizadores tecnológicos para viaje | Procesada | Procesada | Cerrada |
| `TANDA-VIAJE-004A` | Neceseres compartimentados para viaje | Procesada | Procesada | Cerrada |
| `TANDA-VIAJE-004B` | Kits de envases recargables para viaje | Procesada | Procesada | Cerrada |
| `TANDA-VIAJE-005` | Organizadores para calzado | Procesada | Procesada | Cerrada |

Las tandas `002B` y `004B` surgieron como extensiones del alcance inicial durante la investigación. Se mantuvieron porque presentaron señales comerciales suficientes para justificar su procesamiento separado.

## 4. Subcategoría cerrada sin procesamiento formal

### `TANDA-VIAJE-006` — Bolsas para ropa usada o húmeda

Se realizó un screening manual de 20 minutos.

Resultado:

- No se encontró una oferta relevante y suficientemente diferenciada.
- Los resultados útiles fueron escasos y se mezclaban con productos domésticos, bolsas genéricas o categorías ya evaluadas.
- No se generó una tanda formal de PDFs, publicaciones, productos base ni evidencias.
- La ausencia de esta subcategoría no cambia materialmente la lectura del nicho.

Decisión:

> Cerrar la subcategoría sin procesamiento formal y conservarla únicamente como posible SKU complementario futuro.

La decisión no implica que el producto sea inviable para siempre. Implica que no merece más tiempo en esta etapa del método.

## 5. Hallazgos consolidados

### 5.1 Demanda

La demanda existe y es visible en varias subcategorías, especialmente cuando concurren:

- Precio accesible.
- Disponibilidad inmediata.
- Entrega rápida o Full.
- Vendedores consolidados.
- Utilidad simple de comprender.

La demanda premium fue débil o no validada en las subcategorías donde se buscó explícitamente.

### 5.2 Competencia

La competencia es alta o muy alta en la mayor parte del nicho.

Patrones repetidos:

- Pocos productos base reales.
- Muchos vendedores sobre bases equivalentes.
- Variantes por color, cantidad, packaging o financiación.
- Baja barrera técnica.
- Alta comparabilidad.
- Presión de precio.
- Actores locales con reputación, stock y logística consolidados.

### 5.3 Comportamiento commodity

El nicho presenta un nivel commodity elevado.

La mera colocación de un logo no crea una ventaja defendible. Una entrada viable exigiría al menos una combinación de:

- Mejor calidad verificable.
- Configuración de kit más útil.
- Packaging coherente.
- Garantía clara.
- Contenido educativo.
- Mejor experiencia de compra.
- Cross-selling y armado de sistema de productos.

### 5.4 Diferenciación funcional

Las mejores oportunidades de diferenciación observadas no provienen de la estética, sino de resolver fallas reales:

- Cierres y costuras.
- Resistencia de materiales.
- Medidas y capacidades reales.
- Impermeabilidad o control de pérdidas.
- Divisiones internas.
- Válvulas y tapas confiables.
- Compatibilidad con equipaje de mano.
- Instrucciones y rotulado.

### 5.5 Subcategorías con mejor interés relativo

Sin asignar todavía una decisión final, las subcategorías que justifican una revisión de **Margen Potencial** son aquellas que combinan ticket, demanda y posibilidad de mejorar el producto.

Candidatos a comparar en la consolidación:

1. Kits de envases recargables para viaje.
2. Bolsas de compresión al vacío con bomba.
3. Algún organizador o kit textil sólo si la estructura de costos permite evitar competencia directa por precio.

La shortlist definitiva debe surgir de la evaluación formal del nicho, no de esta lista preliminar.

## 6. Tiempos y aprendizaje operativo

Al cierre se registraron **291 minutos activos conocidos**, equivalentes a **4 horas y 51 minutos**, más `TIME-0012`, cuyo tiempo no fue medido.

El proceso manual permitió identificar con claridad tareas automatizables:

- Captura estructurada de publicaciones.
- Detección de variantes y duplicados.
- Normalización de vendedores y marcas.
- Agrupación por producto base.
- Validación de relaciones entre hojas.
- Control de IDs.
- Generación de importables.
- Detección de publicaciones con baja relevancia.

Este aprendizaje alimenta directamente el diseño del `Matrix Validator` y módulos posteriores del Intelligence Engine.

## 7. Estado al cierre

```text
Demanda por subcategoría: procesada
Competencia ML por subcategoría: procesada
TANDA-VIAJE-006: cerrada sin procesamiento formal
Evaluación consolidada del nicho: pendiente
Margen Potencial: pendiente
Facilidad de Importación: pendiente
Matrix Validator: pendiente de especificación e implementación
```

## 8. Próximas acciones

1. Crear la evaluación consolidada de **Demanda** del Nicho 2.
2. Crear la evaluación consolidada de **Competencia** del Nicho 2.
3. Actualizar `Nichos` con valor, confianza y soportes.
4. Definir una shortlist de subcategorías para Margen Potencial.
5. Decidir si se inicia RFQ o se realiza primero un screening de costos públicos.
6. Iniciar la especificación e implementación mínima del `Matrix Validator`.
7. Actualizar `SI-ROADMAP-002` después de cada hito.

## 9. Documentos relacionados

- [SI-RESEARCH-001 — Niche 2 Selection](../si-research-001-niche-2-selection.md)
- [SI-RESEARCH-002 — Travel Organization Scope](./si-research-002-travel-organization-scope.md)
- [SI-ROADMAP-001 — Pilot Closure, Niche 2 and Intelligence Engine MVP](../../08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-008 — Close Niche 2 Demand and Competition](../../09-decision-log/si-decision-008-close-niche-2-demand-and-competition.md)

## 10. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-23 | Cierre inicial de Demanda y Competencia ML del Nicho 2. |
