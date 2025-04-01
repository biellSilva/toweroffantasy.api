from src.common.json_repository import JsonRepository
from src.modules.matrices.model import Suit


class MatriceRepository(JsonRepository[Suit, Suit]):
    def __init__(self) -> None:
        super().__init__(filename="matrices", model=Suit, simple_model=Suit)
