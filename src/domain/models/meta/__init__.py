import strawberry
from pydantic import BaseModel


class MetaLastUpdated(BaseModel):
    username: str = "unknown"
    timestamp: int = 0


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
