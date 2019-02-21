# A = (aij)m x p  e B = (bij)p x n é a matriz C = (cij) m x n
def mat_mul(A,B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B

    C = []

    for linha in range(num_linhas_A):
        C.append([]) # Começando uma nova linha em C
        for coluna in range(num_colunas_B):
            # Adicionando uma nova coluna na linha
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C
                

if __name__ == '__main__':
    A = [ [1, 2, -1], [0, 3, 2] ]
    B = [ [1, -1], [2, 0], [3, 2] ]
    c = mat_mul(A,B)
    print(c)
    resultado = [ [2, -3], [12, 4] ]
    if c == resultado:
        print("Passou no primeiro teste! :-)")
    else:
        print("Nao passou no primeiro teste! :-(")

#multiplica_matriz([[2,3],[0,1], [-1,4] ],[ [1,2,3], [-2,0,4] ])
#multiplica_matriz([[1,2], [3,4] ],[ [-1,3], [4,2] ])
