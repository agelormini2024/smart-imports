---
id: si-func-001
title: Matrix Validator Functional Specification
description: Especificación funcional del primer MVP del Smart Imports Intelligence Engine para validar estructura, IDs, relaciones, valores y fórmulas de la matriz operativa.
version: 1.2.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-24
updated: 2026-08-04
tags:
  - matrix-validator
  - functional-specification
  - data-quality
  - validation
  - intelligence-engine
related:
  - si-agent-001
  - si-roadmap-001
  - si-roadmap-002
  - si-decision-006
  - si-decision-009
  - si-tech-001
  - si-tech-002
  - si-decision-010
audience:
  - founder
  - developer
  - assistant
phase: foundation
---

# SI-FUNC-001 — Matrix Validator

> La primera automatización debe proteger la integridad del conocimiento que ya construimos manualmente.

## 0. Estado de implementación al 2026-08-04

El contrato funcional continúa vigente. La implementación ya cubre la normalización estructural y la mayor parte de las validaciones semánticas del MVP.

Implementado y validado:

- Lectura XLSX read-only mediante SheetJS.
- CLI local y reporte JSON.
- `full-matrix-v3 0.1.0`, `full-matrix-v4 0.6.0` y `full-matrix-v5 0.5.0`.
- `aut29`, `aut30` y `aut31` con cero errores bloqueantes.
- Hojas, columnas, posiciones, PK, FK y listas de FK.
- Fuentes globales y relación `Evidencia Fuentes`.
- Resúmenes normalizados de Competencia, Margen y Tanda.
- Tipos, rangos, vocabularios y valores obligatorios.
- Obligaciones condicionales y consistencia por fila.
- Vistas derivadas formula-driven y tokens de error visibles.
- 35 archivos de test y 144 tests.

Pendiente para aceptar el MVP completo:

- Fixtures XLSX públicos end-to-end y CI.
- Manual operativo final y limpieza de ExcelJS/spikes.
- Definición explícita sobre agregados cruzados y formato general de IDs.
- Revisión humana de los resúmenes migrados.
- Retiro del warning provisional y primera release.

```text
Matrix Validator técnicamente avanzado y utilizable
≠
Matrix Validator MVP publicado
```

## 1. Propósito

Este documento define el comportamiento funcional del **Matrix Validator**, primer MVP del Smart Imports Intelligence Engine.

El Matrix Validator deberá analizar una matriz operativa XLSX de Smart Imports y determinar si puede utilizarse con seguridad como fuente de trabajo. Su función es detectar errores estructurales, IDs inválidos o duplicados, referencias rotas, valores no permitidos, filas incompletas y fórmulas faltantes o dañadas.

El MVP será una herramienta de validación **read-only**:

- No modificará la matriz.
- No corregirá IDs.
- No reordenará columnas.
- No completará datos faltantes.
- No reemplazará decisiones humanas.
- Producirá hallazgos explicables para que la corrección sea revisada y aplicada conscientemente.

## 2. Contexto

La segunda ejecución metodológica confirmó que la matriz ya funciona como sistema operativo inicial, pero también mostró fricciones repetidas:

- Importables con nombres u orden de columnas incompatibles.
- Riesgo de IDs duplicados o con formato incorrecto.
- Referencias a productos base que deben conservar integridad.
- Correcciones que deben reemplazar filas en lugar de duplicarlas.
- Fórmulas que no se extienden automáticamente a un nicho nuevo.
- Fechas y números que pueden cambiar de interpretación según la configuración regional.
- Filas realizadas con información parcial, como tiempos no medidos.
- Variantes comerciales que pueden crear productos base duplicados.

El caso real que inicia este MVP ocurrió en la matriz `v3 aut(28)`:

```text
Evaluaciones!A10 = EV-0009
Formato esperado   = EVAL-0009
```

El registro era único y sus relaciones eran válidas, pero el prefijo incumplía el contrato de IDs. La corrección se realizó reemplazando el valor de la fila existente en `v3 aut(29)`.

## 3. Objetivo funcional

El sistema debe responder cuatro preguntas:

1. ¿La estructura del workbook coincide con la versión de esquema esperada?
2. ¿Cada registro tiene un ID válido y único?
3. ¿Las relaciones entre hojas apuntan a registros existentes y coherentes?
4. ¿La matriz contiene errores que bloquean su uso o advertencias que requieren revisión?

La salida debe permitir:

- Identificar el problema.
- Localizar la celda o fila.
- Comprender por qué importa.
- Conocer el valor esperado y el valor encontrado.
- Distinguir errores bloqueantes de advertencias.
- Utilizar el resultado tanto en consola como desde futuros workflows.

