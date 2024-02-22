from fastapi import APIRouter, Path, Query

from api.enums import RELICS, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import RelicRepo
from api.infra.entitys import Relic, EntityBase


RELIC_REPO = RelicRepo()

router = APIRouter(prefix="/relics", tags=["Relics"])
METADATA = {
    "name": "Relics",
    "description": (
        "Relics are tools that aid the player in exploration or combat \t\n"
        "DOES NOT CONTAINS CN DATA"
    ),
}

INCLUDE = {"id", "name", "icon", "rarity", "version"}


@router.get("/{id}", name="Get relic", response_model=Relic)
async def get_relic(
    id: RELICS = Path(description="Relic ID"),
    lang: LANGS = Query(LANGS("en"), description="Language code"),
    include: bool = Query(True, description="Include all data keys"),
):
    """
    **Return** \n
        Relic
    """

    relic = await RELIC_REPO.get(EntityBase(id=id), lang, VERSIONS("global"))
    if include:
        return PrettyJsonResponse(relic.model_dump())
    else:
        return PrettyJsonResponse(relic.model_dump(include=INCLUDE))


@router.get("", name="All relics", response_model=list[Relic])
async def get_all_relics(
    lang: LANGS = Query(LANGS("en"), description="Language code"),
    include: bool = Query(False, description="Include all data keys"),
):
    """
    **Return** \n
        List[Relic]
    """

    relics = await RELIC_REPO.get_all(lang, VERSIONS("global"))
    if include:
        return PrettyJsonResponse([relic.model_dump() for relic in relics])
    else:
        return PrettyJsonResponse(
            [relic.model_dump(include=INCLUDE) for relic in relics]
        )
