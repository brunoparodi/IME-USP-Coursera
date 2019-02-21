def insertion_sort(lista):
    comp = len(lista)-1
    cont = 0
    for i in range(comp):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            cont+=1
    return lista, cont


def teste():
    lista = [1,2,3,5,4,6,8,7]
    print(insertion_sort(lista))


teste()
