---
id: si-research-055
title: BRAND-CAND-005 — Method v2 Agile — Fase 13 — Shortlist final
description: Cierre de shortlist y estado Portfolio Review Ready de BRAND-CAND-005.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-30
updated: 2026-09-30
brand: brand-hogar
brand_candidate: brand-cand-005
method: method-v2-agile
phase: F13
---

# SI-RESEARCH-055 — BRAND-CAND-005 — Method v2 Agile — Fase 13: Shortlist final

## 1. Objetivo

Cerrar la shortlist de `BRAND-CAND-005 — Compostaje / procesamiento doméstico de residuos orgánicos` integrando los resultados decision-grade acumulados en F0–F12.

F13 **no recalcula costos**, **no reabre sourcing** y **no selecciona proveedor**. La evaluación final es cualitativa estructurada y combina:

```text
economía
+ calidad de evidencia
+ demanda / mercado
+ diferenciación + Brand Fit
+ complejidad operativa
+ riesgo técnico / regulatorio
+ adecuación a primera etapa
```

Reglas de lectura:

```text
FINALIST ≠ ganador
FINALIST ≠ producto seleccionado
FINALIST ≠ PASS TO F14
ECONOMIC FIT ≠ GOOD FIRST PRODUCT
PORTFOLIO REVIEW READY ≠ PRODUCT READY
STOP — REOPENABLE ≠ arquitectura inválida
```

---

## 2. Input validado

F13 parte de:

```text
matrix-aut89-brand-cand-005-phase12.xlsx
```

F12 quedó validada localmente con:

```text
Matrix Validator: 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
Errors: 0
Warnings: 0
Info: 0
Limitations: []
SHA-256: d089ca491a1413be64362bb02da7aef8ac924b6caab75a5b48eea0340d994b78
```

Resultado de F12:

```text
BASE-HOGAR-024
→ STOP — REOPENABLE

BASE-HOGAR-025
→ STOP — REOPENABLE / LOGISTICS GATE

BASE-HOGAR-028
→ PASS TO F13 — CONDITIONED
```

Por lo tanto, F13 evalúa activamente sólo:

```text
BASE-HOGAR-028
```

---

## 3. Lectura integrada del candidato

### 3.1 Mercado y demanda

La demanda global de `BRAND-CAND-005` fue evaluada en F3 como moderada y heterogénea (`3/5`, confianza Media).

Las arquitecturas pasivas y biológicas tradicionales mostraron mejores señales transaccionales locales que los procesadores eléctricos. Para `BASE-HOGAR-028`, la oferta local es visible y de ticket alto, pero la evidencia disponible **no demuestra una señal transaccional fuerte** comparable con las composteras tradicionales.

Por eso:

```text
PRECIO ALTO ≠ DEMANDA VALIDADA
OFERTA VISIBLE ≠ TRACCIÓN TRANSACCIONAL
```

La economía favorable de F11/F12 no corrige esta limitación de evidencia de mercado.

### 3.2 Competencia

La competencia del candidato fue evaluada como moderada y heterogénea (`3/5`, confianza Media).

`BASE-HOGAR-028` se diferencia de las composteras pasivas por el job de conveniencia:

```text
reducir volumen
+ procesar residuos en cocina
+ disminuir manipulación
+ acelerar el preprocesamiento
```

Esa diferenciación comercial existe, pero también eleva la expectativa del usuario y el riesgo de claims incorrectos.

### 3.3 Brand Fit

El potencial de marca de `BRAND-CAND-005` fue evaluado como alto (`4/5`, confianza Media).

La tesis permanece:

```text
NO: vender "composteras"

SÍ: hacer simple y confiable la gestión de residuos orgánicos del hogar
    → elegir el método correcto
    → reducir olor / suciedad / esfuerzo
    → explicar el proceso real
    → acompañar al usuario
    → definir correctamente el output
```

`BASE-HOGAR-028` encaja en este territorio como una solución de conveniencia premium, siempre que la marca mantenga disciplina semántica sobre mecanismo y output.

---

## 4. BASE-HOGAR-028 — evaluación F13

### 4.1 Economía

F13 utiliza sólo el escenario comercialmente ejecutable al MOQ público conservador:

| Escenario | Ejecutable | Margen % | ROI sobre costo |
|---|---|---:|---:|
| 100 u — `MARG-0037` | SÍ | ~31,21% | ~50,23% |

La sensibilidad de 50 unidades (`MARG-0036`) continúa siendo:

```text
NON-EXECUTABLE SENSITIVITY
```

Por lo tanto no se usa como prueba comercial en F13.

Lectura económica:

```text
ECONOMY OBJECTIVE MET
```

La economía deja de ser el gate principal.

### 4.2 Fortaleza principal

```text
economía suficiente en 100 u
+ propuesta premium diferenciada
+ job de conveniencia claro
+ Brand Fit dentro de gestión de residuos orgánicos
```

El PB puede aportar al portfolio una arquitectura claramente distinta de las composteras tradicionales.

### 4.3 Condición dominante

La condición dominante es de **execution risk**, no de margen:

