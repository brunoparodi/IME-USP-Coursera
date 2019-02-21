import random

class Buscador:
    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) -1
        self.contador = 0
        while primeiro <= ultimo:
            meio = (ultimo + primeiro) // 2 # // retorna numero inteiro da div
            if lista[meio] == x:
                self.contador += 1
                return meio
            if x < lista[meio]:
                ultimo = meio - 1
            if x > lista[meio]:
                primeiro = meio + 1
            self.contador += 1
        return -1

    def contador(self):
        self = self.contador + 1
        return self

    def __str__(self, posicao, tentativas):
        self.posicao = posicao
        self.tentativas = tentativas
        print('Posicao do número na lista: ',posicao)
        print('Tentativas de busca       : ',tentativas)

    def cria_lista(self, tamanho):
        lista = [random.randint(0, tamanho)]

        for x in range(tamanho):
            lista.append(random.randint(0, tamanho)) 
        return lista

    def numero_buscado(self, tamanho):
        return random.randint(0, tamanho)

    def ordena_lista(self, lista):
        for x in range(len(lista)):
            for y in range(x + 1, len(lista)):
                if lista[x] > lista[y]:
                    lista[x], lista[y] = lista[y], lista[x]
        return lista

    def exclui_repetidos(self, lista):
        x = 0
        while x < len(lista) - 1:
            if lista[x] == lista[x+1]:
                del lista[x]
                x -= 1
            x += 1
        return lista

if __name__ == '__main__':

    b = Buscador()
    t_list = 5000
    lista_crua = b.cria_lista(t_list)
##    print('lista crua =     ', lista_crua)
    lista_ord = b.ordena_lista(lista_crua)
##    print('lista ordenada = ', lista_ord)
    lista = b.exclui_repetidos(lista_ord)
##    print('lista limpa =    ', lista)    
    num = b.numero_buscado(t_list)
    print('num buscado =      ', num)
    
    print('posição na lista = ',(b.busca_binaria(lista, num)))
    print('número de buscas = ',b.contador)
    

    
    



                
    
