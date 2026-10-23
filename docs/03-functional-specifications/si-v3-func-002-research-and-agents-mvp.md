---
id: si-v3-func-002
title: "Smart Imports v3 — Research and Agents Functional Design (MVP)"
description: "Consolidación funcional del Bloque 2: investigación, agente, coordinación, evidencias, gobernanza, auditoría y validación del primer circuito histórico."
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: "2026-10-22"
updated: "2026-10-22"
language: es
scope: "Bloque 2 — Investigación y Agentes; reproducción histórica inicial y reglas de evolución"
tags:
  - smart-imports-v3
  - functional-design
  - mvp
  - research
  - ai-agents
  - governance
related:
  - si-v3-vision-001
  - si-v3-func-001
  - si-doc-001
  - si-research-123
  - si-research-130
audience:
  - founder
  - partner
  - developer
  - assistant
phase: design
---

# SI-V3-FUNC-002 — Diseño funcional del MVP: investigación y agentes

> **Estado documental:** `draft`, pendiente de revisión documental y aprobación formal. Las decisiones `DF-AG-001` a `DF-AG-016` y las reconciliaciones H1–H3 fueron **acordadas funcionalmente por el Founder en conversación**, pero este documento no implica que la plataforma esté implementada, que el documento tenga estado `approved`, que se autorice gasto ni que se haya abierto `F14`.

## 1. Propósito y fuentes de autoridad

Consolidar el **Bloque 2 — Investigación y Agentes** del diseño funcional de Smart Imports v3. Describe comportamientos y responsabilidades para el primer circuito de investigación comercial asistida por IA, sin fijar una arquitectura física, un proveedor de modelos, prompts, tablas, APIs ni una interfaz definitiva.

**Jerarquía y compatibilidad documental:**

1. `SI-V3-VISION-001 v0.2.1` define el objetivo de producto, las salvaguardas y el alcance mínimo de validación.
2. `SI-V3-FUNC-001 v0.1.0` establece las decisiones `DF-MVP-001..006` y los criterios de aceptación `CA-01..CA-10`; este documento los **complementa, no los reemplaza**.
3. `SI-DOC-001 v0.2.0` rige identificación, metadatos, idioma, estructura, versionado y estado documental.
4. `SI-RESEARCH-123` (F6) y `SI-RESEARCH-130` (F13), junto con el material privado correspondiente, son referencias históricas que **no se entregan al investigador como respuestas** durante la prueba a ciegas.

Ante contradicciones con fuentes canónicas vigentes, corresponde revisión del Founder antes de cambiar reglas o implementar.

## 2. Alcance y fronteras

### 2.1 Primer circuito: reproducción histórica

- Referencia: `BRAND-CAND-009`, con Method v2 `F0–F13 CLOSED` y `F14 NOT OPENED`.
- Product Bases de prueba: `BASE-FIT-010`, `BASE-FIT-012` y `BASE-FIT-013`. `BASE-FIT-011` queda fuera de la muestra inicial por defecto.
- Modalidad: analizar evidencias históricas **preexistentes, controladas y cerradas**, sin entregar conclusiones ni clasificaciones previas de Method v2 al investigador o al auditor inteligente antes de congelar los resultados.
- Resultado buscado: evaluar **razonamiento, evidencia, incertidumbre, trazabilidad, supervisión y costo**, y después contrastar con la referencia histórica.
- No se realizan búsquedas abiertas, RFQ, contactos, negociación, muestras, compras, homologación, dictámenes de viabilidad regulatoria ni decisiones de importación.

### 2.2 Evolución posterior

La segunda prueba será una **reinvestigación autónoma** con fuentes actuales; la tercera, una **misión nueva**. En la investigación autónoma podrá incorporarse evidencia de manera dinámica dentro de permisos, presupuesto y controles. Esta evolución no habilita por sí sola `F14` ni gastos comerciales.

### 2.3 Autoridad y separación de responsabilidades

