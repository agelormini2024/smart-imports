---
id: si-research-097
title: BRAND-CAND-007 — Method v2 — F8 Screening preliminar de origen
version: 0.1.1
status: closed-external-hold
phase: F8
mode: COLLABORATIVE
brand: brand-fitness
brand_candidate: BRAND-CAND-007
source_hypothesis: FIT-CAND-001
scope_alias: Nicho ID 38
scope_value: Marca Fitness — fuerza accesible y compacta
baseline: aut132
matrix: aut133
created: 2026-10-14
updated: 2026-10-14
related:
  - si-bim-proc-003
  - si-decision-020
  - si-research-095
  - si-research-096
---

# SI-RESEARCH-097 — BRAND-CAND-007 — F8 Screening preliminar de origen

> **F8 — SCREENING DE ORIGEN CERRADO CON HOLD EXTERNO.** Las cinco fichas PDF fueron vinculadas en `aut133` con doble PASS técnico. El Founder Review se registra de forma expresa en el checkpoint documental posterior a la validación. Este cierre NO autoriza RFQ, compras, selección de proveedores ni apertura de F9.

## 1. Propósito y límite acordado

F7 habilitó `BASE-FIT-005` y `BASE-FIT-007` como `PASS TO ORIGIN — CONDITIONED`; `BASE-FIT-006` y `BASE-FIT-008` permanecen `DEFER`. La matriz `aut132` tuvo Data Fidelity Preflight v2.4 **PASS** y Matrix Validator `full-matrix-v5 0.7.0` **PASS**, según log de apertura de F8, con SHA-256 `ca2aa758788c53be1307aa10bb0c3b7ba03cbda0126141b1eb121844979d828b`.

Objetivo F8: constatar **existencia de ofertas de origen funcionalmente pertinentes**, clasificar diferencias críticas, documentar señales de OEM/marca propia y determinar si vale la pena **retener cada Product Base para evaluación de fricción de importación**.

**Decisión operativa del Founder (2026-10-14):** la profundización de productos y proveedores se posterga hasta después de la reunión con el socio y el despachante de aduana. No contactar proveedores, gestionar RFQ, negociar FOB, solicitar muestras ni homologar fábricas ahora. Las decisiones de importación dependerán de requisitos aplicables, logística, costos y fricción informados por el despachante, además del criterio del socio.

Principios: `LISTING PUBLICADO ≠ COTIZACIÓN`; `PROVEEDOR CON PERFIL VERIFICADO ≠ PRODUCTO HOMOLOGADO`; `MISMA PRODUCT BASE ≠ MISMO SKU`; `PRECIO PUBLICADO ≠ COSTO PUESTO EN ARGENTINA`; `SCREENING DE ORIGEN ≠ AUTORIZACIÓN DE COMPRA`.

## 2. Capa A — Evidencia capturada: fuentes individualizadas

Se respetan las **cinco publicaciones distintas**; las etiquetas `CAP-F8-A` a `CAP-F8-E` son claves temporales de esta revisión, **no IDs oficiales de la matriz**. La fuente primaria es cada PDF aportado en la conversación. El `productId` fue verificado en hipervínculos embebidos dentro del PDF. Los SHA-256 identifican exactamente las copias examinadas.

| Etiqueta provisional | Product Base | Proveedor publicado | Product ID Alibaba | SHA-256 PDF |
|---|---|---|---|---|
| `CAP-F8-A` | `BASE-FIT-005` | Ningbo Time-Create Fitness Equipment Co., Ltd. | `1601851365077` | `d0128078facc65fb8d6a5efe13f724cce4cee2a669f55d264082389ae99210b6` |
| `CAP-F8-B` | `BASE-FIT-005` | Zhenjiang Deep Fitness Co., Ltd. | `1601666139578` | `056fdcc72d86f24d26d5e6f910c0d66c5d0b0b4a53fafdc2a9838b8f115bf3d8` |
| `CAP-F8-C` | `BASE-FIT-007` | Yiwu City Jian Yi Sport Co., Ltd. | `1600106065113` | `290fc9c0f076ee1c9279f7c3da90b762bc689bee1c8b833d2846fb7fb217b30d` |
| `CAP-F8-D` | `BASE-FIT-007` | Yiwu City Lehe Sport Co., Ltd. | `1601484448871` | `e6ce1c02d4f7489e58e49561ca418eb86c5e031e0d6b3b53941bf2feeadc8810` |
| `CAP-F8-E` | `BASE-FIT-007` | Hebei Brilliant Sporting Goods Trading Co., Ltd. | `1600606590613` | `0bb98ffc598df43fe8cf85f719b5797139e0afe4bbbc1e017013b602f367e307` |

