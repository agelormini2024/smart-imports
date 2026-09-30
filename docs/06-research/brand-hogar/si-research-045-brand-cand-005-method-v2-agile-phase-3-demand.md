---
id: si-research-045
title: BRAND-CAND-005 — Method v2 Agile — F3 Demand
description: Recolección y normalización de demanda observable en Mercado Libre para compostaje y procesamiento doméstico de residuos orgánicos.
version: 0.1.0
status: draft
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-28
updated: 2026-09-28
brand: brand-hogar
brand_candidate: brand-cand-005
method: method-v2-agile
phase: F3
---

# BRAND-CAND-005 — Method v2 Agile — F3 Demand

Fecha: 2026-09-28  
Estado: `CLOSED`

## 1. Input vigente

F2 quedó formalmente cerrada sobre:

```text
matrix-aut75-brand-cand-005-phase2.xlsx
SHA-256: 71548058212577e02933ebd5c3377a1b18617a0195507e3626b4fa0558b6869e
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

F3 es `COLLABORATIVE`: la evidencia local proviene de publicaciones reales de Mercado Libre aportadas por Alejandro y normalizadas contra las arquitecturas A1–A6.

## 2. Regla de lectura

```text
PUBLICACIONES ≠ DEMANDA
VENTAS VISIBLES ≠ TAMAÑO DE MERCADO
VENTAS DEL VENDEDOR ≠ VENTAS DEL ÍTEM
BADGE "MÁS VENDIDO" ≠ CONTADOR DE UNIDADES
MISMA BASE CON MUCHAS MARCAS ≠ MUCHOS PRODUCTOS BASE
```

La ausencia de contador visible tampoco se interpreta como ausencia de demanda.

## 3. Acceso a Mercado Libre

Las URLs directas aportadas por Alejandro fueron preservadas en la matriz.

El acceso directo a varias páginas presentó `403 Forbidden` o `cache miss`, pero el índice público de Mercado Libre permitió recuperar señales suficientes para registrar el batch 1.

Los PDFs locales se conservan como respaldo para los casos donde el mecanismo exacto o algún atributo no quede suficientemente determinado por el índice.

## 4. Batch 1 — publicaciones registradas

### ML-0140 — A2 — Compostera giratoria Ecorege 120 L

```text
Producto: Compostera Giratoria 120 L - Doble Cámara
Arquitectura: A2 — compostaje aeróbico giratorio / tumbler
Marca: Ecorege
Vendedor: FUNDACION REGENERAR
Precio observado: ARS 188.340
Ventas visibles: +1000
Rating: 4.7
Opiniones: 358
```

Señal: fuerte para A2.

La publicación declara dos cámaras de 60 L, estructura giratoria y polipropileno reciclado.

### ML-0141 — A3 — Greener's Family 120 L

```text
Producto: Compostera Urbana Greener's Family 120 Lts + Manual
Arquitectura: A3 — vermicompostaje
Marca: greeners mas verde
Vendedor: GREENERS
Precio observado: ARS 200.000
Ventas del ítem: no informadas
Rating: 4.7
Opiniones: 24
```

La descripción vincula expresamente el funcionamiento con lombrices y estima hasta aproximadamente cuatro meses para completar el procesamiento según población inicial.

La mención `+100 ventas` corresponde al vendedor/tienda y no se traslada al ítem.

### ML-0142 — A3-compatible — Rama 40 L

```text
Producto: Compostera 40 Ltrs Con Canilla + Mesa Y Tapa
Arquitectura: A3 — vermicompostaje / modular
Marca: rama somos
Precio observado: ARS 136.000
Ventas visibles: +500
Rating: 4.9
Opiniones: 153
```

La publicación incluye material seco, compost madre y lombrices rojas californianas, por lo que se normaliza inicialmente como A3-compatible.

### ML-0143 — A1 / A3-compatible — Regenerar 60 L

```text
Producto: Compostera Domiciliaria 60l - Manual Digital - Regenerar
Arquitectura: A1 — compostaje aeróbico modular / A3-compatible
Marca: Regenerar Orgánicos
Vendedor: FUNDACION REGENERAR
Precio observado: ARS 94.558
Ventas visibles: +50
Rating: 4.8
Opiniones: 66
```

La publicación describe tres módulos de compostaje y aclara que Mercado Envíos no permite transportar material vivo. Se mantiene la compatibilidad con lombrices separada del mecanismo mínimo de compostaje.

### ML-0144 — Kompost 45 L / 4 módulos

```text
Producto: Compostera Urbana Balcón Domiciliaria Compost 45 L Kompost F 4 modulos
Arquitectura: A1/A3 — pendiente de PDF
Marca: KOMPOST®
Vendedor: KOMPOST
Precio observado en página del vendedor: ARS 98.852
Ventas del ítem: no informadas
Señal adicional: badge MÁS VENDIDO
Rating visible en listados: 4.8
```

La publicación se registra, pero el mecanismo exacto queda pendiente del PDF antes de usarla para atribuir demanda a A1 o A3.

## 5. Lectura parcial

El batch 1 ya confirma que el mercado local no está limitado a una sola forma de compostera:

- A2 muestra una señal transaccional fuerte;
- los sistemas modulares orientados a compostaje/vermicompostaje también muestran actividad real;
- existen marcas y vendedores especializados;
- la arquitectura y el proceso no pueden deducirse sólo del título comercial.

Todavía **no corresponde puntuar Demanda** porque:

- A1 no está suficientemente aislada;
- A3 aparece mezclada con sistemas híbridos/modulares;
- A4, A5 y A6 aún no tienen cobertura;
- ML-0144 requiere resolver mecanismo con PDF;
- cinco publicaciones no son una muestra suficiente del candidato completo.

## 6. Materialización

Batch 1 preparado en:

```text
matrix-aut76-brand-cand-005-phase3-batch1-corrected.xlsx
SHA-256: d1e0e31dd4c735cc8d6d5f15684ae78e0d4216aebe6c308ac20b7cf887b7a6c3
```

IDs incorporados:

```text
Publicaciones ML: ML-0140 .. ML-0144
Fuentes: SRC-0445 .. SRC-0450
Evidencia parcial: EVID-0269
Evidencia Fuentes: EVSRC-0562 .. EVSRC-0567
```

No se crea todavía `EVAL-0023`.

## 6.1 Corrección estructural de aut76

La primera exportación de `aut76` fue rechazada por el Matrix Validator con 11 errores estructurales:

- `SRC-0445..SRC-0450` sin `Fuentes.Estado`;
- `ML-0140..ML-0144` sin `Publicaciones ML.Fuente Global ID`.

No se detectó un problema conceptual de F3. La corrección completa:

- asigna `ACTIVA` a `SRC-0445..SRC-0450`;
- completa título/actor/link de las nuevas `Fuentes`;
- vincula `ML-0140..ML-0144` con `SRC-0445..SRC-0449`;
- conserva `EVID-0269` y `EVSRC-0562..0567`;
- mantiene F3 `IN PROGRESS`.

Archivo corregido:

```text
matrix-aut76-brand-cand-005-phase3-batch1-corrected.xlsx
SHA-256: d1e0e31dd4c735cc8d6d5f15684ae78e0d4216aebe6c308ac20b7cf887b7a6c3
```

## 7. Estado formal

```text
F3 ANALYSIS
→ IN PROGRESS

