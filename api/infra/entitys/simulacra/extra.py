
from pydantic import BaseModel


class Assets(BaseModel):
    NamePicture: str
    Name2Picture: str
    Name3Picture: str
    Painting: str
    GrayPainting: str
    ThumbPainting: str
    WeaponShowPicture: str
    HasGotAwakenEntrance: str
    NotGotAwakenEntrance: str
    AdvancePainting: str
    AdvanceGrayPainting: str
    TitlePicture: str
    AwakenPhoto: str
    DescPainting: str


class VoiceActors(BaseModel):
    Chinese: str | None
    Japanese: str | None
    English: str | None
    Korean: str | None
    Portuguese: str | None


class Awakening(BaseModel):
    Need: int
    Name: str
    Description: str
    Icon: str