# World State (Memoria Continua del Agente)

## Hitos
1. Proyecto nuevo separado y con stack definido.
2. Backend base con compra, sorteo, validación QR y tests backend.
3. Frontend base con flujo mínimo de compra y validación.
4. CI mejorada con cache y health-check real.
5. Configuración empresarial fusionada desde Codere, Bot_ia, the-architect.

## Fase Actual
Mejora continua sin cambiar stack:
- Cache de validaciones de QR.
- Observabilidad mínima: logs estructurados + métricas.
- Política de reintentos para impresión local.
- Respaldo evidencia de tickets/QR por sorteo.

## Puntos Ciegos Mitigados
- Documentación escluida y versionada.
- Tests backend incluidos.
- Decisiones técnicas en `.agents/decisions`.

## Próximos Pasos
- Confirmar formato final del QR y stock/cartones.
- Confirmar impresoras/servicio local por puesto.
- Confirmar hosting y esquema de despliegue en infra Codere.
