from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.outfits import Outfit
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.outfits.get_all import IGetAllOutfitsUseCase
from src.infra.repository.outifts.global_ import OutfitsGlobalRepository


class GetAllOutfitsUseCase(IGetAllOutfitsUseCase):
    def __init__(self, repository: OutfitsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Outfit]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