| Actor o función | Responsabilidad funcional | Límite |
|---|---|---|
| **Founder / Product Owner** | Define prioridades, autoriza inicio y ampliaciones; resuelve decisiones estratégicas y cierre de misión. | No necesita aprobar cada tarea automática ni cada recomendación preliminar reversible. |
| **Coordinador determinístico** | Preflight, ejecución del plan, dependencias, autorización operativa dentro de límites, presupuestos, incidencias, eventos y revalidaciones. | No inventa criterios comerciales ni amplía unilateralmente alcance o presupuesto. |
| **Investigador IA (rol único)** | Analiza, interpreta, compara, identifica contradicciones, expresa incertidumbre y recomienda. Puede desempeñar tareas diferenciadas, no implica agentes especializados separados. | No declara hechos no verificados, no resuelve por sí mismo cuestiones estratégicas, regulatorias o comerciales reservadas. |
| **Validadores determinísticos** | Exigen estructura, integridad, identidad, restricciones, referencias y trazabilidad. | Un `PASS` estructural **no demuestra verdad factual ni calidad comercial**. |
| **Auditoría inteligente opcional** | Si fue habilitada antes del inicio, cuestiona selectivamente hallazgos y recomendaciones relevantes. | No reemplaza controles obligatorios ni es una verificación independiente garantizada. |

## 3. Registro consolidado de decisiones funcionales

| ID | Acuerdo funcional | Condición esencial |
|---|---|---|
| `DF-AG-001` | Un único **rol investigador** con coordinador y validadores determinísticos. | No crear múltiples agentes especializados como prerrequisito del primer circuito. |
| `DF-AG-002` | IA interpreta/compara/recomienda; sistema controla/valida/registra; Founder conserva decisiones estratégicas. | Validación estructural no es validación factual. |
| `DF-AG-003` | Hallazgos **estructurados**, con evidencia vinculada, incertidumbres y síntesis comercial. | No sustituirlos por un informe narrativo opaco. |
| `DF-AG-004` | Investigación individual por Product Base y comparación comercial posterior. | Resultados independientes; evidencia compartible sin copiar conclusiones automáticamente. |
| `DF-AG-005` | Recomendaciones `PROMOVER`, `ARCHIVAR`, `INDETERMINADO`, justificadas y reversibles cuando corresponda. | Datos insuficientes o contradictorios no equivalen por sí solos a un descarte. |
| `DF-AG-006` | Planificación **híbrida controlada**: IA propone; coordinador decide ajustes operativos dentro de autorizaciones. | Ampliaciones fuera de límites requieren Founder; configuración base inmutable (H1). |
| `DF-AG-007` | Paralelismo condicionado por dependencias, aislamiento de incidencias y comparación con cobertura explícita. | No inferir inferioridad comercial por una falla operativa. |
| `DF-AG-008` | Recuperación selectiva, reintentos fundamentados y finalización con resultados parciales. | No reintentos ilimitados; distinguir fallo de tarea de recomendación comercial. |
| `DF-AG-009` | Control de costos **preventivo**, reservas y conciliación posterior. | Respeto simultáneo de límites; aumentos solo con autorización humana. |
| `DF-AG-010` | Cockpit con observabilidad por niveles, decisiones trazables e intervenciones explícitas. | La intervención humana es transversal; no confundir progreso con calidad. |
| `DF-AG-011` | Intervención humana localizada y continuidad de tareas independientes. | Autorizaciones explícitas, limitadas, auditables; suspensión global si corresponde. |
| `DF-AG-012` | Autocorrección por impacto: reparación verificable, revisión comercial versionada y escalamiento cuando proceda. | No sobrescribir fuentes ni decisiones humanas; aplicar H2. |
| `DF-AG-013` | Auditoría inteligente **opcional y selectiva por riesgo**, presupuesto y trazabilidad. | Selección fija antes de ejecutar; validadores obligatorios siempre activos. |
| `DF-AG-014` | Evaluación multidimensional, reproducción histórica a ciegas, congelación y contraste posterior con v2. | La coincidencia con v2 no es el único criterio de calidad. |
| `DF-AG-015` | Aceptación mediante condiciones críticas obligatorias y evaluación de calidad comercial. | El Founder decide avanzar; no basta un `PASS` técnico. |
| `DF-AG-016` | Contrato de entrada y gestión de evidencias identificables, versionadas y reproducibles. | Corpus cerrado y aislado en prueba histórica; crecimiento autorizado en modo autónomo. |

