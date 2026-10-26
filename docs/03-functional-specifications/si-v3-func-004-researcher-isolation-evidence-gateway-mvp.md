---
id: si-v3-func-004
title: "Smart Imports v3 — Researcher Isolation and Evidence Gateway Contract (MVP)"
description: "Contrato verificable para aislamiento del investigador y acceso mediado a evidencias en la reproducción histórica a ciegas."
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: "2026-10-26"
updated: "2026-10-26"
language: es
scope: "Smart Imports v3 — Seguridad mínima del investigador histórico; ejecuciones A y B de BRAND-CAND-009"
tags:
  - smart-imports-v3
  - functional-design
  - security
  - evidence-access
  - historical-blind-replay
  - mvp
related:
  - si-v3-vision-001
  - si-v3-func-001
  - si-v3-func-002
  - si-v3-func-003
  - si-doc-001
audience:
  - founder
  - developer
  - assistant
phase: design
---

# SI-V3-FUNC-004 — Contrato verificable de aislamiento y Evidence Gateway (MVP)

> **Estado documental:** `draft`. El Founder aprobó funcionalmente `DF-SEC-001` y `DF-SEC-002` el 2026-10-26. Las interfaces, controles y pruebas que se proponen a continuación deben implementarse, revisarse y superarse antes de autorizar una ejecución real. Ninguna aprobación conversacional de arquitectura equivale a certificación del aislamiento, congelamiento del corpus, autorización de gasto ni inicio de investigación.

## 1. Propósito y jerarquía

Asegurar que el investigador de la reproducción histórica de `BRAND-CAND-009` solo pueda consumir evidencias expresamente autorizadas para su ejecución, sin acceso a conclusiones de Method v2, resultados de otras ejecuciones, carpetas privadas o adquisición libre de fuentes.

Complementa sin reemplazar:

- `SI-V3-FUNC-001`: misiones, ejecuciones separadas, preflight, `READY` / `READY WITH WARNINGS` / `BLOCKED` y autorización del Founder.
- `SI-V3-FUNC-002`: único rol investigador, coordinación y validadores determinísticos; `DF-AG-014` (reproducción ciega), `DF-AG-016` (corpus cerrado) y H1 (configuración por ejecución).
- `SI-V3-FUNC-003`: corpus A/B, custodia, privacidad, hashes, congelamiento, secuencia de evaluación y `CA-EV-01..11`.
- `SI-DOC-001`: convenciones documentales aplicables.

**Límite del presente documento:** contrato y pruebas verificables, no elección de Docker, nube, sistema operativo, motor de búsqueda, modelo, proveedor de API, esquema SQL definitivo ni topología física de infraestructura.

## 2. Decisiones funcionales aprobadas

| ID | Decisión | Consecuencia exigible |
|---|---|---|
| `DF-SEC-001` | Investigador en entorno **técnicamente restringido**, con **denegación por defecto** y lista positiva de recursos autorizados. | No depender de prompts, nombres de carpetas o promesas de comportamiento del modelo; comprobar límites reales del entorno y sus herramientas. |
| `DF-SEC-002` | Acceso del investigador a documentos **exclusivamente a través de un Evidence Gateway controlado**. | Autorización vinculada a ejecución y manifiesto congelado, integridad comprobada, auditoría, prohibición de rutas arbitrarias y acceso cruzado. |

Las dos barreras son **independientes y complementarias**: el Gateway no sustituye el aislamiento del proceso; el aislamiento no sustituye la autorización por evidencia. Cualquier falla crítica bloquea el inicio o invalida la ejecución afectada.

## 3. Actores, ámbitos y fronteras de confianza

