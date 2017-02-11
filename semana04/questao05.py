def eh_primo(num):
    if num < 2:
        return False
    temp = int((num / 2) + 1)
    i = 2
    while i < temp:
        if(num % i) == 0:
            return False
        i = i + 1
    return True

num = int(input("Digite um número inteiro: "))

resp = eh_primo(num)
print()
if (resp == False):
    print("não primo")
else:
    print("primo")