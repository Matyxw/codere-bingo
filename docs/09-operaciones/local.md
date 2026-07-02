# Operación — Local

## Requisitos
- Docker y Docker Compose
- Python 3.11
- Node 20

## Arranque rápido
```bash
cp .env.example .env
docker compose up
```

## Puertos útiles
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`
- Postgres: `localhost:5432`

## Verificaciones mínimas
```bash
curl -s http://localhost:8000/health | jq
```

## Flujo mínimo
1. Abrir `/` en frontend.
2. Completar compra.
3. Imprimir ticket con QR.
4. Escanear en `/validar`.

## Troubleshooting
- Puerto ocupado: cambiar en `docker-compose.yml` y `.env.example`.
- QR inválido: revisar SECRET_KEY y reloj del servidor.
- Error en BD: revisar `DATABASE_URL` y health de Postgres.