MATRIX MATERIALIZATION
→ BATCH 1 — aut76

MATRIX VALIDATOR
→ PENDING — corrected aut76

DEMAND SCORE
→ NOT CREATED

PHASE STATUS
→ NOT CLOSED
```

## 8. Próxima recolección

Continuar con evidencia suficiente para cubrir A1–A6.

Cuando un link no permita resolver mecanismo, ventas, opiniones o atributos relevantes, utilizar el PDF guardado por Alejandro como fuente complementaria.

## 9. URLs aportadas

Las cinco URLs originales fueron preservadas en `Publicaciones ML!Link` para trazabilidad y futuras revisiones.


## 10. Batch 2 — A4 Bokashi

Alejandro ejecutó búsquedas específicas:

```text
bokashi
compostera bokashi
balde bokashi
kit bokashi
```

La búsqueda manual produjo sólo **dos publicaciones relevantes nuevas**; el resto de los resultados correspondía a productos ya relevados en el batch anterior.

### ML-0145 — TeraGanix Bokashi

```text
Producto: Contenedor De Compostaje Teraganix Bokashi Con 2 Libras De S
Arquitectura: A4 — bokashi / fermentación anaeróbica
Marca: TeraGanix
Precio indexado: ARS 1.307.000
Ventas visibles del ítem: no informadas
Canal: importación / oferta internacional
```

La publicación indexada de Mercado Libre muestra un kit con Bokashi starter incluido y un ticket extraordinariamente alto para el mercado local. La documentación pública de TeraGanix confirma que el sistema funciona como recipiente hermético para fermentación anaeróbica con Bokashi bran.

### ML-0146 — Sunwood Life Bokashi twin-bin

```text
Producto: Sunwood Life Bokashi Compacto 2 Bins Beige
Arquitectura: A4 — bokashi / fermentación anaeróbica
Marca: Sunwood Life
Precio exacto: no recuperable
Ventas visibles del ítem: no informadas
Canal: importación / oferta internacional
```

La página exacta de Mercado Libre no pudo recuperarse por `cache miss`, por lo que no se sustituyó su precio con otro SKU.

La documentación pública de VermiTek/Sunwood Life describe el `Bokashi Twin Pack` como dos baldes que permiten uso cíclico: mientras uno fermenta, el segundo queda disponible para recibir nuevos residuos.

### Lectura parcial de A4

```text
ARQUITECTURA PRESENTE
→ SÍ

