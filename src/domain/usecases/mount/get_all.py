from abc import ABC, abstractmethod

from src.domain.models.mounts import Mount
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllMountUseCase(IUsecase[GetAllParams, Mount], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Mount]: ...
