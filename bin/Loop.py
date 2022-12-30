import bin.Learn as Learn
import hook.Pool as p
import re


class Loop():
    def __init__(self) -> None:

        p.reld = False

        def loop() -> None:

            # Clean string from unwanted spaces, to lower, remove all special characters,
            # translate text to english and split each space
            i = re.sub(r'[^a-zA-Z0-9 ]', '',
                       p.t(input('> '), src=p.lang, lang='en').strip().lower()
                       ).split()

            # print(i)

            res = Learn.Learn.conditions(i)

            if p.run:
                if res != '':
                    print('\t' + p.t(f'{p.botname} says') + ':')
                    print('\t' + p.t(res))
                loop()
        loop()
