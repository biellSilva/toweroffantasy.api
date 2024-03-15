from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.mounts import Mount
from src.domain.usecases.base import FindParams
from src.domain.usecases.mount.find import IFindMountUseCase
from src.infra.repository.mounts.global_ import MountsGlobalRepository


class FindMountUseCase(IFindMountUseCase):
    def __init__(self, repository: MountsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindParams) -> Mount:
        if params.version == "global":
            if data := await self.repository.find_by_id(**params.model_dump()):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
