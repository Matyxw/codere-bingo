import pytest
from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "codere-bingo"


def test_compra_contrato_422_sin_campos_requeridos():
    response = client.post("/compras", json={})
    assert response.status_code == 422
    body = response.json()
    assert "detail" in body
