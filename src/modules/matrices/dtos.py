from typing import Annotated

from fastapi import Path

from src.modules.base.dtos import BaseSearchDto


class GetMatrix(BaseSearchDto):
    matrix_id: Annotated[str, Path(description="Matrix id")]
