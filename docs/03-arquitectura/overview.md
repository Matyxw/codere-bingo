# Arquitectura

## Backend
- FastAPI async conrutas separadas por dominio.
- SQLAlchemy 2.0 async + Alembic.
- Pydantic para contratos.
- QR firmado + expiración.
- Trazabilidad durable.

## Frontend
- React + Vite + Tailwind v4.
- Páginas: compra y validación.
- Estado centralizado y manejo de errores explícito.

## Infra
- Docker Compose multi-servicio.
- GitHub Codespaces listo.
- CI con cache y health-check.
- Pre-commit automático.