Los PDF de las cinco fuentes permanecen como evidencias privadas; no se suben al repositorio público. Los precios y las condiciones se refieren al **momento de captura**, no son ofertas vinculantes ni cotizaciones EXW/FOB verificadas para nuestro pedido.

## 3. Capa B — Clasificación y comparación de BASE-FIT-005

| Campo | Time-Create (`CAP-F8-A`) | Deep Fitness (`CAP-F8-B`) |
|---|---|---|
| Producto | Kit de 11 piezas, 5 tubos, agarres/anclaje/correas/bolsa | Kit de 11 piezas, 5 tubos, agarres/anclaje/correas/bolsa |
| Longitud declarada | 1.200 mm | 1.200 mm |
| Material | «100 % látex natural» declarado | TPE/látex, «caucho» y «sin látex» según secciones: inconsistente |
| Precio público | US$ 4,68 para 100–499; US$ 4,32 para 500–999; US$ 4,14 para 1.000–2.999; US$ 3,78 para ≥3.000 | US$ 2,46–3,00, sin desglose inequívoco por configuración/cantidad |
| MOQ anunciado | 100 conjuntos para primer tramo | 100 conjuntos para precio publicado; descripción también anuncia 1 sin logo |
| Marca propia | Logo y embalaje anunciados | Logo y embalaje anunciados; logo desde 100 según ficha |
| Proveedor según Alibaba | Trading Company, perfil de 10 años | Fabricante personalizable, perfil verificado por Intertek; no verificación independiente de esta línea |
| Ensayos de resistencia, fatiga, anclaje | No aportados | No aportados; insignias de certificación en la ficha sin comprobar alcance |

**Clasificación:** las dos publicaciones son **funcionalmente compatibles con `BASE-FIT-005`**, NO se demuestra que correspondan al mismo diseño, fábrica, material o calidad. El menor precio público de Deep Fitness es una **señal comercial**, no una ventaja de costo comparado homologada.

**Inconsistencia destacada Deep Fitness:** la ficha menciona 100/150 lb, mientras el desglose de cinco bandas indica 10/15/20/25/30 lb (100 lb nominales sumadas); esto **no** acredita una resistencia segura del sistema combinado o del anclaje.

**Estado propuesto:** `ORIGIN OFFER OBSERVED — CONDITIONED / TECHNICAL SAFETY GATE / NO SUPPLIER APPROVED`.

## 4. Capa B — Clasificación y comparación de BASE-FIT-007

| Campo | Jian Yi (`CAP-F8-C`) | Lehe (`CAP-F8-D`) | Hebei Brilliant (`CAP-F8-E`) |
|---|---|---|---|
| Material declarado | Hierro fundido | Hierro/acero/acero inoxidable (familia; versión no aislada) | Cemento interior + plástico/PVC exterior |
| Variantes | 15, 20, 30, 50 kg y otras mencionadas | 10, 15, 20, 30, 40, 50 kg; título también 25 kg | 10, 15, 20, 30, 40 kg |
| Precio público | US$ 20,80–74 (conjunto/variante exacta pendiente) | US$ 12,86–99,21 (desglose pendiente) | US$ 4,67 (no atribuible a 10/15/20 kg específicos) |
| MOQ público | 2 conjuntos; detalle dice «sin MOQ» para stock | 50 kg de pedido; personalización de embalaje desde 100 kg | 10 conjuntos; personalización de logo/embalaje/gráfica desde 300 conjuntos |
| Packaging / peso | Maletín 42×23×16 cm, 21 kg brutos (variante no identificada con certeza) | Maletín mostrado, sin packing bruto exacto por variante | Paquete 45×25×16 cm y 16 kg brutos (variante no identificada) |
| Marca propia | Personalización anunciada; ficha menciona logo York o ninguno | Logo no incluido en precio y embalaje custom separado; perfil con «PINJIAN» | Logo y embalaje disponibles bajo MOQ mayor |
| Perfil | Fabricante personalizable / Intertek en ficha | Fabricante personalizable / TÜV Rheinland en ficha | Trading Company en ficha |
| Fricción crítica | Masa logística, roscas/fijaciones, composición real, marcas de tercero | Material y peso por variante, costo EXW exacto, MOQ real | Durabilidad de recubrimiento, fijaciones, precio no comparable, MOQ de marca propia |

