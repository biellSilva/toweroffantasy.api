
from pydantic import BaseModel


class Assets(BaseModel):
    avatar: str 
    icon: str 
    lotteryCardImage: str 
    lotteryDrawing: str 
    painting: str 
    namePicture: str 
    grayPainting: str
    thumbPainting: str 
    weaponShowPicture: str 
    hasGotAwakenEntrance: str 
    notGotAwakenEntrance: str 
    advancePainting: str 
    advanceGrayPainting: str 
    backPhoto: str 
    rarityIcon: str 
    soloLeagueBanPickBanner: str 
    descPainting: str


class VoiceActors(BaseModel):
    chinese: str | None
    japanese: str | None
    english: str | None
    korean: str | None
    portuguese: str | None


class Awakening(BaseModel):
    Need: int
    Name: str
    Description: str
    Icon: str