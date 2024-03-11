from src.main.factories.usecases.items.find import FindItemsUsecaseFactory
from src.presentation.controller.items.find import FindItemsController


class FindItemsControllerFactory:

    @staticmethod
    def create() -> FindItemsController:
        return FindItemsController(FindItemsUsecaseFactory.create())
