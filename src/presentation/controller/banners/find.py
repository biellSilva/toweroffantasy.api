from src.domain.models.banner import Banner
from src.domain.usecases.banners.find import FindBannersParams, IFindBannersUseCase


class FindBannersController:
    def __init__(self, usecase: IFindBannersUseCase):
        self.usecase = usecase

    async def handle(
        self, id: str | None = None, version: str = "global"
    ) -> list[Banner]:
        return await self.usecase.execute(FindBannersParams(id=id, version=version))
