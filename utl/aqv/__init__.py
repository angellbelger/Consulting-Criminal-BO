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


def titleFor(txt, num1=0):
    print(f'{cl["b"]}-' * num1)
    print(f'{txt.center(num1)}')
    print(f'-' * num1)
    print(f'{cl["limit"]}')


def boolTitle(txt):
    x = ''
    bool = ''
    while True:
        x = str(input(txt)).title().strip()
        bool = str(input(f'It is correct: {x} \n[ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]'))[0].title()

        if bool == 'N':
            continue
        else:
            return x


def bool(txt):
    x = ''
    bool = ''
    while True:
        x = str(input(txt)).strip()
        bool = str(input(f'It is correct: {x} \n[ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]'))[0].title()

        if bool == 'N':
            continue
        else:
            return x


tiposAtendimentos = ['Apoio aos eventos municipais', 'Apoio as secretarias',
 'Mediação de conflitos', 
 'Averiguação de consumo de entorpecente em logradouros públicos',
'Abordagem por atitude suspeita', 'Intervenção para prevenção de ato infracional',
 'Intervenção/Orientação sócio-educativa',
'Apoio a sociedade civil organizada', 'Intervenção no ambito escolar',
 'Prestação de socorro', 'Transporte de diversos em VTR',
 'Apoio à ocorrência de trânsito',
'Intensificação de Ronda/Averiguação', 'Atendimento social a população de rua',
 'Atendimento ao idoso', 'Documentos e/ou objetos achados',
  'Atendimento a crianças e/ou adolescente em situação de risco',
'Outros atendimentos (Detalhar no histórico)']

def line(x):
    print('-' * x)