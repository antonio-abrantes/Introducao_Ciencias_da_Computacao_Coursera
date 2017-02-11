def maximo(n1, n2):
    lista = []
    lista.append(n1)
    lista.append(n2)

    return max(lista)

num1, num2 = input("Digites dois números inteiros: ").split()

num1 = int(num1)
num2 = int(num2)

print(maximo(num1, num2))