## 4. Principios funcionales

### SI-MV-P001 — Read-only by default

La validación no debe modificar el archivo de entrada.

### SI-MV-P002 — Exact schema before inference

Los nombres y el orden de columnas se validan antes de interpretar los datos.

### SI-MV-P003 — Errors must be actionable

Cada hallazgo debe indicar ubicación, regla incumplida y corrección esperada.

### SI-MV-P004 — Referential integrity is mandatory

Una referencia interna no puede apuntar a un registro inexistente.

### SI-MV-P005 — Warnings do not equal approval

Una matriz sin errores bloqueantes puede contener advertencias que todavía requieren revisión humana.

### SI-MV-P006 — No fuzzy decisions in the MVP

La detección semántica de productos base similares no debe bloquear automáticamente. En el MVP sólo puede producir advertencias conservadoras.

### SI-MV-P007 — Regional compatibility is explicit

Las fechas y números deben validarse sin asumir una única configuración regional.

### SI-MV-P008 — Schema changes are intentional

Una columna nueva al final puede informarse como extensión; una columna insertada, renombrada o reordenada debe considerarse incompatible.

## 5. Usuario principal

El usuario principal inicial es el Founder/operador de la matriz.

Casos de uso:

- Validar una nueva versión antes de declararla vigente.
- Validar una matriz después de incorporar un importable.
- Revisar una matriz recibida en un nuevo chat o sesión.
- Ejecutar validaciones desde un workflow futuro.
- Obtener un reporte para corregir errores sin inspeccionar manualmente todas las hojas.

## 6. Alcance del MVP 0.1

### 6.1 Incluido

- Lectura de archivos `.xlsx`.
- Validación de los perfiles `full-matrix-v3`, `full-matrix-v4` y `full-matrix-v5`.
- Validación de hojas requeridas.
- Validación de nombres y orden de columnas.
- Detección de columnas faltantes o agregadas.
- Validación de IDs primarios.
- Detección de IDs duplicados.
- Validación de formato y secuencia de IDs.
- Validación de referencias entre hojas.
- Validación de criterios, scores, confianza y estados.
- Validación de campos obligatorios.
- Detección de filas parcialmente cargadas.
- Validación de fórmulas obligatorias en filas activas de `Nichos`.
- Detección de tokens de error almacenados en fórmulas.
- Salida legible en consola.
- Salida estructurada JSON.
- Códigos de salida para integración con scripts o CI.
- Pruebas automatizadas con copias controladas de la matriz.

### 6.2 Excluido

- Corrección automática del workbook.
- Recalcular fórmulas con un motor compatible con Excel.
- Validar archivos `.xls`, Google Sheets o CSV.
- Scraping o extracción de fuentes.
- Detectar productos equivalentes mediante IA.
- Evaluar si un score comercial es correcto.
- Modificar metodología o pesos.
- Validar cotizaciones contra documentos originales.
- Validar claims técnicos.
- Validar importables parciales en la primera entrega.
- Interfaz web.
- Persistencia en base de datos.

### 6.3 Incremento posterior previsto

El perfil `importable-v1` podrá validar archivos parciales y compararlos contra una matriz base:

```text
validate importable.xlsx --against matriz-vigente.xlsx
```

No forma parte del MVP 0.1 para evitar ampliar el alcance antes de estabilizar el esquema completo.

## 7. Contrato de entrada

### 7.1 Archivo obligatorio

- Un archivo con extensión `.xlsx`.
- No protegido con contraseña.
- Legible por la librería seleccionada.
- Correspondiente a un schema registrado: `full-matrix-v3`, `full-matrix-v4` o `full-matrix-v5`.

### 7.2 Parámetros funcionales

Ejemplo conceptual:

```bash
smart-imports validate "Smart Imports - matriz de oportunidades - v3 aut(29).xlsx"
```

Opciones mínimas:

```text
--schema full-matrix-v3|full-matrix-v4|full-matrix-v5
--format text|json
--output <path>
--strict
```

Comportamiento:

- `--schema`: selecciona el contrato de estructura. Actualmente se registran `full-matrix-v3`, `full-matrix-v4` y `full-matrix-v5`.
- `--format text`: salida humana en consola.
- `--format json`: reporte estructurado.
- `--output`: guarda el reporte sin modificar el XLSX.
- `--strict`: convierte advertencias configurables en resultado no aprobatorio, pero no cambia su severidad original.

## 8. Resultado global

El resultado de una ejecución será:

