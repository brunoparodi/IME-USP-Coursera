def remove_repetidos():
    tseq = int(input('informe o tamanho da sequencia: '))
    x = 0
    lista = []
    while x < tseq:
        x += 1
        y = int(input('Informe o numero %d da sequencia: ' %x))
        lista.append(y)        
    print('Sequência original: ',lista)
    ordenada = sorted(lista[:])
    print('Sequência ordenada: ',ordenada)
    e = 0
    for i in ordenada:       
        if ordenada[e] == ordenada[e+1]:
            del ordenada[e]
            e = -1
        e += 1
    print('Sequência limpa: ', ordenada)
        

remove_repetidos()
