import json
import os
from googletrans import Translator

translator = Translator()

metapath = os.path.join('meta', 'metadata.json')

with open(metapath) as f:
    metadata = json.load(f)

botname = metadata[0]['bot']['name']
lang = metadata[0]['app']['lang']
run = True
reld = True


def t(trlt: str | list, src: str = 'en', lang: str = lang) -> str | list:
    def localtrans(lt: str):
        return translator.translate(lt, src=src, dest=lang).text

    if type(trlt) == str:
        return localtrans(trlt)

    else:
        return [localtrans(trz) for trz in trlt]


def botInput(text: str, autoStrip: bool = True) -> str:
    i = input('({0}) {1}: '.format(botname, t(f'{text}')))
    if autoStrip:
        i = i.strip()

    return i


def validateList(inpt: list, arr: list, num: str = 'auto') -> bool:
    l = len(arr) if num == 'auto' else num
    return len(set(inpt).intersection(arr)) == l
