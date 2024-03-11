from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.food import Food
from src.domain.usecases.food.find import FindFoodParams, IFindFoodUseCase
from src.infra.repository.food.global_ import FoodGlobalRepository


class FindFoodUseCase(IFindFoodUseCase):
    def __init__(self, repository: FoodGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindFoodParams) -> Food:
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
