from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.relics import Relic
from src.domain.usecases.relics.find import (
    FindRelicsParams,
    IFindRelicsUseCase,
)
from src.infra.repository.relics.global_ import RelicsGlobalRepository


class FindRelicsUseCase(IFindRelicsUseCase):
    def __init__(self, repository: RelicsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindRelicsParams) -> Relic:
        if params.version == "global":
            if data := await self.repository.find_by_id(
                **params.model_dump(exclude={"version"})
            ):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
