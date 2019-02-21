lista = []


x = input('Informe coisas para adicionar a lista. ENTER para parar.  ')


contador = 0
while x != '':
    lista.append(x)
    x = input('Informe coisas para adicionar a lista. ENTER para parar.  ')
    contador = contador + 1

while contador > 0:
    contador = contador - 1
    print(lista[contador],end=',')
