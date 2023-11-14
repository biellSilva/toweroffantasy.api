
import strawberry

from api.infra.entitys.matrices.graphql.extra import MatriceSet


@strawberry.type
class MatriceType:
    id: str
    name: str
    type: str
    description: str
    icon: str
    gachaIcon: str
    rarity: str
    set: MatriceSet

