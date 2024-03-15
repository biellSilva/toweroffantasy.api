from abc import ABC, abstractmethod

from fastapi import Query
from pydantic import BaseModel

from src.domain.models.banner import Banner
from src.domain.usecases.base import IUsecase


class FindBannersParams(BaseModel):
    id: str | None = Query(None, description="Object id")  # type: ignore (override id type)
    version: str = Query("global", description="Game Version")
    filter: str | None = Query(None, description="Filter string")


class IFindBannersUseCase(IUsecase[FindBannersParams, Banner], ABC):
    @abstractmethod
    async def execute(self, params: FindBannersParams) -> list[Banner]: ...
