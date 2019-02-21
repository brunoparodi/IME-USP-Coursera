def main():           
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    tipo_de_jogo = int(input())
    while 1 < tipo_de_jogo > 2:
        main()
    if tipo_de_jogo == 1:
        partida()
    if tipo_de_jogo == 2:
        campeonato()

def campeonato():
        partida()
        partida()
        partida()
        print('Placar: Você 0 X 3 Computador')

def fim():
    print('Fim de jogo! O computador ganhou\n')

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if n < m:
        pc_tira = n
        print('O computador tirou ' ,pc_tira,'peça')
        fim()
    
    elif   n % (m + 1) == 0:        
        print('Você começa')
        while n > 0:
            n = n - usuario_escolhe_jogada(n, m)
            print('sobrou ',n,'peças no tabuleiro')
            if n == 0:
                return fim()
                            
            n = n - computador_escolhe_jogada(n, m)
            print('sobrou ',n,'peças no tabuleiro')
            if n == 0:
                return fim()               
    else:       
        print('Computador começa')
        while n > 0:
            n = n - computador_escolhe_jogada(n, m)
            print('sobrou ',n,'peças no tabuleiro')
            if n == 0:
                return fim()
                
            n = n - usuario_escolhe_jogada(n, m)
            print('sobrou ',n,'peças no tabuleiro')
            if n == 0:
                return fim()
              
def computador_escolhe_jogada(n,m):
    pc_tira = n % (m + 1)
    if pc_tira == 0:
        pc_tira = m
    print('O computador tirou ',pc_tira,'peça')
    return pc_tira
    
def usuario_escolhe_jogada(n,m):
    user_tira = int(input('Quantas peças você vai tirar? '))
    while n <= m and user_tira > n:
        print('Oops! Jogada inválida! Tente de novo.')
        user_tira = int(input('Quantas peças você vai tirar? '))
    while user_tira > m or user_tira <= 0:
        print('Oops! Jogada inválida! Tente de novo.')
        user_tira = int(input('Quantas peças você vai tirar? '))
    print('Você tirou ',user_tira,'peças.')
    return user_tira

main()
