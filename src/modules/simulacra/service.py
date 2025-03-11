from typing import TYPE_CHECKING

from src._types import LangsEnum
from src.exceptions.not_found import SimulacrumNotFoundError
from src.modules._paginator import paginate_items
from src.modules._utils import quality_to_int
from src.modules.simulacra._utils import filter_simulacra
from src.modules.simulacra.dtos import GetSimulacra

if TYPE_CHECKING:
    from src.modules._paginator import Pagination
    from src.modules.gifts.model import Gift
    from src.modules.gifts.repository import GiftsRepository
    from src.modules.simulacra.model import Simulacrum, SimulacrumSimple
    from src.modules.simulacra.repository import ImitationRepository


class ImitationService:
    def __init__(
        self,
        imitation_repository: "ImitationRepository",
        gift_repository: "GiftsRepository",
    ) -> None:
        self.imitation_repository = imitation_repository
        self.gift_repository = gift_repository

    async def get(self, *, lang: LangsEnum, _id: str) -> "Simulacrum":
        if data := await self.imitation_repository.get_id(lang=lang, _id=_id):
            return data
        raise SimulacrumNotFoundError(lang=lang, id=_id)

    async def get_all(self, *, params: GetSimulacra) -> "Pagination[SimulacrumSimple]":
        simulacra = await self.imitation_repository.get_all(lang=params.lang)

        filtered = [data for data in simulacra if filter_simulacra(data, params=params)]

        return paginate_items(filtered, params.page, params.limit)

    async def get_simulacrum_gifts(
        self,
        *,
        lang: LangsEnum,
        _id: str,
    ) -> "list[Gift]":
        simulacrum = await self.get(lang=lang, _id=_id)
        gifts = await self.gift_repository.get_all(lang=lang)

        liked_flags = {like.id for like in simulacrum.extras.like}
        disliked_flags = {dislike.id for dislike in simulacrum.extras.dislike}

        region_flags = {"Genet", "Vera", "Asshai", "Jiuyu"}

        qualities = {"COMMON": (5, 2), "RARE": (10, 4), "EPIC": (20, 8)}

        result_gifts: list[Gift] = []

        for gift in gifts:
            if any(flag in disliked_flags for flag in gift.hobby_flag):
                gift.value = qualities.get(gift.quality, (0, 0))[1]
                continue

            if any(flag in liked_flags for flag in gift.hobby_flag):
                for flag in gift.hobby_flag:
                    if flag in liked_flags:
                        gift.value += qualities.get(gift.quality, (0, 0))[0]

            not_used_regions_flags = (
                (disliked_flags | liked_flags) & region_flags
            ) ^ region_flags
            if not_used_regions_flags:
                gift.value += qualities.get(gift.quality, (0, 0))[0]

            result_gifts.append(gift)

        return sorted(
            result_gifts,
            key=lambda x: (-x.value, -quality_to_int(x.quality)),
        )
