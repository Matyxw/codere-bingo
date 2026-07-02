# AI-READY MANIFEST — Codere Bingo

## Proyecto
- Repo: `Matyxw/codere-cartones`
- Rama: `main`
- URL: https://github.com/Matyxw/codere-cartones

## Stack
- Backend: FastAPI + SQLAlchemy 2.0 async + PostgreSQL + Alembic
- Frontend: React + TypeScript + Vite + Tailwind v4
- Infra: Docker Compose + GitHub Codespaces + GitHub Actions
- Testing: pytest async, vitest
- Lint/typecheck: ruff, mypy

## Skills activas
1. `backend-architect`
2. `frontend-crafter`
3. `qr-auditor`
4. `infra-operator`
5. `security-guardian`
6. `observability-engineer`
7. `quality-enforcer`
8. `documentation-keeper`
9. `integration-debugger`

## Archivos obligatorios antes de editar
1. `AGENTS.md`
2. `.clinerules`
3. `.agents/CONTEXT.md`
4. `.agents/SKILL_MAP.md`
5. `.agents/rules/decision-gate.md`
6. `docs/02-dominio/proyecto.md`

## Comandos
- Backend: `uvicorn backend.main:app --reload`
- Frontend: `npm run dev --prefix frontend`
- Tests backend: `pytest backend/tests -q`
- Lint: `ruff check backend`
- Typecheck: `mypy backend`
- Validación: `make validate`

## Puertos
- Backend: `8000`
- Frontend: `5173`
- Postgres: `5432`

## Nota para IA
- No implementar features sin abrir la skill correspondiente.
- No cambiar dominio sin ADR.
- No introducir dependencias sin skill `infra-operator`.
