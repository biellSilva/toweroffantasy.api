from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.servants import SmartServant
from src.domain.usecases.base import FindParams
from src.domain.usecases.servants.find import IFindServantsUseCase
from src.infra.repository.servants.global_ import SmartServantsGlobalRepository


class FindServantsUseCase(IFindServantsUseCase):
    def __init__(self, repository: SmartServantsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindParams) -> SmartServant:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
