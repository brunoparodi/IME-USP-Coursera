import ordenador
import pytest
import ordenador_bolha
import conta_tempos

class TestaOrdenador:
    @pytest.fixture
    def o(self):
        return ordenador_bolha.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = conta_tempos.ContaTempos()        
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        c = conta_tempos.ContaTempos()        
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True
            

    def test_bolha_curta_aleatoria(self, o, l_aleatoria):
        o.bolha_melhor(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_selecao_direta(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_bolha_curta_aleatoria(self, o, l_quase):
        o.bolha_melhor(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)
