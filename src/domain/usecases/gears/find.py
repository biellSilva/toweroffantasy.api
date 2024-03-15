from abc import ABC, abstractmethod

from src.domain.models.gears import Gear
from src.domain.usecases.base import FindParams, IUsecase


class IFindGearsUseCase(IUsecase[FindParams, Gear], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Gear: ...
