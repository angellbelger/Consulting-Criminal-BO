from utl.lay import colour as cl
from utl.objects import dataBase


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


def showData(query, actor):
    counter = 0
    for index in range(0, len(dataBase)):
        if query in dataBase[index][f"{actor}"]:
            counter += 1
            titleFor('Search by []', 50)
            print(f'\033[35m{dataBase[index]["date"]["dateDay"]}/{dataBase[index]["date"]["dateMonth"]}/{dataBase[index]["date"]["dateYear"]}\033[m - Time: \033[35m{dataBase[index]["time"]}\033[m')
            print(f'Infrator:{cl["p"]} {dataBase[index]["offender"]}{cl["limit"]}')
            print(f'Endereco/local:{cl["p"]} {dataBase[index]["adress"]}{cl["limit"]}')
            print(f'Ponto de Referência:{cl["p"]} {dataBase[index]["reference"]}{cl["limit"]}')
            print(f'POLICE:{cl["p"]} {dataBase[index]["police"]}{cl["limit"]}')
            print(f'Acionamento por:{cl["p"]} {dataBase[index]["trigger"]}{cl["limit"]}')
            print(f'Tipo de Atendimento:{cl["p"]} {dataBase[index]["type"]}{cl["limit"]}')
    
    if counter == 0:
        print('\nNothing Found.\n')