def crialista():
    comp = int(input('informe comprimento da sequencia: '))
    lista = []
    c = 1
    while c <= comp:
        item = int(input('infome o %dº da sequencia: ' %c))
        lista.append(item)
        c = c + 1
    print('a lista ficou:',lista)
    return lista

    
def somalista(lista):
    x = soma = 0
    while x < len(lista):
        soma = soma + lista[x]
        x = x + 1
    return soma
