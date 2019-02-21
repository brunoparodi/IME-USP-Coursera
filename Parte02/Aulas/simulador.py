'''
    Módulo Simulador
    Mantém o estado da simulação e os procedimentos para simular.
    Note que a classe Simulador 'esconde' o módulo random da função main.
    '''

import random
from balde import Balde

#constantes usadas em random
CAP_MIN = 10 #capacidade mínima do balde é 10
CAP_MAX = 51 #já ajustado ao random
VOL_MIN = 1  #sorteia no mínimo 1 para adicionar ao balde
VOL_MAX = 11 #já ajustado ao random. sorteia no máximo 11

class Simulador:
    def __init__(self, semente):
        random.seed(semente)
        capacidade = random.randrange(CAP_MIN, CAP_MAX)
        self.rec = Balde(capacidade)
        self.vol = 0
        self.avisou = False

    def sorteia(self):
        self.vol = random.randrange(VOL_MIN, VOL_MAX)
        print()
        print('Volume atual   : ', self.rec.vol)
        print('Volume sorteado: ', self.vol)
        return self.vol

    def deposita(self):
        ''' adiciona o último volume sorteado -self.vol- ao balde e
            retorna True se o balde estiver MEIO cheio e
            False caso contrário
        '''
        self.rec.deposita(self.vol)

        if self.rec.vol >= self.rec.cap / 2 and not self.avisou:
            self.avisou = True
            print('O volume do balde atingiu/passou a metade')

        return self.rec.cheio

    def finaliza(self):
        print('\nFim da simulação')
        print('Capacidade do balde: %d' % self.rec.cap)
        print('Volume final: %d' % self.rec.vol)

        if self.rec.der > 0:
            print('Balde está cheio e derramou água')
            print('Volume derramado foi: %d' % self.rec.der)
        else:
            if self.rec.cheio:
                print('Balde está cheio e não derramou água')
            elif self.rec.cap - self.rec.vol >= self.vol:
                print('Balde não está cheio')
                print('Havia espaço para encher o último sorteio: %d' % self.vol)
            else:
                print('Balde não está cheio')
                print('Não havia espaço para o último volume sorteado: %d' % self.vol)


if __name__ == '__main__':
    s = Simulador(123)
    v1 = s.sorteia()
    r1 = s.deposita()
    print(v1, r1)
    v2 = s.sorteia()
    r2 = s.deposita()
    print(v2, r2)
    s.finaliza()
    
