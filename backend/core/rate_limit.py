import time
from collections import defaultdict
from starlette.middleware.base import BaseHTTPMiddleware

from backend.core.config import settings


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, *, window_seconds: int = 60, max_requests: int = 120):
        super().__init__(app)
        self.window_seconds = window_seconds
        self.max_requests = max_requests
        self._hits: dict[str, list[float]] = defaultdict(list)

    async def dispatch(self, request, call_next):
        client_host = request.client.host if request.client else "anon"
        now = time.time()
        window = self._hits[client_host]
        cutoff = now - self.window_seconds
        while window and window[0] < cutoff:
            window.pop(0)
        if len(window) >= self.max_requests:
            from fastapi import Response
            return Response("Rate limit exceeded", status_code=429, media_type="text/plain")
        window.append(now)
        return await call_next(request)


def build_rate_limit_middleware(app) -> RateLimitMiddleware:
    return RateLimitMiddleware(
        app,
        window_seconds=settings.jwt_access_ttl * 60 or 60,
        max_requests=120,
    )
