from typing import Annotated

from fastapi import Path

from src.modules.base.dtos import BaseDataDto


class GetImitation(BaseDataDto):
    imitation_id: Annotated[str, Path(description="Imitation id")]
