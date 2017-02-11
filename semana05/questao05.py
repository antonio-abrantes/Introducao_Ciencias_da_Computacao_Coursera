def vogal(caracter):
    vogais = 'aeiou'
    i = 0
    while i < 5:
        if vogais[i] == caracter.lower():
            return True
        i = i + 1
    return False

caracter = input("Digite a letra: ")
print(vogal(caracter))