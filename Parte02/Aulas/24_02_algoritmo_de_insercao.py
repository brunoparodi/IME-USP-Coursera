def insercao(seq):
    
    
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[j] <= seq[i]:
                seq[j] , seq[i] = seq[i] , seq[j]
                

    return seq
        
    
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

def main():
##    seq1 = [54, 2, 11, 4, 17, 7, 21, 1]
##    print(seq1)
##    insercao(seq1)
##    print(seq1)
##    if not crescente(seq1):
##        print("nao ", end='')
##    print("eh crescente")

    seq2 = [23, 42, 4, 16, 8, 15]
    print(insercao(seq2))
main()
