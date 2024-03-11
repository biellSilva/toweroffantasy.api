from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.outfits import Outfit
from src.domain.usecases.outfits.find import FindOutfitsParams, IFindOutfitsUseCase
from src.infra.repository.outifts.global_ import OutfitsGlobalRepository


class FindOutfitsUseCase(IFindOutfitsUseCase):
    def __init__(self, repository: OutfitsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindOutfitsParams) -> Outfit:
        if params.version == "global":
            if data := await self.repository.find_by_id(
                **params.model_dump(exclude={"version"})
            ):
                return data
            raise NotFoundErr

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
