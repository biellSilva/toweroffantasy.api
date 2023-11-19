
from fastapi import APIRouter

from api.enums import ACHIEVS, LANGS, VERSIONS

from api.infra.entitys import Achievement, EntityBase
from api.infra.repository import AchievementRepo

from api.core.response import PrettyJsonResponse


ACHIEV_REPO = AchievementRepo()

router = APIRouter(prefix="/achievements", tags=["Achievements"])
METADATA = {
    'name': 'Achievements',
    'description': 'Player\'s achievements \n\n **DOES NOT CONTAINS CN DATA**',
    }


@router.get('/{id}', name='Get achievement', response_model=Achievement)
async def get_achiev(id: ACHIEVS, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: achievement_id
            
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
        
        include:
            type: bool
            default: True
            desc: Include all data keys
            
    return \n
        Achievement
    '''

    achieve = await ACHIEV_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(achieve.model_dump())
    else:
        return PrettyJsonResponse(achieve.model_dump(include={'id', 'name', 'icon', 'tags'}))
    


@router.get('', name='All achievements', response_model=list[Achievement])
async def get_all_achievs(lang: LANGS = LANGS('en'), include: bool = False):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
        
        include:
            type: bool
            default: False
            desc: Include all data keys
            
    return \n
        List[Achievement]
    '''

    achievs = await ACHIEV_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([achiev.model_dump() for achiev in achievs])
    else:
        return PrettyJsonResponse([achiev.model_dump(include={'id', 'name', 'icon', 'tags'}) for achiev in achievs])