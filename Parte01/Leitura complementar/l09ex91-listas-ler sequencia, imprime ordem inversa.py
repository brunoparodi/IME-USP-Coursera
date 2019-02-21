tam = int(input('informe o tamanho da sequencia: '))
t = 1
lista = []
while t <= tam:
    el = input('informe o %dº elemento: ' %t)
    lista.append(el)
    t += 1
    

x = -1
avesso = []
for i in lista:
    avesso.append(lista[x])
    x -= 1
print(avesso)

def main():
    """
    (exercicio 1 da lista de exercicios sobre vetores).
    Dados n > 0 e uma sequencia com n numeros reais,
    imprimi-los na ordem inversa a da leitura.

    Solucao: Criar uma lista vazia e usar append.

    """

    print ("Le n inteiros e imprime-os em ordem reversa")
    n = int(input("Digite n: "))
    cont = 0
    seq = []  # cria uma lista vazia

    while cont < n:
        num = int(input("Digite um numero da sequencia: "))
        seq.append(num)   # coloca num no final da lista
        cont += 1

    print("Sequencia original: ", seq)


    print("Solucao 1: usando indices decrescentes")
    cont = n-1
    while cont >= 0:
        print (seq[cont], end=' ')
        cont -= 1
    print ()

    # ou ainda, usando indices negativos
    print("Solucao 2: usando indices negativos")
    cont = -1
    while cont >= -n:
        print (seq[cont], end=' ')
        cont -= 1
    print()
