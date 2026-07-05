from fastapi import APIRouter, HTTPException

from backend.core.health import router as health_router
from backend.core import schemas, services, types


router = APIRouter()
router.include_router(health_router)


@router.post("/compras", response_model=schemas.CompraOut)
async def crear_compra(command: types.CompraCommand):
    compra = await services.create_compra(command)
    return schemas.CompraOut.model_validate(compra)


@router.get("/compras/{compra_id}", response_model=schemas.CompraOut)
async def obtener_compra(compra_id: str):
    compra = await services.get_compra(compra_id)
    if not compra:
        raise HTTPException(status_code=404, detail="compra no encontrada")
    return schemas.CompraOut.model_validate(compra)


@router.post("/tickets/validar", response_model=schemas.CompraOut)
async def validar_ticket(validacion_in: schemas.ValidacionQrIn):
    ticket = await services.validate_qr(validacion_in.qr_payload)
    if not ticket:
        raise HTTPException(status_code=404, detail="ticket no encontrado")
    compra = await services.get_compra(ticket["compra_id"])
    if not compra:
        raise HTTPException(status_code=404, detail="compra no encontrada")
    compra["creado_en"] = (
        compra["creado_en"].isoformat() if hasattr(compra["creado_en"], "isoformat") else compra["creado_en"]
    )
    return schemas.CompraOut.model_validate(compra)


@router.post("/sorteos", response_model=schemas.SorteoOut)
async def crear_sorteo(command: types.SorteoCommand):
    sorteo = await services.create_sorteo(command)
    return schemas.SorteoOut.model_validate(sorteo)
