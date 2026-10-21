---
id: si-v3-vision-001
title: "Smart Imports v3 — Product Vision and Initial Scope"
description: "Visión funcional de la plataforma, principios acordados, primer circuito verificable y estrategia de validación."
version: 0.2.1
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: "2026-10-21"
updated: "2026-10-21"
language: es
scope: "Visión funcional, principios, MVP, validación y evolución"
tags:
  - smart-imports
  - v3
  - vision
  - ai-agents
  - business-intelligence
related:
  - si-doc-001
  - si-roadmap-002
  - si-research-123
  - si-research-130
audience:
  - founder
  - partner
  - developer
  - assistant
phase: planning
---

# SI-V3-VISION-001 — Smart Imports v3: Visión del producto y alcance inicial

> **Estado:** versión en revisión (no aprobada) de consolidación de decisiones conversadas. No constituye aprobación de arquitectura, inicio de desarrollo, autorización de gastos, apertura de F14 ni modificación del cierre histórico de Method v2.
>
> **Propósito del documento:** conservar una referencia compartida para tomar decisiones de producto, definir un primer circuito funcional y, posteriormente, diseñar e implementar la solución sin perder el objetivo comercial.

## 1. Visión y propósito

**Smart Imports v3 será una plataforma de inteligencia comercial impulsada por IA, capaz de descubrir, investigar, comparar y fundamentar oportunidades de negocio con autonomía operativa, supervisión humana, trazabilidad y control económico.**

Smart Imports no busca ser solamente un importador que revende productos. Su diferenciación aspiracional combina selección de oportunidades, construcción de marcas, importación, comercio electrónico, automatización, agentes de IA y software propio. **La IA debe generar una ventaja competitiva real**, no funcionar como un complemento decorativo.

La plataforma debe mejorar la calidad y velocidad de las decisiones comerciales y acumular conocimiento aprovechable en nuevas investigaciones. Hoy el proyecto se encuentra en una etapa de investigación y construcción, sin ingresos atribuibles a la plataforma: el gasto tecnológico debe ser responsable, pero no debe imponer un techo artificial al potencial futuro del producto.

### Resultado esperado

Pasar de un proceso intensivo en tareas manuales, archivos y checkpoints a un **sistema de misiones autónomas**, con revisión estratégica del Founder y evidencias que permitan defender o cuestionar cada conclusión.

## 2. Punto de partida: Method v2

Method v2 deja activos importantes: marco metodológico, investigaciones históricas, evaluaciones de productos, vínculos entre fuentes y evidencias, matrices, decisiones documentadas y un Matrix Validator determinístico en TypeScript.

El proceso anterior aportó rigor, pero evidenció fricciones:

- Investigación predominantemente secuencial de un candidato por vez.
- Capturas y registros frecuentes realizados manualmente.
- Versionado sucesivo de archivos XLSX, scripts de materialización y validación, logs y checkpoints.
- Repetición de análisis o informes cuando una dependencia externa seguía sin resolverse.
- Intervención humana excesiva en operaciones de bajo valor estratégico.

**Method v2 no se descarta ni se reescribe históricamente.** Sus reglas, principios de integridad y trazabilidad son insumos para v3; su secuencia F0–F13 no tiene que reproducirse de manera rígida. La revisión externa y las decisiones comerciales vinculadas con F14 permanecen fuera del alcance de este documento.

## 3. Principios de producto acordados

1. **IA como ventaja competitiva:** priorizar investigación comercial útil, fundamentada y escalable.
2. **Autonomía supervisada:** los agentes ejecutan tareas operativas; las decisiones estratégicas relevantes corresponden al usuario.
3. **Rigor sin rigidez:** conservar reglas determinísticas y evidencia, con ejecución flexible, paralela y orientada a dependencias.
4. **Observabilidad activa:** poder conocer qué se hizo, por qué, cuánto costó e intervenir cuando algo no parece correcto.
5. **Memoria comercial compartida:** cada misión aporta conocimiento que futuras misiones pueden reutilizar, sujeto a vigencia y contexto.
6. **Reversibilidad y trazabilidad:** preservar versiones, motivos, decisiones, correcciones y descartes; no borrar silenciosamente el historial.
7. **Incertidumbre explícita:** ausencia de evidencia no implica evidencia negativa; no inventar datos faltantes, costos, márgenes ni ROI.
8. **Control económico:** ningún agente debe decidir unilateralmente ampliar el gasto autorizado.
9. **Complejidad justificada:** empezar con capacidades suficientes para verificar valor; agregar complejidad sólo donde aporte beneficios concretos.
10. **Construcción incremental de punta a punta:** probar pronto el núcleo de inteligencia comercial antes de completar toda la plataforma.

