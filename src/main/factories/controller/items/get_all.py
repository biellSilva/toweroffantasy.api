from src.main.factories.usecases.items.get_all import GetAllItemsUsecaseFactory
from src.presentation.controller.items.get_all import GetAllItemsController


class GetAllItemsControllerFactory:

    @staticmethod
    def create() -> GetAllItemsController:
        return GetAllItemsController(GetAllItemsUsecaseFactory.create())
