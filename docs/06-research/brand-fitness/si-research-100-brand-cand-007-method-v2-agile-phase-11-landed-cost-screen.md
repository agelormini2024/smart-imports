---
id: si-research-100
title: BRAND-CAND-007 — Method v2 — F11 Landed Cost Screen
version: 0.1.0
status: closed
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
phase: F11
mode: AUTO
scope_value: Marca Fitness — fuerza accesible y compacta
baseline: aut135
baseline_sha256: def947f2fa6dcde1a5596e3a16829ab9cd0be514228a778edfd10b1d68ca0c7b
matrix_target: aut136
matrix_sha256: 2e2a9728768b884c407b1abdc0ebbc4a9e0063f85a39f270a59b73fe34c619c6
created: 2026-10-14
---

# SI-RESEARCH-100 — F11 Landed Cost Screen (stress no ejecutable)

> **F11 CLOSED — AUTO — DOBLE PASS técnico sobre `aut136`.** Esta fase sólo prueba restricciones mediante un proxy histórico, **no** construye un landed cost ni un presupuesto de nacionalización. `AIR STRESS SCREEN ≠ LOGISTICS PLAN`.

## 1. Contrato y fuentes

- Baseline de datos F10: `SI-RESEARCH-099`, `aut135` doble PASS, cinco ofertas `COT-0065..0069` con brechas registradas.
- Demanda local: `ML-0178` (bandas), `ML-0180` (GMP 20kg), `ML-0181` (BS Fit 20kg); cotizaciones de origen F8 `COT-0065..0069`.
- Modelo económico F9 `SI-RESEARCH-098`: FX histórico ARS 1.535/USD y techo landed económico del 51,25% del precio bruto local. Es **modelo histórico**, no FX efectivo del día.
- **Proxy histórico F11 de `BRAND-CAND-010`**: USD 10 por kg facturable de transporte aéreo. Es un supuesto de estrés, no una cotización reciente ni una tarifa vigente. En el modelo completo de 010 también se estudiaron aranceles, tasas y gastos, pero **no se trasplantan** aquí: falta clasificación y base material verificable para aplicarlos.
- No utilizar `COT-0066` como precio exacto ni los rangos de `COT-0067..0069` como precio del kit completo de 20 kg.

## 2. BASE-FIT-005 — bandas tubulares

| Magnitud | Valor / condición |
|---|---:|
| Precio local histórico `ML-0178` | ARS 39.999 |
| Techo landed económico F9 | **13,3547** |
| Precio origen publicado `COT-0065`, MOQ tier 100–499 | **4,68** |
| Saldo máximo para **todos** los costos adicionales | **8,6747** |
| Transporte aéreo hipotético, 1 kg facturable a USD 10/kg | **10,00** |
| Sólo producto publicado + proxy aéreo | **14,68** |
| Exceso sobre techo *antes* de arancel, seguro, despacho, tasas | **1,3253** |
| Masa facturable máxima matemática a USD 10/kg *antes de cualquier otro costo* | **0,8675 kg** |

**Interpretación:** con 1 kg facturable y proxy de USD 10/kg, el **origen publicado + flete ilustrativo ya supera el techo**. La ficha comercial informa 1 kg bruto, pero el peso/volumen no están inequívocamente ligados al kit y su packing comparable. Por tanto es **una condición, no un peso de embarque confirmado**. El cálculo tampoco prueba que el transporte marítimo/LCL sea malo ni bueno. El costo de mercancía de USD 4,68 no equivale a FOB confirmado.

## 3. BASE-FIT-007 — mancuernas ajustables, kit 20 kg

| Variable | Observación |
|---|---|
| Techo landed 20 kg `ML-0181`, BS Fit | **USD 21,7016/kit** |
| Techo landed 20 kg `ML-0180`, GMP | **USD 31,0565/kit** |
| Precio de origen atribuible a 20 kg | **No disponible** |
| Peso bruto / carton atribuible a 20 kg | **No disponible** |
| Modelo de escenario aéreo ilustrativo | **SI** el peso facturable fuera al menos 20 kg, USD 10/kg implicaría **al menos USD 200 sólo de flete** |

El condicional **no asigna a ningún proveedor** un flete de USD 200 ni prueba que el bulto pese 20 kg cargables; es una prueba de sensibilidad extrema de una ruta hipotética. Los números 21 kg/16 kg y tamaños de caja están publicados en fichas de familia **sin SKU/variante atribuida**. No completar el costo de origen de `BASE-FIT-007` usando el menor valor del rango Alibaba. Las dos consultas a proveedores podrían mejorar la base F10–F11 al llegar; no deben modificar retroactivamente F8.

## 4. Brechas externas no resueltas

Flete marítimo/LCL y volumetría verificable por variante, clasificación NCM, aranceles, tasas, intervenciones, seguro, despacho, cash outlay, logística local, Incoterm, seguridad/calidad y condiciones de marca propia. Los importes no calculados son **desconocidos**, no cero.

## 5. Capa C y D — decisión técnica F11

- `BASE-FIT-005`: `NON-EXECUTABLE AIR STRESS / UNFAVORABLE UNDER STATED ASSUMPTION / MARITIME UNDETERMINED`.
- `BASE-FIT-007`: `NON-EXECUTABLE AIR STRESS / EXACT 20KG PRICE AND PACKING MISSING / MARITIME UNDETERMINED`.
- `BASE-FIT-006/008`: `DEFER`, sin cambios.
- F11 **no decide** STOP/PASS o rentabilidad. F12 interpretará las sensibilidades **sin recalcular F11**; F13 integrará una shortlist provisional para el Decision Report antes de las reuniones con socio y despachante.

## 6. Materialización y gate confirmados

`aut135 → aut136` materializada y validada el 2026-10-14. Se actualizaron únicamente `Productos Base!N102/N104` y `Nichos!AD39:AF39` (cinco celdas narrativas); se conservaron 29 hojas y 1.942 fórmulas, sin escribir en `Cotizaciones Proveedores`, `Simulación Margen`, publicaciones o campos históricos de score.

**Resultado verificado:** Data Fidelity Preflight v2.4 **PASS** y Matrix Validator `full-matrix-v5 0.7.0` **PASS**, errores 0 / warnings 0 / info 0 / findings [] / limitations []; SHA-256 `2e2a9728768b884c407b1abdc0ebbc4a9e0063f85a39f270a59b73fe34c619c6`. Log canónico privado: `resultado-aut136-f11.log`. Estado: **F11 CLOSED / AUTO / STRESS SCREEN CONDICIONADO**, sin landed ni precio comprable confirmado. F12 interpretará, sin recalcular. Checkpoint documental acumulado previsto al terminar F13.
