frutas_exoticas = ['jaboticaba','cupuaçu','graviola']


for fruta in frutas_exoticas:
    print ('Eu adoro ' + fruta)

primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47, 43, 59, 61, 67, 71, 73, 79, 83, 89, 97]


#for i in range(fim):
#    COMANDO
#
#for i in range(inicio, fim):
#    COMANDO
#
#for i in range(inicio, fim, passo):
#    COMANDO
#

pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(5, 10):
    print(pares[x])

def clonarlista(lista):
    novalista = []
    for objetos_lista in (lista):
        novalista.append(objetos_lista)
    return novalista

#fatias de listas: lista[3:7] | lista[:5] | lista[5:]
#clonar lista: novalista = lista[:]
#pertinencia a uma lista: for oquetivernalista in (lista):
#adição em listas: lista.append = 'valor' | lista.append[4]
#contatenacao de listas: lista1 + lista2
#repetição de listas: lista3 = lista1 * 3 = lista1 + lista1 + lista1
#remoção em listas: del lista[2] | del lista[5:18]

def remove_repetidos():
    lista = []
    x = int(input('informe uma sequencia de números, 0 para finalizar: '))
    while x != 0:
        if not x in lista:
            lista.append(x)
        x = int(input('informe uma sequencia de números, 0 para finalizar: '))
    print(lista)
    return lista
