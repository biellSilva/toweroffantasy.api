
from fastapi import APIRouter

from api.enums import SERVANTS, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import ServantsRepo
from api.infra.entitys import EntityBase, SmartServant


SERVANTS_REPO = ServantsRepo()

router = APIRouter(prefix='/servants', tags=['Smart Servants'])
METADATA = {
    'name': 'Smart Servants',
    'description': 'Smart servants are "pets" that aid the player in exploration or combat \n\n **DOES NOT CONTAINS CN DATA**',
    }


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
    
    servant = await SERVANTS_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(servant.model_dump())
    else:
        return PrettyJsonResponse(servant.model_dump(include={'id', 'name', 'assets', 'element', 'type'}))

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
    
    servants = await SERVANTS_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([servant.model_dump() for servant in servants])
    else:
        return PrettyJsonResponse([servant.model_dump(include={'id', 'name', 'assets', 'element', 'type'}) for servant in servants])
    