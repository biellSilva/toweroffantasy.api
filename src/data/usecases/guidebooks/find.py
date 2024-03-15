from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.guidebook import GuideBook
from src.domain.usecases.base import FindParams
from src.domain.usecases.guidebooks.find import IFindGuidebooksUseCase
from src.infra.repository.guidebooks.global_ import GuidebooksGlobalRepository


class FindGuidebooksUseCase(IFindGuidebooksUseCase):
    def __init__(self, repository: GuidebooksGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindParams) -> GuideBook:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
