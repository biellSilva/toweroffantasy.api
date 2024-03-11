from src.main.factories.usecases.servants.get_all import GetAllServantsUsecaseFactory
from src.presentation.controller.servants.get_all import GetAllServantsController


class GetAllServantsControllerFactory:

    @staticmethod
    def create() -> GetAllServantsController:
        return GetAllServantsController(GetAllServantsUsecaseFactory.create())
