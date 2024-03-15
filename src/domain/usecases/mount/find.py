from abc import ABC, abstractmethod

from src.domain.models.mounts import Mount
from src.domain.usecases.base import FindParams, IUsecase


class IFindMountUseCase(IUsecase[FindParams, Mount], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Mount: ...
