import datetime

print('\nHello, World.\n')


dataBase = list()
people = dict()
dateBO = dict()
menu = ['See people', 'Add People', 'Search by keyword', 'Search by CPF', 'Exit']
option = 0

ok = True
while ok:
    for c in range(0, len(menu)):
        print(f'{c + 1} - {menu[c]}')
    
    option = 0
    option = int(input('Option: '))

    # readin data base

    if option == 1:
        for c in range(0, len(dataBase)):
            print(f'{dataBase[c]}')

    # add people

    elif option == 2:
        date = datetime.datetime.now()
        answer = ''
        answer = str(input(f'It is ok? {date.day}/{date.month}/{date.year}\n[ Y ] | [ N ]: ')).title()[0]
        
        if answer == 'Y':
            dateBO["dateDay"] = date.day
            dateBO["dateMonth"] = date.month
            dateBO["dateYear"] = date.year
        else:
            people["date"] = str(input('Type the data like this Ex. 01//07/2021'))

            ok = True
            while ok:
                dateBO["dateDay"] = int(input('Day:'))
                if date["dateDay"] < 1 or date["dateDay"] > 31:
                    print('Please, type a valid day.')
                    continue
                else:
                    ok = False
            
            ok = True
            while ok:
                dateBO["dateMonth"] = int(input('Month:'))
                if date["dateMonth"] < 1 or date["dateMonth"] > 12:
                    print('Please, type a valid month.')
                    continue
                else:
                    ok = False
            
            ok = True
            while ok:
                dateBO["dateYear"] = int(input('Year:'))
                if date["dateYear"] < 2000 or date.year:
                    print('Please, type a valid year.')
                    continue
                else:
                    ok = False

        print(dateBO)
        people["date"] = dateBO
        people["name"] = str(input('Name: '))
        people["cpf"] = str(input('CPF: ' ))
        people["des"] = str(input('History: '))
    
    # search people by people
    
    elif option == 3:
        nameRAM = str(input('Search by keyword: ')).strip().title()

    elif option == 4:
        break
    
    else:
        print('Please, type a valid command.')

