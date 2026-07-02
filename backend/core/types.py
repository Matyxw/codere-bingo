from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class CartonGrilla(BaseModel):
    model_config = ConfigDict(strict=True)

    id: str = Field(..., min_length=1)
    numeros: list[list[int | None]] = Field(..., min_length=5, max_length=5)


class CompraCommand(BaseModel):
    puesto_id: str = Field(..., min_length=1)
    operador_id: str = Field(..., min_length=1)
    cantidad_cartones: int = Field(..., ge=1, le=6)
    medio_pago: str = Field("efectivo", max_length=20)
    importe_total: float = Field(..., gt=0)
    cliente_nombre: str | None = Field(None, max_length=120)


class CompraResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    qr_payload: str
    cantidad_cartones: int
    importe_total: float
    medio_pago: str
    creado_en: str


class SorteoCommand(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=120)
    modalidad: str = Field("libre", max_length=30)


class SorteoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    nombre: str
    estado: str
    modalidad: str
    creado_en: str


class ValidacionQrCommand(BaseModel):
    qr_payload: str = Field(..., min_length=1, max_length=255)
