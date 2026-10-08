---
id: si-research-070
title: BRAND-CAND-010 — Method v2 Agile — Fase 0 — Research Brief
description: Research Brief prospectivo para movimiento integrado a la jornada sedentaria dentro de Marca Fitness.
version: 0.1.0
status: closed
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-10-05
updated: 2026-10-08
brand: brand-fitness
brand_candidate: brand-cand-010
method: method-v2-agile
phase: F0
---

# SI-RESEARCH-070 — BRAND-CAND-010 — Fase 0 — Research Brief

## 1. Estado

```text
ANALYSIS COMPLETE
DELTA DEFINED
MATRIX MATERIALIZED — aut105
MATRIX VALIDATOR PASS
F0 CLOSED
```

`BRAND-CAND-010` es el primer candidato de Marca Fitness seleccionado para abrir Method v2.

La apertura no modifica la prioridad comercial inmediata de Marca Hogar.

## 2. Input de negocio

```text
Candidate ID: BRAND-CAND-010
Source Hypothesis ID: FIT-CAND-007
Brand: brand-fitness
Candidate: Movimiento integrado a la jornada sedentaria
Decision: PASS TO METHOD V2
Primary Mission: Incorporar movimiento y entrenamiento en la vida cotidiana
Territory Relationship: CORE
Screening Type: PROSPECTIVE
```

Fuente oficial:

```text
docs/07-brand/brands/brand-fitness/candidates/brand-cand-010-integrated-movement-sedentary-day.md
```

La unidad de entrada de Method v2 es el Brand Candidate / Solution.

No existe todavía una Product Base Fitness asociada.

## 3. Pregunta central

> ¿Qué arquitecturas concretas permiten incorporar movimiento frecuente, breve y de baja fricción durante una jornada predominantemente sedentaria, y alrededor de cuáles puede existir un negocio defendible dentro de Marca Fitness?

La investigación debe partir del problema y de arquitecturas de solución.

No debe comenzar desde un SKU, una marca, una publicación, un proveedor ni una tecnología determinada.

## 4. Hipótesis iniciales

### H1 — pluralidad de arquitecturas

Existen múltiples arquitecturas capaces de introducir movimiento durante una jornada sedentaria.

Fase 1 deberá identificarlas y separarlas por mecanismo y experiencia de uso, sin convertir variaciones cosméticas en arquitecturas distintas.

### H2 — movimiento distribuido ≠ entrenamiento formal

```text
MICROACTIVIDAD / MOVIMIENTO DISTRIBUIDO
≠
SESIÓN FORMAL DE ENTRENAMIENTO
```

`BRAND-CAND-010` no exige que el usuario interrumpa su jornada para realizar una rutina fitness completa.

### H3 — baja fricción como dimensión estructural

La utilidad comercial puede depender materialmente de:

- inicio rápido;
- poco espacio;
- poco ruido;
- mínimo montaje;
- fácil guardado;
- compatibilidad con ropa cotidiana;
- sesiones breves;
- repetibilidad durante el día;
- baja fricción mental.

Regla:

```text
LA SOLUCIÓN DEBE SER MÁS FÁCIL DE USAR QUE DE POSTERGAR
```

### H4 — proximidad al escritorio ≠ solución

```text
ESTAR CERCA DEL ESCRITORIO
≠
RESOLVER LA INACTIVIDAD
```

Un objeto de oficina no obtiene Brand Fit sólo por encontrarse en un contexto sedentario.

### H5 — función física central

La solución debe producir o facilitar movimiento físico real.

```text
ERGONOMÍA
MOBILIARIO
PRODUCTIVIDAD
```

por sí solos no son suficientes para ingresar al scope.

### H6 — tecnología como capacidad de soporte

Sensores, recordatorios, apps, gamificación o medición pueden aportar valor.

No constituyen por sí mismos la propuesta de valor.

```text
TECNOLOGÍA
≠
BRAND FIT AUTOMÁTICO
```

### H7 — disciplina de claims

No se presuponen resultados de:

- salud;
- dolor;
- circulación;
- metabolismo;
- pérdida de peso;
- prevención de enfermedad;
- corrección postural;
- tratamiento de efectos del sedentarismo.

Todo claim deberá corresponder a evidencia del mismo nivel.

## 5. Frontera con BRAND-CAND-008

La frontera se congela desde F0 para impedir duplicación posterior de Product Bases.

```text
BRAND-CAND-008
→ existe intención de entrenar
→ sesión / rutina
→ entrenamiento flexible

BRAND-CAND-010
→ la jornada genera inactividad
→ oportunidades breves de movimiento
→ actividad distribuida durante el día
```

