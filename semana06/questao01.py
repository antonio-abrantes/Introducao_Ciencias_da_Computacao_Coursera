def funcao():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    i = 0

    while i < altura:
        linha = ""
        j = 0
        while j < largura:
            linha = linha + "#"
            j = j + 1
        print(linha)
        i = i + 1

funcao()