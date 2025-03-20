from pydantic import BaseModel


class _MountAssets(BaseModel):
    icon: str
    big_icon: str


class _MountSkin(BaseModel):
    id: str
    name: str
    desc: str
    unlock_desc: str
    owner_mount_id: str
    assets: _MountAssets


class MountSimple(BaseModel):
    id: str
    name: str
    quality: str
    mount_type: str
    assets: _MountAssets


class Mount(MountSimple):
    desc: str
    unlock_desc: str
    skins: list[_MountSkin]
