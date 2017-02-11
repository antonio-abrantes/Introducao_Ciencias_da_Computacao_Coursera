def maior_elemento(lista):
    temp = []
    for i in range(len(lista)):
        temp.append(int(lista[i]))
    lista = temp
    return max(lista)

lista = input("Digite os números : ").split()

print(maior_elemento(lista))