### 3.1 Ejecución del investigador (`DF-AG-001..005`)

El investigador trabaja sobre tareas de análisis acotadas. Para cada Product Base produce **hallazgos individuales** y una **síntesis comercial**; la comparación se ejecuta después de disponer de resultados o limitaciones documentadas para las investigaciones participantes. Se permite reutilizar fuentes entre productos preservando sus interpretaciones contextualizadas.

Las recomendaciones significan:

- `PROMOVER`: existen fundamentos para considerar la oportunidad en una etapa posterior; **no aprueba importar, invertir ni confirma margen o rentabilidad**.
- `ARCHIVAR`: existen motivos suficientes para no priorizarla en el contexto actual; la decisión preliminar es **reversible y justificada**.
- `INDETERMINADO`: evidencia insuficiente, contradictoria o incapaz de sostener otra recomendación; se documenta qué falta y qué permitiría avanzar.

Son **recomendaciones comerciales**, no estados operativos (`READY`, `BLOCKED`, tarea fallida, ejecución completada) ni decisiones estratégicas finales.

### 3.2 Planificación, dependencias y recuperación (`DF-AG-006..008`)

El coordinador prepara tareas y dependencias bajo el alcance autorizado. La IA puede **proponer** tareas adicionales, cambios de orden o revisiones cuando surjan evidencias o dificultades. El coordinador puede aceptar cambios operativos compatibles con permisos y reservas presupuestarias, conservando el motivo y los efectos.

Las tareas independientes pueden ejecutarse en paralelo cuando exista capacidad y autorización suficientes. Una tarea dependiente espera hasta que sus entradas estén disponibles o su cobertura parcial sea explícitamente admisible. Una incidencia localizada no detiene trabajo independiente seguro; una afectación global de integridad, seguridad o validez exige detener el trabajo correspondiente.

**Resultados funcionales propuestos para tareas** (etiquetas de referencia, **no catálogo técnico definitivo**): `COMPLETADA`, `COMPLETADA CON LIMITACIONES`, `NO COMPLETADA`, `REQUIERE INTERVENCIÓN`. Una tarea completada puede recomendar `INDETERMINADO` sin representar una falla.

Solo se reintenta cuando cambia algo que hace razonable esperar una mejora, el intento queda justificado y los límites permiten pagarlo. Deben preservarse hallazgos y resultados parciales válidos. El catálogo de estados y las políticas numéricas de reintentos siguen abiertos.

### 3.3 Presupuesto y autorizaciones (`DF-AG-009`, `DF-AG-011`)

Antes de iniciar una tarea o reintento, el coordinador considera **consumo registrado + compromisos reservados + estimación prudente de la nueva operación**, contrastados con los límites autorizados globales y los de misión/ejecución que correspondan.

Las ampliaciones requieren solicitud fundamentada al Founder, con trabajo pendiente, beneficio informativo esperado, costo aproximado e incertidumbre. Una autorización se circunscribe a **qué, cuánto y dónde** permite cambiar; no implica permisos generales. El consumo real se concilia posteriormente con las reservas. Los costos tardíos de proveedores impiden prometer gasto perfectamente instantáneo o imposibilidad absoluta de desvíos sin mecanismos técnicos comprobados.

Una intervención puede ser **autorizar, rechazar o posponer**, con registro de quién, cuándo, motivo, límites y efectos. La ausencia de respuesta no autoriza nada. Por defecto se suspende solo el trabajo dependiente de esa intervención; se detiene globalmente cuando exista riesgo sistémico.

