from src.domain.errors.http import NotFoundErr, NotImplementedErr, VersionNotFoundErr
from src.domain.models.items import Item
from src.domain.usecases.items.find import FindItemsParams, IFindItemsUseCase
from src.infra.repository.items.global_ import ItemsGlobalRepository


class FindItemsUseCase(IFindItemsUseCase):
    def __init__(self, repository: ItemsGlobalRepository) -> None:
        self.repository = repository

    async def execute(self, params: FindItemsParams) -> Item:
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
