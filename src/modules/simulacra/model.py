from typing import Annotated

from pydantic import AliasChoices, Field

from src._types import AssetPath, Translate, TranslateWithValues
from src.common.base_model import ModelBase
from src.common.model import BackgroundColor


class _FashionAssets(ModelBase):
    painting: AssetPath
    gray_painting: AssetPath


class _ImitationFashion(ModelBase):
    id: str
    name: Translate
    desc: Translate
    source: Translate
    imitation_id: str
    quality: str
    only_weapon: bool
    assets: _FashionAssets


class _SimulacrumGift(ModelBase):
    id: str
    name: Translate
    background_color: BackgroundColor


class _SimulacrumVoiceActors(ModelBase):
    chinese: str | None
    japanese: str | None
    english: str | None
    korean: str | None
    portuguese: str | None


class _ImitationExtras(ModelBase):
    gender: Translate | None
    birthday: Translate | None
    age: Translate
    height: Translate | None
    title: Translate
    job: Translate
    belong_to: Translate | None
    hometown: Translate | None
    hometown_map: str | None
    experience_record: Translate | None
    character: Translate | None

    like: list[_SimulacrumGift]
    dislike: list[_SimulacrumGift]

    voice_actors: _SimulacrumVoiceActors


class _ImitationAssets(ModelBase):
    icon: AssetPath | None
    big_icon: AssetPath | None
    name_picture: AssetPath | None
    name_2_picture: AssetPath | None
    name_3_picture: AssetPath | None
    desc_painting: AssetPath | None
    painting: AssetPath | None
    gray_painting: AssetPath | None
    thumb_painting: AssetPath | None
    weapon_show_picture: AssetPath | None
    has_got_awaken_entrance: AssetPath | None
    not_got_awaken_entrance: AssetPath | None
    card_adv_page: AssetPath | None
    advance_painting: AssetPath | None
    advance_gray_painting: AssetPath | None
    back_photo: AssetPath | None
    rarity_icon: AssetPath | None
    job_back: AssetPath | None
    motto_picture: AssetPath | None
    motto_2_picture: AssetPath | None
    title_picture: AssetPath | None
    imitation_virtual_shadow: AssetPath | None
    awaken_name_picture: AssetPath | None
    awaken_photo: AssetPath | None


class _AttributeCondition(ModelBase):
    name: Translate
    desc: Translate
    use_desc: Translate
    icon: AssetPath
    quality: str


class _AttributeModifier(ModelBase):
    id: str
    name: Translate
    desc: Translate
    icon: AssetPath
    value: float
    operator: str


class _Likeability(ModelBase):
    condition: int
    type: str
    name: Translate | None
    context: Translate | None
    desc: TranslateWithValues | None
    unlock_desc: Translate | None
    icon: AssetPath | None
    big_icon: AssetPath | None
    conditions: list[_AttributeCondition]
    modifiers: list[_AttributeModifier]


class SimulacrumSimple(ModelBase):
    id: str
    name: Translate
    sex: str
    rarity: str
    is_limited: bool
    no_weapon: bool

    assets: _ImitationAssets


class Simulacrum(SimulacrumSimple):
    desc: Translate
    unlock_info: Translate
    weapon_id: str | None
    avatar_id: str
    assets_a3: Annotated[
        _ImitationAssets,
        Field(validation_alias=AliasChoices("assets_a3", "assetsA3")),
    ]
    extras: _ImitationExtras
    fashions: list[_ImitationFashion]
    likeabilities: list[_Likeability]
