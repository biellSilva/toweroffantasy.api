from typing import TYPE_CHECKING

from src._types import LangsEnum
from src._utils import is_str_in_list, paginate_items
from src.exceptions.not_found import SimulacrumNotFoundError
from src.modules.simulacra.dtos import GetSimulacra
from src.modules.simulacra.model import Simulacrum, SimulacrumSimple

if TYPE_CHECKING:
    from src.modules.simulacra.repository import ImitationRepository


class ImitationService:
    def __init__(self, repository: "ImitationRepository") -> None:
        self.repository = repository

    async def get(self, *, lang: LangsEnum, _id: str) -> Simulacrum:
        if data := await self.repository.get_id(lang=lang, _id=_id):
            return Simulacrum(**data)
        raise SimulacrumNotFoundError(lang=lang, id=_id)

    async def get_all(
        self,
        *,
        params: GetSimulacra,
        include_id: list[str] | None,
        exclude_id: list[str] | None,
        include_name: list[str] | None,
        exclude_name: list[str] | None,
        include_sex: list[str] | None,
        exclude_sex: list[str] | None,
        include_rarity: list[str] | None,
        exclude_rarity: list[str] | None,
    ) -> list[SimulacrumSimple]:
        simulacra = [
            SimulacrumSimple(**data)
            for data in await self.repository.get_all(lang=params.lang)
        ]

        filtered = [
            data
            for data in simulacra
            if self._filter_get_all(
                data,
                params=params,
                include_id=include_id,
                exclude_id=exclude_id,
                include_name=include_name,
                exclude_name=exclude_name,
                include_sex=include_sex,
                exclude_sex=exclude_sex,
                include_rarity=include_rarity,
                exclude_rarity=exclude_rarity,
            )
        ]

        return paginate_items(filtered, params.page, params.limit)

    def _filter_get_all(
        self,
        data: "SimulacrumSimple",
        /,
        params: GetSimulacra,
        include_id: list[str] | None,
        exclude_id: list[str] | None,
        include_name: list[str] | None,
        exclude_name: list[str] | None,
        include_sex: list[str] | None,
        exclude_sex: list[str] | None,
        include_rarity: list[str] | None,
        exclude_rarity: list[str] | None,
    ) -> bool:
        includes = [
            (include_id, data.id, True),
            (include_name, data.name, False),
            (include_rarity, data.rarity, True),
            (include_sex, data.sex, True),
        ]
        excludes = [
            (exclude_id, data.id, True),
            (exclude_name, data.name, False),
            (exclude_rarity, data.rarity, True),
            (exclude_sex, data.sex, True),
        ]

        for include, value, equals in includes:
            if include and not is_str_in_list(
                value,
                include,
                equals=equals,
            ):
                return False

        for exclude, value, equals in excludes:
            if exclude and is_str_in_list(
                value,
                exclude,
                equals=equals,
            ):
                return False

        if (params.is_limited is not None and data.is_limited == params.is_limited) or (
            params.no_weapon is not None and data.no_weapon == params.no_weapon
        ):
            return True

        return True
