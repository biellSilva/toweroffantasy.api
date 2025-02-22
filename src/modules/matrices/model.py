from pydantic import BaseModel, computed_field

from src._types import AssetPath


class _SuitAssets(BaseModel):
    icon: AssetPath
    remould_icon: AssetPath
    icon_temp: AssetPath


class _SuitSet(BaseModel):
    description: str
    needs: int
    is_global: bool
    add_score: float


class _ModifierAssets(BaseModel):
    icon: AssetPath
    add_icon: AssetPath | None
    dec_icon: AssetPath | None


class _MatriceModifier(BaseModel):
    id: str
    name: str
    description: str
    initial_value: float
    modifier_op: str
    modifier_value: float
    is_percentage: bool
    is_uncommon: bool
    is_tag: bool
    assets: _ModifierAssets


class _MatriceAssets(BaseModel):
    large_icon: AssetPath
    icon: AssetPath


class _SuitMatrice(BaseModel):
    id: str
    suit_id: str
    name: str
    description: str
    rarity: str
    quality: str
    slot_index: int
    max_level: int
    max_star: int
    base_exp: int
    modifiers: list[_MatriceModifier]
    assets: _MatriceAssets


class Suit(BaseModel):
    id: str
    name: str
    quality: str
    assets: _SuitAssets
    sets: list[_SuitSet]
    matrices: list[_SuitMatrice]

    @computed_field
    @property
    def matrice_name(self) -> str:
        name = self.matrices[0].name
        if ":" in name:
            return name.split(":", 1)[0]
        if "・" in name:
            return name.split("・", 1)[0]
        return name

    @computed_field
    @property
    def rarity(self) -> str:
        return self.matrices[0].rarity
