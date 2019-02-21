def main():
           
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato 2')    

def rodada():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    restante = 0
    computador_escolhe_jogada(n,m,restante)

def computador_escolhe_jogada(n,m, restante):
    comeco = m + 1
    if n % comeco == 0 and restante == 0:
        print('Você começa')
        restante = n
        usuario_escolhe_jogada(n,m, restante)
    else:
        if n == m: #caso n e m sejam iguais, computador começa tirando tudo
            print('Computador começa')
            pc_tira = n
            print('O computador tirou ',pc_tira,'peça') 
            restante = n - m            
        elif restante == 0: #computador começa com o pulo do gato
            print('Computador começa')
            pc_tira = n // (m + 1)
            print('O computador tirou ',pc_tira,'peça') 
            restante = n - pc_tira
        elif restante % m == 0:
            pc_tira = restante
            print('O computador tirou ',pc_tira,'peça')
            restante = restante - pc_tira
        else:
            pc_tira = n // restante
            print('O computador tirou ',pc_tira,'peça') 
            restante = restante - pc_tira
        if restante == 0:
            print('Fim de jogo! O computador ganhou')
        else:
            print('Agora resta apenas ',restante,'peça no tabuleiro')
            usuario_escolhe_jogada(n,m,restante)

    
def usuario_escolhe_jogada(n,m,restante):
    tirar = int(input('Quantas peças você vai tirar? '))
    while tirar > m:
        print('Oops! Jogada inválida! Tente de novo.')
        tirar = int(input('Quantas peças você vai tirar? '))
    print('Você tirou ',tirar,'peças.')
    restante = restante - tirar
    print('Agora resta apenas ',restante,'peça no tabuleiro')
    if restante == 0:
        print('Você ganhou, o codigo está errado!!!!')
        main ()
    if restante == 1:
        print('O computador tirou uma peça.')
        print('Fim de jogo! O computador ganhou')
    else:
        computador_escolhe_jogada(n,m,restante)
    
