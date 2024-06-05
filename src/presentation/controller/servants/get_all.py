from src.domain.models.servants import SmartServant
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.servants.get_all import IGetAllServantsUseCase


class GetAllServantsController:
    def __init__(self, usecase: IGetAllServantsUseCase):
        self.usecase = usecase

    async def handle(
        self,
        version: str = "global",
        lang: str = "en",
        filter: str | None = None,
        limit: int | None = None,
    ) -> list[SmartServant]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter, limit=limit)
        )
