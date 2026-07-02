from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update

from backend.core.database import async_session
from backend.core.models import Compra, Carton, Sorteo, TicketQr
from backend.core.config import settings
from backend.core import types


def _now() -> datetime:
    return datetime.utcnow()


def _build_qr_payload(compra_id: str, issued_at: datetime, expiry: datetime) -> str:
    import hashlib, hmac, json, secrets
    body = json.dumps(
        {
            "compra_id": compra_id,
            "iss": settings.qr_issuer,
            "iat": int(issued_at.timestamp()),
            "exp": int(expiry.timestamp()),
            "jti": secrets.token_hex(6),
        },
        separators=(",", ":"),
    )
    sig = hmac.new(settings.secret_key.encode(), body.encode(), hashlib.sha256).hexdigest()
    return f"{body}.{sig}"


async def create_compra(command: types.CompraCommand) -> Compra:
    async with async_session() as session:
        issued_at = _now()
        expiry = issued_at + timedelta(days=settings.audit_retention_days)
        qr = _build_qr_payload("pending", issued_at, expiry)

        compra = Compra(
            operador_id=command.operador_id,
            puesto_id=command.puesto_id,
            cantidad_cartones=command.cantidad_cartones,
            importe_total=command.importe_total,
            qr_payload=qr,
            medio_pago=command.medio_pago,
            cliente_nombre=command.cliente_nombre,
        )
        session.add(compra)
        await session.flush()

        compra.qr_payload = _build_qr_payload(compra.id, issued_at, expiry)

        for orden in range(1, command.cantidad_cartones + 1):
            session.add(Carton(compra_id=compra.id, orden=orden, grilla=_build_grilla()))

        session.add(TicketQr(compra_id=compra.id, qr_payload=compra.qr_payload))
        await session.commit()
        await session.refresh(compra)
        return compra


async def get_compra(compra_id: str) -> Optional[Compra]:
    async with async_session() as session:
        result = await session.execute(select(Compra).where(Compra.id == compra_id))
        return result.scalar_one_or_none()


async def validate_qr(qr_payload_in: str) -> Optional[TicketQr]:
    async with async_session() as session:
        result = await session.execute(select(TicketQr).where(TicketQr.qr_payload == qr_payload_in))
        ticket = result.scalar_one_or_none()
        if not ticket:
            return None
        if ticket.usado:
            return ticket
        ticket.usado = True
        ticket.validado_en = _now()
        await session.commit()
        await session.refresh(ticket)
        return ticket


async def create_sorteo(command: types.SorteoCommand) -> Sorteo:
    async with async_session() as session:
        sorteo = Sorteo(nombre=command.nombre, estado="abierto", modalidad=command.modalidad)
        session.add(sorteo)
        await session.commit()
        await session.refresh(sorteo)
        return sorteo


def _build_grilla() -> str:
    import secrets
    return secrets.token_hex(16)
