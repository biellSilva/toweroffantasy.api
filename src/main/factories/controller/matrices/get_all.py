
from src.presentation.controller.matrices.get_all import GetAllMatricesController
from src.main.factories.usecases.matrices.get_all import GetAllMatricesUsecaseFactory

class GetAllMatricesControllerFactory:

    @staticmethod
    def create() -> GetAllMatricesController:
        return GetAllMatricesController(
            GetAllMatricesUsecaseFactory.create()
        )