| Resultado | Condición |
|---|---|
| `PASS` | No existen errores bloqueantes. Puede haber información de diagnóstico. |
| `PASS_WITH_WARNINGS` | No existen errores bloqueantes, pero hay advertencias. |
| `FAIL` | Existe al menos un error bloqueante. |
| `TECHNICAL_FAILURE` | El archivo no pudo abrirse o la validación no pudo ejecutarse. |

## 9. Severidades

| Severidad | Significado | Efecto |
|---|---|---|
| `ERROR` | La integridad o compatibilidad no está garantizada. | Resultado `FAIL`. |
| `WARNING` | La matriz puede utilizarse, pero requiere revisión. | Resultado `PASS_WITH_WARNINGS`. |
| `INFO` | Hallazgo descriptivo o métrica. | No cambia el resultado. |

## 10. Hojas de los schemas soportados

### 10.1 `full-matrix-v3` — hojas requeridas

```text
Nichos
Evaluaciones
Evidencias
Registro Tiempos
Publicaciones ML
Productos Base
Competencia ML
Cotizaciones Proveedores
Simulación Margen
Fuentes Externas
Competencia Externa
Resumen Competencia
Resumen Margen
Resumen Tanda
Criterios
```

### 10.2 Política de validación de v3

- Las 15 hojas deben existir.
- El orden de hojas se informa como `WARNING` si cambia.
- Las hojas operativas estructuradas validan columnas exactas.
- Las tres hojas `Resumen *` sólo validan existencia en el MVP.
- Una hoja adicional produce `WARNING`.
- Una hoja faltante produce `ERROR`.

### 10.3 `full-matrix-v4`

`full-matrix-v4` conserva las 15 hojas anteriores e incorpora:

```text
Fuentes
Evidencia Fuentes
```

También agrega `Fuente Global ID` en las seis hojas especializadas y campos de migración en `Evidencias`.

La relación canónica de fuentes pasa a ser:

```text
Evidencia Fuentes.Evidencia ID → Evidencias.Evidencia ID
Evidencia Fuentes.Fuente ID → Fuentes.Fuente ID
```

Las tres hojas `Resumen *` continúan validando sólo existencia y son un bloqueo explícito de cierre.

### 10.4 `full-matrix-v5`

`full-matrix-v5` es el contrato de `aut31`. Conserva la normalización de fuentes de v4 e incorpora seis tablas canónicas/de detalle y tres vistas ejecutivas:

```text
Resumen Competencia
Resumen Competencia Segmentos
Resumen Competencia Vista
Resumen Margen
Resumen Margen Productos
Resumen Margen Vista
Resumen Tanda
Resumen Tanda Etapas
Resumen Tanda Vista
```

En v5:

- las cabeceras y tablas de detalle son fuentes de verdad;
- las vistas deben contener fórmulas directas hacia la misma fila de la tabla canónica;
- los IDs, relaciones, valores, tipos, rangos y condiciones son validables;
- las hojas `* Legacy` quedan fuera del contrato operativo.

## 11. Contrato de columnas

Las columnas existentes deben conservar exactamente nombre y posición.

Reglas:

1. Una columna faltante es `ERROR`.
2. Una columna renombrada es `ERROR`.
3. Una columna existente en otra posición es `ERROR`.
4. Una columna nueva insertada entre columnas existentes es `ERROR`.
5. Una columna nueva agregada al final es `WARNING` hasta que el esquema sea actualizado.
6. Columnas vacías después de la última columna definida no se consideran parte del esquema.

### 11.1 `Nichos`

```text
ID
Nicho
Estado
Demanda
Confianza Demanda
Competencia
Confianza Competencia
Margen
Confianza Margen
Facilidad de Importación
Confianza Importación
Potencial Marca
Confianza Marca
Venta Impulsiva
Confianza Vta. Impulsiva
Recompra
Confianza Recompra
Potencial IA
Confianza Potencial IA
Potencial Automatización
Confianza Automatización
Afinidad Personal
Confianza Afinidad Personal
Criterios evaluados
Total de Criterios definidos
Criterios Evaluados en formato 1/10
Score Parcial
Score Final
Confianza Promedio
Proxima Accion
Documento Research
Notas
```

### 11.2 `Evaluaciones`

```text
Evaluación ID
Fecha
Nicho ID
Nicho
Criterio
Valor
Estado
Confianza
Justificación
Soporte IDs
Evaluador
```

### 11.3 `Evidencias`

```text
Evidencia ID
Fecha
Nicho
Criterio
Fuente
Fuente ID
Tipo de Evidencia
Señal
Confianza Evidencia
Resumen
Link / Archivo
Observaciones
Estado
```

