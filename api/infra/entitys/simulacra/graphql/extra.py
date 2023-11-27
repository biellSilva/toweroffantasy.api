
import strawberry


@strawberry.type
class Assets:
    Avatar: str
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


@strawberry.type
class VoiceActors:
    Chinese: str | None
    Japanese: str | None
    English: str | None
    Korean: str | None
    Portuguese: str | None


@strawberry.type
class Awakening:
    Need: int
    Name: str
    Description: str
    Icon: str


@strawberry.type
class Banner:
    bannerNo: int
    start: str
    end: str
    details_link: str
    limited_banner_only: bool
    is_rerun: bool
    final_rerun: bool
    is_collab: bool
    