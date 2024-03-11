from src.data.usecases.items.get_all import GetAllItemsUseCase
from src.infra.repository.items.global_ import ItemsGlobalRepository


class GetAllItemsUsecaseFactory:

    @staticmethod
    def create() -> GetAllItemsUseCase:
        return GetAllItemsUseCase(ItemsGlobalRepository())