### 11.4 `Registro Tiempos`

```text
ID Registro
Fecha
Nicho ID
Nicho
Subcategoría
Tanda ID
Actividad
Actor
Método
Hora Inicio
Hora Fin
Tiempo Activo Min
Tiempo Retrabajo Min
Cantidad Fuentes
Publicaciones Creadas
Productos Base Creados
Duplicados Detectados
Evidencias Creadas
Errores Detectados
Retrabajos
Tipo de Error Principal
Automatización Posible
Interrupciones Excluidas
Precisión Medición
Observaciones
Estado
```

### 11.5 `Publicaciones ML`

```text
ML ID
Fecha Relevamiento
Nicho
Subcategoría
Búsqueda
Producto
Vendedor
Marca
Precio ARS
Precio USD
Ventas visibles
Rating
Cantidad Opiniones
Cantidad Comentarios
Link
Fuente Archivo
Producto Base
ID Producto Base
Es Variante / Duplicado
Tipo de Publicación
Tipo de Vendedor
Garantía
Envío / Full
Cuotas
Stock visible
Observaciones Crudas
```

### 11.6 `Productos Base`

```text
ID Producto Base
Nicho
Subcategoría
Producto Base
Descripción Base
Cantidad Publicaciones Detectadas
Cantidad Vendedores Detectados
Rango Precio ARS
Ventas Máximas Visibles
Rating Promedio
Nivel Commodity
Riesgo Técnico
Oportunidad Principal
Observaciones
```

### 11.7 `Competencia ML`

```text
Competencia ID
Fecha
Nicho
Subcategoría
Fuente ML ID
Producto Base
ID Producto Base
Vendedor Normalizado
Marca Normalizada
Es Variante / Duplicado
Competidor Real
Segmento Competitivo
Nivel de Saturación
Calidad Publicación
Diferenciación
Competencia Precio
Fortaleza Vendedor
Riesgo Técnico / Claim
Debilidades Detectadas
Oportunidad Detectada
Lectura Competitiva
Puntaje Parcial
Confianza
Estado
```

### 11.8 `Cotizaciones Proveedores`

```text
Cotización ID
Fecha
Nicho
Subcategoría
ID Producto Base
Producto Base
Producto Referencia
Proveedor
Plataforma
País
Incoterm
MOQ
Precio Unitario USD
Moneda
Cantidad Cotizada
CBM Caja
Peso Bruto Caja Kg
Unidades por Caja
Certificaciones
Batería / Riesgo Técnico
Link / Archivo
Estado
Observaciones
```

### 11.9 `Simulación Margen`

```text
Margen ID
Fecha
Nicho
Subcategoría
ID Producto Base
Producto Base
Cotización ID
Precio Venta ARS
Precio Venta USD
Precio Neto Estimado USD
Costo FOB USD
Factor Importación Estimado
Costo Importado Estimado USD
Costos Comerciales USD
Margen Unitario USD
Margen Porcentaje
ROI sobre Costo
Precio Piso Competitivo USD
Riesgo Margen
Puntaje Parcial
Confianza
Estado
Observaciones
FOB Objetivo USD
Diferencia vs FOB Público
FOB Negociado USD
MOQ Negociado
Viabilidad Post - Negociación
Próxima Acción
```

### 11.10 `Fuentes Externas`

```text
Fuente ID
Fecha Relevamiento
Nicho
Subcategoría
Fuente
Tipo de Fuente
Producto
Vendedor
Marca
Precio ARS
Precio USD
Rating
Cantidad Opiniones
Ventas visibles
Stock visible
Cuotas
Link / Archivo
Producto Base
ID Producto Base
Señal Comercial
Confianza
Observaciones
Estado
```

### 11.11 `Competencia Externa`

```text
Competencia ID
Fecha
Nicho
Subcategoría
Fuente Externa ID
Producto Base
ID Producto Base
Vendedor / Tienda
Marca Normalizada
Es Variante / Duplicado
Competidor Real
Canal Externo
Segmento Competitivo
Nivel de Saturación
Calidad Publicación
Diferenciación
Competencia Precio
Fortaleza Vendedor
Riesgo Técnico / Claim
Debilidades Detectadas
Oportunidad Detectada
Lectura Competitiva
Puntaje Parcial
Confianza
Estado
```

### 11.12 `Criterios`

```text
Criterio
Descripción
Peso
Cómo medir
Escala
Fuentes sugeridas
<columna separadora vacía>
Lista Estados
Lista Confianza
Lista Prioridad
```