OFERTA RELEVANTE OBSERVADA
→ MUY ESCASA

OFERTA LOCAL / STOCK LOCAL ROBUSTO
→ NO DEMOSTRADO

SEÑAL TRANSACCIONAL LOCAL
→ NO DEMOSTRADA

DEPENDENCIA DE IMPORTACIÓN
→ ALTA EN LA MUESTRA OBSERVADA
```

Esto no significa `demanda nula`. Significa que, con la evidencia observada en Mercado Libre Argentina, Bokashi aparece como una arquitectura de baja densidad comercial local y sin señal transaccional suficiente para sostener una evaluación fuerte de demanda.

## 11. Materialización batch 2

Archivo preparado:

```text
matrix-aut77-brand-cand-005-phase3-batch2.xlsx
SHA-256: 32d8fe748fd961fe04fa6776ab8c0ce3e72b60a88114a615cf8caa8eac95e53f
```

IDs incorporados:

```text
Publicaciones ML: ML-0145 .. ML-0146
Fuentes: SRC-0451 .. SRC-0453
Evidencia parcial: EVID-0270
Evidencia Fuentes: EVSRC-0568 .. EVSRC-0570
```

`EVAL-0023 — Demanda` todavía **no se crea**.

## 12. Estado vigente de F3

```text
BATCH 1
→ VALIDATED — aut76 corrected PASS

BATCH 2 — A4 BOKASHI
→ MATRIX MATERIALIZED — aut77
→ MATRIX VALIDATOR PENDING

A5 / A6
→ PENDING

DEMAND SCORE
→ NOT CREATED

