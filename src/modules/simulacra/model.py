from typing import Annotated

from pydantic import BaseModel, Field

from src.modules.base.model import BackgroundColor


class _FashionAssets(BaseModel):
    painting: str
    gray_painting: str


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
    name_picture: str | None
    name_2_picture: str | None
    name_3_picture: str | None
    desc_painting: str | None
    painting: str | None
    gray_painting: str | None
    thumb_painting: str | None
    weapon_show_picture: str | None
    has_got_awaken_entrance: str | None
    not_got_awaken_entrance: str | None
    card_adv_page: str | None
    advance_painting: str | None
    advance_gray_painting: str | None
    back_photo: str | None
    rarity_icon: str | None
    job_back: str | None
    motto_picture: str | None
    motto_2_picture: str | None
    title_picture: str | None
    imitation_virtual_shadow: str | None
    awaken_name_picture: str | None
    awaken_photo: str | None


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