### 3.4 Cockpit y observabilidad (`DF-AG-010`)

Se respetan **tres niveles** de la visión: (1) ejecutivo, (2) bitácora inteligible y (3) diagnóstico técnico. **Las intervenciones humanas son transversales** a esos niveles, no un cuarto nivel independiente.

El Founder puede identificar el estado de misión/ejecución, Product Bases y tareas; fuentes y fundamentos; observaciones, incidencias y correcciones; presupuesto consumido y comprometido; y solicitudes pendientes con alternativas y consecuencias. La supervisión debe permitir cuestionar un hallazgo y registrar su tratamiento, aunque el Cockpit inicial sea sencillo.

### 3.5 Autocorrección y auditoría (`DF-AG-012..013`)

- **Corrección técnica verificable:** puede automatizarse si preserva el significado y supera controles.
- **Revisión comercial:** puede producir una nueva interpretación o cambiar una recomendación preliminar dentro del alcance autorizado; exige fundamentos, nueva versión, auditoría de cambios y revalidación de dependencias afectadas.
- **Ambigüedad material o decisión estratégica:** se expresa como incertidumbre y se escala cuando resolverla necesita una decisión humana. El investigador no modifica unilateralmente decisiones previas del Founder.
- **Auditoría inteligente opcional:** si está activada al inicio, revisa selectivamente afirmaciones críticas, contradicciones, recomendaciones y consistencia comparativa. Registra objeciones; **no cambia silenciosamente resultados**. Sigue las reglas anteriores de corrección.

La segunda respuesta de un modelo de IA **no certifica por sí misma** la validez factual de una afirmación. Las verificaciones regulatorias, de seguridad y de importación requieren evidencias y competencias adecuadas.

## 4. Reconciliaciones de consistencia aprobadas (H1–H3)

### H1 — Configuración inicial inmutable y cambios operativos controlados

La **configuración base de una ejecución es inmutable**: misión, objetivo, modalidad, capacidades seleccionadas, restricciones, presupuesto inicial e identificación de insumos de partida. El estado efectivo puede evolucionar mediante **eventos y autorizaciones adicionales registradas**, sin alterar retrospectivamente esa base ni los resultados de otras ejecuciones.

- Se admiten reordenamientos, reintentos y otras adaptaciones dentro del alcance aprobado.
- Una ampliación puntual de presupuesto o fuentes que no transforme la modalidad requiere autorización humana delimitada, trazabilidad y comprobación de controles afectados.
- Cambios fundamentales de **modalidad**, selección de **skills opcionales** o condiciones que invaliden el experimento requieren **nueva ejecución**.
- En el ensayo histórico permanecen cerrados el conjunto de evidencias y el aislamiento de las conclusiones de Method v2. Modificarlos exige otra ejecución experimental válida.

Esta precisión complementa, sin eliminar, `DF-MVP-001`, `DF-MVP-002` y `CA-04` de Bloque 1.

### H2 — Autocorrección comercial proporcional al riesgo

El investigador puede corregir datos y actualizar interpretaciones o recomendaciones **preliminares y reversibles** con justificación verificable, nueva versión y revalidación de dependencias. Un cambio de `ARCHIVAR` a `PROMOVER`, o inversamente, **no exige aprobación humana en todos los casos**.

Sí exige tratar explícitamente las ambigüedades materiales, los riesgos relevantes, las autorizaciones nuevas y cualquier reconsideración de una **decisión estratégica ya tomada por el Founder**. La IA no puede anular esa decisión: solo presentar nueva evidencia y proponer revisarla.

### H3 — Primer MVP vertical real y evolución incremental

El primer circuito será **real, persistente, verificable y ampliable**. No se considera necesario implementar ya las versiones avanzadas de todos los comportamientos aprobados; tampoco se los declarará validados sin pruebas.

