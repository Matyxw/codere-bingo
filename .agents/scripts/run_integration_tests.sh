#!/usr/bin/env bash
set -euo pipefail

cd /mnt/d/codigos/importante/Codere-Bingo

if [ ! -d backend/.venv ]; then
  python -m venv backend/.venv
fi
source backend/.venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.lock.txt
export DATABASE_URL="${DATABASE_URL:-postgresql+asyncpg://postgres:postgres@db:5432/codere_bingo}"
export SECRET_KEY="${SECRET_KEY:-test-secret}"
export CORS_ORIGINS="*"
pytest backend/tests -q
echo 'INTEGRATION_TESTS_READY'
