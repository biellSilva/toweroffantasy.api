from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.guidebook import GuideBook
from src.domain.usecases.guidebooks.get_all import (
    GetAllGuidebooksParams,
    IGetAllGuidebooksUseCase,
)
from src.infra.repository.guidebooks.global_ import GuidebooksGlobalRepository


class GetAllGuidebooksUseCase(IGetAllGuidebooksUseCase):
    def __init__(self, repository: GuidebooksGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllGuidebooksParams) -> list[GuideBook]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
