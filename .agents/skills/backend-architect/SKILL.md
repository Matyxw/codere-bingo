---
name: backend-architect
description: >
  Skill para diseñar y ejecutar features backend en FastAPI + SQLAlchemy async + PostgreSQL.
  Aplica solo a backend; no tocar frontend ni dominio adicional.
trigger: "feature backend, endpoint, schema, servicio, migración"
scope: backend
---

# backend-architect

## Cuándo activarla
- Agregar/quitar endpoint
- Modificar schema/servicio/crud
- Nueva migración
- Cambio de contrato API

## Pasos obligatorios
1. Leer `.agents/CONTEXT.md` y `docs/02-dominio/proyecto.md`.
2. Leer `.agents/decisions/adrs.md`.
3. Leer `backend/core/routes.py` y `backend/core/services.py`.
4. Actualizar `backend/core/schemas.py` primero.
5. Implementar servicio y ruta.
6. Actualizar `backend/tests/test_*.py`.
7. Correr `ruff check backend` y `pytest backend/tests -q`.

## Reglas duras
- Sin `shell=True`.
- Sin SQL concatenado; siempre ORM.
- Sin secrets hardcode.
- Typer estricto + docstring.

## Criterio de done
- ruff limpio
- tests backend verdes
- docstring presente
