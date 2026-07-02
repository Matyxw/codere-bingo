from __future__ import annotations

import datetime
import hashlib
import hmac
import json
import os
import secrets
from typing import Optional

from sqlalchemy import select, insert, update

from backend.core.config import settings
from backend.core.database import get_engine
from backend.core import types


def _now() -> datetime.datetime:
    return datetime.datetime.utcnow()


def _build_qr_payload(compra_id: str, issued_at: datetime.datetime, expiry: datetime.datetime) -> str:
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


async def create_compra(command: types.CompraCommand) -> dict:
    engine = get_engine()
    issued_at = _now()
    expiry = issued_at + datetime.timedelta(days=settings.audit_retention_days)
    qr = _build_qr_payload("pending", issued_at, expiry)

    compra_id = secrets.token_hex(16)
    async with engine.begin() as conn:
        await conn.execute(
            insert(Compra)
            .values(
                id=compra_id,
                operador_id=command.operador_id,
                puesto_id=command.puesto_id,
                cantidad_cartones=command.cantidad_cartones,
                importe_total=command.importe_total,
                qr_payload=qr,
                medio_pago=command.medio_pago,
                cliente_nombre=command.cliente_nombre,
                creado_en=issued_at,
            )
            .returning(Compra.id)
        )
        for orden in range(1, command.cantidad_cartones + 1):
            await conn.execute(
                insert(Carton).values(
                    compra_id=compra_id,
                    orden=orden,
                    grilla=secrets.token_hex(16),
                    creado_en=issued_at,
                )
            )
        await conn.execute(
            insert(TicketQr).values(compra_id=compra_id, qr_payload=qr, creado_en=issued_at)
        )

    qr = _build_qr_payload(compra_id, issued_at, expiry)
    async with engine.begin() as conn:
        await conn.execute(update(Compra).where(Compra.id == compra_id).values(qr_payload=qr))
    return {"id": compra_id, "qr_payload": qr, "cantidad_cartones": command.cantidad_cartones, "importe_total": command.importe_total, "medio_pago": command.medio_pago, "cliente_nombre": command.cliente_nombre, "creado_en": issued_at.isoformat()}


async def get_compra(compra_id: str) -> Optional[dict]:
    engine = get_engine()
    async with engine.begin() as conn:
        result = await conn.execute(select(Compra).where(Compra.id == compra_id))
        row = result.fetchone()
        if not row:
            return None
        return dict(row._mapping)


async def validate_qr(qr_payload_in: str) -> Optional[dict]:
    engine = get_engine()
    async with engine.begin() as conn:
        result = await conn.execute(select(TicketQr).where(TicketQr.qr_payload == qr_payload_in))
        row = result.fetchone()
        if not row:
            return None
        ticket = dict(row._mapping)
        if ticket.get("usado"):
            return ticket
        await conn.execute(update(TicketQr).where(TicketQr.id == ticket["id"]).values(usado=True, validado_en=_now()))
        ticket["usado"] = True
        ticket["validado_en"] = _now().isoformat()
        return ticket


async def create_sorteo(nombre: str, modalidad: str = "libre") -> dict:
    engine = get_engine()
    sorteo_id = secrets.token_hex(16)
    now = _now()
    async with engine.begin() as conn:
        await conn.execute(
            insert(Sorteo).values(id=sorteo_id, nombre=nombre, estado="abierto", modalidad=modalidad, creado_en=now)
        )
    return {"id": sorteo_id, "nombre": nombre, "estado": "abierto", "modalidad": modalidad, "creado_en": now.isoformat()}
