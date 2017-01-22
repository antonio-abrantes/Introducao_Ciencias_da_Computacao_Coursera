from math import sqrt

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz = float((-b + sqrt(delta)) / (2 * a))
    print("a raiz desta equação é", raiz)
else:
    r1 = float((-b + sqrt(delta)) / (2 * a))
    r2 = float((-b - sqrt(delta)) / (2 * a))
    #print(r1,' - ',r2)
    if r1 <= r2:
        print('as raízes da equação são', r1,'e', r2)
    else:
        print('as raízes da equação são', r2, 'e', r1)