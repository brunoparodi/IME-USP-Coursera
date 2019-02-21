def bubble_sort(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista [j],lista[j+1] = lista[j+1], lista[j]
                print(lista)             
    return lista


    
##if __name__ == '__main__':
##    print('\nprint',bubble_sort([5, 1, 4, 2]))
##    print('deveria imprimir:\n',
##        '[1, 5, 4, 2]\n',
##        '[1, 4, 5, 2]\n',
##        '[1, 4, 2, 5]\n',
##        '[1, 2, 4, 5]\n',
##        'deve devolver [1, 2, 4, 5]'
##        )

