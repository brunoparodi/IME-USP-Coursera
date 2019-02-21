def busca(lista, elemento):
    inicio = 0
    fim = len(lista) -1
    while inicio <= fim:
        meio = (fim + inicio) // 2
        print(meio)
        if lista[meio] == elemento:
            return meio
        elif elemento < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return False
        


##if __name__ == '__main__':
##    print(busca(['a', 'e', 'i'], 'e'))
##    1
##    print('# deve devolver => 1')
##
##    print(busca([1, 2, 3, 4, 5], 6))
##    2
##    3
##    4
##    print('# deve devolver => False')
##
##    print(busca([1, 2, 3, 4, 5, 6], 4))
##    2
##    4
##    3
##    print('# deve devolver => 3')
