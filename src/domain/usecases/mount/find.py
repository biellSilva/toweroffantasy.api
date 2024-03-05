
from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.domain.models.mounts import Mount

from src.domain.usecases.base import IUsecase


class FindMountParams(BaseModel):
    id: str
    version: str
    lang: str


class IFindMountUseCase(IUsecase[FindMountParams, Mount], ABC):
    @abstractmethod
    async def execute(self, params: FindMountParams) -> Mount: ...


