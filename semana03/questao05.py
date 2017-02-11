numero = int(input('Digite um numero inteiro: '))

#if (numero % 5 == 0) and (numero % 3 == 0):
if numero %(3 and 5) == 0:
    print('FizzBuzz')
else:
    print(numero)