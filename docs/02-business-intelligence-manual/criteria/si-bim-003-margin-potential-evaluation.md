---
id: si-bim-003
title: Margin Potential Evaluation
description: Protocolo metodológico para evaluar el criterio Margen Potencial dentro de la Matriz de Oportunidades de Smart Imports.
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-15
updated: 2026-07-15
tags:
  - business-intelligence
  - margin
  - profitability
  - criteria
  - supplier-rfq
  - scoring
related:
  - si-bim-000
  - si-bim-001
  - si-bim-002
  - si-bim-proc-002
phase: business-intelligence
---

# SI-BIM-003 — Margin Potential Evaluation

> **Un producto puede venderse mucho y aun así no ser negocio.**

---

## 1. Propósito

Este documento define cómo Smart Imports evalúa el criterio **Margen Potencial** dentro de la Matriz de Oportunidades.

El objetivo es determinar si un nicho o subcategoría puede generar margen suficiente después de considerar precio de venta, costo de producto, importación, logística, costos comerciales, riesgos técnicos y presión competitiva.

Este criterio no busca confirmar rentabilidad definitiva en la primera etapa. Busca identificar si vale la pena continuar investigando, negociar proveedores, pedir muestras o descartar productos antes de comprometer capital.

---

## 2. Definición

**Margen Potencial** mide la posibilidad de obtener una diferencia saludable entre el precio neto de venta y el costo total estimado de llevar un producto al mercado.

En términos prácticos, responde:

> ¿Este nicho puede dejar plata después de comprar, importar, vender, entregar, financiar, garantizar y absorber errores razonables?

---

## 3. Qué mide

El criterio Margen Potencial mide señales como:

- Diferencia entre precio local de venta y costo FOB / EXW.
- Precio neto estimado después de comisiones y costos de canal.
- Costos comerciales estimados.
- Costo importado preliminar.
- Margen unitario estimado.
- Margen porcentual.
- ROI sobre costo.
- Necesidad de negociación FOB.
- Viabilidad del MOQ.
- Sensibilidad a flete, volumen, CBM y peso.
- Riesgo de garantía, devoluciones y reclamos.
- Presión competitiva sobre precio.

---

## 4. Qué no mide

Margen Potencial no mide:

- Demanda.
- Competencia en sí misma.
- Facilidad legal o logística de importación.
- Potencial de marca.
- Venta impulsiva.
- Recompra.
- Afinidad personal.
- Calidad final del proveedor.
- Rentabilidad final confirmada.

Un producto puede tener margen potencial alto y aun así ser inviable por restricciones de importación, baja calidad, MOQ excesivo o riesgo técnico.

---

## 5. Principios metodológicos

### 5.1 Precio público Alibaba no es precio final

El precio público de Alibaba debe tratarse como referencia inicial, no como precio final de compra.

```text
Precio público Alibaba ≠ FOB negociado final
```

Un margen preliminar débil con precio público no implica descarte automático.

Un margen preliminar fuerte con precio público tampoco implica compra.

---

### 5.2 Margen se valida en etapas

El criterio debe evaluarse por etapas:

```text
Precio público / referencia inicial
  ↓
Screening preliminar
  ↓
FOB objetivo
  ↓
RFQ formal
  ↓
FOB negociado
  ↓
Simulación importadora más completa
  ↓
Evaluación final de Margen Potencial
```

---

### 5.3 El FOB objetivo guía la negociación

Antes de negociar, Smart Imports debe calcular el **FOB objetivo**.

El FOB objetivo responde:

> ¿Cuánto puedo pagar como máximo en origen para que este producto sea viable en Argentina?

Sin FOB objetivo, la negociación queda sin referencia.

---

### 5.4 No todos los productos del nicho tendrán margen

El criterio puede cerrar favorablemente para el nicho aunque algunos productos base queden descartados.

Ejemplo:

```text
Kits solares: margen ajustado.
Ventiladores solares: margen posible.
Power banks: margen posible pero alto riesgo técnico.
Paneles plegables: margen atractivo si se negocia bien.
```

La evaluación final debe considerar el conjunto del nicho y sus subcategorías, no un único producto aislado.

---

## 6. Fuentes recomendadas

| Fuente | Utilidad |
|---|---|
| Publicaciones ML | Estimar precio local defendible. |
| Fuentes externas locales | Comparar precios fuera de marketplace. |
| Alibaba / proveedores | Obtener FOB/EXW público y referencias de productos. |
| RFQ formal | Obtener precio real por volumen y condiciones. |
| Packing details | Estimar CBM, peso y costo logístico. |
| Certificaciones | Identificar costos y riesgos adicionales. |
| Cotizaciones logísticas | Validar costo importado estimado. |
| Histórico de negociación | Comparar precio público vs precio negociado. |

---

## 7. Hojas operativas recomendadas

### 7.1 `Cotizaciones Proveedores`

Registra referencias de proveedor, precios públicos y cotizaciones formales.

Debe incluir al menos:

- Cotización ID.
- Fecha.
- Nicho.
- Subcategoría.
- ID Producto Base.
- Producto Referencia.
- Proveedor.
- Plataforma.
- País.
- Incoterm.
- MOQ.
- Precio Unitario USD.
- Cantidad cotizada.
- Packing details.
- Certificaciones.
- Link / archivo.
- Estado.

---

### 7.2 `Simulación Margen`

Convierte una cotización en una lectura económica preliminar.

