# Codere Bingo

Sistema de venta de cartones de bingo en sala presencial, con ticket QR, impresión local por puesto y validación en sorteo.

## Stack
- Backend: FastAPI + SQLAlchemy 2.0 async + PostgreSQL + Alembic
- Frontend: React + TypeScript + Vite + Tailwind v4
- Infra: Docker Compose + GitHub Codespaces + GitHub Actions

## Inicio rápido
```bash
# Clonar repo
git clone git@github.com:Matyxw/codere-cartones.git
cd codere-bingo

# Backend local
uvicorn backend.main:app --reload

# Frontend local
npm run dev --prefix frontend

# Tests backend
bash .agents/scripts/local_test.sh
```

## Puertos
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`

## Docs
- Dominio: `docs/02-dominio/proyecto.md`
- Arquitectura: `docs/03-arquitectura/overview.md`
- Operación: `docs/09-operaciones/`
- Roadmap: `docs/04-roadmap/roadmap.md`

## Skills IA
- Catálogo: `.agents/skills/README.md`
- Índice por flujo: `docs/AI-READY.md`
