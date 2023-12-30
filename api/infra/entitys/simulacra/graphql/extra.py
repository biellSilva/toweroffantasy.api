
import strawberry


@strawberry.type
class Assets:
    avatar: str
    characterArtwork: str
    titlePicture: str
    painting: str
    namePicture: str
    grayPainting: str
    thumbPainting: str
    weaponShowPicture: str
    activeImitation: str
    inactiveImitation:str
    advancePainting: str
    advanceGrayPainting: str
    backPhoto: str
    rarityIcon: str
    lotteryCardImage: str
    # lotteryDrawing: str
    matrixPainting: str
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


@strawberry.type
class FashionAssets:
    painting: str
    grayPainting: str


@strawberry.type
class Fashion:
    id: str
    name: str
    description: str
    rarity: int
    source: str
    simulacrumId: str
    weaponId: str
    assets: FashionAssets