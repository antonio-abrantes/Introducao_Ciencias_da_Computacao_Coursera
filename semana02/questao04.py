numero = int(input('Digite um número inteiro: '))
numero_final = int(numero / 10)

result = str(numero_final)

print('O dígito das dezenas é', result[len(result) - 1])