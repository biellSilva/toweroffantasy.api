from abc import ABC, abstractmethod

from src.domain.models.researchs import Research
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllResearchsUseCase(IUsecase[GetAllParams, Research], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[Research]: ...
