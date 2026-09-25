---
id: si-research-032
title: BRAND-CAND-004 — Method v2 Agile — F4 Competition
description: Evaluación de presión competitiva por boundary, arquitectura, actor, precio y service layer para monitoreo doméstico del consumo energético.
version: 0.1.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-25
updated: 2026-09-25
tags:
  - smart-imports
  - method-v2
  - brand-hogar
  - brand-cand-004
  - energy-monitoring
  - phase-4
  - competition
related:
  - si-research-028
  - si-research-029
  - si-research-030
  - si-research-031
phase: business-intelligence
---

# BRAND-CAND-004 — Method v2 Agile — F4 Competition

Fecha: 2026-09-25  
Estado: `CLOSED`

## 1. Input vigente

F3 quedó formalmente cerrada sobre:

```text
matrix-aut62-brand-cand-004-phase3.xlsx
SHA-256: 2975a20df2c0f76f6e1e10ffeb9c4e1176137d5bac91030e1796b7cfb4ee8854
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
```

Muestra reutilizada:

```text
20 publicaciones Mercado Libre
ML-0120 … ML-0139
```

F4 **no vuelve a recolectar demanda**. Reinterpreta las mismas publicaciones como evidencia competitiva.

## 2. Reglas metodológicas

```text
COMPETITION ≠ COUNT OF LISTINGS

LOW COMPETITION ≠ HIGH OPPORTUNITY

PRICE DISPERSION ≠ QUALITY LADDER

QUERY COHORT ≠ REAL COMPETITIVE SEGMENT

SMART / WIFI / APP ≠ MEASUREMENT QUALITY

HYBRID SALES ≠ PURE MONITORING COMPETITION

HIGH SELLER STRENGTH
≠
TECHNICAL DIFFERENTIATION
```

La competencia se evalúa combinando:

```text
saturación observable
+ fuerza del vendedor
+ presión de precio
+ repetición / equivalencia de hardware
+ diferenciación técnica visible
+ service layer
+ complejidad / claims / seguridad
```

## 3. D1 — Plug-level direct meter — standalone

Precio observado:

```text
mínimo   ARS 64,590
mediana  ARS 69,998
máximo   ARS 212,429
```

Lectura competitiva:

```text
COMPETITION: MEDIUM
```

La oferta combina dos publicaciones muy cercanas del mismo vendedor con importadores que amplían el rango de precio. El hardware base —display local, medición V/A/W/kWh, cálculo de costo— es simple y replicable.

La diferenciación visible aparece principalmente en:

- 10A vs 16A;
- memoria ante cortes/desconexión;
- legibilidad de pantalla;
- formato físico/enchufe;
- compatibilidad real con 220–240V / 50Hz;
- documentación y confiabilidad de especificaciones.

Problema competitivo:

> La dispersión de precio es grande, pero no demuestra una escalera de calidad equivalente.

## 4. D2 — Smart plug + energy monitoring

Precio observado:

```text
mínimo   ARS 21,999
mediana  ARS 31,069
máximo   ARS 48,285
```

Lectura competitiva:

```text
COMPETITION: HIGH / VERY HIGH
```

El segmento tiene:

- múltiples marcas;
- vendedores MercadoLíder / tiendas oficiales;
- señales de +100, +500, +1000 y +10000 ventas;
- fuerte cercanía de precios;
- ecosistema Tuya / Smart Life repetido;
- control remoto, timers, asistentes de voz y medición como bundle común.

La capa `smart` es fácilmente replicable. Wi-Fi, Tuya o Alexa no constituyen una barrera por sí mismos.

Diferenciación potencial:

- medición realmente documentada;
- 16A/20A y potencia soportada real;
- plug argentino / seguridad eléctrica;
- certificación visible;
- histórico y persistencia de datos;
- comportamiento sin Internet;
- privacidad / dependencia de cloud;
- soporte y onboarding en español.

## 5. D3 — Installed / DIN-rail direct meter

Precio observado:

```text
mínimo   ARS 26,344
mediana  ARS 44,204
máximo   ARS 69,000
```

Lectura competitiva:

```text
COMPETITION: HIGH / VERY HIGH
```

D3 es el segmento con mejor combinación de demanda atribuible y presión competitiva.

Se observan:

- medidores directos 45A/80A;
- V/A/W/kWh;
- variantes con memoria;
- salida de pulsos;
- productos con IRAM declarado;
- híbridos de protección + monitoring + Wi-Fi;
- varios SKU con +500/+1000 ventas;
- vendedores fuertes y tickets cercanos.

El hardware de medición básica está comoditizado. La defensa no puede descansar en “mide consumo”.

Diferenciación defendible:

```text
accuracy / test evidence
+ safety / certification
+ installation clarity
+ local electrical compatibility
+ data persistence
+ support
+ installer-oriented documentation
```

Los híbridos de protección agregan valor, pero también elevan la carga de seguridad, claims y postventa.

## 6. D4 — CT whole-home / multi-circuit

Precio observado:

```text
mínimo   ARS 39,999
mediana  ARS 236,499
máximo   ARS 1,297,998
```

Lectura competitiva:

```text
COMPETITION: LOW / MEDIUM — SPECIALIZED
```

La oferta es mucho menos densa y más heterogénea:

- split-CT standalone;
- Wi-Fi;
- Zigbee;
- uno a tres circuitos;
- whole-home bidireccional;
- sistemas de 10–20 circuitos;
- Home Assistant;
- solar / exportación a red.

