
from src.presentation.controller.banners.find import FindBannersController
from src.main.factories.usecases.banners.find import FindBannersUsecaseFactory

class FindBannersControllerFactory:

    @staticmethod
    def create() -> FindBannersController:
        return FindBannersController(
            FindBannersUsecaseFactory.create()
        )


