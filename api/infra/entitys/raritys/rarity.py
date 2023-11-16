
from pydantic import BaseModel, BeforeValidator
from typing import Annotated

from api.utils import replace_rarity_asset


class RarityAssets(BaseModel):
    RarityIconImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    SourceIconImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    ArtifactNameBackImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    CardQualityImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    IconBackImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    LotteryExhibitionImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    LotteryExhibitionStuffImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    LotteryDrawingImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    LotteryDrawingStuffImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]
    ImitationRarityBackImage: Annotated[str | None, BeforeValidator(replace_rarity_asset)]

class Raritys(BaseModel):
    N: RarityAssets
    R: RarityAssets
    SR: RarityAssets
    SSR: RarityAssets