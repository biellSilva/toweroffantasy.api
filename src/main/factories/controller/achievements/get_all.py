from src.main.factories.usecases.achievements.get_all import (
    GetAllAchievementsUsecaseFactory,
)
from src.presentation.controller.achievements.get_all import (
    GetAllAchievementsController,
)


class GetAllAchievementsControllerFactory:

    @staticmethod
    def create() -> GetAllAchievementsController:
        return GetAllAchievementsController(GetAllAchievementsUsecaseFactory.create())
