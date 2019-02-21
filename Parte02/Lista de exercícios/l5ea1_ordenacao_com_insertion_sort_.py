def insertion_sort(lista):
    t = len(lista)-1
    for i in range(len(lista)):
        for j in range(len(lista[0:i])):
            if lista[j]>lista[i]:
                lista[j],lista[i]=lista[i],lista[j]
            print(lista)
    return lista

def teste():
    v = [5, 3, 2, 4, 7, 1, 0, 6]
    print(v)
    print(insertion_sort(v))


teste()
