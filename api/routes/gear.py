from fastapi import APIRouter, Path, Query

from api.enums import GEARS, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse
from api.infra.entitys.base import EntityBase
from api.infra.entitys.gear import Gear
from api.infra.repository.gear import GearRepo


ITEM_REPO = GearRepo()

router = APIRouter(prefix="/gear", tags=["Gears"])
METADATA = {
    "name": "Gears",
    "description": "Gear are in-game equipment \t\n DOES NOT CONTAINS CN DATA",
}

INCLUDE = {"id", "name", "rarity", "icon"}


@router.get("/{id}", response_model=Gear)
async def get_item(
    id: GEARS = Path(description="Gear ID"),
    lang: LANGS = Query(LANGS("en"), description="Language code"),
    include: bool = Query(True, description="Include all data keys"),
):
    """
    **Return** \n
        Gear
    """

    item = await ITEM_REPO.get(EntityBase(id=id), lang, VERSIONS("global"))
    if include:
        return PrettyJsonResponse(item.model_dump())
    else:
        return PrettyJsonResponse(item.model_dump(include=INCLUDE))


@router.get("", response_model=list[Gear])
async def get_all_items(
    lang: LANGS = Query(LANGS("en"), description="Language code"),
    include: bool = Query(False, description="Include all data keys"),
):
    """
    **Return** \n
        List[Gear]
    """

    items = await ITEM_REPO.get_all(lang, VERSIONS("global"))
    if include:
        return PrettyJsonResponse([item.model_dump() for item in items])
    else:
        return PrettyJsonResponse([item.model_dump(include=INCLUDE) for item in items])
