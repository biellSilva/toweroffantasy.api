from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.mounts import Mount
from src.domain.usecases.base import IUsecase


class GetAllMountParams(BaseModel):
    version: str
    lang: str


class IGetAllMountUseCase(IUsecase[GetAllMountParams, Mount], ABC):
    @abstractmethod
    async def execute(self, params: GetAllMountParams) -> list[Mount]: ...
