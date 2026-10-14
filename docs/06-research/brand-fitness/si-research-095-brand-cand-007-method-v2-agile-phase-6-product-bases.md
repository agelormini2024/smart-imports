---
id: si-research-095
title: BRAND-CAND-007 — Method v2 — F6 Product Bases
version: 0.1.1
status: closed
phase: F6
mode: AUTO
brand: brand-fitness
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
scope_alias: Nicho ID 38
baseline: aut130
matrix: aut131
created: 2026-10-13
updated: 2026-10-14
related:
  - si-bim-proc-003
  - si-research-090
  - si-research-091
  - si-research-092
  - si-research-093
  - si-research-094
---

# SI-RESEARCH-095 — BRAND-CAND-007 — F6 Product Bases

## 1. Regla y alcance

F6 es la **primera fase que crea Product Bases**. Se heredan F1 (mapa de soluciones), F2 (madurez), F3 (demanda, Founder Approved 3/5 Media), F4 (competencia 3/5 Media validada) y F5 (potencial de marca 3/5 Baja validado). La creación se condiciona a dual PASS canónico en F4 y F5. F6 usa la **misma cohorte F3/F4 de seis publicaciones**, sin nuevas capturas, nuevos precios, fuentes de Alibaba ni inferencias de origen.

```text
PUBLICATION ≠ PRODUCT BASE
ARCHITECTURE ≠ PRODUCT BASE
BRAND ≠ PRODUCT BASE
CAPABILITY CLAIM ≠ VERIFIED TEST
```

Una Product Base normaliza una solución funcional con mecanismo, riesgo, uso y obligaciones técnicos definidos. No representa una marca, un proveedor o un SKU específico.

## 2. Cuatro Product Bases candidatas

| ID | Solución normalizada | ML de respaldo | Diferencia material | Gate crítico |
|---|---|---|---|---|
| `BASE-FIT-005` | Kit de bandas **tubulares con manijas/anclaje** | `ML-0178` / Gadnic | Uso con agarres y puerta; tensión dependiente de elongación | Seguridad del anclaje, ensayo de bandas y accesorios |
| `BASE-FIT-006` | Set de bandas **loop cerradas**, resistencia y asistencia | `ML-0179` / Alpina | Geometría cerrada y usos mixtos con calistenia/movilidad | Durabilidad y progresión; demanda específica de fuerza condicionada |
| `BASE-FIT-007` | Kit compacto **mancuernas/barra con discos ajustables**, formato 20 kg | `ML-0180, ML-0181` / GMP, BS Fit | Masa desmontable, barras/roscas y logística pesada | Composición real, fijación/roscas, tolerancia de masas, flete |
| `BASE-FIT-008` | Sistema de **entrenamiento en suspensión** con cintas y anclaje | `ML-0182, ML-0183` / MrGym, FIT MARK | Resistencia por peso corporal, dependencia del montaje | Seguridad crítica de anclaje, costuras y límites de uso |

La división entre `005` y `006` se justifica por el mecanismo/uso de bandas y la carga de usuario; no son variantes intercambiables sin más. GMP/BS Fit comparten base funcional **sin presumir que sean el mismo SKU, composición o calidad**. MrGym y FIT MARK pertenecen a una base mecánica comparable, pero sus claims 120/200 kg no fueron verificados ni hacen seguro al conjunto.

## 3. Integridad de materialización

- `Productos Base!A102:N105`: cuatro registros nuevos `BASE-FIT-005..008`, sin modificar `BASE-FIT-001..004` ni bases históricas de otros territorios.
- `Publicaciones ML!Q179:R184`: se vincula cada una de las seis publicaciones a su Product Base, **recién en F6**.
- `Competencia ML!F177:G182`: se propagan las mismas vinculaciones, conservando `COMP-0176..0181`.
- No se editan los precios ARS/USD, ventas visibles, IDs originales, fechas, fuente FX ni `Verificaciones ML` históricos.
- Las columnas de volumen/ratings de Product Bases se derivan solamente de los seis comparables observados. No son volumen de mercado, prueba de tamaño de nicho, ni ensayo de calidad.
- No se abre sourcing, F8 ni F14, ni se define presupuesto/ROI. El primer triage y shortlist pre-origin corresponde a F7.

## 4. Lectura para F7 (no es todavía shortlist)

- `BASE-FIT-005`/`006`: favorables por volumen y almacenamiento, pero alto riesgo de indiferenciación, seguridad/durabilidad y limitaciones de resistencia reproducible.
- `BASE-FIT-007`: progresión explícita de carga y demanda observada; la logística de 20 kg, mecanismos y control de materiales son gates comerciales relevantes.
- `BASE-FIT-008`: formato compacto y ventas visibles positivas, con **condición estricta de seguridad**. No admitir equivalencias o claims de carga como sustitutos de ensayos.

No hay finalista ni prioridad de importación definida. La posterior F7 evaluará si cada PB debe pasar, diferirse o detenerse antes de sourcing. `DECISION-GRADE ≠ PROCUREMENT-GRADE`.

## 5. Materialización, doble PASS y cierre de F6

```text
F4: aut129 — doble PASS / CLOSED
F5: aut130 — doble PASS / CLOSED
F6: matrix-aut131-brand-cand-007-phase6-product-bases-pre-gate.xlsx
SHA-256: 99477da455a27a477245b5e4bc66c00992597f1b1ff32c2ab6376258f54c078d
Product Bases: BASE-FIT-005..BASE-FIT-008 (4)
Publicaciones vinculadas: ML-0178..ML-0183 (6)
Data Fidelity Preflight v2.4: PASS (6 publicaciones, 6 verificaciones, 4 Product Bases)
Matrix Validator full-matrix-v5 0.7.0: PASS (0 errores / 0 warnings / 0 info)
F6: CLOSED — AUTO
Next: F7 — Shortlist Pre-Origin / AUTO
Checkpoint documental: único para F4–F6, con commit/push humano.
```

El doble PASS fue confirmado en el log consolidado de validación F4–F6. Las cuatro Product Bases son candidatas normalizadas; **no hay finalista, proveedor seleccionado ni decisión de importación**. F8 continúa siendo `COLLABORATIVE` y requiere revisión explícita del Founder.
