def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
    print(matriz)
    return matriz

#cria_matriz(3, 3)

print(44 in [3, 4, 5, 55, 44])

teste = [3, 4, 5, 55, 44]

teste.append(58)

print(teste)