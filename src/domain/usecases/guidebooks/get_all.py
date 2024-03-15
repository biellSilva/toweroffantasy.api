from abc import ABC, abstractmethod

from src.domain.models.guidebook import GuideBook
from src.domain.usecases.base import GetAllParams, IUsecase


class IGetAllGuidebooksUseCase(IUsecase[GetAllParams, GuideBook], ABC):
    @abstractmethod
    async def execute(self, params: GetAllParams) -> list[GuideBook]: ...
