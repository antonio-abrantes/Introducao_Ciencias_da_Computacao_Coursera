num = int(input("Digite o valor de n: "))

i = 1
while num > 0:
    if(i % 2) != 0:
        print(i)
        num = num - 1
    i = i + 1