Pero:

```text
LOW VISIBLE SATURATION
+
LOWER VISIBLE DEMAND
+
HIGHER INSTALLATION / SERVICE BURDEN
≠
AUTOMATIC OPPORTUNITY
```

Los tickets son muy dispersos y varios productos son importados bajo demanda.

## 7. Lectura transversal

### 7.1 Los segmentos con mejor demanda también son los más competidos

```text
D2 → high demand signal / high competition
D3 → strongest attributable demand / high competition
```

Por lo tanto, la tesis no puede depender de “encontrar poca oferta”.

### 7.2 D1 es accesible pero poco defendible como hardware puro

El producto standalone es fácil de explicar, pero también de copiar. El valor de marca tendría que venir de selección, compatibilidad, precisión defendible, documentación y soporte.

### 7.3 D4 tiene espacio técnico, no necesariamente espacio comercial

La menor densidad de listings coincide con mayor complejidad y menor señal transaccional.

### 7.4 La frontera competitiva puede desplazarse hacia confianza técnica

En este candidato, una marca puede diferenciarse menos por “tener Wi-Fi” y más por:

```text
qué mide
con qué accuracy declarada y demostrable
dónde se instala
qué carga/fase soporta
qué pasa ante corte de energía/internet
cómo conserva datos
qué certificaciones/documentación existen
cómo se instala y se interpreta
qué soporte local recibe el usuario
```

## 8. Evaluación consolidada

Se materializa:

```text
EVAL-0021
Criterio: Competencia
Score: 2 / 5
Confianza: Media
Evidencia: EVID-0260
```

Interpretación:

> La competencia es alta precisamente en D2 y D3, los espacios con mayor evidencia de demanda. D1 mantiene presión intermedia y poca barrera de hardware; D4 es menos saturado pero también menos validado y más complejo. El candidato conserva posibilidades de diferenciación por credibilidad técnica, seguridad, compatibilidad local, datos y soporte, pero no presenta un vacío competitivo simple.

El score `2/5` representa **presión competitiva desfavorable**, no falta de mercado.

## 9. Gate F4

Pregunta:

> ¿La presión competitiva deja espacio suficiente para continuar a F5 — Potencial de Marca sin depender de una falsa lectura de “poca oferta”?

Resultado conceptual:

```text
PASS
```

Razón:

- existe presión real y elevada en D2/D3;
- la competencia no elimina la posibilidad de una propuesta defendible;
- ya se identificaron palancas no triviales de diferenciación;
- D4 queda correctamente interpretado como especializado, no como “blue ocean”;
- F5 puede evaluar si esas palancas son suficientemente coherentes para construir marca.

## 10. Materialización en matriz

Baseline validada:

```text
matrix-aut62-brand-cand-004-phase3.xlsx
SHA-256: 2975a20df2c0f76f6e1e10ffeb9c4e1176137d5bac91030e1796b7cfb4ee8854
Result: PASS
```

F4 agrega:

```text
Competencia ML
→ COMP-0120 … COMP-0139

Fuentes
→ SRC-0427 — análisis interno F4

Evidencias
→ EVID-0260

Evidencia Fuentes
→ EVSRC-0503 … EVSRC-0523

Evaluaciones
→ EVAL-0021 — Competencia = 2/5 — confianza Media
```

No se crean Product Bases en F4. Los campos `Producto Base` / `ID Producto Base` de las filas nuevas de `Competencia ML` permanecen vacíos hasta F6.

Archivo preparado:

```text
matrix-aut63-brand-cand-004-phase4-corrected.xlsx
SHA-256: dc0b9ab767297e58ec6723eba21262dfc3d27030c92ded864b4c64f54531933b
```

## 11. Estado formal de F4

```text
ANALYSIS COMPLETE
→ MATRIX MATERIALIZED — aut63 corrected
→ MATRIX VALIDATOR PASS
→ DOCUMENTARY CHECKPOINT COMPLETE
→ F4 CLOSED
```

Validación oficial:

```text
Matrix Validator 0.1.0
Schema: full-matrix-v5 0.7.0
Result: PASS
errors: 0
warnings: 0
info: 0
limitations: 0
SHA-256: dc0b9ab767297e58ec6723eba21262dfc3d27030c92ded864b4c64f54531933b
```

F5 queda formalmente abierta después de este cierre.

## 12. Próxima acción

F4 queda `CLOSED`. Ejecutar `F5 — Brand Potential` en modalidad `AUTO`.

## 13. Changelog

### 2026-09-25 — v0.1.0

- F3 queda formalmente cerrada sobre `aut62 PASS`;
- se reutilizan ML-0120..ML-0139 para competencia;
- se materializan COMP-0120..COMP-0139 sin crear Product Bases prematuramente;
- D1 se interpreta como competencia media;
- D2 y D3 como alta/muy alta;
- D4 como baja/media pero especializada;
- se materializa EVAL-0021 = 2/5, confianza Media;
- se prepara `matrix-aut63-brand-cand-004-phase4-corrected.xlsx`;
- corrección de aut63: se completan `Fuente Global ID` en `COMP-0120..COMP-0139` con `SRC-0406..SRC-0425`;
- `aut63 corrected` obtiene PASS limpio y F4 queda formalmente `CLOSED`;
- siguiente fase: `F5 — Brand Potential` en AUTO.
