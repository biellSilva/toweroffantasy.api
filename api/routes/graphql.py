from typing import Any, List

import strawberry
from strawberry.fastapi import GraphQLRouter

from api.config import GB_BANNERS
from api.core.exceptions import LanguageNotFound, VersionNotFound
from api.enums import LANGS, VERSIONS
from api.enums import langs as LANGS_
from api.enums import langs_cn as LANGS_CN_
from api.infra.entitys import EntityBase
from api.infra.entitys.graphql import *
from api.infra.repository import *
from api.infra.repository.guidebook import GuideBookRepo
from api.utils import filter_released

SIMU_REPO = SimulacraRepo()
MATRICE_REPO = MatricesRepo()
WEAPON_REPO = WeaponRepo()
SIMU_V2_REPO = SimulacraV2Repo()
ACHIEV_REPO = AchievementRepo()
OUTFIT_REPO = OutfitRepo()
FOOD_REPO = FoodRepo()
ITEM_REPO = ItemRepo()
RELIC_REPO = RelicRepo()
SERVAN_REPO = ServantsRepo()
MOUNTS_REPO = MountsRepo()
GUIDEBOOK_REPO = GuideBookRepo()


def check_params(lang: str, version: str):
    if version not in ["global", "china"]:
        raise VersionNotFound(version)

    if lang not in LANGS_ and lang not in LANGS_CN_:
        raise LanguageNotFound(lang, version)


