from time import time
from typing import Any, Awaitable, Callable, MutableMapping

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class ProcessTimerMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: Callable[
            [
                MutableMapping[str, Any],
                Callable[[], Awaitable[MutableMapping[str, Any]]],
                Callable[[MutableMapping[str, Any]], Awaitable[None]],
            ],
            Awaitable[None],
        ],
        dispatch: (
            Callable[
                [Request, Callable[[Request], Awaitable[Response]]], Awaitable[Response]
            ]
            | None
        ) = None,
    ) -> None:
        super().__init__(app, dispatch)

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:

        start_time = time()
        response: Response = await call_next(request)
        response.headers["X-Process-Time"] = str(time() - start_time)
        return response
