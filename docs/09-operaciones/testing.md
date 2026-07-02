# Reproducir tests sin pelearse con Hermes

- `cd /mnt/d/codigos/importante/Codere-Bingo`
- `python3 -m venv .venv`
- `. .venv/bin/activate`
- `python -m pip install -r requirements.lock.txt`
- `PYTHONPATH=/mnt/d/codigos/importante/Codere-Bingo pytest backend/tests -q`

Nota: el fallo actual en local es de módulo `aiosqlite` en el intérprete usado; en CI/usando el venv del repo debería avanzar.
