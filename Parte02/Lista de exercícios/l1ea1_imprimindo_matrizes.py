def imprime_matriz(matriz):
    linhas = len(matriz)
    
    colunas = len(matriz[0])
    

    
    for l in range(linhas):
        for c in range(colunas):
            print(matriz[l][c],end='')
            if c < colunas-1:
                print(' ',end='')
        print()

        

def t():
    minha_matriz = [[1], [2], [3]]
    imprime_matriz(minha_matriz)

    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    imprime_matriz(minha_matriz)
