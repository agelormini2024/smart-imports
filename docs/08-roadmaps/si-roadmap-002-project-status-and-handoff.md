---
id: si-roadmap-002
title: Project Status and Handoff
description: Estado operativo, bloqueos, próximas acciones y contexto mínimo para retomar Smart Imports.
version: 0.10.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-16
updated: 2026-08-07
tags:
  - status
  - handoff
  - roadmap
  - continuity
related:
  - si-roadmap-001
  - si-agent-001
  - si-func-001
  - si-tech-001
  - si-tech-002
  - si-decision-009
  - si-decision-010
  - si-decision-011
  - si-decision-012
  - si-decision-013
audience:
  - founder
  - partner
  - developer
  - assistant
phase: foundation
---
# SI-ROADMAP-002 — Estado actual y handoff de Smart Imports

> Punto de entrada operativo obligatorio para retomar el proyecto sin depender de un chat específico.

## 1. Fuentes de verdad

```text
Documentación y negocio:
https://github.com/agelormini2024/smart-imports

Software ejecutable:
https://github.com/agelormini2024/smart-imports-engine

Release vigente del Engine:
v0.1.0 — Matrix Validator MVP

Baseline de release del Validator:
aut32 → full-matrix-v5 0.7.0

Matriz operativa vigente:
aut33 → full-matrix-v5 0.7.0
```

Compatibilidad histórica:

```text
aut29 → full-matrix-v3 0.1.0
aut30 → full-matrix-v4 0.6.0
aut31 → full-matrix-v5 0.7.0; checkpoint histórico con EV-0009
aut32 → full-matrix-v5 0.7.0; baseline de release con EVAL-0009
aut33 → full-matrix-v5 0.7.0; matriz operativa comercial vigente / PASS
```

La matriz operativa es la fuente de verdad de los datos estructurados. Los documentos resumen decisiones, estado y método; no deben convertirse en una base paralela.

## 2. Snapshot al 2026-08-07

| Campo | Estado |
|---|---|
| Fase | Foundation avanzada / validación comercial del método |
| Nichos trabajados | 2 |
| Energía Solar Portátil | Investigación piloto cerrada en pausa selectiva |
| Viaje organizado | Demanda y Competencia cerradas; screening de origen/headroom completado; Landed Cost por iniciar |
| Matriz operativa | `matrix-aut33-supplier-screening-headroom-corrected.xlsx` |
| SHA-256 aut33 | `fb1905260ad24fd4bb0a8284082f1bebb92473de99c46963fb65c1228837bfd1` |
| Schema vigente | `full-matrix-v5 0.7.0` |
| Matrix Validator | `v0.1.0` publicado y operativo |
| Tests | 40 archivos / 170 tests |
| CLI | 5 casos operativos verificados |
| E2E público | 10 fixtures XLSX |
| CI | Verde |
| Resultado aut33 | `PASS`; 0 errores, 0 warnings, 0 limitaciones |
| Próxima dependencia | Respuesta FOB de Xichen para `BASE-TRAVEL-024` |

## 3. Matrix Validator — estado cerrado

El Matrix Validator MVP ya no es un bloqueo comercial.

Baseline de release:

```text
Aplicación: 0.1.0
Schema operativo: full-matrix-v5 0.7.0
Fixture privado de release: aut32
Resultado aut32: PASS
Tests: 40 archivos / 170 tests
CLI: 5 casos
E2E: 10 fixtures
CI: verde
Tag: v0.1.0
Commit de release: 9f4125b
GitHub Release: https://github.com/agelormini2024/smart-imports-engine/releases/tag/v0.1.0
Package publication: none; private: true
```

La evolución futura del Validator debe responder a necesidades concretas descubiertas por el trabajo comercial. No se ampliará el schema por anticipación.

Pendientes no bloqueantes posteriores al MVP:

- Agregados cruzados entre hojas.
- Secuencia global y gaps de identificadores.
- Controles históricos adicionales.
- Revisión editorial de resúmenes.
- Decisión final sobre hojas `Legacy`.

## 4. Matriz operativa aut33

`aut33` incorpora el bloque de screening de proveedores y el nuevo concepto de Import Cost Headroom.

Resultado del Validator:

```text
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: 0
SHA-256: fb1905260ad24fd4bb0a8284082f1bebb92473de99c46963fb65c1228837bfd1
```

Principales incorporaciones del ciclo:

- 27 nuevas fuentes de proveedor: publicaciones Alibaba y respuestas directas.
- 13 nuevas evidencias consolidadas por Producto Base.
- 40 relaciones `Evidencia Fuentes`.
- 7 nuevas `Cotizaciones Proveedores`.
- Nuevo snapshot `RES-MARG-0004` de screening de origen/headroom.
- 13 nuevas filas de `Resumen Margen Productos`.
- No se agregaron nuevas filas `MARG-*` porque todavía no existe un Landed Cost suficientemente defendible.

