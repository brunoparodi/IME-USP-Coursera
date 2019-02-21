import math
# 1 - Escreva uma função distancia que recebe dois Points como parâmetros
#e retorna a distância euclidiana entre eles.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x = ' + str(self.x) + ' y = ' + str(self.y)
# 2 - Crie um método reflect_x na classe Point que retorna um novo Point,
# que é a reflexão do ponto no eixo x. Ex:, Point(3, 5).reflect_x() é (3, -5)
    def reflext_x(self):
        return Point(self.x, (self.y)*-1)
# 3 - Crie um método slope_from_origin que retorna a inclinação da linha
# que liga o ponto à origem. Ex Point(4, 10).slope_from_origin() é 2.5
# Angulo X = cateto oposto / cateto adjacente
    def slope_from_origin(self):      
        return self.y / self.x

# A equação de uma reta é “y = ax + b”, (ou talvez “y = mx + c”).
# Os coeficientes a e b são suficientes para descrever a linha.
# Escreva um método na classe Point que recebe outra instância de Point e
# calcula a equação da reta que liga os dois pontos.
# O método deve retornar os dois coeficientes na forma de um tuple com
# dois valores. Por exemplo:
# print(Point(4, 11).get_line_to(Point(6, 15))) é (2, 3)
# y – y0 = m (x – x0) 
# m = yB - yA / xB – xA

    def get_line_to(self, Point):
        m = ( Point.y - self.y ) / (Point.x - self.x)
        a = self.y - Point.y
        c = self.x*Point.y - Point.x - self.y
        return a, c
        
        

def distancia(point1, point2):
    dist = math.sqrt( ((point1.x - point1.y) ** 2 ) + ((point1.y - point2.y) ** 2))
    return dist


p = Point(3,7)
q = Point(9,17)

print(Point(3,5).reflext_x())

print(distancia(p,q))

print(Point(4, 10).slope_from_origin())

print(Point(4, 11).get_line_to(Point(6, 15)))
