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