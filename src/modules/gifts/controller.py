from typing import Annotated

from fastapi import APIRouter, Depends, Query

from src.common.dtos import BaseSearchAllDto
from src.modules._paginator import Pagination
from src.modules.gifts.dtos import GetGift
from src.modules.gifts.model import Gift
from src.modules.gifts.repository import GiftsRepository
from src.modules.gifts.service import GiftsService

router = APIRouter(prefix="/gifts", tags=["gifts"])

SERVICE = GiftsService(GiftsRepository())


@router.get("")
async def get_all_gifts(
    params: Annotated[BaseSearchAllDto, Query()],
) -> Pagination[Gift]:
    return await SERVICE.get_all(params=params)


@router.get("/{gift_id}")
async def get_gift(params: Annotated[GetGift, Depends()]) -> Gift:
    return await SERVICE.get(lang=params.lang, _id=params.gift_id)
