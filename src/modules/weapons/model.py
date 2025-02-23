from pydantic import BaseModel

from src._types import AssetPath


class Element(BaseModel):
    id: str
    name: str
    desc: str
    icon: AssetPath


class Category(BaseModel):
    id: str
    name: str
    icon: AssetPath
    icon_gray: AssetPath


class ShatterOrCharge(BaseModel):
    value: float
    tier: str


class Charge(BaseModel):
    value: float
    tier: str


class Attack(BaseModel):
    id: str
    name: str
    desc: str
    short_desc: str | None
    icon: AssetPath
    tags: list[str]
    operations: list[str]
    values: list[list[float]]


class Skill(BaseModel):
    name: str | None
    desc: str | None
    type: str
    icon: AssetPath
    attacks: list[Attack]


class Attribute(BaseModel):
    id: str
    value: float


class NeedItem(BaseModel):
    id: str
    count: int


class Advancement(BaseModel):
    desc: str
    attributes: list[Attribute]
    need_item: NeedItem
    cost_type: str
    need_golds: int
    star_skill_score: int
    shatter: ShatterOrCharge
    charge: ShatterOrCharge


class Fashion(BaseModel):
    id: str
    name: str
    desc: str
    use_desc: str
    brief: str
    icon: AssetPath
    quality: str
    display_type_text: str


class RecommendedMatrice(BaseModel):
    id: str
    reason: str


class Assets(BaseModel):
    item_icon: AssetPath
    item_large_icon: AssetPath
    weapon_icon_for_matrix: AssetPath
    solo_league_ban_pick_banner: AssetPath
    item_name_image: AssetPath
    lottery_drawing: AssetPath
    lottery_card_image: AssetPath


class MultiElement(BaseModel):
    element: str
    passives: list[str]


class WeaponSimple(BaseModel):
    id: str
    name: str
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


class Weapon(WeaponSimple):
    desc: str
    brief: str
    lottery_desc: str
    skills: list[Skill] = []
    advancements: list[Advancement] = []
    passives: list[str] = []
    multi_element: list[MultiElement] = []
    fashions: list[Fashion] = []
    recommended_matrices: list[RecommendedMatrice] = []
