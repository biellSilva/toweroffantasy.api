from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.banner import Banner
from src.domain.usecases.base import IUsecase


class FindBannersParams(BaseModel):
    id: str | None
    version: str


class IFindBannersUseCase(IUsecase[FindBannersParams, Banner], ABC):
    @abstractmethod
    async def execute(self, params: FindBannersParams) -> list[Banner]: ...
