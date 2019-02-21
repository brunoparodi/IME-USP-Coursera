def encontra_impares(lista, n=1, lista2=[]):
    if lista == []:
        return lista2
    elif lista[0]%2 != 0:
        lista2.append(lista[0])
    return encontra_impares(lista[n:], n, lista2)

def teste():
    print(encontra_impares([3, 2, 4, 5, 1, 0, 6, 7]))
    print(encontra_impares([2, 4, 0, 6,]))
     
def encontra_impares2(lista, n=1, lista2=[]):
    if lista == []:
        return lista2
    elif lista[0]%2 != 0:
        lista2.extend(lista[:n])
    return encontra_impares2(lista[n:], n, lista2)

def teste2():
    print(encontra_impares2([3, 2, 4, 5, 1, 0, 6, 7]))
    print(encontra_impares2([2, 4, 0, 6,]))

def teste3():
    print(encontra_impares2([3, 2, 4, 5, 1, 0, 6, 7]))
    print(encontra_impares2([2, 4, 0, 6,]))
