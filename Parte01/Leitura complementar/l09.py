
def soma_elementos(lista):
    tamanho = len(lista)
    elemento = 0
    somador = 0
    while elemento < tamanho:
        somador = somador + lista[elemento]
        elemento = elemento + 1
    return somador


def soma_reduzida(lista):
    soma = 0
    for elemento in lista:
        soma = soma + elemento
    return soma

#primos = [2, 3, 5, 7, 11, 13]
#for i in primos:
#    x = -1
#    
#    print( "%d: %d"%(i,primos[x]) )

def main():
    """
    (exercicio 1 da lista de exercicios sobre vetores).
    Dados n > 0 e uma sequencia com n numeros reais,
    imprimi-los na ordem inversa a da leitura.
    Solucao: Criar uma lista vazia e usar append.
    """

    print ("Le n inteiros e imprime-os em ordem reversa")
    n = int(input("Digite n: "))
    cont = 0
    seq = []  # cria uma lista vazia

    while cont < n:
        num = int(input("Digite um numero da sequencia: "))
        seq.append(num)   # coloca num no final da lista
        cont += 1

    print("Sequencia original: ", seq)


    print("Solucao 1: usando indices decrescentes")
    cont = n-1
    while cont >= 0:
        print (seq[cont], end=' ')
        cont -= 1
    print ()

    # ou ainda, usando indices negativos
    print("Solucao 2: usando indices negativos")
    cont = -1
    while cont >= -n:
        print (seq[cont], end=' ')
        cont -= 1
    print()

def main2():
    tseq = int(input('informe o tamanho da sequencia: '))
    x = 0
    lista = []
    while x < tseq:
        x += 1
        y = int(input('Informe o numero %d da sequencia: ' %x))
        lista.append(y)        
    print('Sequência original: ',lista)
    ordenada = sorted(lista[:])
    e = 0
    for i in ordenada:
        print(i)        
        if ordenada[e] == ordenada[e+1]:
            del ordenada[e]
            e = -1
        e += 1
    print(ordenada)

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


