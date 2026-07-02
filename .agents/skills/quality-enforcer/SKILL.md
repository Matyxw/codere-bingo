---
name: quality-enforcer
description: >
  Skill para mantener calidad estática y dinámica: ruff, mypy, pytest, vitest, pre-commit.
  No implementar features; solo verificar y hacer cumplir gates.
trigger: "calidad, lint, typecheck, tests, pre-commit, coverage"
scope: calidad
---

# quality-enforcer

## Cuándo activarla
- Antes de cualquier merge
- CI rota
- Nuevo hook pre-commit
- Bloqueo por deuda técnica

## Pasos obligatorios
1. Leer `.pre-commit-config.yaml`.
2. Leer `docs/09-operaciones/testing.md`.
3. Correr `ruff check backend` y `mypy backend`.
4. Correr `pytest backend/tests -q`.
5. Correr `npm --prefix frontend exec vitest run`.

## Reglas duras
- No bypass de CI.
- No merge con tests rotos.

## Criterio de done
- Pipeline verde
- Cobertura mínima aceptada o documentada
