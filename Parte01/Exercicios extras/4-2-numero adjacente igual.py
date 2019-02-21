n = int(input('informe um número: '))
ultimo = n % 10
primeiro = n // 10
fim = 0
if n < 10:
    print('não')
    fim = 10
    ultimo = 1000
elif primeiro == ultimo:
    print('sim')
    fim = 10
    
ultimo1 = primeiro % 10
if ultimo1 == ultimo:
    print('sim')
    fim = 10


while primeiro != 0:
    ultimo1 = primeiro % 10
    primeiro = primeiro // 10
    ultimo2 = primeiro % 10
    if ultimo1 == ultimo2:
        print('sim')
        fim = 10
    if fim == 10:
        primeiro = 0
if fim == 0:
    print('não')



