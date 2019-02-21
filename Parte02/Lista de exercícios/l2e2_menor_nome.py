def menor_nome(nomes):
    nomes_limpos = []
    for nome in nomes:
        nomes_limpos.append(nome.strip())   
    menor = nomes_limpos[0]

    for nome in nomes_limpos:
        if len(nome) < len(menor):
            menor = nome
    return menor.capitalize()


def teste_menor_nomes():
    menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
    # deve devolver 'José'

    menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
    # deve devolver 'José'

    menor_nome([' Bárbara', 'JOSÉ  ', 'Bill'])
    # deve devolver José
