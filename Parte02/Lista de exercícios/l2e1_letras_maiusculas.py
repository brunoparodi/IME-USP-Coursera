def maiusculas(frase):
    frase_maiuscula = ''

    for letra in frase:
        if 65 <= ord(letra) <= 90:
            frase_maiuscula += letra
    return frase_maiuscula
    


def teste_maiusculas():
    if maiusculas('Programamos em python 2?') == 'P':
        print('Para a frase - Programamos em python 2? -, funcionou')
    # deve devolver 'P'
    else: print('Para a frase - Programamos em python 2? - não funcionou')

    if maiusculas('Programamos em Python 3.') == 'PP':
        print('Para a frase - Programamos em Python 3. -, funcionou')
    # deve devolver 'PP'
    else: print('Para a frase - Programamos em Python 3. - não funcionou')

    if maiusculas('PrOgRaMaMoS em python!') == 'PORMMS':
        print('Para a frase - PrOgRaMaMoS em python! -, funcionou')
    # deve devolver 'PORMMS'
    else: print('Para a frase - PrOgRaMaMoS em python! - não funcionou')
