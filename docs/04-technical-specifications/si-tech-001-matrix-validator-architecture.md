---
id: si-tech-001
title: Matrix Validator Technical Architecture
description: Arquitectura técnica mínima del Matrix Validator y base inicial del repositorio privado Smart Imports Intelligence Engine.
version: 0.1.1
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-24
updated: 2026-07-24
tags:
  - technical-specification
  - matrix-validator
  - intelligence-engine
  - typescript
  - nodejs
  - cli
  - architecture
related:
  - si-func-001
  - si-decision-006
  - si-decision-009
  - si-agent-001
  - si-roadmap-002
audience:
  - founder
  - developer
  - assistant
phase: foundation
---

# SI-TECH-001 — Arquitectura técnica del Matrix Validator

> El primer módulo debe ser pequeño, verificable y suficientemente modular para convertirse en la base del Intelligence Engine.

## 1. Propósito

Este documento define la arquitectura técnica mínima para implementar el `Matrix Validator`, primer MVP del Smart Imports Intelligence Engine.

La especificación traduce `SI-FUNC-001` a decisiones de implementación sobre:

- Repositorio.
- Runtime.
- Lenguaje.
- Dependencias.
- Estructura de carpetas.
- Puertos y adaptadores.
- Schemas.
- Reglas.
- Reportes.
- CLI.
- Testing.
- Seguridad.
- CI.
- Evolución futura.

No define todavía la implementación completa de cada regla.

## 2. Decisiones aprobadas que condicionan la arquitectura

### Repositorios

```text
smart-imports
├── Public
├── Documentación y gobierno
└── Fuente documental de verdad

smart-imports-engine
├── Private
├── Código, tests y releases
└── Producto ejecutable
```

La separación está registrada en `SI-DECISION-009`.

### Modo de ejecución

```text
MVP 0.1: CLI local
Hosting: none
Database: none
API: none
Frontend: none
```

### Política de escritura

El proceso será read-only respecto del archivo XLSX de entrada.

El adapter puede utilizar una librería capaz de escribir XLSX, pero la aplicación no expondrá operaciones de escritura durante el MVP.

## 3. Stack técnico

| Área | Decisión |
|---|---|
| Runtime | Node.js 24 LTS |
| Lenguaje | TypeScript 6 |
| Módulos | ESM |
| Package manager | pnpm 11 |
| CLI | Commander 15 |
| XLSX adapter inicial | ExcelJS 4.4 |
| Runtime schemas | Zod 4 |
| Tests | Vitest 4 |
| Hash de archivo | `node:crypto` con SHA-256 |
| Persistencia | Ninguna |
| Hosting | Ninguno |
| CI | GitHub Actions después del primer `pnpm-lock.yaml` |

### 3.1 Node.js

Se selecciona Node.js 24 LTS.

Motivos:

- Línea LTS vigente.
- Commander 15 requiere Node moderno.
- Permite una vida útil mayor que Node 22.
- Node 20 ya no debe utilizarse como runtime objetivo del proyecto.
- Es compatible con el enfoque ESM y las herramientas seleccionadas.

El repositorio incluirá:

```text
.nvmrc
```

con:

```text
24
```

La versión patch no se fija en `.nvmrc`; el `package.json` declara el rango mínimo compatible y CI podrá fijar la línea 24.

### 3.2 TypeScript

Se utiliza TypeScript con configuración estricta.

Objetivos:

- Modelar schemas y findings con tipos explícitos.
- Evitar valores `any`.
- Detectar referencias opcionales mal tratadas.
- Facilitar evolución hacia paquetes o API.
- Mantener separación entre dominio, aplicación e infraestructura.

### 3.3 pnpm

Se utiliza pnpm como package manager del proyecto.

Motivos:

- Es la preferencia técnica del Founder.
- Mantiene un store global y enlaces de contenido que reducen duplicación en disco.
- Aplica una resolución estricta de dependencias, útil para detectar imports no declarados.
- Permite evolucionar a workspaces sin cambiar de package manager cuando el Engine incorpore más aplicaciones o paquetes.
- Su lockfile es determinista y debe versionarse.

