# Roadmap

## C1 — Validar idea
- Definir formato QR y regla de unicidad.
- Definir impresión local: impresora, driver, endpoint local.
- Definir hosting final.

## C2 — MVP operativo
- Backend: compra, ticket QR, validación, sorteo básico.
- Frontend: flujo compra + validación.
- Infra: docker-compose listo para sala.
- Docs: dominio, reglas, ADRs.

## C3 — Producción regulada
- Observabilidad: logs, métricas, alertas.
- Backup/retention: exportación y retención.
- Deploy guiado y rollback.

## C4 — Escala multi-sala
- Multi-tenant por sala/casino.
- Colas/reintentos si se necesitan.
- Dashboard operativo.
