
import strawberry


@strawberry.type
class MountAsset:
    icon: str
    showImage: str


@strawberry.type
class Mount:
    id: str
    name: str | None
    description: str
    assets: MountAsset