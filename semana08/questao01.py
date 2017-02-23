def imprime_matriz(matriz):

    for i in matriz:
        coluna = 0
        resultado = ''
        for j in i:
            coluna = coluna + 1
            if coluna < (len(matriz[0])):
                resultado = resultado + str(j) + ' '
            else:
                resultado = resultado + str(j)
        print(resultado)

matriz = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7]]

imprime_matriz(matriz)