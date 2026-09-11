---
id: si-research-005
title: Niche 3 — Pets: Method v2, Phases 0–6
description: Consolidación de Research Brief, arquitecturas, madurez, demanda, competencia, Potencial de Marca y Productos Base del Nicho 3.
version: 1.0.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-11
updated: 2026-09-11
tags:
  - research
  - niche-003
  - pet-care
  - method-v2
  - product-base
related:
  - si-roadmap-002
  - si-agent-001
  - si-decision-014
phase: research
---

# SI-RESEARCH-005 — Nicho 3: Mascotas, cuidado, bienestar y tecnología — Fases 0–6

## 1. Propósito

Consolidar el trabajo realizado sobre el Nicho 3 hasta el cierre de la Fase 6 y conservar el razonamiento que no debe quedar únicamente en el chat o en la matriz.

La matriz operativa conserva los datos estructurados y la trazabilidad. Este documento conserva:

- alcance;
- reglas metodológicas;
- estado por arquitectura;
- conclusiones de Demanda y Competencia;
- Potencial de Marca;
- normalización de Productos Base;
- limitaciones descubiertas;
- próxima acción.

## 2. Research Brief

### Nicho

**Mascotas — cuidado, bienestar y tecnología**

### Mercado

- Argentina.
- B2C como canal principal.
- B2B como extensión natural cuando la arquitectura lo permita.
- Perros y gatos como especies iniciales.

### Tesis

No se busca un catálogo genérico de pet-tech. Se buscan necesidades donde una marca propia pueda capturar valor mediante una combinación de producto, QA, soporte, repuestos, consumibles, servicio, software, datos o ecosistema.

La complejidad técnica no es un criterio automático de descarte. Debe tratarse como riesgo y evaluarse contra la oportunidad.

## 3. Jerarquía metodológica

Method v2 utiliza:

```text
NICHO
  ↓
NECESIDAD / FAMILIA
  ↓
ARQUITECTURA DE SOLUCIÓN
  ↓
PRODUCTO BASE
```

Reglas principales:

- `publicación ≠ competidor ≠ SKU ≠ Producto Base`;
- normalizar antes de evaluar;
- Demanda y Competencia son dimensiones diferentes;
- un Producto Base describe una configuración comercial, no un proveedor;
- las diferencias superficiales de color, marca, packaging o feature no crean por sí mismas un nuevo PB;
- un PB se separa cuando cambia materialmente el job, segmento, economía estructural, infraestructura o riesgo.

## 4. Arquitecturas evaluadas

### 4.1 Established anchors

- Feeder automático/smart.
- Fuente convencional/recirculante.

Se utilizaron como referencia de madurez y adopción, no como arquitecturas prioritarias de avance.

### 4.2 Arquitecturas que avanzan

| Arquitectura | Madurez | Estado después de Competencia | Potencial de Marca |
|---|---|---|---|
| Vacuum Grooming | Early Established | ADVANCE | MEDIO–ALTO |
| Arenero automático/smart | Emerging | ADVANCE | ALTO — CONDICIONADO |
| Smart Fountain | Emerging | ADVANCE | MEDIO–ALTO |
| GPS + Wellness | Emerging | ADVANCE — CONDITIONAL | ALTO — FUERTEMENTE CONDICIONADO |

### 4.3 Watchlist

- Dedicated Pet Camera + interaction.
- Mobile Pet Robot.

No pasan a Fase 6 en este ciclo.

## 5. Fase 3 — Demanda

### Vacuum Grooming

La necesidad está bien establecida: cortar, cepillar y controlar pelo suelto en el hogar. La señal local es consistente y el producto ya tiene adopción visible. El principal desafío no es demostrar el job sino encontrar una propuesta defendible más allá del OEM genérico.

### Arenero automático/smart

La higiene felina está ampliamente validada; la automatización todavía pertenece a un segmento de mayor ticket. Existe señal local suficiente para continuar, pero el TAM relevante no es “todos los dueños de gatos”. Depende de:

```text
capacidad de pago
× intensidad del problema
× frecuencia de limpieza
× valor asignado a la conveniencia
```

### Smart Fountain

La necesidad de hidratación y las fuentes recirculantes convencionales están fuertemente validadas. La capa smart local tiene menor madurez. La demanda no puede inferirse automáticamente desde el mercado de fuentes convencionales.

### GPS + Wellness

La localización y seguridad tienen señal positiva. Wellness avanzado y aceptación de suscripción/recurrente no quedaron validados localmente. La entrada debe partir de **GPS / localización / seguridad**; Wellness es una capa adicional, no una premisa de demanda comprobada.

