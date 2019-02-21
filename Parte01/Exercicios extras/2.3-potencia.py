n = int(input("digite n: "))
k = int(input("digite k: "))
while k < 0:
    print("informe k maior ou igual a 0")
    k = int(input("digite k: "))
conta = n ** k
print(conta)
