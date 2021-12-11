import datetime
from os import name
from utl.lay import colour as cl
from utl.aqv import readint, titleFor, tiposAtendimentos, boolTitle, bool

print('\n\033[35mHello, World.\033[m\n')

dataBase = list()
people = dict()
dateBO = dict()
menu = ['Data Base', 'Add People', 'Search by keyword', 'Metadata','Exit']
option = 0

okMain = True
while okMain:
    titleFor('BO', 30)
    for c in range(0, len(menu)):
        print(f'{cl["b"]}{c + 1}{cl["limit"]} - {menu[c]}')
    
    option = 0
    option = int(input(f'{cl["b"]}\nOption:{cl["limit"]} '))

    # reading database

    if option == 1:

        ok = True
        while ok:
            titleFor('Data Base', 30)
            if len(dataBase) == 0:
                print('It is empty.')
                ok = False
            else:
                for c in range(0, len(dataBase)):
                    print(f'{cl["b"]}{c}{cl["limit"]} - {dataBase[c]["offender"]}')
                
                ok = True
                while ok:
                    option = readint('See people: ')
                    titleFor('Data')
                    print(f'\033[35m{dataBase[option]["date"]["dateDay"]}/{dataBase[option]["date"]["dateMonth"]}/{dataBase[option]["date"]["dateYear"]}\033[m - Time: \033[35m{dataBase[option]["time"]}\033[m')
                    print(f'Infrator:{cl["p"]} {dataBase[option]["offender"]}{cl["limit"]}')
                    print(f'Endereco/local:{cl["p"]} {dataBase[option]["adress"]}{cl["limit"]}')
                    print(f'Ponto de Referência:{cl["p"]} {dataBase[option]["reference"]}{cl["limit"]}')
                    print(f'POLICE:{cl["p"]} {dataBase[option]["police"]}{cl["limit"]}')
                    print(f'Acionamento por:{cl["p"]} {dataBase[option]["trigger"]}{cl["limit"]}')
                    print(f'Tipo de Atendimento:{cl["p"]} {dataBase[option]["type"]}{cl["limit"]}')
                    print(dataBase)
                    ok = False

    # add people

    elif option == 2:
        date = datetime.datetime.now()
        answer = ''
        answer = str(input(f'It is ok? {date.day}/{date.month}/{date.year}\n[ {cl["b"]}Y{cl["limit"]} ] | [ {cl["r"]}N{cl["limit"]} ]: ')).title()[0]
        
        if answer == 'Y':
            dateBO["dateDay"] = date.day
            dateBO["dateMonth"] = date.month
            dateBO["dateYear"] = date.year

        else:
            ok = True
            while ok:
                dateBO["dateDay"] = readint('Day: ')
                if dateBO["dateDay"] < 1 or dateBO["dateDay"] > 31:
                    print(f'{cl["r"]}Please, type a valid day.{cl["limit"]}')
                    continue
                else:
                    ok = False
            
            ok = True
            while ok:
                dateBO["dateMonth"] = readint('Month: ')
                if dateBO["dateMonth"] < 1 or dateBO["dateMonth"] > 12:
                    print(f'{cl["r"]}Please, type a valid month.{cl["limit"]}')
                    continue
                else:
                    ok = False
            
            ok = True
            while ok:
                dateBO["dateYear"] = readint('Year: ')
                if dateBO["dateYear"] < 2000 or dateBO["dateYear"] > date.year:
                    print(f'{cl["r"]}Please, type a valid year.{cl["limit"]}')
                    continue

                else:
                    ok = False

        print(dateBO)
        people["date"] = dateBO.copy()
        people["offender"] = boolTitle('Infrator: ')
        people["reference"] = str(input('Ponto de Referência: ')).title()
        people["adress"] = str(input('Endereço: ' )).strip()
        people["time"] = str(input('Horário: ')).strip()
        people["police"] = str(input('POLICE: ')).strip().title()
        people["trigger"] = str(input('Acionamento por: ')).title().strip()

        tip = -1
        titleFor('Tipos de Atendimento', 30)
        ok = True
        while ok:
            for c in range(0, len(tiposAtendimentos)):
                print(f'{c} - {tiposAtendimentos[c]}\n')
            
            while tip < 0 or tip > 17:
                tip = readint('Tipo de Atendimento: ')
                if tip < 0 or tip > 17:
                    print(f'{cl["r"]}Please, type a value command.{cl["limit"]}')
            people["type"] = tiposAtendimentos[tip]
            ok = False

        dataBase.append(people.copy())
    
    # search people by people
    
    elif option == 3:
        print('Loading...')

    # metadata

    elif option == 4:
        if len(dataBase) == 0:
            print('Empty')
        else:
            print(dataBase)

    elif option == 5:
        break
    
    else:
        print('Please, type a valid command.')

