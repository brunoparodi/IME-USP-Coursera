def ordenada(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        menor = lista[i]
        for j in range(i+1, tamanho ):
            if lista[j] < lista[i]:
                return False
    return True

def teste():
    lista1 = [30, 59, 72, 99, 87, 93]
    lista2 = [30, 59, 72, 87, 93, 92.9]

    print(ordenada(lista1))
    print(ordenada(lista2))
