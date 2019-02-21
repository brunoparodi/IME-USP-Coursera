def remove_repetidos(lista):
    ordem = sorted(lista[:])
    x = 0
    while x < len(ordem)-1:
        if ordem[x] == ordem[x + 1]:
            del ordem[x]
            x = -1           
        x = x + 1      
    return ordem
    
