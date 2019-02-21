'''
Matriz A = (a de ij) n x n -> Formação da matriz com n linhas e n colunas
Uma matriz simétrica é uma matriz quadrada de ordem n, que satisfaz: A^t = A
Outra forma para esta definição é fazendo as igualdades dos elementos da matriz.
Dizemos que uma matriz é simétrica quando, Aij = Aji para todo i,j
'''

#-----------------------------------------------------
def ler_elem():
    elem = int(input('Informe o elemento da matriz: '))
    return elem

def leia_matriz():
    n = int(input('Informe o tamanho da matriz quadrática: '))

    A = []

    for l in range(n):
        linha = []
        for c in range(n):
            print('linha ',l,'coluna ',c)
            linha.append(ler_elem())
        A.append(linha)
    return A

def imprima_matriz(matriz):
    print('Matriz:',len(matriz),'x',len(matriz[0]))
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            print('%6d' %matriz[i][c],end='')
        print()
    
def verifica_simetrica(matriz):
    '''
    Programa que le n e uma matriz de inteiros n x n
    e verifica se a matriz e simetrica.
    '''
    # escreva o seu programa abaixo e remova o print()
    #print("Vixe! Ainda nao fiz o exercicio!")
    #
    #          0     1     2     3
    #      +-----+-----+-----+-----+
    #   0  | 11  | -3  |  4  |  8  |
    #      +-----+-----+-----+-----+
    #   1  | -3  | 12  |  6  | 11  |
    #      +-----+-----+-----+-----+
    #   2  |  4  |  6  |  5  | 13  |
    #      +-----+-----+-----+-----+
    #   3  |  8  | 11  | 13  |  5  |
    #      +-----+-----+-----+-----+
    #-----------------------------------------------------
    l = c = condicao = 0
    while l < len(matriz):
        while c < len(matriz[0]):
            if matriz[l][c] == matriz[c][l]:
                condicao = condicao + 0
            else:
                return False
            c += 1
        c = 0
        l += 1
            
    if condicao == 0:
        print('Essa matriz é simétrica!!!')
    else:
        print('Essa matriz NÃÃÃÃÃÃO é simétrica =(')

def main():
    matriz = leia_matriz()
    imprima_matriz(matriz)
    verifica_simetrica(matriz)
    
    

def teste_verifica_simetrica():
    matriz = [11,-3,4,8],[-3,12,6,11],[4,6,5,13],[8,11,13,5]
    print(verifica_simetrica(matriz))


