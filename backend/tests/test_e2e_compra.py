from httpx import ASGITransport, AsyncClient
import pytest

from backend.main import app


@pytest.mark.asyncio
async def test_flujo_compra_qr_y_validacion():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        compra_resp = await client.post(
            "/compras",
            json={
                "operador_id": "operador-test",
                "puesto_id": "puesto-test",
                "cantidad_cartones": 2,
                "importe_total": 100.0,
                "cliente_nombre": "Cliente E2E",
            },
        )
        assert compra_resp.status_code == 200, compra_resp.text
        compra = compra_resp.json()
        qr_payload = compra["qr_payload"]
        assert compra["cantidad_cartones"] == 2

        validacion_resp = await client.post("/tickets/validar", json={"qr_payload": qr_payload})
        assert validacion_resp.status_code == 200, validacion_resp.text
        validacion = validacion_resp.json()
        assert validacion["id"] == compra["id"]

        revalidacion_resp = await client.post("/tickets/validar", json={"qr_payload": qr_payload})
        assert revalidacion_resp.status_code == 200
        revalidacion = revalidacion_resp.json()
        assert revalidacion["id"] == compra["id"]
