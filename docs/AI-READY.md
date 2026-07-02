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
1. `backend-architect` — feature backend, endpoint, schema
2. `frontend-crafter` — página, componente, lib/api
3. `qr-auditor` — QR, ticket, validación, HMAC
4. `infra-operator` — deploy, CI, Codespaces, docker
5. `security-guardian` — CORS, headers, rate limit, secrets
6. `observability-engineer` — logs, métricas, traces, request_id
7. `quality-enforcer` — lint, tests, pre-commit, coverage
8. `documentation-keeper` — docs, ADR, README, onboarding
9. `integration-debugger` — imports, rutas, tests, CI, venv

## Archivos obligatorios antes de editar
1. `AGENTS.md`
2. `.clinerules`
3. `.agents/CONTEXT.md`
4. `.agents/SKILL_MAP.md`
5. `.agents/rules/decision-gate.md`
6. `docs/02-dominio/proyecto.md`

## Cómo usar este archivo con IA
- Antes de cualquier tarea, lee `docs/AI-READY.md` y `.agents/skills/README.md`.
- Identifica la skill por trigger/scope.
- Ejecuta los pasos obligatorios de esa skill.
- No cambies dominio sin ADR.
- No introduzcas dependencias sin skill `infra-operator`.

## Comandos
- Backend: `uvicorn backend.main:app --reload`
- Frontend: `npm run dev --prefix frontend`
- Tests backend: `pytest backend/tests -q`
- Lint: `ruff check backend`
- Typecheck: `mypy backend`
- Validación local: `bash .agents/scripts/local_test.sh`
- Smoke-test: `bash .agents/scripts/smoke_test.sh`

## Puertos
- Backend: `8000`
- Frontend: `5173`
- Postgres: `5432`

## Nota para Gemini Pro / Claude Sonnet
- Seguí siempre la skill correspondiente antes de actuar.
- Respetá la decision gate T1/T2/T3.
- No inventes stack ni dependencias.
- Documentá todo cambio.
