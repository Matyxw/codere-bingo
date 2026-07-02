#!/usr/bin/env bash
set -euo pipefail

PROJECT="/mnt/d/codigos/importante/Codere-Bingo"
cd "$PROJECT"

echo '=== Smoke-test: config ==='
test -f AGENTS.md
test -f .clinerules
test -f .agents/WORLD_STATE.md
test -f .agents/skills/README.md
test -f docs/AI-READY.md
test -f .github/workflows/ci.yml
test -f .pre-commit-config.yaml
test -f .devcontainer/devcontainer.json
test -f .agents/scripts/local_test.sh
test -f docs/09-operaciones/testing.md

echo 'Smoke-test passed'
