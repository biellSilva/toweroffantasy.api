
from src.presentation.controller.mount.get_all import GetAllMountController
from src.main.factories.usecases.mount.get_all import GetAllMountUsecaseFactory

class GetAllMountControllerFactory:

    @staticmethod
    def create() -> GetAllMountController:
        return GetAllMountController(
            GetAllMountUsecaseFactory.create()
        )


