---
id: si-bim-proc-001
title: Marketplace Evidence Processing Procedure
description: Procedimiento operativo provisorio para procesar PDFs, publicaciones de marketplace y fuentes externas en la Matriz de Oportunidades de Smart Imports.
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-10
updated: 2026-07-10
tags:
  - business-intelligence
  - procedure
  - evidence
  - marketplace
  - google-sheets
  - automation
  - n8n
related:
  - si-bim-001
  - si-bim-002
  - si-bim-readme
phase: business-intelligence
---

# SI-BIM-PROC-001 — Marketplace Evidence Processing Procedure

> **La investigación la decide una persona. La carga operativa debe tender a automatizarse.**

---

## 1. Propósito

Este documento registra el procedimiento operativo provisorio utilizado para procesar evidencia de marketplaces y fuentes externas dentro de Smart Imports.

Nació durante el piloto **Energía Solar Portátil**, al detectar que una misma publicación de Mercado Libre podía servir tanto para evaluar **Demanda** como **Competencia**.

El objetivo es evitar carga manual repetitiva, mantener trazabilidad y preparar el proceso para una futura automatización con n8n o con una plataforma propia.

---

## 2. Alcance

Este procedimiento aplica a la etapa inicial de investigación de nichos, especialmente cuando se trabaja con:

- PDFs de Mercado Libre.
- PDFs de tiendas externas.
- Capturas o archivos exportados de páginas comerciales.
- Google Trends.
- Google Search.
- Evidencias de demanda.
- Evidencias de competencia.

No define todavía scraping automático, integración con APIs ni arquitectura definitiva de la futura plataforma.

---

## 3. Principio operativo

La regla principal es:

```text
Una fuente se carga una vez como dato base.
Luego se referencia desde Evidencias, Competencia o Evaluaciones.
```

No se debe duplicar la misma información cruda en varias hojas.

---

## 4. Capas de información

La matriz debe separar datos crudos, análisis y decisión.

```text
Publicaciones ML / Fuentes Externas
        ↓
Productos Base
        ↓
Competencia ML / Competencia Externa
        ↓
Evidencias
        ↓
Evaluaciones
        ↓
Nichos
```

### 4.1 Datos crudos

- `Publicaciones ML`
- `Fuentes Externas`

### 4.2 Agrupación y análisis

- `Productos Base`
- `Competencia ML`
- `Competencia Externa`

### 4.3 Evaluación y decisión

- `Evidencias`
- `Evaluaciones`
- `Nichos`

---

## 5. Reglas de IDs

Cada hoja tiene IDs primarios únicos.

```text
ML-xxxx       único en Publicaciones ML
EXT-xxxx      único en Fuentes Externas
BASE-xxxx     único en Productos Base
COMP-xxxx     único en Competencia ML
COMPEXT-xxxx  único en Competencia Externa
EVID-xxxx     único en Evidencias
EVAL-xxxx     único en Evaluaciones
```

Un ID primario no debe repetirse dentro de su hoja.

Los IDs sí pueden repetirse como referencias en otras hojas.

Ejemplo:

```text
BASE-PB-004 puede aparecer en varias publicaciones o fuentes externas.
Pero en Productos Base sólo debe existir una fila con BASE-PB-004.
```

---

## 6. Regla para Productos Base

`Productos Base` no es una lista de publicaciones.

Sólo debe crearse un producto base nuevo cuando aparece un producto realmente diferente.

Si una publicación o fuente externa corresponde a un producto ya detectado:

```text
No crear un nuevo Producto Base.
Referenciar el ID Producto Base existente.
```

Ejemplo aplicado:

```text
Gadnic Power Bank B60+ en Mercado Libre
Gadnic Power Bank B60+ en Frávega
Gadnic Power Bank B60+ en Carrefour

→ Un solo Producto Base.
→ Varias fuentes relacionadas.
```

---

## 7. Reglas para archivos importables

Cuando se genera un XLSX para importar o copiar a la matriz:

1. Usar siempre la matriz actual exportada desde Google Sheets como fuente de verdad.
2. Respetar exactamente nombres de hojas existentes.
3. Respetar exactamente nombres y orden de columnas existentes.
4. No insertar columnas nuevas en el medio.
5. Si hace falta una columna nueva, agregarla al final.
6. No duplicar IDs primarios.
7. Mantener `Evidencias` como capa central para `Evaluaciones`.
8. Crear filas de `Evidencias` tanto para Demanda como para Competencia.

---

## 8. Procedimiento por tanda

Cada tanda corresponde a una subcategoría.

Ejemplos:

- Kits solares.
- Ventiladores solares.
- Power banks solares.
- Paneles solares portátiles.

### Paso 1 — Recibir insumos

El Founder entrega:

- Matriz actual exportada desde Google Sheets.
- PDFs o fuentes de la subcategoría.

### Paso 2 — Clasificar fuente

Cada PDF debe clasificarse como:

```text
Mercado Libre → Publicaciones ML + Competencia ML
Fuente externa → Fuentes Externas + Competencia Externa
```

### Paso 3 — Extraer datos crudos

Para ML se extrae:

