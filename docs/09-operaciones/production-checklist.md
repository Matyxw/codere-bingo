# Checklist producción

## Configuración
- [ ] `.agents/` completo y skills ejecutables
- [ ] `docs/` sincronizadas
- [ ] `AGENTS.md` y `.clinerules` actualizados
- [ ] Devcontainer listo para Codespaces
- [ ] Pre-commit configurado

## Testing
- [ ] Tests backend verdes en CI
- [ ] Tests frontend verdes en CI
- [ ] Tests locales garantizados con `.agents/scripts/local_test.sh`

## Seguridad
- [ ] Security headers activos
- [ ] CORS productivo por ambiente
- [ ] Rate limiting real
- [ ] Secrets rotados

## Observabilidad
- [ ] Logs estructurados
- [ ] Request ID en respuestas
- [ ] Métricas básicas documentadas

## Deploy
- [ ] Staging automatizado
- [ ] Producción por tag
- [ ] Rollback documentado
- [ ] Backup/restore probado

## Operación
- [ ] Agente local configurado por puesto
- [ ] Onboarding documentado
- [ ] Runbooks actualizados
