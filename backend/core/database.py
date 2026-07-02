from __future__ import annotations

import datetime
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from backend.core.config import settings


class Base(DeclarativeBase):
    pass


def _build_engine() -> AsyncEngine:
    url = settings.database_url
    if not url:
        raise RuntimeError("DATABASE_URL missing")
    return create_async_engine(url, echo=False, future=True)


_engine: Optional[AsyncEngine] = None


def get_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        _engine = _build_engine()
    return _engine


async_session = async_sessionmaker(expire_on_commit=False)


def now() -> datetime.datetime:
    return datetime.datetime.utcnow()
