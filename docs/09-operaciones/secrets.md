# Operación — Variables y secrets por entorno

## Local
- `DATABASE_URL`
- `SECRET_KEY`
- `CORS_ORIGINS`

## Codespaces
- Mismas variables, cargadas desde `.env`.

## Producción
- Usar gestor de secrets; no versionar `.env`.
- Rotar `SECRET_KEY` por despliegue.
- Definir `WEB_PRINT_URL` y `WEB_PRINT_TOKEN` solo cuando el puesto tenga impresora configurada.