El MVP requiere un circuito funcional de misión y ejecución, preflight/autorización, investigación real de material histórico, hallazgos trazables, persistencia operativa inicial en PostgreSQL, controles determinísticos críticos, límites de costo, bitácora y Cockpit mínimo, observación humana registrada y resultados auditables/exportables.

Capacidades que pueden madurar después: paralelismo distribuido y optimización avanzada, descubrimiento/captura autónoma de fuentes nuevas, auditoría sofisticada, autocorrección de largas cadenas de dependencias, experiencia visual avanzada, deduplicación/vigencia sofisticadas y agentes especializados adicionales.

**No confundir diseño funcional aprobado con implementación ya demostrada.** Por ejemplo, un coordinador inicialmente secuencial no prueba paralelismo real; una ejecución con auditoría desactivada no prueba que la auditoría selectiva funciona.

## 5. Contratos funcionales de entrada y salida

Los apartados siguientes describen **campos y garantías semánticas**, no esquemas JSON, SQL, clases ni formatos técnicos definitivos.

### 5.1 Entrada mínima de una tarea de investigación

- Identidad de misión, ejecución, tarea y Product Base; objetivo y preguntas por resolver.
- Alcance autorizado, modalidad histórica/autónoma, restricciones, presupuesto/recursos y dependencias.
- Inventario de evidencias utilizables con identificador, procedencia, referencia localizable, fecha y versión/huella disponible; limitaciones de acceso o legibilidad.
- Contexto comercial permitido; criterios de análisis conocidos; configuración original y autorizaciones complementarias aplicables.
- Exclusiones explícitas: qué material no puede consultar ni inferir como si fuera evidencia.

### 5.2 Salida mínima de cada hallazgo (`DF-AG-003`)

- Identificador estable y Product Base/contexto de misión.
- Afirmación o hallazgo y **tipo de contenido**: hecho observado, declaración de tercero, inferencia o hipótesis.
- Evidencia(s) que fundamentan la afirmación, con ubicación verificable y trazabilidad; señalar ausencia de fuente cuando corresponda.
- Procedencia, fecha de captura/publicación cuando se conozca y limitaciones de vigencia o verificación.
- Interpretación comercial e importancia para el objetivo de investigación.
- Contradicciones, incertidumbres, información faltante e impacto posible sobre la recomendación.
- Versión, correcciones previas relacionadas y dependencias de otros resultados.

### 5.3 Salida mínima de la investigación y comparación

Para cada Product Base: síntesis comercial, principales hallazgos rastreables, riesgos, limitaciones, **recomendación** `PROMOVER` / `ARCHIVAR` / `INDETERMINADO` cuando esté fundamentada y condiciones para reconsiderarla. No se exige forzar una recomendación comercial cuando la tarea ni siquiera produjo un análisis utilizable: registrar la incidencia operativa y la cobertura faltante.

Para la comparación: criterios aplicados de manera coherente, evidencias compartidas, cobertura de cada participante, límites de comparabilidad y conclusión contextualizada. Las oportunidades con una investigación fallida o incompleta **no se penalizan por el solo hecho de la falla técnica**.

## 6. Gestión de evidencias: dos modalidades (`DF-AG-016`)

| Atributo | Reproducción histórica (prueba 1) | Investigación autónoma (pruebas posteriores) |
|---|---|---|
| Insumos | Corpus identificado y **cerrado** antes de iniciar. | Contexto y fuentes iniciales identificados; nuevas fuentes permitidas dinámicamente. |
| Acceso a resultados Method v2 | **Prohibido** al investigador y auditor hasta congelación. | Memoria histórica consultable según alcance, diferenciando hechos de decisiones anteriores. |
| Incorporación durante ejecución | No se altera el corpus de la prueba. | Se incorpora evidencia autorizada con fecha, origen, identidad, contexto y registro del uso. |
| Reproducibilidad | Conjunto de entrada y versiones fijados. | Secuencia reproducible de incorporaciones y qué resultados utilizaron cada evidencia. |
| Controles | Preflight, integridad, trazabilidad, privacidad, presupuesto. | Los mismos, más límites de fuentes y restricciones de adquisición y uso. |

