from src.decorators.filter import filter_models
from src.domain.errors.http import VersionNotFoundErr
from src.domain.models.banner import Banner
from src.domain.usecases.banners.find import FindBannersParams, IFindBannersUseCase
from src.infra.repository.banners.china import BannersChinaRepository
from src.infra.repository.banners.global_ import BannersGlobalRepository


class FindBannersUseCase(IFindBannersUseCase):
    def __init__(
        self,
        repository: BannersGlobalRepository,
        repository_china: BannersChinaRepository,
    ) -> None:
        self.repository = repository
        self.repository_china = repository_china

    async def execute(self, params: FindBannersParams) -> list[Banner]:
        if params.version == "global":
            if not params.id:
                models = await self.repository.get_all(**params.model_dump())

            else:
                models = await self.repository.find_by_id(**params.model_dump())

        elif params.version == "china":
            if not params.id:
                models = await self.repository_china.get_all(**params.model_dump())

            else:
                models = await self.repository_china.find_by_id(**params.model_dump())

        else:
            raise VersionNotFoundErr

        return await filter_models(models, params.filter)
