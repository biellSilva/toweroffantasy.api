from pydantic import BaseModel


class _GiftAssets(BaseModel):
    icon: str


class Gift(BaseModel):
    id: str
    name: str
    desc: str
    quality: str
    hobby_flag: list[str]
    value: int
    assets: _GiftAssets