## 4. Modelo de misiones

### 4.1. Cómo se inicia una misión

La visión contempla tres puertas de entrada que comparten un núcleo de ejecución:

- **Por territorio de marca:** por ejemplo, Marca Hogar.
- **Por problema del cliente:** por ejemplo, dificultades derivadas del sedentarismo.
- **Exploración comercial abierta:** a partir de mercado, capital disponible, riesgos y restricciones.

Al inicio, las misiones son **iniciadas por el usuario**. Un radar persistente que proponga misiones por iniciativa propia queda como evolución futura.

### 4.2. Investigación como embudo de oportunidades

La plataforma debe poder investigar **múltiples oportunidades simultáneamente**:

1. Descubrimiento amplio de soluciones y problemas.
2. Filtro preliminar de señales comerciales y riesgos.
3. Comparación de candidatas prometedoras.
4. **Revisión estratégica humana** para decidir cuáles justifican investigación profunda.
5. Investigación profunda adaptativa y presentación de resultados con incertidumbres y condiciones.

No se presupone una cantidad fija de oportunidades por etapa. Los agentes pueden reorganizar, paralelizar o evitar tareas redundantes, sujetos a reglas de integridad y alcance autorizado.

### 4.3. Resultados del filtro preliminar

- **PROMOVER:** señales suficientes para una consideración posterior.
- **ARCHIVAR (reversible):** descarte preliminar fundamentado con reglas, evidencias, confianza, fecha y motivo; puede reabrirse.
- **INDETERMINADO:** información insuficiente o contradictoria; se preserva la incógnita y lo necesario para resolverla.

Los descartes preliminares fundamentados pueden ejecutarse automáticamente y sin autorización individual. La decisión humana se concentra en el paso a investigación profunda y en otras decisiones estratégicas.

### 4.4. Oportunidades emergentes

Si aparece un hallazgo fuera del alcance de una misión, la plataforma podrá:

- Guardarlo en la memoria compartida.
- Realizar una **exploración rápida de costo/esfuerzo acotado**, si las reglas y el presupuesto vigente lo permiten.
- Proponer una nueva misión cuando exista una señal prometedora.

**No abre automáticamente una investigación profunda independiente** ni distrae recursos ilimitados de la misión original.

## 5. Memoria comercial compartida

La **fuente de verdad operativa de v3 será una base de conocimiento central**, con PostgreSQL como orientación tecnológica inicial. Las matrices XLSX y Google Sheets pasarán a funcionar como vistas, exportaciones o mecanismos de transición, no como núcleo transaccional.

La memoria distinguirá:

1. **Entidades y relaciones:** productos, Product Bases, problemas, soluciones, fabricantes, intermediarios, publicaciones, competidores, misiones y vínculos entre ellos.
2. **Evidencias verificables:** origen, URL o referencia, captura o documento cuando corresponda, fecha, observación, procedencia, vigencia y calidad de verificación.
3. **Evaluaciones contextualizadas:** hipótesis, puntuaciones, riesgos y decisiones asociadas a objetivos de misión específicos.

**Reutilizar evidencia no implica reutilizar automáticamente una conclusión comercial.** Un mismo producto puede resultar descartado en una misión y prometedor en otra.

Las evidencias antiguas no se sustituyen silenciosamente: se conservan para auditoría, con actualización y control de vigencia cuando corresponda. La información duplicada debe poder reconocerse sin destruir su origen documental.

## 6. Agentes, recolección y gobernanza

### 6.1. Responsabilidades conceptuales

- **Agentes de investigación:** búsqueda, análisis de demanda, competencia, origen/proveedores, riesgos y otras especialidades que se justifiquen.
- **Orquestación:** planificación de tareas, dependencias, paralelismo, reintentos y recuperación.
- **Motor de gobernanza:** reglas determinísticas, consistencia de datos, integridad, trazabilidad, controles de calidad y autorizaciones.
- **Cockpit:** estado de misiones, oportunidades, rankings, intervenciones, evidencias, costos y decisiones.

Estas son **responsabilidades funcionales**, no una exigencia de implementar un microservicio o un agente separado por cada nombre.

### 6.2. Recolección autónoma con recuperación asistida

El comportamiento objetivo es:

