from typing import Annotated

from pydantic import BaseModel, Field

from src._types import AssetPath
from src.modules.base.model import BackgroundColor


class _FashionAssets(BaseModel):
    painting: AssetPath
    gray_painting: AssetPath


class _ImitationFashion(BaseModel):
    id: str
    name: str
    desc: str
    source: str
    imitation_id: str
    quality: str
    only_weapon: bool
    assets: _FashionAssets


class _SimulacrumGift(BaseModel):
    id: str
    name: str
    background_color: BackgroundColor


class _SimulacrumVoiceActors(BaseModel):
    chinese: str | None
    japanese: str | None
    english: str | None
    korean: str | None
    portuguese: str | None


class _ImitationExtras(BaseModel):
    gender: str | None
    birthday: str | None
    age: str
    height: str | None
    title: str
    job: str
    belong_to: str | None
    hometown: str | None
    hometown_map: str | None
    experience_record: str | None
    character: str | None

    like: list[_SimulacrumGift]
    dislike: list[_SimulacrumGift]

    voice_actors: _SimulacrumVoiceActors


class _ImitationAssets(BaseModel):
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


class _AttributeCondition(BaseModel):
    name: str
    desc: str
    use_desc: str
    icon: str
    quality: str


class _AttributeModifier(BaseModel):
    id: str
    name: str
    desc: str
    icon: str
    value: str
    operator: str


class _Likeability(BaseModel):
    condition: int
    type: str
    name: str | None
    context: str | None
    desc: str | None
    unlock_desc: str | None
    icon: str | None
    big_icon: str | None
    conditions: list[_AttributeCondition]
    modifiers: list[_AttributeModifier]


class Imitation(BaseModel):
    id: str
    name: str
    desc: str
    unlock_info: str
    sex: str
    rarity: str
    weapon_id: str | None
    avatar_id: str
    is_limited: bool
    no_weapon: bool

    fashions: list[_ImitationFashion]
    extras: _ImitationExtras

    assets: _ImitationAssets
    assets_a3: Annotated[_ImitationAssets, Field(validation_alias="assetsA3")]
    likeabilities: list[_Likeability]
