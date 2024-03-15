from abc import ABC, abstractmethod

from src.domain.models.gears import Gear
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllGearsUseCase(IUsecase[GetAllParams, Gear], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Gear]: ...
