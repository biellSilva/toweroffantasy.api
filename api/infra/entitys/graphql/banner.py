
import strawberry


@strawberry.type
class Banner:
    simulacrumId: str | None
    weaponId: str | None
    matrixId: str | None
    simulacrumName: str | None
    element: str | None
    category: str | None
    bannerNumber: int
    startDate: str
    endDate: str
    detailsLink: str
    isLimitedBannerOnly: bool
    isRerun: bool
    isFinalBanner: bool
    isCollab: bool
    noWeapon: bool
    isReleased: bool