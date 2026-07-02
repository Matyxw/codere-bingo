# Backend — API
- Health: `/health`
- Compra: `POST /compras`
- Consulta: `GET /compras/{compra_id}`
- Validación QR: `POST /tickets/validar`
- QR imagen: `GET /tickets/{qr_payload}/qr`
- Sorteo: `POST /sorteos`

# Frontend — Flujo Mínimo
- Nueva compra: ingresar operador, puesto, cantidad, importe y cliente.
- Resultado: respuesta con `qr_payload` y cantidad de cartones.
- Validación: ingresar `qr_payload` y mostrar resultado.

# Infra
- Codespaces: abrir repo → Codespaces → crear.
- Backend local: `uvicorn backend.main:app --reload`
- Frontend local: `npm run dev --prefix frontend`
