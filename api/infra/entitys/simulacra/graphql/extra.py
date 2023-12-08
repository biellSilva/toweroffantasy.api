
import strawberry


@strawberry.type
class Assets:
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


@strawberry.type
class VoiceActors:
    cn: str | None
    jp: str | None
    en: str | None
    kr: str | None
    pt: str | None


@strawberry.type
class Awakening:
    name: str
    description: str
    icon: str
    need: int
