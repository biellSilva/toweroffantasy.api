
import strawberry

from api.infra.entitys.graphql.banner import Banner
from .extra import MatriceSet, MatrixAssets, MatrixMeta


@strawberry.type
class Matrice:
    id: str
    simulacrumId: str | None
    version: str
    name: str
    description: str
    assets: MatrixAssets
    rarity: int
    sets: list[MatriceSet]
    banners: list[Banner]
    meta: MatrixMeta
