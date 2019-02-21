def soma_lista(lista, n=1, soma=0):
    if lista == []:
        return soma
    soma = soma + lista[0]
    return soma_lista(lista[n:], n, soma)


def teste():
    print(soma_lista([3]))
    print(soma_lista([3, 2, 4, 5, 1, 0, 6, 7]))
