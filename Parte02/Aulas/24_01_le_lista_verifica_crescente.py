def main():
    seq1 = [2, 4, 5, 8, 9, 11, 17, 21]
    print(seq1)
    if crescente(seq1):
        print("eh crescente")
    else:
        print("nao eh crescente")

    seq2 = [2, 4, 5, 8, 9, 11, 17, 1, 21]
    print(seq2)
    if crescente(seq2):
        print("eh crescente")
    else:
        print("nao eh crescente")

def crescente(seq):
    ''' (list) -> bool
        retorna True se seq esta em ordem crescente
        e False caso contrario
        '''
    for i in range(len(seq)):
        posicao = i
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                return False
    return True

        
    

main()