1. Buscar fuentes y obtener información cuando el acceso lo permita.
2. Extraer y contrastar datos, conservando procedencia y evidencias disponibles.
3. Registrar claramente información no verificable, contradicciones, duplicados y lagunas.
4. Intentar alternativas permitidas antes de escalar.
5. Pedir al usuario una acción **concreta y excepcional** cuando sea necesaria una verificación humana.
6. Reanudar la tarea desde su checkpoint sin repetir los trabajos ya finalizados.

Debe respetar condiciones de uso, restricciones técnicas y autorizaciones de las fuentes; una fuente inaccesible no habilita a fabricar una prueba ni a eludir controles de acceso.

## 7. Cockpit y observabilidad activa

Se contemplan **tres niveles complementarios**:

| Nivel | Pregunta que responde | Contenido principal |
| --- | --- | --- |
| Ejecutivo | ¿Qué está pasando? | Misiones, estado, oportunidades, bloqueos, gasto y decisiones pendientes. |
| Bitácora inteligente | ¿Qué hizo y por qué? | Actividades, fuentes, hallazgos, validaciones, descartes, cambios y justificaciones. |
| Diagnóstico técnico | ¿Cómo se ejecutó? | Herramientas, agentes, tiempos, errores, reintentos, consumo y trazas técnicas. |

El Cockpit debe ofrecer un **ranking de recomendaciones de IA**, una **vista de portfolio** y una **interfaz conversacional** que permitan comparar oportunidades y cuestionar evaluaciones. La recomendación de la IA y la decisión del Founder quedan diferenciadas y trazadas.

### Intervención desde la bitácora

El usuario podrá identificar un evento, dato, evidencia o conclusión y escribir una observación contextualizada. El sistema debe evaluar el comentario, revisar las dependencias afectadas y proponer o ejecutar las correcciones autorizadas, preservando el historial.

Una observación humana **no reemplaza automáticamente la evidencia**. Ante incertidumbre, el resultado puede mantenerse indeterminado; ante riesgo serio, se detiene o aísla el proceso afectado sin bloquear indiscriminadamente el resto.

## 8. Autodiagnóstico, autocorrección y auditoría inteligente

### 8.1. Autocorrección controlada

La plataforma debe detectar contradicciones, errores estructurales, fuentes obsoletas y conclusiones poco sustentadas. Puede corregir automáticamente aquello que sea **verificable y previamente autorizado**, dejando constancia del cambio.

Cuando la modificación implique una interpretación ambigua, decisiones comerciales, alteración importante de prioridades o riesgo alto, escalará al usuario. El objetivo es **revalidar por impacto**: recalcular o revisar sólo las evaluaciones que dependen de lo cambiado.

### 8.2. Skills opcionales configuradas antes de ejecutar

La **auditoría inteligente adicional** será una capacidad opcional configurable, por ejemplo mediante un interruptor en la configuración de la misión o ejecución.

- **Activada:** una revisión inteligente adicional cuestiona evidencias, inconsistencias y conclusiones relevantes.
- **Desactivada:** se evita ese análisis adicional para economizar recursos.
- **Siempre activos:** integridad, trazabilidad, validaciones obligatorias, controles críticos y límites de autorización.

**La selección de skills queda fija durante una ejecución.** Si el usuario desea otra combinación, espera su conclusión y evalúa una nueva ejecución. La nueva configuración no modifica retroactivamente la anterior. Esto no impide observaciones, intervenciones por errores o paradas críticas durante la ejecución.

Una eventual política de auditoría proporcional al riesgo es una evolución posible, no una complejidad obligatoria del MVP.

## 9. Gobierno de costos y recursos

Se adopta **doble control presupuestario**:

- **Global:** techo autorizado para Smart Imports durante un período definido.
- **Por misión:** asignación máxima para una investigación, contenida dentro de la disponibilidad global.

Los agentes pueden distribuir recursos dentro de ambos límites y priorizar trabajo de mayor utilidad. Ante necesidad de ampliar el presupuesto, deben **explicar qué hallaron, qué incertidumbre resolverán, qué trabajo adicional proponen y su costo estimado**. La ampliación requiere autorización humana explícita.

Al llegar al límite, la misión debe conservar avances y conclusiones parciales, detener de manera controlada las nuevas operaciones de costo y permitir reanudación autorizada. Se deben usar estimaciones, reservas, reconciliación con costos observados y límites preventivos. Dado que algunos proveedores informan consumo con retraso, **el diseño no debe prometer exactitud instantánea o imposibilidad absoluta de pequeños desvíos sin mecanismos técnicos comprobados**.

