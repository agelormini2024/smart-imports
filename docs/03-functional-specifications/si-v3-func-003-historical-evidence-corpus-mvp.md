---
id: si-v3-func-003
title: "Smart Imports v3 — Historical Evidence Corpus and Commercial Memory Contract (MVP)"
description: "Contrato funcional inicial del Bloque 3: corpus histórico en dos niveles, custodia de fuentes, acceso ciego, integridad, privacidad y criterios de aceptación."
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: "2026-10-23"
updated: "2026-10-23"
language: es
scope: "Bloque 3 — Memoria comercial y evidencias; contrato inicial para reproducción histórica BRAND-CAND-009"
tags:
  - smart-imports-v3
  - functional-design
  - mvp
  - evidence
  - historical-blind-replay
  - governance
related:
  - si-v3-vision-001
  - si-v3-func-001
  - si-v3-func-002
  - si-doc-001
  - si-research-123
  - si-research-124
  - si-research-130
audience:
  - founder
  - developer
  - assistant
phase: design
---

# SI-V3-FUNC-003 — Contrato funcional inicial: corpus histórico y evidencias (MVP)

> **Estado:** `draft`, pendiente de revisión documental. El Founder aprobó el **corpus histórico en dos niveles y ejecuciones separadas** el 2026-10-23. Las condiciones técnicas y criterios de aceptación de este documento son especificaciones propuestas para materializar y comprobar ese acuerdo; **no constituyen implementación validada ni autorización de ejecución, gasto o publicación de evidencias privadas**.

## 1. Propósito, autoridad y límites

Formalizar cómo Smart Imports v3 incorpora, delimita y consume un conjunto **cerrado, trazable y privado** de evidencias históricas durante el primer ensayo de `BRAND-CAND-009`, evitando trasladar al investigador las evaluaciones o decisiones de Method v2. Este es el **primer contrato del Bloque 3**; no agota el diseño futuro de memoria comercial.

Relación con especificaciones existentes:

- `SI-V3-FUNC-001 v0.1.0`: misión, ejecuciones independientes, preflight obligatorio, autorización del Founder, estados operativos, resultados parciales y restricciones.
- `SI-V3-FUNC-002 v0.1.0`: `DF-AG-014` (evaluación a ciegas), `DF-AG-016` (corpus histórico cerrado), `DF-AG-003..005` (hallazgos y recomendaciones) y H1 (configuración inicial inmutable).
- `SI-V3-VISION-001 v0.2.1`: visión, separación de responsabilidades, memoria reutilizable y fases posteriores.
- `SI-DOC-001 v0.2.0`: estándar de documentación y estados.

**Fuera de alcance:** capturar nuevas fuentes de Internet, contactar proveedores, emitir RFQ, negociar, comprar, certificar seguridad o viabilidad de importación, habilitar `F14`, fijar APIs, esquema SQL, modelos o estructura física definitiva de almacenamiento.

## 2. Decisión funcional aprobada — dos niveles de corpus

**ACUERDO DEL FOUNDER (2026-10-23):** realizar **dos ejecuciones históricas separadas** sobre las mismas tres Product Bases, con corpus inicial comparable y ampliación de información de origen en una segunda ejecución. No combinar sus resultados como una sola corrida.

| Eje | Ejecución histórica A — Nivel A | Ejecución histórica B — Nivel B |
|---|---|---|
| Objetivo | Investigar con evidencias comerciales de nivel comparable. | Investigar el mismo alcance añadiendo evidencias históricas de origen F8 disponibles. |
| Product Bases | `BASE-FIT-010`, `BASE-FIT-012`, `BASE-FIT-013`. | Las mismas tres Product Bases. |
| Fuentes iniciales mínimas candidatas | Una publicación histórica de Mercado Libre por Product Base, previa verificación y depuración. | El mismo conjunto de Nivel A **más** las cinco publicaciones F8 verificadas de `010` y `012`. |
| Fuentes F8 para `013` | No aplica en Nivel A. | **Cero registradas en el manifiesto recibido**; ello no prueba inexistencia de proveedores ni inferioridad comercial. |
| Corpus | Cerrado, identificado y congelado antes del inicio. | Otro corpus cerrado, identificado y congelado antes del inicio. |
| Conocimiento de otras ejecuciones | No recibe resultados v2 ni de futuras ejecuciones. | No recibe resultados de A ni conclusiones v2; contexto y sesión independientes. |
| Salida | Resultado individual por Product Base, comparación y limitaciones, congelados. | Nueva salida independiente, congelada y comparable por cobertura. |

Estas dos ejecuciones pertenecen **al primer experimento de reproducción histórica**, y son distintas de la futura **reinvestigación autónoma con fuentes actuales** prevista por `SI-V3-FUNC-002`. Esta última no se abre con este contrato.

