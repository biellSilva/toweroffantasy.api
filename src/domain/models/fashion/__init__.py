from pydantic import BaseModel
import strawberry

from .extras import OutfitFashion, WeaponFashion


class Fashion(BaseModel):
    outfit: OutfitFashion
    weapon: WeaponFashion


@strawberry.experimental.pydantic.type(model=Fashion, all_fields=True)
class FashionType:
    pass
