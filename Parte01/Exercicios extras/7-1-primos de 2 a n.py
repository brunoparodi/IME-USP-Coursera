
def éPrimo(p):
    divisor = 2
    while divisor <= (p / 2):
        if p % divisor == 0:
            éPrimo = 0
            return éPrimo
        divisor = divisor + 1
    éPrimo = 1
    return éPrimo

def n_primos(n):
    x = 2
    contador = 0
    while x <= n:        
        contador = contador + éPrimo(x)
        x = x + 1
    return contador