### 2.1. Comparabilidad y sesgos de cobertura

- «Comparable» significa **mismo nivel y criterio de admisión de fuentes**, no la obligación artificial de igual cantidad o calidad de documentos para cada Product Base.
- No se excluyen contradicciones, reseñas negativas ni afirmaciones incómodas para equilibrar resultados.
- La cobertura desigual de F8 en Nivel B es una **limitación de diseño del corpus histórico** derivada de la disponibilidad documental; no puede interpretarse como ausencia de oferta para `BASE-FIT-013`.
- Comparar A y B describe cambios en resultados al cambiar el **conjunto autorizado de evidencias**. Dada la cobertura desigual, no acredita un efecto causal generalizable ni la superioridad objetiva de una Product Base.
- Si la curaduría descubre otras fuentes pertinentes del mismo nivel, se debe revisar y autorizar **antes de congelar** cada corpus; no se agregan fuentes informalmente durante la ejecución.

## 3. Alcance documental comprobado y estado de integridad

### 3.1. Publicaciones de Mercado Libre (Nivel A, candidatas)

| Product Base | Referencia histórica | Identificador de publicación visible en el PDF | Estado |
|---|---|---|---|
| `BASE-FIT-010` | `ML-0189` | `MLA-776567826` | Identidad comercial contrastada; integridad binaria con original local **pendiente**. |
| `BASE-FIT-012` | `ML-0191` | `MLA-620026985` | Identidad comercial contrastada; integridad binaria con original local **pendiente**. |
| `BASE-FIT-013` | `ML-0192` | `MLA-780628597` | Identidad comercial contrastada; integridad binaria con original local **pendiente**. |

Estos registros identifican **candidatos a admitir**, no archivos depurados ni un corpus ya autorizado. Precios, contadores de vendidos, calificaciones y reseñas son observaciones fechadas de capturas, no datos actuales ni certificaciones de demanda o seguridad.

### 3.2. Publicaciones de Alibaba F8 (adición candidata de Nivel B)

- `BASE-FIT-010`: `EVID-0336`, `EVID-0337`, `EVID-0338`.
- `BASE-FIT-012`: `EVID-0342`, `EVID-0343`.
- `BASE-FIT-011`: `EVID-0339`, `EVID-0340`, `EVID-0341` — **fuera de ambas ejecuciones de la muestra**.
- `BASE-FIT-013`: no figura en el manifiesto F8 recibido; no inferir inexistencia de evidencias de fases previas.

El control local informado el 2026-10-23 comparó el SHA-256 de **8/8 PDFs F8** contra sus huellas declaradas, con **0 discrepancias, 0 faltantes y 0 errores**. De ellos, **5** corresponden al alcance de Nivel B. Este resultado prueba identidad binaria con el manifiesto, **no** autenticidad comercial, vigencia, calidad o seguridad de las fuentes.

El archivo privado `f8-source-manifest-009.json` contiene además *interpretaciones, riesgos, compatibilidades y resúmenes redactados durante v2*: **no es entrada autorizada** en su forma original. La curaduría puede usarlo fuera del entorno ciego para localizar fuentes y comprobar identificadores.

## 4. Contrato de entrada: original, derivado y registro

La unidad de evidencia admitida en una ejecución debe tener, como mínimo:

1. **Identidad:** identificador opaco de evidencia v3, Product Base(s) relacionadas y tipo de fuente.
2. **Procedencia:** publicación/URL o referencia documental verificable, emisor/vendedor declarado, fecha de captura y fecha de publicación cuando se conozca (marcar `desconocida` si no).
3. **Integridad:** localizador privado del original bajo custodia, tamaño y SHA-256 observado; si existe versión derivada depurada, su SHA-256, versión y relación explícita con el original.
4. **Acceso:** identificador del corpus, clasificación de uso y autorización por ejecución, sin exponer al investigador rutas físicas externas o índices con conclusiones históricas.
5. **Contenido y confiabilidad:** distinción entre información visible, declaración del anunciante, reseña de comprador, resumen generado por tercero y hecho contrastado; incertidumbres y contradicciones conservadas.
6. **Trazabilidad:** referencia localizable a página, fragmento o registro utilizado por cada hallazgo, con reporte de legibilidad y tratamiento de extracción.
7. **Estado de admisión:** `CANDIDATA`, `VERIFICADA`, `DEPURADA`, `AUTORIZADA`, `EXCLUIDA` como **etiquetas propuestas de curaduría**, no catálogo definitivo de estados operativos.

No se traslada automáticamente la totalidad de una matriz XLSX de Method v2. Cuando una hoja contenga hechos y evaluaciones mezclados, debe prepararse una representación derivada que conserve solo las evidencias y contexto comercial permitido; se registrará cómo se construyó y qué quedó excluido.

