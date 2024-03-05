
from src.presentation.controller.mount.find import FindMountController
from src.main.factories.usecases.mount.find import FindMountUsecaseFactory

class FindMountControllerFactory:

    @staticmethod
    def create() -> FindMountController:
        return FindMountController(
            FindMountUsecaseFactory.create()
        )


