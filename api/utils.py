
import re

from typing import Any

from api.enums import LANGS


def bold_numbers(text: str):
    return re.sub(r'\d+(.\d+)?%?', lambda x: f'**{x.group(0)}**' 
                  if text[x.span(0)[0]-1] not in ('*', '+', '-') or text[x.span(0)[1]] not in ('*', '+', '-') else x.group(0), 
                  text.replace('<shuzhi>', '').replace('</>', ''), flags=re.IGNORECASE)


def replace_cv(text: str):
    return text.replace('CV : ', '')

def replace_icon(text: str):
    if '/Game/Resources/' in text:
        return text.replace('/Game/Resources', '/assets')
    else:
        return text

def replace_rating(text: str, lang: LANGS):
    return f'/assets/L10N/{lang}/{text.replace("/Game/Resources/", "")}'


def put_imitation_icon(text: str):
    if '/assets' in text:
        return text
    return f'/assets/UI/huanxing/lihui/{text}'

def check_string(text: str):
    if text.lower() == 'none':
        return None
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
    

def filter_func(model: dict[str, Any], filter: dict[str, Any]):
    for filter_key, filter_value in filter.items():
        for key, value in model.items():
            if filter_key.lower() == key.lower():

                if isinstance(filter_value, str) and isinstance(value, str):
                    if filter_value.lower() in value.lower():
                        yield True
                    else:
                        yield False

                elif isinstance(filter_value, (int, float, bool)) and isinstance(value, (int, float, bool)):
                    if filter_value == value:
                        yield True
                    else:
                        yield False


