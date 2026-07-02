from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class OperadorIn(BaseModel):
    username: str = Field(..., min_length=3, max_length=80)
    password: str = Field(..., min_length=8)
    nombre_visible: str = Field(..., min_length=2, max_length=120)


class OperadorOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    username: str
    nombre_visible: str
    activo: bool
    creado_en: str


class PuestoIn(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=120)
    ubicacion: str = Field(..., min_length=2, max_length=180)
    impresora_url: Optional[str] = Field(None, max_length=255)


class PuestoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    nombre: str
    ubicacion: str
    impresora_url: Optional[str]
    creado_en: str


class CartonOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    orden: int
    grilla: str


class CompraIn(BaseModel):
    operador_id: str
    puesto_id: str
    cantidad_cartones: int = Field(..., ge=1, le=6)
    importe_total: float = Field(..., gt=0)
    medio_pago: str = Field("efectivo", max_length=20)
    cliente_nombre: Optional[str] = Field(None, max_length=120)


class CompraOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    cantidad_cartones: int
    importe_total: float
    qr_payload: str
    medio_pago: str
    cliente_nombre: Optional[str]
    creado_en: str


class SorteoIn(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=120)
    estado: str = Field("abierto", max_length=30)
    modalidad: str = Field("libre", max_length=30)
    inicia_en: Optional[str] = None
    cierra_en: Optional[str] = None


class SorteoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    nombre: str
    estado: str
    modalidad: str
    inicia_en: Optional[str]
    cierra_en: Optional[str]
    creado_en: str


class ValidacionQrIn(BaseModel):
    qr_payload: str = Field(..., min_length=1, max_length=255)
