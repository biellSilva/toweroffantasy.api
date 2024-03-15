from pydantic import AliasChoices, BaseModel, Field
import strawberry


class OutfitFashionAssets(BaseModel):
    painting: str
    grayPainting: str = Field(
        validation_alias=AliasChoices("grayPainting", "prayPainting")
    )


class OutfitFashion(BaseModel):
    id: str
    name: str
    description: str
    rarity: int
    source: str
    simulacrumId: str
    weaponId: str
    assets: OutfitFashionAssets


class WeaponFashion(BaseModel):
    id: str
    name: str
    description: str
    rarity: int
    type: str
    icon: str


@strawberry.experimental.pydantic.type(model=OutfitFashionAssets, all_fields=True)
class OutfitFashionAssetsType:
    pass


@strawberry.experimental.pydantic.type(model=OutfitFashion, all_fields=True)
class OutfitFashionType:
    pass


@strawberry.experimental.pydantic.type(model=WeaponFashion, all_fields=True)
class WeaponFashionType:
    pass
