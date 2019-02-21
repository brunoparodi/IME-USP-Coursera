from math import sqrt

def maior_primo(x):
    c, p, primos, limite = 1, 1, [2,], x
    for numero in range(3,limite+1,2): #pula de dois em dois
        ehprimo = 1
        for i in primos:
            c += 1 # mudei de lugar
            if numero % i == 0:
                ehprimo = 0
                break
            if i > sqrt(numero):
                break
        if (ehprimo):
            primos.append(numero)
            p += 1
            a = numero
    return(a)
