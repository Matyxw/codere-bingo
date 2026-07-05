import time
from collections import defaultdict

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from backend.core.config import settings


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, *, window_seconds: int = 60, max_requests: int = 120):
        super().__init__(app)
        self.window_seconds = window_seconds
        self.max_requests = max_requests
        self._hits: dict[str, list[float]] = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_host = request.client.host if request.client else "anon"
        now = time.time()
        window = self._hits[client_host]
        cutoff = now - self.window_seconds
        while window and window[0] < cutoff:
            window.pop(0)
        if len(window) >= self.max_requests:
            from fastapi.responses import PlainTextResponse

            return PlainTextResponse("Rate limit exceeded", status_code=429)
        window.append(now)
        return await call_next(request)
