from src.common.json_repository import JsonRepository
from src.modules.gifts.model import Gift


class GiftsRepository(JsonRepository[Gift, Gift]):
    def __init__(self) -> None:
        super().__init__(filename="gifts", model=Gift, simple_model=Gift)
