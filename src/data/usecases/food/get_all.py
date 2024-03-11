from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.food import Food
from src.domain.usecases.food.get_all import GetAllFoodParams, IGetAllFoodUseCase
from src.infra.repository.food.global_ import FoodGlobalRepository


class GetAllFoodUseCase(IGetAllFoodUseCase):
    def __init__(self, repository: FoodGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllFoodParams) -> list[Food]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
