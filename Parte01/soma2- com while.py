print("Digite uma sequeência de valores terminada por zero.")

soma = 0
valor = 1
while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores é: ",soma)
