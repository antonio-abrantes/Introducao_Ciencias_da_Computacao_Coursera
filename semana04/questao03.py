num = input("Digite um número inteiro: ")

i = 0
soma = 0
while i < len(num):
    soma = soma + int(num[i])
    i = i + 1

print(soma)
