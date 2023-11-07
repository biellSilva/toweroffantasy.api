
from fastapi import APIRouter

from api.enums import WEAPONS, LANGS

from api.core.response import PrettyJsonResponse
from api.core.exceptions import ItemNotFound

from api.infra.entitys import Weapon, EntityBase
from api.infra.repository import WeaponRepo


router = APIRouter(prefix='/weapons', tags=['weapons'])

WEAPON_REPO = WeaponRepo()


@router.get('/{id}', response_model=Weapon)
async def get_weapon(id: WEAPONS, lang: LANGS = LANGS('en')):
    '''
    returns \n
        Weapon
    '''

    if weapon := await WEAPON_REPO.get(EntityBase(id=id), lang):
        return PrettyJsonResponse(weapon.model_dump())

    else:
        raise ItemNotFound(headers={'error': f'{id} not found in {lang}'})


@router.get('', response_model=Weapon)
async def get_all_weapons(lang: LANGS = LANGS('en')):
    '''
    returns \n
        Dict[Weapon.id: Weapon]
    '''

    if weapons := await WEAPON_REPO.get_all(lang):
        return PrettyJsonResponse({weapon.id: weapon.model_dump() 
                                   for weapon in weapons})

    else:
        raise ItemNotFound(headers={'error': f'{lang} not found'})