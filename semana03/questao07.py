import math

xa = int(input('digite x do ponto A: '))
ya = int(input('digite y do ponto A: '))

xb = int(input('digite x do ponto B: '))
yb = int(input('digite y do ponto B: '))

result = math.sqrt(float((xa - xb) ** 2) + float((ya - yb) ** 2))

if result >= 10:
    print('longe')
else:
    print('perto')