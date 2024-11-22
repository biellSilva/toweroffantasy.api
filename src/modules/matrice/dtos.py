from typing import Annotated

from fastapi import Path

from src.modules.base.dtos import BaseDataDto


class GetMatrix(BaseDataDto):
    matrix_id: Annotated[str, Path(description="Matrix id")]
