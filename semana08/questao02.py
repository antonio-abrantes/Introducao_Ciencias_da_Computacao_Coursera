def dimensoes(matriz):
    linha = 0
    for i in matriz:
        linha = linha + 1
        coluna = 0
        for j in i:
            coluna = coluna + 1
            resultado = str(linha)+'X'+str(coluna)
    print(resultado)

dimensoes([[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1], [2, 3, 6, 7]])
