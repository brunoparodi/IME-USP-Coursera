linha = 1
coluna = 1
while linha <= 10:
    while coluna <=10:
       print(linha * coluna, end = "\t")
       coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1

def tabuada():
    print('aqui começa o def tabuada')
    tab = 1
    mult = 1
    while tab <= 10:
        while mult <= 10:
            print(tab,'x',mult,'=',tab * mult, end='\t')
            mult = mult + 1
        tab = tab + 1
        print()
        mult = 1
    print('aqui termina o def tabuada')
tabuada()

def desenha(linha):    
    while linha > 0:
        coluna = 1
        while coluna <= linha:
            print('*', end = "")
            coluna = coluna + 1
        print()
        linha = linha - 1
desenha(5)

altura = 5
linha = 1
while linha <= altura:
    print("*", end = "\t")
    coluna = 2
    while coluna < altura: 
        if linha == 1 or linha == altura:
            print("*", end = "\t")
        else:
            print(end = "\t")
        coluna = coluna + 1
    print("*")
    linha = linha + 1
