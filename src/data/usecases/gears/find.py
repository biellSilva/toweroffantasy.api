from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.gears import Gear
from src.domain.usecases.base import FindParams
from src.domain.usecases.gears.find import IFindGearsUseCase
from src.infra.repository.gears.global_ import GearsGlobalRepository


class FindGearsUseCase(IFindGearsUseCase):
    def __init__(self, repository: GearsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindParams) -> Gear:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