Reglas:

- El repositorio debe incluir `pnpm-lock.yaml`.
- `package.json` debe fijar una versión reproducible mediante `packageManager`.
- La línea inicial será pnpm 11, compatible con Node.js 24.
- CI debe utilizar `pnpm install --frozen-lockfile` después de que exista el lockfile.
- No se incorporan workspaces en el MVP.
- El paquete no se publica en el registro npm.

### 3.4 ExcelJS

ExcelJS será el adapter XLSX inicial porque permite leer workbooks, worksheets, celdas, estilos y modelos de fórmulas.

Sin embargo, antes de implementar las reglas se realizará un spike técnico obligatorio.

El spike debe confirmar sobre copias locales:

1. Lectura de las 15 hojas.
2. Preservación del orden.
3. Lectura exacta de encabezados.
4. Distinción entre celda vacía y string vacío.
5. Lectura de fecha Excel y fecha en texto.
6. Lectura de fórmulas.
7. Acceso al resultado cacheado de fórmulas.
8. Lectura de hojas con espacios y caracteres acentuados.
9. Tiempo y memoria sobre la matriz vigente.
10. Ausencia de modificaciones sobre el archivo de entrada.

Si el adapter no cumple estos puntos, debe reemplazarse detrás del puerto `WorkbookReaderPort` sin alterar las reglas de dominio.

### 3.5 Zod

Zod se utiliza para validar:

- Configuración CLI normalizada.
- Definición de schemas ejecutables.
- Estructura del reporte JSON.
- Tipos de hallazgos serializables.
- Configuración externa futura.

Zod no sustituye las reglas de negocio del Validator. Una referencia rota requiere una regla específica, no sólo un schema de objeto.

### 3.6 Commander

Commander se utiliza únicamente en la capa de presentación CLI.

La lógica de validación no debe depender de Commander, `process.argv` ni `process.exit`.

### 3.7 Vitest

Vitest se utiliza para:

- Tests unitarios de reglas.
- Tests de contratos.
- Tests de integración del adapter.
- Tests del resultado y exit code.
- Fixtures sintéticos.
- Pruebas privadas locales opcionales.

## 4. Forma inicial del repositorio

El repositorio comienza como una aplicación TypeScript de un solo paquete.

No se utiliza Turborepo ni estructura de monorepo.

```text
smart-imports-engine/
├── src/
│   ├── modules/
│   │   └── matrix-validator/
│   │       ├── domain/
│   │       ├── application/
│   │       ├── infrastructure/
│   │       │   └── xlsx/
│   │       └── presentation/
│   │           └── cli/
│   ├── schemas/
│   │   └── full-matrix-v3/
│   └── shared/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│       ├── synthetic/
│       └── private/
├── data/
├── reports/
├── docs/
│   ├── adr/
│   ├── development/
│   └── testing/
├── .github/
│   └── workflows/
├── package.json
├── pnpm-lock.yaml
├── tsconfig.json
├── vitest.config.ts
├── .nvmrc
├── .gitignore
├── README.md
└── CHANGELOG.md
```

### 4.1 Criterio para migrar a workspaces

La migración a:

```text
apps/
packages/
```

sólo se evalúa cuando exista al menos uno de estos escenarios:

- CLI y API independientes.
- Frontend y backend.
- Paquete de schemas reutilizado por más de una aplicación.
- Workers con releases propios.
- Integraciones que necesiten despliegues separados.

## 5. Arquitectura interna

Se utilizará una arquitectura modular inspirada en puertos y adaptadores, sin aplicar ceremonias innecesarias.

```text
CLI
↓
ValidateMatrixUseCase
↓
ValidationPipeline
├── Schema rules
├── ID rules
├── Reference rules
├── Value rules
└── Formula rules
↓
ValidationReport
↓
TextReportRenderer / JsonReportRenderer
```

El acceso al XLSX se realiza mediante:

```text
WorkbookReaderPort
↑
ExcelJsWorkbookReader
```

### 5.1 Domain

Contiene conceptos puros:

