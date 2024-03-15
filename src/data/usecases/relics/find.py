from src.domain.errors.http import NotFoundErr, VersionNotFoundErr
from src.domain.models.relics import Relic
from src.domain.usecases.base import FindParams
from src.domain.usecases.relics.find import IFindRelicsUseCase
from src.infra.repository.relics.china import RelicsChinaRepository
from src.infra.repository.relics.global_ import RelicsGlobalRepository


class FindRelicsUseCase(IFindRelicsUseCase):
    def __init__(
        self,
        repository: RelicsGlobalRepository,
        china_repository: RelicsChinaRepository,
    ) -> None:
        self.repository = repository
        self.china_repository = china_repository

    async def execute(self, params: FindParams) -> Relic:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            if data := await self.china_repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        else:
            raise VersionNotFoundErr
