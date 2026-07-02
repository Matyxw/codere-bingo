#!/usr/bin/env bash
set -euo pipefail

PROJECT="/mnt/d/codigos/importante/Codere-Bingo"
cd "$PROJECT"

VENV_DIR=".venv"
PYTHON="${VENV_DIR}/bin/python"
export PYTHONPATH="$PROJECT"
export DATABASE_URL="sqlite+aiosqlite://"
export SECRET_KEY="test-secret"
export CORS_ORIGINS="*"

if [ ! -x "$PYTHON" ]; then
  python3 -m venv "$VENV_DIR"
  "$VENV_DIR/bin/python" -m pip install --upgrade pip
  "$VENV_DIR/bin/python" -m pip install -r requirements.lock.txt
fi

echo '=== validate ==='
"$PYTHON" -m ruff check backend || true
echo 'ruff done'

echo '=== typecheck ==='
"$PYTHON" -m mypy backend || true
echo 'mypy done'

echo '=== tests ==='
"$PYTHON" -m pytest backend/tests -q
echo 'tests done'
