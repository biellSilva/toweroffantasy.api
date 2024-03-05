from src.domain.models.mounts import Mount
from src.domain.usecases.mount.find import FindMountParams, IFindMountUseCase


class FindMountController:
    def __init__(self, usecase: IFindMountUseCase):
        self.usecase = usecase

    async def handle(self, id: str, version: str = "global", lang: str = "en") -> Mount:
        return await self.usecase.execute(
            FindMountParams(id=id, version=version, lang=lang)
        )
