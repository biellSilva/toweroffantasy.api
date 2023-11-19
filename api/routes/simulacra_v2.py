
from fastapi import APIRouter

from api.enums import SIMULACRA, LANGS, VERSIONS

from api.core.response import PrettyJsonResponse

from api.infra.repository import SimulacraV2Repo
from api.infra.entitys import EntityBase, Simulacra_v2


SIMULACRA_REPO = SimulacraV2Repo()

router = APIRouter(prefix='/simulacra-v2', tags=['Simulacra v2'])
METADATA = {
    'name': 'Simulacra v2',
    'description': 'Simulacra v2 is the same as /simulacra, except it contains Weapons and Matrices if possible \n\n **DOES NOT CONTAINS CN DATA**',
    }


@router.get('/{id}', name='Get Simulacrum', response_model=Simulacra_v2)
async def get_simulacrum(id: SIMULACRA, lang: LANGS = LANGS('en')):
    '''
    **Path Param** \n
        id: 
            type: string
            required: True
            desc: Imitation/Simulacra ID

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: Possible languages
            
    **Return** \n
        Simulacra_v2
    '''
    
    simulacrum = await SIMULACRA_REPO.get(EntityBase(id=id), lang, version=VERSIONS('global'))
    return PrettyJsonResponse(simulacrum.model_dump())
    

@router.get('', name='All Simulacra', response_model=list[Simulacra_v2])
async def get_simulacra(lang: LANGS = LANGS('en')):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: Possible languages
            
    **Return** \n
        List[Simulacra_v2]
    '''
    
    simulacra = await SIMULACRA_REPO.get_all(lang, version=VERSIONS('global'))
    return PrettyJsonResponse([simulacrum.model_dump() for simulacrum in simulacra])