Si una futura solución puede aparecer superficialmente en ambos candidatos, deberá declararse el problema primario antes de normalizar Product Bases.

## 6. Scope inicial de Fase 1

Fase 1 deberá buscar familias de solución capaces de responder:

```text
¿CÓMO SE INTRODUCE MOVIMIENTO REAL
DENTRO DE UNA JORNADA
SIN EXIGIR UNA SESIÓN FORMAL DE ENTRENAMIENTO?
```

Debe excluir inicialmente:

- productos puramente ergonómicos;
- mobiliario sin función de movimiento central;
- gadgets de productividad;
- recordatorios sin componente físico;
- productos cuyo uso real requiera una sesión fitness convencional;
- claims médicos o terapéuticos como criterio de entrada.

## 7. Lo que F0 no define

F0 no define:

```text
PRODUCT BASES
PUBLICACIONES
MARCAS
PROVEEDORES
ALIBABA
SHORTLIST
FOB
LANDED COST
MARGEN
ROI
```

Tampoco declara como oportunidad ninguna arquitectura o producto particular.

Ejemplos como pedaleras, walking pads, plataformas, tablas u otras soluciones sólo podrán ingresar si emergen y sobreviven la normalización de Fase 1.

## 8. Contrato de materialización futura

La matriz vigente utiliza `Nichos` como adapter legacy para representar Brand Candidates.

Scope reservado:

```text
Nicho ID target: 37
Nicho: Marca Fitness — movimiento integrado a la jornada sedentaria
Role: MATRIX_SCOPE_ALIAS
Brand Candidate: BRAND-CAND-010
```

Regla:

```text
MATRIX_SCOPE_ALIAS
≠
REDEFINIR BRAND-CAND-010 COMO NICHO
```

F0 no necesita todavía:

```text
NEW PRODUCT BASE
NEW PUBLICACION ML
NEW COMPETENCIA ML
NEW COTIZACION
NEW MARGEN SCENARIO
NEW EVALUACION SCORE
```

El delta esperado es principalmente la incorporación del scope operativo y su trazabilidad documental.

## 9. Dependencia de lineage de matriz

La secuencia global ya reserva para `BRAND-CAND-006`:

```text
aut96  → F5
aut97  → F6
aut98  → F7
aut99  → F8
aut100 → F9
aut101 → F10
aut102 → F11
aut103 → F12
aut104 → F13
```

Por lo tanto:

```text
TARGET FITNESS F0
→ aut105
```

pero:

```text
NO MATERIALIZAR aut105 DESDE aut95
```

El lineage anterior quedó reconciliado hasta `aut104`; `aut105` puede materializarse como siguiente snapshot global cuando se ejecute el cierre de F0 de `BRAND-CAND-010`.

Esto evita dos ramas incompatibles de la matriz.

## 10. Gate F0

Pregunta:

> ¿El Research Brief define con suficiente precisión el problema, las fronteras del candidato y las reglas de investigación para abrir Fase 1 sin preseleccionar productos?

Resultado conceptual:

```text
PASS TO MATRIX MATERIALIZATION
```

Estado formal:

```text
F0 ANALYSIS COMPLETE
F0 MATRIX MATERIALIZED — aut105
F0 MATRIX VALIDATOR PASS
F0 CLOSED
```

## 11. Próximo gate

Una vez que exista el snapshot global correspondiente y el Matrix Validator devuelva PASS limpio:

```text
F0 CLOSED
→ F1 — MARKET / SOLUTION MAP
```

Hasta entonces puede prepararse investigación conceptual, pero no debe declararse F0 cerrada ni materializar Product Bases.

## 12. Decisión operativa

```text
BRAND-CAND-010
→ FIRST FITNESS CANDIDATE OPENED IN METHOD V2

BRAND-CAND-007
BRAND-CAND-008
BRAND-CAND-009
→ ELIGIBLE — NOT OPENED
```

La apertura de `BRAND-CAND-010` no implica prioridad comercial sobre Marca Hogar ni recomendación de importación.


<!-- BRAND-CAND-010-F0-CLOSURE:START -->
## Documentary reconciliation — 2026-10-08

```text
F0 CLOSED — aut105 PASS
SHA-256: a36a6ed5cdce69b526107883fd7a236ba1cbfcf2c7a4f171aac29694da5783d7
Next completed phase: F1 — Market / Solution Map
```
<!-- BRAND-CAND-010-F0-CLOSURE:END -->
