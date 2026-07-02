---
name: observability-engineer
description: >
  Skill para logs, métricas, traces y alertas en runtime.
  No modificar reglas de negocio; solo datos de operación.
trigger: "logs, métricas, traces, alertas, observabilidad, request_id"
scope: observabilidad
---

# observability-engineer

## Cuándo activarla
- Agregar métrica
- Cambiar formato de logs
- Activar traces
- Alta de alerta

## Pasos obligatorios
1. Leer `backend/core/logging.py` y `backend/core/tracing.py`.
2. Leer `.agents/config/observability.yaml`.
3. Garantizar `request_id` en respuesta.
4. Documentar en `docs/09-operaciones/`.

## Reglas duras
- Sin secrets en logs.
- Redactar payloads sensibles.
- Mantener latencia de logging baja.

## Criterio de done
- Logs estructurados en staging
- Métrica/métrica expuesta o documentada
