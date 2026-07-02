# Estado maestro — Codere Bingo
- Repo: `github.com/Matyxw/codere-cartones`
- Rama: `main`
- Smoke-test: PASS
- Último commit: `10de8b6`

## Configuración AI-ready
- `.agents/` completo y fusionado desde `Codere`, `Bot_ia`, `the-architect`
- 9 skills ejecutables para Gemini Pro / Claude Sonnet
- `docs/AI-READY.md` con manifiesto oficial

## Entregado
- CI/CD endurecida con `asyncpg`
- Tests backend: contratos E2E y rate limiting
- Tests frontend: Vitest + Testing Library configurado
- Seguridad: headers, CORS por entorno, rate limiting real
- Observabilidad: logs estructurados, `request_id`
- Deploy: workflows staging/producción endurecidos
- Docs: dominio, arquitectura, operación, backup/restore
- Agente local: configuración y checklist operativos
- Templates GitHub: issue, PR, security policy, CODEOWNERS
- Validación local reproducible: `.agents/scripts/local_test.sh`
- Smoke-test: `.agents/scripts/smoke_test.sh`

## Pendiente para cierre absoluto
1. Ejecutar `bash .agents/scripts/local_test.sh` en tu máquina/Antigravity
2. Conectar staging/producción real a los workflows
3. Definir impresora/puesto para agente local funcional
