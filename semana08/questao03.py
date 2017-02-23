def dimensoes(matriz):
    linha = 0
    for i in matriz:
        linha = linha + 1
        coluna = 0
        for j in i:
            coluna = coluna + 1
    return [linha, coluna]

def verifica_igualdade(m1, m2):
    v_m1 = dimensoes(m1)
    v_m2 = dimensoes(m2)
    if v_m1 == v_m2:
        return True
    else:
        return False

def somar(m1, m2):
    matriz_soma = []
    quant_linhas = len(m1)
    quant_colunas = len(m1[0])
    for i in range(quant_linhas):
        matriz_soma.append([])
        for j in range(quant_colunas):
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def soma_matrizes(m1, m2):
    teste = verifica_igualdade(m1, m2);
    if teste == True:
        return somar(m1, m2)
    else:
        return False

#m1 = [[1], [2], [3]]
#m2 = [[2, 3, 4], [5, 6, 7]]
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))