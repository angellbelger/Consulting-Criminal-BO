import datetime
from os import name
from utl.lay import colour as cl
from utl.aqv import onlyBool, readint, titleFor, tiposAtendimentos, boolTitle, bool, boolNumber

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
    option = readint(f'{cl["b"]}\nOption:{cl["limit"]} ')

    # reading database

    if option == 1:

        ok = True
        while ok:
            titleFor('Database', 30)

            if len(dataBase) == 0:
                print('It is empty.')
                ok = False

            else:
                for c in range(0, len(dataBase)):
                    print(f'{cl["b"]}{c}{cl["limit"]} - {dataBase[c]["offender"]}')
                
                ok = True
                while ok:
                    try:
                        option = readint('See people: ')
                        titleFor('Data', 50)
                        print(f'\033[35m{dataBase[option]["date"]["dateDay"]}/{dataBase[option]["date"]["dateMonth"]}/{dataBase[option]["date"]["dateYear"]}\033[m - Time: \033[35m{dataBase[option]["time"]}\033[m')
                        print(f'Infrator:{cl["p"]} {dataBase[option]["offender"]}{cl["limit"]}')
                        print(f'Endereco/local:{cl["p"]} {dataBase[option]["adress"]}{cl["limit"]}')
                        print(f'Ponto de Referência:{cl["p"]} {dataBase[option]["reference"]}{cl["limit"]}')
                        print(f'POLICE:{cl["p"]} {dataBase[option]["police"]}{cl["limit"]}')
                        print(f'Acionamento por:{cl["p"]} {dataBase[option]["trigger"]}{cl["limit"]}')
                        print(f'Tipo de Atendimento:{cl["p"]} {dataBase[option]["type"]}{cl["limit"]}')
                    
                    except Exception as error:
                        print(f'{cl["r"]}{error.__class__}. Try again.{cl["limit"]}')
                    
                    finally:
                        ok = False

    # add people

    elif option == 2:
        date = datetime.datetime.now()
        answer = ''
        answer = onlyBool(f'It is ok? {date.day}/{date.month}/{date.year}\n[ {cl["b"]}Y{cl["limit"]} ] | [ {cl["r"]}N{cl["limit"]} ]: ').title()[0]
        
        if answer == 'Y':
            dateBO["dateDay"] = date.day
            dateBO["dateMonth"] = date.month
            dateBO["dateYear"] = date.year

        else:
            ok = True
            while ok:
                dateBO["dateDay"] = boolNumber('Day: ')

                if dateBO["dateDay"] < 1 or dateBO["dateDay"] > 31:
                    print(f'{cl["r"]}Please, type a valid day.{cl["limit"]}')
                    continue
                else:
                    ok = False
            
            ok = True
            while ok:
                dateBO["dateMonth"] = boolNumber('Month: ')

                if dateBO["dateMonth"] < 1 or dateBO["dateMonth"] > 12:
                    print(f'{cl["r"]}Please, type a valid month.{cl["limit"]}')
                    continue
                else:
                    ok = False
            
            ok = True
            while ok:
                dateBO["dateYear"] = boolNumber('Year: ')

                if dateBO["dateYear"] < 2000 or dateBO["dateYear"] > date.year:
                    print(f'{cl["r"]}Please, type a valid year.{cl["limit"]}')
                    continue

                else:
                    ok = False

        people["date"] = dateBO.copy()
        people["offender"] = boolTitle('\nInfrator: ')
        people["reference"] = bool('\nPonto de Referência: ')
        people["adress"] = bool('\nEndereço: ' )
        people["time"] = bool('\nHorário: ')
        people["police"] = boolTitle('\nPOLICE: ')
        people["trigger"] = boolTitle('\nAcionamento por: ')

        choose = -1
        titleFor('Tipos de Atendimento', 30)
        ok = True
        while ok:
            for c in range(0, len(tiposAtendimentos)):
                print(f'{cl["b"]}{c}{cl["limit"]} - {tiposAtendimentos[c]}\n')
            
            ok = True
            while ok:
                choose = readint('Tipo de Atendimento: ')

                if choose >= 0 and choose <= 16:
                    people["type"] = tiposAtendimentos[choose]
                    ok = False

                elif choose == 17:
                    people["type"] = str(input('Description: '))
                    ok = False

                elif choose < 0 or choose > 17:
                    print(f'{cl["r"]}Please, type a value command.{cl["limit"]}')
                    continue

        dataBase.append(people.copy())
    
    # search people by people
    
    elif option == 3:

        ok = True
        while ok:

            titleFor('Keyword', 30)

            listKeyword = ['Date', 'Offender', 'POLICE', 'Back']

            for c in range(0, len(listKeyword)):
                print(f'{c + 1} - {listKeyword[c]}')
            
            option = 0
            option = readint(f'{cl["b"]}\nOption:{cl["limit"]} ')

            if option == 1:
                dateRAM = {}
                dateRAM["dateDay"] = readint('Day: ')
                dateRAM["dateMonth"] = readint('Month: ')
                dateRAM["dateYear"] = readint('Year: ')

                # SEARCH date by date

                for index in range(0, len(dataBase)):
                    counter = 0
                    if dateRAM == dataBase[index]["date"]:
                        counter += 1
                        titleFor('Search by Date', 50)
                        print(f'\033[35m{dataBase[index]["date"]["dateDay"]}/{dataBase[index]["date"]["dateMonth"]}/{dataBase[index]["date"]["dateYear"]}\033[m - Time: \033[35m{dataBase[index]["time"]}\033[m')
                        print(f'Infrator:{cl["p"]} {dataBase[index]["offender"]}{cl["limit"]}')
                        print(f'Endereco/local:{cl["p"]} {dataBase[index]["adress"]}{cl["limit"]}')
                        print(f'Ponto de Referência:{cl["p"]} {dataBase[index]["reference"]}{cl["limit"]}')
                        print(f'POLICE:{cl["p"]} {dataBase[index]["police"]}{cl["limit"]}')
                        print(f'Acionamento por:{cl["p"]} {dataBase[index]["trigger"]}{cl["limit"]}')
                        print(f'Tipo de Atendimento:{cl["p"]} {dataBase[index]["type"]}{cl["limit"]}')
                    
                    if counter == 0:
                        print('\nNothing Found.\n')
            
            elif option == 2:
                print('Loading')
            
            elif option == 3:
                print('Loading')

            elif option == 4:
                ok = False
            
            else:
                print(f'{cl["r"]}Please, type a valid command.{cl["limit"]}')

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