La eficiencia se evalúa por **valor de la investigación por unidad de esfuerzo**, no sólo por reducción de tokens. Reutilizar memoria, evitar duplicaciones y asignar profundidad según potencial son mecanismos centrales de economía. Los límites concretos en USD y los umbrales de alerta todavía no están definidos.

## 10. Arquitectura tecnológica: orientación, no decisión final

Se privilegiará el stack ya conocido:

| Necesidad | Orientación inicial |
| --- | --- |
| Cockpit web | React + Next.js + TypeScript |
| Backend / servicios de misión | Node.js + TypeScript; NestJS a evaluar |
| Fuente de verdad | PostgreSQL + Prisma |
| Reglas determinísticas | Reutilización/adaptación del Matrix Validator TypeScript existente |
| IA / análisis y agentes | OpenAI API y componentes especializados según necesidad |
| Automatizaciones | n8n cuando aporte ventajas operativas claras |
| Testing y operación | Vitest/Jest, pnpm, Git/GitHub, Docker |

Se evitarán incorporaciones prematuras de bases de datos, proveedores, frameworks de agentes o infraestructura que no respondan a una necesidad demostrable. **No quedan decididos** topología de despliegue, colas, modelo de datos detallado, herramientas exactas de navegación, framework de agentes ni costos de proveedores.

## 11. Estrategia de implementación: primer circuito de punta a punta

No construiremos toda la plataforma antes de validar su inteligencia comercial. Se desarrollará un **circuito vertical reducido, completo y ampliable**, evitando una maqueta puramente visual o una aplicación descartable.

### Caso de referencia seleccionado

**BRAND-CAND-009 — Mundo Fitness**, con investigación histórica documentada mediante Method v2, será el primer banco de pruebas. **No se reproducirá todo el candidato inicialmente**: se seleccionará una muestra representativa de Product Bases y evidencias según la documentación real.

La muestra debería permitir comparar estos tipos de resultados, presentes con distintos matices en las Product Bases documentadas:

- Una oportunidad relativamente prometedora.
- Una oportunidad archivada o descartada con fundamento.
- Una oportunidad con evidencia insuficiente o incertidumbre.

A partir de la documentación de cierre de F13 y la validación de `aut171`, se dispone de los siguientes casos reales para **proponer** la muestra inicial (selección aún por aprobar):

| Caso de prueba propuesto | Resolución histórica F13 | Qué permite poner a prueba |
| --- | --- | --- |
| `BASE-FIT-010` — cinta de elongación con bucles | `FINALIST — CONDITIONED / EXTERNAL PORTFOLIO REVIEW ONLY` | Evaluación favorable pero condicionada: distinguir potencial de viabilidad comercial o margen probado. |
| `BASE-FIT-012` — disco inflable texturado | `NOT COMMERCIAL FINALIST — SAFETY-GATED` | Identificar un riesgo de seguridad que impide promover comercialmente una oportunidad a pesar de señales de mercado. |
| `BASE-FIT-013` — tabla Freeman | `DEFER — REOPENABLE / NOT SHORTLISTED` | Distinguir una oportunidad diferida/reabrible de un descarte definitivo, sin inventar evidencia de origen. |

`BASE-FIT-011` — plataforma inclinada regulable (`SECONDARY RESERVE — CONDITIONED`) queda como posible cuarto caso si aporta diversidad analítica al ensayo. **Estas resoluciones son decisiones históricas de v2**, no resultados de v3 ni recomendaciones comerciales actuales.

La propuesta se fundamenta en `SI-RESEARCH-123` (F6), `SI-RESEARCH-130` (F13) y el doble PASS de `aut171`; el borrador de F13 previo a la ejecución conservaba metadatos `PENDING_DOUBLE_PASS`, pero el log posterior confirmó los dos controles en `PASS`. No se modificarán por ello archivos ni snapshots históricos.

F14 permanece **NOT OPENED** según la gobernanza de v2 y fuera del experimento v3.

### Primer circuito funcional (MVP inicial)

**Incluye, al mínimo verificable:**

1. Crear o configurar una ejecución acotada, con objetivo, skills opcionales y presupuesto autorizado.
2. Incorporar un subconjunto de evidencias históricas de BRAND-CAND-009, con procedencia verificable.
3. Analizar ese material con IA, identificar oportunidades y producir evaluaciones contextualizadas, con incertidumbre explícita.
4. Guardar entidades, evidencias, conclusiones, versiones y eventos en PostgreSQL.
5. Ejecutar controles determinísticos esenciales y registrar resultados.
6. Mostrar oportunidades, fundamentos, bitácora y consumo en un Cockpit sencillo.
7. Permitir una observación humana sobre un hallazgo y registrar su tratamiento.
8. Generar una salida exportable/auditable cuando sea necesario, sin convertir XLSX en fuente central.

