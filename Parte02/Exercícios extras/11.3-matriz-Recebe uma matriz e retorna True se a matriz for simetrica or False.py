#-----------------------------------------------------
def simetrica(matriz):
    '''(matriz) -> bool

    Recebe uma matriz e returna True se a matriz for simetrica,
    em caso contrario retorna False.

    Pre-condicao: a funcao supoe que a matriz e quadrada

    >>> a = [[1,2,3],[2,1,4],[3,4,1]]
    >>> a
    [[1, 2, 3], [2, 1, 4], [3, 4, 1]]
    >>> imprima_matriz(a)
    Matriz: 3 x 3
         1     2     3
         2     1     4
         3     4     1
    >>> simetrica(a)
    True
    print("Vixe! Ainda nao fiz a funcao!")
    '''
    l = 0
    c = 0
    condicao = 0
    while l < len(matriz):
        while c < len(matriz[0]):
            if matriz[l][c] == matriz[c][l]:
                condicao = condicao + 0
            else:
                return False
            c += 1
        c = 0
        l += 1
            
    return condicao == 0
        
#-----------------------------------------------------
def testes():
    a = [[ 11, -3,  4,  8 ],
         [ -3, 12,  6, 11 ],
         [  4,  6,  5, 13 ],
         [  8, 11, 13,  5 ]]
    if simetrica(a):
        print('Teste 1- informei uma simétrica')
        print("Passou no primeiro teste! :-)")
    else:
        print("Nao passou no primeiro teste! :-(")

    

    b = [[ 11, -3,  4,  8 ],
         [ -3, 12,  6, 11 ],
         [  3,  6,  5, 13 ],
         [  8, 11, 13,  5 ]]
    if simetrica(a):
        print('Teste 2- informei uma Assimétrica')
        print("Passou no primeiro teste! :-)")
    else:
        print("Nao passou no primeiro teste! :-(")

    
