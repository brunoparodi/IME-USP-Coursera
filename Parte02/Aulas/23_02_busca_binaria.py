def busca_binaria(seq, x):
    ''' (list, float) -> bool
        retorna a posicao em que x ocorre na lista ordenada,
        ou None caso contrario, usando o algoritmo de busca binaria.
        '''
    t = len(seq)
    m = int(t / 2)
    
    if seq[m] == x:
        return True

    if seq[m] > x:
        for i in range(0, m-1):
            if seq[i] == x:
                return True
    if seq[m] < x:
        for i in range(m + 1, len(seq)):
            if seq[i] == x:
                return True

    return None


# escreva alguns testes da funcao busca_binaria
seq = [4, 10, 80, 90, 91, 99, 100, 101]
testes = [80, 50,101]

for t in testes:
    pos = busca_binaria(seq, t)
    if pos is None:
        print("Nao achei ", t)
    else:
        print("Achei ", t)

