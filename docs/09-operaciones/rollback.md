# Rollback

Si una release rompe producción:
1. Identificar último commit `main` estable conocido.
2. Para rollback de backend: cambiar tag o apuntar al commit anterior.
3. Para rollback de frontend: redeploy del artifact `frontend-production` conocido.
4. Validar health y métricas básicas.
5. Comunicar a sala: modo offline si corresponde, y reanudar cuando health OK.

## Prueba de rollback
- Ejecutar en staging primero.
- Verificar `/health` y fl mínimo.