## 12. Contrato de IDs

| Hoja | Campo | Formato |
|---|---|---|
| Nichos | `ID` | Entero positivo |
| Evaluaciones | `Evaluación ID` | `EVAL-0000` |
| Evidencias | `Evidencia ID` | `EVID-0000` |
| Registro Tiempos | `ID Registro` | `TIME-0000` |
| Publicaciones ML | `ML ID` | `ML-0000` |
| Productos Base | `ID Producto Base` | `BASE-{FAMILIA}-000` |
| Competencia ML | `Competencia ID` | `COMP-0000` |
| Cotizaciones Proveedores | `Cotización ID` | `COT-0000` |
| Simulación Margen | `Margen ID` | `MARG-0000` |
| Fuentes Externas | `Fuente ID` | `EXT-0000` |
| Competencia Externa | `Competencia ID` | `COMPEXT-0000` |

Consideraciones:

- El ID debe ser único dentro de su hoja.
- Un ID vacío en una fila con otros datos es `ERROR`.
- Un formato inválido es `ERROR`.
- Un salto de secuencia es `WARNING`, porque puede representar un registro eliminado o reservado.
- La existencia de una secuencia mayor no autoriza reutilizar números anteriores.
- El caso `EV-0009` debe producir `MV-ID-002`.

## 13. Integridad referencial

### 13.1 Relaciones bloqueantes

| Origen | Campo | Destino |
|---|---|---|
| Evaluaciones | `Nicho ID` | Nichos.`ID` |
| Evaluaciones | `Criterio` | Criterios.`Criterio` |
| Publicaciones ML | `ID Producto Base` | Productos Base.`ID Producto Base` |
| Competencia ML | `Fuente ML ID` | Publicaciones ML.`ML ID` |
| Competencia ML | `ID Producto Base` | Productos Base.`ID Producto Base` |
| Cotizaciones Proveedores | `ID Producto Base` | Productos Base.`ID Producto Base` |
| Simulación Margen | `ID Producto Base` | Productos Base.`ID Producto Base` |
| Simulación Margen | `Cotización ID` | Cotizaciones Proveedores.`Cotización ID` |
| Fuentes Externas | `ID Producto Base` | Productos Base.`ID Producto Base` |
| Competencia Externa | `Fuente Externa ID` | Fuentes Externas.`Fuente ID` |
| Competencia Externa | `ID Producto Base` | Productos Base.`ID Producto Base` |

Una referencia informada que no exista produce `ERROR`.

### 13.2 Evidencias y fuentes

En `full-matrix-v3`, `Evidencias.Fuente ID` conserva el modelo legado.

En `full-matrix-v4`, la referencia polimórfica deja de ser canónica. La integridad se valida mediante:

```text
Fuentes.Fuente ID
Evidencia Fuentes.Evidencia ID
Evidencia Fuentes.Fuente ID
```

Una evidencia debe tener al menos una relación activa. Las fuentes especializadas deben poseer un `Fuente Global ID` válido. Las columnas legadas se conservan temporalmente para auditoría de migración.

### 13.3 Consistencia de nombres

Cuando un registro contiene simultáneamente ID y nombre:

- `Nicho ID` debe corresponder al mismo nombre de `Nicho`.
- `ID Producto Base` debe corresponder al mismo `Producto Base`.
- Una diferencia exacta produce `ERROR`.
- Diferencias sólo de espacios o mayúsculas producen `WARNING`.

## 14. Valores permitidos

### 14.1 Scores

Los campos de evaluación deben respetar:

```text
1, 2, 3, 4 o 5
```

Cero puede aparecer en celdas calculadas de `Nichos` cuando un criterio no fue evaluado, pero no es un valor válido para una fila de `Evaluaciones`.

### 14.2 Confianza

Valores permitidos en campos de confianza:

```text
Alta
Media
Baja
Media/Baja
```

Las variantes adicionales deberán incorporarse al esquema de forma explícita. Un valor vacío se permite sólo cuando la evaluación correspondiente todavía no existe.

### 14.3 Estados

Los estados se validan por hoja, no mediante una única lista global.

Ejemplos vigentes:

- `Nichos`: `Pendiente`, `En evaluación`, `Validado`, `Descartado`, `Pausado`.
- `Evaluaciones`, `Evidencias`, `Competencia ML`: `Pendiente`, `Revisado`.
- `Cotizaciones Proveedores`, `Simulación Margen`, `Fuentes Externas`, `Competencia Externa`: `Pendiente`, `Revisado`, `Descartado`, `Pausado`.
- `Registro Tiempos`: se permiten estados compuestos vigentes, incluyendo `Completado — tiempo no medido`.

