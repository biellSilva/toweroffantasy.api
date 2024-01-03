
from pydantic import BaseModel


class MetaLastUpdated(BaseModel):
    username: str = 'unknown'
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
