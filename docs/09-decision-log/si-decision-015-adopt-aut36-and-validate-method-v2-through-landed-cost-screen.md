---
id: si-decision-015
title: Adoptar aut36 y validar Method v2 internamente hasta Landed Cost Screen
description: Adopta aut36 como snapshot comercial vigente y formaliza que Method v2 está validado internamente hasta Landed Cost Screen, dejando la revisión del despachante como gate profesional externo.
version: 1.0.0
status: approved
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-15
updated: 2026-09-15
tags:
  - decision
  - method-v2
  - matrix
  - landed-cost
  - customs
related:
  - si-decision-014
  - si-research-005
  - si-research-006
  - si-roadmap-002
audience:
  - founder
  - partner
  - assistant
phase: commercial-validation
---

# SI-DECISION-015 — Adoptar aut36 y validar Method v2 internamente hasta Landed Cost Screen

## Contexto

Method v2 fue aplicado al Nicho 3 desde el Research Brief hasta el primer `Landed Cost Screen`.

La ejecución permitió reducir ocho Productos Base, filtrar por origen y Headroom, reunir un dataset logístico mínimo y estimar costo puesto sólo para candidatos que justificaban esa profundización.

El resultado fue materializado en:

```text
matrix-aut36-niche3-method-v2-checkpoint-corrected.xlsx
```

y validado con Matrix Validator:

```text
full-matrix-v5 0.7.0
PASS
0 errors
0 warnings
0 info
0 limitations
```

SHA-256:

```text
219d9954acca9fefda5f6edef2eab18f93bf0b4564e45d3e1442f13d6db39a53
```

## Decisión

Se decide:

1. Adoptar `aut36` como **snapshot comercial operativo vigente**.
2. Mantener `aut32` como baseline técnica de Matrix Validator v0.1.0.
3. Considerar **Method v2 validado internamente hasta `Landed Cost Screen`**.
4. Tratar la revisión del despachante como **gate profesional externo**.
5. No intentar convertir el screening preliminar en una falsa liquidación aduanera definitiva.
6. Llevar al despachante sólo una shortlist reducida de aproximadamente 5–6 candidatos firmes.
7. Negociar precio y condiciones con proveedores finalistas antes de la validación profesional cuando resulte útil.
8. Mantener `full-matrix-v5 0.7.0` y Matrix Validator v0.1.0 cerrados mientras no aparezca un requerimiento comercial bloqueante.

## Razón

La metodología ya demostró capacidad para:

- reducir el universo inicial;
- separar arquitectura de publicación;
- distinguir origen exacto/comparable/benchmark;
- evitar profundización prematura;
- usar Headroom como filtro;
- exigir dataset mínimo antes de Landed Cost;
- separar costo económico de necesidad de caja;
- identificar candidatos que justifican validación profesional.

La precisión restante depende de información aduanera y regulatoria especializada. Intentar resolverla internamente para todos los candidatos produciría falsa precisión y costo innecesario.

## Consecuencias

### Positivas

- Se reduce tiempo de despachante sobre productos débiles.
- La investigación comercial mantiene velocidad sin inventar costos.
- La negociación se concentra en proveedores con mayor probabilidad de llegar a importación.
- El método tiene un cierre interno claro y reproducible.
- El Engine permanece estable y no se reabre por una necesidad externa.

### Riesgos aceptados

- El `Landed Cost Screen` puede diferir del costo definitivo.
- Una NCM profesional puede modificar derechos o intervenciones.
- Certificaciones o restricciones pueden descartar un candidato avanzado.
- Tarifas logísticas pueden cambiar antes de la importación real.

Estos riesgos son precisamente la razón del gate profesional externo.

## Próximo gate

```text
5–6 candidatos firmes
→ negociación final de origen
→ paquete homogéneo para despachante
→ validación profesional
→ recalcular
→ shortlist final
→ decisión de importación
```

## Información comercial sensible

Los precios exactos de proveedores, objetivos de negociación y escenarios detallados permanecen en la matriz y evidencia privada.

La documentación pública registra el método, estados y decisiones sin publicar información comercial sensible.
