from typing import Annotated

from fastapi import Path

from src.modules.base.dtos import BaseDataDto


class GetGift(BaseDataDto):
    gift_id: Annotated[str, Path(description="Gift id")]
