# Rate limiting

## Estado actual
- Implementación en memoria por IP.
- Configurable por `JWT_ACCESS_TTL` (en minutos) y `max_requests`.
- Bloquea con `429` cuando se supera el límite.

## Próximo paso
- Reemplazar por Redis cuando haya múltiples workers/instancias.
- No requiere cambios en dominios ni rutas.
