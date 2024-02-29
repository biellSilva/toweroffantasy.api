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
