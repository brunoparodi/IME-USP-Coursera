def nome_curto(lista_de_nomes):
    lista_limpa = []
    for i in lista_de_nomes:
        lista_limpa.append(i.strip().capitalize())
    menor = lista_limpa[0]
    for i in lista_limpa:
        if len(i) < len(menor):
            menor = i
    return menor

def teste():
    lista_de_nomes = ['   ana     ','josé','Arquibaldo','Alouhis']
    if nome_curto(lista_de_nomes) == 'Ana':
        print('Está funcionando')
    else:
        print('Precisa corrigir algo')


def pagamento_semanal(valor_por_hora,num_horas = 40):
    assert valor_por_hora >= 0 and num_horas > 0
    return valor_por_hora * num_horas

def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s
######
print(horario_em_segundos (3,0,50))

print(horario_em_segundos(1,2,3))
