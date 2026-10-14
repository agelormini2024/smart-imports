---
id: si-research-098
title: BRAND-CAND-007 — Method v2 — F9 Import Cost Headroom
version: 0.1.0
status: closed
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
phase: F9
mode: AUTO
scope_value: Marca Fitness — fuerza accesible y compacta
baseline: aut133
baseline_sha256: 02a689d96fd98d2b46fea21aa5d6630fa27eff7a5f0e0cfa10d61bae6f8b1ccf
matrix_target: aut134
created: 2026-10-14
---

# SI-RESEARCH-098 — BRAND-CAND-007 — F9 Import Cost Headroom

**ESTADO VALIDADO:** `aut134` generada, Data Fidelity Preflight v2.4 PASS y Matrix Validator full-matrix-v5 0.7.0 PASS (errores=0, warnings=0, info=0, findings=[]). F9 CLOSED / AUTO. Baseline `aut133` inalterada.

## 1. Método económico histórico

Fuente del supuesto: criterio histórico de Method v2 utilizado por `BRAND-CAND-010/F9`, NO estimación de tributos ni cotización logística actual:

- FX de comparación histórico del 13/10/2026: **ARS 1.535 por USD**, capturado y verificado en `ML-0178`, `ML-0180`, `ML-0181`.
- Costo de canal: **25 %** del precio bruto.
- Costo comercial: **5 %** del precio bruto.
- Margen objetivo: **25 %** de las ventas netas tras el costo de canal.
- **Techo económico de costo landed = [(1−0,25)×(1−0,25)−0,05] × precio bruto = 0,5125 × precio bruto**.

Esta fórmula es un presupuesto económico admisible para **todos los componentes del costo landed**, no un cálculo de gastos aduaneros ni un precio FOB objetivo acordado.

## 2. Comparables Mercado Libre / techo importado admisible

| Product Base | Comparable origen local | Precio verificado ARS | USD a FX histórico | Máximo landed económico USD/unidad |
|---|---|---:|---:|---:|
| `BASE-FIT-005` — 11 piezas tubulares | `ML-0178 / SRC-0525` — Gadnic | 39.999 | 26,0580 | **13,3547** |
| `BASE-FIT-007` — kit 20 kg | `ML-0181 / SRC-0528` — BS Fit | 64.999 | 42,3446 | **21,7016** |
| `BASE-FIT-007` — kit 20 kg | `ML-0180 / SRC-0527` — GMP | 93.018 | 60,5980 | **31,0565** |

Valores derivados de importes verificados con mayor precisión interna que los precios USD redondeados ya visibles en la matriz.

## 3. Fuente de origen comparable y brecha

**`BASE-FIT-005` / `COT-0065`, `SRC-0531` — Ningbo Time-Create:** oferta pública **USD 4,68/set** para 100–499 sets. `13,3547 / 4,68 = 2,85×`; máximo económico restante **USD 8,6747/set** para transporte, seguros, tributos no recuperables, tasas, despacho, logística local y cualquier costo que corresponda. No equivale a una estructura de costo landed validada.

**`COT-0066`, `SRC-0532` — Deep Fitness:** anuncio USD 2,46–3,00, sin atribución unívoca a kit/configuración/tier. No se coloca el precio del extremo del rango en el campo de cotización comparable; no se declara ganador por precio.

**`BASE-FIT-007` / `COT-0067..0069`, `SRC-0533..0535`:** precios publicados por familias 10/15/20 kg y materiales distintos; sin precio por kit completo 20 kg atribuido en forma inequívoca. Por ello **NO SE CALCULA** ratio precio local/precio de origen para mancuernas, ni se extrapolan comparables 20 kg a 10/15 kg.

En fecha de esta actualización, el Founder informó que envió **dos consultas comerciales breves a proveedores** para especificar precio por configuración y datos de peso/packing. **Respuestas pendientes; proveedores consultados no identificados documentalmente en este gate**. Es una excepción informativa acotada, sin comprometer compra ni homologar proveedores. Las respuestas deberán incorporarse como nueva evidencia source-bound, con fecha y modelo, sin modificar retroactivamente F8.

## 4. Decisión técnica F9 — validada

- `BASE-FIT-005`: **SURVIVES PRELIMINARY HEADROOM — CONDITIONED**, sujeto a costos de importación, riesgos de seguridad y verificación del producto.
- `BASE-FIT-007`: **UNDETERMINED / MISSING EXACT ORIGIN PRICE**, no STOP ni PASS económico por ahora.
- `BASE-FIT-006` y `BASE-FIT-008`: se conservan en `DEFER` desde F7, sin investigación de origen adicional.

Regla: `HEADROOM ≠ LANDED COST ≠ MARGIN ≠ CASH OUTLAY`. No recalificar la demanda ni el Potencial de Marca por el headroom. No agregar score de Margen en Nichos hasta contar con evidencia económica justificable.

## 5. Materialización y doble gate — realizado

La materialización `aut133 → aut134` actualizó únicamente observaciones de `Productos Base!N102/N104` y `Nichos!AD39:AF39`. No se agregan simulaciones FOB/Landed ficticias; las 29 hojas y 1.942 fórmulas deben conservarse, y las demás celdas no alterarse. Se ejecutó:

```bash
bash scripts/validate-method-v2-checkpoint.sh "<path-aut134>.xlsx" "Marca Fitness — fuerza accesible y compacta" 9
```

**Resultado confirmado:** Data Fidelity Preflight v2.4 PASS y Matrix Validator full-matrix-v5 0.7.0 PASS. F9 CLOSED / AUTO, `aut134` queda como baseline para F10. SHA-256: `cdfd9960d7f1a36222a85c9c31c242a6259d84cef334cf2e259ada3131322071`. Log privado `resultado-aut134-f9.log`; checkpoint documental acumulado previsto al finalizar F13. Ninguna selección ni homologación de proveedor.
