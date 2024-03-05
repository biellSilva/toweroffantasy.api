from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.mounts import Mount
from src.domain.usecases.mount.get_all import GetAllMountParams, IGetAllMountUseCase
from src.infra.repository.mounts.global_ import MountsGlobalRepository


class GetAllMountUseCase(IGetAllMountUseCase):
    def __init__(self, repository: MountsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllMountParams) -> list[Mount]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