Debe incluir al menos:

- Margen ID.
- Producto Base.
- Cotización ID.
- Precio Venta USD.
- Precio Neto Estimado USD.
- Costo FOB USD.
- Factor Importación Estimado.
- Costo Importado Estimado USD.
- Costos Comerciales USD.
- Margen Unitario USD.
- Margen Porcentaje.
- ROI sobre Costo.
- Riesgo Margen.
- Puntaje Parcial.
- Confianza.
- Estado.

---

### 7.3 `FOB Objetivo`

Sirve para preparar negociación.

Debe incluir al menos:

- Producto Base.
- Precio venta USD.
- Costo importado estimado actual.
- Margen actual.
- FOB público.
- FOB objetivo.
- Diferencia requerida.
- Prioridad negociación.

---

### 7.4 `Evidencias`

Toda simulación relevante debe convertirse en evidencia para el criterio Margen Potencial.

Ejemplo:

```text
Criterio: Margen Potencial
Fuente: Simulación Margen
Fuente ID: MARG-0001
Resumen: Producto con margen preliminar ajustado; requiere negociación FOB.
```

---

## 8. Escala de Valor

La escala de Margen Potencial va de 1 a 5. En todos los casos, un valor más alto significa mayor atractivo para Smart Imports.

| Valor | Interpretación | Descripción |
|---:|---|---|
| 1 | Inviable | Margen negativo o extremadamente débil incluso con supuestos razonables. |
| 2 | Débil | Margen bajo; sólo viable con volumen alto, muy buen FOB o estructura eficiente. |
| 3 | Aceptable | Margen posible, pero depende de negociación, costos controlados y buena selección de producto. |
| 4 | Atractivo | Margen saludable en varios productos base o subcategorías, con espacio para absorber costos comerciales. |
| 5 | Muy atractivo | Margen fuerte, defendible y validado con cotizaciones formales y costos importadores razonables. |

---

## 9. Confianza

| Confianza | Condición |
|---|---|
| Baja | Sólo hay precios públicos, supuestos de canal y factores estimados. |
| Media | Hay RFQ formal, FOB por tramos, MOQ y algunos datos de packing. |
| Alta | Hay cotización negociada, packing completo, CBM, peso, HS Code, certificaciones y simulación importadora razonablemente completa. |

---

## 10. Guía práctica de interpretación

### Margen = 1

Usar cuando:

- El producto queda negativo incluso con supuestos optimistas.
- El FOB objetivo es irrealmente bajo.
- El MOQ requerido supera ampliamente la capacidad inicial.
- El riesgo técnico puede destruir el margen.

---

### Margen = 2

Usar cuando:

- El producto podría cerrar sólo con una negociación agresiva.
- El margen depende de volumen alto.
- El costo logístico puede absorber la ganancia.
- El canal de venta deja poco margen neto.

---

### Margen = 3

Usar cuando:

- Hay productos con margen posible, pero todavía no validado.
- El FOB negociado puede cambiar sustancialmente la lectura.
- La categoría requiere seleccionar muy bien proveedor y configuración.
- Faltan costos de importación concretos.

---

### Margen = 4

Usar cuando:

- Varios productos base muestran margen saludable.
- El FOB objetivo parece alcanzable.
- La negociación puede mejorar condiciones sin destruir calidad.
- Hay espacio para comisiones, marketing, garantías y devoluciones.

---

### Margen = 5

Usar cuando:

- El margen se sostiene con cotizaciones formales y costos razonablemente completos.
- El producto conserva margen aun con escenarios conservadores.
- El FOB negociado ya fue confirmado o está muy cerca del objetivo.
- El producto permite construir una oferta defensible.

---

## 11. Estado actual en el piloto Energía Solar Portátil

Durante el piloto Energía Solar Portátil se aplicó una primera evaluación preliminar de Margen Potencial usando:

- Precios locales de Mercado Libre y fuentes externas.
- Referencias públicas de Alibaba.
- Simulación de precio neto.
- Factor estimado de importación.
- Cálculo preliminar de margen.
- Cálculo de FOB objetivo.
- Primeras RFQ con proveedores.

Resultado metodológico actual:

```text
Margen Potencial: En evaluación
Confianza: Baja / Media
```

La evaluación no debe cerrarse hasta recibir cotizaciones reales de proveedores y validar datos mínimos de importación.

---

## 12. Documentos relacionados

- [SI-BIM-000 — Confidence in Evaluations](./si-bim-000-confidence-in-evaluations.md)
- [SI-BIM-001 — Demand Evaluation](./si-bim-001-demand-evaluation.md)
- [SI-BIM-002 — Competition Evaluation](./si-bim-002-competition-evaluation.md)
- [SI-BIM-PROC-002 — Supplier RFQ and Margin Screening](../procedures/si-bim-proc-002-supplier-rfq-and-margin-screening.md)

---

## 13. Preguntas abiertas

- ¿Cuál será el factor de importación estándar por tipo de producto?
- ¿Conviene separar margen por canal: Mercado Libre, e-commerce propio, venta mayorista?
- ¿Qué margen mínimo debe exigir Smart Imports para productos con batería?
- ¿Cómo se modelará el impacto de devoluciones y garantía?
- ¿Cuándo una simulación preliminar pasa de `screening` a `evaluación formal`?

---

## 14. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-15 | Versión inicial del criterio Margen Potencial basada en el piloto Energía Solar Portátil. |
