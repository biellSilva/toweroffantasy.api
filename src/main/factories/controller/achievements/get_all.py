
from src.presentation.controller.achievements.get_all import GetAllAchievementsController
from src.main.factories.usecases.achievements.get_all import GetAllAchievementsUsecaseFactory

class GetAllAchievementsControllerFactory:

    @staticmethod
    def create() -> GetAllAchievementsController:
        return GetAllAchievementsController(
            GetAllAchievementsUsecaseFactory.create()
        )


