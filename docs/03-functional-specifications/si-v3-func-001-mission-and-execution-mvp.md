---
id: si-v3-func-001
title: "Smart Imports v3 — Mission and Execution Functional Design (MVP)"
description: "Diseño funcional inicial de misiones y ejecuciones, con preflight, control de incidencias, resultados parciales y cierre estratégico."
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: "2026-10-22"
updated: "2026-10-22"
tags:
  - smart-imports-v3
  - functional-design
  - mvp
  - missions
  - executions
  - governance
related:
  - si-v3-vision-001
  - si-doc-001
  - si-roadmap-002
audience:
  - founder
  - developer
  - assistant
phase: design
---

# SI-V3-FUNC-001 — Diseño funcional del MVP: misiones y ejecuciones

> **Propósito:** describir el comportamiento funcional del primer circuito de investigación de Smart Imports v3, sin anticipar decisiones de arquitectura o implementación.

## 1. Estado y alcance

Este documento consolida las decisiones tomadas durante el **Bloque 1 — Misión y ejecución** del diseño funcional de Smart Imports v3. Está en estado `draft` para revisión: **no constituye todavía una especificación técnica aprobada**.

El primer caso de prueba del MVP será una **misión de reproducción histórica** sobre `BRAND-CAND-009` (territorio Fitness), limitada inicialmente a tres Product Bases:

- `BASE-FIT-010` — `FINALIST — CONDITIONED` en Method v2.
- `BASE-FIT-012` — `NOT COMMERCIAL FINALIST — SAFETY-GATED` en Method v2.
- `BASE-FIT-013` — `DEFER — REOPENABLE` en Method v2.

Los estados anteriores son **referencias históricas para comparar resultados**, no conclusiones que se deban suministrar a los agentes durante la evaluación a ciegas ni recomendaciones de importación.

La prueba inicial parte de **evidencias históricas conocidas**. La reinvestigación autónoma de fuentes actuales será una etapa posterior y diferenciada. `F14` permanece **NOT OPENED**: quedan fuera del alcance las compras, pedidos, RFQ, negociación, contacto comercial, muestras, homologación y aprobación para importar.

## 2. Conceptos y responsabilidades

### 2.1. Misión

Una **misión** expresa una pregunta u objetivo de inteligencia comercial que perdura a través del tiempo. Conserva su alcance, contexto, oportunidades estudiadas, decisiones estratégicas y vínculos con sus ejecuciones.

### 2.2. Ejecución

Una **ejecución** es una instancia concreta de trabajo dentro de una misión. Tiene configuración fija durante su transcurso, presupuesto autorizado, insumos identificados, resultados, evidencias, bitácora y consumo atribuible. Ninguna ejecución sobrescribe los resultados históricos de otra.

### 2.3. Reparto de responsabilidades

- **Founder / Product Owner:** define el objetivo y las prioridades comerciales; autoriza el inicio, las ampliaciones de presupuesto y el cierre estratégico de la misión; evalúa observaciones relevantes.
- **Sistema / agentes:** planifican y ejecutan el análisis dentro del alcance autorizado; gestionan incidencias recuperables; documentan resultados, incertidumbres y recomendaciones.
- **Gobernanza / validadores:** aplican controles obligatorios de integridad, trazabilidad, coherencia y restricciones, independientemente de las skills opcionales.

## 3. Decisiones funcionales acordadas

| ID | Decisión | Comportamiento exigido |
|---|---|---|
| `DF-MVP-001` | **Misión → ejecuciones** | Una misión puede contener varias ejecuciones independientes y comparables; sus resultados no se sobrescriben. |
| `DF-MVP-002` | **Preflight obligatorio** | Antes de cada ejecución se verifican configuración, evidencias, presupuesto, capacidades e integridad. El inicio requiere autorización humana. |
| `DF-MVP-003` | **Preflight por criticidad** | `READY` y `READY WITH WARNINGS` permiten autorizar el comienzo; `BLOCKED` lo impide. Toda advertencia queda visible y trazada. |
| `DF-MVP-004` | **Cierre parcial de una ejecución** | Una ejecución puede concluir con resultados útiles y limitaciones explícitas, sin requerir que toda la misión esté resuelta. |
| `DF-MVP-005` | **Aislamiento de incidencias** | Si falla una tarea, se intenta recuperar o aislar; el trabajo independiente continúa. Una falla crítica sistémica puede detener la ejecución. |
| `DF-MVP-006` | **Cierre estratégico humano** | La IA puede recomendar cerrar una misión, pero solo el Founder decide cerrarla, mantenerla abierta o solicitar otra ejecución. |

