from balde import Balde
import random

#constantes usadas em random
CAP_MIN = 10 #capacidade mínima do balde é 10
CAP_MAX = 51 #já ajustado ao random
VOL_MIN = 1  #sorteia no mínimo 1 para adicionar ao balde
VOL_MAX = 11 #já ajustado ao random. sorteia no máximo 11

class Simulador2:
    def __main__(self, semente):
        random.seed(semente)
        capacidade = random.randrange(CAP_MIN, CAP_MAX)
        self.recipiente = Balde(capacidade)
        self.volume = 0
        self.transbordo = 0
        self.cheio = False

    def sorteia(self):
        self.volume = random.randrange(VOL_MIN, VOL_MAX)
        print('Volume atual: ', self.recipiente.volume)
        print('Foi adicionado: ',self.volume)
        return self.volume            

    def enche(self, volume):
        self.recipiente.enche(self.volume)

        if self.volume == self.capacidade:
            self.cheio = True
            print('o balde encheu e não transbordou')
        elif self.volume > self.capacidade:
            self.cheio = True
            print('o balde encheu e transbordou %d litros' %(self.volume - self.capacidade))
        else:
            print('ainda há espaço no balde')

    def fim(self):
        if self.cheio:
            return 'fim'
    
