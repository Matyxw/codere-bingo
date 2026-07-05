from __future__ import annotations

import os
import sys
import types
from pathlib import Path

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

os.environ["APP_ENV"] = "test"
os.environ["SECRET_KEY"] = "test-secret"
os.environ["CORS_ORIGINS"] = "*"
os.environ["QR_ISSUER"] = "Codere Bingo"
os.environ["DEFAULT_MAX_CARTONES"] = "6"
os.environ["DEFAULT_MIN_CARTONES"] = "1"
os.environ["AUDIT_RETENTION_DAYS"] = "365"
os.environ["JWT_ACCESS_TTL"] = "30"
os.environ["JWT_REFRESH_TTL"] = "1440"

TEST_DB_PATH = project_root / ".pytest-sqlite.db"
TEST_DB_URL = f"sqlite+aiosqlite:///{TEST_DB_PATH}"
os.environ["DATABASE_URL"] = TEST_DB_URL

backend_pkg = types.ModuleType("backend")
backend_pkg.__path__ = [str(project_root / "backend")]
sys.modules["backend"] = backend_pkg

core_pkg = types.ModuleType("backend.core")
core_pkg.__path__ = [str(project_root / "backend" / "core")]
sys.modules["backend.core"] = core_pkg

from backend.core.config import settings  # noqa: E402
from backend.core.database import get_engine  # noqa: E402
from backend.main import app  # noqa: E402

settings.database_url = TEST_DB_URL
engine = get_engine()


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
async def _db():
    from backend.core.models import Base

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(text("PRAGMA journal_mode=WAL"))
    app.state.engine = engine
    app.state.async_session = __import__(
        "backend.core.database", fromlist=["async_session"]
    ).async_session
    yield
    if TEST_DB_PATH.exists():
        TEST_DB_PATH.unlink()
    await engine.dispose()


def _app_client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_health():
    client = _app_client()
    async with client:
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
        assert response.json()["service"] == "codere-bingo"


@pytest.mark.asyncio
async def test_compra_sin_datos_devuelve_422():
    client = _app_client()
    async with client:
        response = await client.post("/compras", json={})
        assert response.status_code in (400, 422)


@pytest.mark.asyncio
async def test_flujo_compra_qr_y_validacion():
    client = _app_client()
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
