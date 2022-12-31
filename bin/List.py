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

        if (
            p.validateList(i, ['exit', 'end', 'goodbye'], 1) or
            p.listHasNext(i, 'see') and p.validateList(i[1:], ['you', 'ya'], 1) or
            p.validateList(i, ['reload', 'relaunch', 'reboot'], 1)  # reload
        ):
            p.run = False
            if p.validateList(i, ['reload', 'relaunch', 'reboot'], 1):
                p.reld = True

        elif p.validateList(i, ['hello', 'hi'], 1):
            res = 'Hello!'

        elif p.validateList(i, ['how', 'are', 'you']):
            res = 'If you are fine me too'

        elif p.validateList(i, ['tell', 'fact']):
            with requests.get('https://type.fit/api/quotes') as url:
                res = json.loads(url.text)
                res = res[rand.randint(0, len(res))]['text']

        elif (
            (
                p.validateList(i, ['change', 'set'], 1) and
                'name' in i
            ) or 'rename' in i and not
            p.validateList(i, ['my'])
        ):
            if p.listHasNext(i, 'to'):
                i = i[i.index('to') + 1]
            else:
                i = p.t(p.botInput('To name'),
                        src='auto', lang='en').lower()

            p.botname = p.metadata[0]['bot']['name'] = i

            with open(p.metapath, 'w') as f:
                f.write(json.dumps(p.metadata, indent=4))

            res = f'My name was changed to \'{p.botname}\''

        elif (
            p.validateList(i, ['clear', 'clean'], 1) and
            p.validateList(i, ['terminal', 'console', 'cmd', 'cli'], 1)
        ):
            os.system('cls' if os.name == 'nt' else 'clear')

        elif (
            p.validateList(i, ['change', 'set'], 1) and
            'language' in i and not
            p.validateList(i, ['my'])
        ):
            if p.listHasNext(i, 'to'):
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

        else:
            res = 'I can\'t understand you'

        return res

