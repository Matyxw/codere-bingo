---
name: infra-operator
description: >
  Skill para Docker, Codespaces, GitHub Actions y releases.
  No modificar lógica de dominio; solo tooling.
trigger: "deploy, CI, Codespaces, docker, workflow, release"
scope: infra
---

# infra-operator

## Cuándo activarla
- Cambio en `.devcontainer`
- Cambio en `.github/workflows/*.yml`
- Cambio en `docker-compose.yml` o `Dockerfile`
- Release

## Pasos obligatorios
1. Leer `docs/09-operaciones/ambientes.md`.
2. Leer `.agents/config/workflows.schema.yaml`.
3. Probar build local: `docker compose build`.
4. Verificar health en `/health`.
5. Documentar en `docs/09-operaciones/local.md`.

## Reglas duras
- No exponer secrets en workflow.
- Cachear dependencias.
- Health-check real antes de avanzar.

## Criterio de done
- CI verde
- Build listo
- Docs actualizada