En este primer circuito la IA **analiza autónomamente evidencia preexistente**; la búsqueda abierta y captura autónoma de publicaciones actuales es una prueba posterior. No se exige desde el primer día cubrir todos los modos de misión, todos los agentes especializados o todo el método F0–F13.

### Secuencia de validación acordada

**Prueba 1 — Reproducción histórica:** analizar evidencias conocidas sin asumir que las conclusiones anteriores sean infalibles. Verificar razonamiento, trazabilidad, controles y datos.

**Prueba 2 — Reinvestigación autónoma:** entregar el objetivo original sin sus resultados; investigar con fuentes actuales, contrastar diferencias y medir intervención humana y costos.

**Prueba 3 — Nueva misión:** una investigación no utilizada durante el desarrollo, para demostrar valor fuera de los ejemplos históricos.

La prueba 2 requiere incorporar recolección y recuperación asistida; la prueba 3 amplía el alcance funcional. Ninguna debe convertirse en una reproducción interminable de Method v2.

## 12. Cómo sabremos si v3 aporta valor

| Dimensión | Evidencia de mejora a observar |
| --- | --- |
| Autonomía | Menos acciones humanas repetitivas por investigación; intervenciones concentradas en excepciones y decisiones. |
| Agilidad | Menor tiempo de extremo a extremo, mayor paralelismo útil y menos reprocesamiento. |
| Calidad | Evidencia verificable, incertidumbre bien expresada, consistencia y capacidad de sostener conclusiones. |
| Trazabilidad | Cada resultado importante enlazable con su fuente, evaluación, versión y decisión. |
| Costo | Gasto real/estimado por misión, etapa y hallazgo útil, bajo presupuesto autorizado. |
| Memoria | Porcentaje de conocimiento reutilizado y reducción de trabajo duplicado. |

Los objetivos numéricos y umbrales de aceptación se definirán cuando exista una línea de base comparable. **No buscamos coincidencia literal con v2:** una diferencia bien explicada y respaldada puede representar una mejora.

## 13. Capacidades posteriores al primer MVP

La evolución contempla, según resultados de las pruebas y prioridades:

- Recolección autónoma de fuentes actuales con recuperación asistida.
- Embudos de investigación simultánea de múltiples oportunidades.
- Modos de inicio por territorio, problema y exploración abierta.
- Portfolio visual, ranking justificado y conversación integrados con mayor profundidad.
- Agentes y skills especializados adicionales cuando generen valor medible.
- Reutilización y actualización de conocimiento entre misiones.
- Exploración rápida de oportunidades inesperadas y propuestas de nuevas misiones.
- Auditoría inteligente ajustada por riesgo y revalidación por impacto más avanzada.
- Radar persistente de oportunidades como etapa futura, **no requisito del MVP inicial**.
- Mejora de presupuestos, estimación y medición de valor a medida que exista actividad comercial.

## 14. Fuera del alcance y salvaguardas

- No se habilitan compras, RFQ formales, contratación de proveedores, envíos de muestras o compromisos financieros comerciales por el solo hecho de crear v3.
- No se suplen con IA dictámenes de despachante, requisitos regulatorios, homologación, seguridad de producto, costos landed verificables ni decisiones del socio/Founder.
- No se modifican resultados ni decisiones históricas de Method v2 para hacer coincidir la prueba con v3.
- No se incorporan automáticamente documentos privados, matrices, logs, capturas o credenciales al repositorio público.
- No se presume que una fuente pueda consultarse, capturarse, reutilizarse o almacenarse sin restricciones.
- No se confunden conclusiones de IA, datos verificados, hipótesis y decisiones humanas.

## 15. Asuntos abiertos, deliberadamente no decididos