- Producto.
- Vendedor.
- Marca.
- Precio.
- Ventas visibles.
- Rating.
- Opiniones.
- Link o archivo.
- Garantía.
- Envío / cuotas.
- Observaciones crudas.

Para fuentes externas se extrae:

- Fuente.
- Producto.
- Vendedor o tienda.
- Marca.
- Precio.
- Stock o disponibilidad.
- Garantía.
- Link o archivo.
- Relación con producto base.
- Observaciones.

### Paso 4 — Identificar Producto Base

Determinar si el producto es:

- Producto base nuevo.
- Variante de producto existente.
- Duplicado claro.
- Producto relacionado pero distinto.

### Paso 5 — Crear evidencias de Demanda

Las fuentes con señales comerciales relevantes deben generar registros en `Evidencias` con:

```text
Criterio: Demanda
Fuente: Mercado Libre / Fuente Externa
Fuente ID: ML-xxxx / EXT-xxxx
```

### Paso 6 — Crear análisis de Competencia

Para fuentes ML:

```text
Competencia ML
```

Para fuentes externas:

```text
Competencia Externa
```

### Paso 7 — Crear evidencias de Competencia

Cada análisis competitivo relevante debe generar un registro en `Evidencias` con:

```text
Criterio: Competencia
Fuente: Competencia ML / Competencia Externa
Fuente ID: COMP-xxxx / COMPEXT-xxxx
```

### Paso 8 — Generar archivo importable

El archivo debe contener sólo las hojas necesarias para esa tanda.

Ejemplo:

```text
Publicaciones ML
Fuentes Externas
Productos Base
Competencia ML
Competencia Externa
Evidencias
Resumen Competencia
```

### Paso 9 — Revisión humana

El Founder revisa:

- Si los productos base están bien agrupados.
- Si los IDs son únicos.
- Si las evidencias son útiles.
- Si la lectura de competencia tiene sentido.

### Paso 10 — Cierre del criterio

Sólo después de procesar todas las subcategorías relevantes se completa `Evaluaciones`.

---

## 9. Prompt operativo para cada tanda

```text
Te adjunto la matriz actual exportada desde Google Sheets y los PDFs de la subcategoría [NOMBRE].

Necesito que generes un XLSX importable compatible con la matriz, respetando exactamente nombres y orden de columnas existentes.

No dupliques IDs primarios dentro de ninguna hoja. Si una fuente corresponde a un producto base existente, referencialo mediante ID Producto Base y no crees una nueva fila en Productos Base.

Completá las hojas necesarias para Demanda y Competencia:
- Publicaciones ML si son fuentes de Mercado Libre
- Fuentes Externas si son fuentes fuera de Mercado Libre
- Productos Base sólo si aparecen productos base nuevos
- Evidencias para Demanda y Competencia
- Competencia ML o Competencia Externa según corresponda

Si necesitás agregar una columna nueva, agregala al final de la hoja.
```

---

## 10. Ejemplo aplicado: Power Banks solares

Power Banks solares fue la primera tanda donde el procedimiento quedó más estable.

### Hallazgos operativos

- Había muchas publicaciones similares.
- Varias capacidades declaradas parecían difíciles de validar.
- Aparecieron marcas fuertes como Gadnic y Mixio.
- El mismo producto Gadnic aparecía en Mercado Libre y en tiendas externas.
- Fue necesario agrupar por producto base para no inflar competencia.

### Resultado metodológico

La tanda confirmó que:

```text
No conviene contar publicaciones.
Conviene contar productos base + vendedores + canales + nivel commodity.
```

---

## 11. Preparación para n8n

Este procedimiento puede automatizarse con un flujo futuro:

```text
Google Drive Folder
        ↓
PDF nuevo
        ↓
Extracción de texto
        ↓
OpenAI: estructurar fuente
        ↓
OpenAI: detectar Producto Base
        ↓
OpenAI: generar Evidencias
        ↓
OpenAI: generar Competencia ML / Externa
        ↓
Google Sheets: insertar filas con Estado = Pendiente
        ↓
Revisión humana
```

La automatización no debe eliminar la revisión humana. Debe reducir carga operativa.

---

## 12. Casos límite

### Caso 1 — Fuente externa del mismo producto ML

No crear nuevo producto base. Referenciar el existente.

### Caso 2 — Producto visualmente igual con distinta marca

Marcar como posible variante o clon. No decidir sin revisar especificaciones.

### Caso 3 — Misma publicación con distinto precio o cuotas

Registrar como variante comercial si aporta evidencia útil.

### Caso 4 — Fuente externa sin ventas visibles

Puede servir para Competencia y presencia multicanal, pero no necesariamente como evidencia fuerte de Demanda.

### Caso 5 — Producto de ticket o uso distinto

Evaluar si pertenece a otra subcategoría o nicho.

---

## 13. Related Documents

- `criteria/si-bim-001-demand-evaluation.md`
- `criteria/si-bim-002-competition-evaluation.md`
- `README.md` del Business Intelligence Manual.

---

## 14. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-10 | Versión inicial del procedimiento operativo para procesamiento de evidencias de marketplace y fuentes externas. |
