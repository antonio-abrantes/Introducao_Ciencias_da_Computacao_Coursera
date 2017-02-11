def funcao():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    i = 0

    while i < altura:
        linha = ""
        j = 0
        if i == 0 or i == (altura - 1):
            while j < largura:
                linha = linha + "#"
                j = j + 1
            print(linha)
        else:
            linha = "#"
            while j < (largura - 2):
                linha = linha + " "
                j = j + 1
            linha += "#"
            print(linha)
        i = i + 1

funcao()