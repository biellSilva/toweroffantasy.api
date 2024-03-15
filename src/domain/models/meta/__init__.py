from datetime import datetime
from typing import Annotated

import strawberry
from pydantic import BaseModel, BeforeValidator

from src.utils import meta_timestamp_to_iso


class MetaLastUpdated(BaseModel):
    username: str = "unknown"
    timestamp: Annotated[str, BeforeValidator(meta_timestamp_to_iso)] = (
        datetime.now().isoformat()
    )


class RecoMatrix(BaseModel):
    id: str
    pieces: int


class MetaData(BaseModel):
    recommendedPairings: list[str] = []
    recommendedMatrices: list[RecoMatrix] = []
    rating: list[float] = []
    analyticVideoId: str | None = None
    lastUpdated: MetaLastUpdated = MetaLastUpdated()


@strawberry.experimental.pydantic.type(model=MetaLastUpdated, all_fields=True)
class MetaLastUpdatedType:
    pass


@strawberry.experimental.pydantic.type(model=RecoMatrix, all_fields=True)
class RecoMatrixType:
    pass


@strawberry.experimental.pydantic.type(model=MetaData, all_fields=True)
class MetaDataType:
    pass
