from typing import Annotated

from pydantic import Field

from src._types import (
    AssetPath,
    Translate,
    TranslateSplitBreakLine,
    TranslateWithValues,
)
from src.common.base_model import ModelBase
from src.modules.banners.dtos import Banner


class Element(ModelBase):
    id: str
    name: Translate
    desc: Translate
    icon: AssetPath


class Category(ModelBase):
    id: str
    name: Translate
    icon: AssetPath
    icon_gray: AssetPath


class ShatterOrCharge(ModelBase):
    value: float
    tier: str


class Charge(ModelBase):
    value: float
    tier: str


class _AttackTag(ModelBase):
    id: str
    name: Translate


class Attack(ModelBase):
    id: str
    name: Translate
    desc: Translate
    short_desc: Translate | None
    icon: AssetPath
    tags: list[_AttackTag]
    operations: list[str]
    values: list[list[float]]


class Skill(ModelBase):
    name: Translate | None
    desc: Translate | None
    type: str
    icon: AssetPath
    attacks: list[Attack]


class Attribute(ModelBase):
    id: str
    value: float


class NeedItem(ModelBase):
    id: str
    count: int


class Advancement(ModelBase):
    desc: TranslateWithValues
    attributes: list[Attribute]
    need_item: NeedItem
    cost_type: str
    need_golds: int
    star_skill_score: int
    shatter: ShatterOrCharge
    charge: ShatterOrCharge


class Fashion(ModelBase):
    id: str
    name: Translate
    desc: Translate
    use_desc: Translate
    brief: Translate
    icon: AssetPath
    quality: str
    display_type_text: Translate


class RecommendedMatrice(ModelBase):
    id: str
    reason: Translate


class Assets(ModelBase):
    item_icon: AssetPath
    item_large_icon: AssetPath
    weapon_icon_for_matrix: AssetPath
    solo_league_ban_pick_banner: AssetPath
    item_name_image: AssetPath
    lottery_drawing: AssetPath
    lottery_card_image: AssetPath


class MultiElement(ModelBase):
    element: str
    passives: list[TranslateSplitBreakLine]


class WeaponSimple(ModelBase):
    id: str
    name: Translate
    rarity: str
    quality: str

    is_fate: bool
    is_limited: bool
    is_warehouse: bool

    element: Element
    category: Category

    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    assets: Assets

    banners_count: int
    banners: list[Banner]
    imitation_id: str | None = None
    suit_id: str | None = None


class Weapon(WeaponSimple):
    desc: Translate
    brief: Translate
    lottery_desc: Translate
    skills: Annotated[list[Skill], Field(default_factory=list)]
    advancements: Annotated[list[Advancement], Field(default_factory=list)]
    passives: Annotated[list[TranslateSplitBreakLine], Field(default_factory=list)]
    multi_element: Annotated[list[MultiElement], Field(default_factory=list)]
    fashions: Annotated[list[Fashion], Field(default_factory=list)]
    recommended_matrices: Annotated[
        list[RecommendedMatrice],
        Field(default_factory=list),
    ]
