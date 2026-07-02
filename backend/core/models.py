import datetime
import enum
import uuid

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Numeric,
    Boolean,
    Enum,
)
from sqlalchemy.orm import DeclarativeBase, relationship

from backend.core.database import Base


class EstadoSorteo(str, enum.Enum):
    abierto = "abierto"
    cerrado = "cerrado"
    cancelado = "cancelado"


class Operador(Base):
    __tablename__ = "operadores"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    nombre_visible = Column(String(120), nullable=False)
    activo = Column(Boolean, nullable=False, default=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow)


class Puesto(Base):
    __tablename__ = "puestos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(120), nullable=False)
    ubicacion = Column(String(180), nullable=False)
    impresora_url = Column(String(255), nullable=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow)


class Compra(Base):
    __tablename__ = "compras"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    operador_id = Column(String, ForeignKey("operadores.id"), nullable=False)
    puesto_id = Column(String, ForeignKey("puestos.id"), nullable=False)
    cantidad_cartones = Column(Integer, nullable=False)
    importe_total = Column(Numeric(10, 2), nullable=False)
    qr_payload = Column(String, nullable=False, unique=True)
    medio_pago = Column(String(20), nullable=False, default="efectivo")
    cliente_nombre = Column(String(120), nullable=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow)

    operador = relationship("Operador")
    puesto = relationship("Puesto")
    cartones = relationship("Carton", back_populates="compra", order_by="Carton.orden")


class Carton(Base):
    __tablename__ = "cartones"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    compra_id = Column(String, ForeignKey("compras.id"), nullable=False)
    orden = Column(Integer, nullable=False)
    grilla = Column(String, nullable=False)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow)

    compra = relationship("Compra", back_populates="cartones")


class Sorteo(Base):
    __tablename__ = "sorteos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(120), nullable=False)
    estado = Column(Enum(EstadoSorteo), nullable=False, default=EstadoSorteo.abierto)
    modalidad = Column(String(30), nullable=False, default="libre")
    inicia_en = Column(DateTime, nullable=True)
    cierra_en = Column(DateTime, nullable=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow)


class TicketQr(Base):
    __tablename__ = "tickets_qr"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    compra_id = Column(String, ForeignKey("compras.id"), nullable=False)
    qr_payload = Column(String, nullable=False, unique=True)
    usado = Column(Boolean, nullable=False, default=False)
    validado_en = Column(DateTime, nullable=True)
    creado_en = Column(DateTime, default=datetime.datetime.utcnow)
