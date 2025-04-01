from src._types import AssetPath, Translate
from src.common.base_model import ModelBase


class _MountAssets(ModelBase):
    icon: AssetPath | None
    big_icon: AssetPath | None


class _MountSkin(ModelBase):
    id: str
    name: Translate
    desc: Translate
    unlock_desc: Translate
    owner_mount_id: str
    assets: _MountAssets


class MountSimple(ModelBase):
    id: str
    name: Translate
    quality: str
    mount_type: str
    assets: _MountAssets


class Mount(MountSimple):
    desc: Translate
    unlock_desc: Translate
    skins: list[_MountSkin]
