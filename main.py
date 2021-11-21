import datetime
from utl.lay import colour as cl
from utl.aqv import readint, titleFor, tiposAtendimentos, line

print('\nHello, World.\n')

dataBase = list()
people = dict()
dateBO = dict()
menu = ['Data Base', 'Add People', 'Search by keyword', 'Exit']
option = 0

okMain = True
while okMain:
    titleFor('BO', 10)
    for c in range(0, len(menu)):
        print(f'{cl["b"]}{c + 1}{cl["limit"]} - {menu[c]}')
    
    option = 0
    option = int(input(f'{cl["b"]}\nOption:{cl["limit"]} '))

    # reading data base

    if option == 1:
        titleFor('Data Base')
        print(dataBase)
        line(27)

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
        people["date"] = dateBO
        people["name"] = str(input('Nome: ')).strip().title()
        people["reference"] = str(input('Referência: ')).title()
        people["adress"] = str(input('Endereço: ' )).strip()
        people["time"] = str(input('Horário: ')).strip()
        people["gcm"] = str(input('GCM: ')).strip().title()
        people["trigger"] = str(input('Acionamento por: ')).title().strip()

        tip = 0
        print('\nTipo de Atendimento\n')
        ok = True
        while ok:

            for c in range(0, len(tiposAtendimentos)):
                print(f'{c} - {tiposAtendimentos[c]}\n')

            tip = readint('Tipo de Atendimento: ')

            for c in range(0, len(tiposAtendimentos)):
                if tip == tiposAtendimentos[c]:
                    people["type"] = tiposAtendimentos[c]
            ok = False
        dataBase.append(people.copy())
    
    # search people by people
    
    elif option == 3:
        print('Loading')

    elif option == 4:
        break
    
    else:
        print('Please, type a valid command.')

