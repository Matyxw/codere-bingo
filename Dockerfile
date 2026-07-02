FROM python:3.11-slim AS base
RUN useradd -m appuser
WORKDIR /app

FROM base AS deps
COPY requirements.lock.txt .
RUN pip install --no-cache-dir -r requirements.lock.txt

FROM base AS runtime
COPY --from=deps /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=deps /usr/local/bin /usr/local/bin
COPY backend ./backend
COPY requirements.lock.txt .
ENV PYTHONDONTWRITEBYTECODE=1
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
