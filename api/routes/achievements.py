
from fastapi import APIRouter

from api.enums import ACHIEVS, LANGS

from api.infra.entitys import Achievement, EntityBase
from api.infra.repository import AchievementRepo

from api.core.response import PrettyJsonResponse
from api.core.exceptions import ItemNotFound


router = APIRouter(prefix="/achievements", tags=["Achievements"])

ACHIEV_REPO = AchievementRepo()

@router.get('/{id}', name='Get achievement', response_model=Achievement)
async def get_achiev(id: ACHIEVS, lang: LANGS = LANGS('en')):
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
            
    return \n
        Achievement
    '''

    if achieve := await ACHIEV_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(achieve.model_dump())
    
    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})


@router.get('', name='All achievements', response_model=list[Achievement])
async def get_all_achievs(lang: LANGS = LANGS('en')):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
    return \n
        List[Achievement]
    '''

    if achieves := await ACHIEV_REPO.get_all(lang):
        return PrettyJsonResponse([achieve.model_dump() for achieve in achieves])
    
    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})