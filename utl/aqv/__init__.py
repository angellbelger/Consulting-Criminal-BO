from utl.lay import colour as cl


def readint(msg):
    while True:
        try:
            x = int(input(msg))
        except:
            print(f'{cl["r"]}Please, type valid command.{cl["limit"]}')
            continue
        else:
            return x
        break


def titleFor(txt):
    print('-' * len(txt) * 2)
    print(f'{txt.center(10)}')
    print('-' * len(txt) * 2)