import math
a = int(input("informe a: "))
while a == 0:
    a = int(input("informe a diferente de 0: "))
b = int(input("informe b: "))
c = int(input("informe c: "))
delta = ((b ** 2) - (4 * a * c))
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    xp = ((- b + math.sqrt(delta)) / (2 * a))
    xn = ((- b - math.sqrt(delta)) / (2 * a))
if delta > 0:
    if xp < xn:
        print("as raízes da equação são",xp,"e",xn)
    else:
        print("as raízes da equação são",xn,"e",xp)
if delta == 0:
    print("a raiz desta equação é",xp)
