---
id: si-decision-009
title: Separate Knowledge and Intelligence Engine Repositories
description: Registra la separación entre el repositorio documental público de Smart Imports y el repositorio privado que alojará el Smart Imports Intelligence Engine.
version: 0.1.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-24
updated: 2026-07-24
tags:
  - decision-log
  - architecture
  - repositories
  - intelligence-engine
  - security
  - matrix-validator
related:
  - si-decision-006
  - si-func-001
  - si-tech-001
  - si-agent-001
  - si-roadmap-002
phase: foundation
---

# SI-DECISION-009 — Separar el repositorio documental del Intelligence Engine

## 1. Contexto

Smart Imports comenzó como una base de conocimiento, una metodología de inteligencia comercial y una matriz operativa. El repositorio:

```text
agelormini2024/smart-imports
```

se utiliza como fuente documental de verdad y contiene visión, manuales, criterios, procedimientos, investigaciones sanitizadas, roadmaps y decisiones.

El proyecto inicia ahora la construcción de software ejecutable bajo el nombre:

```text
Smart Imports Intelligence Engine
```

Su primer módulo será el `Matrix Validator`, pero la visión incluye futuros módulos para proveedores, RFQ, margen, scoring, automatización y asistencia para decisiones.

El software tendrá un ciclo de vida distinto del conocimiento documental:

- Dependencias y releases.
- Código fuente y tests.
- Configuración de CI.
- Schemas ejecutables.
- Fixtures.
- Posible procesamiento de información comercial sensible.
- Evolución futura hacia CLI, API, workers o una plataforma interna.

Era necesario definir dónde vivirá y evolucionará el Engine antes de crear la especificación técnica.

## 2. Decisión

Se decide mantener dos repositorios con responsabilidades distintas.

### 2.1 Repositorio documental

```text
Repository: agelormini2024/smart-imports
Visibility: Public
```

Responsabilidad:

- Visión.
- Business Manual.
- Business Intelligence Manual.
- Functional Specifications.
- Technical Specifications de alto nivel.
- AI Agents.
- Investigación publicable y sanitizada.
- Roadmaps.
- Decision Log.
- Gobierno del proyecto.

Este repositorio continuará siendo la fuente documental de verdad.

### 2.2 Repositorio del software

```text
Repository: agelormini2024/smart-imports-engine
Visibility: Private
```

Responsabilidad:

- Código fuente.
- Tests.
- Schemas ejecutables.
- CLI.
- Adaptadores XLSX.
- Reportes estructurados.
- Configuración de desarrollo y CI.
- Releases.
- Documentación interna de implementación.
- Futuros módulos del Intelligence Engine.

El repositorio se crea para todo el Intelligence Engine, no únicamente para el Matrix Validator.

### 2.3 Primer modo de ejecución

El MVP 0.1 será una CLI local.

```text
Hosting: none
Database: none
Web interface: none
Persistent service: none
```

Se ejecutará inicialmente en equipos de desarrollo y leerá archivos XLSX desde el filesystem local.

### 2.4 Política de datos

Los datos operativos reales no deben formar parte del historial Git del Engine.

Fuera de Git:

- Matrices vigentes.
- Cotizaciones.
- PDFs de proveedores.
- Datos de contacto.
- Estrategias de negociación.
- Reportes privados.
- Credenciales.
- Archivos de prueba no sanitizados.

Dentro de Git:

- Fixtures sintéticos.
- Fixtures mínimos sanitizados.
- Schemas.
- Tests.
- Ejemplos sin información comercial sensible.

### 2.5 Evolución de módulos

Los módulos futuros evolucionarán dentro de `smart-imports-engine` mientras compartan el mismo dominio y ciclo de releases.

No se creará un repositorio independiente para cada MVP.

La separación en múltiples repositorios sólo se reconsiderará cuando exista una razón técnica u organizacional concreta, por ejemplo:

- Equipos independientes.
- Requisitos de seguridad incompatibles.
- Releases completamente desacoplados.
- Paquetes reutilizables por terceros.
- Escalado operativo que justifique servicios separados.

## 3. Justificación

### 3.1 Separación de responsabilidades

El repositorio público comunica cómo piensa y decide Smart Imports. El repositorio privado ejecuta esas decisiones mediante software.

Mezclar ambos generaría:

- Riesgo de publicar datos operativos.
- Historial Git pesado por archivos binarios.
- Issues técnicos mezclados con decisiones comerciales.
- Releases de software dentro de una base documental.
- Dificultad para controlar accesos.

### 3.2 Seguridad y confidencialidad

El Engine eventualmente procesará información que no debe publicarse:

- Costos.
- FOB.
- MOQ.
- Proveedores.
- Documentación técnica.
- Conversaciones.
- Estrategias de negociación.

Un repositorio privado no reemplaza las buenas prácticas, pero agrega una barrera de protección y permite accesos diferenciados.

### 3.3 Evolución coherente

Matrix Validator, Supplier Response Analyzer, RFQ Generator y Margin Engine compartirán:

- Modelos.
- Schemas.
- Findings.
- Infraestructura.
- Testing.
- Integraciones.
- Convenciones.

Mantenerlos inicialmente en un solo repositorio reduce duplicación y fragmentación prematura.

### 3.4 Evitar infraestructura prematura