- `Finding`.
- `FindingSeverity`.
- `RuleCode`.
- `ValidationResult`.
- `ValidationReport`.
- `MatrixSchema`.
- `SheetSchema`.
- `ColumnSchema`.
- `IdContract`.
- `ReferenceContract`.
- `ValidationRule`.

No importa ExcelJS, Commander, filesystem ni variables de entorno.

### 5.2 Application

Coordina el caso de uso:

- Verifica archivo y extensión.
- Calcula checksum.
- Solicita lectura al adapter.
- Selecciona schema.
- Ejecuta reglas por fases.
- Acumula hallazgos.
- Calcula resultado.
- Devuelve el reporte.

No llama `process.exit`.

### 5.3 Infrastructure

Implementa detalles externos:

- Lectura XLSX mediante ExcelJS.
- Acceso al filesystem.
- Hash SHA-256.
- Escritura opcional del reporte.
- Medición de tiempo.

No contiene decisiones sobre severidad o significado comercial.

### 5.4 Presentation

Implementa:

- Comandos.
- Opciones.
- Formato de salida.
- Mensajes de consola.
- Traducción del resultado a exit code.

## 6. Modelo del workbook normalizado

Las reglas no deben depender directamente de objetos ExcelJS.

El adapter transformará el archivo a un modelo mínimo controlado:

```typescript
interface WorkbookSnapshot {
  file: WorkbookFileMetadata;
  sheets: SheetSnapshot[];
}

interface SheetSnapshot {
  name: string;
  position: number;
  rowCount: number;
  columnCount: number;
  rows: RowSnapshot[];
}

interface RowSnapshot {
  index: number;
  cells: CellSnapshot[];
}

interface CellSnapshot {
  row: number;
  column: number;
  address: string;
  rawValue: unknown;
  normalizedValue: unknown;
  formula?: string;
  formulaResult?: unknown;
  numberFormat?: string;
}
```

Ventajas:

- Las reglas pueden probarse sin ExcelJS.
- El adapter puede reemplazarse.
- Los fixtures unitarios son objetos pequeños.
- El reporte conserva ubicación exacta.
- Las decisiones de normalización quedan centralizadas.

## 7. Schema ejecutable

### 7.1 Ubicación

```text
src/schemas/full-matrix-v3/
```

### 7.2 Forma inicial

El schema vivirá como objetos TypeScript tipados y validados con Zod.

No se utilizará YAML en el MVP.

Motivos:

- Menor complejidad de carga.
- Autocompletado.
- Refactor seguro.
- Tipos compartidos.
- Revisión mediante pull requests.
- No existe todavía un usuario no técnico que necesite editar el schema.

Ejemplo conceptual:

```typescript
export const fullMatrixV3Schema = {
  id: "full-matrix-v3",
  version: "1.0.0",
  sheets: [
    {
      name: "Evaluaciones",
      required: true,
      primaryKey: "Evaluación ID",
      columns: []
    }
  ]
} satisfies MatrixSchema;
```

### 7.3 Versionado

Se separan dos versiones:

```text
Application version
Schema version
```

El reporte debe incluir ambas.

Una modificación incompatible de columnas crea una nueva versión del schema.

Una corrección interna de una regla puede incrementar la versión de aplicación sin modificar el schema.

### 7.4 Columnas agregadas al final

La política inicial permanece:

- Columna agregada al final: `WARNING`.
- Columna insertada, movida o renombrada: `ERROR`.

El schema podrá incorporar posteriormente una allowlist de extensiones reconocidas.

## 8. Contrato de regla

Cada regla implementará un contrato equivalente a:

```typescript
interface ValidationRule {
  readonly code: RuleCode;
  readonly phase: ValidationPhase;
  validate(context: ValidationContext): Finding[];
}
```

Fases:

```text
file
sheet
column
row
id
value
reference
formula
consistency
```

Reglas:

- No lanzan excepciones por datos inválidos esperables.
- Devuelven findings.
- No modifican el snapshot.
- No escriben en consola.
- No dependen del orden accidental de ejecución, salvo que lo declare la fase.
- Deben tener tests unitarios.

