
from enum import Enum, StrEnum
from os import listdir


class Lang(Enum):
    en = 'en-US'
    pt = 'pt-BR'


__simulacras_names: list[str] = []
for file in listdir('src/data/en-US/simulacra'):
    __simulacras_names.append(file.removesuffix('.json'))

SIMULACRAS = StrEnum('SIMULACRAS', __simulacras_names)