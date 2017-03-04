import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra: "))
  ttr = float(input("Entre a relação Type-Token: "))
  hlr = float(input("Entre a Razão Hapax Legomana: "))
  sal = float(input("Entre o tamanho médio de sentença: "))
  sac = float(input("Entre a complexidade média da sentença: "))
  pal = float(input("Entre o tamanho medio de frase: "))

  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

######   Funções auxiliares ########

## Retorna as frases de um texto em uma lista  # [ OK ]
def aux_sep_sentencas(texto):
    sente = separa_sentencas(texto)
    qtdFrases = 0
    frases = []
    for parte in sente:
        frases.append(separa_frases(parte))

    for i in range(len(frases)):
        qtdFrases += len(frases[i])
        #print(frases[i])
    return qtdFrases # Retorna um lista com todas as frases separdas

 #### AUXILIAR PRINCIPAL
def aux_geral(texto):  # [ OK ]
    sente = separa_sentencas(texto)
    frases = []
    for parte in sente:
        frases += separa_frases(parte)
    #print(frases, "Tamanho:", len(frases))
    return frases

def aux_sep_paralavras(frases):  # [ OK ]
    palavras = []
    for frase in frases:
        palavras += separa_palavras(frase)
    return palavras

# Tamanho médio de palavra: é a soma dos tamanhos das palavras dividida pelo número total de palavras. [ OK ]
def tamanho_mediop(texto):
    frases = aux_geral(texto)
    texto_separado = aux_sep_paralavras(frases)
    #print("Texto separado", texto_separado)
    num_palavras = len(texto_separado)
    soma = 0
    for i in texto_separado:
        soma += len(i)
    return soma / num_palavras

def tamanho_medios(texto):  # [ OK ]
    separado = separa_sentencas(texto)
    quant = len(separado)
    numcaracter = 0
    for i in range(quant):
        numcaracter += len(separado[i])
    return numcaracter/quant

# Tamanho médio de frase: é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
# (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
def tamanhomfrase(texto):  # [ OK ]
    separado = aux_geral(texto)
    soma = 0
    for i in separado:
        soma += len(i)
    return soma / len(separado)

def calc_num_palavras(texto):  # Ainda não utilizada
    frases = separa_frases(texto)
    num = 0
    for frase in frases:
        num += len(separa_palavras(frase))
    print(num)

####################################################################################

def compara_assinatura(ass_main, matriz_ass_input): # [ OK ]
    """
    Essa funcao recebe duas assinaturas de texto e deve devolver o grau de
    similaridade nas assinaturas.
    """
    lista_Sab = []
    soma_mod = 0
    if type(matriz_ass_input[0]) is list:
        for lin in range(len(matriz_ass_input)):
            for col in range(len(matriz_ass_input[lin])):
                soma_mod += abs(ass_main[col] - matriz_ass_input[lin][col])
            Sab = soma_mod / 6
            lista_Sab.append(Sab)
        return lista_Sab
    else:
        for i in range(len(matriz_ass_input)):
            soma_mod += abs(ass_main[i] - matriz_ass_input[i])
        Sab = soma_mod / 6
        return Sab

def calcula_assinatura(texto):
    frases = aux_geral(texto)
    num_palavras = aux_sep_paralavras(frases)
    tamanhomp = tamanho_mediop(texto)
    rtypetoken = n_palavras_diferentes(num_palavras) / len(num_palavras)
    rhapaxlego = n_palavras_unicas(num_palavras) / len(num_palavras)
    tamanhoms = tamanho_medios(texto)
    complexs = len(frases) / len(separa_sentencas(texto))
    tamanhomf = tamanhomfrase(texto)
    lista = [tamanhomp, rtypetoken, rhapaxlego, tamanhoms, complexs, tamanhomf]
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto em forma de lista.'''
    return lista

def avalia_textos(textos_main, ass_comparadas):
    """
    Essa funcao recebe uma lista de textos e deve devolver o numero (0 a n-1)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    """
    aux_ass_com = (ass_comparadas[:])
    aux_ass_com.sort()
    for indice in range(len(ass_comparadas)):
        if aux_ass_com[0] == ass_comparadas[indice]:
            copiah = indice
    return copiah -1

def Main():
    print("")
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("")
    print("")
    settings = le_assinatura()
    material_para_analise = le_textos()
    print("O autor do texto", avalia_textos(material_para_analise, settings), "está infectado com COH-PIAH")

Main()