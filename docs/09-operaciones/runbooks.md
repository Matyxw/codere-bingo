# Runbook — Backup/restore

## Backup
1. Detener escritura pesada.
2. Ejecutar `.agents/scripts/backup.sh`.
3. Mover dump a almacenamiento remoto.

## Restore
1. Confirmar punto de restauración.
2. Ejecutar `.agents/scripts/restore.sh <dump>`.
3. Correr `pytest backend/tests/test_contracts.py -q`.
4. Verificar `/health` antes de reanudar operación.
