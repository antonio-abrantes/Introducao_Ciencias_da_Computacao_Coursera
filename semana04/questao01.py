n = int(input("Digite o valor de n: "))

if n >= 1:
    fatorial = n
    while n > 1:
        fatorial = fatorial * (n - 1)
        n = n - 1
else:
    fatorial = 1

print(fatorial)


