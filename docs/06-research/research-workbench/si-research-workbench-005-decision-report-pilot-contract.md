---
id: si-research-workbench-005
title: Research Workbench — Contrato funcional piloto de Decision Report
version: 0.1.0
status: draft
owner: Founder
reviewer: CTO/CSO Virtual
created: 2026-10-30
updated: 2026-10-30
tags: [research-workbench, decision-reporter, comercial, method-v2, pilot-001]
related: [si-research-workbench-002, si-research-workbench-003, si-research-workbench-004, si-research-workbench-006]
---
# SI-RESEARCH-WORKBENCH-005 — Decision Report: contrato funcional piloto

> **Alcance:** registrar el formato y la lógica de los *Decision Reports* elaborados manualmente en RW-P001/CP03. Es un **contrato funcional en experimentación**, no un generador implementado ni un mecanismo certificado. No modifica Method v2 ni sus cierres. Documento público: no incluir cotizaciones privadas, PDFs comerciales originales, comunicaciones, objetivos de negociación ni simulaciones comerciales específicas.

## 1. Decisión de producto: qué debe entregar el Workbench

La salida principal del piloto no es una matriz por sí misma: es una **Ficha de Oportunidad Comercial / Decision Report por producto**, en español llano, comprensible para el Founder, el socio y posteriormente el despachante. La matriz y el registro de evidencias son soporte interno; no deben mantenerse manualmente en paralelo con cifras contradictorias.

**Dos niveles de madurez del mismo expediente**: (a) **preliminar para socio**: decide si el producto merece revisión externa; (b) **listo para consulta al despachante**: contiene especificaciones suficientes, riesgos y preguntas aduaneras concretas, pero no equivale a autorización de importación. Las secciones sin información se marcan **NO CALCULABLE / PENDIENTE / NO VERIFICADO**, nunca se completan con ceros ficticios.

## 2. Estructura de la ficha propuesta (orden de lectura)

| Bloque | Pregunta que debe responder | Contenido mínimo |
|---|---|---|
| Portada y decisión ejecutiva | ¿Qué proponemos hacer? | ID, producto/variante, fotografía referencial identificada como tal, destinatario, estado, una conclusión, confianza y siguiente gate |
| Problema y solución | ¿Para quién y para qué sirve? | Necesidad del atleta, situación de uso, atributos críticos y alcance de la solución |
| Mercado argentino | ¿Hay señales de compra y a qué precio? | Publicaciones comparables, precio y fecha, diferencias, ventas visibles *acumuladas*, evidencia y límites |
| Origen y alternativas | ¿Cuáles son las opciones? | Proveedores y variantes, MOQ, precio de pantalla vs respuesta comercial, incompatibilidades, faltantes |
| Economía: presupuesto máximo | ¿Cuánto puede costarnos puesto en Argentina? | Precio bruto de referencia/hipótesis, costo de canal, gastos comerciales, margen objetivo sobre ingreso neto, costo puesto máximo |
| Economía: Headroom | ¿Cuánto espacio queda para importar? | Costo de origen, presupuesto máximo, holgura absoluta y cociente; interpretación no equivalente a ganancia |
| Economía: sensibilidad | ¿Qué pasa si importar es más caro? | Escenarios declarados, costo puesto supuesto, contribución, margen neto, ROI económico; supuestos visibles |
| Caja y restricciones | ¿Cuánto capital requeriría? | Mercadería, desembolso total si se conoce, IVA/percepciones recuperables vs caja, logística/garantía, MOQ y capital de trabajo |
| Riesgos y decisiones | ¿Qué puede cambiar nuestra recomendación? | Riesgos técnicos/comerciales/regulatorios, evidencia, mitigación proporcional, recomendación y condiciones de reapertura |
| Preguntas por actor | ¿Quién debe resolver qué? | Founder/socio, despachante y proveedor posterior al gate |
| Fuentes y control | ¿Podemos reconstruir la conclusión? | IDs, enlaces originales (según política pública), fecha, tipo de fuente, versión, responsable, incertidumbres y trazabilidad hacia datos privados |

La lectura ejecutiva debe poder completarse sin entender fórmulas. La parte económica tiene que presentar un ejemplo con **unidades y significado de cada número**, no solo una tabla de multiplicadores.

## 3. Modelo económico heredado y explicado (Method v2; no fases obligatorias)

### 3.1 Presupuesto máximo que preserva el margen objetivo

Convención de **baseline didáctica histórica v2**, sujeto a adaptación por canal/producto: canal = **25 % del precio bruto**, costo comercial adicional = **5 % del bruto**, margen objetivo = **25 % del ingreso neto después del canal**. Estos porcentajes son **hipótesis de screening**, no comisiones ni tributos contractuales observados.

Sea `P` el precio bruto expresado en una misma moneda, `c` la proporción del canal, `g` la de gastos comerciales sobre el bruto y `m` el margen objetivo sobre ingreso neto:

- `ingreso_neto = P × (1 - c)`
- `margen_objetivo_monetario = ingreso_neto × m`
- `costo_puesto_maximo = ingreso_neto - P × g - margen_objetivo_monetario`
- `headroom = costo_puesto_maximo / costo_origen` (solo si `costo_origen > 0`)
- `holgura_absoluta = costo_puesto_maximo - costo_origen`