**Aislamiento real:** no basta con no copiar la clasificación histórica en el prompt. La prueba requiere impedir que el investigador, sus herramientas y el auditor consulten documentos, tablas, memorias, resúmenes o rutas que revelen directa o indirectamente las conclusiones de v2. Deben registrarse las exclusiones y verificar cobertura imparcial: no seleccionar solo evidencias favorables ni eliminar contradicciones por conveniencia.

**Privacidad documental:** PDFs, XLSX, capturas, logs y respaldos privados no se suben al repositorio público. Solo se versionan especificaciones, referencias y metadatos no sensibles apropiados.

## 7. Circuito funcional del primer experimento

1. **Preparación externa del corpus:** inventariar evidencias privadas de las tres Product Bases, comprobar su legibilidad, procedencia, identidad y exclusiones de conclusiones históricas.
2. **Misión y ejecución:** configurar la reproducción histórica de `BRAND-CAND-009`, dejando fijadas modalidad, capacidades opcionales, presupuesto inicial y alcance.
3. **Preflight:** aplicar `READY`, `READY WITH WARNINGS` o `BLOCKED` según `SI-V3-FUNC-001`, incluido el aislamiento real del corpus; un bloqueo crítico impide iniciar.
4. **Autorización:** el Founder autoriza expresamente el comienzo de la ejecución después del preflight.
5. **Investigación individual:** el único rol investigador analiza `BASE-FIT-010`, `BASE-FIT-012` y `BASE-FIT-013` en tareas separadas; el coordinador administra dependencias, reservas y recuperación.
6. **Controles y revisión:** validaciones determinísticas siempre activas; autocorrección controlada; auditoría inteligente adicional solo cuando se habilitó antes de ejecutar.
7. **Comparación comercial:** contrastar las Product Bases usando hallazgos disponibles, señalando cobertura parcial e incertidumbre; no atribuir resultados negativos por fallas operativas.
8. **Cierre de la ejecución y congelación:** conservar resultados, fuentes, versiones, bitácora, validaciones, autorizaciones, costos y limitaciones en una versión de salida identificable.
9. **Evaluación de calidad:** revisar condiciones críticas y utilidad comercial del trabajo **sin utilizar primero la conclusión histórica como respuesta esperada**.
10. **Comparación externa con v2:** recién entonces revelar a los evaluadores del experimento los resultados históricos y analizar coincidencias y divergencias; conservar la versión v3 congelada.
11. **Decisión del Founder:** determinar si corresponde corregir, repetir el experimento, realizar la prueba de reinvestigación autónoma o mantener abierta la misión. Terminar una ejecución no cierra automáticamente la misión.

## 8. Aceptación y cobertura verificable

### 8.1 Condiciones críticas no compensables (`DF-AG-015`)

- **Prueba ciega íntegra:** los resultados históricos no contaminan investigador ni auditor antes del congelamiento.
- **Trazabilidad y fidelidad:** referencias localizables y diferenciación explícita entre hechos, declaraciones, inferencias e incógnitas; ninguna afirmación sin soporte se presenta como verificada.
- **Gobernanza:** respeto del preflight, autorización humana, restricciones críticas y presupuesto; incidentes sistémicos afectan la ejecución cuando corresponde.
- **Reconstrucción:** entradas, configuraciones, versiones, tareas, correcciones y decisiones quedan asociadas a la ejecución correspondiente.

Un incumplimiento crítico impide declarar el experimento validado, aunque sus etiquetas comerciales coincidan con v2. Las correcciones verificables previas al congelamiento son válidas si preservan el historial y satisfacen controles.

### 8.2 Dimensiones de evaluación (`DF-AG-014`)

1. Fidelidad a las evidencias.
2. Razonamiento comercial y coherencia de interpretaciones.
3. Tratamiento de incertidumbres y contradicciones.
4. Trazabilidad, control e intervenciones.
5. Eficiencia: costo, esfuerzo, reintentos y trabajo redundante en relación con valor informativo.

