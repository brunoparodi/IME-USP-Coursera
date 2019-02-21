
def cria_matriz(num_linhas,num_colunas):
    '''(int,int) -> matriz(lista de listas)
    Cria e retorna uma matriz com num_linhas e num_colunas
    colunas em que cada elemento é digitado pelo usuário'''
    matriz = []
    for i in range(num_linhas):
        linha=[]
        for j in range(num_colunas):
            valor = int(input('Digite o elemento ['+str(i)+']['+str(j)+']'))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input('Digite o número de linhas da matriz: '))
    col = int(input('Digite o número de colunas da matriz: '))
    return cria_matriz(lin,col)


def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i], end="  ")

mat = [[1,2,3],[4,5,6],[7,8,9]]
tarefa(mat)


def cria_matriz_invertida(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz


