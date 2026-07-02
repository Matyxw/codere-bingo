from __future__ import annotations

import datetime
import enum
import secrets

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Numeric,
    Boolean,
    Enum as SQLEnum,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from backend.core.database import Base


class EstadoSorteo(str, enum.Enum):
    abierto = "abierto"
    cerrado = "cerrado"
    cancelado = "cancelado"


class Operador(Base):
    __tablename__ = "operadores"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: secrets.token_hex(16))
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    nombre_visible: Mapped[str] = mapped_column(String(120), nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    creado_en: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)


class Puesto(Base):
    __tablename__ = "puestos"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: secrets.token_hex(16))
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    ubicacion: Mapped[str] = mapped_column(String(180), nullable=False)
    impresora_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    creado_en: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)


class Compra(Base):
    __tablename__ = "compras"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: secrets.token_hex(16))
    operador_id: Mapped[str] = mapped_column(String, ForeignKey("operadores.id"), nullable=False)
    puesto_id: Mapped[str] = mapped_column(String, ForeignKey("puestos.id"), nullable=False)
    cantidad_cartones: Mapped[int] = mapped_column(Integer, nullable=False)
    importe_total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    qr_payload: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    medio_pago: Mapped[str] = mapped_column(String(20), nullable=False, default="efectivo")
    cliente_nombre: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    creado_en: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)


class Carton(Base):
    __tablename__ = "cartones"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: secrets.token_hex(16))
    compra_id: Mapped[str] = mapped_column(String, ForeignKey("compras.id"), nullable=False)
    orden: Mapped[int] = mapped_column(Integer, nullable=False)
    grilla: Mapped[str] = mapped_column(String, nullable=False)
    creado_en: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)


class Sorteo(Base):
    __tablename__ = "sorteos"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: secrets.token_hex(16))
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    estado: Mapped[EstadoSorteo] = mapped_column(SQLEnum(EstadoSorteo), nullable=False, default=EstadoSorteo.abierto)
    modalidad: Mapped[str] = mapped_column(String(30), nullable=False, default="libre")
    inicia_en: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, nullable=True)
    cierra_en: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, nullable=True)
    creado_en: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)


class TicketQr(Base):
    __tablename__ = "tickets_qr"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: secrets.token_hex(16))
    compra_id: Mapped[str] = mapped_column(String, ForeignKey("compras.id"), nullable=False)
    qr_payload: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    usado: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    validado_en: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, nullable=True)
    creado_en: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
