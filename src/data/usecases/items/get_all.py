from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.items import Item
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.items.get_all import IGetAllItemsUseCase
from src.infra.repository.items.global_ import ItemsGlobalRepository


class GetAllItemsUseCase(IGetAllItemsUseCase):

    def __init__(self, repository: ItemsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Item]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
