larg = int(input('digite a largura: '))
alt = int(input('digite a altura: '))

altini = 1
largini = 1

while altini <= alt:
    while largini <= larg:
        if largini != 1 and largini != larg and altini != 1 and altini != alt:
            print(' ',end='')
        else:
            print('#',end='')
        largini = largini + 1
    largini = 1
    print()
    altini = altini + 1
