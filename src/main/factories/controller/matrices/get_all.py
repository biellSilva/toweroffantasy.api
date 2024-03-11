from src.main.factories.usecases.matrices.get_all import GetAllMatricesUsecaseFactory
from src.presentation.controller.matrices.get_all import GetAllMatricesController


class GetAllMatricesControllerFactory:

    @staticmethod
    def create() -> GetAllMatricesController:
        return GetAllMatricesController(GetAllMatricesUsecaseFactory.create())
