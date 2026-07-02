# Ambientes

## Local
- `docker compose up`
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`
- Health: `http://localhost:8000/health`

## Codespaces
- Abrir repo → Codespaces
- Puertos expuestos: `8000`, `5173`, `5432`
- Backend y frontend listos para usar

## Staging
- Variables: `STAGING_*`
- Deploy automático por push a `main`
- Validación mínima: `/health`, build de frontend

## Producción
- Variables: `PRODUCTION_*`
- Deploy por tag `v*.*.*`
- Rollback documentado
- Secrets desde gestor de secrets Codere