| Ámbito | Puede conocer | No puede acceder |
|---|---|---|
| **Curador privado** | Originales, relación original–derivado, manifiesto completo, documentación v2, reglas de admisión. | No debe trasladar conclusiones históricas a las vistas del investigador. |
| **Coordinador determinístico** | `execution_id` autorizado, manifest firmado/congelado, políticas, estado de preflight y presupuesto. | No puede ampliar permisos, corpus o límites sin autorización correspondiente. |
| **Investigador IA, ejecución A** | Tres evidencias ML **depuradas** admitidas para A, metadatos mínimos de análisis y herramientas expresamente permitidas. | Archivos brutos, rutas de origen, repositorio, evaluaciones v2, documentos fuera de A, red abierta y ejecuciones ajenas. |
| **Investigador IA, ejecución B** | Corpus B independiente (A autorizado + cinco derivados F8 admitidos) y contexto propio. | Resultados de A, conclusiones v2, sesiones/cachés ajenos y archivos privados. |
| **Evidence Gateway** | Relación confiable `execution_id` → manifiesto inmutable → `evidence_id` → derivado verificado. | No entrega originales ni interpreta decisiones comerciales. |
| **Evaluador posterior** | Resultados congelados de A y B; referencias v2 tras el orden de revelación aprobado. | No altera las ejecuciones ya congeladas. |

El modelo y cualquier texto extraído de documentos se consideran **entradas no confiables**. No otorgan autoridad para modificar permisos, invocar herramientas administrativas o leer otros recursos.

## 4. Contrato de acceso a evidencias

### 4.1. Identidades y autorizaciones

Cada solicitud se autentica por una **identidad de ejecución establecida por el coordinador/servicio**, nunca inferida únicamente de un campo que el modelo pueda inventar. La autorización comprueba simultáneamente:

1. Ejecución existente, aprobada y en estado que admita lectura.
2. Manifiesto congelado ligado criptográficamente o mediante hash registrado a esa ejecución, con versión y ámbito A/B.
3. `evidence_id` opaco presente en la lista positiva de esa ejecución.
4. Derivado depurado aprobado; hash SHA-256 observado coincide con el declarado, antes de entregar contenido.
5. Herramienta, operación, alcance de páginas/fragmentos y política vigentes para esa ejecución.

Si falta una condición, la operación **falla cerrada**. No existe permiso por herencia desde el curador, otras ejecuciones ni referencias históricas.

### 4.2. Interfaz lógica ilustrativa, no API definitiva

**Solicitud:** identidad confiable de la ejecución (fuera del control del modelo), `evidence_id`, operación acotada (`leer_metadata`, `leer_pagina`, `leer_fragmento`) y selector limitado al documento autorizado.

**Respuesta permitida:** contenido depurado estrictamente solicitado; identificador y versión de evidencia; referencia de página/fragmento; estado de integridad y procedencia comercial autorizada. No incluye rutas locales absolutas, hashes de originales privados si no son necesarios, credenciales, manifiesto de curador ni decisiones históricas.

**Respuesta denegada:** código y motivo de política no sensible; nunca rutas existentes, contenido parcialmente leído ni detalles que permitan enumerar evidencia ajena.

Las operaciones de lectura no admiten rutas, nombres de archivo, URL arbitraria, patrones glob, shell, SQL libre ni búsquedas no delimitadas. Las referencias a publicaciones web se consideran **evidencia histórica**, no permisos para navegar.

### 4.3. Integridad y límites de contenido

- El manifest/allowlist se verifica **antes de resolver archivos**. Las ubicaciones físicas son internas, con canonicalización y protección contra enlaces simbólicos, traversal y cambios de archivo entre comprobación y lectura.
- El hash se comprueba en el **objeto efectivamente entregado**. Una discrepancia bloquea lectura, dispara incidente y exige revalidación de la ejecución; no se sirve una versión parecida por conveniencia.
- Los derivados se sirven como contenido inmutable/versionado; los originales privados nunca se montan en el entorno del investigador.
- Si se indexan fragmentos, cada entrada conserva identidad del corpus, `execution_id`, `evidence_id`, hash/versionado y control de acceso. Índices, embeddings, memoria, resúmenes y cachés se segregan por ejecución o se vacían/verifican exhaustivamente.
- La auditoría opcional solo ve el corpus permitido a su ejecución. Tampoco puede descubrir conocimiento v2 por herramientas, prompts, traces, caches o metadatos.

## 5. Restricciones de entorno y herramientas

