from pydantic import BaseModel

from src._types import AssetPath


class _GiftAssets(BaseModel):
    icon: AssetPath


class Gift(BaseModel):
    id: str
    name: str
    desc: str
    quality: str
    hobby_flag: list[str]
    value: int
    assets: _GiftAssets
