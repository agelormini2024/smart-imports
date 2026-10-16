---
id: si-research-105
title: BRAND-CAND-008 — Method v2 Agile — Fase 2 — Maturity
description: Evaluación de madurez de arquitecturas de entrenamiento flexible y portátil, separada de la madurez de productos/SKU.
version: 0.2.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-16
updated: 2026-10-16
brand: brand-fitness
brand_candidate: brand-cand-008
method: method-v2-agile
phase: F2
mode: AUTO
---

# SI-RESEARCH-105 — BRAND-CAND-008 — F2: Maturity

## 1. Estado y contrato

```text
SCREENING: CLOSED — PASS TO METHOD V2
F0: CLOSED / aut139 DOUBLE PASS
F1: CLOSED / aut140 DOUBLE PASS
F1 SHA-256: e757eea904bb4f117d2be20d83903b3adb646ed66c1d85575205d55f2d5b39ab
F2: CLOSED — AUTO / aut141 DOUBLE PASS
MATRIX SCOPE ALIAS: Nicho ID 39
F2 INPUT: aut140 (VALIDATED)
F2 OUTPUT: aut141 (VALIDATED / DOUBLE PASS)
F2 SHA-256: d0332a267fac3b7c0ae48e776f10d965100864a0c0dc563d839fdeab9cb6deca
PRODUCT BASES: NOT DEFINED
F3: CLOSED — COLLABORATIVE / aut142-r1 DOUBLE PASS (posterior a F2)
F14: NOT OPENED
```

**Contrato vigente:** `SI-BIM-PROC-003 v1.0.6`, fase F2: *arquitecturas → Maturity; no demanda / competencia / origen*. Se analiza la **madurez del principio funcional**, no la de fabricantes, productos, materiales específicos ni proveedores. Tampoco se puntúa demanda, competencia, marca o viabilidad económica en esta fase.

## 2. Pregunta y criterio de análisis

> ¿Qué tan establecidos están los mecanismos de entrenamiento identificados en F1, y qué restricciones de su implementación pueden anular la utilidad de la portabilidad entre contextos?

Se aplican cinco ejes de lectura cualitativa: (a) principio de entrenamiento, (b) dependencia del entorno, (c) facilidad real de preparación y traslado como **hipótesis por comprobar**, (d) posibilidad de adaptar intensidad/progresión, y (e) controles de seguridad pendientes.

**No son cinco mercados independientes.** Los códigos `SOL-008-A1..A5` son arquitecturas conceptuales y no Product Bases, SKUs, variantes ni publicaciones comerciales.

## 3. Evidencia y límites de inferencia

### Fuentes públicas de referencia — nivel de mecanismo

1. **ACSM (17/03/2026), actualización de entrenamiento de resistencia.** Respalda el uso de modalidades como peso corporal, bandas y entrenamiento domiciliario en programas de resistencia. No verifica sistemas comerciales determinados, portabilidad efectiva ni demanda local. https://acsm.org/resistance-training-guidelines-update-2026/ — citado previamente en F1.
2. **ACE (julio de 2025), entrenamiento con bandas.** Describe configuraciones de bandas y anclajes y precauciones de inspección. No acredita la calidad de una banda, mosquetón o anclaje particular. https://www.acefitness.org/continuing-education/certified/july-2025/8897/the-ace-workout-builder-for-resistance-band-workouts/ — citado previamente en F1.
3. **NSCA, Resistance Band Training.** Explica que la carga elástica depende de la elongación; no demuestra valores de resistencia, tolerancia al desgaste ni durabilidad de un producto ofrecido en el mercado. https://www.nsca.com/education/articles/kinetic-select/resistance-band-training/ — citado previamente en F1.

**Alcance de la evidencia:** sostiene la existencia/funcionalidad de ciertos principios físicos y formatos de entrenamiento. No se aportaron ensayos independientes de las cinco arquitecturas en variantes concretas, registros de fallas, datos de preparación cronometrada, comparables comerciales ni evidencia transaccional argentina.