### 3.1. Reglas transversales provenientes de la visión v3

- **Presupuesto en dos niveles:** límite global del sistema y presupuesto autorizado por ejecución/misión; los agentes no pueden aprobar ampliaciones por sí mismos.
- **Ampliación justificada:** ante recursos insuficientes, se solicita aprobación con trabajo pendiente, valor esperado e incertidumbres; no se promete retorno económico inexistente.
- **Skills opcionales:** la auditoría inteligente puede activarse o desactivarse antes de iniciar; la configuración se mantiene fija durante la ejecución. Una nueva configuración implica otra ejecución.
- **Controles obligatorios no desactivables:** integridad, evidencia, trazabilidad, restricciones críticas y decisiones reservadas a humanos.
- **Observabilidad activa:** el usuario puede señalar un dato o conclusión cuestionable, aportar observaciones y solicitar revisión; la intervención y su tratamiento quedan registrados.
- **Conocimiento comercial compartido:** los hallazgos podrán reutilizarse entre misiones con procedencia y vigencia; las decisiones comerciales se mantienen contextualizadas.
- **Diferencia entre ausencia de evidencia y evidencia negativa:** información insuficiente nunca se transforma automáticamente en un descarte comercial definitivo.
- **Cierre de misión no equivale a autorización de importación.**

## 4. Primer circuito funcional: reproducción histórica

### 4.1. Configuración inicial de la misión

La plantilla de prueba histórica deberá permitir identificar como mínimo:

1. **Objetivo y nombre de la misión.**
2. **Referencia de investigación:** `BRAND-CAND-009`.
3. **Alcance:** `BASE-FIT-010`, `BASE-FIT-012` y `BASE-FIT-013`.
4. **Modalidad:** reproducción con evidencias históricas previamente incorporadas.
5. **Restricciones comerciales:** no habilitar `F14`, importación, contacto ni compromiso comercial.

La experiencia de creación de misiones por **territorio**, **problema** o **exploración abierta** es parte de la visión general, **no requisito de implementación en el primer circuito**.

### 4.2. Configuración de la ejecución

Antes de iniciar se definen presupuesto autorizado, capacidades opcionales (incluida auditoría inteligente), referencia al conjunto de evidencias históricas y restricciones. La interfaz no debe obligar al usuario a elegir modelos, prompts ni parámetros técnicos internos.

### 4.3. Preflight

El sistema realiza las siguientes comprobaciones mínimas:

| Área | Verificación funcional |
|---|---|
| Configuración | Objetivo, alcance y opciones válidas. |
| Evidencias | Fuentes e insumos necesarios identificados; ausencias y limitaciones diferenciadas. |
| Presupuesto | Autorización y disponibilidad bajo el límite de la ejecución y el límite global; costo estimado preventivamente. |
| Capacidades | Skills seleccionadas disponibles para la ejecución. |
| Integridad | Identificadores, referencias y restricciones obligatorias sin fallas críticas. |

**Resultados del Preflight:**

- `READY`: condiciones obligatorias satisfechas.
- `READY WITH WARNINGS`: hay limitaciones no críticas que se muestran y conservan.
- `BLOCKED`: faltan condiciones indispensables; no se habilita el inicio.

Una advertencia no autoriza conclusiones no sustentadas. La autorización humana de inicio ocurre después del Preflight y no se repite por cada tarea `AUTO`.

### 4.4. Investigación y recuperación

La ejecución analiza las evidencias históricas y obtiene conclusiones propias. Para evitar sesgos en la prueba histórica, las **conclusiones de v2 se reservan para la comparación posterior**, sin suministrarlas como respuestas al agente evaluador.

Ante una incidencia localizada, el sistema debe intentar una recuperación razonable, registrar el problema y proseguir con tareas no dependientes. Si el problema compromete la validez de toda la ejecución —por ejemplo, una falla global de integridad— debe detener o bloquear el trabajo afectado conforme a sus controles.

### 4.5. Resultados y comparación

Cada ejecución conserva, como mínimo:

- Resultado por Product Base y justificación vinculada con evidencias.
- Distinción entre hechos, inferencias, supuestos y datos faltantes.
- Limitaciones, advertencias e incidencias no resueltas.
- Resultados de validaciones obligatorias.
- Configuración, presupuesto autorizado, consumo registrado y bitácora de decisiones/intervenciones.
- Identificación de la ejecución y vínculo con la misión.

Tras concluir la evaluación, se comparan resultados de v3 con la referencia histórica de v2. Una discrepancia no se considera automáticamente un error: debe explicarse y, si corresponde, investigarse.

