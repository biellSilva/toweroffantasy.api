
from fastapi import APIRouter
from typing import Any

from api.enums import SIMULACRAS, LANGS
from api.core.response import PrettyJsonResponse

from api.infra.repository import SimulacraRepo, WeaponRepo, MatriceRepo
from api.infra.entitys import EntityBase, Simulacra_v2


router = APIRouter(prefix='/simulacra-v2', tags=['simulacra-v2'])

SIMULACRA_REPO = SimulacraRepo()
MATRICE_REPO = MatriceRepo()
WEAPON_REPO = WeaponRepo()

@router.get('/{id}', response_model=Simulacra_v2)
async def get_simulacra(id: SIMULACRAS, lang: LANGS = LANGS('en')):
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
        Simulacra
    '''
    
    if simulacra := await SIMULACRA_REPO.get(EntityBase(id=id), lang):
        if simulacra.weapon_id:
            weapon = await WEAPON_REPO.get(EntityBase(id=simulacra.weapon_id), lang)
        else:
            weapon = None

        matrice = await MATRICE_REPO.get_by_name(simulacra.name, lang)

        data = simulacra.model_dump()
        data.update({'weapon': weapon, 'matrice': matrice})

        return PrettyJsonResponse(Simulacra_v2(**data).model_dump())
    

@router.get('', response_model=list[Simulacra_v2])
async def get_all_simulacra(lang: LANGS = LANGS('en')):
    '''
    **Query Params** \n
        lang:
            type: string
            default: en
            desc: possible languages to use
            
    **Return** \n
        List[Simulacra_v2]
    '''
    
    simu_lista: list[dict[str, Any]] = []

    for simulacra in await SIMULACRA_REPO.get_all(lang):
        if simulacra.weapon_id:
            weapon = await WEAPON_REPO.get(EntityBase(id=simulacra.weapon_id), lang)
        else:
            weapon = None

        matrice = await MATRICE_REPO.get_by_name(simulacra.name, lang)

        data = simulacra.model_dump()
        data.update({'weapon': weapon, 'matrice': matrice})
        
        simu_lista.append(Simulacra_v2(**data).model_dump())
    
    return PrettyJsonResponse(simu_lista)