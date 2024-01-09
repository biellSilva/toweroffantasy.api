
from fastapi import APIRouter, Path, Query

from api.enums import SERVANTS, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import ServantsRepo
from api.infra.entitys import EntityBase, SmartServant


SERVANTS_REPO = ServantsRepo()

router = APIRouter(prefix='/servants', tags=['Smart Servants'])
METADATA = {
    'name': 'Smart Servants',
    'description': ('Smart servants are "pets" that aid the player in exploration or combat \t\n'
                    'DOES NOT CONTAINS CN DATA'),
}

INCLUDE = {'id', 'name', 'assets', 'element', 'type'}


@router.get('/{id}', name='Get Smart Servant', response_model=SmartServant)
async def get_servant(id: SERVANTS = Path(description='Smart Servant ID'), 
                      lang: LANGS = Query(LANGS('en'), description='Language code'), 
                      include: bool = Query(True, description='Include all data keys')):
    '''       
    **Return** \n
        SmartServant
    '''
    
    servant = await SERVANTS_REPO.get(EntityBase(id=id), lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse(servant.model_dump())
    else:
        return PrettyJsonResponse(servant.model_dump(include=INCLUDE))

@router.get('', name='All Smart Servant', response_model=list[SmartServant])
async def get_all_mounts(lang: LANGS = Query(LANGS('en'), description='Language code'), 
                         include: bool = Query(False, description='Include all data keys')):
    '''
    **Return** \n
        List[SmartServant]
    '''
    
    servants = await SERVANTS_REPO.get_all(lang, VERSIONS('global'))
    if include:
        return PrettyJsonResponse([servant.model_dump() for servant in servants])
    else:
        return PrettyJsonResponse([servant.model_dump(include=INCLUDE) for servant in servants])
    