from src.main.factories.usecases.mount.find import FindMountUsecaseFactory
from src.presentation.controller.mount.find import FindMountController


class FindMountControllerFactory:

    @staticmethod
    def create() -> FindMountController:
        return FindMountController(FindMountUsecaseFactory.create())
