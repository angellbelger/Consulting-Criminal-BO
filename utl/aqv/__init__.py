from utl.lay import colour as cl


def readint(msg):
    while True:

        try:
            x = int(input(msg))

        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')
            continue

        else:
            return x


def titleFor(txt, num1=0):
    print(f'{cl["b"]}-' * num1)
    print(f'{txt.center(num1)}')
    print(f'-' * num1)
    print(f'{cl["limit"]}')


def onlyBool(txt):
    x = ''
    while True:
        try:
            x = str(input(txt)).title()[0]
        
        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')
        
        else:
            return x


def boolTitle(txt):
    x = ''
    bool = ''
    while True:
        try:
            x = str(input(txt)).title().strip()
            bool = str(input(f'It is correct: {cl["p"]}"{x}"{cl["limit"]} \nYour answer [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]: '))[0].title()

            if bool == 'N':
                continue

            elif bool not in 'NY':
                print(f'{cl["r"]}Please, type a valid command.{cl["limit"]}')

            else:
                return x
        
        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')


def bool(txt):
    x = ''
    bool = ''
    while True:
        try:
            x = str(input(txt)).strip()
            bool = str(input(f'It is correct: {cl["p"]}"{x}"{cl["limit"]} \nYour answer [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]: '))[0].title()

            if bool == 'N':
                continue

            elif bool not in 'NY':
                print(f'{cl["r"]}Please, type a valid command.{cl["limit"]}')

            else:
                return x
        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')


def boolNumber(txt):
    while True:
        try:
            x = int(input(txt))
        except Exception as error:
            print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')
            continue
        else:
            bool = ''
            bool = str(input(f'It is correct: {cl["p"]}"{x}"{cl["limit"]} \nYour answer [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]: '))[0].title()

            if bool not in 'NY':
                print(f'{cl["r"]}Please, type a valid command.{cl["limit"]}')
            
            elif bool == 'N':
                continue
                
            else:
                return x


def line(x):
    print('-' * x)