# Release

## Staging
- Trigger: push a `main`
- Build: frontend artifact
- Deploy: placeholder hasta conectar infra
- Validación: `/health` y build del frontend

## Producción
- Trigger: tag `v*.*.*`
- Build: frontend artifact
- Deploy: placeholder hasta conectar infra
- Rollback: volver a tag anterior o reusar artifact de `frontend-production`

## Checklist
- [ ] Tests pasan en CI
- [ ] Build de frontend pasa
- [ ] `.env` de producción cargada
- [ ] `/health` responde OK después de deploy
- [ ] Rollback probado en staging
