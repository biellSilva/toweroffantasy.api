
from pydantic import BaseModel


class MountAsset(BaseModel):
    icon: str | None
    showImage: str | None


class MountPart(BaseModel):
    id: str
    name: str = 'none'
    description: str
    rarity: str
    icon: str
    type: str
    

class UnlockItem(BaseModel):
    amount: int
    item: MountPart