## 6. Fase 4 — Competencia

### 6.1 Vacuum Grooming

Conclusión:

- competencia directa: **MEDIA–ALTA**;
- fragmentación de marcas: alta;
- OEM replicability: alta;
- features básicas: commoditizadas;
- sustituto compuesto `clipper + deshedder + aspiradora doméstica`: **muy fuerte**;
- diferenciación defendible: servicio, especialización, repuestos, accesorios, garantía, contenido y ecosistema.

**Estado: ADVANCE.**

### 6.2 Arenero automático/smart

Conclusión:

- competencia directa: **ALTA**;
- duplicación OEM: alta;
- diversidad mecánica: genuina;
- smart básico: fácilmente replicable;
- QA, seguridad y postventa: barreras importantes;
- sustitutos tradicionales: **muy fuertes**.

Una propuesta `tambor genérico + Tuya + logo` no constituye ventaja.

**Estado: ADVANCE.**

### 6.3 Smart Fountain

Conclusión:

- competencia directa: **MEDIA**;
- sensor-smart: adopción local suficiente;
- WiFi/app: poca defensibilidad aislada;
- fuentes recirculantes convencionales: principal sustituto;
- diferenciación posible: higiene, materiales, confiabilidad, mantenimiento, filtros, repuestos y monitoreo real.

**Estado: ADVANCE.**

### 6.4 GPS + Wellness

Conclusión:

- competencia directa global: **MEDIA**;
- GPS Core local: **MEDIA–ALTA**;
- tags colaborativos / Find networks: sustitutos **muy fuertes** del GPS Core;
- hardware GPS 4G: altamente replicable;
- sistema completo hardware + red + backend + app + datos: mucho más defendible;
- backend continuity risk: muy alto;
- Wellness avanzado local: todavía no validado.

**Estado: ADVANCE — CONDITIONAL.**

## 7. Reglas metodológicas surgidas de Competencia

### 7.1 OEM no significa proveedor exacto

Distinguir siempre:

1. plataforma OEM;
2. proveedor candidato;
3. relación proveedor-cliente;
4. fabricante exacto.

Un match visual no prueba una relación comercial.

### 7.2 Sustituto puede ser una combinación

Un competidor indirecto no necesita ser un solo SKU. Ejemplo:

```text
clipper + deshedder + aspiradora doméstica
```

puede competir fuertemente contra Vacuum Grooming.

### 7.3 Safety claim no equivale a seguridad validada

Especialmente en areneros:

```text
mecanismo declarado
≠
mecanismo validado
```

La validación de seguridad pertenece a fases posteriores.

### 7.4 Network generation no equivale a network compatibility

Para GPS:

```text
"4G"
≠
compatible con Argentina
```

Se requiere:

- tecnología celular;
- modem/variante;
- bandas exactas;
- operadores;
- fallback;
- escenario de cobertura.

### 7.5 Standby battery no equivale a tracking battery

La autonomía de un tracker debe compararse bajo intervalos reales de tracking, cobertura y frecuencia de uso.

### 7.6 Tercera fabricación no equivale a white-label genérico

Un producto puede ser fabricado por un tercero y seguir siendo propiedad de diseño, firmware, marca y ecosistema del cliente.

## 8. Fase 5 — Potencial de Marca

Definición:

> **Potencial de Marca = capacidad de una arquitectura para sostener una propuesta comercial reconocible y preferible más allá del precio y de las especificaciones genéricas del hardware.**

Regla:

> **Poder ponerle logo a un OEM ≠ tener potencial de marca.**

### Ejes utilizados

1. relevancia de marca en la compra;
2. espacio para diferenciación real;
3. defensibilidad frente a copia OEM;
4. relación postventa;
5. potencial de ecosistema;
6. capacidad de agregar valor local;
7. evolución de la ventaja competitiva.

### Resultados

| Arquitectura | Potencial | Principal fortaleza | Principal condición |
|---|---|---|---|
| Vacuum Grooming | MEDIO–ALTO | especialización + portfolio + servicio | hardware replicable |
| Arenero automático/smart | ALTO — CONDICIONADO | confianza + QA + postventa | seguridad y riesgo reputacional |
| Smart Fountain | MEDIO–ALTO | ownership + filtros + mantenimiento | sustituto convencional fuerte |
| GPS + Wellness | ALTO — FUERTEMENTE CONDICIONADO | servicio + software + datos | complejidad IoT y valor Wellness no validado |

## 9. Fase 6 — Productos Base

Definición adoptada:

