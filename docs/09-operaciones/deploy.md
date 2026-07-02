# Deploy

## Staging
- Trigger automático: push a `main`
- Build: frontend artifact
- Deploy: placeholder hasta conectar infra
- Health check: placeholder hasta conectar URL
- Retention: artifacts 7 días

## Producción
- Trigger: tag `v*.*.*`
- Build: frontend artifact
- Deploy: placeholder hasta conectar infra
- Health check: placeholder hasta conectar URL
- Retention: artifacts 30 días
- Notificación: placeholder para Slack/webhook

## Scripts locales
- Staging: `.agents/scripts/deploy_staging.sh`
- Producción: `.agents/scripts/deploy_production.sh`

## Checklist pre-deploy
- [ ] Tests pasan en CI
- [ ] Build de frontend pasa
- [ ] `.env` de producción configurado
- [ ] Health check definido
- [ ] Rollback documentado

## Rollback
- Staging: redeploy artifact anterior
- Producción: revert tag o reusar artifact `frontend-production`
