from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from src.context.database_conn import DatabaseConnection

if TYPE_CHECKING:
    from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_: "FastAPI") -> AsyncGenerator[None, None]:
    """Application lifespan event."""

    await DatabaseConnection.create_all()

    yield

    await DatabaseConnection.close_engine()