El Matrix Validator no necesita disponibilidad permanente. Alojarlo como servicio antes de validar el núcleo agregaría:

- Despliegue.
- Autenticación.
- Gestión de secretos.
- Monitoreo.
- Costos.
- Superficie de ataque.

La CLI local permite probar el valor funcional con menor costo y riesgo.

## 4. Alternativas consideradas

### Alternativa A — Mantener documentación y código en `smart-imports`

Descartada.

Ventaja:

- Un único repositorio.

Problemas:

- Mezcla ciclos de vida.
- Complica la visibilidad pública.
- Aumenta el riesgo de exponer datos o fixtures.
- Une releases técnicos con cambios metodológicos.

### Alternativa B — Crear un repositorio por cada módulo

Descartada para la etapa actual.

Ejemplo:

```text
smart-imports-matrix-validator
smart-imports-supplier-analyzer
smart-imports-margin-engine
```

Problemas:

- Configuración y dependencias duplicadas.
- Schemas replicados.
- Versiones difíciles de coordinar.
- Sobrecosto operativo antes de tener más de un producto ejecutable.

### Alternativa C — Crear un monorepo complejo desde el inicio

Descartada por ahora.

No existen todavía múltiples aplicaciones o paquetes que justifiquen:

```text
apps/
packages/
```

El repositorio puede migrar a workspaces cuando aparezca un segundo ejecutable real.

### Alternativa D — Construir directamente una aplicación web alojada

Descartada para el MVP 0.1.

Agrega infraestructura y experiencia de usuario antes de demostrar que las reglas de validación son correctas.

### Alternativa E — Repositorio privado único para todo Smart Imports

Descartada.

Reduciría la capacidad de compartir públicamente la metodología y la documentación sanitizada.

## 5. Consecuencias

### Positivas

- Frontera clara entre conocimiento y ejecución.
- Menor riesgo de exposición accidental.
- Releases y CI independientes.
- Evolución modular sin fragmentar cada MVP.
- El repositorio documental continúa siendo compartible.
- La CLI puede validarse sin hosting.
- Los datos operativos permanecen fuera de Git.

### Riesgos

- Dos repositorios deben mantenerse sincronizados.
- Puede haber documentación duplicada.
- Los enlaces cruzados pueden quedar desactualizados.
- Un repositorio privado no impide por sí mismo subir secretos.
- Una futura migración a monorepo requerirá trabajo.

### Mitigaciones

- `SI-ROADMAP-002` mantiene el estado transversal.
- Las decisiones y especificaciones de alto nivel viven únicamente en `smart-imports`.
- La documentación interna del código vive en `smart-imports-engine`.
- `.gitignore` bloquea datos y formatos sensibles por defecto.
- Los fixtures públicos deben ser sintéticos o sanitizados.
- Cada release del Engine referencia las especificaciones que implementa.
- No copiar matrices reales al repositorio para simplificar tests.

## 6. Impacto

### Repositorios

Crear:

```text
agelormini2024/smart-imports-engine
```

con visibilidad privada.

Mantener:

```text
agelormini2024/smart-imports
```

con visibilidad pública.

### Documentación

En `smart-imports`:

```text
docs/03-functional-specifications/si-func-001-matrix-validator.md
docs/04-technical-specifications/si-tech-001-matrix-validator-architecture.md
docs/09-decision-log/si-decision-009-separate-knowledge-and-engine-repositories.md
```

En `smart-imports-engine`:

```text
README.md
docs/adr/
docs/development/
docs/testing/
CHANGELOG.md
```

### Roadmap

La siguiente secuencia queda aprobada:

```text
Aprobar SI-FUNC-001
→ registrar separación de repositorios
→ aprobar arquitectura técnica mínima
→ crear smart-imports-engine privado
→ ejecutar spike XLSX
→ implementar Matrix Validator
→ volver al screening de Margen
```

### Hosting

No se contrata ni configura hosting para MVP 0.1.

El alojamiento se reconsiderará cuando exista una necesidad concreta de:

- Ejecución remota.
- Integración con n8n.
- API interna.
- Procesamiento programado.
- Interfaz web.
- Usuarios múltiples.

## 7. Criterios para revisar esta decisión

La decisión deberá revisarse si ocurre alguno de estos eventos:

- El Engine incorpora una API o frontend independiente.
- Aparece un segundo equipo de desarrollo.
- Un módulo necesita requisitos de seguridad diferentes.
- Se decide publicar parte del Engine como open source.
- La integración con n8n requiere un servicio persistente.
- El repositorio único del Engine genera acoplamiento operativo real.

## 8. Documentos relacionados

- [SI-DECISION-006 — Build the Intelligence Engine Incrementally](./si-decision-006-build-intelligence-engine-incrementally.md)
- [SI-FUNC-001 — Matrix Validator](../03-functional-specifications/si-func-001-matrix-validator.md)
- [SI-TECH-001 — Matrix Validator Architecture](../04-technical-specifications/si-tech-001-matrix-validator-architecture.md)
- [SI-AGENT-001 — Smart Imports Intelligence Engine](../05-ai-agents/si-agent-001-smart-imports-intelligence-engine.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 9. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-24 | Decisión aprobada de separar el repositorio documental público del repositorio privado del Intelligence Engine. |
