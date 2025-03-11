from typing import TYPE_CHECKING

from src.exceptions.not_found import GiftNotFoundError
from src.modules._paginator import paginate_items

if TYPE_CHECKING:
    from src._types import LangsEnum
    from src.modules._paginator import Pagination
    from src.modules.base.dtos import BaseSearchAllDto
    from src.modules.gifts.model import Gift
    from src.modules.gifts.repository import GiftsRepository


class GiftsService:
    def __init__(self, repository: "GiftsRepository") -> None:
        self.repository = repository

    async def get(self, *, lang: "LangsEnum", _id: str) -> "Gift":
        if data := await self.repository.get_id(lang=lang, _id=_id):
            return data
        raise GiftNotFoundError(lang=lang, id=_id)

    async def get_all(self, *, params: "BaseSearchAllDto") -> "Pagination[Gift]":
        data = await self.repository.get_all(lang=params.lang)

        return paginate_items(data, params.page, params.limit)
