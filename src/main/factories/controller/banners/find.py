from src.main.factories.usecases.banners.find import FindBannersUsecaseFactory
from src.presentation.controller.banners.find import FindBannersController


class FindBannersControllerFactory:

    @staticmethod
    def create() -> FindBannersController:
        return FindBannersController(FindBannersUsecaseFactory.create())
