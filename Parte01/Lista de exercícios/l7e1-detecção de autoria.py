import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo
    e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e
    devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e
    devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e
    devolve uma lista das palavras dentro da frase'''
    return frase.split()

def numero_sentencas(texto):
    return len(separa_sentencas(texto))
def numero_frases(texto):
    return len(lista_frases(texto))
def numero_palavras(texto):
    return len(lista_palavras(texto))
def numero_letras(texto):
    lp = lista_palavras(texto)
    num_letras = 0
    c = 0
    for n in lista_palavras(texto):
        num_letras = num_letras + len(lp[c])
        c += 1
    return num_letras

def complexidade(texto):
    return numero_frases(texto) / numero_sentencas(texto)

def media_frase(texto):
    return tamanho_frases(texto) / numero_frases(texto)

def lista_frases(texto):#pega sentenças e faz uma lista com as frases
    s = separa_sentencas(texto)
    n = numero_sentencas(texto)
    f = []
    c = 0
    while c < n:
        f = f + separa_frases(s[c]) 
        c += 1
    return f

def lista_palavras(texto):#pega frases e faz uma lista com as palavras
    f = lista_frases(texto)
    n = numero_frases(texto)
    p = []
    c = 0
    while c < n:
        p = p + separa_palavras(f[c])
        c +=1
    return p

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e
    devolve o numero de palavras que aparecem uma unica vez'''
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

def cont_palavras_unicas(texto):
    lp = lista_palavras(texto)
    return n_palavras_unicas(lp)

def cont_palavras_diferentes(texto):
    lp = lista_palavras(texto)
    return n_palavras_diferentes(lp)

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e
    devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def media_palavras(texto): #recebe texto e faz média das palavras
    c = 0
    tam = 0
    for palavra in lista_palavras(texto):
        tam = tam + len(palavra)
        c += 1
    media = tam / len(lista_palavras(texto))
    return media

def media_sentencas(texto): #media cadacteres / sentenca
    c = 0
    t_sent = 0
    for sentencas in separa_sentencas(texto):
        t_sent = t_sent + len(sentencas)
        c += 1
    media = t_sent / len(separa_sentencas(texto))
    return media

def tamanho_frases(texto):
    c = 0
    t_frases = 0
    for frases in lista_frases(texto):
        t_frases = t_frases + len(frases)
        c += 1
    return t_frases

def type_token(texto):
    return cont_palavras_diferentes(texto) / numero_palavras(texto)

def hapax_legomana(texto):
    return cont_palavras_unicas(texto) / numero_palavras(texto)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e
    deve devolver o grau de similaridade nas assinaturas.'''
    s_ab = 0
    for i in range(0,6):
        if (as_a[i] - as_b[i]) < 0:
            s_ab = s_ab + (as_a[i] - as_b[i]) * -1
        else:
            s_ab = s_ab + (as_a[i] - as_b[i])
    return s_ab/6
    '''
    c = 0
    somaa = 0
    for i in range(0,6):
        somaa = (somaa) + (as_a[i])
        c += i  

    somab = 0
    for i in range(0,6):
        somab = (somab + as_b[i])
        c += i  
    s_ab = ((somaa - somab) / 6)
    return s_ab
    '''

            

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e
    deve devolver a assinatura do texto.'''
    wal = media_palavras(texto)
    ttr = type_token(texto)
    hlr = hapax_legomana(texto)
    sal = media_sentencas(texto)
    sac = complexidade(texto)
    pal = media_frase(texto)    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e
    deve devolver o numero (1 a n) do texto com maior probabilidade
    de ter sido infectado por COH-PIAH.'''
    comp =[]
    for t in textos:
        comp.append(compara_assinatura(calcula_assinatura(t),ass_cp))
    texto = 1
    t = 0
    while t < (len(comp)-1):
        if comp[t] >= comp[t+1]:
            texto += 1
        
        t += 1
    return texto



