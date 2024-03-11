from src.main.factories.usecases.mount.get_all import GetAllMountUsecaseFactory
from src.presentation.controller.mount.get_all import GetAllMountController


class GetAllMountControllerFactory:

    @staticmethod
    def create() -> GetAllMountController:
        return GetAllMountController(GetAllMountUsecaseFactory.create())