## 9. Pipeline

Orden:

```text
1. File preflight
2. Workbook load
3. Sheet validation
4. Column validation
5. Row shape validation
6. Primary ID validation
7. Value validation
8. Reference validation
9. Formula validation
10. Consistency warnings
11. Report generation
```

Si una fase no puede ejecutarse por falta de estructura:

- Debe registrar el error causal.
- Debe omitir reglas dependientes.
- No debe generar cientos de errores derivados que oculten el problema principal.

Ejemplo:

> Si falta `Productos Base`, se informa `MV-SHEET-001` y se omiten referencias hacia esa hoja con una nota de diagnóstico, en lugar de marcar cada producto como inexistente.

## 10. Findings y reporte

### 10.1 Finding

El modelo sigue el contrato funcional de `SI-FUNC-001`.

Debe ser serializable y estable.

No debe contener:

- Objetos de ExcelJS.
- Stack traces en reportes normales.
- Valores confidenciales completos cuando no sean necesarios.
- Paths absolutos en modo público.

### 10.2 Checksum

El reporte incluirá SHA-256 del archivo de entrada.

Objetivos:

- Identificar exactamente qué archivo fue validado.
- Comparar reportes.
- Evitar confusión entre archivos con el mismo nombre.
- Mantener trazabilidad sin copiar la matriz al repositorio.

### 10.3 Report renderers

Se implementarán dos adapters:

```text
TextReportRenderer
JsonReportRenderer
```

Ambos reciben el mismo `ValidationReport`.

El conteo y resultado deben ser idénticos.

## 11. CLI

Comando principal:

```bash
smart-imports validate <file>
```

Opciones:

```text
--schema <id>
--format <text|json>
--output <path>
--strict
```

Ejemplos:

```bash
smart-imports validate "./data/matrix.xlsx"

smart-imports validate "./data/matrix.xlsx"   --schema full-matrix-v3   --format json   --output "./reports/matrix-report.json"
```

Durante desarrollo:

```bash
pnpm validate -- "./data/matrix.xlsx"
```

El binario público dentro del repositorio será:

```text
smart-imports
```

El módulo se seguirá llamando:

```text
matrix-validator
```

Esto permite agregar futuros subcomandos:

```text
smart-imports suppliers analyze
smart-imports margin simulate
smart-imports rfq generate
```

## 12. Exit codes

La capa CLI traduce el resultado:

| Resultado | Exit code |
|---|---:|
| `PASS` | 0 |
| `PASS_WITH_WARNINGS` | 0 |
| `FAIL` | 1 |
| `TECHNICAL_FAILURE` | 2 |
| Warning con `--strict` | 3 |

Los casos de uso nunca llaman `process.exit`.

## 13. Manejo de errores

### Errores de validación

Se convierten en findings.

Ejemplos:

- ID inválido.
- Referencia rota.
- Score fuera de rango.
- Fórmula faltante.

### Fallos técnicos

Se convierten en `TECHNICAL_FAILURE`.

Ejemplos:

- Archivo inexistente.
- Archivo protegido.
- XLSX corrupto.
- Error inesperado de lectura.
- Falta de permisos.

En modo normal se muestra un mensaje controlado.

El stack trace sólo aparece mediante una opción futura `--debug`.

## 14. Fechas y números

### Fechas

El adapter conserva:

- Valor crudo.
- Tipo detectado.
- Number format.
- Valor normalizado cuando sea seguro.

No se transforma automáticamente un texto ambiguo como:

```text
07/08/2026
```

La regla produce una advertencia o error según el contrato funcional.

### Números

El adapter no elimina silenciosamente:

- Puntos.
- Comas.
- Símbolos monetarios.
- Espacios.

La normalización debe devolver evidencia de cómo interpretó el valor.

Cuando exista ambigüedad regional, la regla no adivina.

## 15. Fórmulas

El adapter debe exponer:

- Fórmula.
- Resultado cacheado, si existe.
- Dirección.
- Tipo de celda.

El MVP no recalcula fórmulas.

Reglas iniciales:

