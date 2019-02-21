def acha(seq, x):
    ''' (list, float) -> int
        retorna a posicao em que x ocorre na lista, ou None caso contrario
        '''
    for i in seq:
        if i == x:
            return True
    return False


def main():
    ''' programa que le uma sequencia com N elementos e a imprime
        sem repeticoes.
        '''
    seq = [5,6,82,4138,984,897,17,67,4138,984,897]
    n1 = 0
    n2 = 1
    while n1 < len(seq):
        while n2 < (len(seq)):
            if seq[n1] == seq[n2]:
                del seq[n2]
            n2 += 1
        n1 += 1
        n2 = n1+1
    return seq



if __name__ == '__main__':
    print('tem que retornar True: ',acha([5,6,82,4138,984,897,17,67], 984))

    print(main())

