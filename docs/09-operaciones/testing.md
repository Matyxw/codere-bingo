# Testing backend

## Objetivo
Tener suite backend reproducible en Codespaces y CI sin depender de venv locales rotos.

## Comandos
```bash
# Instalar lockfile
python -m pip install -r requirements.lock.txt

# Unit tests (SQLite async)
pytest backend/tests/test_main.py -q

# E2E
pytest backend/tests/test_e2e_compra.py -q
```

## Nota
En Codespaces recomiendo correr desde la imagen devcontainer oficial; evita venv locales rotos.
