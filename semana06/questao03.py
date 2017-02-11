def primo(n):
    cont_div = 0
    for i in range(1, n + 1):
        if (n % i) == 0:
            cont_div = cont_div + 1

    if cont_div <= 2:
        return True
    return False

def n_primos(num):
    i = 2
    soma = 0

    while i <= num:
        if primo(i):
            soma = soma + 1
        i = i + 1

    return soma

num = int(input('Digite o número inteiro: '))

print(n_primos(num))