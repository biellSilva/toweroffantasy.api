from typing import Annotated

from fastapi import Path

from src.common.dtos import BaseSearchDto


class GetGift(BaseSearchDto):
    gift_id: Annotated[str, Path(description="Gift id")]
