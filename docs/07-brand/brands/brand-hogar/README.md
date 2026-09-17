---
id: brand-hogar
title: Marca Hogar
description: Primera instancia real del Brand System de Smart Imports.
version: 0.6.0
status: review
owner: Alejandro Gelormini
reviewer: CTO/CSO Virtual
created: 2026-09-16
updated: 2026-09-17
tags:
  - brand
  - home
  - portfolio
  - missions
  - brand-fit
related:
  - si-brand-001
  - si-brand-002
  - si-decision-016
---

# Marca Hogar

> **Un hogar que funciona mejor.**

## 1. Identidad de trabajo

```text
Brand ID: brand-hogar
Working name: Marca Hogar
Descriptor interno: Un hogar que funciona mejor.
```

`Marca Hogar` es un identificador interno, no un nombre comercial. El descriptor es una guía estratégica interna, no un slogan público.

## 2. Territorio

> **Marca Hogar desarrolla y selecciona soluciones que mejoran de forma tangible cómo funciona el hogar: sus condiciones ambientales, el uso de recursos y la gestión de residuos y problemas domésticos recurrentes.**

La marca se mantiene deliberadamente centrada en el hogar. Por ahora no se extiende a consumo responsable general fuera del hogar.

## 3. Misiones v0.1

### Misión 1 — Mejorar las condiciones del hogar

Incluye problemas vinculados con calidad del aire, humedad, determinados contaminantes, calidad del agua, olores y condiciones específicas de higiene ambiental.

No convierte a la marca en una marca genérica de wellness.

### Misión 2 — Usar mejor los recursos

Busca medir, reducir, optimizar o evitar desperdicio de agua, energía, consumibles domésticos u otros recursos relevantes.

### Misión 3 — Reducir y gestionar residuos

Busca mejorar cómo el hogar reduce, separa, trata, reaprovecha, contiene o gestiona residuos.

### Misión 4 — Resolver problemas domésticos recurrentes conectados con el núcleo

Adyacencia restrictiva. La solución debe resolver un problema recurrente, conectarse fuertemente con ambiente/recursos/residuos/higiene, producir una mejora central y tangible y no expandir arbitrariamente el territorio.

## 4. Núcleo

```text
CONDICIONES DEL HOGAR
RECURSOS
RESIDUOS
```

## 5. Adyacencias

Sólo se aceptan cuando están conectadas con el núcleo.

`higiene doméstica especializada` puede ser adyacente; `limpieza general` no habilita automáticamente toda la categoría de electrodomésticos.

## 6. Exclusiones iniciales

- seguridad personal o patrimonial;
- entretenimiento;
- decoración;
- wellness personal genérico;
- automatización por mera conveniencia;
- Pet Care genérico;
- Smart Home genérico;
- consumo responsable general fuera del hogar.

Una exclusión de Brand Fit no implica una mala oportunidad comercial.

## 7. Pruebas de frontera

| Producto | Lectura | Razón |
|---|---|---|
| Detector de fugas + corte | Natural | Agua, desperdicio y prevención. |
| Tratamiento doméstico de agua | Natural | Condición central del hogar. |
| Purificador de aire | Natural | Condición ambiental central. |
| Compostera | Natural | Gestión de residuos. |
| Monitor energético | Natural | Uso de energía. |
| `BASE-PET-003` | Adyacente defendible | Higiene + residuo + problema recurrente. |
| GPS para mascotas | Fuera | Ubicación/seguridad del animal. |
| Cámara Wi-Fi | Fuera | Seguridad patrimonial. |
| Robot aspirador | Borde | Riesgo de abrir cleaning appliances genéricos. |
| Botella reutilizable | Fuera por foco actual | Consumo responsable fuera del sistema hogar. |

## 8. Arquitectura de portfolio

El portfolio se organiza por misiones y problemas, no por categorías comerciales.

| Producto | Categoría comercial | Misión |
|---|---|---|
| Detector de fugas | Smart Home | Usar mejor los recursos |
| Tratamiento de agua | Water Treatment | Mejorar condiciones del hogar |
| Purificador de aire | Calidad ambiental | Mejorar condiciones del hogar |
| Compostera | Gestión de residuos | Reducir y gestionar residuos |
| `BASE-PET-003` | Pet Care | Problemas domésticos recurrentes |

## 9. Candidate Register

