# Logica de programação em Python

def fib(n):
    n -= 1

    lista = [1, 1]
    cont = 2

    while cont <= n:
        lista.append(lista[cont - 1] + lista[cont - 2])
        cont = cont + 1
    return lista[n]

termo = 7

print(fib(termo))