`aut32` se conserva como baseline técnico de release. `aut33` es la matriz operativa comercial vigente.

## 5. Evolución del método — Import Cost Headroom

Durante el screening del Nicho 2 se descartó usar un factor genérico de importación como sustituto de un costo puesto real.

Se incorpora como puerta de decisión preliminar:

```text
Import Cost Headroom
=
Costo puesto económico unitario máximo compatible con el margen objetivo
÷
Costo unitario de origen
```

El indicador responde:

> ¿Cuánto puede crecer el costo de origen antes de que el producto deje de cumplir el margen objetivo?

No estima el costo real de importación. Su función es decidir qué productos justifican invertir tiempo en NCM, packing, CBM, flete, derechos, gastos de nacionalización y demás componentes del Landed Cost.

El benchmark anecdótico `FOB × 2,60` aportado por un importador de sillas de oficina se conserva únicamente como stress test empírico externo. No se adopta como factor de cálculo de Smart Imports.

## 6. Resultado del screening del Nicho 2

### 6.1 Candidatos para Landed Cost

| Prioridad | Producto | Headroom aprox. | Lectura actual |
|---:|---|---:|---|
| 1 | `BASE-TRAVEL-024` — kit x11 de envases plásticos | `5,80x` | Señal más fuerte; comparable limpio y packing conocido |
| 2 | `BASE-TRAVEL-022` — kit mixto x15/x17 | `3,19x` | Fuerte; comparabilidad cercana, no exacta |
| 3 | `BASE-TRAVEL-010` — bolsas al vacío + bomba manual | `2,22x` | Investigable; demanda fuerte |
| 4 | `BASE-TRAVEL-018` — neceser colgante | `2,06x` | Investigable; comparable de origen razonable |
| Condicional | `BASE-TRAVEL-023` — set x3 de 60 ml | `3,15x` si se confirma composición | No avanzar a Landed Cost hasta aclarar el set |

### 6.2 Casos frágiles o pausados

| Producto | Headroom aprox. | Decisión actual |
|---|---:|---|
| `BASE-TRAVEL-021` | `1,52x` | Pausar; precio EXW confirmado deja poco espacio |
| `BASE-TRAVEL-003` | `1,40x` | Pausar |
| `BASE-TRAVEL-013` | `1,35x` | Pausar |
| `BASE-TRAVEL-001` | no formal | Benchmark |
| `BASE-TRAVEL-016` | no formal | PDF no comparable al Producto Base |
| `BASE-TRAVEL-017` | no formal | PDF no comparable al Producto Base |
| `BASE-TRAVEL-019` | orientativo | Benchmark |
| `BASE-TRAVEL-020` | orientativo | Benchmark / commodity |

La shortlist es una hipótesis de trabajo, no un filtro irreversible. `BASE-TRAVEL-024` reingresó con fuerza después del screening y demuestra que el método debe permitir rescatar productos cuando aparece evidencia económica superior.

## 7. BASE-TRAVEL-024 — estado puntual

Producto:

```text
Kit de 11 envases plásticos y accesorios con pouch
Proveedor: Taizhou Xichen Plastic Industry Co., Ltd.
Material principal: PET
Precio informado: USD 0,74 a 100/300; USD 0,73 a 500; USD 0,72 a 1.000
MOQ: 2
Puerto informado: Ningbo / Shanghai
Incoterm del precio: todavía no confirmado
```

Packing publicado:

```text
Caja master: 65 × 49,5 × 51,5 cm
Cantidad: 110 sets
Peso bruto: 16,33 kg
CBM por caja: ~0,1657 m³
Peso bruto por set: ~0,1485 kg
```

Se envió follow-up al proveedor solicitando:

- FOB Ningbo o Shanghai para 500 y 1.000 sets completos x11 + pouch.
- Cantidad total de cajas.
- Dimensión de caja.
- Peso bruto total.
- CBM total.
- HS code sugerido.
- Material/safety report disponible.

No completar la simulación de margen hasta recibir o estimar de forma defendible el Landed Cost.

## 8. Modelo de Landed Cost — definición pendiente de formalización

El circuito del Nicho 2 reveló que `Simulación Margen` no debe absorber todo el detalle aduanero y logístico.

Después de cerrar el circuito completo del Nicho 2 se diseñará formalmente un modelo normalizado con, como mínimo:

```text
Landed Cost
Landed Cost Componentes
Resumen Landed Cost
```

Responsabilidad esperada:

```text
Landed Cost
→ calcula/representa el costo puesto por escenario y escala

Landed Cost Componentes
→ conserva el detalle trazable de flete, seguro, derechos, tasas,
  terminal, despachante, transporte local, impuestos y percepciones

Resumen Landed Cost
→ vista rápida por producto y escenario

Simulación Margen
→ consume el costo puesto resultante; no reemplaza al modelo de Landed Cost
```

