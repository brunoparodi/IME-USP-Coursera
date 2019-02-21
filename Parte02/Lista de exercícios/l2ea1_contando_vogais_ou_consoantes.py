def conta_letras(frase,contar='vogais'):
    quantidade = 0
    vogais = 'AEIOUaeiou'

    if contar == 'vogais':
        for palavra in frase:
            for letra in palavra:
                if letra in vogais:
                    quantidade +=1
        return quantidade

    if contar == 'consoantes':
        for palavra in frase:
            for letra in palavra:
                if not letra in vogais and not letra in ' ':
                    quantidade +=1
        return quantidade

def testa_conta_letras():
    print(conta_letras('programamos em python') == 6,
    # deve devolver 6
    conta_letras('programamos em python', 'vogais') == 6,
    # deve devolver 6
    conta_letras('programamos em python', 'consoantes') == 13)
    # deve devolver 13
