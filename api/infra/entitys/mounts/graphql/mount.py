
import strawberry


@strawberry.type
class MountAsset:
    icon: str
    showImage: str

@strawberry.type
class MountPart:
    id: str
    name: str
    description: str
    rarity: int
    icon: str
    type: str
    
@strawberry.type
class UnlockItem:
    amount: int
    item: MountPart

@strawberry.type
class Mount:
    id: str
    name: str | None
    rarity: int
    description: str
    assets: MountAsset
    version: str
    unlockItems: list[UnlockItem]