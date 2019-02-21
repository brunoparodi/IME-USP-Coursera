import ordenador_bolha
import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(5000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -100
        lista[n//5] = -200
        lista[n//8] = -300
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        lista11 = self.lista_quase_ordenada(n)
        lista12 = lista11[:]
        lista13 = lista11[:]

        o = ordenador_bolha.Ordenador()

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Selecao_direta demorou ',depois-antes, ' segundos')

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print('Bolha demorou          ',depois-antes, ' segundos')

        antes = time.time()
        o.bolha_melhor(lista3)
        depois = time.time()
        print('Bolha_melhor demorou   ',depois-antes, ' segundos')

        antes = time.time()
        o.selecao_direta(lista12)
        depois = time.time()
        print('Selecao_direta qo demorou ',depois-antes, ' segundos')

        antes = time.time()
        o.bolha(lista11)
        depois = time.time()
        print('Bolha demorou qo          ',depois-antes, ' segundos')

        antes = time.time()
        o.bolha_melhor(lista13)
        depois = time.time()
        print('Bolha_melhor qo demorou   ',depois-antes, ' segundos')



if __name__ == '__main__':
    c = ContaTempos()
    c.compara(5000)
