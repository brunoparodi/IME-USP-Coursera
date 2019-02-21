import Bhaskara_codigos_testaveis
import pytest

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara_codigos_testaveis.Bhaskara()
    
    def testa_uma_raiz(self, b):
#       b = Bhaskara_codigos_testaveis.Bhaskara()
        assert b.calcula_raizes(1, 0, 0) == (1, 0)

    def testa_duas_raizes(self, b):
#       b = Bhaskara_codigos_testaveis.Bhaskara()
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)

    def testa_zero_raizes(self, b):
#       b = Bhaskara_codigos_testaveis.Bhaskara()
        assert b.calcula_raizes(10, 10, 10) == (0)

    def testa_raiz_negativa(self, b):
#       b = Bhaskara_codigos_testaveis.Bhaskara()
        assert b.calcula_raizes(10, 20, 10) == (1 ,-1)
