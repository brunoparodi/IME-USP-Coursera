def fatorial(x):
    if x <= 1:
        return 1
    if x < 2:
        return x
    else:
        return fatorial(x-1) * x

def teste():
    a = fatorial(0)
    b = fatorial(1)
    c = fatorial(2)
    d = fatorial(4)

    print(a, b , c, d)
