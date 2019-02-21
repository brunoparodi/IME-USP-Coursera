import math
ax = int(input('ponto ax: '))
ay = int(input('ponto ay: '))
bx = int(input('ponto bx: '))
by = int(input('ponto by: '))

d = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)

if d > 10:
    print('longe')
else:
    print('perto')
