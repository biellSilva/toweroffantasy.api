from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.banner import Banner
from src.domain.usecases.banners.find import FindBannersParams, IFindBannersUseCase
from src.infra.repository.banners.global_ import BannersGlobalRepository


class FindBannersUseCase(IFindBannersUseCase):
    def __init__(self, repository: BannersGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindBannersParams) -> list[Banner]:
        if params.version == "global":
            if not params.id:
                return await self.repository.get_all(
                    **params.model_dump(exclude={"version", "id"})
                )
            return await self.repository.find_by_id(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
