def soma_elementos(lista):
    i = 0
    soma = 0
    while i < len(lista):
        soma += int(lista[i])
        i = i + 1
    return soma

lista = input("Digite os números : ").split()

print(soma_elementos(lista))