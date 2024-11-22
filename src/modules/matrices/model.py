from pydantic import BaseModel


class _SuitAssets(BaseModel):
    icon: str
    remould_icon: str
    icon_temp: str


class _SuitSet(BaseModel):
    description: str
    needs: int
    is_global: bool
    add_score: float


class _ModifierAssets(BaseModel):
    icon: str
    add_icon: str | None
    dec_icon: str | None


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
    large_icon: str
    icon: str


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
