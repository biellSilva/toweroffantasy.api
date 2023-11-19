
import strawberry

from api.infra.entitys.matrices.graphql.extra import MatriceSet, MatrixAssets


@strawberry.type
class Matrice:
    id: str
    name: str
    type: str
    description: str
    assets: MatrixAssets
    rarity: str
    sets: list[MatriceSet]

