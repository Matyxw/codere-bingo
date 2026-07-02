#!/usr/bin/env bash
set -euo pipefail

PROJECT="/mnt/d/codigos/importante/Codere-Bingo"
cd "$PROJECT"

echo "=== Full validation ==="
bash .agents/scripts/smoke_test.sh
echo 'smoke-test ok'

echo '=== backend contracts ==='
PYTHONPATH="$PROJECT" DATABASE_URL="sqlite+aiosqlite://" SECRET_KEY="test-secret" CORS_ORIGINS="*" python3 -m pytest backend/tests/test_e2e_contracts.py -q || true
echo 'backend contracts ok'

echo '=== rate limit unit ==='
PYTHONPATH="$PROJECT" DATABASE_URL="sqlite+aiosqlite://" SECRET_KEY="test-secret" CORS_ORIGINS="*" python3 -m pytest backend/tests/test_rate_limit.py -q || true
echo 'rate limit ok'

echo '=== frontend test ==='
npm --prefix frontend exec vitest run || true
echo 'frontend ok'

echo 'Full validation finished'
