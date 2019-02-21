def soma_matrizes(m1,m2):
    linhas = len(m1)
    colunas = len(m2[0])
    soma = []
    
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(m1[l][c]+m2[l][c])
        soma.append(linha)
        print(linha)

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[10,20,30],[40,50,60],[70,80,90]]
    print(soma_matrizes(A,B))
