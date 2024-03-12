from src.decorators.filter import filter_models
from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.food import Food
from src.domain.usecases.food.get_all import GetAllFoodParams, IGetAllFoodUseCase
from src.infra.repository.food.global_ import FoodGlobalRepository


class GetAllFoodUseCase(IGetAllFoodUseCase):
    def __init__(self, repository: FoodGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllFoodParams) -> list[Food]:
        if params.version == "global":
            models = await self.repository.get_all(**params.model_dump())

        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr

        return filter_models(models, params.filter)
