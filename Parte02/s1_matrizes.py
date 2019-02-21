A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
A

def cria_matriz(num_linhas,num_colunas,valor):
    matriz = []
    for i in range(num_linhas):
        linha=[]
        for c in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz

def crie_matriz(n_linhas, n_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)	
    Cria e retorna uma matriz com n_linhas linha e n_colunas
    colunas em que cada elemento é igual ao valor dado.
    '''
    matriz = [] # lista vazia
    for i in range(n_linhas):
       # cria a linha i
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha.append(valor)

        # coloque linha na matriz
        matriz.append(linha)

    return matriz


def teste_crie_matriz():
    A = crie_matriz(5,5,0)
    A[1][1] = 2
    print(A)

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

def teste_leia_matriz():
    a_mat = leia_matriz()
    print(a_mat)
