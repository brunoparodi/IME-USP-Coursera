x = int(input('numero: '))
lista = []
if x == 0:
    print(lista)
while x != 0:    
    lista.append(x)
    x = int(input('numero: '))

inv = len(lista)
listainvertida = []
while inv > 0:
    print(lista[inv-1])
    inv = inv - 1

    
