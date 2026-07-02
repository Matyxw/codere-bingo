.PHONY: help backend frontend tests lint validate clean

help:
	@echo "Codere Bingo - Comandos"
	@echo "  make backend		- Run backend"
	@echo "  make frontend		- Run frontend"
	@echo "  make tests		- Run tests"
	@echo "  make lint		- Run lint"
	@echo "  make validate		- Run validation"
	@echo "  make clean		- Clean caches"

backend:
	uvicorn backend.main:app --reload

frontend:
	npm run dev --prefix frontend

tests:
	pytest backend/tests -q

lint:
	ruff check backend

validate:
	bash .agents/scripts/validate_project.sh

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache htmlcov .coverage