@strawberry.type
class Query:

    @strawberry.field(name="simulacrum")
    async def get_simulacrum(self, id: str, lang: str = "en") -> Simulacra:
        version = "global"
        check_params(lang=lang, version=version)

        simulacrum = await SIMU_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return simulacrum  # type: ignore

    @strawberry.field(name="simulacra")
    async def get_simulacra(
        self, lang: str = "en", includeUnreleased: bool = False
    ) -> List[Simulacra]:
        version = "global"
        check_params(lang=lang, version=version)

        simulacra = await SIMU_REPO.get_all(lang=lang, version=VERSIONS(version))

        if not includeUnreleased:
            simulacra = filter(filter_released, simulacra)

        return simulacra  # type: ignore

    @strawberry.field(name="simulacrum_v2")
    async def get_simulacrum_v2(self, id: str, lang: str = "en") -> SimulacraV2:

        version = "global"
        check_params(lang=lang, version=version)

        simulacrum = await SIMU_V2_REPO.get(
            EntityBase(id=id), lang=LANGS(lang), version=VERSIONS(version)
        )
        return simulacrum  # type: ignore

    @strawberry.field(name="simulacra_v2")
    async def get_simulacra_v2(
        self, lang: str = "en", includeUnreleased: bool = False
    ) -> List[SimulacraV2]:
        version = "global"
        check_params(lang=lang, version=version)

        simulacra = await SIMU_V2_REPO.get_all(
            lang=LANGS(lang), version=VERSIONS(version), graphql=True
        )

        if not includeUnreleased:
            simulacra = filter(filter_released, simulacra)

        return simulacra  # type: ignore

    @strawberry.field(name="weapon")
    async def get_weapon(self, id: str, lang: str = "en") -> Weapon:
        version = "global"
        check_params(lang=lang, version=version)

        weapon = await WEAPON_REPO.get(
            EntityBase(id=id),
            lang=LANGS(lang),
            version=VERSIONS(version),
            graphql=True,
        )
        return weapon  # type: ignore

    @strawberry.field(name="weapons")
    async def get_weapons(
        self, lang: str = "en", includeUnreleased: bool = False
    ) -> List[Weapon]:
        version = "global"
        check_params(lang=lang, version=version)

        weapons = await WEAPON_REPO.get_all(
            lang=lang, version=VERSIONS(version), graphql=True
        )

        if not includeUnreleased:
            weapons = filter(filter_released, weapons)

        return weapons  # type: ignore

    @strawberry.field(name="matrix")
    async def get_matrice(self, id: str, lang: str = "en") -> Matrice:
        version = "global"
        check_params(lang=lang, version=version)

        matrix = await MATRICE_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return matrix  # type: ignore

    @strawberry.field(name="matrices")
    async def get_matrices(
        self, lang: str = "en", includeUnreleased: bool = False
    ) -> List[Matrice]:
        version = "global"
        check_params(lang=lang, version=version)

        matrix = await MATRICE_REPO.get_all(lang=lang, version=VERSIONS(version))

        if not includeUnreleased:
            matrix = filter(filter_released, matrix)

        return matrix  # type: ignore

    @strawberry.field(name="achievement")
    async def get_achivement(self, id: str, lang: str = "en") -> Achievement:
        version = "global"
        check_params(lang=lang, version=version)

        achivement = await ACHIEV_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return achivement  # type: ignore

    @strawberry.field(name="achievements")
    async def get_achivements(self, lang: str = "en") -> List[Achievement]:
        version = "global"
        check_params(lang=lang, version=version)

        achivements = await ACHIEV_REPO.get_all(lang=lang, version=VERSIONS(version))
        return achivements  # type: ignore

    @strawberry.field(name="relic")
    async def get_relic(self, id: str, lang: str = "en") -> Relic:
        version = "global"
        check_params(lang=lang, version=version)

        relic = await RELIC_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return relic  # type: ignore

    @strawberry.field(name="relics")
    async def get_relics(self, lang: str = "en") -> List[Relic]:
        version = "global"
        check_params(lang=lang, version=version)

        relics = await RELIC_REPO.get_all(lang=lang, version=VERSIONS(version))
        return relics  # type: ignore

    @strawberry.field(name="outfit")
    async def get_outfit(self, id: str, lang: str = "en") -> Outfit:
        version = "global"
        check_params(lang=lang, version=version)

        outfit = await OUTFIT_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return outfit  # type: ignore

    @strawberry.field(name="outfits")
    async def get_outfits(self, lang: str = "en") -> List[Outfit]:
        version = "global"
        check_params(lang=lang, version=version)

        outfits = await OUTFIT_REPO.get_all(lang=lang, version=VERSIONS(version))
        return outfits  # type: ignore

    @strawberry.field(name="servant")
    async def get_servant(self, id: str, lang: str = "en") -> SmartServant:
        version = "global"
        check_params(lang=lang, version=version)

        servant = await SERVAN_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return servant  # type: ignore

    @strawberry.field(name="servants")
    async def get_servants(self, lang: str = "en") -> List[SmartServant]:
        version = "global"
        check_params(lang=lang, version=version)

        servants = await SERVAN_REPO.get_all(lang=lang, version=VERSIONS(version))
        return servants  # type: ignore

    @strawberry.field(name="mount")
    async def get_mount(self, id: str, lang: str = "en") -> Mount:
        version = "global"
        check_params(lang=lang, version=version)

        mount = await MOUNTS_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return mount  # type: ignore

    @strawberry.field(name="mounts")
    async def get_mounts(self, lang: str = "en") -> List[Mount]:
        version = "global"
        check_params(lang=lang, version=version)

        mounts = await MOUNTS_REPO.get_all(lang=lang, version=VERSIONS(version))
        return mounts  # type: ignore

    @strawberry.field(name="food")
    async def get_food(self, id: str, lang: str = "en") -> Food:
        version = "global"
        check_params(lang=lang, version=version)

        food = await FOOD_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return food  # type: ignore

    @strawberry.field(name="foods")
    async def get_foods(self, lang: str = "en") -> List[Food]:
        version = "global"
        check_params(lang=lang, version=version)

        foods = await FOOD_REPO.get_all(lang=lang, version=VERSIONS(version))
        return foods  # type: ignore

    @strawberry.field(name="item")
    async def get_item(self, id: str, lang: str = "en") -> Item:
        version = "global"
        check_params(lang=lang, version=version)

        item = await ITEM_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return item  # type: ignore

    @strawberry.field(name="items")
    async def get_items(self, lang: str = "en") -> List[Item]:
        version = "global"
        check_params(lang=lang, version=version)

        items = await ITEM_REPO.get_all(lang=lang, version=VERSIONS(version))
        return items  # type: ignore

    @strawberry.field(name="banners")
    async def get_banners(self, includeUnreleased: bool = False) -> List[Banner]:

        if not includeUnreleased:
            return list(filter(lambda x: x.isReleased, GB_BANNERS))  # type: ignore

        return GB_BANNERS  # type: ignore

    @strawberry.field(name="guidebook")
    async def get_guidebook(self, id: str, lang: str = "en") -> Guidebook:
        version = "global"
        check_params(lang=lang, version=version)

        item = await GUIDEBOOK_REPO.get(
            EntityBase(id=id), lang=lang, version=VERSIONS(version)
        )
        return item  # type: ignore

    @strawberry.field(name="guidebooks")
    async def get_guidebooks(self, lang: str = "en") -> List[Guidebook]:
        version = "global"
        check_params(lang=lang, version=version)

        items = await GUIDEBOOK_REPO.get_all(lang=lang, version=VERSIONS(version))
        return items  # type: ignore


graphql = GraphQLRouter[Any, Any](
    schema=strawberry.Schema(query=Query),
    path="/graphql",
    keep_alive=True,
    allow_queries_via_get=False,
)
METADATA = {
    "name": "GraphQL",
    "description": "GraphQL provides a complete and understandable description of the data \n\n **SOME FIELDS CONTAINS CN DATA**",
    "externalDocs": {
        "description": "GraphQL docs",
        "url": "https://api.toweroffantasy.info/",
    },
}