**Observación técnica Jian Yi:** se enumeran 4×2,5 + 4×1,25 + 4×0,5 kg = **17 kg en discos**; la diferencia hasta 20 kg podría estar en barras y accesorios, pero **no está documentada la masa neta exacta de la configuración**. No asumir que toda la carga es utilizable como se anuncia.

**Observación técnica Lehe:** el anuncio declara varias configuraciones, pero no desglosa precio, discos, barras, peso bruto o material específico para cada una. La variante de **15 kg es una hipótesis comercial para explorar**, no una variante seleccionada ni con demanda validada específicamente. La ficha indica precios EXW; marca y packaging personalizado requieren una cotización aparte.

**Observación técnica Hebei:** confirma tecnología **cemento/PVC** y conversión de mancuernas a barra, distinta técnicamente de hierro fundido. La tarifa logística mostrada por la interfaz para diez conjuntos NO es una cotización de transporte consolidado. El MOQ de logo/embalaje 300 sets podría generar fricción de capital. El precio US$ 4,67 NO queda asignado a un set completo de 10/15/20 kg.

**Relación societaria:** Jian Yi y Lehe anuncian productos «PINJIAN», pero las fichas tienen **razones sociales diferentes**. No inferir que sean el mismo fabricante o que compartan fábrica.

**Estado propuesto:** `ORIGIN OFFERS OBSERVED — CONDITIONED / LOGISTICS + QUALITY GATE / NO SUPPLIER APPROVED`.

## 5. Capa C — Lectura comercial, sin seleccionar productos ni proveedores

| Product Base | Viabilidad de investigar más adelante | Bloqueo externo principal | Prioridad de fricción para el despachante |
|---|---|---|---|
| `BASE-FIT-005` | Dos ofertas funcionalmente comparables, pequeñas y aparentemente personalizables; proveedor Deep con precio público inferior | Falta de datos técnicos verificables de bandas, anclajes y accesorios | Identificar clasificación y requisitos aplicables al kit completo (materiales, accesorios, etiquetado, verificaciones) + impacto económico real |
| `BASE-FIT-007` | Tres ofertas de origen; hierro fundido y cemento no son equivalentes técnicamente; posibilidad de 10/15/20 kg para entrada más liviana | Peso, transporte, integridad estructural, fijaciones, MOQ de personalización; margen sin calcular | Clasificación y requisitos por material/configuración, tributación y fricción logística; estimar incidencia de bulto pesado para un embarque mixto |

No se asigna score ni prioridad definitiva en F8. La menor masa por kit **puede** reducir costo logístico absoluto, pero no garantiza mayor margen ni demanda; tampoco se extrapola la evidencia F3 de 20 kg a 10/15 kg.

## 6. Capa D — Decisión de screening para Founder Review

