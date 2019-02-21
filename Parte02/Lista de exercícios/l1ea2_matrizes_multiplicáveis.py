def sao_multiplicaveis(m1,m2):
    return len(m1[0]) == len(m2)

def t():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    print(sao_multiplicaveis(m1, m2))
    print('Esperado False')
    
    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    print(sao_multiplicaveis(m1, m2))
    print('Esperado True')
