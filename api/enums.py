
from enum import StrEnum
from os import listdir


class Lang(StrEnum):
    en = 'en-US'
    pt = 'pt-BR'


__simulacras_new_names: list[str] = [file.removesuffix('.json') for file in listdir('src/data/en-US/simulacra_v2')]
SIMULACRAS_V2 = StrEnum('SIMULACRAS_NEW', __simulacras_new_names)

__simulacras_names: list[str] = [file.removesuffix('.json') for file in listdir('src/data/en-US/simulacra')]
SIMULACRAS = StrEnum('SIMULACRAS', __simulacras_names)

__matrices_names: list[str] = [file.removesuffix('.json') for file in listdir('src/data/en-US/matrices')]
MATRICES = StrEnum('MATRICES', __matrices_names)

__weapons_names: list[str] = [file.removesuffix('.json') for file in listdir('src/data/en-US/weapons')]
WEAPONS = StrEnum('WEAPONS', __weapons_names)

__relics_names: list[str] = [file.removesuffix('.json') for file in listdir('src/data/en-US/relics')]
RELICS = StrEnum('RELICS', __relics_names)