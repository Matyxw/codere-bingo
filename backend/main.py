from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import settings
from backend.core.routes import router
from backend.core.middleware import SecurityHeadersMiddleware
from backend.core.rate_limit import build_rate_limit_middleware

app = FastAPI(title="Codere Bingo")
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(build_rate_limit_middleware(app=app))
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_origins] if settings.cors_origins != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
