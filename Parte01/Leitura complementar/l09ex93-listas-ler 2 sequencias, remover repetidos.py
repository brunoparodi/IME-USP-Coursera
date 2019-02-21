def cria_lista(tseq):
    print('O tamanho da sequencia é: ', tseq)
    x = 0
    lista = []
    while x < tseq:
        x += 1
        y = int(input('Informe o numero %d da sequencia: ' %x))
        lista.append(y)        
    return lista

def ordenar(lista):
    lista = sorted(lista[:])
    return lista

def remove_repetidos(lista):
    lista = ordenar(lista)
    e = 0
    while e < len(lista)-1:
        if lista[e] == lista[e+1]:
            del lista[e]
            e = -1
        e += 1
    return lista



def seq(m,n):
    listam = cria_lista(m)
    print('Primeira sequencia: ',listam,'\n')
    listan = cria_lista(n)
    print('Segunda sequencia: ',listan,'\n')

    print('m',ordenar(listam))
    print('n',ordenar(listan))

    print('soma ordenada', ordenar(listam)+ordenar(listan))

    print('ordenagem da soma', ordenar(listam+listan))

    print('sem repetido', remove_repetidos(ordenar(listam+listan)))