- Presencia de fórmula en rangos obligatorios.
- Token de error.
- Comparación estructural con la fórmula patrón.
- Advertencia cuando falta resultado cacheado.

La comparación de fórmulas debe normalizar referencias relativas antes de marcar diferencias. Una comparación textual directa puede producir falsos positivos al copiar fórmulas entre filas.

## 16. Testing

### 16.1 Capas

```text
Unit
Contract
Integration
Private local
```

### 16.2 Fixtures versionables

Dentro de Git:

```text
tests/fixtures/synthetic/
```

Contenido:

- Workbook mínimo válido.
- ID inválido.
- ID duplicado.
- Hoja faltante.
- Columna movida.
- Referencia rota.
- Fórmula faltante.
- Fecha ambigua.

Los archivos deben ser sintéticos y pequeños.

### 16.3 Fixtures privados

Fuera de Git:

```text
tests/fixtures/private/
```

Puede contener localmente:

- `aut(28)`.
- `aut(29)`.
- Copias controladas de matrices reales.

La carpeta se ignora excepto por un README.

Los tests privados se ejecutan sólo cuando existe:

```text
SMART_IMPORTS_PRIVATE_FIXTURES_DIR
```

CI nunca depende de datos privados.

### 16.4 Regla de no modificación

Los tests de integración deben calcular el checksum antes y después de validar.

Ambos deben coincidir.

### 16.5 Cobertura

Objetivo del MVP:

- 100% de las reglas bloqueantes con al menos un test positivo y uno negativo.
- Cobertura general como señal, no como sustituto de buenos casos.

## 17. Seguridad

### Secretos

No deben existir secretos en el MVP.

`.env` está ignorado.

### Datos

`.gitignore` bloqueará por defecto:

```text
data/**
reports/private/**
tests/fixtures/private/**
*.xlsx
*.xls
*.pdf
```

Se permitirán explícitamente fixtures sintéticos controlados.

### Logs

El reporte de consola no debe mostrar filas completas.

Sólo debe incluir los valores necesarios para explicar el hallazgo.

### Dependencias

Antes de cada release:

```bash
pnpm audit
```

Las actualizaciones mayores se revisan conscientemente, especialmente ExcelJS y Commander.

## 18. CI inicial

GitHub Actions se habilitará después de generar y commitear `pnpm-lock.yaml`.

Pipeline:

```text
checkout
setup-pnpm 11
setup-node 24 con caché pnpm
pnpm install --frozen-lockfile
pnpm typecheck
pnpm test
pnpm build
```

No se suben matrices reales como artifacts.

Los reportes sintéticos de test pueden conservarse si no contienen información sensible.

## 19. Desarrollo local

Secuencia inicial:

```bash
nvm install 24
nvm use
corepack enable pnpm
pnpm install
pnpm typecheck
pnpm test
pnpm build
```

El primer `pnpm install` debe generar `pnpm-lock.yaml`, que se commiteará antes de activar CI.

## 20. Plan de implementación

### Fase 0 — Foundation

- Crear repositorio privado.
- Incorporar scaffold.
- Habilitar pnpm mediante Corepack.
- Generar `pnpm-lock.yaml`.
- Confirmar build y tests.
- Activar CI.

### Fase 1 — XLSX adapter spike

- Implementar `WorkbookReaderPort`.
- Implementar adapter ExcelJS.
- Probar lectura contra matrices privadas.
- Documentar limitaciones.
- Decidir `go/no-go` de ExcelJS.

### Fase 2 — Estructura

- `MV-FILE-*`.
- `MV-SHEET-*`.
- `MV-COL-*`.
- Modelo normalizado.
- Reporte base.

### Fase 3 — IDs y relaciones

- `MV-ID-*`.
- `MV-REF-*`.
- Índices de registros.
- Caso `EV-0009`.

### Fase 4 — Valores y filas

- `MV-VAL-*`.
- `MV-ROW-*`.
- Estados por hoja.
- Fechas y números.

### Fase 5 — Fórmulas y consistencia

- `MV-FORM-*`.
- `MV-CONS-*`.
- Casos de Nichos.
- Tandas.

