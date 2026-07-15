---
id: si-bim-proc-002
title: Supplier RFQ and Margin Screening Procedure
description: Procedimiento operativo provisorio para solicitar cotizaciones a proveedores, calcular FOB objetivo, negociar condiciones y alimentar el criterio Margen Potencial.
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-15
updated: 2026-07-15
tags:
  - business-intelligence
  - supplier
  - rfq
  - margin
  - negotiation
  - alibaba
related:
  - si-bim-003
  - si-bim-proc-001
  - si-bim-000
phase: business-intelligence
---

# SI-BIM-PROC-002 — Supplier RFQ and Margin Screening Procedure

> **Negociar sin FOB objetivo es pedir descuento a ciegas.**

---

## 1. Propósito

Este procedimiento define cómo Smart Imports debe pasar de referencias públicas de proveedores a una evaluación preliminar de margen más útil.

El proceso cubre:

- Selección de productos base para cotizar.
- Búsqueda de referencias públicas en Alibaba u otras plataformas.
- Solicitud de RFQ formal.
- Registro de cotizaciones.
- Cálculo preliminar de margen.
- Cálculo de FOB objetivo.
- Negociación inicial.
- Conversión de resultados en evidencias para el criterio Margen Potencial.

---

## 2. Alcance

Aplica a la etapa inicial de investigación de nichos, antes de una compra formal.

No reemplaza:

- Cotización logística final.
- Despacho aduanero.
- Cálculo impositivo definitivo.
- Validación legal de importación.
- Auditoría de fábrica.
- Compra de muestra.
- Orden de compra formal.

---

## 3. Flujo general

```text
Productos Base priorizados
        ↓
Referencias públicas de proveedores
        ↓
Cotizaciones Proveedores
        ↓
Simulación Margen
        ↓
FOB Objetivo
        ↓
RFQ / Negociación
        ↓
FOB Negociado
        ↓
Evidencias
        ↓
Evaluaciones
```

---

## 4. Regla de selección de productos

No se deben cotizar todos los productos detectados.

Primero se eligen productos base representativos, por ejemplo:

- Producto con mayor demanda.
- Producto con mejor señal competitiva.
- Producto con posible margen atractivo.
- Producto con baja complejidad logística.
- Producto que pueda diferenciarse por marca o calidad.

Para el piloto Energía Solar Portátil se priorizaron inicialmente:

- Kit solar tipo AT-999 / variantes DAT.
- Ventilador solar multifunción 8 pulgadas.
- Ventilador solar multifunción 12 pulgadas.
- Power bank solar 30.000 / 50.000 mAh.
- Panel solar plegable 30W / 40W.

---

## 5. RFQ estándar

Mensaje base para proveedores:

```text
Hello, my name is Alejandro. I am evaluating products for import to Argentina.

I am interested in this product and would like to request a formal quotation.

Please send me:

1. Best FOB price for 300, 500, 1000 and 3000 units
2. EXW price
3. MOQ
4. Product datasheet
5. Packing details: units per carton, carton size, gross weight and net weight
6. CBM per carton
7. Lead time
8. Available certifications
9. HS Code
10. Sample cost and shipping cost to Argentina
11. Custom logo and custom packaging options

This is for a first evaluation. If the numbers are competitive, we may request samples and continue with a formal order.

Thank you.
```

---

## 6. Requisitos para productos con batería

Todo producto con batería debe requerir información adicional.

Mensaje adicional:

```text
Also, please confirm:

1. Battery type
2. Real battery capacity
3. Battery voltage
4. Wh rating
5. MSDS certificate
6. UN38.3 certificate
7. Battery test report, if available
```

---

## 7. Regla de batería para el piloto

Para el caso piloto Energía Solar Portátil se establece la siguiente regla operativa:

```text
Battery type: lithium only.
Lead-acid battery is not acceptable for our import evaluation.
```

Motivo:

- Restricciones y complejidades de importación.
- Riesgo logístico.
- Peso adicional.
- Menor atractivo técnico frente a alternativas de litio.
- Mayor dificultad para construir una propuesta moderna y confiable.

Si una ficha de proveedor muestra información contradictoria, debe repreguntarse antes de avanzar.

Ejemplo de pregunta:

```text
Please confirm clearly that this model uses lithium battery, not lead-acid battery.
Lead-acid battery is not acceptable for our import evaluation in Argentina.
```

---

## 8. Datos mínimos para registrar una cotización

Una cotización útil debe incluir al menos:

- Proveedor.
- Producto o modelo.
- ID Producto Base relacionado.
- Incoterm.
- Precio FOB por tramos.
- Precio EXW si está disponible.
- MOQ.
- Packing details.
- CBM.
- Peso bruto.
- Peso neto.
- Certificaciones.
- HS Code.
- Lead time.
- Costo de muestra.
- Costo estimado de envío de muestra.
- Condiciones de logo y packaging.

Si faltan datos críticos, la cotización debe quedar como incompleta.

---

## 9. Interpretación de respuestas incompletas

Muchos proveedores responden primero con datos parciales.

Si la respuesta sólo incluye precio y MOQ, se debe repreguntar.

Mensaje de seguimiento:

