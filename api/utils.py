
import re

from typing import TYPE_CHECKING

from api.enums import LANGS
from api.config import SIMULACRA_SORT_ORDER, WEAPON_SORT_ORDER, MATRIX_SORT_ORDER


if TYPE_CHECKING:
    from api.infra.entitys import Simulacra, Weapon, Matrix


def bold_numbers(text: str):
    return re.sub(r'\d+(.\d+)?%?', lambda x: f'**{x.group(0)}**' 
                  if text[x.span(0)[0]-1] not in ('*', '+', '-') or text[x.span(0)[1]] not in ('*', '+', '-') else x.group(0), 
                  text.replace('<shuzhi>', '').replace('</>', ''), flags=re.IGNORECASE)

def replace_cv(text: str):
    if not text or text == '':
        return None
    return text.replace('CV : ', '')

def replace_icon(text: str):
    if '/Game/Resources/' in text:
        return text.replace('/Game/Resources', '/assets')
    else:
        return text

def localized_asset(text: str, lang: LANGS):
    return f'/assets/L10N/{lang}/Resources/{text.replace("/Game/Resources/", "")}'

def put_imitation_icon(text: str):
    if '/assets' in text:
        return text
    return f'/assets/UI/huanxing/lihui/{text}'

def check_string(text: str):
    if text.lower() == 'none':
        return None
    return text

def replace_rarity_asset(text: str):
    if text.lower() == 'none':
        return None
    if '/Game/Resources/' in text:
        return text.replace('/Game/Resources', '/assets')
    else:
        return text

def classifier(number: float):
    if number >= 15:
        return 'SS'
    elif number >= 10.01:
        return 'S'
    elif number >= 8:
        return 'A'
    elif number >= 4:
        return 'B'
    else:
        return 'C'
    
def matrice_set_rework(rarity: str, sets: list[dict[str, str]]):
    if rarity == 'N':
        return [{'need': 4, 'description': sets[0].get('2', '')}]
    elif rarity == 'R':
        return [{'need': 3, 'description': sets[0].get('2', '')}]
    elif rarity == 'SR':
        return [{'need': 3, 'description': sets[0].get('2', '')}]
    elif rarity == 'SSR':
        return [{'need': 2, 'description': sets[0].get('2', '')}, 
                {'need': 4, 'description': sets[0].get('4', '')}]
    else:
        return None

def trait_rework(trait: dict[str, dict[str, str]]):
    return [value for key, value in trait.items() if not key == 'id']

def voice_actors_rework(va: list[dict[str, str]]):
    return {key.lower(): value for i in va for key, value in i.items()}

def classify_rework(value: float):
    return {'tier': classifier(value), 'value': value}

def material_rework(mats: dict[str, int]):
    return [{'id': key.lower(), 'need': value} for key, value in mats.items()]

def pet_material_rework(mats: dict[str, int]):
    return [{'id': key.lower(), 'xpGain': value} for key, value in mats.items()]

def relic_advanc_rework(advanc: list[dict[str, str]]):
    return [value for i in advanc for key, value in i.items() if not key == 'id']


def sort_simulacra(simulacrum: 'Simulacra') -> tuple[int, int]:
    if simulacrum.rarity == 'SSR':
        if simulacrum.banners:
            return (-1, -simulacrum.banners[-1].bannerNo)
        else:
            return (-1, SIMULACRA_SORT_ORDER.index(simulacrum.id))
        
    elif simulacrum.rarity == 'SR':
        if simulacrum.banners:
            return (1, -simulacrum.banners[-1].bannerNo)
        else:
            return (1, SIMULACRA_SORT_ORDER.index(simulacrum.id))
        
    return 2, 1

def sort_weapons(weapon: 'Weapon') -> tuple[int, int]:
    if weapon.rarity == 'SSR':
        if weapon.banners:
            return -1, -weapon.banners[-1].bannerNo
        else:
            return -1, WEAPON_SORT_ORDER.index(weapon.id)
    
    elif weapon.rarity == 'SR':
        if weapon.banners:
            return 1, -weapon.banners[-1].bannerNo
        else:
            return 1, WEAPON_SORT_ORDER.index(weapon.id)
    
    elif weapon.rarity == 'R':
        if weapon.banners:
            return 2, -weapon.banners[-1].bannerNo
        else:
            return 2, WEAPON_SORT_ORDER.index(weapon.id)
    
    return 3, 0
    
def sort_matrices(matrice: 'Matrix') -> tuple[int, int]:
    if matrice.rarity == 'SSR':
        if matrice.banners:
            return -1, -matrice.banners[-1].bannerNo
        else:
            return -1, MATRIX_SORT_ORDER.index(matrice.id)
    
    elif matrice.rarity == 'SR':
        if matrice.banners:
            return 1, -matrice.banners[-1].bannerNo
        else:
            return 1, MATRIX_SORT_ORDER.index(matrice.id)
    
    elif matrice.rarity == 'R':
        if matrice.banners:
            return 2, -matrice.banners[-1].bannerNo
        else:
            return 2, MATRIX_SORT_ORDER.index(matrice.id)

    elif matrice.rarity == 'N':
        if matrice.banners:
            return 3, -matrice.banners[-1].bannerNo
        else:
            return 3, MATRIX_SORT_ORDER.index(matrice.id)
    
    return 4, 0