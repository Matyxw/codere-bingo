# Conexión de infra real

## Staging
1. Definir URL de staging y health check.
2. Reemplazar placeholders en `.github/workflows/deploy-staging.yml`.
3. Cargar secrets en GitHub Environment `staging`.
4. Ejecutar deploy manual desde Actions.

## Producción
1. Definir URL de producción y health check.
2. Reemplazar placeholders en `.github/workflows/deploy-production.yml`.
3. Cargar secrets en GitHub Environment `production`.
4. Crear tag `v*.*.*` para disparar deploy.
5. Verificar `/health` y rollback.

## Secrets mínimos
- `DATABASE_URL`
- `SECRET_KEY`
- `CORS_ORIGINS`
- `WEB_PRINT_URL` (por puesto)
- `WEB_PRINT_TOKEN` (por puesto)

## Agente local
- Definir modelo de impresora.
- Definir endpoint local del puesto.
- Cargar `WEB_PRINT_URL` y `WEB_PRINT_TOKEN` en `.env` del puesto.
- Instalar binario del agente.