### 4.6. Finalización de ejecución y cierre de misión

La ejecución puede terminar **completa**, **con limitaciones documentadas** o **fallida** por un problema técnico; estas situaciones no se confunden entre sí. La misión puede seguir abierta con una o varias ejecuciones ya concluidas.

La IA podrá **recomendar** el cierre de la misión, con sus razones y asuntos pendientes. El Founder conserva la decisión de cerrarla, solicitar otra ejecución o mantenerla abierta. Las conclusiones de investigación no reemplazan las decisiones de compra, inversión o cumplimiento externo.

## 5. Criterios de aceptación funcional iniciales

- **CA-01:** crear una misión histórica de `BRAND-CAND-009` y asociarle una ejecución sin duplicar la misión.
- **CA-02:** rechazar el inicio si el Preflight devuelve `BLOCKED`; permitir iniciar `READY WITH WARNINGS` con advertencias visibles y registradas.
- **CA-03:** no iniciar ninguna ejecución sin autorización humana ni exceder deliberadamente el presupuesto aprobado; ante incertidumbre del costo, reservar margen y detener nuevas tareas antes de superar la autorización.
- **CA-04:** guardar la configuración de la ejecución y mantenerla fija mientras se ejecuta; habilitar una nueva ejecución con otra configuración.
- **CA-05:** si `BASE-FIT-013` tiene una incidencia no crítica, permitir que continúen las tareas independientes de `BASE-FIT-010` y `BASE-FIT-012`.
- **CA-06:** permitir una ejecución concluida con limitaciones sin clasificar una Product Base como comercialmente descartada solo por falta de datos.
- **CA-07:** preservar evidencias, resultados y bitácora de una ejecución al crear otra; no sobrescribir su historial.
- **CA-08:** mantener la misión abierta hasta decisión explícita del Founder, incluso si la IA recomienda cerrarla.
- **CA-09:** poder inspeccionar las fuentes y fundamentos de cada conclusión desde la experiencia de supervisión, aunque el Cockpit inicial sea mínimo.
- **CA-10:** la reproducción histórica no debe abrir `F14` ni desencadenar actividades de sourcing, compras o homologación.

## 6. Propuestas todavía no aprobadas: detalles a resolver

Estos puntos son **preguntas de diseño posteriores**, no decisiones ya tomadas:

1. Catálogo definitivo de estados de ejecución y misión, y sus transiciones exactas (por ejemplo, pausa, fallo y cancelación).
2. Política de reintentos, límites de recuperación y criterios concretos de criticidad de incidentes.
3. Cómo estimar, reservar, conciliar y mostrar costos de IA y herramientas en tiempo real.
4. Formato mínimo de evidencia importada y mecanismo para aislar conclusiones históricas durante el ensayo.
5. Experiencia exacta del Cockpit para observaciones, cambios y resolución de excepciones.
6. Arquitectura del backend, base de datos, orquestación, agentes y adaptación del Matrix Validator; estas decisiones corresponden a diseño técnico posterior.
7. Identificador y ruta documentales finales: comprobar disponibilidad y coherencia con los índices del repositorio antes de incorporar.

## 7. Relación con la hoja de ruta

1. **Bloque 1 (este documento):** objetivo de misión, ejecuciones, Preflight, incidencias, finalización y gobierno.
2. **Bloque 2:** comportamiento del proceso de investigación y sus agentes.
3. **Bloque 3:** memoria comercial y evidencias.
4. **Bloque 4:** evaluación, validaciones y conclusiones.
5. **Bloque 5:** Cockpit, observabilidad y participación humana.

Una vez consolidado el diseño funcional, se prepararán encargos pequeños, con criterios de aceptación y pruebas, para la **IA implementadora (Claude Code)**. El código, los diffs y las pruebas serán revisados antes de cualquier integración aprobada por el Founder.

## 8. Documentos relacionados

- `SI-V3-VISION-001 v0.2.1` — Visión y alcance inicial de Smart Imports v3.
- `SI-DOC-001 v0.2.0` — Estándar documental.
- `SI-ROADMAP-002` — Estado operativo y handoff del proyecto.
- Expediente e investigaciones de `BRAND-CAND-009`, con `SI-RESEARCH-123` (F6) y `SI-RESEARCH-130` (F13), entre otras fuentes históricas.

## 9. Changelog

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-10-22 | Primer borrador del Bloque 1: DF-MVP-001 a DF-MVP-006, flujo funcional, criterios de aceptación y cuestiones abiertas. |
