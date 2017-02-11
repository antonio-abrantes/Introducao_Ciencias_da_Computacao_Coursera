def primo(n):
    cont_div = 0
    for i in range(1, n + 1):
        if (n % i) == 0:
            cont_div = cont_div + 1

    if cont_div <= 2:
        return True
    return False

def maior_primo(n):
    if primo(n):
        return n
    else:
        while n >= 2:
            n = n -1
            if primo(n):
                return n

num = int(input('Digite o número inteiro: '))

print(maior_primo(num))