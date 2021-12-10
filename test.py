import datetime

# test 05


pessoas = dict()
individuo = dict()


while True:
    individuo["name"] = str(input('nome: '))
    individuo["age"] = int(input('age: '))
    pessoas["individuo"] = individuo
    print(pessoas)
    #for c in range(0, len(pessoas)):
     #   print(f'{c} - {pessoas[c]["name"] - pessoas[c]["age"]}')

