class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return  self.a + self.b + self.c




import pytest

@pytest.mark.parametrize('entrada, saida',[
    ((1,1,1),3),
    ((10,20,10),40)
    ])

def testa_triangulo(entrada, saida):
    
    assert Triangulo.perimetro(entrada) == saida
