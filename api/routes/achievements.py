
from fastapi import APIRouter, Path, Query

from api.enums import ACHIEVS, LANGS, VERSIONS

from api.infra.entitys import Achievement, EntityBase
from api.infra.repository import AchievementRepo

from api.core.response import PrettyJsonResponse


ACHIEV_REPO = AchievementRepo()

router = APIRouter(prefix="/achievements", tags=["Achievements"])
METADATA = {
    'name': 'Achievements',
    'description': ('Player\'s achievements\t\n'
                   'DOES NOT CONTAINS CN DATA'),
}

INCLUDE = {'id', 'name', 'icon', 'tags'}


@router.get('/{id}', name='Get achievement', response_model=Achievement)
async def get_achiev(id: ACHIEVS = Path(description='Achievement ID'), 
                     lang: LANGS = Query(LANGS('en'), description='Language code'), 
                     include: bool = Query(True, description='Include all data keys')):
    '''  
    **Return** \t\n
        Achievement
    '''

    achieve = await ACHIEV_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(achieve.model_dump())
    else:
        return PrettyJsonResponse(achieve.model_dump(include=INCLUDE))
    


@router.get('', name='All achievements', response_model=list[Achievement])
async def get_all_achievs(lang: LANGS = Query(LANGS('en'), description='Language code'), 
                          include: bool = Query(True, description='Include all data keys')):
    '''
    **Return** \t\n
        List[Achievement]
    '''

    achievs = await ACHIEV_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([achiev.model_dump() for achiev in achievs])
    else:
        return PrettyJsonResponse([achiev.model_dump(include=INCLUDE) for achiev in achievs])