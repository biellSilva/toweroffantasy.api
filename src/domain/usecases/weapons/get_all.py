from abc import ABC, abstractmethod

from src.domain.models.weapons import Weapon
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllWeaponsUseCase(IUsecase[GetAllParams, Weapon], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Weapon]: ...