Debe distinguirse:

```text
Costo puesto económico
≠
Desembolso financiero total
```

IVA, percepciones y otros conceptos recuperables deben separarse de los costos económicos definitivos.

No modificar todavía el schema v5 por esta necesidad. Primero se completará manualmente al menos un circuito de Landed Cost y luego se diseñará el contrato de datos definitivo.

## 9. Smart Imports Decision Reporter — definición post-Nicho 2

La matriz ya contiene suficiente información como para resultar difícil de leer rápidamente en una reunión de decisión.

Después de cerrar el Nicho 2 se diseñará un módulo de Smart Imports Engine que reciba una matriz validada y produzca un reporte ejecutivo para Founder y socio.

Principios definidos:

1. La matriz validada es la fuente de verdad.
2. El reporte es una vista derivada, no una segunda base de datos.
3. La primera versión debe ser determinística.
4. Las decisiones del reporte deben provenir de decisiones registradas en la matriz, no de inferencias autónomas de un LLM.
5. Una futura capa narrativa con IA deberá distinguir datos, decisiones registradas y texto generado.

Contenido esperado:

- Estado general del nicho.
- Productos investigados y priorizados.
- Demanda y competencia.
- Headroom.
- Landed Cost cuando exista.
- Margen y ROI cuando existan.
- Riesgos.
- Razones para avanzar, pausar o descartar.
- Pendientes críticos.

Nombre de trabajo del módulo:

```text
Decision Reporter
```

La implementación no comienza hasta completar el circuito del Nicho 2 y realizar su retrospectiva.

## 10. Estado comercial

### Energía Solar Portátil

- Sirvió como primera ejecución integral del método.
- No se fuerza una conclusión positiva.
- AT-999 permanece pausado.
- Paneles y demás candidatos sólo se retomarán si recuperan prioridad.

### Viaje organizado y equipaje funcional

- Demanda: cerrada.
- Competencia: cerrada.
- Screening de proveedores/origen: completado.
- Headroom: incorporado.
- aut33: `PASS`.
- Landed Cost: siguiente etapa.
- Primer producto: `BASE-TRAVEL-024`.

## 11. Dependencias actuales

| Dependencia | Estado | Acción |
|---|---|---|
| FOB de `BASE-TRAVEL-024` | Esperando proveedor | Continuar cuando responda Xichen |
| Packing total 500/1.000 | Parcial | Confirmar con proveedor |
| NCM | Hipótesis, no definitiva | Validar posteriormente con despachante |
| Derechos/tasas | Pendiente de escenario | Incorporar en Landed Cost |
| Flete internacional | Pendiente | Cotizar/estimar por escala |
| Gastos locales | Pendiente | Calibrar con despachante y experiencia real |
| Modelo de Landed Cost | Definición conceptual | Formalizar después del circuito Nicho 2 |
| Decision Reporter | Definición conceptual | Diseñar después de la retrospectiva Nicho 2 |

## 12. Próxima secuencia

```text
Esperar respuesta Xichen para BASE-TRAVEL-024
→ construir primer Landed Cost por escenarios 500 / 1.000
→ comparar contra headroom
→ alimentar Simulación Margen
→ repetir sólo con candidatos sobrevivientes
→ cerrar Nicho 2 end-to-end
→ retrospectiva metodológica
→ formalizar modelo Landed Cost
→ diseñar Decision Reporter
→ actualizar schema/Engine sólo si el proceso manual lo justifica
→ comenzar investigación de nuevos nichos
```

## 13. Protocolo para abrir un nuevo chat

1. Compartir ambos repositorios o sus URLs.
2. Pedir lectura inicial de `SI-ROADMAP-002`.
3. Indicar que el Matrix Validator v0.1.0 está cerrado y no debe reabrirse sin una necesidad comercial concreta.
4. Adjuntar `aut33` sólo cuando la tarea requiera datos privados de la matriz.
5. No volver a adjuntar PDFs ya consolidados salvo que sea necesario auditar una fuente específica.
6. Adjuntar la nueva respuesta de Xichen cuando llegue.
7. Continuar de a un paso por vez.

## 14. Próxima acción concreta

```text
Recibir respuesta FOB de Xichen para BASE-TRAVEL-024
→ construir el primer Landed Cost defendible
→ comparar escenario realista con headroom 5,80x
```

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.7.0 | 2026-08-03 | Handoff de v3/v4 y normalización de fuentes. |
| 0.8.0 | 2026-08-04 | Adopción de aut31/v5, 144 tests y cierre técnico de vistas derivadas. |
| 0.9.0 | 2026-08-05 | Adopción de aut32, cierre del MVP y publicación de `v0.1.0`. |
| 0.10.0 | 2026-08-07 | Registra aut33 validada, Import Cost Headroom, shortlist de Landed Cost y definiciones post-Nicho 2 para Landed Cost y Decision Reporter. |
