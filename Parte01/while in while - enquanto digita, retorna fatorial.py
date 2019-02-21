num = 5
while num >= 0:    
    num = int(input('Informe um numero maior que 0 para fatoriar: '))
    if num < 0:
        print('fim')
    else:
        fatorial = 1
        while num > 1:
            fatorial = fatorial * num
            num = num - 1
        print(fatorial)
