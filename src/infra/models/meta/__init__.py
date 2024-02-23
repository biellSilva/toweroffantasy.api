from typing import TypedDict

from src.infra.models.meta.extra import RawLastUpdate, RawRecoMatrice


class RawMeta(TypedDict):
    recommendedPairings: list[str]
    recommendedMatrices: list[RawRecoMatrice]
    rating: list[int]
    analyticVideoId: str | None
    lastUpdated: RawLastUpdate