## 5. Frontera de seguridad y aislamiento ciego

**Tres ámbitos diferenciados:**

- **Custodia histórica privada:** originales de PDFs, matrices, manifests, documentos de fases, logs y resultados de Method v2. Acceso de curaduría, no del investigador.
- **Corpus permitido por ejecución:** versiones depuradas, identidades opacas y metadatos mínimos aprobados. Solo ese conjunto se hace accesible a investigador y auditor inteligente habilitado.
- **Evaluación reservada:** clasificaciones, shortlist, juicios y decisiones de Method v2; resultados de A reservados frente al investigador B; usados únicamente por evaluadores autorizados después de los congelamientos definidos.

Aislamiento comprobable, **no solo por prompt**: investigador, herramientas, recuperación semántica, cachés, memoria, archivos de trabajo y auditoría opcional no deben poder acceder a rutas, índices, textos o resúmenes que revelen decisiones v2. En reproducción cerrada se deshabilita la adquisición libre de fuentes externas; el eventual uso de un proveedor de modelos no autoriza navegación web ni envío de originales con datos personales sin tratamiento aprobado.

En cada ejecución se usa contexto limpio y corpus expresamente identificado. Quedan prohibidas inferencias derivadas de nomenclaturas `FINALIST`, `STOP`, `DEFER`, `F13`, rankings, puntuaciones o rutas históricas de decisión. La mera ausencia de fuentes F8 para una Product Base debe mostrarse como **limitación de cobertura**, no como señal de descarte.

## 6. Privacidad y fidelidad de documentos

Las capturas de Mercado Libre incluyen cabeceras de sesión con datos personales. **No incorporar originales sin depurar al conjunto que consume el investigador**.

- Conservar el original íntegro en custodia privada; generar un derivado explícito para el corpus.
- Depurar identificadores de cuenta, domicilio, datos de sesión y cualquier otro dato personal no pertinente; preservar precio, título, descripción, reseñas, identificador público de publicación y evidencia comercial relevante.
- Comprobar que la depuración es efectiva **también en texto extraíble o capas internas del PDF**, no solo por un rectángulo visual.
- Conservar identidad del original, derivado, método/versión de depuración, resultado del control y hashes; cambios materiales en datos comerciales obligan a revisión.
- No publicar PDFs, XLSX, manifiestos privados, rutas del equipo, credenciales o logs en GitHub. La especificación pública solo contiene metadatos comerciales no sensibles.

## 7. Congelamiento y secuencia de evaluación

1. **Curaduría de Nivel A:** localizar, comprobar y depurar los tres PDFs ML; registrar ausencias y un manifiesto de admisión sin evaluaciones v2.
2. **Preflight A:** comprobar integridad, privacidad, aislamiento, legibilidad, alcance, presupuesto/capacidades y bloqueos críticos. Respetar `READY`, `READY WITH WARNINGS` y `BLOCKED` de Bloque 1.
3. **Autorización A:** el Founder aprueba explícitamente el inicio después de preflight; corpus cerrado e inmutable durante la ejecución.
4. **Investigación A:** producir hallazgos por Product Base, comparabilidad, evidencia y limitaciones. **Congelar A** con identidad de corpus, configuración, resultados, validaciones, bitácora y costo.
5. **Curaduría y preflight B:** construir un segundo corpus con los mismos derivados autorizados A más las cinco evidencias F8 pertinentes, depuradas y verificadas. Registrar por Product Base la cobertura desigual.
6. **Autorización y ejecución B:** segunda ejecución distinta, mismo alcance, sesión limpia y **sin acceso a resultados A ni v2**. **Congelar B** con su propia configuración y resultados.
7. **Evaluación del experimento:** comprobar primero integridad, independencia y calidad de razonamiento de A y B sin revelar v2; después habilitar comparación externa con referencias v2, sin reescribir resultados congelados.
8. **Decisión del Founder:** aceptar, solicitar corrección/nueva ejecución o avanzar a una fase posterior. Las ejecuciones no cierran la misión automáticamente ni habilitan `F14`.

La congelación de A **no habilita revelar la evaluación v2 al investigador B**. Toda modificación del corpus, modalidad o selección de capacidades requiere **una nueva ejecución**, nunca una mutación retroactiva. Los datos faltantes no se convierten automáticamente en `ARCHIVAR`.

## 8. Preflight y criterios de aceptación del contrato

Propuesta de criterios verificables específicos del corpus (complementarios a `CA-01..CA-10`):

