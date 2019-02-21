#-----------------------------------------------------
def imprima_matriz(matriz):
    '''(matriz) -> None

    Recebe e imprime uma matriz de inteiros.

    >>> a = [[1,2,3],[2,1,4],[3,4,1]]
    >>> a
    [[1, 2, 3], [2, 1, 4], [3, 4, 1]]
    >>> imprima_matriz(a)
    Matriz: 3 x 3
         1     2     3
         2     1     4
         3     4     1
    print("Vixe! Ainda nao fiz a funcao!")
    '''
    print('Matriz:',len(matriz),'x',len(matriz[0]))
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            
            print('%6d' %matriz[i][c],end='')
        print()
    

#-----------------------------------------------------
# testes
a = [[1,2,3],[2,1,4],[3,4,1]]
imprima_matriz(a)

