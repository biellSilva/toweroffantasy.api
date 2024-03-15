from abc import ABC, abstractmethod

from src.domain.models.guidebook import GuideBook
from src.domain.usecases.base import FindParams, IUsecase


class IFindGuidebooksUseCase(IUsecase[FindParams, GuideBook], ABC):
    @abstractmethod
    async def execute(self, params: FindParams) -> GuideBook: ...
