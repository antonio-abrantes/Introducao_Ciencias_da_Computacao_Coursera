def remove_repetidos(lista):
    temp = []
    for i in range(len(lista)):
        temp.append(int(lista[i]))
    lista = temp

    nova_lista = []
    for item in lista:
        if not item in nova_lista:
            nova_lista.append(item)
    nova_lista.sort()
    return nova_lista

lista = input("Digite os números : ").split()

print(remove_repetidos(lista))
