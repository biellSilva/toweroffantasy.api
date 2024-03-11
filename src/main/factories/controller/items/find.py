
from src.presentation.controller.items.find import FindItemsController
from src.main.factories.usecases.items.find import FindItemsUsecaseFactory

class FindItemsControllerFactory:

    @staticmethod
    def create() -> FindItemsController:
        return FindItemsController(
            FindItemsUsecaseFactory.create()
        )


