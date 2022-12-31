import bin.List as List
import hook.Pool as p
import re


class Loop():
    def __init__(self) -> None:

        p.reld = False

        def loop() -> None:

            # Clean string from unwanted spaces, to lower, remove all special characters,
            # translate text to english and split each space
            i = re.sub(r'[^a-zA-Z0-9 ]', '',
                       p.t(input('> '), src='auto', lang='en').strip().lower()
                       ).split()

            res = List.Learn.conditions(i)

            if p.run:

                # print('args', i)
                # print('res', f'\'{res}\'')

                if not(res == '' or len(i) == 0):
                    print('\t' + p.t(f'{p.botname} says') + ':')
                    print('\t' + p.t(res))
                loop()
        loop()
