from fastapi import APIRouter
from fastapi.testclient import TestClient

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok", "service": "codere-bingo"}


@router.post("/compras")
def compra_stub():
    return {"status": "stub"}


@router.post("/tickets/validar")
def validar_stub():
    return {"status": "stub"}


app = None
client = TestClient(router)


def test_health_contract():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "codere-bingo"


def test_compra_contract_missing_body():
    response = client.post("/compras", json={})
    assert response.status_code == 200


def test_validacion_contract_missing_payload():
    response = client.post("/tickets/validar", json={})
    assert response.status_code == 200
