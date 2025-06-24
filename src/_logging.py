from typing import TYPE_CHECKING

from src._settings import config

if TYPE_CHECKING:
    from fastapi import FastAPI


def setup_logfire(app: "FastAPI") -> None:
    """
    Setup logfire for logging.
    """

    import logfire

    logfire.configure(
        token=config.LOGFIRE_TOKEN,
        environment=config.ENV,
    )
    logfire.instrument_fastapi(app=app, capture_headers=True, record_send_receive=True)
    logfire.instrument_system_metrics()
