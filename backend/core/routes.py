from fastapi import APIRouter, HTTPException

from backend.core.health import router as health_router
from backend.core import schemas, services

router = APIRouter()
router.include_router(health_router)


@router.post("/compras", response_model=schemas.CompraOut)
async def crear_compra(command: schemas.CompraIn):
    compra = await services.create_compra(
        services.types.CompraCommand(**command.model_dump())
    )
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
    compra = await services.get_compra(ticket.compra_id)
    return schemas.CompraOut.model_validate(compra)


@router.post("/sorteos", response_model=schemas.SorteoOut)
async def crear_sorteo(sorteo_in: schemas.SorteoIn):
    sorteo = await services.create_sorteo(
        services.types.SorteoCommand(**sorteo_in.model_dump())
    )
    return schemas.SorteoOut.model_validate(sorteo)