1. Selección exacta de Product Bases y evidencias de BRAND-CAND-009 para el primer ensayo.
2. Indicadores cuantitativos, línea de base y criterios de aprobación de cada prueba.
3. Presupuestos iniciales, moneda, período de control global, reservas, umbrales de alerta y reporte de costos.
4. Modelo de datos y mecanismos precisos de procedencia, versiones, deduplicación y vigencia.
5. Mecanismo concreto para adaptar el Validator de XLSX a reglas sobre PostgreSQL sin perder cobertura crítica.
6. Orquestación técnica de ejecuciones largas, reintentos, checkpoints, concurrencia e idempotencia.
7. Acceso autorizado a marketplaces, tratamiento de capturas/documentos y política de retención.
8. Controles de privacidad y seguridad, roles, respaldos y operación del Cockpit.
9. Alcance y contrato técnico de cada skill, agente y auditor inteligente.
10. Arquitectura física, alojamiento, despliegue, proveedores y gasto operativo.
11. Plan gradual de migración/importación de la memoria histórica, sin contaminar el registro canónico.
12. Registro en índices y referencias de navegación del repositorio, a resolver en el checkpoint de publicación.

## 16. Gobierno del documento y siguiente paso

Este documento es una **propuesta de consolidación funcional, versión 0.2.1 en estado `review`**, todavía pendiente de aprobación documental explícita.

**Verificación de continuidad (21/10/2026):** el preflight de solo lectura sobre `main` local, `HEAD d6e9df5`, finalizó **PASS, 0 errores y 0 advertencias**. Se confirmaron `SI-DOC-001 v0.2.0`, `SI-ROADMAP-002 v1.23.16`, `SI-RESEARCH-123` (F6), `SI-RESEARCH-130` (F13), la carpeta `docs/00-vision/` y la ausencia de colisiones para la ruta `docs/00-vision/si-v3-vision-001-product-vision-and-initial-scope.md` y el ID `si-v3-vision-001`. La comparación de commits entre `main` y `origin/main` fue **local y sin `fetch`**: no certifica el estado remoto actual.

El checkpoint confirmó **F0–F13 CLOSED, F14 NOT OPENED**, la shortlist histórica condicionada y el doble PASS de `aut171`. Los documentos históricos pueden contener anotaciones de estados intermedios; no deben reescribirse para hacerlos coincidir con el cierre posterior. El referente de continuidad es el checkpoint publicado en `SI-ROADMAP-002` y el commit de cierre indicado.

Orden de trabajo propuesto:

1. Incorporar sólo este Markdown nuevo en la ruta verificada, sin alterar archivos de Method v2 ni el índice de Git, y revisar el cambio resultante.
2. Resolver la revisión documental y los enlaces de navegación/índices necesarios, sin mezclar decisiones técnicas todavía abiertas con hechos ya aprobados.
3. Solicitar aprobación expresa antes de cualquier `git add`, `commit` o `push`. Conservar matrices, PDFs, logs y capturas privadas fuera del repositorio público.
4. Luego del cierre documental, comenzar la definición funcional y técnica detallada del primer circuito, de manera incremental.

**Criterio rector:** Smart Imports debe apoyarse en la IA para generar una ventaja comercial sostenible; el software, los agentes y las automatizaciones tienen sentido en la medida en que ayudan a investigar y decidir mejor, con control de costos y evidencia defendible.


## 17. Documentos relacionados

- [SI-DOC-001 — Documentation Standards](../standards/si-doc-001-documentation-standards.md) — estándar de formato, metadatos, nomenclatura, estados y versionado.
- [SI-ROADMAP-002 — Estado actual y handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md) — continuidad operativa de Method v2.
- [SI-RESEARCH-123 — BRAND-CAND-009, F6](../06-research/brand-fitness/si-research-123-brand-cand-009-method-v2-agile-phase-6-product-bases.md) — definición de las cuatro Product Bases.
- [SI-RESEARCH-130 — BRAND-CAND-009, F13](../06-research/brand-fitness/si-research-130-brand-cand-009-method-v2-agile-phase-13-final-shortlist.md) — resoluciones históricas y restricciones de seguridad y evaluación externa.

> Los resultados de validación del snapshot `aut171` se comprobaron con el log privado original. El log, los XLSX y los PDF no deben publicarse en el repositorio.

## 18. Changelog

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-10-21 | Primer borrador de consolidación de visión, principios, MVP y evolución. |
| 0.2.0 | 2026-10-21 | Revisión documental preliminar, muestra histórica fundamentada en `BRAND-CAND-009`, metadatos y estructura alineados con la copia disponible de `SI-DOC-001 v0.2.0`. Pendiente contraste final con la rama `main` vigente. |
| 0.2.1 | 2026-10-21 | Preflight documental de `main` local `d6e9df5` confirmado; ruta e ID libres, referencias canónicas verificadas, estado `review` y eliminación de pendientes ya resueltos. |
