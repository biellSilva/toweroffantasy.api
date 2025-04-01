from src._types import AssetPath, Translate
from src.common.base_model import ModelBase


class _GiftAssets(ModelBase):
    icon: AssetPath


class Gift(ModelBase):
    id: str
    name: Translate
    desc: Translate
    quality: str
    hobby_flag: list[str]
    value: int
    assets: _GiftAssets
