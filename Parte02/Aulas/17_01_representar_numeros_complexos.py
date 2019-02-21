# CÓDIGO RUIM

class Complexo:
    def __init__(self, num):
        self.numero = num

    def soma(self, somado):
        return self + somado

    def multiplica(self, multiplicado):
        return self * multiplicado

    def __str__(self, numero):
        return str(self) + ' + ' + str(numero) + 'j'

    
def testes():
    cpx1 = Complexo(2,3)
    print(cpx1)
