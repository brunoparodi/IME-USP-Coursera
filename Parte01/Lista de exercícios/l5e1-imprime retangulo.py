largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
l_inicial = 1
a_inicial = 1

while a_inicial <= altura:
    while l_inicial <= largura:
        print('#', end='')
        l_inicial = l_inicial + 1
    print()
    l_inicial = 1
    a_inicial = a_inicial + 1
    
