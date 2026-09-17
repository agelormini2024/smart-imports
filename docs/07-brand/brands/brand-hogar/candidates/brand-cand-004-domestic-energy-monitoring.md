---
id: brand-cand-004
title: Domestic Energy Monitoring
description: Brand Candidate Screening de monitoreo doméstico del consumo energético para Marca Hogar.
version: 0.1.0
status: pass-to-method-v2
brand: brand-hogar
created: 2026-09-17
updated: 2026-09-17
tags:
  - brand-candidate
  - home
  - energy
  - resources
  - monitoring
  - screening
related:
  - si-brand-001
  - si-brand-002
---

# BRAND-CAND-004 — Monitoreo doméstico del consumo energético

## 1. Identificación

```text
Candidate ID: BRAND-CAND-004
Brand: brand-hogar
Solution: Monitoreo doméstico del consumo de energía
Primary Mission: Usar mejor los recursos
Screening Date: 2026-09-17
Decision: PASS TO METHOD V2
```

## 2. Solution

> **Monitoreo doméstico del consumo de energía orientado a hacer visibles patrones, consumos anómalos y oportunidades de uso más eficiente de los recursos.**

La Solution no presupone un Product Base concreto.

Method v2 podrá normalizar posteriormente arquitecturas como:

```text
medición en punto de consumo
monitor central del hogar
medición por circuito
monitor + identificación/desagregación de consumos
```

## 3. Problema reconocible

> **Falta de visibilidad sobre cómo, cuándo y dónde se consume energía dentro del hogar, dificultando identificar desperdicios, anomalías u oportunidades de optimización.**

## 4. Screening

- Problema reconocible: fuerte.
- Mission Fit: muy fuerte.
- Centralidad: muy fuerte.
- Tangibilidad de la medición: muy fuerte.
- Tecnología útil: muy fuerte.
- Brand Relevance: `HIGH`.
- Brand Credibility: `PENDING BY PRODUCT BASE / MEASUREMENT ACCURACY / ACTIONABILITY / CLAIM`.
- Territory Risk: `LOW`.

La Solution pertenece directamente a la misión `Usar mejor los recursos`.

## 5. Regla metodológica principal

> **Measurement ≠ Savings.**

En español:

> **Medir consumo no equivale a reducir consumo.**

Debe mantenerse separada la siguiente cadena:

```text
medir
↓
medir correctamente
↓
presentar información útil
↓
generar información accionable
↓
permitir cambios
↓
producir ahorro
```

Cada paso necesita evidencia propia.

## 6. Actionability

No todos los monitores ofrecen el mismo valor práctico.

Un equipo que sólo muestre consumo instantáneo puede ser menos útil que otro que permita:

```text
consumo histórico
comparación
picos
alertas
patrones
desagregación
costos estimados
anomalías
```

Por eso se registra conceptualmente `ACTIONABILITY` como aspecto a observar durante Method v2.

No se incorpora todavía como campo formal de matriz.

## 7. Tangibilidad y claims

La medición puede expresarse mediante variables objetivas como:

```text
W
kW
kWh
horarios
picos
históricos
costos estimados
```

Pero:

```text
measurement claim
≠
savings claim
```

Un claim de ahorro requiere evidencia adicional.

## 8. Brand Credibility

```text
Brand Relevance: HIGH
Brand Credibility:
PENDING BY PRODUCT BASE /
MEASUREMENT ACCURACY /
ACTIONABILITY /
CLAIM
```

La credibilidad dependerá de qué mide, cómo mide, precisión real, calidad de la información, utilidad práctica y claims comerciales.

## 9. Precisión de medición

Method v2 deberá validar:

```text
accuracy
measurement range
resolution
sampling
voltage/current compatibility
calibration
measurement methodology
```

También debe evitar confundir:

> **precision displayed ≠ measurement accuracy**

## 10. Experiencia de marca

Existe potencial de valor mediante:

- explicación de W y kWh;
- interpretación de picos;
- comparación entre períodos;
- identificación de consumos anómalos;
- configuración de alertas;
- traducción de consumo a costo;
- educación sobre patrones de consumo;
- soporte;
- integración con software.

Existe además una posible capa futura de diferenciación:

```text
hardware
↓
datos
↓
software
↓
analítica
↓
información accionable
```

Esa posibilidad no forma parte del criterio de aprobación del Brand Fit.

## 11. Monitoring ≠ Control / Optimization

No deben mezclarse prematuramente:

```text
MONITORING
```

con:

```text
CONTROL / OPTIMIZATION
```

Un Product Base puede sólo medir. Otro puede además controlar cargas, circuitos o automatizaciones.

Method v2 deberá normalizar esas arquitecturas por separado cuando corresponda.

## 12. Claims / assumptions to validate

Method v2 deberá validar, según cada Product Base:

```text
qué mide
dónde mide
accuracy
measurement range
resolution
sampling frequency
arquitectura de sensores
instalación requerida
compatibilidad eléctrica con Argentina
número de circuitos / dispositivos
datos históricos
alertas
desagregación de consumo
método de identificación de cargas
dependencia de nube
funcionamiento offline
app / plataforma
exportación de datos
privacidad
costo recurrente / suscripción
actionability
automatización disponible
claims de ahorro
certificaciones
seguridad eléctrica
instalación y postventa
```

## 13. Territory Risk

```text
LOW
```

Aceptar esta Solution no implica aceptar Smart Home o automatización genérica.

La frontera es:

> **gestión útil y verificable del recurso energía.**

## 14. Decisión

```text
PASS TO METHOD V2
```

Razón:

> La Solution pertenece directamente a `Usar mejor los recursos`, aborda un problema reconocible de falta de visibilidad sobre el consumo energético y permite generar información objetiva y potencialmente accionable. Sin embargo, la medición no debe confundirse con ahorro: Method v2 deberá validar precisión, utilidad práctica y cualquier claim de optimización.

## 15. Method v2 handoff

Method v2 recibe:

```text
Monitoreo doméstico del consumo de energía orientado a hacer visibles patrones, consumos anómalos y oportunidades de uso más eficiente de los recursos.
```

Debe mantener separados:

```text
measurement
accuracy
actionability
control
optimization
savings claim
```

antes de evaluar demanda, competencia, origen, Headroom, Landed Cost y decisión comercial.

## 16. Aprendizaje metodológico

```text
BRAND-CAND-001
Smart ≠ Brand Fit

BRAND-CAND-002
Brand Relevance ≠ Brand Credibility

BRAND-CAND-003
Component specification ≠ System performance

BRAND-CAND-004
Measurement ≠ Savings
```

## 17. Documentos relacionados

- [Marca Hogar](../README.md)
- [Brand Candidate Screening](../../../si-brand-002-brand-candidate-screening-method.md)
