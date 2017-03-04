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

# compara_assinatura(calcula_assinatura(texto_a),calcula_assinatura(texto_b))
def compara_assinatura(ass_main, matriz_ass_input):
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


def compara_assinatura3(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    print("Ass 1", as_a)
    print("Ass 2", as_b)
    somado = 0
    for i in range(len(as_a)):
        somado += abs(as_a[i] - as_b[i])
    grau = (somado/6)
    print(grau)
    return grau

def compara_assinatura2(ass_main, matriz_ass_input):
    """
    IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve
    devolver o grau de similaridade nas assinaturas.
    """
    lista_Sab = []
    for lin in range(len(matriz_ass_input)):
        indx = 0
        for col in range(len(matriz_ass_input[lin])):
            soma_mod = 0
            soma_mod = soma_mod + abs(ass_main[indx] - matriz_ass_input[lin][col])
            indx += 1
        Sab = soma_mod / 6
        lista_Sab.append(Sab)
    return lista_Sab

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

def avalia_textos3(textos_main, ass_comparadas):
    """
    Essa funcao recebe uma lista de textos e deve devolver o numero (0 a n-1)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    """
    aux_ass_com = ass_comparadas[:]
    aux_ass_com.sort()
    for indice in range(len(ass_comparadas)):
        if aux_ass_com[0] == ass_comparadas[indice]:
            copiah = indice
    return copiah

def avalia_textos2(textos, ass_cp):
    lista_test = []
    for i in range(len(textos)):
        ass_t = calcula_assinatura(textos[i])
        grau = compara_assinatura(ass_cp, ass_t)
        lista_test.append(grau)
    Gripe_COHPIAH = [0]
    Gripe_COHPIAH[0] = min(lista_test)
    #print("Assinaturas:", ass_cp)
    #print("Gripe", Gripe_COHPIAH)
    i = 0
    while Gripe_COHPIAH[0] in lista_test:
      del lista_test[0]
      if Gripe_COHPIAH[0] in lista_test:
        i += 1
      else:
        break
    i += 1
    return i


def Main():
    print("")
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("")
    print("")
    settings = le_assinatura()
    material_para_analise = le_textos()
    print("O autor do texto", avalia_textos(material_para_analise, settings), "está infectado com COH-PIAH")

#texto = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."


#Main()


texto_a = "Navegadores antigos tinham uma frase gloriosa:""Navegar é preciso; viver não é preciso"".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
texto_b = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
texto_c = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
#print(compara_assinatura([4.34, 0.05, 0.02, 12.81, 2.16, 0.0], [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]))
#print(calcula_assinatura(texto_c))
#print("Resultado:", compara_assinatura([4.34, 0.05, 0.02, 12.81, 2.16, 0.0],[3.96, 0.05, 0.02, 22.22, 3.41, 0.0]))
#print(len(calcula_assinatura(texto_a))," e ", len(calcula_assinatura(texto_b)))
#print(tamanhomfrase(texto_a))
#print(tamanho_mediop(texto_a))
#print(len(texto_b))
#print(tamanho_mediop(texto_c))
#aux_separa_frase(texto_a)
#print(len(separa_frases(texto_a)))
#aux_sep_sentencas(texto_b)
#a = aux_geral(texto_a)
#print(aux_sep_paralavras(a))
#print(tamanho_mediop(texto_b))
#print(calcula_assinatura(teste))
#print(tamanho_mediop(teste))
textos = [texto_a, texto_b, texto_c]
material_para_analise = textos
print("O autor do texto", avalia_textos(material_para_analise, [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]), "está infectado com COH-PIAH")