---
id: si-research-003
title: Supplier Negotiation Round 01 — Portable Solar Energy
description: Resumen público de la primera ronda estructurada de cotizaciones, validación documental, repreguntas y negociación de proveedores del nicho Energía Solar Portátil.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-20
updated: 2026-07-20
tags:
  - research
  - suppliers
  - negotiation
  - portable-solar-energy
  - margin
  - importability
related:
  - si-bim-003
  - si-bim-proc-002
  - si-roadmap-001
  - si-roadmap-002
  - si-decision-005
audience:
  - founder
  - partner
  - analyst
visibility: public-summary
phase: validation
---

# SI-RESEARCH-003 — Primera ronda de negociación con proveedores

> Una respuesta de proveedor no es una conclusión: es nueva evidencia que debe validarse, compararse y convertir en una próxima acción.

---

## 1. Propósito

Consolidar los aprendizajes de la primera ronda estructurada de proveedores del nicho **Energía Solar Portátil**, sin convertir este documento público en una segunda base operativa ni exponer información comercial sensible.

Los precios exactos, FOB objetivo, simulaciones, documentos originales y datos de contacto permanecen en:

- La matriz XLSX privada.
- El archivo privado de proveedores.
- Las cotizaciones y certificados originales.

---

## 2. Alcance de la ronda

Se procesaron respuestas de proveedores correspondientes a:

- Kits solares portátiles.
- Ventiladores solares.
- Power banks solares.
- Paneles solares plegables.

El flujo aplicado fue:

```text
Respuesta
  ↓
Extracción
  ↓
Validación técnica y comercial
  ↓
Detección de faltantes y contradicciones
  ↓
Comparación con requisitos excluyentes
  ↓
Repregunta o negociación
  ↓
Registro en matriz
  ↓
Próxima acción
```

---

## 3. Resultado consolidado por proveedor

| Proveedor / familia | Estado | Hallazgo principal | Próxima acción |
|---|---|---|---|
| DAT / kits solares | En aclaración | La versión original con plomo quedó descartada. El proveedor informó una variante de litio dentro del objetivo comercial preliminar, pero el modelo exacto, Incoterm, MOQ reducido y documentación siguen pendientes. | Confirmar modelo, cantidad mínima real, configuración completa, Incoterm, batería y muestra. |
| Ani Technology / ventiladores | En aclaración | Se recibieron precios y documentos, pero parte de la documentación corresponde a celdas o modelos diferentes de los ventiladores cotizados. | Esperar respuesta sobre orden mixta, precios por cantidades, accesorios, certificados aplicables y muestras. |
| Nulike / power banks | No viable al precio actual | La cotización formal quedó fuera de la estructura de margen objetivo y no aportó evidencia suficiente sobre capacidad real, Wh y correspondencia documental. | Solicitar modelos más simples o de menor capacidad y abrir búsqueda paralela de otro fabricante. |
| Shine Solar / paneles plegables | Prioridad alta | Presentó condiciones flexibles, orden mixta, MOQ bajo, packing utilizable y una estructura preliminar de margen favorable para 15W y 40W. | Validar lógica de precios mixtos, documentos por modelo, muestras, garantía y condiciones EXW/FCA/FOB. |

---

## 4. Hallazgos metodológicos

### 4.1 El MOQ puede ser más importante que una pequeña reducción de FOB

Para una primera importación, una oferta con menor MOQ y orden mixta puede reducir más riesgo que una reducción marginal de precio condicionada a una gran cantidad de un único producto.

### 4.2 El modelo y la documentación deben coincidir

No debe considerarse válida una certificación cuando difieren:

- Modelo.
- Química de batería.
- Capacidad.
- Configuración de celdas.
- Producto terminado frente a batería transportada por separado.

### 4.3 EXW, FCA y FOB deben compararse dentro de la estrategia logística

Cuando exista consolidación de varios proveedores, el precio FOB individual puede no ser la alternativa más eficiente.

El análisis futuro deberá comparar:

```text
EXW fábrica
FCA depósito del consolidador
FOB del proveedor
```

### 4.4 Los claims comerciales requieren una puerta de validación

Ejemplos:

- Capacidad real.
- Autonomía.
- Potencia.
- IP68.
- Waterproof.
- Certificación aplicable.
- Batería de litio específica.

Estos claims deben permanecer como `no confirmados` hasta que exista evidencia aplicable.

---

## 5. Impacto preliminar sobre el nicho

### Kits solares

La variante de litio reabre la posibilidad comercial del producto, pero la oportunidad depende de conseguir una cantidad inicial razonable y documentación coincidente.

### Ventiladores

La familia sigue siendo viable para investigación, aunque todavía no existe una selección de muestra por falta de cotizaciones comparables y documentación específica.

### Power banks

La subcategoría mantiene demanda, pero la combinación de FOB elevado, claims de capacidad y complejidad logística aumenta su riesgo. Corresponde buscar alternativas y no depender del proveedor actual.

### Paneles plegables

Pasan a ser la subcategoría con mejor avance comercial de esta ronda. Los modelos compactos y medios combinan:

- Packing razonable.
- Orden mixta.
- MOQ controlado.
- Baja complejidad por ausencia de batería.
- Margen preliminar positivo.

---

## 6. Próximas acciones

1. Esperar las aclaraciones enviadas a DAT, Ani, Nulike y Shine Solar.
2. Revisar documentos técnicos por modelo.
3. Comparar condiciones para muestras.
4. Mantener búsqueda paralela de proveedores de power banks.
5. Reemplazar las simulaciones preliminares cuando existan costos definitivos.
6. No cerrar Margen Potencial ni Facilidad de Importación todavía.
7. Retomar en paralelo la ejecución operativa de Viaje organizado.

---

## 7. Relación con la matriz

La actualización importable asociada agrega:

- Cotizaciones preliminares de DAT y Shine Solar.
- Simulaciones de margen para paneles de 15W y 40W.
- Evidencias de Margen Potencial.
- Evidencia preliminar de Facilidad de Importación.

No se crean nuevos productos base.

Los valores exactos y supuestos permanecen en la matriz privada para evitar duplicación y exposición comercial.

---

## 8. Requisitos nuevos para el Intelligence Engine

Esta ronda refuerza la necesidad de:

- Supplier Response Analyzer.
- Certificate-to-Model Matcher.
- Claims Validation Gate.
- Incoterm Cost Comparator.
- Mixed Order Simulator.
- Supplier Follow-up Generator.
- Private Supplier Knowledge Base.

---

## 9. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-20 | Primera consolidación pública de negociación y validación de proveedores del Nicho 1. |