Las listas definitivas se almacenarán en el schema del Validator y deberán versionarse.

### 14.4 Fechas

Se aceptan:

- Celdas de fecha válidas de Excel.
- Texto ISO `YYYY-MM-DD`.

No se debe asumir que `24/07/2026` significa lo mismo en todas las configuraciones. Un texto ambiguo produce `WARNING`; una fecha imposible produce `ERROR`.

### 14.5 Números

- Los campos numéricos deben preferentemente ser celdas numéricas.
- Un texto que puede interpretarse de manera inequívoca produce `WARNING`.
- Un texto con separadores regionales ambiguos produce `ERROR`.
- Los símbolos monetarios deben permanecer fuera de campos destinados a cálculo.

## 15. Filas y campos obligatorios

### 15.1 Fila vacía

Una fila completamente vacía se ignora.

### 15.2 Fila parcial

Una fila con datos pero sin ID primario produce `ERROR`.

### 15.3 Campos mínimos

Para cada hoja estructurada se definirá una lista versionada de campos requeridos. Como mínimo:

- Identificador primario.
- Fecha cuando la hoja registra una observación temporal.
- Entidad o nicho.
- Referencias internas aplicables.
- Estado.
- Campos de decisión como score y confianza cuando el registro está `Revisado`.

### 15.4 Tiempo no medido

`Registro Tiempos.Tiempo Activo Min` puede estar vacío cuando:

```text
Precisión Medición = No medido
```

En ese caso, el Estado debe explicitar que la actividad se completó sin medición. No debe inventarse una duración.

## 16. Fórmulas

### 16.1 Alcance inicial

El MVP validará:

- Presencia de fórmulas esperadas.
- Fórmulas en filas activas de `Nichos`.
- Tokens de error almacenados: `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`.
- Diferencias respecto de la fórmula patrón de la fila anterior.

### 16.2 Filas activas

Una fila de `Nichos` con estado distinto de `Pendiente` debe tener las fórmulas previstas en el rango de cálculo.

El caso histórico de una fila del Nicho 2 sin fórmulas debe producir `ERROR`.

### 16.3 Limitación

El MVP no incluirá un motor de recálculo equivalente a Excel. Por lo tanto:

- Puede validar fórmula y valor cacheado.
- No puede garantizar que el resultado se haya recalculado después de una edición.
- Esta limitación debe aparecer en el reporte.

## 17. Catálogo mínimo de reglas

| Código | Severidad | Regla |
|---|---|---|
| `MV-FILE-001` | ERROR | El archivo no puede abrirse. |
| `MV-FILE-002` | ERROR | Extensión o formato no soportado. |
| `MV-SHEET-001` | ERROR | Falta una hoja requerida. |
| `MV-SHEET-002` | WARNING | Existe una hoja no definida. |
| `MV-SHEET-003` | WARNING | Cambió el orden de las hojas. |
| `MV-COL-001` | ERROR | Falta una columna requerida. |
| `MV-COL-002` | ERROR | Una columna fue renombrada. |
| `MV-COL-003` | ERROR | El orden de columnas cambió. |
| `MV-COL-004` | ERROR | Se insertó una columna nueva antes del final. |
| `MV-COL-005` | WARNING | Se agregó una columna al final aún no registrada. |
| `MV-ID-001` | ERROR | ID primario vacío. |
| `MV-ID-002` | ERROR | Formato de ID inválido. |
| `MV-ID-003` | ERROR | ID primario duplicado. |
| `MV-ID-004` | WARNING | Salto de secuencia. |
| `MV-REF-001` | ERROR | Referencia a Producto Base inexistente. |
| `MV-REF-002` | ERROR | Referencia a Publicación ML inexistente. |
| `MV-REF-003` | ERROR | Referencia a Fuente Externa inexistente. |
| `MV-REF-004` | ERROR | Referencia a Cotización inexistente. |
| `MV-REF-005` | ERROR | Referencia a Nicho inexistente. |
| `MV-REF-006` | ERROR | Criterio no definido. |
| `MV-REF-007` | WARNING | Fuente de evidencia con prefijo no registrado. |
| `MV-VAL-001` | ERROR | Score fuera del rango permitido. |
| `MV-VAL-002` | ERROR | Confianza no permitida. |
| `MV-VAL-003` | ERROR | Estado no permitido para la hoja. |
| `MV-VAL-004` | ERROR | Fecha inválida. |
| `MV-VAL-005` | WARNING | Fecha válida pero ambigua. |
| `MV-VAL-006` | ERROR | Número no interpretable o regionalmente ambiguo. |
| `MV-ROW-001` | ERROR | Fila parcial sin ID. |
| `MV-ROW-002` | ERROR | Campo obligatorio faltante. |
| `MV-ROW-003` | WARNING | Fila vacía dentro del bloque de datos. |
| `MV-FORM-001` | ERROR | Fórmula obligatoria faltante. |
| `MV-FORM-002` | ERROR | Fórmula con token de error. |
| `MV-FORM-003` | WARNING | Fórmula diferente del patrón esperado. |
| `MV-CONS-001` | ERROR | ID y nombre de Nicho no coinciden. |
| `MV-CONS-002` | ERROR | ID y nombre de Producto Base no coinciden. |
| `MV-CONS-003` | WARNING | Posible Producto Base duplicado por coincidencia exacta normalizada. |
| `MV-CONS-004` | WARNING | Identificador de Tanda inconsistente con la subcategoría o registros relacionados. |