F3
→ NOT CLOSED
```

Próxima cobertura prioritaria:

```text
A5 — procesador eléctrico térmico / triturador / deshidratador
A6 — procesador eléctrico biológico / in-vessel
```


## 13. Batch 3 — A5 Procesador eléctrico térmico / deshidratador

Alejandro aportó cinco links surgidos de las búsquedas de compostera/procesador eléctrico.

La normalización separa cuatro candidatos de countertop food recycler de un triturador de jardín que no pertenece al core A5.

### ML-0147 — NutriChef

```text
Producto: Nutrichef Compostador Eléctrico De Cocina, Reciclador De Alimentos
Arquitectura: A5
Marca: NUTRICHEF
Precio indexado ML: ARS 1.224.000
Ventas visibles del ítem: no informadas
Canal: importado
```

La documentación pública de NutriChef define el mecanismo como:

```text
SECADO
+ TRITURACIÓN
+ ENFRIAMIENTO
→ PRE-COMPOST
```

y declara reducción de volumen de hasta 90 %.

Por lo tanto se mantiene la regla:

```text
FOOD RECYCLER
≠
COMPOST MADURO
```

### ML-0148 — Compostera eléctrica 4 L sin olor / bajo ruido

```text
Arquitectura: A5 probable
Marca: pendiente
Precio exacto: pendiente
Mecanismo exacto: pendiente de PDF
```

La página exacta de Mercado Libre no pudo recuperarse. El título por sí solo no permite afirmar secado, molienda, fermentación ni biología.

Se registra como observación válida de oferta, pero no se usa todavía para claims técnicos.

### ML-0149 — Fryline 4 L

```text
Producto: Compostador Eléctrico Fryline 4L Para Cocina Y Fertilizantes
Arquitectura: A5
Marca: FRYLINE
Precio indexado ML: ARS 1.101.000
Ventas visibles del ítem: no informadas
Canal: importación desde EE.UU.
```

Una publicación indexada de la misma familia/modelo FR describe:

```text
high-temperature drying
+ grinding
+ cooling
→ reducción hasta 90 %
```

También declara filtro de carbón de aproximadamente 1000 horas.

La oferta de Mercado Libre advierte que el equipo importado trabaja a 110–120 V y requiere transformador para uso seguro en Argentina.

### ML-0150 — Growell EC04 3,2 L

```text
Arquitectura: A5
Marca: GROWELL
Modelo: EC04
Precio indexado ML: ARS 1.269.000
Ventas visibles del ítem: no informadas
Canal: importado
```

La documentación de Growell/retail del EC04 confirma:

```text
GRINDING
+ HIGH-TEMPERATURE DRYING
+ COOLING
→ PRE-COMPOST
```

con reducción declarada de hasta 90 %, ciclos de preprocesamiento de hasta 8 horas y filtro de carbón con aviso de reemplazo aproximadamente a las 300 horas.

### ML-0151 — Garthen TOG-2300

```text
Producto: Triturador Orgánico Eléctrico Garthen
Clasificación: ADJACENT — OUT OF CORE A5
Marca: GARTHEN / Grupo GMEG
Precio indexado: ARS 559.065
```

Mercado Libre describe el equipo como triturador de material vegetal:

- hojas;
- restos de frutas/hortalizas;
- cortezas;
- podas;
- ramas.

Es 220 V, 1800 W y pesa aproximadamente 27 kg.

Su job es:

```text
TRITURAR MATERIAL VEGETAL
→ REDUCIR VOLUMEN / PREPARAR PARA COMPOSTAJE POSTERIOR
```

No es un procesador countertop de residuos de cocina A5 y **no cuenta como evidencia de demanda del core**.

## 14. Lectura parcial de A5

La arquitectura A5 está claramente presente en Mercado Libre Argentina, pero la muestra observada comparte tres características:

```text
OFERTA PRESENTE
→ SÍ

STOCK / PRODUCCIÓN LOCAL
→ NO DEMOSTRADO

CANAL DOMINANTE OBSERVADO
→ IMPORTACIÓN

TICKET OBSERVADO
→ MUY ALTO

VENTAS DEL ÍTEM VISIBLES
→ NO DEMOSTRADAS
```

La evidencia actual sostiene una **señal de demanda débil**, no porque la arquitectura sea inexistente, sino porque la oferta visible es de importación, cara y sin tracción transaccional atribuible.

Además, los equipos NutriChef, Fryline y Growell muestran que el naming comercial `compostador eléctrico` agrupa principalmente procesos de secado/trituración/enfriamiento.

La clasificación correcta permanece:

```text
A5 = PREPROCESSOR / FOOD RECYCLER

