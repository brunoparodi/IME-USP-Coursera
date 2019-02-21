#-------------------------------------------------------
def leia_matriz():
    '''(None) -> matriz (lista de listas)

    Funcao que le do teclado o numero n_linhas de linhas
    e o numero n_colunas de colunas e os elementos de
    uma matriz de inteiros dimensao n_linha x n_colunas.

    A funcao cria e retorna a matriz lida.
    
    print("Vixe! Ainda nao fiz a funcao!")
    '''
    nl = int(input('Linhas: '))
    nc = int(input('Colunas: '))
    
    matriz = []
    for l in range(nl):
        linhas = []
        for c in range(nc):
            linhas.append(int(input('Elemento %d' %l+',%d: ' %c)))
        matriz.append(linhas)

    return matriz

#-----------------------------------------------------
# teste
a_mat = leia_matriz()
print(a_mat)
