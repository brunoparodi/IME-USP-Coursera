n = int(input("informe um numero: "))
comeco = n // 10
resto = n % 10
soma = 0
soma = resto + soma
while comeco > 0 :
    
    resto = comeco % 10
    soma = resto + soma
    comeco = comeco // 10

print(soma)
