from typing import Any

from src.exceptions.base import ApiError
from src.exceptions.unauthorized import (
    ExpiredTokenError,
    InvalidTokenError,
    MissingTokenError,
)


def generate_docs(
    *excs: type[ApiError] | ApiError,
    auth: bool = False,
) -> dict[Any, Any]:
    """Generate docs for exception.

    Args:
        excs (type[ApiError] | ApiError): Exception class or instance.
        auth (bool): Authentication flags.
    """
    docs: dict[Any, Any] = {}

    if auth:
        excs = (*excs, MissingTokenError, ExpiredTokenError, InvalidTokenError)

    for exc in excs:
        if not isinstance(exc, ApiError):
            exc = exc()  # noqa: PLW2901

        if exc.status_code not in docs:
            docs[exc.status_code] = {
                "content": {
                    "application/json": {
                        "examples": {
                            exc.__class__.__name__: {
                                "value": exc.example(),
                            },
                        },
                    },
                },
            }

        else:
            docs[exc.status_code]["content"]["application/json"]["examples"][
                exc.__class__.__name__
            ] = {
                "value": exc.example(),
            }

    return docs
