from typing import TYPE_CHECKING

from src.exceptions.not_found import GiftNotFoundError

if TYPE_CHECKING:
    from src._types import LangsEnum
    from src.modules.gifts.model import Gift
    from src.modules.gifts.repository import GiftsRepository


class GiftsService:
    def __init__(self, repository: "GiftsRepository") -> None:
        self.repository = repository

    async def get(self, *, lang: "LangsEnum", _id: str) -> "Gift":
        if data := await self.repository.get_id(lang=lang, _id=_id):
            return data
        raise GiftNotFoundError(lang=lang, id=_id)

    async def get_all(self, *, lang: "LangsEnum") -> list["Gift"]:
        return await self.repository.get_all(lang=lang)