NO asumir:
A5 = FINISHED COMPOST
```

## 15. Materialización batch 3

Archivo preparado:

```text
matrix-aut78-brand-cand-005-phase3-batch3.xlsx
SHA-256: bf17feb84a88cbf24579d0cabe2646a0cace6e8dc7e63c278d3bd5f9c2b3d1c8
```

IDs incorporados:

```text
Publicaciones ML: ML-0147 .. ML-0151
Fuentes: SRC-0454 .. SRC-0459
Evidencia parcial: EVID-0271
Evidencia Fuentes: EVSRC-0571 .. EVSRC-0576
```

`ML-0151` es adyacente y no suma al core A5.

`EVAL-0023 — Demanda` todavía **no se crea**.


## 15.1 Corrección estructural de aut78

La primera exportación de `aut78` fue rechazada por el Matrix Validator con 2 errores de vocabulario controlado:

```text
EVSRC-0572.Rol = COMPLEMENTARIA
EVSRC-0575.Rol = COMPLEMENTARIA
```

El schema `full-matrix-v5 0.7.0` permite únicamente:

```text
Evidencia Fuentes.Rol = PRINCIPAL
```

La corrección no modifica la interpretación metodológica de esas fuentes. `EVSRC-0572` sigue documentado como evidencia con mecanismo pendiente de PDF y `EVSRC-0575` sigue documentado como publicación adyacente fuera del core A5; únicamente se ajusta el valor técnico del campo `Rol` al vocabulario permitido por el schema.

Archivo corregido:

```text
matrix-aut78-brand-cand-005-phase3-batch3-corrected.xlsx
SHA-256: 631d258916e3a70aa52b765315e5597856a909fa1be4f5362b451472b6653f88
```

## 16. Estado vigente de F3

```text
BATCH 1 — A1/A2/A3
→ VALIDATED — aut76 corrected PASS

BATCH 2 — A4
→ VALIDATED — aut77 PASS

BATCH 3 — A5
→ MATRIX MATERIALIZED — aut78 corrected
→ MATRIX VALIDATOR PENDING

A6
→ PENDING

DEMAND SCORE
→ NOT CREATED

F3
→ NOT CLOSED
```

Próxima cobertura:

```text
A6 — procesador eléctrico biológico / in-vessel
```

ML-0148 sólo requiere PDF si la evidencia de A6 no permite cerrar F3 sin resolver esa ambigüedad.


## 17. A6 — procesador eléctrico biológico / in-vessel

Se ejecutó la búsqueda colaborativa específica para A6 con términos orientados a:

```text
compostera biologica electrica
compostera microbiana
compostera automatica biologica
compostador con microorganismos
compostera inteligente cocina
smart composter
reencle
food waste composter microorganismos
```

Resultado reportado por Alejandro:

> las búsquedas devolvieron los mismos productos que ya aparecían bajo `compostera eléctrica`; no apareció una publicación nueva claramente diferenciable.

La interpretación metodológica es:

```text
A6 — OFERTA DIFERENCIADA OBSERVADA EN ML ARGENTINA
→ NO

A6 — DEMANDA LOCAL
→ NO DEMOSTRADA

A6 — MERCADO INEXISTENTE
→ NO CONCLUIR
```

No se reclasifica un equipo A5 como A6 por naming comercial.

Para considerar una publicación como A6 se requiere evidencia suficiente de:

```text
MICROORGANISMOS / MEDIO BIOLÓGICO
+ AIREACIÓN / AGITACIÓN
+ CONTROL DE CONDICIONES
→ DEGRADACIÓN BIOLÓGICA ACTIVA
```

Las búsquedas abiertas no produjeron una cohorte local diferenciada con esa evidencia.

Se materializa:

```text
EVID-0272
Señal: Débil
Confianza: Media
```

## 18. Evaluación consolidada de demanda

La evidencia completa de F3 muestra una estructura muy desigual por arquitectura:

```text
A1 — aeróbico pasivo / modular
→ demanda observable

A2 — tumbler
→ señal fuerte; caso con +1000 vendidos

A3 — vermicompostaje
→ demanda observable; caso modular con +500 vendidos

A4 — Bokashi
→ oferta muy escasa / importada
→ sin tracción local fuerte demostrada

