
from pydantic import BaseModel


class MountAsset(BaseModel):
    icon: str | None
    showImage: str | None