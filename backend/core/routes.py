from fastapi import APIRouter

from backend.core.health import router as health_router
from backend.core.routes import router as domain_router

router = APIRouter()
router.include_router(health_router)
router.include_router(domain_router)
