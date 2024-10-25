from typing import TYPE_CHECKING, Any, TypeVar

from src.context.database_conn import DatabaseConnection
from src.modules.base.table import BaseTable

if TYPE_CHECKING:
    from sqlalchemy import Delete, ScalarResult, Select

_T = TypeVar("_T", bound=Any)
_M = TypeVar("_M", bound=BaseTable)


class BaseRepository:
    _session = DatabaseConnection.session_maker()

    async def _execute_query(self, query: "Select[tuple[_T]]") -> "ScalarResult[_T]":
        """Helper method to execute a query and return the result."""
        async with self._session() as session:
            result = await session.execute(query)
            return result.scalars()

    async def _save(self, model: _M) -> _M:
        """Saves a model."""
        async with self._session() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        return model

    async def _delete(self, statement: "Delete") -> None:
        """Deletes a record."""
        async with self._session() as session:
            await session.execute(statement)
            await session.commit()
