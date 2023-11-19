
import strawberry

@strawberry.type
class RarityAssets:
    RarityIconImage: str | None
    SourceIconImage: str | None
    ArtifactNameBackImage: str | None
    CardQualityImage: str | None
    IconBackImage: str | None
    LotteryExhibitionImage: str | None
    LotteryExhibitionStuffImage: str | None
    LotteryDrawingImage: str | None
    LotteryDrawingStuffImage: str | None
    ImitationRarityBackImage: str | None

@strawberry.type
class Raritys:
    N: RarityAssets
    R: RarityAssets
    SR: RarityAssets
    SSR: RarityAssets