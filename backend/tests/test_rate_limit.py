import asyncio
import time

import pytest

from backend.core.rate_limit import RateLimitMiddleware


class FakeRequest:
    def __init__(self, client_host="127.0.0.1"):
        self.client = type("Client", (), {"host": client_host})()


class FakeCallNext:
    def __init__(self, responses):
        self._responses = responses
        self.calls = 0

    async def __call__(self, request):
        response = self._responses[min(self.calls, len(self._responses) - 1)] if self._responses else None
        self.calls += 1
        return response


def test_rate_limit_blocks_after_max_requests():
    middleware = RateLimitMiddleware(None, window_seconds=60, max_requests=2)
    request = FakeRequest()
    responses = [
        type("Response", (), {"status_code": 200})(),
        type("Response", (), {"status_code": 200})(),
        type("Response", (), {"status_code": 200})(),
    ]
    call_next = FakeCallNext(responses)

    result = asyncio.get_event_loop().run_until_complete(middleware.dispatch(request, call_next))
    assert result.status_code == 200
    assert call_next.calls == 1

    result = asyncio.get_event_loop().run_until_complete(middleware.dispatch(request, call_next))
    assert result.status_code == 200
    assert call_next.calls == 2

    result = asyncio.get_event_loop().run_until_complete(middleware.dispatch(request, call_next))
    assert result.status_code == 429
    assert result.body == b"Rate limit exceeded"


def test_rate_limit_does_not_block_after_window_reset():
    middleware = RateLimitMiddleware(None, window_seconds=60, max_requests=2)
    request = FakeRequest()
    responses = [type("Response", (), {"status_code": 200})()]
    call_next = FakeCallNext(responses)

    asyncio.get_event_loop().run_until_complete(middleware.dispatch(request, call_next))
    asyncio.get_event_loop().run_until_complete(middleware.dispatch(request, call_next))

    middleware._hits[request.client.host].clear()
    result = asyncio.get_event_loop().run_until_complete(middleware.dispatch(request, call_next))
    assert result.status_code == 200
