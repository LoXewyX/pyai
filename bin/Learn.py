import requests
import random as rand
import json
from googletrans import constants
import os

import hook.Pool as p


class Learn():
    def __init__(self) -> None:
        pass

    def conditions(i: str) -> str:

        res = ''

        if p.validateList(i, ['hello']):
            res = 'Hello!'

        elif p.validateList(i, ['tell', 'fact']):
            with requests.get('https://type.fit/api/quotes') as url:
                res = json.loads(url.text)
                res = res[rand.randint(0, len(res))]['text']

        elif p.validateList(i, ['change', 'name']) and not p.validateList(i, ['my']):
            if 'to' in i and len(i) > i.index('to') + 1:
                i = i[i.index('to') + 1]
            else:
                i = p.t(p.botInput('To name'),
                        src='auto', lang='en').lower()

            p.botname = p.metadata[0]['bot']['name'] = i

            with open(p.metapath, 'w') as f:
                f.write(json.dumps(p.metadata, indent=4))

            res = f'My name was changed to \'{p.botname}\''

        elif p.validateList(i, ['clear', 'clean'], 1) and p.validateList(i, ['terminal', 'console', 'cmd', 'cli'], 1):
            os.system('cls' if os.name == 'nt' else 'clear')

        elif p.validateList(i, ['change', 'language']) and not p.validateList(i, ['my']):
            if 'to' in i and len(i) > i.index('to') + 1:
                i = i[i.index('to') + 1]
            else:
                i = p.t(p.botInput('To language'),
                        src='auto', lang='en').lower()

            if i in constants.LANGCODES:

                p.lang = p.metadata[0]['app']['lang'] = i

                with open(p.metapath, 'w') as f:
                    f.write(json.dumps(p.metadata, indent=4))
                res = f'Language was changed to \'{p.lang}\'\nRelaunch the app to display your language'

            else:
                res = f'Language \'{i}\' does not exist'

        elif p.validateList(i, ['language']) and not p.validateList(i, ['my']):
            res = f'My current language is \'{p.lang}\''

        elif p.validateList(i, ['exit', 'end', 'reload'], 1):
            p.run = False
            if 'reload' in i:
                p.reld = True

        else:
            res = 'I can\'t understand you'

        return res
