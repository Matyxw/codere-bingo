# Backup / Restore

## Backup
- Automático: `bash .agents/scripts/backup.sh`
- Manual:
  ```bash
  BACKUP_DIR=/backups/codere-bingo bash .agents/scripts/backup.sh
  ```

## Restore
- `bash .agents/scripts/restore.sh /backups/codere-bingo/codere_bingo-YYYYMMDD_HHMMSS.dump`

## Reglas
- Rotar backups cada 30 días.
- Validar restore semanal.
- Nunca restaurar sobre producción sin verificar fecha y base.