| ID | Candidate | Mission | Territory Relationship | Status | Brand Relevance | Brand Credibility |
|---|---|---|---|---|---|---|
| [`BRAND-CAND-001`](./candidates/brand-cand-001-water-leak-detection-and-shutoff.md) | Detección de fugas + corte automático | Usar mejor los recursos | `CORE` | `PASS TO METHOD V2` | HIGH | PENDING BY PRODUCT BASE |
| [`BRAND-CAND-002`](./candidates/brand-cand-002-domestic-water-treatment.md) | Tratamiento doméstico de agua | Mejorar condiciones del hogar | `CORE` | `PASS TO METHOD V2` | HIGH | PENDING BY PRODUCT BASE / CLAIM |
| [`BRAND-CAND-003`](./candidates/brand-cand-003-domestic-air-treatment.md) | Tratamiento doméstico del aire interior | Mejorar condiciones del hogar | `CORE` | `PASS TO METHOD V2` | HIGH | PENDING BY PRODUCT BASE / CLAIM / TEST METHOD |
| [`BRAND-CAND-004`](./candidates/brand-cand-004-domestic-energy-monitoring.md) | Monitoreo doméstico del consumo energético | Usar mejor los recursos | `CORE` | `PASS TO METHOD V2` | HIGH | PENDING BY PRODUCT BASE / MEASUREMENT ACCURACY / ACTIONABILITY / CLAIM |
| [`BRAND-CAND-005`](./candidates/brand-cand-005-organic-waste-processing.md) | Compostaje / procesamiento de residuos orgánicos | Reducir y gestionar residuos | `CORE` | `PASS TO METHOD V2` | HIGH | PENDING BY PRODUCT BASE / PROCESS / OUTPUT / CLAIM |
| [`BRAND-CAND-006`](./candidates/brand-cand-006-pet-003-retrospective-screening.md) | PET-003 — gestión automatizada de residuos sanitarios de mascotas | Resolver problemas domésticos recurrentes conectados con el núcleo | `STRONG ADJACENCY` | `BRAND FIT CONFIRMED` | HIGH | PENDING BY PRODUCT BASE / SAFETY / ODOR-HYGIENE CLAIM / USER EXPERIENCE |

`BRAND-CAND-006` ya cuenta con investigación previa en Method v2. Su screening será retrospectivo y no reinicia su evaluación comercial.

## 10. Próximo candidato

```text
Aplicar Brand System v0.3 a nuevas oportunidades reales cuando aparezcan; no crear candidatos sólo para probar el método
```

Objetivo: mantener Brand System v0.3 en observación empírica y revisar futuras excepciones sólo cuando aparezcan oportunidades reales.

## 11. Documentos relacionados

- [SI-BRAND-001](../../si-brand-001-reusable-brand-system.md)
- [SI-BRAND-002](../../si-brand-002-brand-candidate-screening-method.md)
- [Candidates](./candidates/README.md)

## 12. Changelog

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-09-17 | Primera instancia formal de Marca Hogar con territorio, misiones, límites y Candidate Register. |
| [`BRAND-CAND-003`](./candidates/brand-cand-003-domestic-air-treatment.md) | Tratamiento doméstico del aire interior | Mejorar condiciones del hogar | `CORE` | `PASS TO METHOD V2` | HIGH | PENDING BY PRODUCT BASE / CLAIM / TEST METHOD |
| [`BRAND-CAND-004`](./candidates/brand-cand-004-domestic-energy-monitoring.md) | Monitoreo doméstico del consumo energético | Usar mejor los recursos | `CORE` | `PASS TO METHOD V2` | HIGH | PENDING BY PRODUCT BASE / MEASUREMENT ACCURACY / ACTIONABILITY / CLAIM |
| [`BRAND-CAND-005`](./candidates/brand-cand-005-organic-waste-processing.md) | Compostaje / procesamiento de residuos orgánicos | Reducir y gestionar residuos | `CORE` | `PASS TO METHOD V2` | HIGH | PENDING BY PRODUCT BASE / PROCESS / OUTPUT / CLAIM |
| [`BRAND-CAND-006`](./candidates/brand-cand-006-pet-003-retrospective-screening.md) | PET-003 — gestión automatizada de residuos sanitarios de mascotas | Resolver problemas domésticos recurrentes conectados con el núcleo | `STRONG ADJACENCY` | `BRAND FIT CONFIRMED` | HIGH | PENDING BY PRODUCT BASE / SAFETY / ODOR-HYGIENE CLAIM / USER EXPERIENCE |

| 0.6.0 | 2026-09-17 | Se consolida Brand System v0.3: candidatos 001–005 = CORE; candidato 006 = STRONG ADJACENCY. |