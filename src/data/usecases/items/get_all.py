from src.domain.errors.http import NotImplementedErr, VersionNotFoundErr
from src.domain.models.items import Item
from src.domain.usecases.items.get_all import GetAllItemsParams, IGetAllItemsUseCase
from src.infra.repository.items.global_ import ItemsGlobalRepository


class GetAllItemsUseCase(IGetAllItemsUseCase):

    def __init__(self, repository: ItemsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: GetAllItemsParams) -> list[Item]:
        if params.version == "global":
            return await self.repository.get_all(
                **params.model_dump(exclude={"version"})
            )
        elif params.version == "china":
            raise NotImplementedErr

        else:
            raise VersionNotFoundErr
