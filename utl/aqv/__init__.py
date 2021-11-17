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
    num1 = len(txt) * 2
    print('-' * num1)
    print(f'{txt.center(num1)}')
    print('-' * num1)


tiposAtendimentos = ['Apoio aos eventos municipais', 'Apoio as secretarias', 'Mediação de conflitos', 'Averiguação de consumo de entorpecente em logradouros públicos',
'Abordagem por atitude suspeita', 'Intervenção para prevenção de ato infracional', 'Intervenção/Orientação sócio-educativa',
'Apoio a sociedade civil organizada', 'Intervenção no ambito escolar', 'Prestação de socorro', 'Transporte de doversos em VTR', 'Apoio à ocorrência de trânsito',
'Intensificação de Ronda/Averiguação', 'Atendimento social a população de rua', 'Atendimento ao idoso', 'Documentos e/ou objetos achados', 'Atendimento a crianças e/ou adolescente em situação de risco',
'Outros atendimentos (Detalhar no histórico)']

def line(x):
    print('-' * x)