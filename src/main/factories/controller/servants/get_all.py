
from src.presentation.controller.servants.get_all import GetAllServantsController
from src.main.factories.usecases.servants.get_all import GetAllServantsUsecaseFactory

class GetAllServantsControllerFactory:

    @staticmethod
    def create() -> GetAllServantsController:
        return GetAllServantsController(
            GetAllServantsUsecaseFactory.create()
        )


