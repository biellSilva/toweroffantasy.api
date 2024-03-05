from src.main.factories.usecases.matrices.find import FindMatricesUsecaseFactory
from src.presentation.controller.matrices.find import FindMatricesController


class FindMatricesControllerFactory:

    @staticmethod
    def create() -> FindMatricesController:
        return FindMatricesController(FindMatricesUsecaseFactory.create())
