n = 10000
c = 1
s = 1
while c < n:
    c += 1
    s = s + (1/c)
print(s)

n2 = n
c = n2
s = 0
while c > 0:
    s = 1/c + s
    c -= 1
print(s)

#resolvido: Direita para esquerda é mais preciso
n = 100
soma_ed = 0
soma_de  = 0

for i in range (1, n+1):
    soma_ed += 1/i
    soma_de += 1/(n+1-i)

print("Soma ED  :", soma_ed)
print("Soma DE  :", soma_de)
print("Diferenca:", soma_de - soma_ed)
