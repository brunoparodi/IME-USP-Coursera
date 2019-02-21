class Triangulo():
    def __init__(self, cateto1, cateto2, hipotenusa):
        self.lado1 = cateto1
        self.lado2 = cateto2
        self.lado3 = hipotenusa



    def semelhantes(self, triangulo):
        return (
            self.lado1 / triangulo.lado1 ==
            self.lado2 / triangulo.lado2 ==
            self.lado3 / triangulo.lado3
            )
t1 = Triangulo(2, 2, 2)
t2 = Triangulo(4, 4, 4)
print(t1.semelhantes(t2))
