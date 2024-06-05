from src.domain.models.mounts import Mount
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.mount.get_all import IGetAllMountUseCase


class GetAllMountController:
    def __init__(self, usecase: IGetAllMountUseCase):
        self.usecase = usecase

    async def handle(
        self,
        version: str = "global",
        lang: str = "en",
        filter: str | None = None,
        limit: int | None = None,
    ) -> list[Mount]:
        return await self.usecase.execute(
            GetAllParams(version=version, lang=lang, filter=filter, limit=limit)
        )
