import strawberry
from pydantic import BaseModel


class MountAsset(BaseModel):
    icon: str | None
    showImage: str | None


class MountPart(BaseModel):
    id: str
    name: str
    description: str
    rarity: int
    icon: str
    type: str


class UnlockItem(BaseModel):
    amount: int
    item: MountPart


@strawberry.experimental.pydantic.type(model=MountAsset, all_fields=True)
class MountAssetType:
    pass


@strawberry.experimental.pydantic.type(model=MountPart, all_fields=True)
class MountPartType:
    pass


@strawberry.experimental.pydantic.type(model=UnlockItem, all_fields=True)
class UnlockItemType:
    pass
