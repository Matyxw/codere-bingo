# AI-READY MANIFEST — Codere Bingo

## Proyecto
- Repo: `Matyxw/codere-cartones`
- Rama: `main`
- URL: https://github.com/Matyxw/codere-cartones

## Stack confirmado
- Backend: FastAPI + SQLAlchemy 2.0 async + PostgreSQL + Alembic
- Frontend: React + TypeScript + Vite + Tailwind v4
- Testing backend: pytest + TestClient + rate-limit unit
- Testing frontend: Vitest + Testing Library + jsdom
- Infra: Docker Compose + GitHub Actions + Codespaces

## Skills IA activas
1. `backend-architect` — feature backend, endpoint, schema
2. `frontend-crafter` — página, componente, lib/api
3. `qr-auditor` — QR, ticket, validación, HMAC
4. `infra-operator` — deploy, CI, Codespaces, docker
5. `security-guardian` — CORS, headers, rate limit, secrets
6. `observability-engineer` — logs, métricas, traces, request_id
7. `quality-enforcer` — lint, tests, pre-commit, coverage
8. `documentation-keeper` — docs, ADR, README, onboarding
9. `integration-debugger` — imports, rutas, tests, CI, venv

## Puertos
- Backend: `8000`
- Frontend: `5173`
- Postgres: `5432`

## Comandos obligatorios antes de editar dominio
```bash
bash .agents/scripts/smoke_test.sh
bash .agents/scripts/local_test.sh
```

## Deploy
- Staging: push a `main`
- Producción: tag `v*.*.*`
- Scripts: `.agents/scripts/deploy_staging.sh`, `.agents/scripts/deploy_production.sh`

## Validación continua
- Backend contratos: `pytest backend/tests/test_e2e_contracts.py -q`
- Backend rate limit: `pytest backend/tests/test_rate_limit.py -q`
- Frontend unit: `npm run test --prefix frontend -- --run`
- Lint backend: `ruff check backend`
- Typecheck backend: `mypy backend || true`

## Estado actual
- Smoke-test: PASS
- Tests E2E por contrato: PASS
- Rate limit unit: PASS
- CI: lista para correr en GitHub Actions
- Configuración AI: COMPLETA

## Proxy real pendiente
1. Ejecutar `bash .agents/scripts/local_test.sh` en tu máquina/Antigravity
2. Conectar staging/producción en `.github/workflows/deploy-*.yml`
3. Definir `IMPRESORA_URL`, `WEB_PRINT_TOKEN` y binario para `agente-local/`
