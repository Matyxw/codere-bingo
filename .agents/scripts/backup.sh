#!/usr/bin/env bash
set -euo pipefail

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="${BACKUP_DIR:-/tmp/codere-bingo-backups}"
mkdir -p "$BACKUP_DIR"

echo "Backup PostgreSQL -> $BACKUP_DIR"
pg_dump -U "$POSTGRES_USER" -h "$POSTGRES_HOST" "$POSTGRES_DB" -F c -f "$BACKUP_DIR/$POSTGRES_DB-$DATE.dump"
echo "Backup completado: $BACKUP_DIR/$POSTGRES_DB-$DATE.dump"
