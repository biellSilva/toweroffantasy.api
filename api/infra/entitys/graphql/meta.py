
import strawberry


@strawberry.type
class MetaLastUpdated:
    username: str 
    timestamp: int 

@strawberry.type
class RecoMatrix:
    id: str
    pieces: int

@strawberry.type
class MetaData:
    recommendedPairings: list[str] 
    recommendedMatrices: list[RecoMatrix] 
    rating: list[float] 
    analyticVideoId: str | None 
    lastUpdated: MetaLastUpdated 