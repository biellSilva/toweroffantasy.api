from src.main.factories.usecases.achievements.find import FindAchievementsUsecaseFactory
from src.presentation.controller.achievements.find import FindAchievementsController


class FindAchievementsControllerFactory:

    @staticmethod
    def create() -> FindAchievementsController:
        return FindAchievementsController(FindAchievementsUsecaseFactory.create())
