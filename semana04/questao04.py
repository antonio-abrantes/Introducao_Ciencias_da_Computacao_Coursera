num = input("Digite um número inteiro: ")
i = 1
achou = False

if len(num) <= 2:
    if len(num) == 2 and num[0] == num[i]:
        achou = True
else:
    while i < (len(num) - 1) and not achou:
        if num[i - 1] == num[i] or num[i + 1] == num[i]:
            achou = True
        i = i + 1

if achou == True:
    print("sim")
else:
    print("não")