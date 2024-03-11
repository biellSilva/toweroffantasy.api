from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.outfits import Outfit
from src.domain.usecases.outfits.get_all import (
    GetAllOutfitsParams,
    IGetAllOutfitsUseCase,
)
from src.infra.repository.outifts.global_ import OutfitsGlobalRepository


class GetAllOutfitsUseCase(IGetAllOutfitsUseCase):
    def __init__(self, repository: OutfitsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllOutfitsParams) -> list[Outfit]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