### Fase 6 — Cierre MVP

- Text renderer.
- JSON renderer.
- Strict mode.
- Exit codes.
- Documentación de uso.
- Validación privada de `aut(29)`.

## 21. Criterios técnicos de aceptación

La arquitectura se considera correctamente implementada cuando:

1. El dominio no importa ExcelJS ni Commander.
2. Las reglas se prueban sobre snapshots sintéticos.
3. El adapter XLSX puede reemplazarse mediante un puerto.
4. La CLI y JSON producen el mismo resultado.
5. El archivo de entrada conserva el mismo SHA-256.
6. Los errores estructurales evitan cascadas engañosas.
7. CI funciona sin matrices reales.
8. `aut(28)` detecta `MV-ID-002` en test privado.
9. `aut(29)` no presenta errores bloqueantes de IDs y referencias en test privado.
10. No existe persistencia ni servicio permanente.
11. El repositorio no contiene datos comerciales reales.
12. El módulo puede evolucionar sin crear un repositorio nuevo.

## 22. Riesgos técnicos

| Riesgo | Mitigación |
|---|---|
| ExcelJS no expone algún detalle requerido | Spike temprano y puerto reemplazable |
| Fórmulas cacheadas desactualizadas | Informar limitación y no recalcular |
| Falsos positivos por fórmula relativa | Normalización estructural |
| Cascada de errores | Dependencias entre fases |
| Fixture real subido por error | `.gitignore`, revisión y tests sintéticos |
| Schema acoplado al código | Registry versionado y contrato explícito |
| Crecimiento prematuro del Engine | Un paquete y un módulo hasta existir necesidad real |
| Node local desactualizado | `.nvmrc` y `engines` |
| Dependencias sin lockfile | Generarlo antes de activar CI |

## 23. Decisiones técnicas derivadas

Las preguntas abiertas de `SI-FUNC-001` se resuelven inicialmente así:

1. **Schema:** objetos TypeScript tipados y validados con Zod.
2. **Columnas nuevas al final:** warning hasta actualizar el schema.
3. **Checksum:** SHA-256 incluido en el reporte.
4. **Importables futuros:** requerirán matriz base mediante `--against`.
5. **Prefijos externos:** configuración versionada; no nueva hoja en el MVP.
6. **Fixtures reales:** locales y fuera de Git.
7. **Hosting:** no existe en MVP 0.1.
8. **Base de datos:** no existe en MVP 0.1.

## 24. Evolución futura

### API

Se considera cuando n8n u otros clientes necesiten ejecución remota.

### Container

Se considera antes de desplegar el primer servicio persistente.

### Workspaces

Se consideran al existir múltiples aplicaciones.

### Persistencia

Se considera cuando sea necesario:

- Historial de reportes.
- Comparación de matrices.
- Usuarios.
- Jobs.
- Proveedores.
- Cotizaciones.
- RAG.

La base de datos no se elige antes de conocer esos casos de uso.

## 25. Referencias técnicas

- Node.js Releases.
- TypeScript 6 release notes.
- Commander documentation.
- ExcelJS repository and workbook model.
- Zod documentation.
- Vitest documentation.

Las versiones exactas deben quedar fijadas por `pnpm-lock.yaml` y el campo `packageManager` de `package.json`.

## 26. Documentos relacionados

- [SI-FUNC-001 — Matrix Validator](../03-functional-specifications/si-func-001-matrix-validator.md)
- [SI-DECISION-006 — Build the Intelligence Engine Incrementally](../09-decision-log/si-decision-006-build-intelligence-engine-incrementally.md)
- [SI-DECISION-009 — Separate Knowledge and Engine Repositories](../09-decision-log/si-decision-009-separate-knowledge-and-engine-repositories.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 27. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-24 | Primera arquitectura técnica mínima del Matrix Validator y del repositorio Smart Imports Intelligence Engine. |
| 0.1.1 | 2026-07-24 | Se reemplaza npm por pnpm 11 como package manager y se actualizan lockfile, comandos, setup local y CI. |
