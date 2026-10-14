---
id: si-research-099
title: BRAND-CAND-007 — Method v2 — F10 Minimum Landed Cost Dataset
version: 0.1.0
status: closed
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
phase: F10
mode: AUTO
scope_value: Marca Fitness — fuerza accesible y compacta
baseline: aut134
baseline_sha256: cdfd9960d7f1a36222a85c9c31c242a6259d84cef334cf2e259ada3131322071
matrix_target: aut135
created: 2026-10-14
---

# SI-RESEARCH-099 — BRAND-CAND-007 — F10 Minimum Landed Cost Dataset

## 1. Propósito

Consolidar el **dataset mínimo verificable y el registro explícito de brechas** a partir de F8 y F9. Este gate de Method v2 es AUTO. F10 **no genera FOB, landed cost, margen, ROI ni habilita compra**.

La evaluación `decision-grade` admite proxies documentados en F11, pero **un proxy no transforma una cotización pública incompleta en un precio confirmable de compra**. Las dos consultas breves realizadas por el Founder a proveedores de mancuernas siguen pendientes de respuesta al preparar este Research.

## 2. Datos por oferta (Capa A — publicaciones de origen, sin extrapolación)

| Cotización / Fuente | PB | Precio de origen usable | MOQ publicado | Datos logísticos observados | Cobertura y brechas |
|---|---|---|---|---|---|
| `COT-0065` / `SRC-0531` — Ningbo Time-Create | `BASE-FIT-005` | **USD 4,68/set** para 100–499 | 100 sets al tier | La ficha declara 1 kg bruto; no se confirmó el carton por set ni CBM | **PARCIAL**: sin packing exacto/Incoterm; no hay pruebas de fatiga/anclaje |
| `COT-0066` / `SRC-0532` — Zhenjiang Deep | `BASE-FIT-005` | USD 2,46–3,00, **rango NO utilizable como precio exacto** | 100 sets públicos; logo sujeto a variante | Peso bruto y dimensiones no vinculados a set/tier | **INCOMPLETO**: composición contradictoria; precio y packing pendientes |
| `COT-0067` / `SRC-0533` — Yiwu Jian Yi | `BASE-FIT-007` | USD 20,80–74, **sin precio de kit 20 kg** | Anuncio: 2 sets; texto: “sin MOQ” para stock | Declara 21 kg brutos y 42×23×16 cm, **variante no vinculada** | **INCOMPLETO**: falta atribuir precio, materiales, carga exacta y packing a 20 kg |
| `COT-0068` / `SRC-0534` — Yiwu Lehe | `BASE-FIT-007` | USD 12,86–99,21, **sin precio por configuración** | **50 kg de masa total del pedido**, no 50 sets; custom packaging desde 100 kg | Sin medidas y peso bruto exactos por variante | **INCOMPLETO**: 10/15/20 kg no equivalentes en demanda, ni seleccionados |
| `COT-0069` / `SRC-0535` — Hebei Brilliant | `BASE-FIT-007` | USD 4,67 publicado, **NO atribuible a kit 10/15/20 kg** | 10 sets general; **300 sets para personalización de marca** | Declara 16 kg y 45×25×16 cm, **variante no vinculada** | **INCOMPLETO**: cemento/PVC, no equivalente materialmente a hierro fundido |

El perfil verificado del proveedor y las insignias comerciales no acreditan ensayos independientes de un producto específico. Ninguna publicación es una cotización formal ni documenta un costo puesto en Argentina.

## 3. Datos reutilizados de F9 (Capa B — variables económicas de comparación)

- FX histórico de ML (13/10/2026): 1.535 ARS/USD; **no es un tipo de cambio actual ni operativo**.
- Modelo histórico para headroom: techo económico landed del 51,25 % del precio bruto local bajo los supuestos definidos en F9.
- `BASE-FIT-005` máximo landed USD **13,3547** sobre `ML-0178` y precio origen **4,68** a tier de 100–499, sin confirmar FOB ni transporte.
- `BASE-FIT-007` máximo landed 20 kg USD **21,7016** (`ML-0181` BS Fit) o **31,0565** (`ML-0180` GMP); costo exacto de origen 20 kg **NO DISPONIBLE**.

## 4. Dataset mínimo para F11 — clasificación de brechas (Capa C)

`BASE-FIT-005`: existe al menos una **referencia unit price+MOQ** pública; se desconoce volumen logístico/peso facturable y gastos exigibles. F11 puede estudiar una **sensibilidad condicionada**, con proxies numéricos explícitos y sin declarar valor de aduana ni landed real.

`BASE-FIT-007`: **faltan precio y packing exactos de la misma variante de 20 kg**. F11 NO puede presentar un costo unitario ejecutable del kit. Sólo puede calcular umbrales económicos o sensibilidades hipotéticas, nunca sustituir un precio de origen por el extremo más bajo del rango Alibaba.

Para ambos casos siguen pendientes NCM, tributos aplicables, intervenciones, Incoterm/FOB, seguro, transporte y costos de despacho; el despachante debe confirmar los requisitos en la reunión. **No se los declara conocidos.**

## 5. Capa D — resultado AUTO validado

- F10: `MINIMUM DATASET DOCUMENTED — WITH MATERIAL GAPS`.
- F11 (próximo): únicamente screening de escenarios **explícitamente hipotéticos** donde falten datos; separar `NON-EXECUTABLE SENSITIVITY` de un escenario económicamente accionable.
- `BASE-FIT-005`: `PARCIAL / AIR-SENSITIVITY ELIGIBLE ONLY`.
- `BASE-FIT-007`: `INCOMPLETE / 20KG EXACT UNIT COST PENDING`.
- `BASE-FIT-006/008`: `DEFER` sin cambio.

La materialización `aut134 → aut135` actualizó únicamente las observaciones de `Productos Base!N102/N104` y `Nichos!AD39:AF39`. Preservó cotizaciones, mercado, fórmulas y simulaciones de margen. **Doble PASS técnico confirmado**: Data Fidelity Preflight v2.4 PASS; Matrix Validator full-matrix-v5 0.7.0 PASS; 0 errores, 0 warnings, 0 info; `29` hojas y `1.942` fórmulas. Matriz `aut135` SHA-256 `def947f2fa6dcde1a5596e3a16829ab9cd0be514228a778edfd10b1d68ca0c7b`. F10 **CLOSED — AUTO — MINIMUM DATASET WITH MATERIAL GAPS**. No significa `DATASET COMPLETE` ni `LANDED VALIDATED`. Siguiente F11 con escenarios no ejecutables declarados.
