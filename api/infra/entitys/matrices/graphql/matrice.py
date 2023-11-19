
import strawberry

from api.infra.entitys.banners import BannerSchema
from .extra import MatriceSet, MatrixAssets


@strawberry.type
class Matrice:
    id: str
    name: str
    type: str
    description: str
    assets: MatrixAssets
    rarity: str
    sets: list[MatriceSet]
    banners: list[BannerSchema]
