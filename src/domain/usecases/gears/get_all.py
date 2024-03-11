from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.domain.models.gears import Gear
from src.domain.usecases.base import IUsecase


class GetAllGearsParams(BaseModel):
    version: str
    lang: str


class IGetAllGearsUseCase(IUsecase[GetAllGearsParams, Gear], ABC):
    @abstractmethod
    async def execute(self, params: GetAllGearsParams) -> list[Gear]: ...
