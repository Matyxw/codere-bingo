# Skills base del proyecto

## skill: backend-architect
- Dominio: FastAPI + SQLAlchemy async + PostgreSQL.
- Regla: toda feature trae schema/servicio/ruta.
- Regla: nunca `shell=True`, siempre ORM.
- Regla: config por `pydantic-settings`, nunca hardcodear.
- Checklist: docstring, type hints, sin `Any` salvo justificación crítica.
- Criterio de done: ruff limpio + test backend verde.

## skill: frontend-crafter
- Dominio: React + Vite + Tailwind v4 + TypeScript.
- Regla: componentes pequeños, tipado estricto.
- Regla: cero emojis, iconos locales.
- Regla: estado centralizado, loading/error/empty siempre.
- Criterio de done: página navegable + test frontend verde.

## skill: qr-auditor
- Dominio: generación, firma, validación y trazabilidad de QR/HMAC.
- Regla: QR único por compra con payload mínimo + HMAC + expiración.
- Regla: validación idempotente.
- Regla: trazabilidad durable en BD.
- Criterio de done: E2E compra→QR→validación sin duplicados.

## skill: infra-operator
- Dominio: Docker Compose, GitHub Codespaces, GitHub Actions.
- Regla: devcontainer debe abrir en Codespaces sin pasos invisibles.
- Regla: CI con cache, health-check real y jobs separados.
- Regla: rollback documentado.
- Criterio de done: CI verde + deploy staging funcional.

## skill: security-guardian
- Dominio: seguridad aplicada al stack existente.
- Regla: security headers activos.
- Regla: CORS estricto por ambiente, nunca `*` en producción.
- Regla: secrets solo desde env, rotación por despliegue.
- Regla: rate limiting básico antes de Redis.
- Criterio de done: auditoría aplicada, no solo documentada.

## skill: observability-engineer
- Dominio: logs, métricas y traces en runtime.
- Regla: `request_id` en toda respuesta.
- Regla: logs estructurados, sin emojis, con trace_id.
- Regla: métricas básicas de latencia y error rate.
- Criterio de done: logs/métricas visibles en staging.

## skill: quality-enforcer
- Dominio: testing, lint, type-check, pre-commit.
- Regla: ruff, mypy, pytest y vitest deben pasar en CI.
- Regla: pre-commit automático antes de cada commit.
- Criterio de done: pipeline CI verde sin bypass manual.

## skill: documentation-keeper
- Dominio: Obsidian + docs del repo.
- Regla: feature sin doc en Obsidian no se implementa.
- Regla: doc por feature con dominio, MVP, ADR y ejemplo.
- Criterio de done: docs sincronizadas con código, enlistadas en `README.md`.

## skill: integration-debugger
- Dominio: resolver fallos de imports, rutas y configuración del proyecto.
- Entradas soportadas:
  - ruta no encontrada, validación 422, 404
  - import circular, modulo no encontrado
  - venv roto, lockfile desincronizado
  - CI con cache corrupto
- Acciones: autodiagnóstico, reintento, parche puntual sin tocar dominio.
- Criterio de done: reproduce el fallo, lo marca en `docs/06-sesiones`, lo evita en adelante.
