import json

from src.domain.models.mounts import Mount
from src.domain.usecases.mount.get_all import GetAllMountParams, IGetAllMountUseCase


class GetAllMountController:
    def __init__(self, usecase: IGetAllMountUseCase):
        self.usecase = usecase

    async def handle(
        self, version: str = "global", lang: str = "en", filter: str = ""
    ) -> list[Mount]:
        return await self.usecase.execute(
            GetAllMountParams(
                version=version, lang=lang, filter=json.loads(filter) if filter else {}
            )
        )
