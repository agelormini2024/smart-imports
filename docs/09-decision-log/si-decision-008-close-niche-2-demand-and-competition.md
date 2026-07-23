---
id: si-decision-008
title: Close Niche 2 Demand and Competition
description: Registra el cierre de la primera etapa de Demanda y Competencia del Nicho 2 y la decisión de no procesar formalmente bolsas para ropa usada.
version: 0.1.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-07-23
updated: 2026-07-23
tags:
  - decision-log
  - niche-002
  - demand
  - competition
  - scope
  - closure
related:
  - si-decision-003
  - si-decision-004
  - si-decision-007
  - si-research-002
  - si-research-004
  - si-roadmap-002
phase: business-intelligence
---

# SI-DECISION-008 — Cerrar Demanda y Competencia del Nicho 2

## 1. Contexto

El alcance inicial de **Viaje organizado y equipaje funcional** incluía seis subcategorías.

Durante la ejecución se incorporaron dos extensiones con señales suficientes para un análisis separado:

- Bolsas de compresión al vacío con bomba.
- Kits de envases recargables para viaje.

Se completaron Demanda y Competencia ML de siete subcategorías. La última subcategoría pendiente era:

```text
Bolsas para ropa usada o húmeda
```

Después de un screening manual de 20 minutos, la oferta relevante encontrada fue escasa y no aportó una señal capaz de modificar la evaluación general del nicho.

## 2. Decisión

Se decide:

1. Cerrar la primera etapa de **Demanda y Competencia ML** del Nicho 2.
2. No procesar formalmente `TANDA-VIAJE-006`.
3. No generar publicaciones, productos base, evidencias ni competencia artificiales para completar una lista predefinida.
4. Mantener las bolsas para ropa usada o húmeda como posible SKU complementario futuro, fuera de la evaluación actual.
5. Pasar a la consolidación del nicho y a la selección de subcategorías para Margen Potencial.

## 3. Justificación

- El método busca evidencia relevante, no llenar una matriz por obligación.
- Forzar una tanda con resultados poco pertinentes degradaría la calidad del análisis.
- Las siete subcategorías procesadas ya permiten evaluar demanda, competencia, comportamiento commodity y oportunidades de diferenciación.
- La subcategoría descartada no representa una hipótesis estratégica central.
- El tiempo adicional tendría un costo de oportunidad superior a su valor informativo esperado.
- La decisión es reversible si posteriormente aparece nueva evidencia.

## 4. Alternativas consideradas

### Alternativa A — Seguir buscando hasta completar una tanda

Descartada porque implicaría ampliar términos hacia productos domésticos o genéricos y reducir la precisión del nicho.

### Alternativa B — Registrar publicaciones débiles igualmente

Descartada porque confundiría ausencia de evidencia con evidencia de demanda.

### Alternativa C — Reemplazarla por una nueva subcategoría

Descartada en esta etapa para evitar expansión continua del alcance. Las extensiones sólo deben incorporarse cuando surgen señales concretas.

### Alternativa D — Cerrar sin procesamiento formal

Aprobada porque conserva disciplina metodológica y permite avanzar hacia evaluación y margen.

## 5. Consecuencias

### Positivas

- Se cierra el alcance sin sobredocumentar ni forzar datos.
- Se preserva la calidad de las evidencias.
- Se libera tiempo para consolidación, margen y automatización.
- Se crea un antecedente metodológico para cerrar tandas por insuficiencia de señal.

### Riesgos

- Podría omitirse una oportunidad muy pequeña o emergente.
- La falta de procesamiento impide asignar métricas específicas a la subcategoría.

### Mitigación

- Mantener la subcategoría en backlog.
- Reabrirla únicamente ante una nueva señal de mercado, proveedor o comportamiento del cliente.

## 6. Impacto

### Matriz

- Registrar `TIME-0022`.
- No crear filas de `Publicaciones ML`, `Productos Base`, `Evidencias` ni `Competencia ML` para `TANDA-VIAJE-006`.
- La evaluación consolidada debe aclarar que la subcategoría fue cerrada por señal insuficiente.

### Documentación

- Crear `SI-RESEARCH-004`.
- Actualizar `SI-ROADMAP-002`.
- Actualizar README e índice del Decision Log.

### Roadmap

La próxima acción pasa de recolección a:

```text
Consolidar Demanda y Competencia del Nicho 2
→ actualizar Evaluaciones y Nichos
→ seleccionar shortlist para Margen Potencial
→ iniciar Matrix Validator
```

## 7. Documentos relacionados

- [SI-RESEARCH-002 — Travel Organization Scope](../06-research/niche-002-travel-organization/si-research-002-travel-organization-scope.md)
- [SI-RESEARCH-004 — Niche 2 Demand and Competition Closure](../06-research/niche-002-travel-organization/si-research-004-demand-competition-closure.md)
- [SI-ROADMAP-002 — Project Status and Handoff](../08-roadmaps/si-roadmap-002-project-status-and-handoff.md)

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-07-23 | Decisión aprobada de cierre de Demanda y Competencia del Nicho 2. |
