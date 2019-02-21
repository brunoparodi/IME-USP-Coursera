import random

class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            posicao_do_minimo = i # Inicialmente, o menor elemento já visto é o i-ésimo
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            # Coloca o menor elemento encontrado no início da sub-lista
            # Para isso, troca de lugar os elementos das posições i e posicao_do_minimo
            # a, b = b, a
            lista[i] , lista[posicao_do_minimo] = lista[posicao_do_minimo] , lista[i]
        return lista

    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1): #começa a busca pelo fim
            for j in range(i): #vai do começo até a posição i
                if lista[j] > lista[j+1]:
                    lista[j] , lista[j+1] = lista[j+1] , lista[j]
        return lista

    def bolha_melhor(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1): #começa a busca pelo fim
            trocou = False
            for j in range(i): #vai do começo até a posição i
                if lista[j] > lista[j+1]:
                    lista[j] , lista[j+1] = lista[j+1] , lista[j]
                    trocou = True
            if not trocou:
                return lista
        return lista

if __name__ == '__main__':
    o = Ordenador()
#    print(o.selecao_direta([5,1,7,3,2]))
#    print(o.bolha([5,1,7,3,2]))
    print(o.bolha_melhor([2, 3, 4, 5, 1]))
    
