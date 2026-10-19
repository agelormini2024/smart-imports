---
id: si-method-note-001
title: Smart Imports — Procedimiento operativo de materialización y validación de matrices Method v2
description: Continuidad del flujo de trabajo del Founder y del asistente; producción de XLSX completos, trazabilidad y checkpoints canónicos.
version: 0.1.0
status: ready_for_documentary_checkpoint
owner: Alejandro Gelormini
created: 2026-10-19
updated: 2026-10-19
scope: Smart Imports / Method v2
publication_status: PREPARED_FOR_F4_F13_CHECKPOINT
---

# Procedimiento operativo — materialización y validación de matrices

## 1. Objetivo y alcance

**Mantener sin cambios un método de trabajo ya adoptado por el proyecto**: el asistente prepara la matriz XLSX completa para cada avance y el Founder ejecuta únicamente la validación local y revisa las decisiones que requieren intervención. No se traslada al Founder la carga de importar CSV, copiar rangos o reconstruir referencias cruzadas en Google Sheets.

Esta nota complementa operativamente a `SI-BIM-PROC-003` y `SI-ROADMAP-002`; **no modifica sus gates, fases o requisitos**. Se propone incorporar/referenciar esta regla en el próximo checkpoint documental, previa revisión del Founder.

## 2. Roles y secuencia obligatoria

1. **Baseline.** Partir del último XLSX que obtuvo **Data Fidelity Preflight PASS + Matrix Validator PASS**. Registrar nombre y SHA-256; no editarlo ni sobrescribirlo.
2. **Preparación a cargo del asistente.** Analizar las fuentes y archivos entregados, comprobar información de producto/proveedor y normalizar datos en los rangos/columnas definidos por el esquema. Conservar el idioma español en el contenido funcional.
3. **Materialización a cargo del asistente.** Generar y entregar el nuevo XLSX completo (`autNNN`), no solamente importables CSV. Si se usan CSV intermedios, son insumos técnicos internos de la generación; **el usuario no debe pegarlos manualmente en hojas**.
4. **Auditoría de integridad previa a la entrega.** Comprobar que sólo se modificaron las hojas, filas y celdas autorizadas; no se perdieron fórmulas, hojas, registros históricos ni URLs originales; IDs nuevos son únicos y las referencias cruzadas son coherentes. Asegurar integridad del XLSX generado y SHA-256 final.
5. **Paquete entregable.** Incluir matriz XLSX completa, script `.sh` de validación, documentación/Research de la fase y, cuando corresponda, documentación metodológica. El paquete se descarga/descomprime en Desktop, como los anteriores. No se exige Excel ni edición manual con Numbers.
6. **Intervención mínima del Founder.** Ejecutar **un comando en Warp**, adjuntar el log resultante y decidir los gates `COLLABORATIVE` cuando corresponda. Ningún proceso debe ejecutar `git add`, `commit` ni `push` sin revisión específica.
7. **Doble PASS.** Cerrar técnicamente una fase sólo si el Data Fidelity Preflight y el Matrix Validator del Engine registran PASS, con cero errores y advertencias, y la trazabilidad queda conforme.
8. **Founder Review y documentación.** Los gates colaborativos exigen aprobación expresa. Preparar y publicar solamente documentación permitida en Git en el checkpoint establecido: no incluir XLSX privados, capturas PDF, respaldos, scripts de trabajo, logs ni datos sensibles.

## 3. Contingencia cuando falla la herramienta de planillas

Una importación o exportación fallida en el entorno del asistente **no cambia el procedimiento** ni constituye motivo para trasladar la carga al Founder. Debe intentarse la vía automática ya probada: una materialización de celdas acotada, con controles de integridad, o un script de construcción automático reproducible que entregue XLSX completo. Si no puede comprobarse la integridad, **no entregar un XLSX como válido**: informar el bloqueo y resolverlo antes de solicitar validación.

La auditoría estructural local es distinta del **doble PASS canónico**, que continúa ejecutándose con el Engine local del proyecto.

## 4. Trazabilidad mínima de cada snapshot

Registrar nombre y SHA-256 de baseline y resultado; fase y modo; rangos/hojas autorizados; IDs creados; URL original literal (con parámetros) para cada publicación; proveedor, fecha, precio público, MOQ y ambigüedades; archivos PDF privados y sus SHA-256; cadena `COT → SRC → EVID → EVSRC`; resultados de los dos validadores y estado de aprobación del Founder.

Las referencias públicas de Alibaba **no equivalen** a RFQs, precios FOB/EXW, certificaciones, muestras, homologación ni decisiones de compra.

## 5. Aplicación inmediata — BRAND-CAND-008 / F8

- Baseline `aut147` — SHA-256 `68e5b7797a05d33e289f1dd928507b434414673ef98c313e82a999ec318392d5` — F7 CLOSED.
- Materialización `aut148` — 3 referencias Alibaba, `COT-0070..0072`, `SRC-0541..0543`, `EVID-0327..0329`, `EVSRC-0743..0745`; Product Base `BASE-FIT-009`.
- Resultado local `aut148` — SHA-256 `786676c581f97a972f38688a7dc6e0a27371e535c4cf224360fed71afa45c2c4` — sólo auditoría estructural; pendiente doble PASS en Mac.
- F8 COLLABORATIVE — Founder Review pendiente. F9 NOT OPENED.

**Estado de esta nota:** propuesta documental para incorporar al repositorio en el siguiente checkpoint; no constituye commit ni actualización publicada de `SI-BIM-PROC-003`.

## 6. Continuidad de ejecución — F13 de BRAND-CAND-008

F8 y F12 fueron validadas después de las capturas históricas mencionadas en la sección 5; su estado anterior allí es una fotografía histórica, no el estado vigente. Para F13, la última baseline doble PASS es `aut152` y el nuevo snapshot es `aut153`, con doble PASS todavía pendiente. Se mantiene el mismo flujo: XLSX completo preparado por el asistente, un único script de validación en Warp, log adjunto por el Founder, checkpoint documental tras el cierre.

## 7. Confirmación y continuidad posterior a F13

El 19/10/2026, `BRAND-CAND-008` completó F0–F13 con validaciones canónicas en cada snapshot, incluyendo la reconciliación Tipo B de F6 y la aprobación expresa del Founder en F8. El último XLSX, `aut153`, obtuvo doble PASS (SHA-256 `4c88c0ac2e4d459f17707da38d8f4b72fb7cdaf0d157dc1d3e8b8c4505b10540`). Los estados preliminares de las secciones 5 y 6 son fotografías históricas previas a ese resultado. La operación estable es **matriz XLSX completa preparada por el asistente → validación local en Warp → revisión del log → checkpoint documental y control de Git**.
