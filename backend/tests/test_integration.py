from __future__ import annotations

import os
import sys
import types
from pathlib import Path

import pytest
from httpx import ASGITransport, AsyncClient

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

os.environ.setdefault("APP_ENV", "test")
os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite://")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("CORS_ORIGINS", "*")
os.environ.setdefault("QR_ISSUER", "Codere Bingo")
os.environ.setdefault("DEFAULT_MAX_CARTONES", "6")
os.environ.setdefault("DEFAULT_MIN_CARTONES", "1")
os.environ.setdefault("AUDIT_RETENTION_DAYS", "365")
os.environ.setdefault("JWT_ACCESS_TTL", "30")
os.environ.setdefault("JWT_REFRESH_TTL", "1440")

backend_pkg = types.ModuleType("backend")
backend_pkg.__path__ = [str(project_root / "backend")]
sys.modules["backend"] = backend_pkg

core_pkg = types.ModuleType("backend.core")
core_pkg.__path__ = [str(project_root / "backend" / "core")]
sys.modules["backend.core"] = core_pkg

from backend.main import app  # noqa: E402


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
async def _init():
    from backend.core.database import get_engine
    from backend.core.models import Base

    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


async def _app_client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test"), app


@pytest.mark.asyncio
async def test_health():
    client, _ = await _app_client()
    async with client:
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
        assert response.json()["service"] == "codere-bingo"


@pytest.mark.asyncio
async def test_flujo_compra_qr_y_validacion():
    client, _ = await _app_client()
    async with client:
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


@pytest.mark.asyncio
async def test_compra_sin_datos_devuelve_422():
    client, _ = await _app_client()
    async with client:
        response = await client.post("/compras", json={})
        assert response.status_code in (400, 422)