```text
Thank you for your reply.

To properly evaluate the product, could you please send the full quotation details?

I especially need:

1. FOB price for each model separately
2. FOB price for 300, 500, 1000 and 3000 units
3. EXW price
4. Units per carton
5. Carton size
6. Gross weight and net weight
7. CBM per carton
8. Available certifications
9. HS Code
10. Sample cost and shipping cost to Argentina

Thank you.
```

---

## 10. FOB objetivo

Antes de negociar precio, se debe calcular un FOB objetivo por producto base.

El FOB objetivo responde:

> ¿Qué FOB máximo permite que este producto tenga margen razonable?

Fórmula conceptual:

```text
Precio venta defendible
- costos de canal
- costos comerciales
- margen mínimo deseado
- costos de importación estimados
= FOB objetivo aproximado
```

El FOB objetivo no es un número exacto. Es una guía para negociar.

---

## 11. Cómo negociar

La negociación debe comparar:

```text
FOB público
FOB objetivo
FOB ofrecido por RFQ
FOB negociado posible
MOQ requerido
```

Si el proveedor está cerca del objetivo, se negocia.

Si está lejos, se puede pedir:

- Mejor precio por mayor volumen.
- Versión estándar sin logo.
- Packaging estándar.
- Modelo alternativo similar.
- Menor cantidad de accesorios.
- Configuración técnica distinta.

No se debe aceptar una reducción de costo que destruya calidad, seguridad o cumplimiento documental.

---

## 12. Respuesta cuando el precio es alto

Ejemplo:

```text
Thank you for your quotation.

For the Argentina market, the current FOB price is too high for us.

For 1000 to 3000 units, we need to be closer to USD X FOB, depending on the final specifications, battery type and packing.

Can you offer a better price or recommend a similar model that can meet this target?
```

---

## 13. Criterios de decisión después de RFQ

| Situación | Próxima acción |
|---|---|
| FOB negociado menor o cercano al FOB objetivo | Pedir muestra / avanzar validación técnica. |
| FOB público alto pero proveedor dispuesto a negociar | Continuar negociación. |
| FOB muy lejos del objetivo | Pedir modelo alternativo o pausar. |
| Producto con batería no aceptable | Descartar configuración o pedir versión litio. |
| Falta MSDS / UN38.3 en productos con batería | No avanzar hasta recibir documentación. |
| MOQ demasiado alto | Negociar primera orden menor o buscar otro proveedor. |
| Datos logísticos incompletos | Mantener cotización como incompleta. |

---

## 14. Evidencias para Margen Potencial

Cada cotización o simulación relevante debe generar evidencia.

Ejemplos:

```text
Criterio: Margen Potencial
Fuente: Cotización Proveedor
Fuente ID: COT-0001
Resumen: Proveedor cotiza AT-999 a USD 10.21 FOB para 1000 unidades, pero el producto usa batería de plomo-ácido y queda fuera del requisito operativo.
```

```text
Criterio: Margen Potencial
Fuente: Simulación Margen
Fuente ID: MARG-0002
Resumen: Panel plegable 30W/40W muestra margen preliminar atractivo con FOB público de USD 21, pendiente de RFQ formal.
```

---

## 15. Aprendizajes iniciales del piloto

Durante el piloto Energía Solar Portátil se detectaron aprendizajes importantes:

- Los precios públicos de Alibaba pueden ser muy distintos al FOB negociable.
- Los productos con batería requieren validación documental antes de evaluar margen final.
- Algunos productos populares localmente pueden usar tecnologías no aceptables para importación, como baterías de plomo-ácido.
- El proveedor puede tener variantes más adecuadas que el producto inicialmente investigado.
- El cálculo de FOB objetivo ayuda a negociar sin improvisar.
- La comparación entre productos base es más útil que negociar productos aislados.

---

## 16. Futuro flujo con n8n

Este procedimiento podrá automatizarse parcialmente:

```text
PDF / respuesta proveedor / Alibaba
        ↓
Extracción de datos
        ↓
Cotizaciones Proveedores
        ↓
Simulación Margen
        ↓
FOB Objetivo
        ↓
Generación de repregunta o negociación sugerida
        ↓
Evidencias
        ↓
Evaluaciones
```

---

## 17. Documentos relacionados

- [SI-BIM-003 — Margin Potential Evaluation](../criteria/si-bim-003-margin-potential-evaluation.md)
- [SI-BIM-PROC-001 — Marketplace Evidence Processing](./si-bim-proc-001-marketplace-evidence-processing.md)
- [SI-BIM-000 — Confidence in Evaluations](../criteria/si-bim-000-confidence-in-evaluations.md)

---

## 18. Preguntas abiertas

- ¿Qué margen mínimo objetivo debe exigir Smart Imports para cada tipo de producto?
- ¿Qué factor de importación usar en screening preliminar por categoría?
- ¿Cuándo pedir muestra?
- ¿Cuándo descartar un proveedor por falta de respuesta?
- ¿Cómo registrar versiones de un mismo producto con batería distinta?
- ¿Cómo integrar costos reales de despachante, flete, seguro e impuestos?

---

## 19. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-15 | Versión inicial del procedimiento RFQ y screening de margen basada en el piloto Energía Solar Portátil. |
