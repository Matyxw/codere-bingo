from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import settings
from backend.core.routes import router
from backend.core.middleware import SecurityHeadersMiddleware
from backend.core.rate_limit import RateLimitMiddleware

app = FastAPI(title="Codere Bingo")
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(
    RateLimitMiddleware,
    window_seconds=settings.jwt_access_ttl * 60 or 60,
    max_requests=120,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_origins] if settings.cors_origins != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
