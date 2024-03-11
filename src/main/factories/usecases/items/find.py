from src.data.usecases.items.find import FindItemsUseCase
from src.infra.repository.items.global_ import ItemsGlobalRepository


class FindItemsUsecaseFactory:

    @staticmethod
    def create() -> FindItemsUseCase:
        return FindItemsUseCase(ItemsGlobalRepository())