Por cada **USD 100 brutos**, la baseline permite **USD 51,25 de costo económico puesto máximo**, después de reservar costo del canal, costo comercial y margen objetivo. **Headroom no mide margen**, sino cuánto podría crecer el costo de origen antes de consumir ese presupuesto.

### 3.2 Estimaciones de costo puesto y resultado

- `costo_economico_puesto = costo_origen + flete + seguro + carga_aduanera_economica + gastos_locales`, con criterios contables/tributarios explicitados y sin duplicar costos.
- Solo para **prueba de sensibilidad** se admite `costo_puesto_hipotetico = costo_origen × factor`, con cada factor identificado como heredado/hypotético, **no calibrado** y no equivalente a presupuesto del despachante.
- `contribucion_unitaria = ingreso_neto - P × g - costo_puesto`; otras provisiones variables se incorporan explícitamente donde correspondan, evitando doble cómputo.
- `margen_neto_pct = contribucion_unitaria / ingreso_neto`.
- `ROI_economico = contribucion_unitaria / costo_puesto` (denominador económico **no** es desembolso total ni retorno integral del negocio).
- `precio_bruto_equilibrio_objetivo = costo_puesto / ((1-c)×(1-m)-g)` si el denominador es positivo.
- `caja_total` se calcula **separadamente** y considera tributos anticipados, percepciones, stocks, repuestos, contingencias y demás conceptos que consumen efectivo aun cuando algunos sean recuperables.

**Regla de integridad:** cada precio tiene moneda, fecha, canal, condición, MOQ, variante y procedencia. El escenario **conservador plausible** no es el peor escenario imaginable; debe justificar valores y mostrar sensibilidad. Datos ausentes ⇒ **NO CALCULABLE**, nunca cero como sustituto silencioso.

## 4. Clasificación de evidencia y gates

- **Observado:** captura de publicación fechada, no compra confirmada. Contadores de Mercado Libre pueden ser acumulados y no equivalen a ventas mensuales.
- **Declarado:** mensaje del proveedor o ficha de Alibaba; acredita que la afirmación fue hecha, no la prestación técnica.
- **Corroborado parcialmente:** páginas de ensayo parciales con modelo/resultado, sin informe completo ni vínculo verificado al lote futuro.
- **Hipótesis:** precio objetivo de venta, tipo de cambio de referencia, factores de importación y provisiones de costo; versiones fechadas, sensibles a cambios.
- **Decisión humana:** mantener, relegar, investigar o preparar para revisión profesional; no implica homologación ni compra.

**Secuencia aprobada**: screening de Workbench → revisión del socio/Founder → **visto bueno del despachante** (clasificación, intervenciones, restricciones y estimación de importación) → **recién entonces investigación profunda con proveedores** (muestras, homologación, ensayos completos, negociaciones, visitas/QA) → selección de 3–4 productos para primera importación si la economía y el portfolio lo respaldan.

Las consultas exploratorias realizadas antes del despachante no autorizan una fase de negociación profunda. El despachante filtra y estima; la decisión comercial permanece en Founder y socio.

## 5. Arquitectura funcional mínima y lecciones para v3

- Una sola fuente estructurada para producto, variante, publicación, proveedor, **identidad potencial de fabricante**, cotización, evidencia técnica, mercado, escenario, resultado y recomendación. Todos con IDs y fechas.
- Ficha derivada de esa fuente; no copiar números manualmente a documentos desconectados. La matriz histórica `aut171` es **antecedente metodológico**, no matriz que debamos sobrescribir ni copiar con sus 29 hojas.
- Los cambios de hipótesis producen **nueva versión de escenario y reporte**, sin reescribir precios/decisiones históricos.
- Validador proporcional al riesgo: consistencia de moneda, unidades, trazabilidad, configuración equivalente, ausencia de datos, porcentajes base, fórmula y protección de evidencia privada.
- Registrar esfuerzo activo y fricciones, cuando exista medición: búsqueda de equivalentes, discrepancias publicitarias, correspondencia modelo-ensayo, búsqueda de fabricantes, recolección, edición, revisiones y cálculo. **No inventar tiempos**.
- Documentos funcionales/negocio en español; código, convenciones técnicas y metadata según normas de repositorio.

## 6. Estado y límites del piloto

En RW-P001 se produjeron **tres informes provisionales** C01, C03 y C08. El formato todavía requiere iteración con el Founder y Eduardo: legibilidad de sensibilidad, comparables de mercado, coherencia del precio propuesto, consistencia de variantes y costo puesto realmente plausible. La automatización del Decision Reporter **no está implementada ni validada**. No hay candidatos homologados ni autorizados para importar.

Los reportes PDF/DOCX, cotizaciones privadas y hojas de simulación están bajo custodia privada, identificados en `SI-RESEARCH-WORKBENCH-006`. **Este contrato piloto no publica sus cifras negociadas.**

## 7. Próximo punto de validación

Usar los tres informes con el socio; registrar qué preguntas generan, qué se entiende sin explicación, qué errores revelan y cuánto trabajo implicó crear/actualizar cada ficha. Refinar el formato después, y solo entonces congelar una plantilla de aceptación preliminar para el futuro generador v3.

## Changelog

- **2026-10-30 · v0.1.0 DRAFT** — Contrato funcional reconstruido a partir de Method v2, guía económica didáctica v0.4 y pilotos C01/C03/C08; no implica implementación ni aprobación de compra.
