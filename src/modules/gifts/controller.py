from typing import Annotated

from fastapi import Depends

from src._types import LangsEnum
from src.core.router import ApiRouter
from src.exceptions.not_found import GiftNotFoundError
from src.modules.base.dtos import BaseDataDto
from src.modules.gifts.dtos import GetGift
from src.modules.gifts.model import Gift
from src.modules.gifts.repository import GiftsRepository
from src.modules.gifts.service import GiftsService

router = ApiRouter(prefix="/gifts", tags=["gifts"])

SERVICE = GiftsService(GiftsRepository())


@router.get("", response_model=list[Gift])
async def get_all_gifts(params: Annotated[BaseDataDto, Depends()]) -> list[Gift]:
    return await SERVICE.get_all(lang=params.lang)


@router.get(
    "/{gift_id}",
    response_model=Gift,
    exceptions=[GiftNotFoundError(lang=LangsEnum.EN, id="gift_id")],
)
async def get_gift(params: Annotated[GetGift, Depends()]) -> Gift:
    return await SERVICE.get(lang=params.lang, _id=params.gift_id)