- señal transaccional local débil/no visible;
- electrodoméstico con mayor carga de postventa;
- compatibilidad exacta `220–240V / 50Hz` y plug/configuración local;
- filtros de carbón: SKU, disponibilidad, vida útil y costo de reemplazo;
- repuestos generales;
- warranty / service plan;
- documentación y certificaciones declaradas;
- seguridad térmica y eléctrica;
- consumo, ruido, limpieza y comportamiento real del ciclo;
- accepted inputs;
- claims sobre reducción de volumen, olor, higienización y naturaleza del output.

Además:

```text
REDUCCIÓN DE VOLUMEN ≠ COMPOSTAJE
DESHIDRATACIÓN / TRITURACIÓN ≠ COMPOST TERMINADO
PROCESAMIENTO RÁPIDO ≠ ESTABILIZACIÓN BIOLÓGICA
RESIDUO CON ASPECTO DE TIERRA ≠ ENMIENDA VALIDADA
```

### 4.4 Adecuación a primera etapa

El PB **no se convierte en first-stage fit por tener margen suficiente**.

Su complejidad de servicio, electricidad y claims continúa siendo material.

Clasificación explícita:

```text
NOT FIRST-STAGE FIT
```

Esto no elimina el PB de la comparación transversal: permite conservarlo como opción de portfolio sin confundirlo con el candidato natural para la primera importación.

---

## 5. Decisión F13

### BASE-HOGAR-028

```text
FINALIST — CONDITIONED
ELIGIBLE FOR PORTFOLIO REVIEW
NOT FIRST-STAGE FIT
```

La condición no es cosmética: debe permanecer visible en Portfolio Review.

### BASE-HOGAR-024

```text
STOP — REOPENABLE
```

Permanece fuera de F13 por economía fuertemente negativa bajo el screen vigente. Sólo se reabre ante un cambio estructural demostrado en logística, packing/nesting, costo de origen o precio defendible.

### BASE-HOGAR-025

```text
STOP — REOPENABLE / LOGISTICS GATE
```

El escenario ejecutable de 439 unidades fue negativo bajo aéreo. Sólo se reabre con:

```text
packing real
+ modelo marítimo/LCL
+ costos consistentes
→ nuevo escenario decision-grade
```

---

## 6. Resultado consolidado de BRAND-CAND-005

Resultado materializado de F13:

```text
BASE-HOGAR-024
→ STOP — REOPENABLE

BASE-HOGAR-025
→ STOP — REOPENABLE / LOGISTICS GATE

BASE-HOGAR-028
→ FINALIST — CONDITIONED
→ ELIGIBLE FOR PORTFOLIO REVIEW
→ NOT FIRST-STAGE FIT
```

Por lo tanto, después del PASS del Matrix Validator y del checkpoint documental:

```text
BRAND-CAND-005
→ F0–F13 CLOSED
→ PORTFOLIO REVIEW READY
→ FREEZE
```

F13 **no abre F14**.

---

## 7. Datos requeridos para revisión externa / Portfolio Review

Para `BASE-HOGAR-028`, conservar como checklist:

```text
clasificación aduanera probable / NCM
intervenciones y requisitos de importación
seguridad / certificación eléctrica aplicable
220–240V / 50Hz exacto
plug / configuración Argentina
verificación documental CE / FCC / CB / RoHS / KC declarados
filter SKU / availability / replacement cost
repuestos generales
warranty / service plan
consumo / ruido / temperatura / limpieza
accepted inputs
claims de reducción de volumen
claims de olor
claims de higienización
naturaleza real del output
rotulado e instrucciones
red flags para primera importación
```

Regla operativa:

```text
DECISION-GRADE ≠ PROCUREMENT-GRADE
```

No corresponde invertir todavía en procurement-grade antes de comparar el portfolio y aplicar el gate externo.

---

## 8. Evidencia y trazabilidad materializada

Nuevos IDs:

```text
RES-MARG-0021
SRC-0477
EVID-0282
EVSRC-0624
```

No se crea `EVAL-0026`, porque F13 no introduce un nuevo criterio formal del modelo legacy; integra criterios ya evaluados.

Matriz:

```text
matrix-aut90-brand-cand-005-phase13.xlsx
SHA-256: 2bb0e30d75f98d9d90b60942b0b84ea409544e0966b5d5a4fd88e51fc65fbe9e
```

`Resumen Margen Vista!A22:T22` fue materializada como **derived view mediante fórmulas**, no con valores pegados.

---

## 9. Próximo checkpoint

Estado al materializar `aut90`:

```text
F12
→ CLOSED — aut89 PASS

F13
→ CONCEPTUAL ANALYSIS COMPLETE
→ MATRIX MATERIALIZATION COMPLETE — aut90
→ MATRIX VALIDATOR PASS — 0 errors / 0 warnings / 0 info / 0 limitations
→ CLOSED — aut90 PASS

F14
→ NOT OPENED
```

`aut90` obtuvo `PASS` limpio. F13 queda formalmente `CLOSED`. La secuencia de cierre del candidato es:

```text
ejecutar documentary checkpoint completo de BRAND-CAND-005
→ publicar SI-RESEARCH F0–F13
→ actualizar dossier del candidato
→ actualizar índices Research / Marca Hogar
→ actualizar README raíz
→ actualizar SI-ROADMAP-002
→ verificar documentación + git diff --check
→ git add / commit / push manual por Alejandro
→ recién entonces abrir BRAND-CAND-006 — residuos de mascotas
```

Hasta completar ese cierre:

```text
BRAND-CAND-006 = NOT OPENED
F14 = NOT OPENED
```
