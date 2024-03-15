from abc import ABC, abstractmethod

from src.domain.models.servants import SmartServant
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllServantsUseCase(IUsecase[GetAllParams, SmartServant], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[SmartServant]: ...
