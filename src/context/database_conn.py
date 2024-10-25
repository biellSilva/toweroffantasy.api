from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from src._settings import config
from src.modules.base.table import BaseTable


class DatabaseConnection:
    """Database Connection Manager"""

    _engine: AsyncEngine | None = None

    @staticmethod
    def get_engine() -> AsyncEngine:
        """Get the engine."""
        if DatabaseConnection._engine is None:
            return DatabaseConnection.create_engine()
        return DatabaseConnection._engine

    @staticmethod
    async def close_engine() -> None:
        """Close the engine."""
        if DatabaseConnection._engine is not None:
            await DatabaseConnection._engine.dispose()
            DatabaseConnection._engine = None

    @staticmethod
    def create_engine() -> AsyncEngine:
        """Create the engine."""
        if DatabaseConnection._engine is not None:
            err_msg = (
                "AsyncEngine is already set. "
                "Use `PostgreSqlConnection.get_engine()` to get the engine."
            )
            raise ValueError(err_msg)

        if config.ENV == "test":
            DatabaseConnection._engine = create_async_engine(config.DB_URL)
            return DatabaseConnection._engine

        DatabaseConnection._engine = create_async_engine(
            config.DB_URL,
            pool_size=20,
            max_overflow=10,
            pool_recycle=3600,
            pool_pre_ping=True,
        )
        return DatabaseConnection._engine

    @staticmethod
    async def create_all() -> None:
        """Create all tables."""
        engine = DatabaseConnection.get_engine()

        async with engine.begin() as async_conn:
            await async_conn.run_sync(BaseTable.metadata.create_all)

    @staticmethod
    async def drop_all() -> None:
        """Drop all tables."""
        if config.ENV == "prod":
            return

        engine = DatabaseConnection.get_engine()

        async with engine.begin() as async_conn:
            await async_conn.run_sync(BaseTable.metadata.drop_all)

    @staticmethod
    def session_maker() -> async_sessionmaker[AsyncSession]:
        """Get the session maker."""
        return async_sessionmaker(
            DatabaseConnection.get_engine(),
            expire_on_commit=False,
        )
