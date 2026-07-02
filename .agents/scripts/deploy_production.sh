#!/usr/bin/env bash
set -euo pipefail

echo "=== Deploy Production Local ==="
echo "1. Tag release: git tag v1.0.0 && git push origin v1.0.0"
echo "2. Build backend: docker compose build backend"
echo "3. Build frontend: npm run build --prefix frontend"
echo "4. Deploy: blue-green or rolling update"
echo "5. Health: curl -f https://codere-bingo.example.com/health"
echo "6. Rollback: git revert HEAD && git push origin main"
