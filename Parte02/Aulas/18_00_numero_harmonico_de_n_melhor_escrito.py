class Racional:
    def __init__(self, n=0, d=1):
        self.put (n, d)

    def __str__(self):
        return '%d/%d' %(self.num, self.den)

    def get(self):
        return self.num, self.den

    def put(self, n, d):
        self.num = n
        self.den = d

    def mul(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Racional(n, d)

    def div(self, other):
        return Racional(self.num * other.den, self.den * other.num)

    def add(self, other):
        if self.den != other.den:
            mmc = self.calcula_mmc(other)
            return '%d/%d' %((((mmc / self.den) * self.num) + ((mmc / other.den) * other.num)), mmc)
        else:
            return '%d/%d' %(self.num + other.num),self.den

    def sub(self, other):
        if self.den != other.den:
            mmc = self.calcula_mmc(other)
            return '%d/%d' %((((mmc / self.den) * self.num) - ((mmc / other.den) * other.num)), mmc)
        else:
            return '%d/%d' %(self.num - other.num),self.den

    def calcula_mmc(self, other):
        a = self.den
        b = other.den
        resto = None
        while resto is not 0:
            resto = a % b
            a  = b
            b  = resto
        mmc = (self.den * other.den) / a
        return mmc
    
        
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
    print('add den diferentes',r1,r2,r1.add(r2))

    r1 = Racional(10,4)
    r2 = Racional(12,5)
    print('sub den diferentes',r1,r2,r1.sub(r2))
    