## 4. Matriz de madurez interpretativa — sin scores comerciales

| Arquitectura | Madurez del principio | Dependencias y fragilidad de la promesa portátil | Confianza mecanismo / implementación | Condición crítica para continuar |
|---|---|---|---|---|
| `SOL-008-A1` — resistencia elástica portátil | **ESTABLECIDO**, para resistencia elástica como mecanismo | Tipo de anclaje, elongación y rango de ejercicios, desgaste del material, unión asa-banda. La variante *sin anclaje* requiere demostrar sesiones suficientemente completas. | **MEDIA / BAJA** | Diferenciar sistema útil entre contextos de simple set de bandas; especificar seguridad, resistencia y progresión sin duplicar `BASE-FIT-005/006` |
| `SOL-008-A2` — peso corporal con soportes ligeros | **ESTABLECIDO**, para ejercicios de peso corporal; **NO DEMOSTRADO** que agregar soportes cree valor diferencial | Superficie, espacio, fricción/adhesión, nivel de usuario, transporte y guardado de accesorios. | **MEDIA / BAJA** | Demostrar que el implemento habilita una mejora funcional y que existe un problema comercial distinto de entrenar sin equipamiento |
| `SOL-008-A3` — suspensión/anclaje portátil | **ESTABLECIDO** como mecanismo de ejercicio con peso corporal; **CONDICIONADO** como sistema replicable entre lugares | Punto de fijación admisible, resistencia de puerta/estructura, instalación y revisión de anclajes. Riesgo de caídas/roturas. | **MEDIA / BAJA** | **GATE DE SEGURIDAD CRÍTICO**; no promover ni atribuir seguridad a un sistema sin pruebas y condiciones de anclaje; prevenir duplicación de `BASE-FIT-008` |
| `SOL-008-A4` — resistencia modular compacta | **COMPONENTES/PRINCIPIOS CONOCIDOS**; madurez del conjunto **NO DEMOSTRADA** | Intercambio de piezas, uniones, bloqueos, esfuerzo de armado, mantenimiento y resistencia bajo carga. Múltiples configuraciones no equivalen a simplicidad. | **BAJA / BAJA** para el conjunto | Verificar arquitectura concreta, tiempos de montaje, componentes, durabilidad y utilidad real frente a alternativas simples |
| `SOL-008-A5` — entrenamiento portátil por intervalos | **ESTABLECIDO** el método general de ejercicio por intervalos; **NO DEMOSTRADO** un producto diferenciado | Altura libre, superficie, impacto, ruido y aceptación del contexto. Con implemento mínimo puede haber muy poco valor importable. | **MEDIA / BAJA** | Corroborar que puede usarse en más de un contexto relevante sin prometer universalidad ni confundir método de entrenamiento con oportunidad de producto |

**Escala usada:** `ESTABLECIDO` refiere al principio general de entrenamiento; `CONDICIONADO` o `NO DEMOSTRADO` se refiere al sistema/implementación. La confianza es una valoración de la **evidencia disponible**, no un score comercial. *La madurez mecánica no implica seguridad certificada*.

## 5. Lectura de riesgo y deduplicación

- `A1` y `A3`: mecanismo entrenable plausible, pero requieren controles de anclaje/fatiga, especialmente `A3`. La coexistencia con soluciones analizadas en `BRAND-CAND-007` **no** habilita crear Product Bases duplicadas en `008`.
- `A2` y `A5`: su posible debilidad no es el principio del ejercicio, sino demostrar una solución comercial diferenciada y usable en contextos cambiantes. No interpretar ausencia de implementos complejos como oportunidad de importación.
- `A4`: mayor riesgo de asignar madurez al conjunto por analogía con componentes conocidos. Queda estrictamente condicionada la confiabilidad de un diseño concreto.
- **Fronteras:** `007` = fuerza accesible/compacta; `008` = entrenamiento entre contextos; `009` = movilidad/estabilidad/recuperación; `010` = microactividad en jornada sedentaria. Cada eventual solución se asignará por su problema primario.

