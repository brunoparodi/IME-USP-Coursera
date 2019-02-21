# A = (aij)m x p  e B = (bij)p x n é a matriz C = (cij) m x n
def multiplica_matriz(A,B):
    colunas_a = len(A[0])
    linhas_b = len(B)
    if colunas_a != linhas_b:
        print('Essa multiplicação não é válida.\n'
              'O número de colunas da 1ª matriz é '+str(colunas_a)+'.\n'
              'O número de linhas da 2ª matriz é '+str(linhas_b)+'.\n'
              'Porém, precisam ser iguais. Informe outras matrizes.')
        return
    C = cria_c(A,B)
    X = cria_c(A,B)
    for l in range(len(X)):
        for c in range(len(X[0])):
            C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
            C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
            C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
            C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]

def cria_c(A,B):
    C = []
    for l in A[0]:
        linha= []
        for c in B:
            linha.append(0)
        C.append(linha)
    return C       

def teste():
    a = [ [1, 2, -1], [0, 3, 2] ]
    b = [ [1, -1], [2, 0], [3, 2] ]
    c = multiplica_matriz(a,b)
    return c
    resultado = [ [2, -3], [12, 4] ]
    if c == resultado:
        print("Passou no primeiro teste! :-)")
    else:
        print("Nao passou no primeiro teste! :-(")

#multiplica_matriz([[2,3],[0,1], [-1,4] ],[ [1,2,3], [-2,0,4] ])
#multiplica_matriz([[1,2], [3,4] ],[ [-1,3], [4,2] ])
