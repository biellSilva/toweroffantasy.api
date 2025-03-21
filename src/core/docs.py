from typing import Any

from src.exceptions.base import ApiError


def generate_docs(*excs: type[ApiError] | ApiError) -> dict[Any, Any]:
    """Generate docs for exception.

    Args:
        excs (type[ApiError] | ApiError): Exception class or instance.
    """
    docs: dict[Any, Any] = {}
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
