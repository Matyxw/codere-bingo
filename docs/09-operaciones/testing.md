# Testing

## Backend
- Unit tests: `pytest backend/tests/test_main.py -q`
- E2E: `pytest backend/tests/test_e2e_compra.py -q`
- Requiere `asyncpg`.
- En local usar entorno aislado: `.agents/scripts/run_integration_tests.sh`

## Frontend
- Unit + component tests: `npm --prefix frontend exec vitest run`
- E2E Playwright está planeado pero no bloquea el repo.

## CI
- GitHub Actions provee PostgreSQL 16 real como service.
- Correr tests desde Codespaces/Docker asegura dependencias correctas.

## Nota
Si falla import por `asyncpg`, primero correr el script de entorno aislado o usar Docker Codespaces.
