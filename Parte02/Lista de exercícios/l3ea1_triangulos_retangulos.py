class Triangulo:
    def __init__(self, cateto1, cateto2, hipotenusa):
        self.lado1 = cateto1
        self.lado2 = cateto2
        self.lado3 = hipotenusa

    def retangulo(self):
        return self.lado1 ** 2 + self.lado2 ** 2 == self.lado3 ** 2