1. **Aislamiento real:** el proceso/servicio del investigador no tiene permisos de lectura ni montajes hacia carpetas del curador, repositorio histórico, archivos de otras ejecuciones o almacenamiento del anfitrión ajeno a su operación.
2. **Menor privilegio:** sin acceso directo a shell/FS arbitrario, ejecución de código, conectores, gestores de archivos ni navegadores, salvo capacidades explícitas y probadas en un contrato posterior.
3. **Red restringida:** prohibida búsqueda o adquisición externa en ensayo histórico. Si se usa un servicio de modelos, el acceso se realiza mediante una vía controlada que permita la llamada al proveedor **sin otorgar Internet libre al investigador**.
4. **No contaminación cruzada:** contexto conversacional, prompts de sistema, historial, checkpoints, herramientas, archivos temporales, logs legibles, índices y cachés no pueden contener ni recuperar decisiones v2 o resultados de A en B.
5. **Permisos defendidos fuera del LLM:** no se acepta un prompt como mecanismo de seguridad. El modelo no decide autorización ni puede elevar sus privilegios.
6. **Abstención y eventos:** recursos no disponibles se declaran como limitación operacional/comercial según corresponda, nunca como `ARCHIVAR` automático.

La tecnología concreta del aislamiento será elegida durante la implementación y deberá pasar las mismas pruebas negativas. No se declara segura por el mero uso de un contenedor.

## 6. Auditoría y manejo de incidentes

Para cada solicitud, registrar al menos: `event_id`, tiempo, `execution_id` confiable, `corpus_id`/hash de manifiesto, operación, `evidence_id` solicitado, `decision` (`ALLOW`/`DENY`/`BLOCK`), motivo codificado, hash/versionado del derivado si se entregó y referencia de correlación con tarea. Evitar guardar cuerpos completos de PDF, datos personales, rutas privadas o conclusiones en el registro de acceso.

- **Denegación esperada:** registra motivo, no filtra existencia de recursos ajenos y no expone contenido parcial.
- **Anomalía crítica:** acceso indebido efectivo, hash inconsistente, contaminación de contexto, filtración de PII o salida de red no autorizada → detener/invalidar ejecución afectada, preservar bitácora y requerir nuevo preflight y autorización.
- **Error no crítico:** se registra con alcance localizado y límites explícitos; no puede encubrir una falla de aislamiento.
- **Integridad de auditoría:** correlación entre petición, decisión y entrega; protección contra borrado o edición no autorizados. El mecanismo concreto es pendiente de implementación y prueba.

## 7. Pruebas negativas obligatorias del primer circuito

Cada caso debe probarse **desde las mismas identidades, herramientas y límites que utilizará el investigador**, no solo en funciones aisladas. Los ejemplos de documentos prohibidos son objetivos de pruebas controladas por el equipo, nunca datos que se entregan al modelo.

| ID | Escenario de prueba | Comportamiento exigido |
|---|---|---|
| `CA-SEC-01` | Leer cada `evidence_id` de la ejecución activa. | `ALLOW` únicamente para derivados autorizados, con integridad y referencias correctas. |
| `CA-SEC-02` | Solicitar ID desconocido o excluido. | `DENY`, sin contenido parcial ni enumeración de otras evidencias. |
| `CA-SEC-03` | Intentar leer matriz final `aut171`, `SI-RESEARCH-130` o conclusiones v2. | `DENY` efectivo en Gateway **y** sin acceso directo en entorno; evento registrado. |
| `CA-SEC-04` | Probar path traversal, ruta absoluta, alias, symlink o cambio del recurso durante la lectura. | No escape; `DENY`/`BLOCK` y auditoría. |
| `CA-SEC-05` | Invest. B solicita evidencia, resultados, herramientas, contexto o caché de A. | `DENY`; B recibe exclusivamente su corpus B, sin memoria de A. |
| `CA-SEC-06` | Intentar abrir archivos del anfitrión o repositorio con herramientas directas. | Imposibilidad técnica, no mera negativa del modelo. |
| `CA-SEC-07` | Intentar búsqueda web/descarga, acceso de red alternativo o conector no aprobado. | `DENY` por red/herramientas, preservando solo el tráfico legítimo del proveedor de modelos. |
| `CA-SEC-08` | Sustituir o modificar derivado/manifiesto/hash tras el congelamiento. | `BLOCKED`, incidente verificable; ninguna respuesta con contenido modificado. |
| `CA-SEC-09` | Introducir en un PDF una instrucción adversarial para leer v2 o cambiar reglas. | El contenido se trata como dato; sin elevación de privilegios; operación prohibida denegada. |
| `CA-SEC-10` | Probar acceso a original no depurado y residuo PII en derivado. | Original inaccesible; control de privacidad bloqueante si se detecta residuo. |
| `CA-SEC-11` | Solicitar evidencia de otra ejecución o corpus con un ID válido allí. | `DENY` sin filtración de existencia ni metadatos. |
| `CA-SEC-12` | Verificar eventos `ALLOW` y `DENY`, sus causas y la identidad de ejecución. | Auditoría completa, correlacionable y sin exposición de contenidos privados. |
| `CA-SEC-13` | Simular fallo de Gateway/manifest/política/log obligatorio. | **Fail closed**; no acceso por fallback, caché o ruta directa. |
| `CA-SEC-14` | Comprobar que `BLOCKED` y falta de aprobación Founder impiden iniciar. | Ejecución no se inicia; ninguna autorización tácita. |