```text
BASE-FIT-005: ORIGIN OPTIONS OBSERVED / CONDITIONED / HOLD FOR EXTERNAL FRICTION REVIEW
BASE-FIT-007: ORIGIN OPTIONS OBSERVED / CONDITIONED / HOLD FOR EXTERNAL FRICTION REVIEW
BASE-FIT-006: DEFER (se conserva F7)
BASE-FIT-008: DEFER (se conserva F7)
Supplier approval: NONE
RFQ/contact/sample: NONE
Import/portfolio finalist: NONE
Sourcing deepening: ON HOLD — AFTER PARTNER + CUSTOMS BROKER MEETING
F8 Founder Review: APPROVED — aprobación expresa registrada en el checkpoint documental único F7–F8
F8 matrix materialization: aut133 — SHA-256 02a689d96fd98d2b46fea21aa5d6630fa27eff7a5f0e0cfa10d61bae6f8b1ccf
F8 canonical validation: Data Fidelity PASS + Matrix Validator PASS — 0 errores / warnings / info
F8 documentary checkpoint (together with F7): cierre aprobado, aplicación documental sujeta al script verificado
```

La recomendación es **congelar este conjunto de evidencias** como suficiente para un *screening de origen*, sin confundirlo con *sourcing*. No elevar `PASS TO ORIGIN` a una decisión comercial de importar. No iniciar F9–F13 con supuestos ficticios de precio o costo.

## 7. Agenda sintética para socio + despachante

Pedir al despachante, sobre las dos soluciones funcionales y sus principales variantes/materiales, que identifique:

- clasificación arancelaria/NCM y necesidad de desagregar kits por componentes;
- intervenciones, certificaciones técnicas, etiquetado, seguridad y documentación exigibles, si corresponden;
- tributos/cargos relevantes y documentación/condiciones de despacho;
- fricciones logísticas por bulto/peso/material; impacto potencial de consolidar con productos de otra familia;
- incertidumbres, consultas profesionales adicionales y documentación que haya que solicitar **recién después** al proveedor.

Revisar con el socio: capital/volumen de prueba, preferencia por primera etapa de catálogo, tolerancia a riesgos de posventa y estrategia de marca. Sin resultados de estas reuniones **no se escogen proveedores ni se aprueban variantes**.

## 8. Materialización, aprobación y cierre F7–F8

```text
F7: aut132 / SHA-256 ca2aa758788c53be1307aa10bb0c3b7ba03cbda0126141b1eb121844979d828b / doble PASS / CLOSED AUTO
F8: aut133 / SHA-256 02a689d96fd98d2b46fea21aa5d6630fa27eff7a5f0e0cfa10d61bae6f8b1ccf
Data Fidelity Preflight v2.4: PASS — 6 publicaciones / 6 verificaciones / 4 Product Bases
Matrix Validator full-matrix-v5 0.7.0: PASS — errors 0 / warnings 0 / info 0 / findings [] / limitations []
Nuevas fichas registradas: COT-0065..0069 (5)
Fuentes: SRC-0531..0535 (5)
Evidencias: EVID-0312..0316 (5)
Vínculos: EVSRC-0728..0732 (5)
Product Bases en origen: BASE-FIT-005, BASE-FIT-007 — HOLD / condicionadas
Product Bases diferidas: BASE-FIT-006, BASE-FIT-008 — DEFER / reapertura fundamentada
F8: CLOSED / COLLABORATIVE / FOUNDER REVIEW APPROVED / EXTERNAL FRICTION HOLD
F9: NOT OPENED — no asumir precios FOB, landed cost ni viabilidad de importación
```

El doble PASS canónico está en `resultado-aut133-f8.log`. La matriz `aut133` es **snapshot técnico previo a la decisión humana**: sus celdas de resumen pueden indicar `Founder Review pendiente` porque ése era el estado al momento de validar. No se editan retrospectivamente esas celdas ni se declara un `aut134` inexistente. La aprobación posterior se documenta en este Research y en el checkpoint de Git, con aceptación explícita del Founder durante su aplicación.

**Condición de reapertura:** primero reunión con el socio y el despachante para revisar clasificaciones, intervenciones, tributos, logística, posventa y fricción real. Recién entonces decidir qué investigar más profundamente, si alguna Product Base merece prioridad o si hay que reordenar la cartera.

**Estado final F8: SCREENING PRELIMINAR COMPLETO / EVIDENCIAS VINCULADAS / DOBLE PASS / EXTERNAL REVIEW HOLD. Sin proveedores homologados, sin compras y sin inicio de F9.**
