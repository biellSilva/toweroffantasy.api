
from fastapi import APIRouter

from api.enums import SERVANTS, LANGS

from api.core.exceptions import ItemNotFound
from api.core.response import PrettyJsonResponse

from api.infra.repository import ServantsRepo
from api.infra.entitys import EntityBase, SmartServant


router = APIRouter(prefix='/servants', tags=['Smart Servants'])

SERVANTS_REPO = ServantsRepo()


@router.get('/{id}', name='Get Smart Servant', response_model=SmartServant)
async def get_servant(id: SERVANTS, lang: LANGS = LANGS('en'), include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: str
            required: True
            desc: servant_id

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
        
        include:
            type: bool
            default: True
            desc: Include all data keys
            
    **Return** \n
        SmartServant
    '''
    
    if mount := await SERVANTS_REPO.get(EntityBase(id=id), lang):
        if include:
            return PrettyJsonResponse(mount.model_dump())
        else:
            return PrettyJsonResponse(mount.model_dump(include={'id', 'name', 'assets', 'element', 'type'}))
    else:
        raise ItemNotFound(detail={'error': f'{id} not found in {lang}'})

@router.get('', name='All Smart Servant', response_model=list[SmartServant])
async def get_all_mounts(lang: LANGS = LANGS('en'), include: bool = False):
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
            
    **Return** \n
        List[SmartServant]
    '''
    
    if servants := await SERVANTS_REPO.get_all(lang):
        if include:
            return PrettyJsonResponse([servant.model_dump() for servant in servants])
        else:
            return PrettyJsonResponse([servant.model_dump(include={'id', 'name', 'assets', 'element', 'type'}) for servant in servants])
    
    else:
        raise ItemNotFound(detail={'error': f'{lang} not found'})