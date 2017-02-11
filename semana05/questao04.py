def maximo(n1, n2, n3):
    lista = []
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)

    return max(lista)

num1, num2, num3 = input("Digites três números inteiros: ").split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

print(maximo(num1, num2, num3))