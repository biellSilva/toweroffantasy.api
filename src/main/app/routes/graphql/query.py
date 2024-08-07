from typing import List

import strawberry

from src.domain.models.achievements import AchievementType
from src.domain.models.banner import BannerType
from src.domain.models.food import FoodType
from src.domain.models.gears import GearType
from src.domain.models.guidebook import GuideBookType
from src.domain.models.items import ItemType
from src.domain.models.matrices import MatrixType
from src.domain.models.mounts import MountType
from src.domain.models.outfits import OutfitType
from src.domain.models.relics import RelicType
from src.domain.models.researchs import ResearchType
from src.domain.models.servants import SmartServantType
from src.domain.models.simulacra import SimulacraType
from src.domain.models.simulacra_v2 import SimulacraV2Type
from src.domain.models.weapons import WeaponType
from src.main.factories.controller.achievements.find import (
    FindAchievementsControllerFactory,
)
from src.main.factories.controller.achievements.get_all import (
    GetAllAchievementsControllerFactory,
)
from src.main.factories.controller.banners.find import FindBannersControllerFactory
from src.main.factories.controller.food.find import FindFoodControllerFactory
from src.main.factories.controller.food.get_all import GetAllFoodControllerFactory
from src.main.factories.controller.gears.find import FindGearsControllerFactory
from src.main.factories.controller.gears.get_all import GetAllGearsControllerFactory
from src.main.factories.controller.guidebooks.find import (
    FindGuidebooksControllerFactory,
)
from src.main.factories.controller.guidebooks.get_all import (
    GetAllGuidebooksControllerFactory,
)
from src.main.factories.controller.items.find import FindItemsControllerFactory
from src.main.factories.controller.items.get_all import GetAllItemsControllerFactory
from src.main.factories.controller.matrices.find import FindMatricesControllerFactory
from src.main.factories.controller.matrices.get_all import (
    GetAllMatricesControllerFactory,
)
from src.main.factories.controller.mount.find import FindMountControllerFactory
from src.main.factories.controller.mount.get_all import GetAllMountControllerFactory
from src.main.factories.controller.outfits.find import FindOutfitsControllerFactory
from src.main.factories.controller.outfits.get_all import GetAllOutfitsControllerFactory
from src.main.factories.controller.relics.find import FindRelicsControllerFactory
from src.main.factories.controller.relics.get_all import GetAllRelicsControllerFactory
from src.main.factories.controller.researchs.find import FindResearchControllerFactory
from src.main.factories.controller.researchs.get_all import (
    GetAllResearchsControllerFactory,
)
from src.main.factories.controller.servants.find import FindServantsControllerFactory
from src.main.factories.controller.servants.get_all import (
    GetAllServantsControllerFactory,
)
from src.main.factories.controller.simulacra.find import FindSimulacraControllerFactory
from src.main.factories.controller.simulacra.getall import (
    GetallSimulacraControllerFactory,
)
from src.main.factories.controller.simulacra_v2.find import (
    FindSimulacraV2ControllerFactory,
)
from src.main.factories.controller.simulacra_v2.get_all import (
    GetAllSimulacraV2ControllerFactory,
)
from src.main.factories.controller.weapons.find import FindWeaponsControllerFactory
from src.main.factories.controller.weapons.get_all import GetAllWeaponsControllerFactory


@strawberry.type
class Query:
    simulacrum: SimulacraType = strawberry.field(
        resolver=FindSimulacraControllerFactory.create().handle
    )
    simulacra: List[SimulacraType] = strawberry.field(
        resolver=GetallSimulacraControllerFactory.create().handle
    )

    weapon: WeaponType = strawberry.field(
        resolver=FindWeaponsControllerFactory.create().handle
    )
    weapons: List[WeaponType] = strawberry.field(
        resolver=GetAllWeaponsControllerFactory.create().handle
    )

    matrix: MatrixType = strawberry.field(
        resolver=FindMatricesControllerFactory.create().handle
    )
    matrices: List[MatrixType] = strawberry.field(
        resolver=GetAllMatricesControllerFactory.create().handle
    )

    simulacrum_v2: SimulacraV2Type = strawberry.field(
        resolver=FindSimulacraV2ControllerFactory.create().handle
    )
    simulacra_v2: List[SimulacraV2Type] = strawberry.field(
        resolver=GetAllSimulacraV2ControllerFactory.create().handle
    )

    mount: MountType = strawberry.field(
        resolver=FindMountControllerFactory.create().handle
    )
    mounts: List[MountType] = strawberry.field(
        resolver=GetAllMountControllerFactory.create().handle
    )

    relic: RelicType = strawberry.field(
        resolver=FindRelicsControllerFactory.create().handle
    )
    relics: List[RelicType] = strawberry.field(
        resolver=GetAllRelicsControllerFactory.create().handle
    )

    food: FoodType = strawberry.field(
        resolver=FindFoodControllerFactory.create().handle
    )
    foods: List[FoodType] = strawberry.field(
        resolver=GetAllFoodControllerFactory.create().handle
    )

    achievement: AchievementType = strawberry.field(
        resolver=FindAchievementsControllerFactory.create().handle
    )
    achievements: List[AchievementType] = strawberry.field(
        resolver=GetAllAchievementsControllerFactory.create().handle
    )

    banners: List[BannerType] = strawberry.field(
        resolver=FindBannersControllerFactory.create().handle
    )

    gear: GearType = strawberry.field(
        resolver=FindGearsControllerFactory.create().handle
    )
    gears: List[GearType] = strawberry.field(
        resolver=GetAllGearsControllerFactory.create().handle
    )

    guidebook: GuideBookType = strawberry.field(
        resolver=FindGuidebooksControllerFactory.create().handle
    )
    guidebooks: List[GuideBookType] = strawberry.field(
        resolver=GetAllGuidebooksControllerFactory.create().handle
    )

    item: ItemType = strawberry.field(
        resolver=FindItemsControllerFactory.create().handle
    )
    items: List[ItemType] = strawberry.field(
        resolver=GetAllItemsControllerFactory.create().handle
    )

    outfit: OutfitType = strawberry.field(
        resolver=FindOutfitsControllerFactory.create().handle
    )
    outfits: List[OutfitType] = strawberry.field(
        resolver=GetAllOutfitsControllerFactory.create().handle
    )

    servant: SmartServantType = strawberry.field(
        resolver=FindServantsControllerFactory.create().handle
    )
    servants: List[SmartServantType] = strawberry.field(
        resolver=GetAllServantsControllerFactory.create().handle
    )

    research: ResearchType = strawberry.field(
        resolver=FindResearchControllerFactory.create().handle
    )
    researchs: List[ResearchType] = strawberry.field(
        resolver=GetAllResearchsControllerFactory.create().handle
    )
