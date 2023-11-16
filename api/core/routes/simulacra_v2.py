
from fastapi import APIRouter

from api.enums import SIMULACRAS, LANGS
from api.core.response import PrettyJsonResponse

from api.infra.repository import SimulacraV2Repo
from api.infra.entitys import EntityBase, Simulacra_v2


router = APIRouter(prefix='/simulacra-v2', tags=['simulacra-v2'])

SIMULACRA_REPO = SimulacraV2Repo()


@router.get('/{id}', name='Get Simulacrum', response_model=Simulacra_v2)
async def get_simulacrum(id: SIMULACRAS, lang: LANGS = LANGS('en')):
    '''
    **Path Param** \n
        id: 
            type: string
            required: True
            desc: imitation_id

    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
    **Return** \n
        Simulacra_v2
    '''
    
    if simulacrum := await SIMULACRA_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(simulacrum.model_dump())
    

@router.get('', name='All Simulacra', response_model=list[Simulacra_v2])
async def get_simulacra(lang: LANGS = LANGS('en')):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
    **Return** \n
        List[Simulacra_v2]
    '''
    
    if simulacra := await SIMULACRA_REPO.get_all(lang):
        return PrettyJsonResponse([simulacrum.model_dump() for simulacrum in simulacra])