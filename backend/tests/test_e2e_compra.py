import os
import sys
import types
from pathlib import Path

import pytest
from httpx import ASGITransport, AsyncClient

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

os.environ.setdefault("DATABASE_URL", "sqlite://")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("CORS_ORIGINS", "*")

backend_pkg = types.ModuleType("backend")
backend_pkg.__path__ = [str(project_root / "backend")]
sys.modules["backend"] = backend_pkg

core_pkg = types.ModuleType("backend.core")
core_pkg.__path__ = [str(project_root / "backend" / "core")]
sys.modules["backend.core"] = core_pkg

from backend.main import app  # noqa: E402


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
