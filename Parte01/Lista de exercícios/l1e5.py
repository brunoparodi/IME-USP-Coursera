numero = int(input('Digite um número inteiro: '))
mi = numero // 1000
cen = numero //100
dez = numero // 10

cen1 = dez - cen*10


print('O dígito das dezenas é',cen1)
