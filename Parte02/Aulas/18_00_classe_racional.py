class Racional:
    def __init__(self, n=0, d=1): #define valor padrão para Racional()
        self.num = n
        self.den = d
        print( '%d/%d' %(n,d))

    def add(self, n, d):
        return '%d/%d' % ((self.num + n),(self.den + d))

    def sub(self, n, d):
        return (self.num - n) / (self.den - d)

    def mult(self, n, d):
        return (self.num * n) / (self.den * d)

    def div(self, n, d):
        return (self.num / n) / (self.den / d)

    def __str__(self):
#        return str(self.numerador) + '/' + str(self.denominador)
        return '%d/%d' %(self.num, self.den)


def testes():
    r = Racional(2,3)
    print(r)
    print(r.add(2,3))
    
    a = Racional(2, 3)
    print(a)
    b = Racional(1, 4)
    print(b)

'''
class Racional:
    def __init__(self, a, b, n=0, d=1):
        self.num = n
        self.den = d
        print("Construtor: ", a, b, n, d)
        # observe que a e b não se tornam atributos de Racional

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

# testes
r1 = Racional('in', 'out')
r2 = Racional('a', 'b', 4)
r3 = Racional('x', 'y', d=5, n=3)
r3 = Racional('x', 'y', n=5, d=3)
r4 = Racional('x', 'y', 5, 3)'''

