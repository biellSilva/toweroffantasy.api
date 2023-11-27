
from fastapi import APIRouter

from api.enums import SIMULACRA, SIMULACRA_CN, LANGS, LANGS_CN, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.entitys import Simulacra, EntityBase
from api.infra.repository import SimulacraRepo


SIMU_REPO = SimulacraRepo()

router = APIRouter(prefix='/simulacra', tags=['Simulacra'])
METADATA = {
    'name': 'Simulacra',
    'description': 'Simulacra are the player\'s representation of the characters found in Tower of Fantasy \n\n **CONTAINS CN DATA**',
    }

INCLUDE = {'id', 'Name', 'AssetsA0', 'WeaponId', 'MatrixId'}


@router.get('/{id}', name='Get simulacrum', response_model=Simulacra)
async def get_simulacrum(id: SIMULACRA | SIMULACRA_CN, 
                        #  version: VERSIONS = VERSIONS('global'),
                         lang: LANGS | LANGS_CN = LANGS('en'), 
                         include: bool = True):
    '''
    **Path Param** \n
        id: 
            type: string
            required: True
            desc: Imitation/Simulacrum ID
            schema: SIMULACRA | SIMULACRA_CN


    **Query Params** \n
        version (DISABLED):
            type: string
            default: global
            desc: Game version
            schema: VERSIONS

        lang:
            type: string
            default: en
            desc: Possible languages
            schema: LANGS | LANGS_CN

        include:
            type: bool
            default: True
            desc: Include all data keys
            
    **Return** \n
        Simulacra

    '''

    if version == 'china': # handling cn version
        lang = LANGS_CN('cn')
    
    simulacra = await SIMU_REPO.get(EntityBase(id=id), lang, version=VERSIONS('global'))

    if include:
        return PrettyJsonResponse(simulacra.model_dump())
    else:
        return PrettyJsonResponse(simulacra.model_dump(include=INCLUDE))
    


@router.get('', name='All simulacra', response_model=list[Simulacra])
async def get_all_simulacra( # version: VERSIONS = VERSIONS('global'), 
                            lang: LANGS | LANGS_CN = LANGS('en'), 
                            include: bool = False):
    '''
    **Query Params** \n
        version (DISABLED):
            type: str
            default: global
            desc: Game version
            schema: VERSIONS
        
        lang:
            type: string
            default: en
            desc: Possible languages
            schema: LANGS | LANGS_CN
    
        include:
            type: bool
            default: False
            desc: Include all data keys
            
    **Return** \n
        List[Simulacra]

    '''

    if version == 'china': # handling cn version
        lang = LANGS_CN('cn')
    
    simulacras = await SIMU_REPO.get_all(lang=lang, version=VERSIONS('global'))

    if include:
        return PrettyJsonResponse([simulacra.model_dump() for simulacra in simulacras])
    else:
        return PrettyJsonResponse([simulacra.model_dump(include=INCLUDE) for simulacra in simulacras])
    