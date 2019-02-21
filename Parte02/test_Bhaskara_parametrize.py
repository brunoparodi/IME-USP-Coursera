import Bhaskara_codigos_testaveis
import pytest

@pytest.mark.parametrize('entrada, esperado',[
    [(10,20,10),(1,-1)]
     ])

def testa_Bhaskara (entrada, esperado):
    assert Bhaskara_codigos_testaveis.Bhaskara.calcula_raizes(entrada) == esperado
