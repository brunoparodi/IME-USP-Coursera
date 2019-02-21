import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return 'x = ' + str(self.x) + ' y = ' + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

p = Point(3,4)         # Instantiate an object of type Point
q = Point(5,12)         # and make a second point
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY())


def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()
    dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
    return dist

print(p)
#print(p.getX(),p.getY())
#print(p.distanceFromOrigin())
#print(distance(p,q))
