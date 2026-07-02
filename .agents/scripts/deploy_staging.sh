#!/usr/bin/env bash
set -euo pipefail

echo "=== Deploy Staging Local ==="
echo "1. Build backend: docker compose build backend"
echo "2. Build frontend: npm run build --prefix frontend"
echo "3. Deploy: rsync -avz frontend/dist/ user@staging:/var/www/codere-bingo/"
echo "4. Backend: docker compose -f docker-compose.staging.yml up -d"
echo "5. Health: curl -f https://staging.example.com/health"
