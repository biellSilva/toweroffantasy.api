
import strawberry


@strawberry.type
class Banner:
    simulacrumId: str
    weaponId: str | None
    matrixId: str | None
    simulacrumName: str
    bannerNumber: int
    startDate: str
    endDate: str
    detailsLink: str
    isLimitedBannerOnly: bool
    isRerun: bool
    isFinalBanner: bool
    isCollab: bool