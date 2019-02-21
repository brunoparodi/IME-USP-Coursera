def primos( n ):
    if n < 2:  return []
    if n == 2: return [2]
    nums = range(3, n+1, 2)
    nums_length = (n // 2) - 1 + (n % 2)
    idx = 0
    idx_sqrtn = (int(n**0.5) - 3) // 2
    while idx <= idx_sqrtn:
        nums_at_idx = (idx << 1) + 3
        for j in range( idx * (nums_at_idx + 3) + 3, nums_length, nums_at_idx ):
            nums[j] = 0
        idx += 1
        while idx <= idx_sqrtn:
            if nums[idx] != 0:
                break
            idx += 1
    return [2] + [x for x in nums if x != 0]

def meu_primos(limite):
    lista_de_primos = primos(limite)
    print ('Primos: ',' '.join(str(x) for x in lista_de_primos))
    print ('\n\nForam encontrados %d números primos.' % len(lista_de_primos))

from math import sqrt
print ('Primos: 2')
limite = int(input('informe um numero para verificar se é primo: '))
c, p, primos, = 1, 1, [2,]
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
print(a)

print ("\n\nForam encontrados %d números primos." %p)
print ("Foram necessárias %d comparações." %c)
