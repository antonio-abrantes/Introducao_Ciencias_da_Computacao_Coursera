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
    if v_m1[0] == v_m2[1] and v_m1[1] == v_m2[0]:
        return True
    else:
        return False

def sao_multiplicaveis(m1, m2):
    multiplicaveis = verifica_igualdade(m1, m2)
    return multiplicaveis

#m1 = [[1], [2]]
#m2 = [[1, 2]]
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(sao_multiplicaveis(m1, m2))