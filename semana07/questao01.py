def recebeNumero():
    lista = []
    while True:
        temp = int(input("Digite um número: "))
        if temp == 0:
            break
        lista.append(temp)
    print()
    for i in range((len(lista) -1), -1, -1 ):
        print(lista[i])

recebeNumero()
