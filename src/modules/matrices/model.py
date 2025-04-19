from pydantic import computed_field

from src._types import AssetPath, Translate, TranslateWithValues
from src.common.base_model import ModelBase


class _SuitAssets(ModelBase):
    icon: AssetPath
    remould_icon: AssetPath
    icon_temp: AssetPath


class _SuitSet(ModelBase):
    description: TranslateWithValues
    needs: int
    is_global: bool
    add_score: float


class _ModifierAssets(ModelBase):
    icon: AssetPath
    add_icon: AssetPath | None
    dec_icon: AssetPath | None


class _MatriceModifier(ModelBase):
    id: str
    name: Translate
    description: Translate
    initial_value: float
    modifier_op: str
    modifier_value: float
    is_percentage: bool
    is_uncommon: bool
    is_tag: bool
    assets: _ModifierAssets


class _MatriceAssets(ModelBase):
    large_icon: AssetPath
    icon: AssetPath


class _SuitMatrice(ModelBase):
    id: str
    suit_id: str
    name: Translate
    description: Translate
    rarity: str
    quality: str
    slot_index: int
    max_level: int
    max_star: int
    base_exp: int
    modifiers: list[_MatriceModifier]
    assets: _MatriceAssets


class Suit(ModelBase):
    id: str
    name: Translate
    quality: str
    assets: _SuitAssets
    sets: list[_SuitSet]
    matrices: list[_SuitMatrice]

    imitation_id: str | None = None
    weapon_id: str | None = None
    banners_count: int = 0

    @computed_field
    @property
    def matrice_name(self) -> str:
        name = self.matrices[-1].name
        if ":" in name:
            return name.split(":", 1)[0].strip()
        if "・" in name:
            return name.split("・", 1)[0].strip()
        if "(" in name:
            return name.split("(", 1)[0].strip()
        return name.strip()

    @computed_field
    @property
    def rarity(self) -> str:
        return self.matrices[0].rarity

    @computed_field
    @property
    def matrice_assets(self) -> _MatriceAssets:
        return self.matrices[0].assets
