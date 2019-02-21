
def le_matriz():
    m = int(input('Informe o número de LINHAS da matriz: '))
    n = int(input('Informe o número de COLUNAS da matriz: '))
    A = []
    for l in range(m):
        linha = []
        for c in range(n):
            elemento = int(input('Informe elemento '+str(l)+'x'+str(c)+': '))
            linha.append(elemento)
        A.append(linha)
    return A

def imprime_matriz(matriz):
    
    print('Matriz ficou assim:')
    for l in range(len(matriz)):
        print(matriz[l])
    
def verifica_nulidade(matriz):

    item = int(input('Informe o número para verificar. 0 para nulidade: '))
    linhas_nulas = 0
    colunas_nulas = 0
    cont_m = 0
    cont_n = 0

    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[l][c] == item:
                cont_n = cont_n + 1
            if cont_n == len(matriz[0]):
                linhas_nulas = linhas_nulas + 1
        cont_n = 0

    for c in range(len(matriz[0])):
        for l in range(len(matriz)):
            if matriz[l][c] == item:
                cont_m = cont_m + 1
            if cont_m == len(matriz):
                colunas_nulas += 1
        cont_m = 0
    print ('Linhas nulas: ',linhas_nulas)
    print ('Colunas nulas: ',colunas_nulas)

def main():
    matriz = le_matriz()
    imprime_matriz(matriz)
    verifica_nulidade(matriz)

def teste():
    matriz = [[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0]]
    imprime_matriz(matriz)
    verifica_nulidade(matriz)
    
