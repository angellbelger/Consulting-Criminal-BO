import datetime

x = datetime.datetime.now()

print(x.day)
y = int(input('Number: '))

if x.day == y:
    print('True')
else:
    print('False')