| ID | Comprobación | Condición esperada |
|---|---|---|
| `CA-EV-01` | Inventario | Cada evidencia del corpus tiene identidad, origen, Product Base y referencia localizable; ninguna fuente aparece por descubrimiento implícito. |
| `CA-EV-02` | Integridad | Se calcula y compara la huella del original, y se registra separadamente la del derivado; desajustes críticos bloquean la admisión. |
| `CA-EV-03` | Privacidad | Los documentos ofrecidos al investigador están depurados y verificados en capas visuales y extraíbles; filtración de datos personales bloquea admisión. |
| `CA-EV-04` | Acceso negativo | Intentos de acceder a `SI-RESEARCH-130`, shortlist, matrices con decisiones o archivos fuera del corpus son efectivamente rechazados y registrados. |
| `CA-EV-05` | Inmutabilidad | El identificador/huella del corpus de cada ejecución permanece fijo antes y después de ejecutar; cambio implica nueva ejecución. |
| `CA-EV-06` | Independencia | B no puede leer resultados, memoria, resúmenes ni bitácoras analíticas de A, ni resultados v2, antes de su congelamiento. |
| `CA-EV-07` | Cobertura | A incluye las tres Product Bases con criterios comunes; B agrega solo las cinco fuentes F8 pertinentes; `011` excluida; ausencia F8 de `013` señalada sin penalización automática. |
| `CA-EV-08` | Fidelidad | Hallazgos referencian fuentes admitidas y diferencian hechos, afirmaciones de terceros, inferencias, contradicciones y faltantes. |
| `CA-EV-09` | Orden de revelación | No se revelan conclusiones v2 al investigador/auditor, ni resultados de A al investigador B; la comparación externa se realiza tras congelar ambas ejecuciones. |
| `CA-EV-10` | Restricciones operativas | `BLOCKED` impide ejecutar; solo el Founder autoriza inicios y ampliaciones; sin navegación abierta, sourcing, compras, contacto ni `F14`. |
| `CA-EV-11` | Reproducibilidad | Un tercero autorizado puede reconstruir qué versiones de evidencia, configuración, controles, permisos y resultados se utilizaron en A y B. |

Los casos de prueba deben incluir, por lo menos: documento mal clasificado, hash distinto, PDF con texto personal residual, intento de leer archivo excluido, acceso cruzado de A a B, manifiesto incompleto, evidencia contradictoria y ausencia de fuente F8 para `013`.

**Regla de criticidad propuesta:** cualquier filtración de decisiones históricas, fallo real de aislamiento, manipulación no autorizada del corpus o exposición de información personal al investigador debe devolver `BLOCKED` (antes de ejecutar) o detener/invalidar la ejecución afectada (si se detecta durante/después). Las advertencias no críticas, como falta de determinada evidencia comercial, deben quedar visibles y no se traducen en resultado comercial negativo por defecto.

## 9. Memoria comercial: frontera inicial y pendientes

En el MVP la memoria debe **conservar identidad de fuentes, vínculos a Product Bases, procedencia, versiones, hallazgos y contexto de cada ejecución**, con persistencia operativa inicial en PostgreSQL de acuerdo con H3. Esto **no** implica almacenar los PDFs originales dentro de la base ni aprobar todavía el diseño físico de almacenamiento.

Antes de implementar queda por precisar: formatos y esquemas, política de almacenamiento/cifrado/retención, sistema de permisos, herramientas de saneamiento, reconstrucción segura de XLSX, reglas de deduplicación entre corpus, vigencia de fuentes, alcance de reutilización comercial entre misiones y tratamiento concreto de datos personales. La reinvestigación autónoma con capturas dinámicas es posterior y tiene contrato propio de incorporación controlada.

## 10. Estado y próximos checkpoints

- **Decisión aprobada:** dos niveles, en ejecuciones históricas independientes, con diferencia de cobertura documentada.
- **Verificado a partir de los registros locales compartidos:** 8/8 hashes F8 coincidentes; las cinco fuentes F8 seleccionadas corresponden a `010` y `012`.
- **Identificado, pero no validado como corpus:** tres PDFs de Mercado Libre, uno por Product Base. Sus hashes frente a originales locales y saneamiento siguen pendientes.
- **Pendiente de aprobación:** criterios detallados `CA-EV-01..11`, ubicación física final, mecanismos técnicos concretos y admisión de cada evidencia depurada.
- **Sin autorización:** edición de archivos históricos, acceso automático a repositorios o memorias de v2 por el investigador, gasto en API, inicio de ejecución, contacto comercial o `F14`.

Próximo checkpoint de trabajo: **materializar y validar un manifiesto privado de Nivel A y una prueba de saneamiento e aislamiento**, sin comprometer el repositorio público con datos personales ni fuentes privadas.

## 11. Changelog

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-10-23 | Primer borrador del Bloque 3: contrato de corpus histórico en dos niveles aprobado funcionalmente; reglas propuestas de custodia, aislamiento, trazabilidad, privacidad, secuencia A/B y criterios `CA-EV-01..11`. |
