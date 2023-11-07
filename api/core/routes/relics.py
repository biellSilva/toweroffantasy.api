
from fastapi import APIRouter

from api.enums import RELICS, LANGS

from api.core.response import PrettyJsonResponse
from api.core.exceptions import ItemNotFound

from api.infra.repository import RelicRepo
from api.infra.entitys import Relic, EntityBase


router = APIRouter(prefix='/relics', tags=['relics'])

RELIC_REPO = RelicRepo()


@router.get('/{id}', response_model=Relic)
async def get_relic(id: RELICS, lang: LANGS = LANGS('en')):
    '''
    return \n
        Relic
    '''

    if relic := await RELIC_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(relic.model_dump())
    
    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})

@router.get('', response_model=dict[str, Relic])
async def get_all_relics(lang: LANGS = LANGS('en')):
    '''
    return \n
        Dict[Relic.id: Relic]
    '''

    if relics := await RELIC_REPO.get_all(lang):
        return PrettyJsonResponse({relic.id: relic.model_dump() 
                                   for relic in relics})
    
    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})