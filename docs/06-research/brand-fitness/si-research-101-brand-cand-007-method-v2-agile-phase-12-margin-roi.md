---
id: si-research-101
title: BRAND-CAND-007 — Method v2 — F12 Margin + ROI
version: 0.1.0
status: closed
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
phase: F12
mode: AUTO
scope_value: Marca Fitness — fuerza accesible y compacta
baseline: aut136
baseline_sha256: 2e2a9728768b884c407b1abdc0ebbc4a9e0063f85a39f270a59b73fe34c619c6
matrix_target: aut137
matrix_sha256: bae4d15aca6f6599ae7895ae59b6284c5fb917014b08bed531fb1683eb2d82ca
created: 2026-10-14
---

# SI-RESEARCH-101 — BRAND-CAND-007 — F12 Margin + ROI

> **F12 CLOSED / AUTO / DOBLE PASS confirmado en `aut137`.** F12 **interpreta F11, no recalcula** costos landed ni fabrica un valor de margen o ROI. Resultado legítimo posible: **MARGIN / ROI NOT DETERMINABLE**.

## 1. Contrato, baseline y alcance

- `SI-RESEARCH-100` / F11, matriz `aut136`, Data Fidelity Preflight PASS y Matrix Validator PASS. Resultado: **AIR STRESS NO EJECUTABLE Y CONDICIONADO; NO LANDED CONFIRMADO**.
- `SI-RESEARCH-098` / F9: el techo económico landed procede del modelo histórico (ARS 1.535/USD del 13/10/2026, costo canal 25%, costo comercial 5%, margen objetivo 25% de venta neta), **no constituye cotización ni tipo de cambio actual**.
- F10 `SI-RESEARCH-099` contiene ofertas públicas `COT-0065..0069` con precio exacto por SKU y packing insuficientes para una inversión.
- Dos consultas exploratorias hechas por el Founder a proveedores de mancuernas aguardan respuesta. No se asigna una contestación inexistente.
- Product Bases 006/008 siguen DEFER desde F7, sin análisis económico de origen adicional.

## 2. Capa A — Hechos y resultados *ya calculados* en F9/F11 (sin recalcular)

| Concepto | `BASE-FIT-005` — bandas tubulares | `BASE-FIT-007` — mancuernas 20 kg |
|---|---|---|
| Comparables locales | `ML-0178`, PVP histórico ARS 39.999 | `ML-0181`, ARS 64.999; `ML-0180`, ARS 93.018 |
| Techo económico landed de F9 | USD **13,3547**/kit | USD **21,7016** (BS Fit) o USD **31,0565** (GMP)/kit |
| Origen de referencia | `COT-0065`, **USD 4,68/kit** publicado, tier 100–499 | `COT-0067..0069`, **sin precio atribuible** a kit completo 20 kg |
| Resto nominal antes de demás costos | USD **8,6747/kit** (NO margen) | No computable sin precio específico de origen |
| Sensibilidad aérea F11 | **SI** 1 kg facturable × USD 10/kg: solo producto + flete = USD **14,68**, **1,3253** más que el techo y faltan impuestos/cargos | **SI** >=20 kg facturables × USD 10/kg: >=USD **200** *solo flete*, sin que ese peso tarifable o ruta sean hechos comprobados |
| Costo landed / márgenes / ROI | **No calculados** | **No calculados** |

**Precisión de interpretación:** el saldo de USD 8,6747 es espacio disponible para **todos** los costos adicionales antes de alcanzar el techo objetivo, **no ganancia**. El exceso de USD 1,3253 existe sólo bajo la combinación de precio publicado, 1 kg facturable y proxy aéreo histórico. No demuestra economía marítima, ni implica que el costo faltante sea cero.

## 3. Capa C — Interpretación de viabilidad y riesgos

### `BASE-FIT-005`

- El **AIR STRESS es desfavorable bajo sus hipótesis**. Se agota el techo económico antes de completar seguro, derechos/tasas, despacho y logística.
- No hay landed cost aceptable verificado, por lo que **no corresponde asignar margen bruto, margen neto ni ROI numérico**.
- Una eventual alternativa marítima/LCL, consolidación mixta o menor masa facturable podrá evaluarse **con datos verificables** de packing, condiciones de compra y fricción de importación; F12 no concluye que esa ruta sea viable.
- Seguridad y material de bandas/anclajes permanecen condiciones de calidad no homologadas.

### `BASE-FIT-007`

- La **demanda observada para 20 kg** no valida automáticamente los kits de 10/15 kg.
- Sin **precio completo por variante** y packing verificable del mismo SKU no podemos determinar landed, ni margen, ni ROI; usar el extremo inferior de un rango de familias de producto sería un error metodológico.
- La sensibilidad aérea condicional es adversa; **no constituye presupuesto** y no descarta una ruta de carga marítima mixta.
- Se documenta incertidumbre sustantiva de material (hierro vs cemento), resistencia mecánica, MOQ personalizado, transporte y requisitos regulatorios.

### Clasificación por evidencia

| Base | Resultado económico F12 | Confidence | No inferir |
|---|---|---|---|
| `BASE-FIT-005` | `UNFAVORABLE UNDER AIR STRESS / ECONOMIC VIABILITY UNDETERMINED` | **Baja** para viabilidad de importación | margen o ROI real, STOP definitivo, logística marítima |
| `BASE-FIT-007` | `EXACT 20KG UNIT COST MISSING / MARGIN+ROI UNDETERMINED` | **Baja** para viabilidad de importación | precio 20kg desde mínimos de rango, ROI/margen, STOP definitivo |

La confianza aquí califica el **análisis económico de importación**, no modifica scores ni confianza F3/F4/F5 ya cerrados.

## 4. Capa D — Decisión técnica F12

- `BASE-FIT-005`: **HOLD — REOPENABLE / MARITIME + PACKING + REGULATORY + QUALITY GATE**. No PASS económico, no STOP definitivo.
- `BASE-FIT-007`: **HOLD — REOPENABLE / QUOTED 20KG CONFIGURATION + LOGISTICS GATE**. No PASS económico, no STOP definitivo.
- `BASE-FIT-006` y `BASE-FIT-008`: **DEFER**, sin modificaciones de F7/F8.
- **Ningún margen o ROI numérico defendible**: `NOT DETERMINABLE FROM CURRENT DATA`, no equivalente a cero.
- F13 deberá integrar la evidencia F3–F12 y emitir **Final Shortlist con condicionantes y Decision Report para socio+despachante**, sin abrir F14 ni autorizar una importación.

## 5. Materialización y gate confirmados

`aut136 → aut137`: doble PASS técnico confirmado. Solo cinco celdas narrativas: `Productos Base!N102/N104` y `Nichos!AD39:AF39`. Se conservaron las 29 hojas, 1.942 fórmulas, todas las fuentes y el registro histórico; `Simulación Margen` y score de Nichos **no** se completan con costos ficticios.

Se ejecutaron Data Fidelity Preflight v2.4 y Matrix Validator `full-matrix-v5 0.7.0`, `phase=12` usando `scripts/validate-method-v2-checkpoint.sh`. Data Fidelity Preflight v2.4 PASS y Matrix Validator `full-matrix-v5 0.7.0` PASS, errores=0, warnings=0, info=0; SHA de `aut137`: `bae4d15aca6f6599ae7895ae59b6284c5fb917014b08bed531fb1683eb2d82ca`. **F12 CLOSED, F13 AUTO habilitada.** El checkpoint documental se realizará después de F13, sin cierre independiente intermedio.
