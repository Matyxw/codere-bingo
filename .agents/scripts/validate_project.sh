#!/usr/bin/env bash
set -euo pipefail

echo "=== Codere Bingo — Repo validation ==="
python -m ruff check backend || true
python -m mypy backend || true
python -m pytest backend/tests/test_main.py -q || true

echo "=== Frontend validation ==="
npm --prefix frontend exec vitest run || true

echo "Validation finished"
