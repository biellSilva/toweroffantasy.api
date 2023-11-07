
from fastapi import APIRouter

from api.enums import SIMULACRAS, LANGS
from api.core.response import PrettyJsonResponse

from api.infra.repository import SimulacraRepo, WeaponRepo, MatriceRepo
from api.infra.entitys import EntityBase, Simulacra_v2


router = APIRouter(prefix='/simulacra-v2', tags=['simulacra_v2'])

SIMULACRA_REPO = SimulacraRepo()
MATRICE_REPO = MatriceRepo()
WEAPON_REPO = WeaponRepo()

@router.get('/{id}', response_model=Simulacra_v2)
async def get_simulacra(id: SIMULACRAS, lang: LANGS = LANGS('en')):
    ''' Get simulacra with his weapon and matrice based on id '''
    
    if simulacra := await SIMULACRA_REPO.get(EntityBase(id=id), lang):
        weapon = await WEAPON_REPO.get(EntityBase(id=simulacra.weapon), lang)
        matrice = await MATRICE_REPO.get_by_name(simulacra.name, lang)
        data = simulacra.model_dump()
        data.update({'weapon': weapon, 'matrice': matrice})
        return PrettyJsonResponse(Simulacra_v2(**data).model_dump())

@router.get('', response_model=dict[str, Simulacra_v2])
async def get_all_simulacra(lang: LANGS = LANGS('en')):
    ''' Get simulacra with his weapon and matrice based on id '''
    
    _: dict[str, Simulacra_v2] = {}

    for simulacra in await SIMULACRA_REPO.get_all(lang):
        weapon = await WEAPON_REPO.get(EntityBase(id=simulacra.weapon), lang)
        matrice = await MATRICE_REPO.get_by_name(simulacra.name, lang)
        data = simulacra.model_dump()
        data.update({'weapon': weapon, 'matrice': matrice})
        _.update({simulacra.id: Simulacra_v2(**data)})
    
    return PrettyJsonResponse({id: simulacra.model_dump() for id, simulacra in _.items()})