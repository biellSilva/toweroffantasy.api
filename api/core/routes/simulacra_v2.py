
from fastapi import APIRouter

from api.enums import SIMULACRAS, LANGS
from api.core.response import PrettyJsonResponse

from api.infra.repository import SimulacraRepo, WeaponRepo, MatriceRepo
from api.infra.entitys import EntityBase, Simulacra_v2


router = APIRouter(prefix='/simulacra/v2', tags=['simulacra_v2'])

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
        return PrettyJsonResponse(Simulacra_v2(**data).model_dump(exclude_none=True))