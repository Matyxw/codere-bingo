#!/bin/bash
set -euo pipefail
python -m ruff check backend
python -m mypy backend || true
python -m pytest backend/tests -q
npm --prefix frontend run build --silent 2>/dev/null || true