> **Producto Base es una configuración normalizada y comercialmente significativa de una arquitectura de solución, suficientemente concreta para permitir comparación de mercado, búsqueda de origen y evaluación económica, pero independiente de una marca, publicación, vendedor o proveedor particular.**

Resultado:

| ID | Arquitectura | Producto Base |
|---|---|---|
| BASE-PET-001 | Vacuum Grooming | Vacuum Grooming doméstico integrado |
| BASE-PET-002 | Arenero automático/smart | Arenero automático rotativo cerrado |
| BASE-PET-003 | Arenero automático/smart | Arenero automático open-top / acceso amplio |
| BASE-PET-004 | Arenero automático/smart | Arenero automático de rastrillo |
| BASE-PET-005 | Smart Fountain | Fuente inteligente automatizada/conectada |
| BASE-PET-006 | Smart Fountain | Fuente con monitoreo cuantitativo de hidratación |
| BASE-PET-007 | GPS + Wellness | Tracker GPS 4G para mascotas |
| BASE-PET-008 | GPS + Wellness | Tracker GPS + Wellness avanzado |

### Normalización aplicada

- Vacuum Grooming: múltiples competidores y OEM convergen en **1 PB**.
- Areneros: las diferencias mecánicas justifican **3 PB**.
- Smart Fountain: `sensor-smart` y `connected-smart` se unifican; monitoreo cuantitativo se separa → **2 PB**.
- GPS: GPS Core + actividad básica se unifican; Wellness avanzado se separa → **2 PB**.

## 10. Materialización en la matriz

Snapshot operativo:

```text
matrix-aut34-niche3-phase6-corrected.xlsx
```

Validación:

```text
Matrix Validator: v0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
SHA-256:
ad791f8d5fe5c0bb0b18994d4c12d45b187499216f3dbd90cd42e4a9b08f9bf5
```

`aut34` incorpora el Nicho 3, sus ocho Productos Base y la evidencia estructurada consolidada. No incorpora todavía Landed Cost, nuevos snapshots MARG ni un screening exhaustivo de origen.

## 11. Necesidades futuras de Matrix vNext

El trabajo real reveló tres necesidades de modelado. No bloquean el ciclo actual y no justifican reabrir `full-matrix-v5` todavía.

1. **Familia + Arquitectura explícitas**
   La matriz actual utiliza `Subcategoría` como representación temporal de Arquitectura.

2. **Tipo de competencia explícito**
   Se necesita distinguir de forma canónica:
   `DIRECTA | INDIRECTA | SUSTITUTO | BENCHMARK`.

3. **Next Action alineado con Method v2**
   `Nichos.Proxima Accion` conserva una secuencia legacy de criterios; el método vigente avanza por fases.

## 12. Riesgos e hipótesis abiertas

### Vacuum Grooming

- posibilidad real de posicionamiento especializado;
- repuestos/servicio como barrera acumulativa;
- riesgo de caer en private label genérico.

### Arenero automático/smart

- seguridad y QA requieren evaluación de proveedor mucho más estricta;
- compatibilidad con arenas locales;
- capacidad real de postventa y repuestos.

### Smart Fountain

- cuánto premium admite el mercado sobre una buena fuente convencional;
- valor incremental de monitoreo cuantitativo;
- precisión de medición y disponibilidad de filtros.

### GPS + Wellness

- compatibilidad celular documental;
- continuidad de backend;
- autonomía real;
- ergonomía 24/7;
- aceptación local de recurrencia;
- demanda real de Wellness avanzado.

## 13. Próxima fase

### Fase 7 — Shortlist pre-origen

Objetivo:

> Reducir los ocho Productos Base a los candidatos que justifican invertir tiempo en screening formal de origen.

Todavía no corresponde:

- seleccionar proveedor final;
- calcular Landed Cost;
- negociar MOQ;
- realizar RFQ exhaustivo;
- decidir compra.

El orden sigue siendo:

```text
Fase 7 — shortlist pre-origen
→ Fase 8 — origin screening + comparabilidad
→ Fase 9 — Headroom
→ Fase 10 — Minimum Landed Cost Dataset
→ Fase 11 — Landed Cost
→ Fase 12 — Margin + ROI
→ Fase 13 — final shortlist
→ Fase 14 — validación real
```

## 14. Documentos relacionados

- [Niche 003 — README](./README.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-DECISION-014 — Adopt Niche 3 Method v2 and aut34](../../09-decision-log/si-decision-014-adopt-niche3-method-v2-and-aut34.md)

## 15. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-11 | Consolidación inicial de Fases 0–6, Method v2, ocho PB y validación de `aut34`. |
