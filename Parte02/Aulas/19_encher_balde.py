import random

# definicao de constantes
CAP_MIN = 10
CAP_MAX = 51 # ja ajustado ao random
VOL_MIN = 1
VOL_MAX = 11 # ja ajustado ao random

def teste_seed():  # funcao para teste do simulador
    sim = Simulador(123)
    sort = sim.sorteia()

def main():
    semente = int(input("Digite a semente para gerar numeros pseudo-aleatorios: "))
    jogo    = Simulador(semente)

    fim = False
    while not fim:
        jogo.sorteia()
        opcao = input("Deseja utilizar o volume sorteado? (s/n): ")
        if opcao == 's':
            fim = jogo.deposita()  # retorna True caso o balde fique cheio
        else:
            fim = True
    jogo.finaliza()

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
        print("Volume atual   : ", self.rec.vol)
        print("Volume sorteado: ", self.vol)

    def deposita(self):
        ''' adiciona o ultimo volume sorteado self.vol
            ao balde e retorna True se o
            balde estiver cheio e False caso contrario.
            '''
        self.rec.deposita(self.vol)
        
        if self.rec.vol >= self.rec.cap/2 and not self.avisou:
            self.avisou = True
            print("O volume do balde atingiu/passou a metade.")

        return self.rec.cheio
    
    def finaliza(self):
        print("\nFim da simulacao")
        print("Capacidade do balde: %d" % self.rec.cap)
        print("Volume final: %d" % self.rec.vol)

        if self.rec.der > 0:
            print("Balde esta cheio e houve derramamento de agua")
            print("Volume derramado foi: %d" %(self.rec.der))
        else:
            if self.rec.cheio:
                print("Balde esta cheio e nao houve derramamento de agua")
            elif self.rec.cap - self.rec.vol >= self.vol:
                print("Balde nao esta cheio.")
                print("Havia espaco para o ultimo volume sorteado: %d" % self.vol)
            else:
                print("Balde nao esta cheio.")
                print("Nao havia espaco para o ultimo volume sorteado: %d" % self.vol)


class Balde:
    def __init__(self, cap):
        self.cap = cap
        self.vol = 0
        self.der = 0
        self.cheio = False

    def __str__(self):
        return 'volume de água atual: %d' %self.vol

    def deposita(self, vol):
        self.vol += vol
        if self.vol >= self.cap:
            self.cheio = True
            self.der = self.vol - self.cap
            self.vol = self.cap
            pass
        return 'colocado %d de água' % vol

##    def cheio(self):
##        if self.volume >= self.capacidade:
##            return True

##    def derramado(self):
##        if self.volume > self.capacidade:
##            self.derramado = self.volume - self.capacidade
##            return self.derramado
##        else: return self.derramado

main()