## 18. Contrato de hallazgo

Cada hallazgo debe contener:

```json
{
  "code": "MV-ID-002",
  "severity": "ERROR",
  "sheet": "Evaluaciones",
  "row": 10,
  "column": "A",
  "cell": "A10",
  "recordId": "EV-0009",
  "message": "El ID no cumple el formato de Evaluaciones.",
  "expected": "EVAL-0000",
  "actual": "EV-0009",
  "remediation": "Reemplazar el ID de la fila existente por EVAL-0009. No agregar una fila nueva."
}
```

Campos obligatorios:

- `code`
- `severity`
- `message`

Campos de ubicación obligatorios cuando el problema pertenece a una celda:

- `sheet`
- `row`
- `column`
- `cell`

Campos opcionales:

- `recordId`
- `expected`
- `actual`
- `relatedId`
- `remediation`

## 19. Salida de consola

Ejemplo:

```text
Smart Imports Matrix Validator
File: Smart Imports - matriz de oportunidades - v3 aut(28).xlsx
Schema: full-matrix-v3
Result: FAIL

Errors: 1
Warnings: 0
Info: 15

[ERROR] MV-ID-002 Evaluaciones!A10
ID inválido: EV-0009
Esperado: EVAL-0000
Acción: reemplazar el ID de la fila existente por EVAL-0009.

La matriz no debe declararse vigente hasta corregir los errores.
```

## 20. Salida JSON

Estructura mínima:

```json
{
  "reportVersion": "1.0",
  "schema": "full-matrix-v3",
  "file": {
    "name": "Smart Imports - matriz de oportunidades - v3 aut(28).xlsx"
  },
  "result": "FAIL",
  "summary": {
    "errors": 1,
    "warnings": 0,
    "info": 15
  },
  "findings": []
}
```

El JSON no debe incluir contenido confidencial innecesario. Los valores de celdas sólo se incluyen cuando son necesarios para explicar el hallazgo.

## 21. Códigos de salida

| Exit code | Significado |
|---:|---|
| `0` | `PASS` o `PASS_WITH_WARNINGS` sin `--strict`. |
| `1` | `FAIL` por errores de validación. |
| `2` | `TECHNICAL_FAILURE`. |
| `3` | Advertencias tratadas como fallo mediante `--strict`. |

## 22. Flujo funcional

```text
Seleccionar XLSX
↓
Abrir workbook
↓
Identificar schema
↓
Validar hojas
↓
Validar columnas
↓
Validar filas e IDs
↓
Validar valores
↓
Validar relaciones
↓
Validar fórmulas
↓
Generar findings
↓
Calcular resultado
↓
Mostrar o guardar reporte
```

La validación debe continuar después de encontrar un error siempre que sea técnicamente posible, para producir un reporte completo en una sola ejecución.

## 23. Criterios de aceptación del MVP

El MVP se considera funcionalmente aceptado cuando:

1. Detecta `EV-0009` en una copia de `aut(28)` como `MV-ID-002`.
2. La matriz corregida `aut(29)` no presenta errores bloqueantes en IDs ni relaciones.
3. Detecta un ID duplicado agregado intencionalmente.
4. Detecta una hoja requerida eliminada.
5. Detecta una columna renombrada.
6. Detecta una columna movida de posición.
7. Detecta una referencia a Producto Base inexistente.
8. Detecta una referencia ML inexistente desde `Competencia ML`.
9. Detecta una cotización inexistente desde `Simulación Margen`.
10. Detecta un score de Evaluación fuera de 1–5.
11. Detecta una confianza no permitida.
12. Detecta una fila parcial sin ID.
13. Detecta fórmulas faltantes en una fila activa de `Nichos`.
14. Detecta tokens de error de fórmula.
15. Produce reporte de texto y JSON con el mismo conteo.
16. No modifica el archivo validado.
17. Finaliza con el exit code correcto.
18. Incluye tests automatizados para todas las reglas bloqueantes del MVP.
19. Las tres hojas `Resumen *` poseen estructura tabular y contrato ejecutable.
20. CI valida fixtures públicos sin depender de matrices privadas.
21. El reporte ya no declara reglas parcialmente implementadas.

## 24. Casos de prueba derivados del trabajo real

| Caso | Resultado esperado |
|---|---|
| `Evaluaciones!A10 = EV-0009` | ERROR `MV-ID-002`. |
| Dos filas con `COMP-0046` | ERROR `MV-ID-003`. |
| Publicación con `BASE-TRAVEL-999` | ERROR `MV-REF-001`. |
| Fila activa de Nicho sin fórmulas | ERROR `MV-FORM-001`. |
| Columna agregada al final | WARNING `MV-COL-005`. |
| Columna insertada antes de `Observaciones` | ERROR `MV-COL-004`. |
| `TIME` completado sin minutos y precisión `No medido` | Válido. |
| `TIME` completado sin minutos y precisión `Exacta` | ERROR `MV-ROW-002`. |
| Evidencia con `ML-SEARCH-*` | Permitida según tipo de fuente; no exigir existencia en Publicaciones ML. |
| Nueva hoja de análisis auxiliar | WARNING `MV-SHEET-002`. |

## 25. Métricas de éxito

- Cantidad de errores detectados antes de declarar una matriz vigente.
- Reducción del tiempo de revisión manual.
- Reducción de correcciones posteriores.
- Cantidad de importaciones que pasan sin referencias rotas.
- Cobertura de reglas mediante tests.
- Tiempo de ejecución sobre la matriz vigente.
- Cantidad de falsos positivos.
- Cantidad de reglas surgidas de errores reales.

## 26. Evolución prevista

### 0.1 — Full Matrix Validator

- Estructura.
- IDs.
- Valores.
- Referencias.
- Fórmulas.
- CLI y JSON.

### 0.2 — Importable Validator

- Archivos parciales.
- Comparación contra matriz base.
- Detección de colisiones antes de importar.
- Validación de que las correcciones reemplazan filas.

### 0.3 — Duplicate and Normalization Assistant

- Posibles productos base duplicados.
- Variantes.
- Nombres normalizados.
- Recomendación no bloqueante.

### 0.4 — Workflow Integration

- n8n.
- CI.
- Reportes históricos.
- Gate previo a publicar una nueva matriz.

## 27. Preguntas abiertas

1. ¿El schema debe vivir inicialmente como objetos TypeScript o como JSON/YAML externo?
2. ¿Las columnas nuevas al final deben ser siempre warning o requerir una allowlist?
3. ¿Conviene incorporar un checksum del archivo en el reporte para trazabilidad?
4. ¿El futuro perfil de importables debe exigir siempre una matriz base?
5. ¿Los prefijos de fuentes estratégicas deben registrarse en una hoja o en configuración?

Las preguntas 1, 3, 4 y 5 ya fueron resueltas por la implementación y los ADR del repositorio de software. Las decisiones restantes deben actualizarse al cerrar el siguiente schema.

## 28. Documentos relacionados

- [SI-DOC-001 — Documentation Standards](../standards/si-doc-001-documentation-standards.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-ROADMAP-001 — Pilot Closure, Niche 2 and Engine MVP](../08-roadmaps/si-roadmap-001-pilot-closure-niche-2-engine-mvp.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)
- [SI-DECISION-006 — Build the Intelligence Engine Incrementally](../09-decision-log/si-decision-006-build-intelligence-engine-incrementally.md)

## 29. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-24 | Primera especificación funcional del Matrix Validator basada en la matriz v3 y en errores observados durante los Nichos 1 y 2. |
| 1.0.0 | 2026-07-24 | Especificación funcional aprobada por el Founder. Las decisiones de repositorio y arquitectura mínima se derivan a SI-DECISION-009 y SI-TECH-001. |
| 1.1.0 | 2026-08-03 | Estado as-built de v3/v4 y normalización de fuentes. |
| 1.2.0 | 2026-08-04 | Adopción de aut31/v5, tipos, rangos, consistencia y vistas derivadas. |
