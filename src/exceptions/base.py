from typing import TYPE_CHECKING, Any

from fastapi.responses import JSONResponse

if TYPE_CHECKING:
    from fastapi import Request


class ApiError(Exception):
    """Base class for API exceptions."""

    def __init__(
        self,
        *,
        message: str = "Internal Server Error",
        status_code: int = 500,
        **metadata: Any,
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.metadata = metadata
        super().__init__(f"STATUS CODE: {status_code} - MESSAGE: {message}")

    @staticmethod
    async def handle_error(_: "Request", exc: "ApiError") -> JSONResponse:
        return JSONResponse(
            {
                "className": exc.__class__.__name__,
                "message": exc.message,
                "statusCode": exc.status_code,
                "metadata": exc.metadata,
            },
            status_code=exc.status_code,
        )
