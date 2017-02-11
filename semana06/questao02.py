from math import pow

def verifica(h, a, b ):
    if pow(h,2) == (pow(a,2) + pow(b,2)):
        return True
    else:
        return False

def teste(h, a):
    soma = 0
    b = 1
    while True:
        if (pow(a,2) + pow(b,2)) > pow(h,2):
            break
        if verifica(h, a, b):
            soma = h
            break
        b = b + 1
    return soma

def soma_hipotenusas(h):
    soma = 0
    t = 1
    while t <= h:
        i = 1
        while i < h:
            v = teste(t, i)
            if v > 0:
                soma = soma + v
                break
            i = i + 1
        t = t + 1
    return soma

h = int(input("Digite a hipotenusa: "))

print(soma_hipotenusas(h))