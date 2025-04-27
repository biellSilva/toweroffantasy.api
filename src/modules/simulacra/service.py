from typing import TYPE_CHECKING

from src._types import DislikedGiftValue
from src.exceptions.not_found import SimulacrumNotFoundError
from src.modules._paginator import Pagination
from src.modules._utils import quality_to_int

if TYPE_CHECKING:
    from src._types import DislikedGiftValue, LikedGiftValue
    from src.modules.gifts.model import Gift
    from src.modules.gifts.repository import GiftsRepository
    from src.modules.simulacra.dtos import GetSimulacra, GetSimulacrum
    from src.modules.simulacra.model import Simulacrum, SimulacrumSimple
    from src.modules.simulacra.repository import SimulacraRepository


class ImitationService:
    def __init__(
        self,
        imitation_repository: "SimulacraRepository",
        gift_repository: "GiftsRepository",
    ) -> None:
        self.imitation_repository = imitation_repository
        self.gift_repository = gift_repository

    async def get(self, *, params: "GetSimulacrum") -> "Simulacrum":
        if data := await self.imitation_repository.get_simulacrum(params):
            return data
        raise SimulacrumNotFoundError(id=params.simulacrum_id)

    async def get_all(
        self,
        *,
        params: "GetSimulacra",
    ) -> "Pagination[SimulacrumSimple]":
        simulacra = await self.imitation_repository.get_simulacra(params)
        count = await self.imitation_repository.count_simulacra(params)
        return Pagination(
            data=simulacra,
            page=params.page,
            limit=params.limit,
            max_page=count // params.limit + 1,
            total_items=count,
        )

    async def get_simulacrum_gifts(self, *, params: "GetSimulacrum") -> "list[Gift]":
        simulacrum = await self.get(params=params)
        gifts = await self.gift_repository.get_all(lang=params.lang)

        liked_flags = {like.id for like in simulacrum.extras.like}
        disliked_flags = {dislike.id for dislike in simulacrum.extras.dislike}

        region_flags = {"Genet", "Vera", "Asshai", "Jiuyu"}

        qualities: dict[str, tuple[LikedGiftValue, DislikedGiftValue]] = {
            "COMMON": (5, 2),
            "RARE": (10, 4),
            "EPIC": (20, 8),
        }

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
