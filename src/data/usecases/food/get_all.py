from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.food import Food
from src.domain.usecases.base import GetAllParams
from src.domain.usecases.food.get_all import IGetAllFoodUseCase
from src.infra.repository.food.global_ import FoodGlobalRepository


class GetAllFoodUseCase(IGetAllFoodUseCase):
    def __init__(self, repository: FoodGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllParams) -> list[Food]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        models = await filter_models(models=models, filter_str=params.filter)
        return models[: params.limit] if params.limit else models
