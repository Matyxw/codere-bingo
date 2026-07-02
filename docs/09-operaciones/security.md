# Seguridad aplicada

## Middleware
- Security headers activos por defecto.
- Rate limiting básico por IP (placeholder hasta Redis).

## CORS
- Definir `CORS_ORIGINS` en `.env` por entorno.
- En producción usar dominios exactos; nunca `*`.

## Secrets
- Rotar `SECRET_KEY` por despliegue.
- Nunca versionar `.env`.
- `WEB_PRINT_TOKEN` solo cuando hay impresora activa.

## QR/HMAC
- QR firmado con `SECRET_KEY`.
- Validación idempotente: primer escaneo válido, siguientes retornan misma marca.

## Cumplimiento
- Trazabilidad mínima: operador, puesto, fecha, importe, ticket.
- Retención configurable por `AUDIT_RETENTION_DAYS`.