A5 — food recycler térmico
→ oferta visible
→ principalmente importación
→ ticket muy alto
→ sin ventas del ítem visibles

A6 — biológico in-vessel
→ sin cohorte local diferenciada observada
```

Conclusión de demanda:

```text
DEMAND SIGNAL: MODERATE / HETEROGENEOUS
CONFIDENCE: MEDIUM
MINIMUM SUFFICIENT EVIDENCE: REACHED
```

La demanda existe de forma clara para el problema doméstico de residuos orgánicos, pero está concentrada en soluciones convencionales y relativamente simples.

Las arquitecturas más complejas no muestran una validación local equivalente.

## 19. Evaluación del candidato

Se materializa:

```text
EVAL-0023
Criterio: Demanda
Score: 3 / 5
Confianza: Media
Evidencia: EVID-0273
```

Interpretación:

> La demanda local de BRAND-CAND-005 es moderada y heterogénea. A1–A3 aportan evidencia suficiente de demanda real, con señales transaccionales fuertes en algunos productos. A4–A6 presentan oferta escasa, importación de ticket alto o ausencia de una cohorte diferenciada. La evidencia alcanza para continuar a competencia, pero no justifica una lectura de demanda alta para todo el candidato.

El `3/5` no significa:

- que el mercado total haya sido cuantificado;
- que A4–A6 carezcan de demanda;
- que la baja competencia aparente sea una oportunidad;
- que una arquitectura haya sido seleccionada;
- que exista Product Base;
- que origen, landed cost o margen estén validados.

## 20. Gate F3

Pregunta:

> ¿Existe demanda local observable y suficientemente defendible como para justificar continuar a F4 — Competition?

Resultado conceptual:

```text
PASS
```

Razón:

- existe señal transaccional real en A1–A3;
- A2 aporta una señal especialmente fuerte;
- la diversidad de arquitecturas observadas confirma que el job doméstico existe;
- A4–A6 fueron suficientemente exploradas para evitar confundir ausencia de listings con demanda nula;
- ampliar la búsqueda en F3 ya presenta rendimientos decrecientes;
- la siguiente incertidumbre material es **competencia**, no demanda.

## 21. Materialización final de F3

Baseline validada:

```text
matrix-aut78-brand-cand-005-phase3-batch3-corrected.xlsx
SHA-256: 631d258916e3a70aa52b765315e5597856a909fa1be4f5362b451472b6653f88
Result: PASS
```

F3 final agrega:

```text
Fuentes
→ SRC-0460 .. SRC-0461

Evidencias
→ EVID-0272 — A6 / sin oferta diferenciada observada
→ EVID-0273 — Demanda consolidada

Evidencia Fuentes
→ EVSRC-0577 .. EVSRC-0582

Evaluaciones
→ EVAL-0023 — Demanda = 3/5 — confianza Media
```

`Nichos` ID 35 queda con:

```text
Demanda: 3
Confianza Demanda: Media
Criterios evaluados: 1/10
Score parcial: 3
Confianza promedio: Media
```

Archivo preparado:

```text
matrix-aut79-brand-cand-005-phase3.xlsx
SHA-256: eee0ef6df614395888176e5de0acd654139caf7e612d48867768cead6e6f11e5
```

## 22. Estado formal de F3

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut79
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F3 CLOSED
```

F4 queda formalmente abierta sobre `aut79 PASS`.


Validación oficial:

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: eee0ef6df614395888176e5de0acd654139caf7e612d48867768cead6e6f11e5
Report: aut79-brand-cand-005-phase3-validation-report.json
```

F4 — Competition queda formalmente abierta después de este cierre.


## 23. Próxima acción

Validar `aut79`.

Resultado ejecutado:

```text
F3 CLOSED — aut79 PASS
→ F4 — Competition
→ AUTO
```

F4 podrá reutilizar `ML-0140..ML-0151`, separando:

```text
CORE COMPETITOR
vs
ADJACENT PRODUCT
vs
ARCHITECTURE VARIANT
vs
DUPLICATE / SAME PRODUCT FAMILY
```

y sin crear Product Bases antes de F6.
