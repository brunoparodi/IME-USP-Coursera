def busca(lista, elemento):
    indice = 0
    for i in lista:
        if i == elemento:
            return indice
        else:
            indice += 1
    return False

def teste():
    print(busca(['a', 'e', 'i'], 'e'))
    print('deve devolver => 1')

    print(busca([12, 13, 14], 15))
    print('deve devolver => False')
