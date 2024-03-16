from abc import ABC, abstractmethod

from src.domain.models.researchs import Research
from src.domain.usecases.base import FindParams, IUsecase


class IFindResearchsUseCase(IUsecase[FindParams, Research], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> Research: ...
