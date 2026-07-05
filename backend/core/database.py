from __future__ import annotations

import os
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from backend.core.config import settings


class Base(DeclarativeBase):
    pass


def _build_engine() -> AsyncEngine:
    url = (
        os.environ.get("DATABASE_URL")
        or getattr(settings, "database_url", None)
        or "sqlite+aiosqlite:///.pytest-sqlite.db"
    )
    return create_async_engine(url, echo=False, future=True)


_engine: Optional[AsyncEngine] = None


def get_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        _engine = _build_engine()
    return _engine


engine = get_engine()
async_session = async_sessionmaker(engine, expire_on_commit=False)


def now() -> "datetime.datetime":
    import datetime

    return datetime.datetime.utcnow()
