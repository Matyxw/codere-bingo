#!/usr/bin/env bash
set -euo pipefail

RESTORE_FILE="${1:-}"
if [ -z "$RESTORE_FILE" ] || [ ! -f "$RESTORE_FILE" ]; then
  echo "Uso: $0 <archivo.dump>"
  exit 1
fi

echo "Restore PostgreSQL desde $RESTORE_FILE"
pg_restore -U "$POSTGRES_USER" -h "$POSTGRES_HOST" -d "$POSTGRES_DB" "$RESTORE_FILE"
echo "Restore completado."
