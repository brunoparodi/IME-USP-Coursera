import random

class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # Coloca o menor elemento encontrado no início da sub-lista
            # Para isso, troca de lugar os elementos das posições i e posicao_do_minimo
            # a, b = b, a
            lista[i] , lista[posicao_do_minimo] = lista[posicao_do_minimo] , lista[i]

if __name__ == '__main__':
##    aleatorio = random.seed(17)
##    print(aleatorio)
##    lista = [10, 3, 8, -10, 200, 17, 32]
##    print(lista)
##    o = Ordenador()
##    print(o)
##    o.selecao_direta(lista)
##    print(lista)
    lista = []
    inicio = 1
    fim = 100
    tamanho = int(input('informe o tamanho da lista:  '))
    
    for i in range(tamanho):
        aleatorio2 = random.randint(inicio, fim)
        lista.append(aleatorio2)
    print('lista desordenada:  ', lista)
    o = Ordenador()
    o.selecao_direta(lista)
    print()
    print()
    print('lista ordenada:  ', lista)

    
    
    seq = lista
    def busca_sequencial(seq, x):
        for i in range(len(seq)):
            print(i)
            if seq[i] == x:
                return True
        return False
    print(busca_sequencial(seq, x))
