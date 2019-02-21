#https://panda.ime.usp.br/aulasPython/static/aulasPython/aula07.html
#---------------------Exercício 7.0--------------------------------
def quantosprimos():
    n = int(input('Informe numeros maior que 1. Informe 0 para terminar: '))
    contador = 0
    while n != 0:
        if eprimo(n) == True:
            contador = contador + 1
        n = int(input('Informe numeros maior que 1. Informe 0 para terminar: '))
    print('A quantidade de primos é : %d' %contador) 
def eprimo(p):
    primo = True
    div = 2
    while div < p:
        if p % div == 0:
            primo = False
            return primo
        div = div + 1
    return primo
#----------------------Exercício 7.1-------------------------------
def multiplicidade():
    n = int(input('n = '))
    multiplicidade = 0
    fator = 2
    while n // fator != 0:
        while n % fator == 0:
            multiplicidade = multiplicidade + 1
            n = n // fator
        if multiplicidade != 0:
            print('fator', fator,'multiplicidade', multiplicidade)
        multiplicidade = 0
        fator = fator + 1    
#----------------------Exercício 7.2-------------------------------
def mdc():
    # leia o tamanho da sequencia
    n = int(input("Digite o tamanho da sequencia (>0): "))
    mdc_atual = int(input("Digite o 1o. numero: "))
    i = 1 # contador de numeros lidos
    while i < n:
        num = int(input("Digite o %do. numero: " %(i+1)))
        i = i + 1
        mdc_atual = calc_mdc(mdc_atual,num)
    print("O mdc eh", mdc_atual)
def calc_mdc(a,b):
    """Recebe dois inteiros positivos a e b e retorna
    o seu maximo divisor comum."""
    mdc = a;
    while a % mdc != 0 or b % mdc != 0:
        mdc = mdc - 1
    return mdc
#-----------------------Exercício 7.3------------------------------
def fatorial(f):
    n = f
    while n > 1:
        n = n - 1
        f = f * n
    return f
def soma_fatorial_sequencia():
    n = int(input('Informe uma sequencia de números. Informe 0 para terminar: '))
    soma = 0
    while n != 0:
        soma = fatorial(n) + soma
        n = int(input('Informe uma sequencia de números. Informe 0 para terminar: '))
    return soma
