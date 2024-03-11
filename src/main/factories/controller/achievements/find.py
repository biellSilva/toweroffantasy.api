
from src.presentation.controller.achievements.find import FindAchievementsController
from src.main.factories.usecases.achievements.find import FindAchievementsUsecaseFactory

class FindAchievementsControllerFactory:

    @staticmethod
    def create() -> FindAchievementsController:
        return FindAchievementsController(
            FindAchievementsUsecaseFactory.create()
        )


