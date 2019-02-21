numero = int(input("Informe um número: "))
ultimo = numero % 10
primeiro = numero // 10

soma = 0
soma = soma + ultimo

while primeiro // 10 != 0:
    ultimo = primeiro % 10
    primeiro = primeiro // 10
    soma = soma + ultimo
soma = soma + primeiro


print('soma ',soma)