## 6. Interpretación y decisión de F2

**Resultado:** `READY FOR F3 EVIDENCE COLLECTION — CONDITIONED`; no es validación de demanda ni selección de arquitectura ganadora. Las cinco familias permanecen como **hipótesis de búsqueda** a contrastar, con diferentes gates. `A3` tiene un gate de seguridad especialmente restrictivo; `A4` presenta baja confianza sobre el sistema integral.

No se descartó una arquitectura sólo por falta de datos de SKU en F2: esa sería una inferencia indebida. Tampoco se declara oportunidad de importación, diferenciación de marca, rentabilidad, proveedor ni Product Base. 

## 7. Preparación de F3 — COLLABORATIVE, sin ejecutarla aquí

En F3 será necesaria una **cohorte de Mercado Libre argentina**, verificable por publicación exacta, que permita distinguir problemas/formatos y contrastar al menos las arquitecturas comercialmente representadas. Priorizar variedad de mecanismo y evitar reutilizar ventas de `BRAND-CAND-007` como si probaran demanda de `008`.

Los campos mínimos serán los del contrato: URL precisa, fecha, producto/modelo, clasificación, `Precio ARS`, `Precio USD`, ventas visibles literales o `No informadas`, `FX ARS/USD`, fecha y fuente/basis del FX, y ledger `Verificaciones ML`. La selección y lectura de la cohorte, así como la aprobación del cierre F3, requieren participación del Founder. **No se capturaron publicaciones ni se asignaron scores en F2.**

## 8. Materialización / gate técnico

- Baseline **aut140**, validada por `Data Fidelity Preflight v2.4` y `Matrix Validator 0.1.0 / full-matrix-v5 0.7.0`, ambos PASS sin errores/warnings/findings/limitations.
- Nuevo snapshot materializado: `matrix-aut141-brand-cand-008-phase2-maturity.xlsx`, SHA-256 `d0332a267fac3b7c0ae48e776f10d965100864a0c0dc563d839fdeab9cb6deca` (sólo metadatos del alias `Nichos ID 39`; ningún score ni registro de mercado).
- La matriz anterior permanece inmutable. **Comparación estructural aut140 → aut141: 29 hojas y 1.942 fórmulas preservadas, exactamente 3 celdas con cambios (`Nichos!AD40:AF40`), sin alteraciones de celdas históricas.** Este control no sustituye la validación canónica.
- **F2 CLOSED** tras confirmar el doble PASS del snapshot `aut141`, consistencia del Research y SHA-256.
- La ejecución posterior de F3 fue **COLLABORATIVE**, con puntuación aprobada por el Founder y doble PASS en `aut142-r1`; se documenta en `SI-RESEARCH-106`.

## 9. Estado documental

`SI-RESEARCH-105` es la numeración de trabajo, que debe verificarse libre antes de su publicación. Preparado para integrar en `docs/06-research/brand-fitness/` en checkpoint F0–F3. Los XLSX, logs, archivos de evidencia y scripts permanecen privados y **fuera de Git**.

## 10. Adenda de cierre canónico (2026-10-16)

El log privado `validation-aut141-brand-cand-008-f2.log` confirmó **Data Fidelity Preflight v2.4 PASS** y **Matrix Validator 0.1.0 / full-matrix-v5 0.7.0 PASS**, con `errors=0`, `warnings=0`, `info=0`, `findings=[]` y `limitations=[]`.

La matriz validada es `matrix-aut141-brand-cand-008-phase2-maturity.xlsx`, SHA-256 `d0332a267fac3b7c0ae48e776f10d965100864a0c0dc563d839fdeab9cb6deca`. **F2 CLOSED — AUTO.** La nota de preparación anterior pertenece al momento previo al doble PASS; el cierre formal queda asentado en esta adenda.

La fase F3 fue ejecutada posteriormente de forma colaborativa y queda documentada por separado en `SI-RESEARCH-106`, sin reescribir el análisis de madurez aquí.
