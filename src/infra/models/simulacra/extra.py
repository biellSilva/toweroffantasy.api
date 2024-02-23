from typing import TypedDict


class RawSimulacraAssets(TypedDict):
    avatar: str | None
    titlePicture: str | None
    characterArtwork: str | None
    painting: str | None
    namePicture: str | None
    grayPainting: str | None
    thumbPainting: str | None
    weaponShowPicture: str | None
    activeImitation: str | None
    inactiveImitation: str | None
    advancePainting: str | None
    advanceGrayPainting: str | None
    backPhoto: str | None
    rarityIcon: str | None
    lotteryCardImage: str | None
    matrixPainting: str | None
    descPainting: str | None


class RawVoiceActors(TypedDict):
    cn: str | None
    jp: str | None
    en: str | None
    kr: str | None
    pt: str | None


class RawAwakening(TypedDict):
    name: str | None
    description: str | None
    icon: str | None
    need: int


class _RawFashionAsset(TypedDict):
    painting: str
    prayPainting: str


class RawFashion(TypedDict):
    id: str
    name: str
    description: str
    rarity: int
    source: str
    simulacrumId: str
    assets: _RawFashionAsset
    weaponId: str


class RawNitai(TypedDict):
    title: str
    description: str
    photo: str
