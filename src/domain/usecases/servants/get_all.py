from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.servants import SmartServant
from src.domain.usecases.base import IUsecase


class GetAllServantsParams(BaseModel):
    version: str
    lang: str


class IGetAllServantsUseCase(IUsecase[GetAllServantsParams, SmartServant], ABC):
    @abstractmethod
    async def execute(self, params: GetAllServantsParams) -> list[SmartServant]: ...
