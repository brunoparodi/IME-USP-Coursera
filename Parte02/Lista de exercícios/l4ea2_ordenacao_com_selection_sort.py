def ordena(lista):
    tamanho = len(lista)

    for i in range(tamanho):
        posicao_do_minimo = i

        for j in range(i + 1, tamanho):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j

        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo] , lista[i]

    return lista

if __name__ == '__main__':
    print(ordena([14867, 52561, 10532, 22679, 76877, 2641, 46727, 3158, 61259, 67356]))
