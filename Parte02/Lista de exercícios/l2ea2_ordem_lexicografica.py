def primeiro_lex(lista):
    palavra = '~~~~~~~~~~~~~~~~~~~~~~~~'
    for p in lista:
        if p < palavra:
            palavra = p
    return palavra

def testa_primeiro_lex():
    print(
    primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A',
    # deve devolver 'A'

    primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA'
    # deve devolver 'AAAAAA'
    )