Los resultados propuestos de la **evaluación del MVP**, distintos de estados operativos y etiquetas de producto, son: `VALIDADO PARA AVANZAR`, `VALIDADO CON LIMITACIONES` y `NO VALIDADO`. Los criterios detallados de comprobación deben definirse **antes** de correr el ensayo. No se aprueban aquí puntuaciones o umbrales arbitrarios sin línea de base.

### 8.3 Relación con los criterios existentes del Bloque 1

`CA-01..CA-10` de `SI-V3-FUNC-001` siguen vigentes íntegramente. Esta consolidación agrega su dimensión investigadora sin eliminar condiciones como: bloqueo al preflight `BLOCKED`, autorización de inicio, preservación entre ejecuciones, continuidad frente a incidente localizado, soporte de resultados parciales, intervención humana y exclusión de `F14`.

**Especial atención:** `CA-04` exige conservar la configuración; H1 precisa que la configuración **original** no cambia, mientras que eventos y autorizaciones adicionales pueden modificar el estado efectivo sin reescribir la base.

### 8.4 Alcance real de la prueba y de los resultados

Una coincidencia con v2 no demuestra que v3 sea comercialmente correcto. Una divergencia fundamentada tampoco es un error automático: Method v2 es una **referencia histórica documentada**, no una verdad económica demostrada. La reproducción histórica por sí sola no acredita precisión frente a mercados actuales, capacidad autónoma de captura ni viabilidad de importación.

## 9. Pendientes deliberadamente abiertos antes de implementar y ejecutar

**Diseño funcional de detalle y pruebas:** catálogo definitivo y transiciones de estados, dependencias, matriz de criticidad, política de reintentos y escalamiento, criterios medibles de aceptación, selección de casos de prueba de incidencias y tratamiento de observaciones.

**Corpus histórico:** inventario real de los archivos privados, clasificación de contenido potencialmente contaminante, acceso autorizado por tarea, controles contra filtración de conclusiones v2 y prueba de reproducibilidad. **No declarar disponible ni limpio un corpus aún no inspeccionado.**

**Control económico:** importes, moneda, período del límite global, reservas prudentes, cotas por tarea, condiciones de detención y reconciliación de costos diferidos.

**Contratos técnicos y arquitectura:** esquema de almacenamiento y versionado, APIs, herramientas de lectura y extracción de PDFs, implementación del coordinador, adaptación/reutilización del Matrix Validator, política de acceso a fuentes, modelos/prompts y forma concreta del Cockpit. PostgreSQL es la orientación del núcleo persistente inicial; no se aprueba aquí el diseño físico.

**Auditoría inteligente:** criterios de selección por riesgo, presupuestos, mecanismo de evaluación de objeciones y pruebas que acrediten su contribución. Una primera ejecución con auditoría desactivada no satisface la validación de esa capacidad.

**Publicación y desarrollo:** la consolidación documental no autoriza por sí sola modificar `main`, crear implementaciones, llamar APIs de pago, contratar servicios ni efectuar commit/push. La implementación mediante Claude Code requiere encargos posteriores y revisión de código/pruebas.

## 10. Decisiones relacionadas y referencias

- `SI-V3-VISION-001` — visión, modos futuros de misión, memoria comercial, gobierno y estrategia de validación.
- `SI-V3-FUNC-001` — Bloque 1: `DF-MVP-001..006` y `CA-01..CA-10`.
- `SI-DOC-001` — estándar documental.
- `SI-RESEARCH-123`, `SI-RESEARCH-130` — referencia histórica v2, reservada para comparación posterior.
- Handoff conversacional del 2026-10-22 — apoyo de continuidad, **no documento canónico incorporado al repositorio**.

## 11. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-10-22 | Borrador de consolidación de `DF-AG-001..016` y reconciliaciones H1–H3; mantiene límites del primer MVP y asuntos abiertos. |
