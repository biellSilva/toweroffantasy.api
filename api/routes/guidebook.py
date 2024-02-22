from fastapi import APIRouter, Path, Query

from api.enums import GUIDEBOOKS, LANGS, VERSIONS

from api.infra.entitys import EntityBase
from api.infra.entitys.guidebooks import GuideBook

from api.core.response import PrettyJsonResponse
from api.infra.repository.guidebook import GuideBookRepo


GUIDE_REPO = GuideBookRepo()

router = APIRouter(prefix="/guidebooks", tags=["Guidebooks"])
METADATA = {
    "name": "Guidebooks",
    "description": "Contains guidebooks \t\n DOES NOT CONTAINS CN DATA",
}

INCLUDE = {"id", "name", "icon"}


@router.get("/{id}", response_model=GuideBook)
async def get_guidebook(
    id: GUIDEBOOKS = Path(description="Guidebook ID"),
    lang: LANGS = Query(LANGS("en"), description="Language code"),
    include: bool = Query(True, description="Include all data keys"),
):
    """
    **Return** \n
        Guidebook
    """

    item = await GUIDE_REPO.get(EntityBase(id=id), lang, VERSIONS("global"))
    if include:
        return PrettyJsonResponse(item.model_dump())
    else:
        return PrettyJsonResponse(item.model_dump(include=INCLUDE))


@router.get("", response_model=list[GuideBook])
async def get_all_guidebooks(
    lang: LANGS = Query(LANGS("en"), description="Language code"),
    include: bool = Query(False, description="Include all data keys"),
):
    """
    **Return** \n
        List[Guidebook]
    """

    items = await GUIDE_REPO.get_all(lang, VERSIONS("global"))
    if include:
        return PrettyJsonResponse([item.model_dump() for item in items])
    else:
        return PrettyJsonResponse([item.model_dump(include=INCLUDE) for item in items])
