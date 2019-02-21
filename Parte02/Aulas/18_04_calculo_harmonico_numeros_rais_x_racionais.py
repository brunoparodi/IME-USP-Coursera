def mainED(n):
    # modifique o codigo para incluir o calculo de DE
    # e verifique se o resultado é diferente de ED usando
    # soma de reais e soma de racionais.

    
    soma_ed = 0
    soma_ed_rac = Racional()

    for i in range(1, n+1):
        soma_ed = soma_ed + 1/i
        soma_ed_rac = soma_ed_rac + Racional(1, i)

    print("Soma ED:          ", soma_ed)
    print("Soma ED racional: ", soma_ed_rac)
    print("                = ", soma_ed_rac.num/soma_ed_rac.den)
    print()

def mainDE(n):
    soma_de = 0
    soma_de_rac = Racional()
    i = 1
    for i in range(1, n):
        soma_de += 1/i
        soma_de_rac = soma_de_rac + Racional(1, i)
    print('Soma DE:          ',soma_de)
    print("Soma DE racional: ", soma_de_rac)
    print("                = ", soma_de_rac.num/soma_de_rac.den)
    print()

def mdc(a, b):
    ''' (int, int) -> int
        recebe dois inteiros diferentes de zero e retorna o maximo
        divisor comum entre a e b'''
    if b == 0: return a
    if a == 0: return b
    while a%b != 0:
        a, b = b, a%b
    return b

class Racional:
    def __init__(self, n=0, d=1):
        div = mdc(n, d)
        self.num = n//div
        self.den = d//div

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

    def __add__(self, other):
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return Racional(n, d)

    # escreva aqui o seu codigo para os metodos
    # __truediv__
    # __mul__
    # __sub__
    # e ao menos um teste para cada metodo

    def __truediv__(self, other):
        n = self.num * other.den
        d = self.den * other.num
        return Racional(n, d)

    def __mul__(self, other):
        return Racional(self.num * other.num, self.den * other.den)
        
    def __sub__(self, other):
        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        return Racional(n, d)

def testa_racional():
    print('testando mul:')
    r1 = Racional(2)
    r2 = Racional(1,5)
    print(r1.mul(r2))
    print(r1.div(r2))

    r1 = Racional(2)
    r2 = Racional(1,5)
    print(r1, '*', r2, '=>', r1.mul(r2))
    #teste do div:
    print(r1, '/', r2, '=>', r1.div(r2))

def testa_mmc():
    r1 = Racional(10,4)
    r2 = Racional(12,5)
    print('add den diferentes',r1,r2,r1 + r2)

    r1 = Racional(10,4)
    r2 = Racional(12,5)
    print('sub den diferentes',r1,r2,r1 - r2)
    
def testa_operações():
    r1 = Racional(2,3)
    r2 = Racional(1,4)
    r3 = Racional(3,5)
    r4 = r1 + r2 * r3
    print(str(r4)
          + ' é igual a '
          + str(r1)
          + ' + '
          + str(r2)
          + ' * '
          + str(r3)
          )

    
    r5 = Racional(10,5)
    r6 = Racional(2,8)
    r7 = r5 / r6
    print('Testando divisão de ',r5,' e ',r6, ' = ', r7)


    r8 = Racional(20,5)
    r9 = Racional(12,7)
    r10 = Racional(1,2)
    print(r8,' * ',r9,' * ',r10,' = ',r8*r9*r10)

#mainED(50)
#mainDE(50)
testa_operações()