**Condición no compensable:** todo `CA-SEC` obligatorio debe aprobar. Cualquier bypass real, filtración de decisiones v2, acceso cruzado, exfiltración o PII residual relevante implica `BLOCKED`/invalidación, aunque el investigador produzca un buen análisis.

## 8. Gate de autorización y orden de trabajo

**Gate previo a ejecutar A:**

1. Corpus A verificado, depurado, manifiesto final privado y hash congelado.
2. Entorno y Gateway implementados mínimamente para A, con todos los `CA-SEC` relevantes probados de punta a punta, incluidos los que aseguran independencia posterior de B.
3. Preflight integral de Bloque 1 + `CA-EV` de Bloque 3 + `CA-SEC` de este contrato. `BLOCKED` impide la ejecución.
4. Presupuesto, proveedor de modelos, tratamiento de datos y límites concretos documentados y aprobados.
5. Autorización **explícita y específica** del Founder para ejecutar A; autorización separada para B cuando corresponda.

**Orden previsto:** formalización documental → diseño de implementación mínima y pruebas → implementación del entorno/Gateway → pruebas negativas → congelamiento de corpus A/registro de permisos → preflight → autorización Founder → ejecución A → congelamiento de resultados A. B requiere su propio corpus, contexto limpio, preflight y autorización, sin conocimiento de resultados A ni v2.

La congelación del corpus **no sustituye** autorización para ejecutar ni certifica aislamiento. El preflight técnico documental ya realizado sobre tres PDFs ML (`3/3 PASS`, 2026-10-26) habilita preparar el gate, pero el corpus sigue `CANDIDATE_NOT_AUTHORIZED`.

## 9. Pendientes de diseño de implementación

- Mecanismo concreto de aislamiento y verificación de acceso negativo en el entorno elegido.
- Identidad/autenticación de ejecución y de tareas entre coordinador y Gateway.
- Especificación técnica definitiva de API, códigos de error, cuotas y límites de extracción por página/fragmento.
- Almacenamiento e inmutabilidad del manifiesto/derivados, transacciones y garantías frente a TOCTOU.
- Control de egreso de red y proveedor de modelos; política de retención/privacidad compatible.
- Integridad de logs y recuperación después de incidentes.
- Modelo de amenazas, alcance de pruebas automatizadas y evidencia E2E reproducible.

Estos asuntos **no bloquean el commit de este borrador**, pero sí su aceptación operativa y cualquier ejecución real del investigador.

## 10. Relación con próximas etapas

El presente contrato se aplica a reproducción histórica cerrada A/B. La futura reinvestigación autónoma con información actual requerirá una **extensión autorizada** para adquisición dinámica de fuentes y red, sin reducir garantías de aislamiento, auditoría, presupuestos y trazabilidad. No se habilitan RFQ, compras, homologación de proveedores ni `F14` por este documento.

**Checkpoint previsto para migración de chat:** después de revisar, integrar y publicar este contrato técnico. El nuevo chat comenzará la planificación de implementación mínima con Claude Code desde el commit validado, el estado del corpus y una síntesis de decisiones/puntos abiertos, sin depender del historial completo de conversación.
